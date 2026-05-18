#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Historial de modificaciones:
# - Última modificación el 2026-05-18 (Fase 2 - Épica 3)

"""
merci-sre.py — Agente de Observabilidad y Métricas (Fase 4).
Expone el estado del ecosistema DevSecOps en el puerto 8001 para Prometheus.
"""

import time
import re
import json
from pathlib import Path
from prometheus_client import start_http_server, Gauge

REPO_ROOT = Path(__file__).resolve().parents[2]

# Declaración de métricas (Gauges: valores que pueden subir y bajar)
ROADMAP_TASKS = Gauge('merci_roadmap_tareas_total', 'Tareas del Roadmap', ['estado'])
DOCS_INCUBACION = Gauge('merci_documentos_incubacion_total', 'Borradores en incubación')
DOCS_PROMOCION = Gauge('merci_documentos_promocion_total', 'Documentos listos para promover (borrador)')
DOCS_BIBLIOTECA = Gauge('merci_documentos_biblioteca_total', 'Documentos publicados en biblioteca')
LINKEDIN_QUEUE = Gauge('merci_linkedin_queue_total', 'Publicaciones en cola para LinkedIn')
DOCUMENT_DRIFT = Gauge('merci_document_drift_total', 'Archivos con deriva documental')
PIPELINE_DURATION = Gauge('merci_pipeline_duration_seconds', 'Tiempo de ejecución de merci-total.py')

def actualizar_metricas_pipeline():
    """Lectura de JSON (Deriva y Duración). Se refrescan periódicamente (cada 10s)."""
    drift_path = REPO_ROOT / "observabilidad" / ".drift_report.json"
    if drift_path.exists():
        try:
            data = json.loads(drift_path.read_text(encoding="utf-8"))
            DOCUMENT_DRIFT.set(len(data))
        except Exception:
            pass

    duration_path = REPO_ROOT / "observabilidad" / ".pipeline_duration.json"
    if duration_path.exists():
        try:
            data = json.loads(duration_path.read_text(encoding="utf-8"))
            PIPELINE_DURATION.set(data.get("duration_seconds", 0.0))
        except Exception:
            pass

def actualizar_estado_documental():
    """Lectura de Markdown y YAML Frontmatter. Se refresca cada segundo para feedback instantáneo."""
    # 1. Analizar tareas del Roadmap
    roadmap_path = REPO_ROOT / "ROADMAP.md"
    if roadmap_path.exists():
        content = roadmap_path.read_text(encoding="utf-8")
        pendientes = len(re.findall(r'- \[\s*\] ', content))
        completadas = len(re.findall(r'- \[\s*[xX]\s*\] ', content))
        ROADMAP_TASKS.labels(estado="pendiente").set(pendientes)
        ROADMAP_TASKS.labels(estado="completada").set(completadas)

    # 2. Contar documentos por estado (incubación y promoción) mediante YAML Frontmatter
    laboratorio_dir = REPO_ROOT / "laboratorio"
    if laboratorio_dir.exists():
        en_incubacion = 0
        borradores = 0
        for md_file in laboratorio_dir.rglob("*.md"):
            # Excluir bitácoras para evitar falsos positivos
            if md_file.name.startswith("bitacora"):
                continue
            try:
                content = md_file.read_text(encoding="utf-8", errors="ignore")
                match = re.match(r"^\s*---\r?\n(.*?)\n---", content, re.DOTALL)
                if match:
                    if re.search(r'^estado:\s*["\']incubacion["\']', match.group(1), re.MULTILINE | re.IGNORECASE):
                        en_incubacion += 1
                    elif re.search(r'^estado:\s*["\']borrador["\']', match.group(1), re.MULTILINE | re.IGNORECASE):
                        borradores += 1
            except Exception:
                pass
        DOCS_INCUBACION.set(en_incubacion)
        DOCS_PROMOCION.set(borradores)

    # 3. Contar documentos en la biblioteca pública
    biblioteca_dir = REPO_ROOT / "biblioteca"
    if biblioteca_dir.exists():
        DOCS_BIBLIOTECA.set(len(list(biblioteca_dir.glob("*.md"))))

    # 4. Contar publicaciones en cola para LinkedIn
    directorios_sociales = [REPO_ROOT / "blog", REPO_ROOT / "art-de-cote", REPO_ROOT / "biblioteca"]
    en_cola_social = 0
    for dir_path in directorios_sociales:
        if dir_path.exists():
            for md_file in dir_path.rglob("*.md"):
                try:
                    content = md_file.read_text(encoding="utf-8", errors="ignore")
                    match = re.match(r"^\s*---\r?\n(.*?)\n---", content, re.DOTALL)
                    if match:
                        yaml_block = match.group(1)
                        # Solo contamos si está publicado y en cola
                        if re.search(r'^estado:\s*["\']publicado["\']', yaml_block, re.MULTILINE | re.IGNORECASE) and \
                           re.search(r'^estado_social:\s*["\'](en_cola|aprobado)["\']', yaml_block, re.MULTILINE | re.IGNORECASE):
                            en_cola_social += 1
                except Exception:
                    pass
    LINKEDIN_QUEUE.set(en_cola_social)

def main():
    puerto = 8001
    print(f"👁️  [Merci SRE] Iniciando Agente de Observabilidad en el puerto {puerto}...")
    start_http_server(puerto, addr="0.0.0.0")
    
    ticks = 0
    while True:
        # QUÉ HACE: Muestreo Escalonado orientado a la Experiencia de Autor (Author Experience).
        # POR QUÉ: Prioriza ver en tiempo real los cambios de estado (YAML) al usar merci-promote o merci-blogger.
        actualizar_estado_documental()
        
        if ticks % 10 == 0:
            actualizar_metricas_pipeline()
            
        ticks += 1
        time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👁️  [Merci SRE] Agente de Observabilidad detenido por el usuario. ¡Hasta la vista!")