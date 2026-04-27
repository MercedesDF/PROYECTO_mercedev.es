#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
merci-init.py — Inicializador del Boilerplate (Fase 10).
Escanea el repositorio recién clonado, purga los datos de origen (mercedev)
e inyecta el nuevo nombre y dominio del proyecto.
"""

import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

TARGET_EXTENSIONS = {'.html', '.php', '.md', '.py', '.js', '.scss', '.yaml', '.yml'}

def replace_in_files(old_str: str, new_str: str):
    """
    QUÉ HACE: Recorre recursivamente el repositorio buscando y reemplazando cadenas.
    POR QUÉ: Automatiza la personalización del boilerplate, evitando buscar
    y reemplazar manualmente en Nginx, WordPress, HTML y código fuente.
    """
    print(f"  🔄 Reemplazando '{old_str}' por '{new_str}'...")
    count = 0
    for root, dirs, files in os.walk(REPO_ROOT):
        # Excluimos la carpeta .git, los binarios y el propio script
        if '.git' in root or '.assets-raw' in root or 'assets/images' in root:
            continue
            
        for file in files:
            file_path = Path(root) / file
            if file_path.suffix in TARGET_EXTENSIONS and file_path.name != "merci-init.py":
                try:
                    content = file_path.read_text(encoding="utf-8")
                    if old_str in content:
                        new_content = content.replace(old_str, new_str)
                        file_path.write_text(new_content, encoding="utf-8")
                        count += 1
                except Exception as e:
                    print(f"    ⚠️ No se pudo procesar {file_path.name}: {e}")
    print(f"    ✅ Modificados {count} archivos.")

def purge_directory(dir_path: Path):
    """
    QUÉ HACE: Elimina todo el contenido de una carpeta excepto el archivo .gitkeep.
    POR QUÉ: Limpia la biblioteca y el laboratorio del proyecto clonado para empezar de cero.
    """
    print(f"  🗑️  Purgando directorio: {dir_path.relative_to(REPO_ROOT)}...")
    if not dir_path.exists():
        return
        
    for item in dir_path.iterdir():
        if item.name == ".gitkeep":
            continue
        if item.is_file():
            item.unlink()
        elif item.is_dir():
            # Importación local para evitar dependencias innecesarias globales
            import shutil
            shutil.rmtree(item)

def main():
    print("🚀 [Merci Init] Preparación de nuevo proyecto a partir del Boilerplate.")
    print("⚠️  ADVERTENCIA DE SEGURIDAD: Este script es DESTRUCTIVO.")
    print("Destruirá la biblioteca actual y reemplazará todas las referencias de mercedev.es")
    print("Solo debes ejecutar esto cuando hayas CLONADO este repo para un proyecto NUEVO.\n")
    
    confirm = input("¿Estás segura de querer formatear este código base? Escribe 'DESTRUIR' para continuar: ")
    if confirm != "DESTRUIR":
        print("Operación cancelada. El repositorio está a salvo.")
        sys.exit(0)
        
    nuevo_dominio = input("Introduce el nuevo dominio (ej. midominio.com): ").strip()
    nuevo_nombre = input("Introduce el nombre del proyecto (ej. Mi Empresa): ").strip()
    
    if not nuevo_dominio or not nuevo_nombre:
        print("❌ Error: Los datos no pueden estar vacíos.")
        sys.exit(1)

    # 1. Reemplazo de identidad
    replace_in_files("mercedev.es", nuevo_dominio)
    replace_in_files("mercedev", nuevo_nombre.lower().replace(" ", ""))
    replace_in_files("Mercedes", nuevo_nombre)

    # 2. Purga de datos históricos
    purge_directory(REPO_ROOT / "biblioteca")
    purge_directory(REPO_ROOT / "laboratorio")
    purge_directory(REPO_ROOT / "public" / "biblioteca")
    purge_directory(REPO_ROOT / "public" / "descargas")
    
    print("\n🎉 ¡Inicialización completada! Bienvenido a tu nuevo proyecto.")

if __name__ == "__main__":
    main()