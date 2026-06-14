import os

path = "scripts/merci/merci-publish.py"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if "sub_temas_ordenados = sorted(estanterias[tema_principal].keys())" in line:
        skip = True
        new_lines.append('        pubs_tema = sorted(estanterias[tema_principal], key=lambda x: (x["tipo"].lower() == "compendio", x["fecha"]), reverse=True)\n')
        new_lines.append('        for pub in pubs_tema:\n')
        new_lines.append('            pub_slug = pub.get("slug", slugify(pub["titulo"]))\n')
        new_lines.append('            pub_titulo_html = html.escape(pub["titulo"])\n')
        new_lines.append('            pub_fecha_html = html.escape(str(pub["fecha"]))\n')
        new_lines.append('\n')
        new_lines.append('            enlaces_indice_html += f\'                        <li class="library-nav__article-item">\\n\'\n')
        new_lines.append('            enlaces_indice_html += f\'                            <a href="#{pub_slug}" class="library-nav__article-link" aria-label="Ir al resumen de: {pub_titulo_html} ({pub_fecha_html})">{pub_titulo_html}</a>\\n\'\n')
        new_lines.append('            enlaces_indice_html += f\'                        </li>\\n\'\n')
        continue

    if "enlaces_indice_html += f\'                    </ul>\\n                </li>\\n\'" in line:
        skip = False
        new_lines.append(line)
        continue

    if skip:
        continue
    
    new_lines.append(line)

lines2 = new_lines
new_lines = []
skip = False
for i, line in enumerate(lines2):
    if "for sub_tema in sub_temas_ordenados:" in line:
        skip = True
        new_lines.append('        secciones_html += \'\\n            <div class="library-grid">\'\n')
        new_lines.append('        cards_html = ""\n')
        new_lines.append('        for pub in pubs_tema:\n')
        new_lines.append('            pub_slug = pub.get("slug", slugify(pub["titulo"]))\n')
        new_lines.append('            pub_titulo_html = html.escape(pub["titulo"])\n')
        new_lines.append('            pub_desc_html = html.escape(pub["descripcion"])\n')
        new_lines.append('            pub_fecha_html = html.escape(str(pub["fecha"]))\n')
        new_lines.append('            badge_html = html.escape(str(pub["tipo"])).capitalize()\n')
        new_lines.append('            fase_badge_html = f" &middot; Fase {html.escape(str(pub[\'fase\']))}" if pub.get("fase") else ""\n')
        new_lines.append('            clase_css = "card--booklet" if pub["tipo"].lower() == "cuadernillo" else "card--book"\n')
        new_lines.append('\n')
        new_lines.append('            cards_html += f"""\n')
        new_lines.append('            <article class="card {clase_css}" id="{pub_slug}">\n')
        new_lines.append('                <header>\n')
        new_lines.append('                    <span class="card__meta">{pub_fecha_html} — {badge_html}{fase_badge_html}</span>\n')
        new_lines.append('                    <h2 class="card__title"><a href="{pub["url"]}" aria-label="Leer artículo completo: {pub_titulo_html} ({pub_fecha_html})">{pub_titulo_html}</a></h2>\n')
        new_lines.append('                </header>\n')
        new_lines.append('                <div class="card__content">\n')
        new_lines.append('                    <p>{pub_desc_html}</p>\n')
        new_lines.append('                </div>\n')
        new_lines.append('            </article>"""\n')
        new_lines.append('        secciones_html += cards_html\n')
        new_lines.append('        secciones_html += \'\\n            </div>\\n        </section>\'\n')
        continue

    if "secciones_html += '\\n        </section>'" in line:
        skip = False
        # Do not append, since we already closed the section in the loop above
        continue
    
    if skip:
        continue
    
    new_lines.append(line)

with open(path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)
print("Done!")
