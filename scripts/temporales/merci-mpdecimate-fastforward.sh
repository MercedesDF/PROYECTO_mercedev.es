#!/bin/bash
# =========================================================================
# SCRIPT TEMPORAL: merci-mpdecimate-fastforward.sh
# =========================================================================
#
# ¿Por qué está en 'temporales' y no en la línea de producción?
# -------------------------------------------------------------------------
# Este script utiliza el filtro 'mpdecimate' de FFmpeg para analizar un vídeo
# y eliminar todos los fotogramas donde no se detecta movimiento (por ejemplo,
# cuando una terminal se queda bloqueada o pensando durante minutos).
#
# EL PROBLEMA: El reajuste de tiempos ('setpts=N/FRAME_RATE/TB') colapsa 
# literalmente todo ese tiempo muerto, pegando los fotogramas activos uno 
# detrás de otro. El resultado visual es un efecto de "cámara súper-rápida" o 
# "timelapse hiperactivo" que marea al espectador humano y no permite leer
# lo que sucede en pantalla.
# 
# CONCLUSIÓN: Es útil como herramienta de compresión extrema para logs visuales
# brutos, pero no sirve para el montaje de vídeos de 'showcase'. Para un acabado
# profesional y humano, es mandatorio usar editores con 'padding' (CapCut, 
# auto-editor, Premiere).
#
# Uso empírico:
# bash merci-mpdecimate-fastforward.sh <input.webm> <output.mp4>
# =========================================================================

INPUT_FILE=$1
OUTPUT_FILE=$2

if [ -z "$INPUT_FILE" ] || [ -z "$OUTPUT_FILE" ]; then
    echo "❌ Error: Faltan argumentos."
    echo "👉 Uso: bash $0 <archivo_entrada> <archivo_salida.mp4>"
    exit 1
fi

echo "🎬 Analizando y triturando fotogramas estáticos con FFmpeg..."
ffmpeg -y -i "$INPUT_FILE" -vf "mpdecimate,setpts=N/FRAME_RATE/TB" -an -c:v libx264 -preset fast -crf 28 "$OUTPUT_FILE"

echo "✅ Proceso completado. Has creado un engendro hiperactivo."
