---
titulo: "Sanitización de Metadatos YAML: Prevención XSS y Rotura del DOM"
descripcion: "Cómo el escapado de caracteres HTML en metadatos YAML previene inyecciones XSS y asegura la integridad del DOM en generadores estáticos."
estado: "publicado"
estado_social: "publicado_linkedin"
subtema: "Blog"
tipo: "cuadernillo"
fase: "Epic 3 - Fase 1"
alt_portada: "Esquema conceptual mostrando la sanitización de cadenas en Python antes de inyectarlas en el DOM."
fecha: "2026-05-17"
linkedin_id: "urn:li:share:7463498897894842369"
---
<!-- linkedin:
Las entidades HTML pueden romper tu sitio web. Aprende cómo el escapado de caracteres en los metadatos YAML previene inyecciones XSS y asegura la integridad del DOM en los generadores de sitios estáticos.
#DevSecOps #DesarrolloWeb #Seguridad
-->

Durante una de las compilaciones rutinarias de la Biblioteca, se detectó un fallo crítico: la página dejó de cargar repentinamente y parte de la interfaz desapareció. El origen no era un error de CSS ni una caída del servidor, sino un campo de metadatos en un archivo Markdown.

El texto de una descripción contenía etiquetas HTML literales como `<script>`. Al ser procesadas "en crudo" por el generador de sitios estáticos (SSG), el navegador las interpretó como código ejecutable. Esto no solo rompió la estructura del DOM por la falta de etiquetas de cierre, sino que abrió la puerta al clásico vector de ataque Cross-Site Scripting (XSS).

Para solucionarlo, se aplicó una política de seguridad estricta desde el origen (*Shift-Left Security*). Se refactorizaron los orquestadores en Python (`merci-publish.py` y `merci-wp.py`) integrando la función nativa `html.escape()`. Ahora, todo metadato extraído del YAML Frontmatter es sanitizado antes de inyectarse en el HTML o en la compilación de PDFs.

La lección arquitectónica es innegociable: confiar ciegamente en las entradas de datos —incluso si provienen de archivos locales redactados por el propio equipo— es un antipatrón. Sanitizar las cadenas en tiempo de compilación (*Build Time*) cierra de forma permanente cualquier vía de inyección secundaria.

Si quieres profundizar en cómo implementamos este blindaje en nuestro motor SSG, te invito a leer el [cuadernillo técnico completo](/biblioteca/sanitizacion-de-metadatos-yaml-prevencion-xss-y-rotura-del-dom.html).