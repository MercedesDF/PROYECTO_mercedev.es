#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
merci_extract_boilerplate.py — Extractor automatizado de bitácora.
Extrae el historial fundacional (Fases 1 a 6) y lo convierte en un libro publicado.
"""

import re
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
BITACORA_IN = REPO_ROOT / "laboratorio" / "bitacora-mercedev.md"
LIBRO_OUT = REPO_ROOT / "biblioteca" / "bitacora-merci-boilerplate.md"

def main():
    print("⚙️ [Merci Extractor] Leyendo bitácora del laboratorio...")
    contenido = BITACORA_IN.read_text(encoding="utf-8")

    # 1. Definir el punto de corte exacto
    marcador_corte = "### 2026-04-23 — Milestone: Cierre definitivo de Fase 6 y validación 100/100"
    
    if marcador_corte not in contenido:
        print("❌ Error: No se encontró el marcador de la Fase 6 en la bitácora.")
        return

    # 2. Extraer desde el marcador hacia abajo (el pasado)
    partes = contenido.split(marcador_corte)
    historial_extraido = marcador_corte + partes[1]

    # 3. Limpiar el pie de página de instrucciones del laboratorio
    historial_extraido = re.split(r"## Cuando pases esto a la biblioteca", historial_extraido)[0].strip()

    # 4. Inyectar metadatos estrictos (Shift-Left Data Quality)
    yaml_frontmatter = f"""---
titulo: "Bitácora Fundacional: Merci Boilerplate (Fases 1 a 6)"
descripcion: "Registro cronológico inmutable de la construcción del motor híbrido DevSecOps, desde el primer commit hasta la validación 100/100."
tipo: "bitacora"
tema: "Arquitectura y Rendimiento"
volumen: 1
fecha: "{datetime.now().strftime('%Y-%m-%d')}"
estado: "publicado"
portada: "portada-auditoria.webp"
alt_portada: "Puntuación de 100/100 en la auditoría de rendimiento de Lighthouse."
---

"""
    # 5. Escribir el nuevo libro directamente en la biblioteca
    LIBRO_OUT.write_text(yaml_frontmatter + historial_extraido, encoding="utf-8")
    print(f"✅ Extracción exitosa. El libro fundacional ha sido creado en: {LIBRO_OUT.relative_to(REPO_ROOT)}")

if __name__ == "__main__":
    main()