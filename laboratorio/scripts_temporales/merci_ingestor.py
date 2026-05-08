# TODO(Fase 3): Intento obsoleto de ingesta de evidencias desde los directorios multimedia del anfitrión (host). Descartado por depender de rutas absolutas del usuario y crear acoplamiento. Sustituido por copia manual a .assets-raw/.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
merci_ingestor.py — Utilidad para ingestar imágenes y vídeos recientes.

Este script escanea carpetas de captura del usuario en busca de archivos
(imágenes o vídeos) modificados en los últimos 30 minutos.
"""

import argparse
import sys
from datetime import datetime, timedelta
from pathlib import Path
import shutil

# Configuración de rutas
REPO_ROOT = Path(__file__).resolve().parents[2]
ASSETS_RAW_DIR = REPO_ROOT / ".assets-raw"

USER_CAPTURE_DIRS = [
    Path.home() / "Pictures",
    Path.home() / "Videos",
    Path.home() / "Desktop",
]

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".tiff"}
VIDEO_EXTENSIONS = {".mp4", ".mov", ".webm", ".avi", ".mkv"}
ALL_EXTENSIONS = IMAGE_EXTENSIONS.union(VIDEO_EXTENSIONS)

def find_recent_media(scan_dirs: list[Path], time_delta_minutes: int) -> list[Path]:
    recent_files = []
    now = datetime.now()
    time_threshold = now - timedelta(minutes=time_delta_minutes)

    for scan_dir in scan_dirs:
        if not scan_dir.is_dir():
            continue

        for file_path in scan_dir.rglob("*"):
            if file_path.is_file() and file_path.suffix.lower() in ALL_EXTENSIONS:
                try:
                    mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
                    if mtime > time_threshold:
                        recent_files.append(file_path)
                except OSError:
                    continue
    return recent_files

def ingest_media(files_to_ingest: list[Path]):
    if not ASSETS_RAW_DIR.exists():
        ASSETS_RAW_DIR.mkdir(parents=True)

    for src_path in files_to_ingest:
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            dest_filename = f"{timestamp}_{src_path.name}"
            dest_path = ASSETS_RAW_DIR / dest_filename
            shutil.move(str(src_path), str(dest_path))
            print(f"Movido: {src_path.name}")
        except Exception as e:
            print(f"Error al mover {src_path.name}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Merci Ingestor.")
    parser.add_argument("--duration", type=int, default=30)
    args = parser.parse_args()

    found_files = find_recent_media(USER_CAPTURE_DIRS, args.duration)

    if not found_files:
        print("No se encontraron archivos recientes.")
        sys.exit(0)

    print("\nArchivos encontrados:")
    for i, f in enumerate(found_files):
        print(f"  {i+1}. {f.name}")

    response = input("\n¿Mover archivos a .assets-raw/? (s/n): ").lower()
    if response == 's':
        ingest_media(found_files)

if __name__ == "__main__":
    main()