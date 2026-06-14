import os

path = "laboratorio/bitacora-mercedev-epic-08.md"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

entry = """### 2026-06-14 — Arquitectura de Información: 4 Macro-temas y Subtemas

**Contexto:** La categorización de la Biblioteca y el Blog sufría de una fuerte fragmentación. Múltiples temas redundantes dificultaban la navegación lateral y diluían la densidad del contenido.

**Hecho:** Se ha ejecutado una refactorización arquitectónica profunda:
1. **Script de Migración Automatizado (`migrate-themes.py`):** Rastreo de 126 archivos Markdown para reescribir su Frontmatter, mapeando los temas antiguos a 4 macro-temas fijos (*Desarrollo y Arquitectura*, *DevSecOps e Infraestructura*, *Inteligencia Artificial y Agentes*, *Productividad y Gobernanza*) + *Varios*.
2. **Jerarquía Dual:** Inyección del atributo `subtema` en los 126 cuadernillos y actualización de la `plantilla-cuadernillo.md`.
3. **SSG y UI (`merci-publish.py` y `_library-grid.scss`):** Modificación del generador estático para leer ambas dimensiones y modificación del Grid CSS (`grid-column: 1 / -1`) para que los subtítulos fluyan dentro de la cuadrícula de alta densidad sin romperla.

**Motivo / criterio:** *Consolidación y Escalabilidad*. Imponer un techo de cristal de 5 estanterías garantiza un panel de navegación limpio de por vida, delegando la hiper-segmentación al subtema dentro del cuerpo principal.

"""

marker = "## Registro cronológico\n\n"
insert_pos = content.find(marker)
if insert_pos != -1:
    insert_pos += len(marker)
    new_content = content[:insert_pos] + entry + content[insert_pos:]
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Bitacora 1 updated successfully.")
else:
    print("Could not find marker.")
