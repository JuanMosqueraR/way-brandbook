"""
concat_reel_clips.py — Concatena 2+ clips de Kling en un solo video 9:16,
aplicando cover-crop centrado a cada clip individualmente antes de unir
(mismo criterio de escalado "cover" que usa add_reel_captions.py, para que
el resultado sea homogéneo aunque los clips fuente tengan relación de
aspecto distinta entre sí).

Usado para armar el Reel de la Opción 2 ("Así nace la nueva WAY"), que a
diferencia de la Opción 3 parte de 2 clips separados en vez de uno solo ya
completo. El resultado de este script es un archivo INTERMEDIO (sin textos
todavía) pensado para pasarse como --video a add_reel_captions.py.

Audio: siempre se genera una pista de audio silenciosa explícita en la
salida (aunque los clips fuente no traigan audio o se pida ignorarlo), para
que el paso de mux de add_reel_captions.py (que asume un stream de audio
para copiar con -map 1:a:0) no falle por falta de stream.

Uso:
    python scripts/concat_reel_clips.py \
        --videos assets/videos/2/1.mp4 assets/videos/2/2.mp4 \
        --output <ruta_temporal>.mp4 \
        --width 1080 --height 1920

Requisitos: pip install moviepy imageio-ffmpeg (ya instalados en este repo).
"""

from __future__ import annotations

import argparse
from pathlib import Path


def cover_crop(clip, target_w: int, target_h: int):
    """Escala 'cover' + recorte centrado — mismo criterio que build_video()
    en add_reel_captions.py, duplicado acá a propósito (4 líneas) para no
    tener que tocar ese script ya probado con la Opción 3."""
    scale = max(target_w / clip.w, target_h / clip.h)
    resized = clip.resized(scale)
    x_center, y_center = resized.w / 2, resized.h / 2
    return resized.cropped(x_center=x_center, y_center=y_center, width=target_w, height=target_h)


def main() -> None:
    from moviepy import VideoFileClip, concatenate_videoclips, AudioClip

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--videos", nargs="+", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--width", type=int, default=1080)
    parser.add_argument("--height", type=int, default=1920)
    args = parser.parse_args()

    clips = [VideoFileClip(str(p)) for p in args.videos]
    fps = clips[0].fps or 24
    cropped = [cover_crop(c, args.width, args.height) for c in clips]

    final = concatenate_videoclips(cropped, method="chain")
    # pista de audio silenciosa explícita (ver docstring)
    silent_audio = AudioClip(lambda t: 0, duration=final.duration, fps=44100)
    final = final.with_audio(silent_audio)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    final.write_videofile(
        str(args.output), fps=fps, codec="libx264", audio_codec="aac",
        preset="slow", ffmpeg_params=["-crf", "18", "-pix_fmt", "yuv420p"],
    )

    for c in clips:
        c.close()
    final.close()
    print(f"Listo: {args.output} ({final.duration:.3f}s, {args.width}x{args.height})")


if __name__ == "__main__":
    main()
