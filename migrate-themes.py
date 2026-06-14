import os
import glob

dirs_to_check = ['biblioteca/*.md', 'blog/*.md', 'laboratorio/**/*.md']
files = []
for d in dirs_to_check:
    files.extend(glob.glob(d, recursive=True))

theme_map = {
    "arquitectura de software": ("Desarrollo y Arquitectura", "Arquitectura"),
    "arquitectura y backend": ("Desarrollo y Arquitectura", "Backend"),
    "arquitectura y frontend": ("Desarrollo y Arquitectura", "Frontend"),
    "arquitectura y rendimiento": ("Desarrollo y Arquitectura", "Rendimiento"),
    "ingeniería de estilos": ("Desarrollo y Arquitectura", "Estilos"),
    "ingeniería de interfaz estática": ("Desarrollo y Arquitectura", "Frontend"),
    "rendimiento y ux": ("Desarrollo y Arquitectura", "UX"),
    "seguridad y arquitectura": ("Desarrollo y Arquitectura", "Seguridad"),
    "interfaz de usuario y rendimiento": ("Desarrollo y Arquitectura", "Frontend"),

    "automatización y python": ("DevSecOps e Infraestructura", "Automatización"),
    "devsecops": ("DevSecOps e Infraestructura", "DevSecOps"),
    "devsecops y arquitectura": ("DevSecOps e Infraestructura", "DevSecOps"),
    "devsecops y automatización": ("DevSecOps e Infraestructura", "Automatización"),
    "devsecops y gobernanza": ("DevSecOps e Infraestructura", "Gobernanza"),
    "infraestructura y automatización": ("DevSecOps e Infraestructura", "Infraestructura"),
    "infraestructura y despliegue": ("DevSecOps e Infraestructura", "Despliegue"),
    "sos terminal": ("DevSecOps e Infraestructura", "Terminal"),

    "inteligencia artificial y gobernanza": ("Inteligencia Artificial y Agentes", "Gobernanza"),
    "inteligencia artificial y rag": ("Inteligencia Artificial y Agentes", "RAG"),

    "identidad y autoridad técnica": ("Productividad y Gobernanza", "Identidad"),
    "desarrollo y productividad": ("Productividad y Gobernanza", "Productividad"), # We will respect existing subtema if present
    
    "blog": ("Varios", "Blog")
}

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    new_lines = []
    in_frontmatter = False
    
    # We will track if we found tema and subtema
    found_tema = None
    found_subtema = None
    
    tema_idx = -1
    subtema_idx = -1
    
    # First pass to find properties
    for i, line in enumerate(lines):
        if line == "---":
            in_frontmatter = not in_frontmatter
            
        if in_frontmatter:
            if line.startswith("tema:"):
                found_tema = line.split(":", 1)[1].strip().strip('"').strip("'")
                tema_idx = i
            elif line.startswith("subtema:"):
                found_subtema = line.split(":", 1)[1].strip().strip('"').strip("'")
                subtema_idx = i
                
    if found_tema is None:
        continue # No tema to migrate
        
    # Map the old tema
    mapped = theme_map.get(found_tema.lower(), ("Varios", found_tema))
    new_macro = mapped[0]
    
    # If the file already has a subtema (like the ones the user manually edited), keep it.
    new_sub = found_subtema if found_subtema else mapped[1]

    # Special logic for the ones the user manually modified:
    # They set tema: "Desarrollo y Productividad" and subtema: "Agentes".
    # I mapped "desarrollo y productividad" to macro "Productividad y Gobernanza".
    # So new_macro = "Productividad y Gobernanza" and new_sub = "Agentes".
    
    # Let's apply the changes
    for i, line in enumerate(lines):
        if i == tema_idx:
            new_lines.append(f'tema: "{new_macro}"')
            if subtema_idx == -1: # We need to insert subtema right after tema
                new_lines.append(f'subtema: "{new_sub}"')
        elif i == subtema_idx:
            new_lines.append(f'subtema: "{new_sub}"')
        else:
            new_lines.append(line)
            
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))

print(f"Migration completed on {len(files)} files.")
