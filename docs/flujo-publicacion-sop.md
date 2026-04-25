# SOP: Flujo de Publicación y Ciclo de Vida del Conocimiento

Este documento detalla el Procedimiento Operativo Estándar (SOP - Standard Operating Procedure) o *Runbook* para gobernar el ciclo de vida del contenido dentro del ecosistema DevSecOps de Merci. 

Dado que la automatización del proyecto consta de múltiples herramientas especializadas (orquestadores, optimizadores, auditores), el **orden de ejecución** es un factor crítico de arquitectura. Alterar este orden puede provocar fallos en cadena, como sitemaps desactualizados o enlaces rotos que escapen a la auditoría.

## El Flujo Maestro (Paso a Paso)

Para llevar una idea desde su concepción en local hasta su publicación segura en producción, el pipeline inamovible es el siguiente:

### 1. Sincronización (`git pull`)
Iniciar siempre la sesión descargando los últimos cambios del repositorio remoto para asegurar la paridad con el servidor y evitar conflictos de integración (Merge Conflicts).

### 2. Incubación (Redacción manual)
Redactar la idea, borrador o apunte técnico en la carpeta efímera `laboratorio/`. En esta fase no hay restricciones de validación, el documento es de uso interno y puede estar roto o incompleto.

### 3. Curación (`merci promote`)
Utilizar el asistente interactivo de consola para validar la madurez del documento. El script auditará el YAML Frontmatter, exigirá el cumplimiento de los criterios de accesibilidad estrictos (WAI-ARIA, como obligar a incluir `alt_portada`), actualizará la fecha, cambiará el estado a `publicado` y trasladará el archivo físicamente a su estantería definitiva en la `biblioteca/`.

### 4. Compilación (`merci publish`)
El motor SSG (Static Site Generation) lee los documentos "publicados" de la biblioteca, inyecta el marco visual global (header y footer extraídos dinámicamente de la portada), genera los artefactos descargables (PDF mediante WeasyPrint) y deposita todo el código HTML estático final en la carpeta `public/`.

### 5. Aseguramiento de Calidad (`merci total`)
Ejecutar el orquestador global de Quality Assurance (QA). 
*¿Por qué exactamente en este paso?* 
Porque el actualizador del sitemap (`merci-sitemap.py`) y el escáner de enlaces rotos (`merci-linkcheck.py`) necesitan que los archivos HTML ya hayan sido generados por el paso anterior (`publish`) para poder leerlos y auditarlos correctamente. Alterar este orden dejaría a los rastreadores "ciegos" frente al nuevo contenido. Además, este paso compila el CSS final de SASS.

### 6. Trazabilidad (Bitácora)
Abrir `laboratorio/bitacora-mercedev.md` y documentar rápidamente la maniobra técnica realizada siguiendo la estructura de conocimiento de los 3 átomos (Desafío, Maniobra, Aprendizaje).

### 7. Empaquetado Atómico (`merci commit`)
El script de CI/CD (Integración y Despliegue Continuos) lee la bitácora, realiza el auto-stage de todos los archivos nuevos o modificados (HTML, PDF, Markdown) y sella el repositorio de forma atómica en un único commit. Antes de hacerlo, validará todo contra el hook de seguridad *pre-commit* (búsqueda de secretos, validación de sintaxis y JSON-LD).

### 8. Despliegue (`git push`)
Enviar el paquete cerrado e inmaculado al servidor, disparando la actualización instantánea en producción.

---

### Herramientas Situacionales
Comandos paralelos como `merci watch` (vigilante de estilos en tiempo real) o `merci audit` (lanzar un linter aislado) son situacionales para el trabajo de diseño (UI) o depuración. Sin embargo, para la publicación de conocimiento, los 8 pasos descritos conforman la **tubería inamovible** del sistema.