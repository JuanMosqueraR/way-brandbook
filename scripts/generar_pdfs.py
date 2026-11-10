"""Genera los PDF de entrega-cliente/05-Documentos-de-Marca/ (y la guía del kit) desde los HTML.

    python scripts/generar_pdfs.py [brandbook|guias|anexo|kit|todo]

Requiere `playwright` (Chromium local, no la herramienta MCP; ver CLAUDE.md, incidente de seguridad)
y `pymupdf`. Después de generar, revisar con PyMuPDF: páginas, primera y última, y que no haya
enlaces ni texto ajeno (get_links / get_text).

- Brandbook: A4 con margen de exportación (28 px arriba, 37 px abajo; el CSS de impresión del HTML no
  lleva relleno vertical) y, estampados después con PyMuPDF, el nombre de la sección a la izquierda
  («02 · Sobre WAY», «(continúa)» desde la segunda página) y «n / N» a la derecha: Helvetica 7,5 pt,
  #6B665E. Método reconstruido el 10-nov-2026 y validado contra el PDF del 5-sep (mismas 38 páginas,
  38 de 38 pies idénticos, mismo texto).
- Guías, anexo y guía del kit: A4 con `emulate_media('print')`, sin márgenes ni pies.
"""
import pathlib
import re
import sys

import pymupdf
from playwright.sync_api import sync_playwright

RAIZ = pathlib.Path(__file__).resolve().parent.parent
DOCS = RAIZ / "entrega-cliente" / "05-Documentos-de-Marca"
PIES = {"01": "Portada", "02": "Sobre WAY", "03": "Audiencia", "04": "Personalidad de Marca", "05": "Logo",
        "06": "Colores", "07": "Tipografía", "08": "Voz y Tono", "09": "Fotografía", "10": "Aplicaciones"}
SIMPLES = {
    "guias": [("guia-ecommerce.html", DOCS / "Guia-Ecommerce-WAY.pdf"), ("guia-instagram.html", DOCS / "Guia-Instagram-WAY.pdf")],
    "anexo": [("anexo-pantallas-digital.html", DOCS / "Anexo-Pantallas-Digital-WAY.pdf")],
    "kit": [("guia-kit-pantallas.html", RAIZ / "entrega-cliente" / "07-Pantallas-y-Digital" / "Guia-Canva-e-Illustrator.pdf")],
}


def _pdf(pw_browser, html, out, **opciones):
    pg = pw_browser.new_page()
    pg.goto((RAIZ / html).as_uri(), wait_until="networkidle")
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(1500)
    pg.emulate_media(media="print")
    pg.pdf(path=str(out), format="A4", print_background=True, **opciones)
    pg.close()


def brandbook(browser):
    destino = DOCS / "WAY-Brandbook.pdf"
    tmp = destino.with_suffix(".tmp.pdf")
    _pdf(browser, "brandbook.html", tmp, margin={"top": "28px", "bottom": "37px", "left": "0", "right": "0"})
    d = pymupdf.open(tmp)
    n, actual, vistos = d.page_count, "01", set()
    html = (RAIZ / "brandbook.html").read_text(encoding="utf-8")
    etiquetas = {num: re.sub(r"\s+", "", lab.upper()) for num, lab in re.findall(r'<span class="section-label">(\d\d) — ([^<]+)</span>', html)}
    for i, p in enumerate(d):
        if i:
            arriba = " ".join(s["text"] for b in p.get_text("dict")["blocks"] for l in b.get("lines", []) for s in l["spans"] if s["bbox"][1] < 70)
            txt = re.sub(r"\s+", "", arriba.upper())
            for num, lab in etiquetas.items():
                if f"{num}—{lab}" in txt:
                    actual = num
                    break
        pie = f"{actual} · {PIES[actual]}" + ("  (continúa)" if actual in vistos else "")
        vistos.add(actual)
        color = (107 / 255, 102 / 255, 94 / 255)
        p.insert_text((36.0, 825.9), pie, fontname="helv", fontsize=7.5, color=color)
        num_txt = f"{i + 1} / {n}"
        ancho = pymupdf.get_text_length(num_txt, fontname="helv", fontsize=7.5)
        p.insert_text((559.9 - ancho, 825.9), num_txt, fontname="helv", fontsize=7.5, color=color)
    d.set_metadata({**d.metadata, "title": "WAY — Brandbook Oficial 2026"})
    d.save(destino, deflate=True, garbage=3)
    d.close()
    tmp.unlink()
    print(destino.name, n, "páginas")


def main():
    que = sys.argv[1] if len(sys.argv) > 1 else "todo"
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        if que in ("brandbook", "todo"):
            brandbook(b)
        for clave, trabajos in SIMPLES.items():
            if que in (clave, "todo"):
                for html, out in trabajos:
                    _pdf(b, html, out)
                    print(out.name, pymupdf.open(out).page_count, "páginas")
        b.close()


if __name__ == "__main__":
    main()
