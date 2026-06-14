import os

path = "scripts/merci/merci-publish.py"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old_return = """    return {
        "titulo": titulo,
        "descripcion": descripcion,
        "url": f"{base_url_path}{out_filename}",
        "tipo": tipo,
        "fecha": meta.get("fecha", "1970-01-01"),
        "tema": tema,
        "fase": fase,
        "out_html_path": out_path,
        "out_pdf_path": out_pdf_path,
        "slug": slug
    }"""

new_return = """    return {
        "titulo": titulo,
        "descripcion": descripcion,
        "url": f"{base_url_path}{out_filename}",
        "tipo": tipo,
        "fecha": meta.get("fecha", "1970-01-01"),
        "tema": tema,
        "subtema": meta.get("subtema", "General").strip().strip('"\\''),
        "fase": fase,
        "out_html_path": out_path,
        "out_pdf_path": out_pdf_path,
        "slug": slug
    }"""

if old_return in content:
    content = content.replace(old_return, new_return)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Fixed subtema successfully.")
else:
    print("Could not find old_return")

