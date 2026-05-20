#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
merci-glosario-ai.py — Automatización Extendida del Glosario.
Delega a un modelo local (Ollama) la definición de nuevos términos DevSecOps
y los anexa automáticamente al glosario técnico, manteniendo fricción cero.
"""

import os
import sys
import subprocess

# Archivos objetivo de la biblioteca y el prompt
GLOSSARY_FILE = '/home/hildegahr/Escritorio/PROYECTO_mercedev.es/laboratorio/biblioteca/glosario-tecnico.md'
PROMPT_FILE = '/home/hildegahr/Escritorio/PROYECTO_mercedev.es/laboratorio/prompts/prompt-glosario.md'
# Modelo de IA local por defecto para código y DevSecOps
MODEL = 'qwen2.5-coder'

def add_new_terms_via_ollama(terms_list):
    """
    Función que orquesta la llamada a Ollama y la escritura del resultado.
    """
    
    # Verificamos que el System Prompt exista para garantizar el formato estricto
    # Si falta el prompt, el modelo podría alucinar el formato y corromper el glosario.
    if not os.path.exists(PROMPT_FILE):
        print(f"Error: No se encontró el prompt en {PROMPT_FILE}")
        sys.exit(1)

    # Cargamos el prompt del sistema que instruye a la IA a comportarse como Arquitecto
    with open(PROMPT_FILE, 'r', encoding='utf-8') as f:
        system_prompt = f.read()

    # Formateamos los argumentos pasados por la CLI para el usuario final
    user_prompt = f"Define los siguientes términos DevSecOps:\n{', '.join(terms_list)}"

    print(f"Consultando a {MODEL} para los términos: {terms_list}...")
    
    # Llamada directa a Ollama (Zero-Dependency approach)
    # Utilizamos subprocess en lugar de librerías externas (como requests o litellm) 
    # para cumplir con la política del proyecto de 0 dependencias ajenas donde sea posible.
    cmd = [
        "ollama", "run", MODEL,
        f"SYSTEM: {system_prompt}\n\nUSER: {user_prompt}"
    ]
    
    try:
        # Ejecutamos el comando de consola y capturamos la salida estándar (stdout)
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        response = result.stdout.strip()
        print("\n--- Respuesta recibida ---\n")
        print(response)
        
        # Si la IA respondió con éxito, anexamos el resultado al glosario.
        # Utilizamos el modo 'a' (append) para inyectar los datos de forma segura
        # al final del archivo sin destruir el contenido previo (patrón Append-Only).
        if response:
            with open(GLOSSARY_FILE, 'a', encoding='utf-8') as f:
                f.write("\n" + response + "\n")
            print(f"\n¡Éxito! Términos añadidos al final de {GLOSSARY_FILE}.")
            print("NOTA: Por favor revisa y ordena alfabéticamente el glosario si es necesario.")
    except subprocess.CalledProcessError as e:
        print("Error al ejecutar Ollama:", e.stderr)

if __name__ == "__main__":
    # Aseguramos que se haya pasado al menos un término por argumento CLI
    if len(sys.argv) < 2:
        print("Uso: python3 merci-glosario-ai.py Término1 Término2 ...")
        sys.exit(1)
    
    terms = sys.argv[1:]
    add_new_terms_via_ollama(terms)
