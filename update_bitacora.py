import os

path = "laboratorio/bitacora-mercedev-epic-08.md"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

entry = """### 2026-06-14 — Hotfix: Resolución de fallo silencioso en generador SSG (merci-publish.py)

**Contexto:** Tras el commit anterior de Alta Densidad, se observó que la compilación de la Biblioteca no reflejaba los cambios estructurales (`.library-grid` y omisión de subtemas) en los HTML estáticos generados.

**Hecho:** Se detectó que la refactorización en `merci-publish.py` falló de forma silenciosa, dejando la lógica antigua intacta (iterando sobre `sub_temas_ordenados`). Se ha ejecutado un script correctivo robusto para reescribir los bucles de renderizado HTML del SSG, eliminando la jerarquía de subtemas y envolviendo las iteraciones directamente en `.library-grid`. Tras recompilar, la Biblioteca consolida finalmente la alta densidad.

**Motivo / criterio:** *QA y Trazabilidad*. Un fallo en la inyección de código derivó en un falso positivo del pipeline de compilación (que reportó éxito porque el código original de Python seguía siendo válido sintácticamente, pero sin aplicar el rediseño). Se documenta para enfatizar la verificación visual (QA) post-compilación.

"""

marker = "## Registro cronológico\n\n"
insert_pos = content.find(marker)
if insert_pos != -1:
    insert_pos += len(marker)
    new_content = content[:insert_pos] + entry + content[insert_pos:]
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Bitacora updated successfully.")
else:
    print("Could not find marker.")
