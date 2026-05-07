#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
try:
    from litellm import completion
except ImportError:
    print("❌ Error: LiteLLM no está instalado. Ejecuta: pip install -r requirements.txt")
    sys.exit(1)

print("🧠 Conectando con Ollama (Modelo local: phi3)...")
print("⏳ Esperando respuesta (latencia cero)...\n")

try:
    # QUÉ HACE: Usa la API estandarizada de LiteLLM para llamar a un modelo alojado en Ollama.
    # POR QUÉ: Permite cambiar a Gemini, Claude o OpenAI en el futuro modificando solo la variable 'model'.
    response = completion(
        model="ollama/phi3",
        messages=[{"role": "user", "content": "Hola. Actúa como Merci, mi asistente DevSecOps. Dime que estás viva y operativa en una sola frase breve en español."}],
        api_base="http://localhost:11434"
    )
    print(f"🤖 Merci responde:\n{response.choices[0].message.content}")
except Exception as e:
    print(f"❌ Error de conexión con la IA local: {e}")