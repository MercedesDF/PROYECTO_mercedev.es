#!/usr/bin/env python3
# recorder_experiment.py — Artefacto de Art de Coté.
import subprocess
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = REPO_ROOT / "laboratorio" / "evidencias"

def record_session(duration=60):
    if not OUTPUT_DIR.exists(): OUTPUT_DIR.mkdir(parents=True)
    target_path = OUTPUT_DIR / f"{datetime.now().strftime('%Y-%m-%d_%H-%M')}_evidencia.mp4"
    
    command = [
        "ffmpeg", "-f", "x11grab", "-video_size", "1920x1080",
        "-i", ":0.0", "-nostdin", "-t", str(duration),
        "-c:v", "libx264", "-preset", "ultrafast", "-crf", "28", str(target_path)
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Grabación finalizada en: {target_path}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    record_session(10) # Prueba de 10 seg