#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
merci-ssot.py — Agente Sync SSOT (Fase 3).

Objetivo: Analiza las últimas entradas de la bitácora activa y verifica si el 
ROADMAP-AI-ORQUESTACION-SELF-HEALING-SYSTEM.md necesita ser actualizado 
(marcar tareas como completadas [x] o deprecadas). Si detecta deriva documental, 
auto-sana el archivo del Roadmap reescribiéndolo automáticamente.
"""

import sys
from pathlib import Path
import warnings
import json
import urllib.request
import re

warnings.filterwarnings("ignore", category=FutureWarning)

try:
    from litellm import completion
    import litellm
    litellm.telemetry = False
except ImportError:
    print("ℹ️ [Merci SSOT] LiteLLM no está instalado. Omitiendo agente SSOT.")
    sys.exit(0)

REPO_ROOT = Path(__file__).resolve().parents[2]
ENV_PATH = REPO_ROOT / ".env"
ROADMAP_PATH = REPO_ROOT / "laboratorio" / "ROADMAP-AI-ORQUESTACION-SELF-HEALING-SYSTEM.md"
BITACORA_PATH = REPO_ROOT / "laboratorio" / "bitacora-mercedev-orquestacion-ia.md"

def cargar_api_key():
    if not ENV_PATH.exists():
        return None
    for linea in ENV_PATH.read_text(encoding="utf-8").splitlines():
        if linea.startswith("GEMINI_API_KEY="):
            return linea.split("=", 1)[1].strip().strip('"\'')
    return None

def auto_descubrir_modelo(api_key):
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode("utf-8"))
            validos = [m["name"].split("/")[-1] for m in data.get("models", []) if "generateContent" in m.get("supportedGenerationMethods", []) and "gemini" in m.get("name", "").lower()]
            for familia in ["1.5-flash", "1.5-pro"]:
                for v in validos:
                    if familia in v: return v
            return "gemini-1.5-flash"
    except Exception:
        return "gemini-1.5-flash"

def clean_markdown(text: str) -> str:
    """Limpia el código de salida de la IA para que sea Markdown puro."""
    # Buscar el inicio real del Markdown y amputar la basura conversacional
    inicio_md = text.find("# ")
    if inicio_md != -1:
        text = text[inicio_md:]
        
    text = text.strip()
    if text.startswith("```markdown"):
        text = text[11:]
    elif text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    return text.strip() + "\n"

def main():
    print("\n🤖 [Merci SSOT] Analizando deriva documental entre Bitácora y Roadmap...")
    
    if not ROADMAP_PATH.exists() or not BITACORA_PATH.exists():
        print("  ❌ [Merci Error] No se encuentra el Roadmap o la Bitácora de IA.")
        return

    roadmap_content = ROADMAP_PATH.read_text(encoding="utf-8")
    bitacora_full = BITACORA_PATH.read_text(encoding="utf-8")
    
    # Extraer solo las 2 últimas entradas de la bitácora para proteger la ventana de contexto local (LM Studio)
    entradas = re.split(r'(?=### \d{4}-\d{2}-\d{2})', bitacora_full)
    bitacora_reciente = "".join(entradas[1:3]) if len(entradas) > 1 else bitacora_full[:2000]

    system_prompt = """Eres el Agente SSOT (Single Source of Truth) de un ecosistema DevSecOps.
Tu objetivo es evitar la Deriva Documental (Document Drift).
Recibirás las últimas entradas de la Bitácora y el estado actual del Roadmap en Markdown.

REGLAS INNEGOCIABLES:
1. Evalúa si los hitos logrados en la Bitácora corresponden a tareas no marcadas (- [ ]) en el Roadmap.
2. Si un agente o tarea fue completado o DEPRECADO (movido a Art de Coté), cambia su estado a `- [x]` en el Roadmap. (Ej: `- [x] Agente Bibliotecario (Deprecado a Art de Coté)`).
3. Devuelve ÚNICA Y EXCLUSIVAMENTE el código Markdown completo del Roadmap actualizado. COPIA EL ROADMAP ORIGINAL DE PRINCIPIO A FIN Y APLICA TUS CAMBIOS. NO RESUMAS.
PROHIBIDO usar frases como "Here is the updated roadmap" o "After evaluating...". 
TU RESPUESTA DEBE EMPEZAR CON EL SÍMBOLO "# " DEL TÍTULO DEL ROADMAP Y TERMINAR CON LA ÚLTIMA LÍNEA DEL MISMO.
4. NO uses cadenas de pensamiento (Chain of Thought) ni expliques tu razonamiento. Devuelve DIRECTAMENTE el código Markdown final."""

    prompt = f"--- ESTADO ACTUAL DEL ROADMAP ---\n{roadmap_content}\n\n--- ÚLTIMAS ENTRADAS BITÁCORA ---\n{bitacora_reciente}"

    api_key = cargar_api_key()
    if not api_key:
        print("  ⚠️ [Merci Warn] Falta GEMINI_API_KEY. Abortando SSOT.")
        return

    modelo_activo = auto_descubrir_modelo(api_key)
    print(f"  🧠 Consultando a {modelo_activo}...")
    
    try:
        respuesta = completion(
            model=f"gemini/{modelo_activo}",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            api_key=api_key,
            temperature=0.0,
            max_tokens=2500,
            timeout=600
        )
    except Exception as e_cloud:
        print(f"  ❌ [Merci Error] Falló Gemini y el agente SSOT requiere la nube para tareas complejas. Detalle: {e_cloud}")
        return
            
    try:
        raw_response = respuesta.choices[0].message.content
        nuevo_roadmap = clean_markdown(raw_response)
        
        # SONDA DE DEPURACIÓN: Guardar la respuesta cruda antes de que actúe el escudo
        debug_path = REPO_ROOT / "laboratorio" / "DEBUG-ROADMAP.md"
        debug_path.write_text(raw_response, encoding="utf-8")
        print(f"  🐞 [Merci Debug] Salida cruda de la IA guardada en: {debug_path.relative_to(REPO_ROOT)}")
        
        # ESCUDO ANTI-ALUCINACIONES (Sanity Checks)
        if len(nuevo_roadmap) < len(roadmap_content) * 0.5:
            print("  ❌ [Merci Error] La IA devolvió un resumen en lugar del documento completo. Destrucción evitada.")
            return
        if "# " not in nuevo_roadmap:
            print("  ❌ [Merci Error] La IA no devolvió un formato Markdown válido. Destrucción evitada.")
            return
        
        if nuevo_roadmap.strip() != roadmap_content.strip():
            ROADMAP_PATH.write_text(nuevo_roadmap, encoding="utf-8")
            print("  ✅ [Éxito] Deriva documental sanada. Roadmap reescrito automáticamente.")
        else:
            print("  ✅ [Éxito] El Roadmap ya está perfectamente sincronizado.")
            
    except Exception as e:
        print(f"  ❌ [Merci Error] Fallo procesando la respuesta de la IA: {e}")

if __name__ == "__main__":
    main()