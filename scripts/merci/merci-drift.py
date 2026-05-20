#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Historial de modificaciones:
# - Última modificación el 2026-05-20 13:03 (Fase 2 - Épica 3)

"""
merci-drift.py — Detector de Deriva Documental (Document Drift).

Compara la fecha de última modificación (Regla 17) de los scripts del 
ecosistema frente a la de los manuales maestros. Si un script es más 
reciente que los manuales, emite una advertencia y guarda una métrica para el SRE.
"""

import re
import sys
import json
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS_DIR = REPO_ROOT / "scripts" / "merci"
DRIFT_REPORT_PATH = REPO_ROOT / "observabilidad" / ".drift_report.json"

MANUALES_MAESTROS = [
    REPO_ROOT / "README.md",
    REPO_ROOT / "instrucciones.md"
]

# El grupo de hora (HH:MM) es opcional para mantener retrocompatibilidad con scripts que solo tienen fecha.
DATE_PATTERN = re.compile(r"[-—–]\s*Última modificación el (\d{4}-\d{2}-\d{2}(?:\s\d{2}:\d{2})?)")

def extraer_fecha(filepath: Path) -> datetime | None:
    """Extrae la fecha normalizada de la cabecera del archivo."""
    if not filepath.exists():
        return None
    content = filepath.read_text(encoding="utf-8", errors="ignore")
    match = DATE_PATTERN.search(content)
    if match:
        try:
            valor = match.group(1)
            # Si la cadena incluye hora, la parsea completa. Si no, asume 00:00
            # para no romper archivos que aún solo tienen fecha (Retrocompatibilidad).
            if len(valor) > 10:
                return datetime.strptime(valor, "%Y-%m-%d %H:%M")
            else:
                return datetime.strptime(valor, "%Y-%m-%d")
        except ValueError:
            return None
    return None

def main():
    print("🕵️‍♂️  [Merci Drift] Analizando deriva documental entre código y manuales...")

    fechas_manuales = [extraer_fecha(m) for m in MANUALES_MAESTROS if extraer_fecha(m)]
    if not fechas_manuales:
        print("  ⚠️ [Merci Warn] No se pudieron extraer fechas de los manuales maestros.")
        sys.exit(0) # Salida limpia para no bloquear el pipeline

    fecha_referencia = max(fechas_manuales)
    archivos_en_deriva = [{"archivo": s.name, "fecha_script": extraer_fecha(s).strftime("%Y-%m-%d")} 
                          for s in SCRIPTS_DIR.glob("*.py") 
                          if extraer_fecha(s) and extraer_fecha(s) > fecha_referencia]

    DRIFT_REPORT_PATH.parent.mkdir(exist_ok=True)
    DRIFT_REPORT_PATH.write_text(json.dumps(archivos_en_deriva, indent=2), encoding="utf-8")

    if archivos_en_deriva:
        print(f"  ⚠️ [ADVERTENCIA] Deriva Documental detectada en {len(archivos_en_deriva)} script(s).")
        for item in archivos_en_deriva:
            print(f"     - {item['archivo']} (Código: {item['fecha_script']} > Manual: {fecha_referencia.strftime('%Y-%m-%d')})")
    else:
        print("  ✅ [Éxito] Sincronización perfecta. Ningún script es más reciente que los manuales.")

if __name__ == "__main__":
    main()