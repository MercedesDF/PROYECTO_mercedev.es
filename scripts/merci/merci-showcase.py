#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
merci-showcase.py — Orquestador de despliegue para la demostración interactiva.

Aplica el patrón de 'Clon Efímero': Copia el repositorio en una carpeta temporal,
ejecuta el instanciador destructivo (merci-init.py) para purgar datos privados y 
telemetría, y sube el Boilerplate inmaculado al subdominio público vía rsync.
"""

import sys
import shutil
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRATCH_DIR = REPO_ROOT / "scratch" / "showcase_build"

# Configuración de infraestructura (CloudPanel)
REMOTE_USER = "mercedev-php"
REMOTE_HOST = "mercedev.es"
REMOTE_PATH = "/home/mercedev-php/htdocs/boilerplate.mercedev.es/"

def main():
    print("🚀 [Merci Showcase] Iniciando construcción del Clon Efímero...")

    if SCRATCH_DIR.exists():
        shutil.rmtree(SCRATCH_DIR)
    SCRATCH_DIR.parent.mkdir(parents=True, exist_ok=True)

    print("  📦 Copiando código fuente al entorno de aislamiento...")
    # QUÉ HACE: Ignora carpetas privadas/pesadas y evita conflictos de permisos con enlaces simbólicos.
    ignore_patterns = shutil.ignore_patterns('.git', '.venv', '__pycache__', 'scratch', 'node_modules', 'observabilidad', '.privado', 'backups', '.assets-raw', 'blog', 'tienda')
    shutil.copytree(REPO_ROOT, SCRATCH_DIR, ignore=ignore_patterns, symlinks=True)

    print("  🧹 Inyectando guillotina (merci-init.py) para purgar identidad y datos privados...")
    init_script = SCRATCH_DIR / "scripts" / "merci" / "merci-init.py"
    try:
        subprocess.run(["python3", str(init_script)], cwd=SCRATCH_DIR, check=True)
    except subprocess.CalledProcessError:
        print("  ❌ [Error] El proceso de inicialización falló en el clon efímero.")
        sys.exit(1)

    print(f"  🌐 Desplegando Boilerplate inmaculado en {REMOTE_HOST} (rsync)...")
    rsync_cmd = ["rsync", "-avz", "--delete", "-e", "ssh -o StrictHostKeyChecking=accept-new", f"{SCRATCH_DIR}/", f"{REMOTE_USER}@{REMOTE_HOST}:{REMOTE_PATH}"]
    subprocess.run(rsync_cmd, check=True)

    print("  🗑️ Destruyendo el Clon Efímero...")
    shutil.rmtree(SCRATCH_DIR)
    print("✨ [Merci Showcase] ¡Despliegue completado con éxito absoluto!")

if __name__ == "__main__":
    main()