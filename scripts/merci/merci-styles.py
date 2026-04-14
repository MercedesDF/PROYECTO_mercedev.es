#!/usr/bin/env python3
import os
import subprocess
import urllib.request
import tarfile
import sys

# Sistema Merci - Compilador SASS Standalone
# Descarga automáticamente Dart Sass si no está presente y compila main.scss a main.css,
# manteniendo la filosofía de 0 dependencias globales al sistema host.

DART_SASS_VERSION = "1.80.3"
DART_SASS_URL = f"https://github.com/sass/dart-sass/releases/download/{DART_SASS_VERSION}/dart-sass-{DART_SASS_VERSION}-linux-x64.tar.gz"

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
BIN_DIR = os.path.join(BASE_DIR, 'scripts', 'merci', 'bin')
SASS_BIN = os.path.join(BIN_DIR, 'dart-sass', 'sass')

def ensure_dart_sass():
    """Verifica si dart-sass existe localmente. Si no, lo descarga y extrae."""
    if os.path.exists(SASS_BIN):
        return True
        
    print(f"Merci: No se encontró Dart Sass local, procesando descarga segura (v{DART_SASS_VERSION})...")
    
    if not os.path.exists(BIN_DIR):
        os.makedirs(BIN_DIR)
        
    tar_path = os.path.join(BIN_DIR, 'dart-sass.tar.gz')
    
    try:
        urllib.request.urlretrieve(DART_SASS_URL, tar_path)
        print("Merci: Descarga completada. Extrayendo binarios...")
        
        with tarfile.open(tar_path, 'r:gz') as tar:
            
            import sys
            
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(tar, BIN_DIR)
            
        # Clean tarball
        os.remove(tar_path)
        print("Merci: Dart Sass configurado internamente con éxito.")
        
    except Exception as e:
        print(f"Merci Error crítico: Imposible descargar/instalar Dart Sass. Motivo: {e}")
        sys.exit(1)

def compile_styles():
    """Ejecuta dart-sass prestando atención a que sea independiente."""
    ensure_dart_sass()
    
    sass_main = os.path.join(BASE_DIR, 'src', 'scss', 'main.scss')
    css_dir = os.path.join(BASE_DIR, 'public', 'css')
    css_main = os.path.join(css_dir, 'main.css')
    
    if not os.path.exists(css_dir):
        os.makedirs(css_dir)

    print("Merci: Compilando arquitectura inteligente SASS a CSS (Dart Sass local)...")
    
    # Run dart-sass
    try:
        # syntax: sass src/scss/main.scss public/css/main.css --style=compressed
        subprocess.run(
            [SASS_BIN, sass_main, css_main, '--style=compressed'],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"Merci: CSS compilado con éxito en -> {css_main}")
    except subprocess.CalledProcessError as e:
        print(f"Merci Error: Fallo crítico al compilar la estructura SASS:\n{e.stderr}")
        sys.exit(1)

if __name__ == "__main__":
    compile_styles()
