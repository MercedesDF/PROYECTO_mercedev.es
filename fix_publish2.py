import os

path = "scripts/merci/merci-publish.py"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update the grouping block
old_group = """    # Agrupar publicaciones por tema (Estanterías)
    estanterias = {}
    for pub in publicaciones:
        # QUÉ HACE: Implementa agrupación por Tema principal (sin subtemas para máxima densidad).
        tema_raw = pub.get("tema") or "General"
        tema_completo = str(tema_raw).split('/')
        tema_principal = tema_completo[0].strip().casefold()

        if tema_principal not in estanterias:
            estanterias[tema_principal] = []

        estanterias[tema_principal].append(pub)"""

new_group = """    # Agrupar publicaciones por tema (Estanterías)
    estanterias = {}
    for pub in publicaciones:
        # QUÉ HACE: Implementa agrupación por Tema principal y Subtema desde el frontmatter.
        tema_principal = pub.get("tema", "Varios").strip()
        sub_tema = pub.get("subtema", "General").strip()

        if tema_principal not in estanterias:
            estanterias[tema_principal] = {}

        if sub_tema not in estanterias[tema_principal]:
            estanterias[tema_principal][sub_tema] = []

        estanterias[tema_principal][sub_tema].append(pub)"""

content = content.replace(old_group, new_group)

# 2. Extract and replace the rendering loop completely.
# Since we know the exact line content for the start and end of the loop, we can just find it.
start_marker = "        enlaces_indice_html += f'                    <ul class=\"library-nav__article-list\">\\n'"
end_marker = "        secciones_html += '\\n            </div>\\n        </section>'"

idx_start = content.find(start_marker)
idx_end = content.find(end_marker) + len(end_marker)

if idx_start != -1 and idx_end != -1:
    new_loop = """        enlaces_indice_html += f'                    <ul class="library-nav__article-list">\\n'

        sub_temas_ordenados = sorted(estanterias[tema_principal].keys())
        for sub_tema in sub_temas_ordenados:
            sub_tema_html = html.escape(sub_tema)
            enlaces_indice_html += f'                        <li class="library-nav__sub-theme">{sub_tema_html}</li>\\n'

            pubs_sub_tema = sorted(estanterias[tema_principal][sub_tema], key=lambda x: (x["tipo"].lower() == "compendio", x["fecha"]), reverse=True)
            for pub in pubs_sub_tema:
                pub_slug = pub.get("slug", slugify(pub["titulo"]))
                pub_titulo_html = html.escape(pub["titulo"])
                pub_fecha_html = html.escape(str(pub["fecha"]))

                enlaces_indice_html += f'                        <li class="library-nav__article-item">\\n'
                enlaces_indice_html += f'                            <a href="#{pub_slug}" class="library-nav__article-link" aria-label="Ir al resumen de: {pub_titulo_html} ({pub_fecha_html})">{pub_titulo_html}</a>\\n'
                enlaces_indice_html += f'                        </li>\\n'

        enlaces_indice_html += f'                    </ul>\\n                </li>\\n'

        secciones_html += f\"\"\"
        <section class="library-section" id="{tema_slug}">
            <div class="library-section__header">
                <h2 class="library-section__title home-card__title--highlight"><a href="#{tema_slug}" aria-label="Ver sección: {tema_html}">{tema_html}</a></h2>
                <a href="#top" class="library-section__back-link">↑ Volver arriba</a>
            </div>\"\"\"

        secciones_html += '\\n            <div class="library-grid">'
        for sub_tema in sub_temas_ordenados:
            sub_tema_html = html.escape(sub_tema)
            secciones_html += f'\\n                <h3 class="library-subsection__title">{sub_tema_html}</h3>'

            pubs_sub_tema = sorted(estanterias[tema_principal][sub_tema], key=lambda x: (x["tipo"].lower() == "compendio", x["fecha"]), reverse=True)
            for pub in pubs_sub_tema:
                pub_slug = pub.get("slug", slugify(pub["titulo"]))
                pub_titulo_html = html.escape(pub["titulo"])
                pub_desc_html = html.escape(pub["descripcion"])
                pub_fecha_html = html.escape(str(pub["fecha"]))
                badge_html = html.escape(str(pub["tipo"])).capitalize()
                fase_badge_html = f" &middot; Fase {html.escape(str(pub['fase']))}" if pub.get("fase") else ""
                clase_css = "card--booklet" if pub["tipo"].lower() == "cuadernillo" else "card--book"

                secciones_html += f\"\"\"
                <article class="card {clase_css}" id="{pub_slug}">
                    <header>
                        <span class="card__meta">{pub_fecha_html} — {badge_html}{fase_badge_html}</span>
                        <h2 class="card__title"><a href="{pub["url"]}" aria-label="Leer artículo completo: {pub_titulo_html} ({pub_fecha_html})">{pub_titulo_html}</a></h2>
                    </header>
                    <div class="card__content">
                        <p>{pub_desc_html}</p>
                    </div>
                </article>\"\"\"
        secciones_html += '\\n            </div>\\n        </section>'"""
        
    content = content[:idx_start] + new_loop + content[idx_end:]
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Publish script updated.")
else:
    print("Failed to find markers!")

