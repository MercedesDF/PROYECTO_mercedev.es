#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
merci_truncate_bitacora.py — Limpiador de laboratorio.
Elimina el bloque del Volumen I de la bitácora activa para iniciar el Volumen II en limpio.
"""

from pathlib import Path

BITACORA_PATH = Path(__file__).resolve().parents[2] / "laboratorio" / "bitacora-mercedev.md"

def main():
    content = BITACORA_PATH.read_text(encoding="utf-8")
    
    marcador_corte = "### 2026-04-23 — Milestone: Cierre definitivo de Fase 6 y validación 100/100"
    marcador_footer = "## Cuando pases esto a la biblioteca"
    
    if marcador_corte not in content or marcador_footer not in content:
        print("❌ Error: Marcadores de corte no encontrados. Operación abortada.")
        return

    parte_superior = content.split(marcador_corte)[0]
    parte_inferior = marcador_footer + content.split(marcador_footer)[1]
    nuevo_contenido = parte_superior.rstrip() + "\n\n---\n\n" + parte_inferior
    
    BITACORA_PATH.write_text(nuevo_contenido, encoding="utf-8")
    print("✅ Laboratorio purgado con éxito. ¡Bienvenido al borrador del Volumen II!")

if __name__ == "__main__":
    main()