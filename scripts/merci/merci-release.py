#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
merci-release.py — Orquestador de exportación al Boilerplate.
Automatiza el SOP de mantenimiento: Clona el proyecto en un directorio efímero,
lo purga con merci-init.py y lo sincroniza vía rsync al repositorio local del Boilerplate.
"""

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

def main():
    print("🚀 [Merci Release] Iniciando orquestador de exportación al Boilerplate...")
    
    # 1. Resolver ruta del repositorio destino (Hermano de la matriz por defecto)
    default_dest = (REPO_ROOT.parent / "merci-boilerplate").resolve()
    
    parser = argparse.ArgumentParser(description="Orquestador de exportación al Boilerplate.")
    parser.add_argument('--dest', type=str, help="Ruta al repositorio de merci-boilerplate")
    parser.add_argument('--non-interactive', action='store_true', help="Ejecutar en modo no interactivo sin prompts")
    args = parser.parse_known_args()[0]
    
    if args.dest:
        dest_path = Path(args.dest).resolve()
    elif args.non_interactive:
        dest_path = default_dest
    else:
        print("\n👉 Introduce la ruta a tu REPOSITORIO OFICIAL LOCAL de 'merci-boilerplate'")
        print("   (El script creará el clon efímero en segundo plano de forma invisible)")
        dest_input = input(f"   [Enter] para usar por defecto: {default_dest}\n   O escribe una ruta alternativa: ").strip()
        dest_path = Path(dest_input).resolve() if dest_input else default_dest
    
    if not dest_path.exists() or not (dest_path / ".git").is_dir():
        print(f"  ❌ Error: La ruta '{dest_path}' no parece ser un repositorio Git válido.")
        sys.exit(1)
        
    print(f"\n  📦 Destino verificado: {dest_path}")
    
    # 2. Flujo del Clon Efímero
    print("  🛠️  Creando clon efímero para purga de datos...")
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_repo = Path(tmpdir) / "clone"
        
        # Clonar localmente
        subprocess.run(["git", "clone", str(REPO_ROOT), str(tmp_repo)], capture_output=True, check=True)
        
        # Inyectar cambios locales no comiteados en el clon (esencial para probar fixes pre-commit)
        subprocess.run(["rsync", "-a", "--exclude=.git", "--exclude=.venv", "--exclude=__pycache__", f"{REPO_ROOT}/", f"{tmp_repo}/"], capture_output=True, check=True)
        
        print("  🧹 Ejecutando instanciación destructiva (merci-init.py) en el clon efímero...")
        init_script = tmp_repo / "scripts" / "merci" / "merci-init.py"
        
        # Invocación no interactiva con argumentos de marca blanca
        init_cmd = [
            sys.executable,
            str(init_script),
            "--force",
            "--dominio", "tuempresa.es",
            "--nombre", "Tu Empresa",
            "--ia"
        ]
        result_init = subprocess.run(init_cmd, cwd=str(tmp_repo))
        if result_init.returncode != 0:
            print("  ❌ Error durante la instanciación. Abortando.")
            sys.exit(1)
        
        print("\n  📤 Sincronizando código inmaculado hacia el repositorio destino (rsync)...")
        rsync_cmd = ["rsync", "-av", "--delete", "--exclude=.git", f"{tmp_repo}/", f"{dest_path}/"]
        subprocess.run(rsync_cmd, capture_output=True, check=True)
        
    print(f"\n✅ [Merci Release] ¡Éxito! El Boilerplate ha sido actualizado en {dest_path.name}")
    
    # 3. Flujo de Publicación (Automated QA, Commit & Push)
    print("\n🚀 [Merci Release] Fase 2: Auditoría y Publicación")
    
    # QUÉ HACE: Extrae la versión del README.md (que ya fue renombrado de README-merci.md por merci-init)
    readme_path = dest_path / "README.md"
    version = "vX.X.X"
    if readme_path.exists():
        match = re.search(r'# Merci Boilerplate (v\d+\.\d+\.\d+)', readme_path.read_text(encoding="utf-8"))
        if match: version = match.group(1)
            
    print(f"  🔍 Versión detectada para la release: {version}")
    print("  🧪 Ejecutando 'merci total' en el Boilerplate para QA estricto...")
    
    # QUÉ HACE: Ejecuta el orquestador maestro utilizando el entorno virtual actual (sys.executable)
    result_total = subprocess.run([sys.executable, "scripts/merci/merci-total.py"], cwd=str(dest_path))
    if result_total.returncode != 0:
        print("\n  ❌ 'merci total' falló en el Boilerplate. Revisa los errores en la terminal antes de publicar.")
        sys.exit(1)
        
    print("  📦 Empaquetando y publicando en GitHub...")
    subprocess.run(["git", "add", "."], cwd=str(dest_path), check=True)
    
    # Solo hacemos commit y push si realmente hay cambios tras el rsync
    status = subprocess.run(["git", "status", "--porcelain"], cwd=str(dest_path), capture_output=True, text=True)
    if status.stdout.strip():
        subprocess.run(["git", "commit", "-m", f"feat: release \"{version}\""], cwd=str(dest_path), check=True)
        subprocess.run(["git", "push"], cwd=str(dest_path), check=True)
        print(f"\n🎉 [Merci Release] ¡Publicación completa! La {version} está en la nube.")
    else:
        print(f"\n🎉 [Merci Release] El Boilerplate ya estaba actualizado con la {version}. No hay cambios que subir.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 [Merci Release] Operación cancelada por la usuaria. Saliendo limpiamente.")
        sys.exit(130)