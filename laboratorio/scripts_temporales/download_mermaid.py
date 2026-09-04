import base64
import json
import urllib.request
import os

mermaid_code = """graph TD
    %% Entidades principales
    U("Usuaria / Mercedes")
    IDE["Orquestador / IDE Antigravity"]
    LLM("Modelo Local LiteLLM")
    
    %% Scripts
    LIB("merci-librarian.py")
    BLOG("merci-blogger.py")
    CI("merci total")
    
    %% Artefactos
    RAW["/notas_rapidas/nota.txt"]
    DOC["/biblioteca/cuadernillo.md"]
    POST["/blog/post.md"]
    RULES["Reglas: AGENTS.md & docs/plantillas"]

    %% Flujo de Intención
    U -->|"1. Escribe idea cruda"| RAW
    U -->|"2. Da orden de publicación"| IDE

    %% Orquestación y Gobernanza
    IDE -.->|"Consulta Reglas (Regla 7 y 8)"| RULES
    IDE -->|"3. Invoca Librarian"| LIB
    
    %% Agent Chaining (Fase Táctica)
    LIB -->|"Consulta LLM"| LLM
    LLM -->|"Estructura Markdown"| LIB
    LIB -->|"4. Genera Cuadernillo"| DOC
    LIB -->|"5. Agent Chaining"| BLOG
    BLOG -->|"Consulta LLM"| LLM
    LLM -->|"Escribe Marketing"| BLOG
    BLOG -->|"6. Genera Teaser"| POST

    %% Zero-Trust QA (Auditoría Autónoma)
    IDE -.->|"7. Audita sintaxis y plantilla (Regla 8)"| DOC
    IDE -.->|"7. Audita semántica y YAML (Regla 8)"| POST
    
    %% Bucle de Corrección Silenciosa
    DOC -.->|"Si hay alucinación"| IDE
    IDE -.->|"Corrige formato sin molestar"| DOC
    
    %% Despliegue y Aprobación Final
    IDE -->|"8. Todo en verde. Lanza CI estático"| CI
    CI -->|"Web construida en 7s"| IDE
    IDE -->|"9. Notifica éxito y solicita commit"| U
    U -->|"10. Ejecuta merci commit"| Produccion("Git Producción")"""

state = {
    "code": mermaid_code,
    "mermaid": {"theme": "default"}
}

json_str = json.dumps(state)
b64_str = base64.b64encode(json_str.encode('utf-8')).decode('utf-8')

url = f"https://mermaid.ink/img/{b64_str}"

os.makedirs("docs/img", exist_ok=True)
output_path = "docs/img/diagrama-agentes.png"

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response, open(output_path, 'wb') as out_file:
    data = response.read()
    out_file.write(data)

print(f"Downloaded to {output_path}")
