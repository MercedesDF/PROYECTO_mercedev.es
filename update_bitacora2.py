import os

path = "laboratorio/bitacora-mercedev-epic-08.md"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

entry = """### 2026-06-14 — Hotfix: Extracción de Subtema en SSG

**Contexto:** Tras el commit de la reestructuración jerárquica de la Biblioteca, se observó que todas las agrupaciones de segundo nivel aparecían con el título "General" a pesar de que el Frontmatter de los Markdown tenía el subtema correcto.

**Hecho:** Se identificó que la función `procesar_archivo` en `merci-publish.py` no estaba retornando el atributo `subtema` en su diccionario de salida hacia el orquestador maestro, provocando que la función `generar_indice` usara el valor por defecto ("General"). Se ha parcheado la extracción YAML para arrastrar este atributo al diccionario `pub` del motor SSG.

**Motivo / criterio:** *Consistencia de Datos*. Garantizar que el ciclo de vida del metadato (desde el Markdown puro hasta el renderizado HTML) no se interrumpa en las funciones intersecantes.

"""

marker = "## Registro cronológico\n\n"
insert_pos = content.find(marker)
if insert_pos != -1:
    insert_pos += len(marker)
    new_content = content[:insert_pos] + entry + content[insert_pos:]
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Bitacora 2 updated successfully.")
else:
    print("Could not find marker.")
