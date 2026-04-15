#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
merci-commit.py — Automatización de commits impulsados por la bitácora.

Extrae la última entrada cronológica de la bitácora y la utiliza 
para redactar y ejecutar un commit atómico estructurado.
"""

import re
import sys
import subprocess
from pathlib import Path

# Definición de rutas absolutas basadas en la ubicación del script
REPO_ROOT = Path(__file__).resolve().parents[2]
BITACORA_PATH = REPO_ROOT / "laboratorio" / "bitacora-mercedev.md"

def parse_latest_entry(content: str):
    """Analiza el texto de la bitácora y extrae los datos de la última entrada."""
    try:
        # Dividimos el texto para quedarnos solo con lo que hay debajo del registro
        _, registro = content.split("## Registro cronológico", 1)
    except ValueError:
        print("[Merci Error] No se encontró la cabecera '## Registro cronológico'.")
        sys.exit(1)

    # RegEx (Regular Expressions - Expresiones Regulares) para capturar el primer bloque:
    # Busca "### YYYY-MM-DD — Título" y captura todo hasta el siguiente "###" o el final.
    pattern = r"###\s+(\d{4}-\d{2}-\d{2})\s+—\s+([^\n]+)\n(.*?)(?=###\s+\d{4}-\d{2}-\d{2}|$)"
    match = re.search(pattern, registro, re.DOTALL)

    if not match:
        print("[Merci Error] No se detectaron entradas válidas en el registro.")
        sys.exit(1)

    date, title, body = match.groups()
    
    # RegEx adicionales para extraer bloques específicos dentro del cuerpo
    context_match = re.search(r"\*\*Contexto:\*\*\s*(.*?)(?=\*\*Hecho:\*\*|\*\*Detalle)", body, re.DOTALL)
    hecho_match = re.search(r"\*\*Hecho:\*\*\s*(.*?)(?=\*\*Detalle|\*\*Motivo)", body, re.DOTALL)

    context = context_match.group(1).strip() if context_match else "Sin contexto explícito."
    hecho = hecho_match.group(1).strip() if hecho_match else "Sin hechos documentados."

    return title.strip(), context, hecho

def main():
    print("Merci revisa el estado técnico...")
    
    if not BITACORA_PATH.exists():
        print(f"[Merci Error] Archivo de bitácora no localizado en {BITACORA_PATH}")
        sys.exit(1)

    content = BITACORA_PATH.read_text(encoding="utf-8")
    title, context, hecho = parse_latest_entry(content)

    # Formateo del mensaje para Git
    commit_subject = title
    commit_body = f"Contexto:\n{context}\n\nHecho:\n{hecho}"

    try:
        # 1. Añadir todos los archivos modificados/nuevos al stage (incluyendo la bitácora)
        print("[Merci Git] Añadiendo archivos al stage (git add .)...")
        subprocess.run(["git", "add", "."], cwd=REPO_ROOT, check=True)

        # 2. Ejecutar el commit con dos banderas -m (sujeto y cuerpo)
        print(f"[Merci Commit] Ejecutando: '{commit_subject}'")
        subprocess.run(["git", "commit", "-m", commit_subject, "-m", commit_body], check=True)
        
        print("\n[Merci Éxito] Commit atómico finalizado correctamente.")
        
    except subprocess.CalledProcessError as e:
        # Shift-Left: Captura de errores si Git falla (ej. si pre-commit lo bloquea)
        print(f"\n[Merci Error] La ejecución de Git ha fallado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()