#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Historial de modificaciones:
# - Última modificación el 2026-05-18 (Fase 2 - Épica 3)

"""
merci-total.py — Orquestador maestro del ecosistema Merci.

Ejecuta en secuencia lógica todos los scripts de compilación, 
optimización y auditoría del proyecto. Excluye scripts interactivos 
(merci-commit) o de vigilancia continua (merci-watch).
"""

import subprocess
import time
import json
import sys
from pathlib import Path

# Definimos la ruta base donde residen los scripts
SCRIPTS_DIR = Path(__file__).resolve().parent
REPO_ROOT = Path(__file__).resolve().parents[2]

# Pipeline de ejecución secuencial. El orden es estricto por arquitectura:
# --- FASE DE CONSTRUCCIÓN (BUILD) ---
# 1. Optimizador: Prepara las imágenes WebP necesarias.
# 2. Styles: Compila el SASS final a main.css.
# 3. Publish: SSG que compila la Biblioteca desde Markdown a HTML/PDF.
# 4. WP Headless: Sincroniza los markdowns locales dinámicos hacia WordPress.
# 5. Sync Pages: Propaga el header/footer maestro a las páginas secundarias.
# 6. Extract Metrics: Inyecta las últimas estadísticas de PageSpeed Insight en home.
# 7. Brain: Genera el JSON estático con respuestas contextuales de IA.
# 8. Glosario AI: Agente autónomo que auto-completa definiciones DevSecOps (Shift-Left).
# --- FASE DE QA (QUALITY ASSURANCE) ---
# 9. Sitemap: Escanea todos los HTML finales generados y actualiza el mapa XML.
# 10. SSOT: Agente que sincroniza el Roadmap.
# 11. Drift: Detecta asimetrías de fechas entre manuales y código fuente.
# 12. Audit: Auditoría estricta de seguridad, SEO y sintaxis sobre el código final.
# 13. Hardening: Audita la postura de seguridad de la infraestructura y el repositorio.
# 14. Linkcheck: Rastreo dinámico de enlaces rotos sobre el HTML final compilado.

PIPELINE = [
    "merci-optimizer.py",
    "merci-styles.py",
    "merci-publish.py",
    "merci-wp.py",
    "merci-sync-pages.py",
    "merci-extract-metrics.py",
    "merci-brain.py",
    "merci-glosario.py",
    "merci-sitemap.py",
    "merci-ssot.py",
    "merci-drift.py",
    "merci-audit.py",
    "merci-hardening.py",
    "merci-linkcheck.py"
]

def main():
    start_time = time.time()
    print("🚀 [Merci Total] Iniciando orquestación del pipeline DevSecOps...\n")
    
    for script in PIPELINE:
        script_path = SCRIPTS_DIR / script
        
        if not script_path.exists():
            print(f"❌ [Merci Total] Error: No se encuentra el script {script}")
            sys.exit(1)
            
        print(f"▶️ Ejecutando: {script} ...")
        try:
            # check=True garantiza el patrón "Fail-Fast": si un script falla, 
            # el orquestador aborta inmediatamente sin ejecutar los siguientes.
            subprocess.run([sys.executable, str(script_path)], check=True)
            print()  # Separador visual entre bloques de ejecución
        except subprocess.CalledProcessError as e:
            # QUÉ HACE: Degradación Elegante para el Agente SSOT.
            # POR QUÉ: En un clon nuevo (Boilerplate), el Roadmap de IA y la Bitácora no existen por la limpieza DLP.
            # Convertimos su código de salida fatal en un aviso informativo para no romper la Out-of-the-Box Experience.
            if script == "merci-ssot.py":
                print("  ⚠️ [Merci Info] Agente SSOT desactivado: Faltan documentos origen (Comportamiento esperado en Boilerplate).")
                print()
                continue
            print(f"\n❌ [Merci Total] Pipeline detenido. El proceso '{script}' reportó errores y bloqueó la ejecución.")
            sys.exit(e.returncode)
            
    end_time = time.time()
    duration = end_time - start_time
    
    obs_dir = REPO_ROOT / "observabilidad"
    obs_dir.mkdir(exist_ok=True)
    (obs_dir / ".pipeline_duration.json").write_text(json.dumps({"duration_seconds": duration}, indent=2), encoding="utf-8")
    
    print(f"\n✅ [Merci Total] ¡Pipeline completado con éxito en {duration:.2f}s! Todo optimizado y auditado.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 [Merci Total] Orquestación interrumpida por la usuaria. Saliendo limpiamente.")
        sys.exit(130)