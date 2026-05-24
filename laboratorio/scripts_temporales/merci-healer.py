#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
merci-healer.py — Cirujano DevSecOps de un solo uso.
Cura la deuda técnica documental y purga los falsos acrónimos.
"""

import json
import re
from pathlib import Path

# Al estar en laboratorio/scripts_temporales/, subimos 2 niveles para llegar a la raíz
REPO_ROOT = Path(__file__).resolve().parents[2]

def main():
    print("🏥 [Merci Healer] Iniciando cirugía DevSecOps...")

    # 1. Purgar archivo zombi (El causante de la mitad de las advertencias)
    old_md = REPO_ROOT / "laboratorio" / "biblioteca" / "glosario-tecnico.md"
    if old_md.exists():
        old_md.unlink()
        print("  ✅ Archivo zombi 'laboratorio/biblioteca/glosario-tecnico.md' erradicado.")

    # 2. Purgar ruido del Glosario JSON
    json_path = REPO_ROOT / "laboratorio" / "biblioteca" / "glosario-tecnico.json"
    if json_path.exists():
        data = json.loads(json_path.read_text("utf-8"))
        terminos = data.get("terminos", {})
        ignorados = data.get("ignorados", [])
        
        ruido = ["ADR-04", "ADR-06", "AM", "CAMBIOS", "COPIA", "CREATE", "DATABASE", "DEBE", "DNI", "DOMINIO", "ES6", "FLUSH", "GET", "HEALING", "LICENSE", "MIT", "MP4", "NPM", "NXDOMAIN", "PIPELINE", "POST", "PUT", "README", "SECURITY", "SIGINT", "SQL", "TTL", "UNA", "VPS", "AKIA", "AI-"]
        purgados = 0
        for r in ruido:
            if r in terminos:
                del terminos[r]
                if r not in ignorados:
                    ignorados.append(r)
                purgados += 1
                
        data["terminos"] = terminos
        data["ignorados"] = ignorados
        json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), "utf-8")
        print(f"  ✅ {purgados} falsos acrónimos extirpados del JSON.")

    # 3. Expandir acrónimos reales en el registro histórico
    fixes = {
        "laboratorio/bitacora-mercedev-epic-01.md": [(r"\bCRLF\b", "Retorno de carro y avance de línea (CRLF)")],
        "laboratorio/bitacora-mercedev-epic-02.md": [
            (r"\bJWT\b", "Token Web JSON (JWT)"),
            (r"\bSSRF\b", "Falsificación de Petición del Lado del Servidor (SSRF)"),
            (r"\bTCP\b", "Protocolo de Control de Transmisión (TCP)")
        ],
        "laboratorio/bitacora-mercedev-epic-03.md": [(r"\bCWV\b", "Métricas Web Principales (CWV)")]
    }

    for rel_path, replacements in fixes.items():
        p = REPO_ROOT / rel_path
        if p.exists():
            content = p.read_text("utf-8")
            for pat, repl in replacements:
                content = re.sub(pat, repl, content)
            p.write_text(content, "utf-8")
            
    print("  ✅ Acrónimos reales consolidados y expandidos en las bitácoras.")
    print("\n🎉 Operación completada. Ejecuta 'merci total' para confirmar el 0/0.")

if __name__ == "__main__":
    main()