#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
merci-deploy.py — Agente de Despliegue Remoto (Continuous Deployment Local).
Conecta por SSH al servidor de producción, sincroniza el código fuente
y purga la caché de Varnish automáticamente.
"""

import os
import subprocess
import sys
from pathlib import Path

# Configuración del entorno de producción
SSH_USER = "mercedev-php"
SSH_HOST = "mercedev.es"
REMOTE_WEB_DIR = "~/htdocs/mercedev.es"
REMOTE_WP_DIR = "~/htdocs/wordpress"
REPO_ROOT = Path(__file__).resolve().parents[2]

def run_local_command(command: str, description: str, custom_env: dict[str, str] | None = None) -> bool:
    """
    QUÉ HACE: Ejecuta un comando en la shell del sistema local.
    POR QUÉ: Centraliza la subida de código o la inyección de contenidos controlando el código de retorno.
    """
    print(f"  {description}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True, env=custom_env)
    
    if result.returncode != 0:
        print(f"    ❌ Error: {result.stderr.strip()}")
        return False
        
    print("    ✅ Hecho.")
    return True

def run_remote_command(command: str, description: str) -> bool:
    """
    QUÉ HACE: Ejecuta un comando remoto a través de una conexión SSH sin interacción.
    POR QUÉ: Permite automatizar la actualización y purga de caché en el VPS de producción.
    """
    print(f"  {description}")
    # Se asume que las claves SSH están configuradas (sin contraseña interactiva)
    ssh_cmd = ["ssh", "-o", "StrictHostKeyChecking=accept-new", f"{SSH_USER}@{SSH_HOST}", command]
    result = subprocess.run(ssh_cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"    ❌ Error: {result.stderr.strip()}")
        return False
        
    print("    ✅ Hecho.")
    return True

def main() -> None:
    """
    QUÉ HACE: Orquesta el flujo de despliegue continuo subiendo el código a Git, tirándolo en producción y purgando la caché de Varnish.
    POR QUÉ: Provee un mecanismo automatizado de despliegue de un solo paso libre de plugins.
    """
    print("🚀 [Merci Deploy] Iniciando orquestación de despliegue en producción...")

    if not run_local_command("git push origin main", "📤 Subiendo código local a GitHub (git push)..."):
        sys.exit(1)

    if not run_remote_command(f"cd {REMOTE_WEB_DIR} && git pull origin main", "📥 Sincronizando código desde GitHub (git pull)..."):
        sys.exit(1)

    # Sincronización Headless WP en Producción (Evita editar .env a mano)
    env_path = REPO_ROOT / ".env"
    if env_path.exists():
        env_data = {}
        for line in env_path.read_text(encoding="utf-8").splitlines():
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                env_data[k.strip()] = v.strip().strip('"').strip("'")
        
        prod_url = env_data.get("WP_PROD_URL")
        prod_user = env_data.get("WP_PROD_USER")
        prod_pass = env_data.get("WP_PROD_APP_PASSWORD")
        
        if prod_url and prod_user and prod_pass:
            print("\n  🌐 Detectadas credenciales de producción para WordPress.")
            custom_env = os.environ.copy()
            custom_env["WP_URL"] = prod_url
            custom_env["WP_USER"] = prod_user
            custom_env["WP_APP_PASSWORD"] = prod_pass
            if not run_local_command(f"{sys.executable} {REPO_ROOT}/scripts/merci/merci-wp.py", "📦 Inyectando artículos Headless en CMS de producción...", custom_env):
                print("  ⚠️ La sincronización de WP falló. Continuando con el despliegue estático...")
            else:
                run_local_command(f"{sys.executable} {REPO_ROOT}/scripts/merci/merci-shop.py", "🛒 Inyectando catálogo de tienda en WooCommerce de producción...", custom_env)

    # Purgar la caché enviando peticiones HTTP PURGE locales desde el propio servidor.
    run_remote_command(f"curl -s -X PURGE https://{SSH_HOST}/ > /dev/null", "🧹 Purgando caché de la portada (Varnish)...")
    run_remote_command(f"curl -s -X PURGE https://{SSH_HOST}/blog/ > /dev/null", "🧹 Purgando caché del blog (Varnish)...")
    
    print("\n🎉 ¡Despliegue completado! La producción está actualizada y la caché es fresca (Zero-Plugins).")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 [Merci Deploy] Despliegue cancelado por la usuaria. Saliendo limpiamente.")
        sys.exit(130)
    except Exception as e:
        print(f"❌ [Merci Deploy] Error fatal inesperado: {e}")
        sys.exit(1)