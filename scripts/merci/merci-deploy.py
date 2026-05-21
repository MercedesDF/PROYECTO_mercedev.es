#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
merci-deploy.py — Agente de Despliegue Remoto (Continuous Deployment Local).
Conecta por SSH al servidor de producción, sincroniza el código fuente
y purga la caché de Varnish automáticamente.
"""

import subprocess
import sys

# Configuración del entorno de producción
SSH_USER = "mercedev-php"
SSH_HOST = "mercedev.es"
REMOTE_WEB_DIR = "~/htdocs/mercedev.es"
REMOTE_WP_DIR = "~/htdocs/wordpress"

def run_remote_command(command, description):
    print(f"  {description}")
    # Se asume que las claves SSH están configuradas (sin contraseña interactiva)
    ssh_cmd = ["ssh", f"{SSH_USER}@{SSH_HOST}", command]
    result = subprocess.run(ssh_cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"    ❌ Error: {result.stderr.strip()}")
        return False
        
    print("    ✅ Hecho.")
    return True

def main():
    print("🚀 [Merci Deploy] Iniciando orquestación de despliegue en producción...")

    if not run_remote_command(f"cd {REMOTE_WEB_DIR} && git pull origin main", "📥 Sincronizando código desde GitHub (git pull)..."):
        sys.exit(1)

    run_remote_command(f"cd {REMOTE_WP_DIR} && wp varnish purge", "🧹 Purgando caché de Varnish en la memoria RAM...")
    print("\n🎉 ¡Despliegue completado! La producción está actualizada y la caché es fresca.")

if __name__ == "__main__":
    main()