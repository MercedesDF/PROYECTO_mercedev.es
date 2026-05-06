#!/usr/bin/env python3
import os
import re
from pathlib import Path

# Diccionario heurístico de fechas a fases (Extraído de la bitácora del proyecto)
MAPA_FASES = {
    "2026-04-12": "1 (Infraestructura Base)",
    "2026-04-14": "2 (Arquitectura y SEO)",
    "2026-04-15": "3-5 (SASS, WP y Hardening)",
    "2026-04-16": "3-5 (SASS, WP y Hardening)",
    "2026-04-17": "6 (Despliegue y Auditoría)",
    "2026-04-20": "6 (Despliegue y Auditoría)",
    "2026-04-21": "6 (Despliegue y Auditoría Final)",
    "2026-04-23": "6 (Despliegue y Auditoría Final)",
    "2026-04-24": "7 (Automatización y Clasificación)",
    "2026-04-25": "7 (Automatización y Clasificación)",
    "2026-04-26": "10 (Empaquetado y Release)",
    "2026-04-27": "8 (Expansión de Contenido)",
    "2026-04-28": "8 (Expansión de Contenido)",
    "2026-04-29": "8 (Expansión de Contenido)",
    "2026-04-30": "8 (Expansión de Contenido)",
    "2026-05-01": "8 (Expansión de Contenido)",
    "2026-05-02": "9 (Inteligencia y Autonomía)",
    "2026-05-04": "8.4 (Identidad y Autoridad)",
    "2026-05-05": "11 (CI/CD y Lighthouse)",
    "2026-05-06": "11 (Cierre Arquitectónico)"
}

def procesar_archivos(directorio):
    target_dir = Path(directorio)
    if not target_dir.exists():
        return
    
    for filepath in target_dir.rglob("*.md"):
        content = filepath.read_text(encoding="utf-8-sig")
        
        # Si ya tiene el campo fase o no tiene fecha, lo saltamos
        if re.search(r'^fase\s*:', content, re.MULTILINE) or not re.search(r'^fecha\s*:\s*"([^"]+)"', content, re.MULTILINE):
            continue
        
        # Buscar la fecha y determinar la fase
        fecha = re.search(r'^fecha\s*:\s*"([^"]+)"', content, re.MULTILINE).group(1)
        fase = MAPA_FASES.get(fecha, "Desconocida (Revisar manualmente)")
        
        # Inyectar el campo fase justo debajo del campo fecha
        nuevo_contenido = re.sub(r'(^fecha\s*:\s*"[^"]+"\n)', f'\\1fase: "{fase}"\n', content, flags=re.MULTILINE)
        filepath.write_text(nuevo_contenido, encoding="utf-8")
        print(f"✅ Inyectada fase '{fase}' en {filepath.name}")

if __name__ == "__main__":
    print("🚀 Iniciando inyección de fases en YAML Frontmatter...")
    procesar_archivos("biblioteca")
    procesar_archivos("laboratorio")
    print("✨ Proceso completado.")