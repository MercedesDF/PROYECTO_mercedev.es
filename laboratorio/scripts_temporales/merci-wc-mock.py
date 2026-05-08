#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TODO(Fase 4.3): Script experimental de inyección Headless Mock. 
# Usado para poblar la tienda WooCommerce con productos de prueba en local y validar estilos SASS sin pasar por la GUI de WP. 
# Mantenido como utilidad auxiliar/Art de Coté.

"""
merci-wc-mock.py — Inyector Headless de Productos para WooCommerce.
Lee el .env de forma segura y envía un payload JSON a la API REST de WC.
"""
import os
import json
import urllib.request
import base64
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
ENV_PATH = REPO_ROOT / ".env"

def inyectar_producto():
    print("🚀 [Merci WC Mock] Iniciando inyector Headless...")
    
    if not ENV_PATH.exists():
        print("❌ Error: No se encontró el archivo .env seguro.")
        return
        
    # Extraer credenciales ingenuamente
    env_data = {}
    for linea in ENV_PATH.read_text(encoding="utf-8").splitlines():
        if "=" in linea and not linea.startswith("#"):
            clave, valor = linea.split("=", 1)
            env_data[clave.strip()] = valor.strip().strip('"').strip("'")
            
    wp_url = env_data.get("WP_URL", "").rstrip('/')
    
    # QUÉ HACE: Amputa el subdirectorio de WP para encontrar la raíz del dominio estático.
    domain_root = wp_url.removesuffix('/blog')
    
    wp_user = env_data.get("WP_USER", "")
    wp_app_password = env_data.get("WP_APP_PASSWORD", "")
    
    endpoint = f"{wp_url}/wp-json/wc/v3/products"
    
    payload = {
        "name": "Camiseta Mercí en la nube",
        "type": "simple",
        "regular_price": "25.00",
        "description": "Nuestra simpática asistente en su nube.",
        "short_description": "La prenda oficial del ecosistema Merci en la nube.",
        "status": "publish",
        "images": [
            {
                # URL absoluta de la imagen ya optimizada por merci-optimizer
                "src": f"{domain_root}/assets/images/camiseta-mercienlanube.webp"
            }
        ]
    }
    
    data = json.dumps(payload).encode("utf-8")
    auth_b64 = base64.b64encode(f"{wp_user}:{wp_app_password}".encode("utf-8")).decode("utf-8")
    
    req = urllib.request.Request(endpoint, data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", f"Basic {auth_b64}")
    
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 201:
                res = json.loads(response.read().decode("utf-8"))
                print(f"✅ ¡Éxito! Producto inyectado con ID: {res.get('id')}")
                print("🌐 Abre tu navegador y recarga la página de la tienda.")
    except urllib.error.HTTPError as e:
        print(f"❌ Error HTTP {e.code}: {e.read().decode('utf-8')}")
    except Exception as e:
        print(f"❌ Error de conexión: {e}")

if __name__ == "__main__":
    inyectar_producto()