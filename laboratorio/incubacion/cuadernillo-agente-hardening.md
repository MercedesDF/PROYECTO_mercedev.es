---
titulo: "Transformación de Checklist Pasiva a Escudo Activo con merci-hardening.py"
descripcion: "Se convierte un checklist de seguridad pasivo en un escudo activo que audita la postura de seguridad real de la infraestructura."
tipo: "cuadernillo"
tema: "DevSecOps y Gobernanza"
fecha: "2026-05-12"
fase: "Épica 2 - Fase 4"
estado: "borrador"
alt_portada: "Un escudo activo que audita la postura de seguridad real de la infraestructura."
---

**linkedin:
Se transformó un checklist de seguridad pasivo en un escudo activo con merci-hardening.py, garantizando el Continuous Compliance de la arquitectura antes de cada commit. #DevSecOps #Gobernanza
**

## El Desafío (Síntoma)
Se detectó que el proyecto necesitaba una solución más proactiva para asegurar la postura de seguridad real de la infraestructura, ya que un checklist pasivo no proporcionaba auditoría empírica.

## La Maniobra (Lógica)
Se creó merci-hardening.py, un agente que audita la postura de seguridad real de la infraestructura en local. El escudo activo comprueba:
- Permisos 600 en el archivo .env
- Reglas DLP críticas en el .gitignore
- Bloqueo de la exposición de archivos rogue como wp-config.php en la raíz
- Búsqueda de Mixed Content (http://) en el HTML estático

## El Aprendizaje / Deuda Técnica
La solución es la óptima porque garantiza el Continuous Compliance de la arquitectura antes de cada commit, lo que previene vulnerabilidades y asegura una postura de seguridad más sólida. Se ha asumido una pequeña deuda técnica en términos de mantenimiento del script, pero esta solución es valiosa para la longo plazo.