#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
merci-promote.py — Flujo de Promoción Laboratorio -> Biblioteca (Fase 7.3).
Herramienta interactiva de consola (CLI) para trasladar, curar y estandarizar borradores.
"""

import re
from datetime import datetime
from pathlib import Path

# 1. Definición de rutas absolutas unificadas
REPO_ROOT = Path(__file__).resolve().parents[2]
LABORATORIO_DIR = REPO_ROOT / "laboratorio"
BIBLIOTECA_DIR = REPO_ROOT / "biblioteca"

def main():
    print("🚀 [Merci Promote] Iniciando flujo de promoción de conocimiento...")

    # 2. Escaneo del directorio excluyendo la bitácora central
    borradores = [f for f in LABORATORIO_DIR.glob("*.md") if f.name != "bitacora-mercedev.md"]
    
    if not borradores:
        print("  ℹ️ No se encontraron borradores en el laboratorio.")
        return

    print("\n📄 Borradores efímeros disponibles:")
    for idx, f in enumerate(borradores, start=1):
        print(f"  [{idx}] {f.name}")

    # 3. Interfaz de selección por consola
    try:
        seleccion = int(input("\n👉 Selecciona el número del borrador a promover (0 para cancelar): "))
        if seleccion == 0:
            print("  🛑 Operación cancelada.")
            return
        if seleccion < 1 or seleccion > len(borradores):
            print("  ❌ Selección inválida.")
            return
    except ValueError:
        print("  ❌ Entrada inválida. Debes introducir un número.")
        return

    borrador_elegido = borradores[seleccion - 1]
    contenido = borrador_elegido.read_text(encoding="utf-8")

    # 4. Extracción de Metadatos usando expresiones regulares
    # Extrae el bloque entre los dos --- iniciales
    match = re.match(r"^---\n(.*?)\n---\n(.*)", contenido, re.DOTALL)
    if not match:
        print(f"  ❌ Error: El archivo {borrador_elegido.name} no tiene un YAML Frontmatter válido.")
        print("  Por favor, añade la estructura base (plantilla) antes de promoverlo.")
        return

    yaml_raw, md_body = match.groups()
    
    # Parseo manual del YAML para evitar instalar PyYAML (Cero dependencias externas)
    meta = {}
    for linea in yaml_raw.splitlines():
        if ":" in linea:
            key, val = linea.split(":", 1)
            # Limpiamos espacios y comillas residuales
            meta[key.strip()] = val.strip().strip('"\'')

    print(f"\n⚙️ Curación de metadatos para: {meta.get('titulo', borrador_elegido.name)}")
    
    # 5. Auditoría interactiva y curación de datos (Shift-Left Quality)
    # Mostramos el valor actual por defecto. Si el usuario pulsa Enter sin escribir, se conserva.
    nuevo_tema = input(f"  🏷️  Tema/Estantería [{meta.get('tema', 'General')}]: ").strip() or meta.get('tema', 'General')
    nueva_desc = input(f"  📝 Descripción [{meta.get('descripcion', '')}]: ").strip() or meta.get('descripcion', '')
    nuevo_alt = input(f"  👁️  Alt de la portada [{meta.get('alt_portada', '')}]: ").strip() or meta.get('alt_portada', '')

    # Bloqueo estricto si falta el atributo de accesibilidad
    if not nuevo_alt:
        print("  ❌ Error: El texto alternativo 'alt_portada' es obligatorio para mantener el 100/100 en WAI-ARIA.")
        return

    # 6. Máquina de Estados: Reconstrucción del YAML definitivo
    meta['tema'] = nuevo_tema
    meta['descripcion'] = nueva_desc
    meta['alt_portada'] = nuevo_alt
    meta['estado'] = 'publicado'  # Cambio de estado automatizado
    meta['fecha'] = datetime.now().strftime("%Y-%m-%d") # Auto-sellado con fecha de promoción actual

    nuevo_yaml = "---\n"
    for k, v in meta.items():
        # Reinyectamos las comillas dobles para seguridad del string en YAML
        nuevo_yaml += f'{k}: "{v}"\n'
    nuevo_yaml += "---"

    # Ensamblamos el contenido final
    nuevo_contenido = f"{nuevo_yaml}\n{md_body}"

    # 7. Traslado físico de archivos (Promoción)
    destino = BIBLIOTECA_DIR / borrador_elegido.name
    
    # Guardar en destino
    destino.write_text(nuevo_contenido, encoding="utf-8")
    # Purgar origen
    borrador_elegido.unlink()

    print(f"\n✅ Promoción exitosa. El archivo reside ahora en: biblioteca/{destino.name}")
    print("  💡 Siguiente paso: Ejecuta 'python3 scripts/merci/merci-publish.py' para compilarlo.")

if __name__ == "__main__":
    main()