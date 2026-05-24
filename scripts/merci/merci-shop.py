#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
merci-shop.py — Orquestador Headless para WooCommerce (Mock E-commerce).
Lee los archivos Markdown de laboratorio/tienda/ y los sincroniza
con la API REST de WooCommerce usando autenticación segura.
"""

import os
import sys
import json
import base64
import urllib.request
import urllib.error
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TIENDA_DIR = REPO_ROOT / "laboratorio" / "tienda"
ENV_PATH = REPO_ROOT / ".env"

def cargar_credenciales() -> tuple[str, str]:
    """
    QUÉ HACE: Lee el .env local y genera el token de Autenticación Básica.
    POR QUÉ: Evita tener credenciales hardcodeadas (quemadas) en el código,
    respetando el principio Zero Trust y la seguridad Shift-Left.
    """
    if not ENV_PATH.exists():
        print("❌ No se encontró el archivo .env")
        sys.exit(1)
        
    env_vars = {}
    for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"): continue
        if "=" in line:
            key, val = line.split("=", 1)
            env_vars[key.strip()] = val.strip().strip("'\"")
            
    wp_url = env_vars.get("WP_URL", "").rstrip("/")
    wp_user = env_vars.get("WP_USER", "")
    wp_pass = env_vars.get("WP_APP_PASSWORD", "")
    
    if not wp_url or not wp_user or not wp_pass:
        print("❌ Faltan credenciales (WP_URL, WP_USER, WP_APP_PASSWORD) en el .env")
        sys.exit(1)
        
    credenciales = f"{wp_user}:{wp_pass}"
    auth_b64 = base64.b64encode(credenciales.encode("utf-8")).decode("utf-8")
    return wp_url, f"Basic {auth_b64}"

def realizar_peticion_wc(url: str, auth_header: str, method: str = "GET", data: dict | None = None) -> dict | None:
    """
    QUÉ HACE: Ejecuta peticiones HTTP a la API REST de WooCommerce (v3).
    POR QUÉ: Usa X-Authorization para eludir la ceguera de proxy de Varnish/Nginx
    y un User-Agent corporativo para evitar bloqueos por WAF.
    """
    headers = {
        "Authorization": auth_header,
        "X-Authorization": auth_header,
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Merci-Boilerplate-Agent/1.0"
    }
    
    payload = json.dumps(data).encode("utf-8") if data else None
    req = urllib.request.Request(url, data=payload, method=method, headers=headers)
    
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"  ❌ Error HTTP {e.code}: {error_body}")
        return None
    except Exception as e:
        print(f"  ❌ Error de conexión: {e}")
        return None

def main():
    print("\n🛒 [Merci Shop] Iniciando Orquestador Headless de WooCommerce...")
    
    wp_url, auth_header = cargar_credenciales()
    wc_endpoint = f"{wp_url}/wp-json/wc/v3/products"
    
    print(f"  🔗 Conectando a WooCommerce en: {wp_url}")
    
    # Health Check: Intentamos traer solo 1 producto para validar credenciales
    respuesta = realizar_peticion_wc(f"{wc_endpoint}?per_page=1", auth_header)
    
    if respuesta is not None:
        print("  ✅ Conexión exitosa. Autenticación verificada.")
    else:
        print("  🛑 Falló la validación de credenciales o el endpoint es inaccesible.")
        sys.exit(1)
        
    # Aseguramos que la estantería del catálogo exista para futuros pasos
    TIENDA_DIR.mkdir(parents=True, exist_ok=True)
    print("\n  [TODO] Siguiente paso: Parsear YAML de laboratorio/tienda/*.md y sincronizar el catálogo.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[Merci Shop] Interrumpido por el usuario.")
        sys.exit(130)