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
    tema = meta.get("tema", "Estantería General")
    
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
            <a href="/biblioteca/" class="card__back-link">← Volver a la Biblioteca</a>
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
    
    # Devolvemos los metadatos para construir el índice
    return {
        "titulo": titulo,
        "descripcion": descripcion,
        "url": f"/biblioteca/{out_filename}",
        "tipo": tipo,
        "fecha": meta.get("fecha", "1970-01-01"),
        "tema": tema
    }

def generar_indice_biblioteca(publicaciones, header_html, footer_html):
    print("📖 Generando índice temático de la Biblioteca...")
    
    # Agrupar publicaciones por tema (Estanterías)
    estanterias = {}
    for pub in publicaciones:
        tema = pub["tema"]
        if tema not in estanterias:
            estanterias[tema] = []
        estanterias[tema].append(pub)
        
    secciones_html = ""
    
    # Ordenar temas alfabéticamente y procesar sus publicaciones
    for tema in sorted(estanterias.keys()):
        # Ordenamos los artículos dentro de un mismo tema del más nuevo al más antiguo
        pubs_tema = sorted(estanterias[tema], key=lambda x: x["fecha"], reverse=True)
        
        cards_html = ""
        for pub in pubs_tema:
            clase_css = "card--booklet" if pub["tipo"] == "cuadernillo" else "card--book"
            badge = "Cuadernillo" if pub["tipo"] == "cuadernillo" else "Bitácora"
            
            cards_html += f"""
                <article class="card {clase_css}">
                    <header>
                        <span class="card__meta">{pub["fecha"]} — {badge}</span>
                        <h2 class="card__title"><a href="{pub["url"]}">{pub["titulo"]}</a></h2>
                    </header>
                    <div class="card__content">
                        <p>{pub["descripcion"]}</p>
                    </div>
                </article>"""
                
        secciones_html += f"""
        <section class="biblioteca-tema" style="margin-bottom: 4rem;">
            <h2 class="home-card__title--highlight" style="margin-bottom: 1.5rem; border-bottom: 1px solid rgba(0,0,0,0.1); padding-bottom: 0.5rem;">{tema}</h2>
            <div class="home-grid">
                {cards_html}
            </div>
        </section>"""
                
    html_final = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Biblioteca — mercedev.es</title>
    <meta name="description" content="Índice de publicaciones técnicas y cuadernillos de la Biblioteca.">
    <link rel="canonical" href="https://mercedev.es/biblioteca/">
    <link rel="stylesheet" href="/css/main.css">
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "CollectionPage",
      "name": "La Biblioteca - mercedev.es",
      "description": "Índice de publicaciones técnicas y cuadernillos de la Biblioteca.",
      "url": "https://mercedev.es/biblioteca/"
    }}
    </script>
</head>
<body>
    {header_html}
    <main class="main--padded section">
        <header style="margin-bottom: 3rem;">
            <h1 class="home-card__title--highlight">La Biblioteca</h1>
            <p>Documentación técnica, cuadernillos DevSecOps y arquitectura de software.</p>
        </header>
        {secciones_html}
    </main>
    {footer_html}
</body>
</html>"""

    out_path = PUBLIC_BIBLIOTECA / "index.html"
    out_path.write_text(html_final, encoding="utf-8")
    print("  ✅ Índice generado con éxito: public/biblioteca/index.html")

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

    publicaciones_procesadas = []

    # Por ahora, compilamos todos los archivos .md que existan en la biblioteca
    for md_file in BIBLIOTECA_DIR.glob("*.md"):
        meta = procesar_archivo(md_file, header_html, footer_html)
        if meta:
            publicaciones_procesadas.append(meta)
            
    generar_indice_biblioteca(publicaciones_procesadas, header_html, footer_html)
            
    print("🚀 [Merci Publish] Pipeline de conversión finalizado.")

if __name__ == "__main__":
    main()