#!/usr/bin/env python3
import re
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
GLOSSARY_MD = REPO_ROOT / 'laboratorio' / 'biblioteca' / 'glosario-tecnico.md'
GLOSSARY_JSON = REPO_ROOT / 'laboratorio' / 'biblioteca' / 'glosario-tecnico.json'
IGNORE_FILE = REPO_ROOT / 'laboratorio' / 'biblioteca' / '.glosario_ignore.txt'

def parse_markdown():
    if not GLOSSARY_MD.exists():
        return {}
        
    content = GLOSSARY_MD.read_text(encoding='utf-8')
    blocks = content.split('### ')[1:] # Ignorar la cabecera del documento
    
    terminos = {}
    
    for block in blocks:
        lines = block.strip().split('\n')
        term_name = lines[0].strip()
        
        ingles = ""
        espanol = ""
        definicion = ""
        apariciones = {}
        
        # Parseo iterativo
        mode = None
        for line in lines[1:]:
            line = line.strip()
            if not line or line == "---":
                continue
                
            if line.startswith('**Inglés:**'):
                ingles = line.replace('**Inglés:**', '').strip()
            elif line.startswith('**Español:**'):
                espanol = line.replace('**Español:**', '').strip()
            elif line.startswith('**Definición:**'):
                definicion = line.replace('**Definición:**', '').strip()
                mode = 'definicion'
            elif line.startswith('**Apariciones en Bitácoras:**'):
                mode = 'apariciones'
            elif mode == 'apariciones' and line.startswith('- `'):
                # - `bitacora.md`: L1, L2
                parts = line.split('`')
                if len(parts) >= 3:
                    fname = parts[1]
                    lines_part = parts[2].replace(':', '').strip()
                    apariciones[fname] = [l.strip() for l in lines_part.split(',')]
            elif mode == 'definicion':
                # Por si la definición ocupa varias líneas
                definicion += " " + line
                
        terminos[term_name] = {
            "ingles": ingles,
            "espanol": espanol,
            "definicion": definicion,
            "apariciones": apariciones
        }
        
    return terminos

def get_ignored():
    ignored = []
    if IGNORE_FILE.exists():
        with open(IGNORE_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip() and line.strip() not in ignored:
                    ignored.append(line.strip())
    return ignored

def main():
    terminos = parse_markdown()
    ignorados = get_ignored()
    
    data = {
        "terminos": terminos,
        "ignorados": ignorados
    }
    
    with open(GLOSSARY_JSON, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"✅ Migración completa. {len(terminos)} términos convertidos a JSON.")

if __name__ == '__main__':
    main()
