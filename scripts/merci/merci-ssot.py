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
    litellm.suppress_debug_info = True
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
    inicio_md = text.find("# 🗺️ ROADMAP")
    if inicio_md == -1:
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
    
    # Extraer solo las últimas 2 entradas de la bitácora para ser precisos y evitar diluir el prompt
    entradas = re.split(r'(?=### \d{4}-\d{2}-\d{2})', bitacora_full)
    bitacora_reciente = "".join(entradas[1:3]) if len(entradas) > 1 else bitacora_full[:2000]

    system_prompt = """Eres el Agente SSOT de un ecosistema DevSecOps.
Tu misión es actualizar el ROADMAP basándote en los últimos avances de la BITÁCORA.

INSTRUCCIONES DE RAZONAMIENTO PREVIO (Piensa paso a paso):
1. Analiza los bloques "Hecho" o "Contexto" de la Bitácora.
2. Busca qué tareas pendientes `- [ ]` del Roadmap se corresponden con esos hechos (algo descartado o relegado a cloud también se considera completado).
3. Escribe en texto plano qué tareas vas a actualizar de `[ ]` a `[x]`. Si se menciona un círculo rojo en la bitácora, añade 🔴.

INSTRUCCIONES DE SALIDA:
Tras tu razonamiento, imprime todo el código del Roadmap actualizado.
DEBES REESCRIBIR EL ROADMAP ENTERO DE PRINCIPIO A FIN.
ASEGÚRATE de haber cambiado físicamente los `- [ ]` por `- [x]` en las líneas que detectaste. ¡NO actúes como una fotocopiadora ciega, aplica los cambios!"""

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
            max_tokens=4000,
            timeout=600
        )
    except Exception as e_cloud:
        print(f"  ⚠️ [Merci Warn] Falló Gemini ({e_cloud}). Intentando Fallback local con Ollama (qwen2.5-coder)...")
        try:
            respuesta = completion(
                model="ollama/qwen2.5-coder",
                api_base="http://localhost:11434",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.0,
                max_tokens=4000,
                timeout=600
            )
        except Exception as e_local:
            print(f"  ❌ [Merci Error] Falló también el motor local de Ollama. Detalle: {e_local}")
            return
            
    try:
        raw_response = respuesta.choices[0].message.content
        nuevo_roadmap = clean_markdown(raw_response)
        
        # ESCUDO ANTI-ALUCINACIONES (Sanity Checks)
        if len(nuevo_roadmap) < len(roadmap_content) * 0.5:
            print("  ❌ [Merci Error] La IA devolvió un resumen en lugar del documento completo. Destrucción evitada.")
            return
        if "# " not in nuevo_roadmap:
            print("  ❌ [Merci Error] La IA no devolvió un formato Markdown válido. Destrucción evitada.")
            return
        
        if nuevo_roadmap.strip() != roadmap_content.strip():
            # Identificar qué fases han sido actualizadas comparando líneas
            old_lines = roadmap_content.strip().splitlines()
            new_lines = nuevo_roadmap.strip().splitlines()
            fases_modificadas = set()
            fase_actual = "Fase General"
            
            for i, new_line in enumerate(new_lines):
                if new_line.startswith("## "):
                    fase_actual = new_line.replace("##", "").strip()
                if i >= len(old_lines) or new_line != old_lines[i]:
                    fases_modificadas.add(fase_actual)
                    
            ROADMAP_PATH.write_text(nuevo_roadmap, encoding="utf-8")
            print("  ✅ [Éxito] Deriva documental sanada. Roadmap reescrito automáticamente.")
            if fases_modificadas:
                print(f"  🗺️  Avance registrado en: {', '.join(fases_modificadas)}")
        else:
            print("  ℹ️ [Merci Info] Sin avances en roadmap-ai. Ya está perfectamente sincronizado.")
            
    except Exception as e:
        print(f"  ❌ [Merci Error] Fallo procesando la respuesta de la IA: {e}")

if __name__ == "__main__":
    main()