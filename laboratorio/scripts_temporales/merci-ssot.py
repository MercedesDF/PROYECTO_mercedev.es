#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
merci-ssot.py — Agente Sync SSOT (Fase 3).

Objetivo: Analiza las últimas entradas de la bitácora activa y verifica si el 
ROADMAP.md (Roadmap Maestro) necesita ser actualizado 
(marcar tareas como completadas [x] o deprecadas). Si detecta deriva documental, 
auto-sana el archivo del Roadmap reescribiéndolo automáticamente.
"""

import json
import logging
import os
import re
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", category=FutureWarning)

try:
    os.environ["LITELLM_LOCAL_MODEL_COST_MAP"] = "True"
    logging.getLogger('LiteLLM').setLevel(logging.ERROR)
    from litellm import completion
    import litellm
    litellm.telemetry = False
    litellm.suppress_debug_info = True
except ImportError:
    print("ℹ️ [Merci SSOT] LiteLLM no está instalado. Omitiendo agente SSOT.")
    sys.exit(0)

REPO_ROOT = Path(__file__).resolve().parents[2]
ROADMAP_PATH = REPO_ROOT / "ROADMAP.md"
PROMPT_PATH = REPO_ROOT / "laboratorio" / "prompts" / "prompt-ssot.md"

def obtener_bitacora_activa() -> Path | None:
    """
    QUÉ HACE: Busca dinámicamente la bitácora más reciente en el laboratorio.
    POR QUÉ: Determina de forma autónoma cuál es el frente de trabajo activo y de dónde extraer metadatos.
    """
    bitacoras = list((REPO_ROOT / "laboratorio").glob("bitacora-mercedev-epic-*.md"))
    if not bitacoras:
        return None
    return max(bitacoras, key=lambda p: p.stat().st_mtime)

def extract_json_array(text: str) -> list[str]:
    """
    QUÉ HACE: Extrae un array JSON de la respuesta de la IA, ignorando texto basura.
    POR QUÉ: Permite limpiar la salida de los modelos de lenguaje que inyectan explicaciones adicionales.
    """
    match = re.search(r'\[.*?\]', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(0))
        except json.JSONDecodeError:
            pass
    return []

def main() -> None:
    """
    QUÉ HACE: Analiza las últimas entradas de la bitácora activa y verifica si el ROADMAP.md necesita ser actualizado.
    POR QUÉ: Corrige la deriva documental sincronizando el estado real del proyecto con la Única Fuente de Verdad.
    """
    print("\n🤖 [Merci SSOT] Analizando deriva documental entre Bitácora y Roadmap...")
    
    BITACORA_PATH = obtener_bitacora_activa()
    if not ROADMAP_PATH.exists() or not BITACORA_PATH:
        print("  ❌ [Merci Error] No se encuentra el Roadmap o la Bitácora de IA.")
        sys.exit(1)

    roadmap_content = ROADMAP_PATH.read_text(encoding="utf-8")
    bitacora_full = BITACORA_PATH.read_text(encoding="utf-8")
    
    # Extraer estrictamente las tareas pendientes del roadmap
    pending_tasks = re.findall(r'- \[\s*\] (.*)', roadmap_content)
    if not pending_tasks:
        print("  ℹ️ [Merci Info] No hay tareas pendientes en el Roadmap. Ya está 100% completado.")
        return
    pending_list_str = "\n".join([f"- {t}" for t in pending_tasks])

    # Extraer solo las últimas 2 entradas de la bitácora para ser precisos y evitar diluir el prompt
    entradas = re.split(r'(?=### \d{4}-\d{2}-\d{2}(?:\s\d{2}:\d{2})?)', bitacora_full)
    bitacora_reciente = "".join(entradas[1:3]) if len(entradas) > 1 else bitacora_full[:2000]

    # QUÉ HACE: Amputa matemáticamente todo el texto de la bitácora excepto el bloque "Hecho".
    # POR QUÉ: Previene la alucinación inercial. Si la IA no lee el bloque "Siguiente paso", es imposible que asuma tareas futuras como completadas.
    hechos = re.findall(r'\*\*Hecho:\*\*(.*?)(?=\*\*Detalle técnico:|\*\*Motivo / criterio:|\*\*Siguiente paso o deuda:|### |$)', bitacora_reciente, re.DOTALL)
    bitacora_filtrada = "\n".join([h.strip() for h in hechos]) if hechos else "No hay acciones registradas."

    if not PROMPT_PATH.exists():
        print("  ❌ [Merci Error] Falta el archivo rector: prompt-ssot.md")
        sys.exit(1)
    system_prompt = PROMPT_PATH.read_text(encoding="utf-8")

    prompt = f"--- ÚLTIMOS HECHOS EXTRAÍDOS ---\n{bitacora_filtrada}\n\n--- TAREAS PENDIENTES ---\n{pending_list_str}"

    print("  🏠 Consultando a motor en la nube (Antigravity Proxy - Gemini Flash)...")
    
    try:
        respuesta = completion(
            model="openai/gemini-2.5-flash",
            api_base="http://localhost:4000",
            api_key="sk-antigravity",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.0,
            max_tokens=4000
        )
        raw_response = respuesta.choices[0].message.content
    except Exception as e_proxy:
        print(f"  ❌ [Merci Error] Falló el enrutador LiteLLM Proxy. Detalle: {e_proxy}")
        sys.exit(1)

    try:
        tareas_completadas = extract_json_array(raw_response)

        if not tareas_completadas:
            print("  ℹ️ [Merci Info] Sin avances en el Roadmap Maestro. Ya está perfectamente sincronizado.")
            return

        nuevo_roadmap = roadmap_content
        cambios_aplicados = 0
        
        for tarea in tareas_completadas:
            pattern = re.compile(r'- \[\s*\] ' + re.escape(tarea))
            if pattern.search(nuevo_roadmap):
                nuevo_roadmap = pattern.sub(f"- [x] {tarea}", nuevo_roadmap)
                cambios_aplicados += 1
                
        if cambios_aplicados > 0:
            ROADMAP_PATH.write_text(nuevo_roadmap, encoding="utf-8")
            print(f"  ✅ [Éxito] Deriva documental sanada. {cambios_aplicados} tarea(s) marcada(s) como completada(s).")
        else:
            print("  ℹ️ [Merci Info] La IA sugirió tareas pero no hubo coincidencia exacta. Sin cambios.")
            
    except Exception as e:
        print(f"  ❌ [Merci Error] Fallo procesando la respuesta de la IA: {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 [Merci SSOT] Ejecución interrumpida por la usuaria. Saliendo limpiamente.")
        sys.exit(130)
    except Exception as e:
        print(f"❌ [Merci SSOT] Error fatal inesperado: {e}")
        sys.exit(1)