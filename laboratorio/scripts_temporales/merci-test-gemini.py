#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
scripts/temporales/merci-test-gemini.py

QUÉ HACE: Script efímero de depuración utilizado para consultar la API de Google (Gemini)
          e iterar sobre varios nombres de modelos hasta encontrar el que es válido
          y aceptado por la versión de la API actual (v1beta).
POR QUÉ ESTÁ AQUÍ Y NO EN EL GENERAL: 
          Fue creado durante la Fase 4 de la Épica 9 (Chaos Engineering) cuando el Chaos Monkey
          descubrió que el Fallback a la nube fallaba. El proxy usaba 'gemini-1.5-flash', que 
          quedó obsoleto y empezó a arrojar errores 404 (NotFoundError). Este script nos permitió 
          descubrir que debíamos actualizar a 'gemini-2.5-flash'. Se preserva como herramienta de
          auditoría por si en el futuro la API vuelve a cambiar sus alias o versiones de modelo.
"""

import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
try:
    from litellm import completion
    import litellm
    litellm.telemetry = False
    litellm.suppress_debug_info = True

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        env_path = REPO_ROOT / ".env"
        if env_path.exists():
            for line in env_path.read_text(encoding="utf-8").splitlines():
                if line.startswith("GEMINI_API_KEY="):
                    api_key = line.split("=", 1)[1].strip("\"' \n\r")
                    os.environ["GEMINI_API_KEY"] = api_key
                    break
    
    print("API Key loaded?", bool(api_key))
    if api_key:
        print("API Key starts with:", api_key[:4])
    
    models_to_try = [
        "gemini/gemini-2.5-flash",
        "gemini/gemini-1.5-flash-latest",
        "gemini/gemini-1.5-pro",
        "gemini/gemini-pro"
    ]
    for model in models_to_try:
        try:
            respuesta = completion(
                model=model,
                messages=[{"role": "user", "content": "Hola"}],
                api_key=api_key,
                temperature=0.65
            )
            print("EXITO con el modelo:", model)
            print("Respuesta:", respuesta.choices[0].message.content)
            break
        except Exception as e:
            print("FALLO con el modelo:", model, "Error:", str(e))
except Exception as e:
    print("ERROR FATAL:", str(e))
