#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
laboratorio/scripts_temporales/merci-fix-artdecote.py

QUÉ HACE: Realiza un reemplazo (Find & Replace) masivo mediante Expresiones Regulares en 
          todos los archivos Markdown de la carpeta `art-de-cote/`. Específicamente, inyecta
          los metadatos obligatorios `subtema: "General"` y `destacado: "false"` a continuación 
          del campo `tema:` en aquellos documentos que no lo tengan.
POR QUÉ ESTÁ AQUÍ Y NO EN EL GENERAL: 
          Es una utilidad efímera de "Data Healing" o normalización de esquemas. Fue creada 
          para resolver una inconsistencia en la base de datos documental (YAML Frontmatter) 
          que estaba rompiendo la compilación. Se preserva en scripts temporales porque el 
          patrón de búsqueda y reemplazo en masa sobre markdowns es un snippet muy útil para 
          el futuro.
"""

import os
import glob
import re

files = glob.glob("art-de-cote/*.md")

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    if "subtema:" not in content:
        content = re.sub(r'tema: (.*)', r'tema: \1\nsubtema: "General"\ndestacado: "false"', content)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {filepath}")
