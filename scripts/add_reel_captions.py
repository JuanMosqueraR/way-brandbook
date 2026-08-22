"""
add_reel_captions.py — Superpone texto en pantalla (tipografía de marca WAY,
Bodoni Moda itálica sobre velo degradado cálido) a un clip de Reel ya aprobado
en contenido, y exporta a 1080x1920 sin tocar la imagen ni el audio original.

Estilo replicado de brandbook.html, sección 10 (.ig-mini-tile--promo):
Bodoni Moda itálica 400, marfil #F7F3EE, velo direccional cálido
rgba(20,14,10,.65) -> transparente.

Uso (ejemplo, ver el bloque __main__ para el caso de Opción 3):

    python scripts/add_reel_captions.py \
        --video assets/videos/3/1.mp4 \
        --output assets/videos/3/1-final.mp4 \
        --captions captions_opcion3.json

Donde captions_opcion3.json es una lista de objetos:
    [{"text": "...", "start": 0.3, "duration": 2.6}, ...]

Si no se pasa --captions, corre con la config por default embebida al final
del archivo (Opción 3, "Detrás de cámara").

Requisitos: pip install moviepy imageio-ffmpeg pillow numpy
Las fuentes Bodoni Moda y los PNG de emoji (Twemoji) se descargan una sola
vez a una carpeta cache fuera del repo (no se commitean, mismo criterio que
el resto del pipeline de wordmark del proyecto — ver CLAUDE.md).
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
import urllib.request
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------------------
# Paleta y tipografía de marca (brandbook.html :root + sección 07/10)
# ---------------------------------------------------------------------------
COLOR_MARFIL = (247, 243, 238, 255)
COLOR_NEGRO = (42, 31, 24, 255)
SCRIM_RGB = (20, 14, 10)  # rgba(20,14,10,.65) del brandbook, sección 10

FONT_SIZE = 66
LINE_SPACING = 1.25
MAX_TEXT_WIDTH_RATIO = 0.82  # margen ~9% de cada lado del canvas
SAFE_TOP = 250   # zona segura Reels: evitar UI superior de Instagram
SAFE_BOTTOM = 260  # evitar caption/UI inferior de Instagram
TEXT_CENTER_Y_RATIO = 0.62  # posición vertical del bloque de texto (bajo el rostro)

# Estilo "subtitle" — tratamiento discreto para líneas que subtitulan diálogo
# real (a diferencia de las líneas de texto no-diegético tipo tarjeta), inspirado
# en .tiktok-video .play del brandbook: texto + sombra suave, sin velo, más
# chico y más abajo, para que se lea como transcripción y no como declaración
# de marca — no debe competir con la cara de la persona hablando.
SUBTITLE_FONT_SIZE = 42
SUBTITLE_CENTER_Y_RATIO = 0.83
SUBTITLE_SHADOW_OFFSET = (0, 3)
SUBTITLE_SHADOW_BLUR = 3
SUBTITLE_SHADOW_ALPHA = 150  # ~rgba(0,0,0,.6) del brandbook

FADE_DURATION = 0.4  # segundos, fade in/out de cada texto

CACHE_DIR = Path(tempfile.gettempdir()) / "way-brandbook-assets"
FONTS_DIR = CACHE_DIR / "fonts"
EMOJI_DIR = CACHE_DIR / "emoji"

FONT_URLS = {
    "regular": "https://raw.githubusercontent.com/google/fonts/main/ofl/bodonimoda/BodoniModa%5Bopsz%2Cwght%5D.ttf",
    "italic": "https://raw.githubusercontent.com/google/fonts/main/ofl/bodonimoda/BodoniModa-Italic%5Bopsz%2Cwght%5D.ttf",
}

# Rango amplio de codepoints emoji (suficiente para los emoji de marca
# actuales: 👀 💛 ✨ — y para futuras líneas de otras opciones de Reel).
EMOJI_PATTERN = re.compile(
    "["
    "\U0001F300-\U0001FAFF"
    "\U00002600-\U000027BF"
    "\U0001F1E6-\U0001F1FF"
    "\U00002190-\U000021FF"
    "]+",
    flags=re.UNICODE,
)


@dataclass
class Caption:
    text: str
    start: float
    duration: float
    style: str = "veil"  # "veil" (tarjeta de marca, default) | "subtitle" (discreto, ver arriba)


# ---------------------------------------------------------------------------
# Assets (fuentes + emoji) — se descargan una sola vez a un cache fuera del repo
# ---------------------------------------------------------------------------

def ensure_fonts() -> dict[str, Path]:
    FONTS_DIR.mkdir(parents=True, exist_ok=True)
    paths = {}
    for name, url in FONT_URLS.items():
        dest = FONTS_DIR / f"BodoniModa-{name}.ttf"
        if not dest.exists():
            print(f"Descargando fuente {name}...", file=sys.stderr)
            urllib.request.urlretrieve(url, dest)
        paths[name] = dest
    return paths


def ensure_emoji_png(codepoint_hex: str) -> Path | None:
    """Descarga (y cachea) el PNG de Twemoji para un codepoint dado.
    Devuelve None si no se pudo obtener (falla silenciosa, no bloquea el render)."""
    EMOJI_DIR.mkdir(parents=True, exist_ok=True)
    dest = EMOJI_DIR / f"{codepoint_hex}.png"
    if dest.exists() and dest.stat().st_size > 0:
        return dest
    url = f"https://cdn.jsdelivr.net/gh/jdecked/twemoji@latest/assets/72x72/{codepoint_hex}.png"
    try:
        urllib.request.urlretrieve(url, dest)
        if dest.stat().st_size == 0:
            dest.unlink(missing_ok=True)
            return None
        return dest
    except Exception as exc:  # noqa: BLE001
        print(f"  aviso: no se pudo descargar emoji {codepoint_hex}: {exc}", file=sys.stderr)
        return None


def codepoints_for(emoji_str: str) -> str:
    """Convierte un emoji (posiblemente multi-codepoint) al slug hex que usa Twemoji."""
    cps = [f"{ord(ch):x}" for ch in emoji_str if ord(ch) != 0xFE0F]  # descarta variation selector
    return "-".join(cps)


# ---------------------------------------------------------------------------
# Render de cada línea de texto como overlay RGBA transparente
# ---------------------------------------------------------------------------

def wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int, draw: ImageDraw.ImageDraw) -> list[str]:
    words = text.split(" ")
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        bbox = draw.textbbox((0, 0), candidate, font=font)
        if bbox[2] - bbox[0] <= max_width or not current:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def render_caption_overlay(
    text: str,
    canvas_size: tuple[int, int],
    italic_font_path: Path,
    style: str = "veil",
) -> Image.Image:
    width, height = canvas_size
    discreet = style == "subtitle"

    font_size = SUBTITLE_FONT_SIZE if discreet else FONT_SIZE
    center_y_ratio = SUBTITLE_CENTER_Y_RATIO if discreet else TEXT_CENTER_Y_RATIO

    # separar emoji final del texto (las 4 líneas de marca llevan el emoji al final)
    emoji_match = EMOJI_PATTERN.search(text)
    emoji_str = emoji_match.group(0) if emoji_match else ""
    plain_text = EMOJI_PATTERN.sub("", text).strip()

    font = ImageFont.truetype(str(italic_font_path), font_size)
    font.set_variation_by_axes([400, 16])  # wght 400 · opsz 16, igual que el wordmark

    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    max_text_width = int(width * MAX_TEXT_WIDTH_RATIO)
    lines = wrap_text(plain_text, font, max_text_width, draw)

    line_height = int(font_size * LINE_SPACING)
    block_height = line_height * len(lines)
    if emoji_str:
        block_height += int(font_size * 0.9)  # línea extra reservada al emoji

    center_y = int(height * center_y_ratio)
    top = center_y - block_height // 2
    top = max(SAFE_TOP, min(top, height - SAFE_BOTTOM - block_height))

    if not discreet:
        # --- velo degradado direccional cálido (brandbook .ig-mini-tile--promo) ---
        pad = 60
        band_top = max(0, top - pad)
        band_bottom = min(height, top + block_height + pad)
        band_h = band_bottom - band_top
        if band_h > 0:
            grad = np.zeros((band_h, width, 4), dtype=np.uint8)
            # linear-gradient(100deg, transparent 45%, rgba(20,14,10,.65) 100%)
            # 100deg ~ mayormente horizontal con leve inclinación vertical
            xs = np.linspace(0, 1, width)
            ys = np.linspace(0, 1, band_h)
            xx, yy = np.meshgrid(xs, ys)
            proj = xx * np.cos(np.deg2rad(10)) + yy * np.sin(np.deg2rad(10))
            proj = (proj - proj.min()) / (proj.max() - proj.min())
            alpha = np.clip((proj - 0.45) / (1.0 - 0.45), 0, 1) * (0.65 * 255)
            grad[..., 0] = SCRIM_RGB[0]
            grad[..., 1] = SCRIM_RGB[1]
            grad[..., 2] = SCRIM_RGB[2]
            grad[..., 3] = alpha.astype(np.uint8)
            scrim = Image.fromarray(grad, "RGBA")
            overlay.alpha_composite(scrim, (0, band_top))
            draw = ImageDraw.Draw(overlay)
    else:
        # --- sombra suave en vez de velo (brandbook .tiktok-video .play:
        # text-shadow 0 1px 3px rgba(0,0,0,.6)) — discreto, sin tapar la cara ---
        shadow_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        shadow_draw = ImageDraw.Draw(shadow_layer)
        sx, sy = SUBTITLE_SHADOW_OFFSET
        y = top
        for line in lines:
            bbox = shadow_draw.textbbox((0, 0), line, font=font)
            line_w = bbox[2] - bbox[0]
            x = (width - line_w) // 2
            shadow_draw.text((x + sx, y + sy), line, font=font, fill=(0, 0, 0, SUBTITLE_SHADOW_ALPHA))
            y += line_height
        from PIL import ImageFilter
        shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(SUBTITLE_SHADOW_BLUR))
        overlay.alpha_composite(shadow_layer)
        draw = ImageDraw.Draw(overlay)

    # --- texto marfil centrado ---
    y = top
    last_line_bbox = None
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        line_w = bbox[2] - bbox[0]
        x = (width - line_w) // 2
        draw.text((x, y), line, font=font, fill=COLOR_MARFIL)
        last_line_bbox = (x, y, x + line_w, y + line_height)
        y += line_height

    # --- emoji final, alineado a la última línea ---
    if emoji_str and last_line_bbox is not None:
        emoji_size = int(font_size * 0.85)
        codepoints = codepoints_for(emoji_str)
        emoji_path = ensure_emoji_png(codepoints)
        lx, ly, lrx, lry = last_line_bbox
        ex = lrx + int(font_size * 0.35)
        ey = ly + (line_height - emoji_size) // 2
        if emoji_path is not None:
            emoji_img = Image.open(emoji_path).convert("RGBA").resize((emoji_size, emoji_size))
            overlay.alpha_composite(emoji_img, (ex, ey))
        # si falla la descarga, se omite el emoji en vez de romper el render

    return overlay


# ---------------------------------------------------------------------------
# Composición sobre el video
# ---------------------------------------------------------------------------

def build_video(
    video_path: Path,
    output_path: Path,
    captions: list[Caption],
    target_size: tuple[int, int] = (1080, 1920),
) -> None:
    from moviepy import VideoFileClip, ImageClip, CompositeVideoClip
    import moviepy.video.fx as vfx

    fonts = ensure_fonts()

    base = VideoFileClip(str(video_path))
    target_w, target_h = target_size

    # escala "cover" + recorte centrado (no distorsiona, no deja franjas)
    scale = max(target_w / base.w, target_h / base.h)
    resized = base.resized(scale)
    x_center, y_center = resized.w / 2, resized.h / 2
    cropped = resized.cropped(
        x_center=x_center, y_center=y_center, width=target_w, height=target_h
    )

    overlay_clips = []
    for cap in captions:
        img = render_caption_overlay(cap.text, target_size, fonts["italic"], style=cap.style)
        arr = np.array(img)
        clip = (
            ImageClip(arr, transparent=True)
            .with_start(cap.start)
            .with_duration(cap.duration)
            .with_effects([vfx.CrossFadeIn(FADE_DURATION), vfx.CrossFadeOut(FADE_DURATION)])
        )
        overlay_clips.append(clip)

    composite = CompositeVideoClip([cropped, *overlay_clips], size=target_size).with_duration(base.duration)

    silent_path = output_path.with_name(output_path.stem + "_silent" + output_path.suffix)
    composite.without_audio().write_videofile(
        str(silent_path), fps=base.fps or 24, codec="libx264",
        audio=False, preset="slow", ffmpeg_params=["-crf", "18", "-pix_fmt", "yuv420p"],
    )
    base.close()
    composite.close()

    # mux del audio original sin re-encodear (bit a bit, -c:a copy).
    # Sin -shortest a propósito: el track de audio original del clip Kling
    # dura ~0.04s más que el track de video (360 frames a 24fps = 15.0s
    # exactos; el audio se extiende unos ms más, típico remanente/priming
    # del encoder AAC). -shortest cortaría ese remanente y alteraría el
    # audio — se prefiere copiarlo íntegro, byte a byte, aunque el
    # contenedor quede con el audio unos milisegundos más largo que el video.
    import imageio_ffmpeg
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    cmd = [
        ffmpeg_exe, "-y",
        "-i", str(silent_path),
        "-i", str(video_path),
        "-map", "0:v:0", "-map", "1:a:0",
        "-c:v", "copy", "-c:a", "copy",
        str(output_path),
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    silent_path.unlink(missing_ok=True)
    print(f"Listo: {output_path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def load_captions(path: Path | None, default: list[Caption]) -> list[Caption]:
    if path is None:
        return default
    data = json.loads(path.read_text(encoding="utf-8"))
    return [Caption(**item) for item in data]


# Config por default: Opción 3 — "Detrás de cámara" (assets/videos/3/1.mp4, 15.04s)
# Timings ubicados a partir de los beats visuales reales del clip (no del guion
# de 25s de estrategia-lanzamiento.html, que no aplica a este clip de 15s):
#   0.0–3.0s   prenda sola en el rincón, nadie en cuadro
#   3.0–8.5s   Lizzie entra, descuelga y examina la prenda, candid, sin mirar a cámara
#   9.0–11.5s  Lizzie habla a cámara (línea con diálogo real — confirmado por el cliente)
#   11.8–15.0s cierre, prenda en alto, mirando a cámara
DEFAULT_CAPTIONS_OPCION3 = [
    Caption("Un día normal en WAY… o casi 👀", start=0.3, duration=2.6),
    Caption("Estamos cambiando de imagen", start=3.8, duration=4.2),
    # style="subtitle": es la única línea con diálogo real (Lizzie la dice en
    # cámara) — tratamiento discreto (más chica, sin velo, más abajo) para que
    # lea como transcripción y no tape su cara en el único momento sin actuación
    # del video. Las otras 3 líneas son texto no-diegético, se quedan en "veil".
    Caption("Y quería que lo supieran primero ustedes 💛", start=9.0, duration=2.5, style="subtitle"),
    Caption("Bienvenidas a esta nueva etapa ✨", start=11.8, duration=3.24),
]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--video", type=Path, default=Path("assets/videos/3/1.mp4"))
    parser.add_argument("--output", type=Path, default=Path("assets/videos/3/1-final.mp4"))
    parser.add_argument("--captions", type=Path, default=None, help="JSON con lista de {text,start,duration}")
    parser.add_argument("--width", type=int, default=1080)
    parser.add_argument("--height", type=int, default=1920)
    args = parser.parse_args()

    captions = load_captions(args.captions, DEFAULT_CAPTIONS_OPCION3)
    build_video(args.video, args.output, captions, target_size=(args.width, args.height))


if __name__ == "__main__":
    main()
