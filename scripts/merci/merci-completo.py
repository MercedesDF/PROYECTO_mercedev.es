#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
merci-completo.py — Orquestador Supremo DevSecOps (End-to-End).
Ejecuta en cadena: QA (merci total) -> Sello (merci commit) -> Producción (merci deploy).
"""

import subprocess
import sys
import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

def ejecutar_fase(script, nombre):
    print(f"\n{'='*60}")
    print(f"🌟 INICIANDO FASE: {nombre}")
    print(f"{'='*60}\n")
    
    custom_env = os.environ.copy()
    custom_env["MERCI_IS_COMPLETO"] = "1"
    # Ejecutamos sin capturar salida para preservar interactividad (ej. inputs de merci-commit) y colores
    result = subprocess.run([sys.executable, str(REPO_ROOT / "scripts" / "merci" / script)], env=custom_env)
    if result.returncode != 0:
        print(f"\n❌ [Merci Completo] La cadena se rompió en la fase: {nombre}. Abortando despliegue global.")
        sys.exit(1)

def main():
    print("🚀 [Merci Completo] Iniciando Cadena de Suministro End-to-End...")
    ejecutar_fase("merci-total.py", "QA & Compilación (merci total)")
    ejecutar_fase("merci-commit.py", "Sello Atómico (merci commit)")
    ejecutar_fase("merci-deploy.py", "Despliegue y Sincronización (merci deploy)")
    
    print(f"\n{'='*60}")
    print("🏆 [Merci Completo] ¡Cadena de Suministro ejecutada con éxito absoluto!")
    print("   Tu ecosistema está auditado, empaquetado, sincronizado en CMS/Catálogo y desplegado en Producción.")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 [Merci Completo] Cadena de suministro interrumpida por la usuaria. Saliendo limpiamente.")
        sys.exit(130)