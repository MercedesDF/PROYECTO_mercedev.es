#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_ia.py — Sonda de validación de conexión con Ollama y LiteLLM.

Objetivo: Comprobar que el entorno virtual de Python puede comunicarse 
de forma privada y sin latencia con el modelo de IA local (qwen2.5-coder) 
ejecutado en el sistema anfitrión.
"""

import sys

try:
    from litellm import completion
    import litellm
except ImportError:
    print("❌ [Merci Error] LiteLLM no está instalado en el entorno virtual.")
    print("💡 Ejecuta: pip install litellm")
    sys.exit(1)

def test_local_llm():
    print("🚀 Iniciando sonda de conexión con motor Ollama local (Modelo: qwen2.5-coder)...")
    
    # QUÉ HACE: Desactiva el envío de métricas de uso a los servidores de LiteLLM.
    # POR QUÉ: DevSecOps y Privacidad. Mantenemos el aislamiento total del proyecto.
    litellm.telemetry = False

    mensajes = [
        {"role": "system", "content": "Eres un asistente técnico experto en DevSecOps. Responde de forma muy breve y directa."},
        {"role": "user", "content": "Hola, ¿estás operativo? Responde con un simple 'Sí, sistemas en línea' y una breve frase sobre DevSecOps."}
    ]

    try:
        # QUÉ HACE: Realiza una petición de generación delegando la sintaxis a LiteLLM.
        # POR QUÉ: Permite usar el estándar de la industria mientras apuntamos a nuestro servidor local privado.
        respuesta = completion(
            model="ollama/qwen2.5-coder",
            messages=mensajes,
            api_base="http://localhost:11434",
            max_tokens=50
        )

        contenido = respuesta.choices[0].message.content
        print(f"\n✅ [Éxito] Enlace sináptico establecido. Respuesta de la IA:\n")
        print(f"🤖 qwen2.5-coder: {contenido}\n")

    except Exception as e:
        print(f"\n❌ [Merci Error] Fallo en la comunicación con Ollama: {e}")
        print("💡 Asegúrate de que el servicio de Ollama está levantado en el sistema anfitrión.")
        print("💡 Comprueba que el modelo 'qwen2.5-coder' está correctamente descargado ('ollama run qwen2.5-coder').")
        sys.exit(1)

if __name__ == "__main__":
    test_local_llm()