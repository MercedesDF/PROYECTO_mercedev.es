#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

def extraer_fecha(filepath: Path) -> datetime | None:
    """Extrae la fecha física de modificación del archivo en el sistema operativo (st_mtime)."""
    if not filepath.exists():
        return None
    return datetime.fromtimestamp(filepath.stat().st_mtime)

def main():
    print("🕵️‍♂️  [Merci Drift] Analizando deriva documental entre código y manuales...")

    fechas_manuales = [extraer_fecha(m) for m in MANUALES_MAESTROS if extraer_fecha(m)]
    if not fechas_manuales:
        print("  ⚠️ [Merci Warn] No se pudieron extraer fechas de los manuales maestros.")
        sys.exit(0) # Salida limpia para no bloquear el pipeline

    fecha_referencia = max(fechas_manuales)
    # Extraer el contenido de todos los manuales maestros para comprobación semántica estricta
    manuales_textos = {m.name: (m.read_text(encoding="utf-8", errors="ignore") if m.exists() else "") for m in MANUALES_MAESTROS}

    archivos_en_deriva = []
    for s in SCRIPTS_DIR.glob("*.py"):
        if s.name == "__init__.py": continue
        motivos = []
        fecha_script = extraer_fecha(s)
        
        # 1. Deriva Temporal (Fecha)
        if fecha_script and fecha_script > fecha_referencia:
            motivos.append(f"Temporal: {fecha_script.strftime('%Y-%m-%d %H:%M')} > Manuales: {fecha_referencia.strftime('%Y-%m-%d %H:%M')}")
            
        # 2. Deriva Semántica (Presencia en manuales maestros)
        faltantes = [nombre for nombre, contenido in manuales_textos.items() if s.name not in contenido]
        if faltantes:
            motivos.append(f"Semántica: No mencionado en {', '.join(faltantes)}")
            
        if motivos:
            archivos_en_deriva.append({"archivo": s.name, "motivos": " | ".join(motivos)})

    DRIFT_REPORT_PATH.parent.mkdir(exist_ok=True)
    DRIFT_REPORT_PATH.write_text(json.dumps(archivos_en_deriva, indent=2), encoding="utf-8")

    if archivos_en_deriva:
        print(f"  ⚠️ [ADVERTENCIA] Deriva Documental detectada en {len(archivos_en_deriva)} script(s).")
        for item in archivos_en_deriva:
            print(f"     - {item['archivo']} ({item['motivos']})")
    else:
        print("  ✅ [Éxito] Sincronización perfecta. Ningún script es más reciente que los manuales y todos están documentados.")

if __name__ == "__main__":
    main()