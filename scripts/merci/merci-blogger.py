#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
merci-blogger.py — Agente Redactor DevRel (Fase 1: Motor de Difusión).
Transforma notas crudas en artículos atractivos para el blog y
redacta el anuncio para LinkedIn, dejándolo "en_cola" para la difusión asíncrona.
"""

import sys
import re
from datetime import datetime
from pathlib import Path

try:
    from litellm import completion
    import litellm
    litellm.telemetry = False
    litellm.suppress_debug_info = True
except ImportError:
    print("❌ [Merci Blogger] Falta 'litellm'. Instálalo con: pip install litellm")
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parents[2]
PROMPT_PATH = REPO_ROOT / "laboratorio" / "prompts" / "prompt-blogger.md"
NOTAS_DIR = REPO_ROOT / "laboratorio" / "notas_rapidas"
INCUBACION_DIR = REPO_ROOT / "laboratorio" / "incubacion"

def slugify(texto: str) -> str:
    import unicodedata
    texto = str(texto)
    texto = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('ascii')
    texto = re.sub(r'[^\w\s-]', '', texto.lower())
    return re.sub(r'[-\s]+', '-', texto).strip('-_')

def main():
    print("✍️  [Merci Blogger] Iniciando Agente Redactor de Marketing...")
    
    if not PROMPT_PATH.exists():
        print(f"❌ Error: No se encuentra el cerebro del agente en {PROMPT_PATH.name}")
        sys.exit(1)
        
    system_prompt = PROMPT_PATH.read_text(encoding="utf-8")
    system_prompt = system_prompt.replace("{fecha}", datetime.now().strftime("%Y-%m-%d"))
    
    NOTAS_DIR.mkdir(parents=True, exist_ok=True)
    INCUBACION_DIR.mkdir(parents=True, exist_ok=True)
    
    # QUÉ HACE: Filtra notas ignorando el .gitkeep y la carpeta de procesadas.
    notas = [f for f in NOTAS_DIR.glob("*") if f.is_file() and f.name != ".gitkeep"]
    if not notas:
        print(f"  🤷‍♀️ No hay notas crudas en {NOTAS_DIR.relative_to(REPO_ROOT)}. ¡Escribe algo primero!")
        sys.exit(0)
        
    print("\n  📄 Notas crudas disponibles:")
    for i, nota in enumerate(notas, 1):
        print(f"    {i}. {nota.name}")
        
    try:
        seleccion = int(input("\n  👉 Elige el número de la nota a procesar (0 para salir): ").strip())
        if seleccion == 0: return
        nota_elegida = notas[seleccion - 1]
    except (ValueError, IndexError):
        print("  ❌ Selección inválida.")
        sys.exit(1)
        
    nota_contenido = nota_elegida.read_text(encoding="utf-8")
    if not nota_contenido.strip():
        print("  ❌ La nota está vacía.")
        sys.exit(1)
        
    print(f"\n  🧠 Redactando artículo a partir de '{nota_elegida.name}'...")
    
    print("  🏠 Consultando a motor local (Ollama - qwen2.5-coder)...")
    try:
        respuesta = completion(
            model="ollama/qwen2.5-coder",
            api_base="http://localhost:11434",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": nota_contenido}
            ],
            temperature=0.6,
            max_tokens=3000
        )
        respuesta_texto = respuesta.choices[0].message.content
    except Exception as e:
        print(f"  ❌ Error en motor local: {e}")
        sys.exit(1)
            
    # Limpieza de bloque de código Markdown residual
    if respuesta_texto.startswith("```markdown"):
        respuesta_texto = respuesta_texto[11:]
    if respuesta_texto.endswith("```"):
        respuesta_texto = respuesta_texto[:-3]
    respuesta_texto = respuesta_texto.strip()
    
    # Autonombrado (Slugify)
    titulo_match = re.search(r'^titulo:\s*["\']?([^"\'\n]+)["\']?', respuesta_texto, re.MULTILINE)
    titulo = titulo_match.group(1) if titulo_match else "articulo-generado"
    filename = slugify(titulo) + ".md"
    
    out_path = INCUBACION_DIR / filename
    out_path.write_text(respuesta_texto, encoding="utf-8")
    
    # Archivar la nota cruda para que no vuelva a molestar
    archivo_dir = NOTAS_DIR / "_procesadas"
    archivo_dir.mkdir(exist_ok=True)
    nota_elegida.rename(archivo_dir / nota_elegida.name)
    
    print(f"\n  ✅ ¡Artículo redactado con éxito y post encolado!")
    print(f"  📁 Guardado en: {out_path.relative_to(REPO_ROOT)}")
    print(f"  🧹 Nota original movida a: {archivo_dir.relative_to(REPO_ROOT)}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n  🛑 Cancelado por el usuario.")