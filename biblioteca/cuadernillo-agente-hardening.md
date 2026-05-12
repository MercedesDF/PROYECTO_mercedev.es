---
titulo: "Transformación de Checklist de Seguridad Pasiva en Escudo Activo"
descripcion: "Se convierte un checklist de seguridad pasivo en un escudo activo mediante merci-hardening.py, garantizando el Continuous Compliance."
tipo: "cuadernillo"
tema: "DevSecOps y Gobernanza"
fecha: "2026-05-12"
fase: "Epic 2 - Fase 4"
estado: "publicado"
alt_portada: "Descripción visual de la imagen de portada para accesibilidad WAI-ARIA."
---
## El Desafío (Síntoma)
Se detectó que el proyecto tenía un checklist de seguridad pasivo en texto plano, lo que no garantizaba una postura de seguridad real y continuo.

## La Maniobra (Lógica)
Se creó merci-hardening.py, un agente que audita la postura de seguridad real de la infraestructura en local. El script comprueba empíricamente que el archivo .env tenga permisos 600, que el .gitignore contenga reglas DLP críticas, bloquea la exposición de archivos rogue como wp-config.php en la raíz y busca Mixed Content (http://) en el HTML estático.

## El Aprendizaje / Deuda Técnica
Se garantiza el Continuous Compliance de la arquitectura antes de cada commit. La solución es óptima porque automatiza la verificación de seguridad, reduciendo el riesgo de vulnerabilidades y asegurando que los cambios cumplen con las políticas de seguridad establecidas.