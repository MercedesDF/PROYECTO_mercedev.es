#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
merci-completo.py — Orquestador Supremo DevSecOps (End-to-End).
Ejecuta en cadena: QA (merci total) -> Sello (merci commit) -> Producción (merci deploy).
"""

import subprocess
import sys
import os
import time
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

def ejecutar_fase(script, nombre):
    print(f"\n{'='*60}")
    print(f"🌟 INICIANDO FASE: {nombre}")
    print(f"{'='*60}\n")
    
    custom_env = os.environ.copy()
    custom_env["MERCI_IS_COMPLETO"] = "1"
    # Ejecutamos sin capturar salida para preservar interactividad (ej. inputs de merci-commit) y colores
    start_time = time.time()
    result = subprocess.run([sys.executable, str(REPO_ROOT / "scripts" / "merci" / script)], env=custom_env)
    end_time = time.time()
    
    if result.returncode != 0:
        print(f"\n❌ [Merci Completo] La cadena se rompió en la fase: {nombre}. Abortando despliegue global.")
        sys.exit(1)
        
    return end_time - start_time

def main():
    start_time = time.time()
    print("🚀 [Merci Completo] Iniciando Cadena de Suministro End-to-End...")
    
    fases_durations = {}
    fases_durations["merci-total.py"] = ejecutar_fase("merci-total.py", "QA & Compilación (merci total)")
    fases_durations["merci-commit.py"] = ejecutar_fase("merci-commit.py", "Sello Atómico (merci commit)")
    fases_durations["merci-deploy.py"] = ejecutar_fase("merci-deploy.py", "Despliegue y Sincronización (merci deploy)")
    
    total_duration = time.time() - start_time
    
    obs_dir = REPO_ROOT / "observabilidad"
    obs_dir.mkdir(exist_ok=True)
    
    pipeline_data = {
        "duration_seconds": total_duration,
        "breakdown": fases_durations
    }
    (obs_dir / ".completo_duration.json").write_text(json.dumps(pipeline_data, indent=2), encoding="utf-8")

    print(f"\n{'='*60}")
    print(f"🏆 [Merci Completo] ¡Cadena de Suministro ejecutada con éxito absoluto en {total_duration:.2f}s!")
    print("   Tu ecosistema está auditado, empaquetado, sincronizado en CMS/Catálogo y desplegado en Producción.")
    print(f"{'='*60}\n")
    
    print("⏱️  Desglose de Tiempos de Ejecución:")
    print("-" * 40)
    for s_name, s_time in fases_durations.items():
        print(f"  {s_name:<25} : {s_time:>5.2f}s")
    print("-" * 40)
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 [Merci Completo] Cadena de suministro interrumpida por la usuaria. Saliendo limpiamente.")
        sys.exit(130)