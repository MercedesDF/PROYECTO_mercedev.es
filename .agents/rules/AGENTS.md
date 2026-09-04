# Reglas Globales (Gobernanza de Agentes)

Este documento contiene las reglas universales (Juramento Hipocrático) para todos los agentes del espacio de trabajo `PROYECTO_mercedev.es` bajo la orquestación de Antigravity IDE.

## 1. Single Source of Truth (SSOT)
Antes de ejecutar cualquier acción que modifique el comportamiento, dependencias o arquitectura del repositorio, **DEBES leer obligatoriamente `instrucciones.md`**. Es la única fuente de verdad. 

## 2. Filosofía Zero-Bloat y Minimalismo
- Está estrictamente prohibido instalar dependencias pesadas, librerías de NPM (Node.js) o frameworks CSS/JS de terceros.
- Todas las soluciones técnicas deben ser desarrolladas en Vanilla JS, HTML5 estricto, o SCSS compilado.
- El rendimiento (Core Web Vitals) y la accesibilidad técnica no son negociables (100/100). Todo script debe estar asincronizado (`defer`/`async`).

## 3. Soberanía del Castellano y Voz Editorial
- Todo el código (comentarios) y la documentación (bitácoras, README) deben estar redactados en español.
- Los acrónimos deben definirse la primera vez que se usan (Inglés/Español).
- Sigue la **Regla 80/20** en redacción: 80% utilidad técnica, 20% tono (sin humo comercial). Redacción en infinitivo o impersonal para documentos.

## 4. Trazabilidad de Operaciones (Bitácora)
Cualquier hito cerrado o sesión de trabajo **debe quedar registrado** en la bitácora activa dentro del directorio `laboratorio/` (`bitacora-mercedev-epic-NN.md`) siguiendo estrictamente su plantilla cronológica inversa.

## 5. Protocolo de Resiliencia (Fail-Fast)
Si falla una automatización, el agente SRE/QA debe aplicar **Degradación Elegante (Graceful Degradation)** para evitar bloquear el *pipeline* estático y notificarlo en la bitácora. La web no puede romperse por culpa de herramientas accesorias.

## 6. Prohibición de Commits Autónomos (Zero-Trust)
Los agentes tienen acceso a la terminal, pero **nunca deben ejecutar `merci commit` ni `git commit` por su cuenta** para enviar código a producción o empaquetar de forma definitiva. Esa acción es responsabilidad y sello exclusivo de la desarrolladora humana (Mercedes). Solo los agentes SRE/QA pueden ejecutar comandos de *testing* y *linting*.

## 7. Uso Obligatorio de Plantillas (Estandarización)
Cualquier agente que actúe como redactor (DevRel, Publisher, etc.) y deba generar un nuevo documento, está **obligado a consultar el directorio `docs/`** y utilizar la plantilla correspondiente (ej. `plantilla-cuadernillo.md`) como esqueleto inicial. Está estrictamente prohibido inventar estructuras nuevas si ya existe una plantilla oficial, garantizando así la coherencia visual y documental del proyecto.

## 8. Zero-Trust en Resultados (QA Autónomo)
El Orquestador (IDE) y los Agentes **tienen prohibido** dar por válido el trabajo de los scripts de generación de contenido local (Librarian, Blogger, etc.) basándose únicamente en el éxito de la terminal (Exit Code 0). Tras delegar una tarea de generación, el Orquestador **debe obligatoriamente abrir, leer y auditar** el documento resultante para confirmar que cumple con la plantilla, la longitud, y la integridad de los datos (ausencia de truncamiento o alucinaciones) **ANTES** de notificárselo a la desarrolladora humana. El humano debe recibir certezas, no deberes de revisión.

## 9. Optimización de Activos (Zero-Bloat Assets)
Cualquier imagen, vídeo o archivo multimedia generado o descargado por el IDE o los Agentes **debe depositarse obligatoriamente en el directorio de ingesta `.assets-raw/`**. Está terminantemente prohibido alojar o enlazar archivos crudos (PNG, JPG, MP4) directamente en directorios de documentación (`docs/`) o producción (`public/`). Todos los *assets* deben pasar forzosamente por el pipeline `merci-optimizer.py` para su conversión a formatos de ultra-rendimiento (WebP/WebM) y ser enlazados posteriormente desde su ubicación optimizada (ej. `assets/images/`).
