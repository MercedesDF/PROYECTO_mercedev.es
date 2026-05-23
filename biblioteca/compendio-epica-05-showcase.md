---
titulo: "Compendio Estratégico: Épica 5 - Showcase y Distribución"
descripcion: "Estrategias de Dogfooding, Out-of-the-Box Experience y despliegue Zero-Friction para la demostración pública del framework."
tipo: "compendio"
tema: "DevSecOps y Gobernanza"
fecha: "2026-05-22"
fase: "Epic 5 - Fase 1"
estado: "publicado"
alt_portada: "Escaparate digital exhibiendo un proyecto web pulido bajo un foco de luz."
---
**Contexto:** Un Boilerplate Open Source carece de tracción si los usuarios no pueden auditarlo visual e interactivamente antes de descargarlo. El objetivo era desplegar un entorno de demostración continuo sin arrastrar datos privados de la matriz.

**Maniobras Arquitectónicas:**
1. **Dogfooding Extremado:** Se validó la OOBE (Out-of-the-Box Experience) de la plantilla. Al instanciarse, las carpetas vaciadas devolvían error 403. Se dotó a `merci-init.py` de la capacidad para inyectar "Placeholders anti-403" que heredan automáticamente el menú, footer y la IA de la portada principal, logrando una navegación ininterrumpida.
2. **El Clon Efímero:** Para aislar la infraestructura, el orquestador de despliegue (`merci-showcase.py`) copia el ecosistema a una carpeta temporal, lo purga de metadatos privados usando la propia herramienta de inicialización y despliega el código inmaculado.
3. **Hardening de Infraestructura:** Se eliminó el "hardcoding" de variables, delegando rutas, dominios y llaves SSH personalizadas al archivo oculto `.env` y blindando el comando `rsync` contra los bloqueos inmutables de CloudPanel.

**Aprendizaje / Deuda Técnica:**
Crear un Showcase no es solo levantar una web, es demostrar el valor de tu infraestructura automatizada. Hacer que el entorno de demostración se despliegue usando exactamente las mismas herramientas que recibirá el cliente (Dogfooding) saca a la luz los errores de experiencia de usuario temprana (como los 403). Garantizar una Marca Blanca sin destruir el diseño requiere anonimización selectiva y un control estricto del "Document Root".
