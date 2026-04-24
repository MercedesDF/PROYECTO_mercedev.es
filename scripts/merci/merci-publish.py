#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
merci-publish.py — Orquestador maestro de publicación (Fase 7.1).
Transforma documentos Markdown de la biblioteca en páginas HTML estáticas.
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    print("🛡️ [Merci Error] Falta la librería 'markdown'. Ejecuta: pip install markdown")
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parents[2]
BIBLIOTECA_DIR = REPO_ROOT / "biblioteca"
PUBLIC_BIBLIOTECA = REPO_ROOT / "public" / "biblioteca"

def procesar_archivo(filepath: Path, header_html: str, footer_html: str):
    print(f"📖 Leyendo: {filepath.name}...")
    content = filepath.read_text(encoding="utf-8")
    
    # 1. Extraer YAML Frontmatter y Cuerpo del Markdown
    match = re.match(r"^---\n(.*?)\n---\n(.*)", content, re.DOTALL)
    if not match:
        print(f"  ❌ Error: No se encontró YAML Frontmatter válido en {filepath.name}")
        return False
        
    yaml_raw, md_body = match.groups()
    
    # 2. Parsear metadatos manualmente (Cero dependencias extra para YAML simple)
    meta = {}
    for line in yaml_raw.splitlines():
        if ":" in line:
            key, val = line.split(":", 1)
            meta[key.strip()] = val.strip().strip('"\'')
            
    titulo = meta.get("titulo", "Documento sin título")
    tipo = meta.get("tipo", "cuadernillo")
    descripcion = meta.get("descripcion", f"Documento técnico: {titulo}")
    
    print(f"  ⚙️  Procesando {tipo}: {titulo}")
    
    out_filename = filepath.stem + ".html"
    canonical_url = f"https://mercedev.es/biblioteca/{out_filename}"

    # 3. Convertir Markdown a HTML (Soportando bloques de código)
    html_content = markdown.markdown(md_body, extensions=['fenced_code'])
    
    # 4. Generar el HTML final inyectando las clases BEM estructurales
    clase_css = "card--booklet" if tipo == "cuadernillo" else "card--book"
    
    html_final = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titulo} — mercedev.es</title>
    <meta name="description" content="{descripcion}">
    <link rel="canonical" href="{canonical_url}">
    <link rel="stylesheet" href="/css/main.css">
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{titulo}",
      "description": "{descripcion}",
      "url": "{canonical_url}"
    }}
    </script>
</head>
<body>
    {header_html}
    <main class="main--padded section">
        <article class="card {clase_css}">
            <header>
                <h1 class="home-card__title--highlight">{titulo}</h1>
            </header>
            <div class="card__content">
                {html_content}
            </div>
        </article>
    </main>
    {footer_html}
</body>
</html>"""

    # 5. Escribir el documento final en el núcleo estático
    out_path = PUBLIC_BIBLIOTECA / out_filename
    PUBLIC_BIBLIOTECA.mkdir(parents=True, exist_ok=True)
    
    out_path.write_text(html_final, encoding="utf-8")
    print(f"  ✅ Publicado con éxito: public/biblioteca/{out_filename}")
    return True

def main():
    print("🚀 [Merci Publish] Iniciando orquestador de publicación...")
    
    # 0. Extraer Header y Footer dinámicamente de la portada (Single Source of Truth)
    header_html, footer_html = "", ""
    index_path = REPO_ROOT / "public" / "index.html"
    if index_path.exists():
        index_content = index_path.read_text(encoding="utf-8")
        h_match = re.search(r"(<header.*?</header>)", index_content, re.DOTALL | re.IGNORECASE)
        f_match = re.search(r"(<footer.*?</footer>)", index_content, re.DOTALL | re.IGNORECASE)
        header_html = h_match.group(1) if h_match else ""
        footer_html = f_match.group(1) if f_match else ""

    # Por ahora, compilamos todos los archivos .md que existan en la biblioteca
    for md_file in BIBLIOTECA_DIR.glob("*.md"):
        procesar_archivo(md_file, header_html, footer_html)
            
    print("🚀 [Merci Publish] Pipeline de conversión finalizado.")

if __name__ == "__main__":
    main()