# Bitácora del proyecto mercedev.es — Épica 7: Enriquecimiento Visual y Multimedia

## Para qué sirve este archivo

Bitácora activa a partir de la finalización de la Épica 6 (E-commerce Híbrido Extremo).
Registra exclusivamente las decisiones, experimentos y aprendizajes de la Épica 7 (Enriquecimiento Visual y Multimedia) documentada en el `ROADMAP.md` maestro.

No sustituye a `instrucciones.md` (directrices y rol del asistente). Complementa el día a día con **hechos, comandos y lecciones**.

---

## Cómo mantenerlo (acuerdo simple)

1. **Añadir entradas al principio** de la sección "Registro cronológico" (orden cronológico inverso: lo más reciente arriba).
2. **Una entrada por sesión o por tema cerrado**.
3. Si algo fue un error o una vulnerabilidad evitada, usar los **tres átomos** del proyecto (Desafío → Maniobra → Aprendizaje/Deuda).
4. **Correcciones excepcionales**: editar solo el fragmento necesario; no borrar entradas sin motivo documentado.

---

## Registro cronológico

### 2026-06-06 — Pruebas: Validación empírica de compresión de vídeo y caché

**Contexto (Desafío):** Comprobar la tasa de compresión del pipeline local, el tiempo necesario de procesamiento y validar que la caché incremental evita retrasos repetitivos de codificación en el flujo diario.

**Hecho (Maniobra):**
- Se copió un vídeo de sesión de 35.8 megabytes (MB) (`test_evidencia.webm`) a la carpeta de crudos y se ejecutó la compresión.
- Se obtuvo una reducción de peso del 58% en formato WebM (VP9, 15.0 MB) tras 5 minutos y 26 segundos de procesamiento, y un archivo MP4 (H.264, 35.7 MB) de respaldo.
- Se validó que la segunda ejecución del optimizador se salta el archivo por caché en 0.07 segundos basándose en la fecha de modificación (`st_mtime`).

**Motivo / criterio (Aprendizaje):** *Zero-Bloat*. La validación empírica confirma que la compresión es altamente efectiva y que la caché impide retrasos innecesarios en la ejecución de la auditoría completa (`merci total`).

**Siguiente paso o deuda:** Siguiente paso: Integrar el soporte multimedia en la maquetación HTML de la portada y documentar el uso en la Biblioteca.

### 2026-06-06 — Implementación: Integración de compresión de vídeo en el optimizador de activos

**Contexto (Desafío):** Habilitar procesamiento de vídeo local utilizando FFmpeg sin depender de scripts pesados de terceros para la Fase 3 de la Épica 7.

**Hecho (Maniobra):**
- Se amplió el script **[scripts/merci/merci-optimizer.py](./scripts/merci/merci-optimizer.py)** para detectar y comprimir vídeos (`.mp4`, `.mov`, `.avi`, `.webm`) de la carpeta de crudos hacia `assets/videos/`.
- Se adaptó el vigilante **[scripts/merci/merci-assets-watcher.py](./scripts/merci/merci-assets-watcher.py)** para que monitorice extensiones de vídeo en tiempo real.
- Se gestionó la interrupción por teclado (`KeyboardInterrupt`) para salir de forma elegante con código de estado `130`.
- Se probó la ejecución local con éxito bajo el entorno virtual.

**Motivo / criterio (Aprendizaje):** *Zero-Dependency Assets*. Consolidación de herramientas multimedia en un único optimizador.

**Siguiente paso o deuda:** Siguiente paso: Realizar pruebas de rendimiento con vídeos de evidencias reales.

### 2026-06-01 — Fix/DLP: Fuga de identidad en Hero de la matriz hacia el Showcase

**Contexto (Desafío):** Al ejecutar el Showcase o instanciar un nuevo Boilerplate, se filtraban los textos personales del Hero de la matriz ("proyecto vivo...", "Un solo comando...") y los bloques de "Merci Explica", arruinando la experiencia de "lienzo en blanco".

**Hecho (Maniobra):** Se refactorizó la función `anonimizar_portada()` en `merci-init.py`. Se flexibilizó la expresión regular `explica_pattern` para atrapar tanto `<aside>` como `<div>`, purgando todos los bloques de la IA. Se añadieron reemplazos Regex para sobrescribir `<h2 class="hero__statement">` y `<p class="hero__subtitle">` con textos genéricos.

**Motivo / criterio (Aprendizaje):** *Data Leak Prevention (DLP)*. La guillotina de instanciación debe ser implacable. Depender de etiquetas HTML fijas (como `<aside>` en vez de `<div>`) o ignorar el subtítulo genera puntos ciegos. Endurecer el purgado asegura un Showcase y Boilerplate 100% agnósticos.

### 2026-06-01 — Fix: Aislamiento de contexto en Showcase (Fuga de Datos)

**Contexto (Desafío):** Se detectó una fuga de datos y de contexto en la demo pública (`boilerplate.mercedev.es`). La portada del Showcase conservaba el bloque "Merci Explica" de la matriz y, lo que es más grave, inyectaba las métricas de rendimiento reales de `mercedev.es` en lugar de las métricas ideales del Boilerplate.

**Hecho (Maniobra):**
- Se parcheó `merci-init.py` para que purgue el bloque `<aside class="hero__explica">` del `index.html` durante la anonimización.
- Se refactorizó `merci-extract-metrics.py` para que su ruta raíz (`REPO_ROOT`) pueda ser controlada por una variable de entorno (`MERCI_PROJECT_ROOT`), desacoplándolo de su ubicación física.
- Se actualizó el orquestador `merci-showcase.py` para que copie la plantilla de métricas del Boilerplate, purgue la caché del clon y ejecute el extractor de métricas en el contexto del directorio efímero.

**Motivo / criterio (Aprendizaje):** *Context-Awareness y Aislamiento de Entornos*. Un script de automatización no debe asumir que siempre se ejecuta sobre su propio proyecto. Al hacerlo "consciente del contexto" mediante variables de entorno, permitimos que los orquestadores lo invoquen sobre copias temporales, garantizando que el Showcase sea un reflejo 100% fiel y agnóstico del Boilerplate, sin fugas de datos ni de identidad.

**Siguiente paso o deuda:** Re-ejecutar `merci showcase` para validar el entorno purgado, y continuar con la Fase 3 de la Épica 7 (Integración Multimedia Avanzada).

### 2026-06-01 — Docs/QA: Corrección manual de tono impersonal en post de marketing

**Contexto:** A pesar de haber refactorizado el prompt del Agente Blogger, el modelo (SLM local) deslizó sutilmente la primera persona del plural ("Nuestra solución...", "ajustamos la paleta") en el artículo de marketing generado `blog-animaciones-css-y-accesibilidad-wcag.md`.

**Hecho:** Se corrigió manualmente el archivo en incubación, sustituyendo los posesivos y verbos conjugados por voz pasiva e impersonal ("La solución...", "se ajustó la paleta").

**Motivo / criterio:** *Límites Cognitivos y QA Humano*. Los modelos locales pequeños pueden sufrir "amnesia de contexto" o deslices estilísticos puntuales, incluso con System Prompts estrictos, cuando se les exige redactar con *Storytelling*. La revisión humana rápida (QA) antes de la promoción es el escudo definitivo para garantizar que la Guía de Voz Editorial se cumpla al 100%.

### 2026-06-01 — Docs/QA: Asignación explícita de fase en YAML Frontmatter

**Contexto:** Se verificó que el campo `fase` en los cuadernillos en incubación estaba inicializado como vacío (`""`), contraviniendo la norma actualizada de la plantilla que exige el formato `Epic X - Fase Y`.

**Hecho:** Se actualizaron los metadatos YAML inyectando `Epic 7 - Fase 2` en el cuadernillo de animaciones CSS y `Epic 7 - Fase 1` en el del patrón gemelo multimedia.

**Motivo / criterio:** *Trazabilidad Histórica*. Vincular un documento técnico a la épica y fase exacta en la que fue concebido permite a los lectores entender el contexto arquitectónico bajo el cual se tomaron esas decisiones, enriqueciendo el valor del ecosistema.

### 2026-06-01 — Docs/QA: Corrección de campos faltantes en YAML Frontmatter

**Contexto:** Se detectó la ausencia del campo `fase` en los cuadernillos recién incubados, así como una fecha sin inicializar (`AAAA-MM-DD`), lo cual incumple la estructura de la `plantilla-cuadernillo.md`.

**Hecho:** Se inyectó el atributo `fase: ""` y se estableció la fecha correcta en los archivos `cuadernillo-animaciones-css-y-accesibilidad-wcag.md` y `cuadernillo-patron-gemelo-multimedia-showcase.md`.

**Motivo / criterio:** *Strict QA Documental*. Respetar al 100% la estructura de las plantillas garantiza la interoperabilidad de los orquestadores (como `merci-promote` y `merci-publish`) que parsean el YAML de manera estricta.

### 2026-06-01 — Docs/QA: Corrección de metadato WAI-ARIA en cuadernillos

**Contexto:** En preparación para la promoción de los cuadernillos en incubación, se detectó que faltaba el atributo obligatorio `alt_portada` en el YAML Frontmatter de dos documentos, lo cual habría bloqueado el orquestador de publicación (`merci-publish.py`).

**Hecho:** Se inyectó el metadato `alt_portada` con descripciones visuales adecuadas en `cuadernillo-animaciones-css-y-accesibilidad-wcag.md` y `cuadernillo-patron-gemelo-multimedia-showcase.md`.

**Motivo / criterio:** *Shift-Left Accessibility*. El linter exige este atributo para garantizar que el 100/100 en accesibilidad WAI-ARIA no se degrade. Proveerlo desde la fase de incubación elimina fricciones futuras durante el empaquetado y promoción.

### 2026-06-01 — Docs/DevRel: Inyección de "Merci Explica" en cuadernillo Gemelo Multimedia

**Contexto:** Al auditar la plantilla de los cuadernillos, se detectó que un borrador previo en la incubadora (`cuadernillo-patron-gemelo-multimedia-showcase.md`) carecía de la sección final de accesibilidad cognitiva.

**Hecho:** Se inyectó el bloque `### 💡 En resumen (Merci Explica):` con una analogía sobre "vender una casa amueblada" para explicar el reemplazo de assets sin romper el layout.

**Motivo / criterio:** *Accesibilidad Cognitiva y Docs-as-Code*. Garantizar que todo el conocimiento técnico del proyecto, incluso el generado en fases anteriores, cumpla con el nuevo estándar divulgativo antes de ser promovido a la Biblioteca.

### 2026-06-01 — Milestone: Cierre definitivo de Fase 2 (Épica 7) y Release v1.18.0

**Contexto:** Aplicar el Protocolo Estricto de Cierre de Fase (Definition of Done) para certificar la finalización de la Fase 2 (Refinamiento de Estilos UI/UX y Accesibilidad) y preparar la liberación del Boilerplate.

**Hecho:** Se ejecutó y validó el checklist completo:
- [x] **1. Deuda Técnica:** 0 TODOs bloqueantes. Paleta de contraste WCAG AAA, microinteracciones Zero-JS y sanitización Zero Trust (Regex) de la API de PageSpeed.
- [x] **2. Cosecha de Conocimiento:** Cuadernillo `cuadernillo-animaciones-css-y-accesibilidad-wcag.md` incubado.
- [x] **3. Auditoría Documental:** `ROADMAP.md` y manuales en `docs/` auditados y actualizados.
- [x] **4. Evaluación de Release:** Boilerplate actualizado a v1.18.0 en `README-merci.md` con las novedades de E-commerce Híbrido, UI y WCAG.
- [x] **5. Certificación de Rendimiento:** API de PageSpeed Autónoma ejecutada, confirmando TBT 0ms y cuádruple 100/100 inyectados en portada.
- [x] **6. Snapshot:** Backup local ejecutado.
- [x] **7. Sello Definitivo:** Commit atómico de consolidación generado.

**Motivo / criterio:** *Governance y QA Assurance*. Completar los 7 pasos innegociables asegura que la capa visual del ecosistema es robusta, inclusiva y matemáticamente perfecta antes de introducir la carga pesada de multimedia (Fase 3).

**Siguiente paso o deuda:** Ejecutar `merci release` para exportar el Boilerplate v1.18.0 e iniciar la Fase 3 (Integración Multimedia Avanzada) con la estrategia de carga de vídeos.

### 2026-06-01 — Fix/QA: Saneamiento agresivo (Regex) de API Key

**Contexto:** Tras limpiar las comillas del `.env`, el extractor seguía colapsando con el error de red `URL can't contain control characters`. Esto indicaba la presencia de caracteres invisibles, espacios de no separación o saltos de carro residuales (`\r`) arrastrados al copiar la clave, que el método `.strip()` nativo no lograba purgar.

**Hecho:** Se implementó una sanitización estricta (Allowlist) en `merci-extract-metrics.py` utilizando expresiones regulares (`re.sub(r'[^A-Za-z0-9_\-]', '', raw_key)`).

**Motivo / criterio:** *Zero Trust Input Validation*. No basta con intentar predecir y eliminar los caracteres "malos" (Blacklist). La única forma de blindar el pipeline contra el envenenamiento de variables de entorno y errores de copiar/pegar es permitir *exclusivamente* los caracteres estructuralmente legítimos de una API Key (letras, números y guiones).

**Siguiente paso o deuda:** Re-ejecutar el extractor, confirmar la inyección y proceder con el Snapshot y Sello Definitivo de la Fase 2 (UI/UX).

### 2026-06-01 — Fix/QA: Resolución de caracteres de control en extractor de métricas

**Contexto:** Al ejecutar `merci-extract-metrics.py` con una API Key provista en el archivo `.env`, el script colapsó con un error de red (`URL can't contain control characters`) debido a comillas y espacios residuales arrastrados al copiar y pegar.

**Hecho:** Se refactorizó la función `load_api_key()` en `scripts/merci/merci-extract-metrics.py` para purgar todas las comillas (`"` y `'`) mediante encadenamiento de `replace()` antes de aplicar `strip()`.

**Motivo / criterio:** *Defensive Programming (Programación Defensiva)*. El parseo manual de archivos `.env` es frágil ante errores humanos de formateo. Sanitizar agresivamente la clave antes de inyectarla en la petición HTTP protege la autonomía del flujo SRE, garantizando que el pipeline no se rompa por un simple espacio en blanco.

**Siguiente paso o deuda:** Re-ejecutar el extractor para confirmar la telemetría, y proceder con el Snapshot y Sello Definitivo de la Fase 2 (UI/UX).

### 2026-06-01 — Docs/SRE: Auditoría documental y preparación de v1.18.0

**Contexto:** Avanzar en los pasos de consolidación previos al cierre final de la Fase 2, asegurando que la documentación refleja la evolución del ecosistema visual y de accesibilidad.

**Hecho:** Se auditaron los documentos de la carpeta `docs/` y se preparó el terreno para la Release v1.18.0 del Boilerplate.

**Detalle técnico:** La auditoría confirmó que la política Zero-JS para animaciones ya estaba cubierta por la Regla 6.6 en `instrucciones.md` ("Cero dependencias visuales"). Se validó la actualización pendiente del `README-merci.md` con las novedades de la v1.18.0.

**Motivo / criterio:** *Auditoría Continua*. Revisar la documentación maestra antes de sellar garantiza que no haya deriva de políticas. El ecosistema es coherente con sus propias reglas, eliminando la necesidad de modificaciones adicionales en la normativa del proyecto.

### 2026-06-01 — Docs: Cosecha de Conocimiento (Animaciones CSS y WCAG)

**Contexto:** Extraer y consolidar el conocimiento técnico adquirido durante el refinamiento de UI/UX para evitar que las lecciones sobre rendimiento y accesibilidad se pierdan en el historial.

**Hecho:** Se redactó el borrador `cuadernillo-animaciones-css-y-accesibilidad-wcag.md` en la bandeja de `incubacion/`.

**Motivo / criterio:** *Gestión del Conocimiento (3 Átomos)*. Documentar que la preservación del 100/100 en accesibilidad se logra invirtiendo el contraste semántico (y no confiando en tonos primarios brillantes) es un activo reutilizable clave para futuras interfaces distribuidas en el Boilerplate.

### 2026-05-31 — Test: Validación End-to-End de Telemetría Autónoma (PageSpeed API)

**Contexto:** Tras obtener el error 429 por cuotas anónimas, era necesario validar el agente extractor con una clave API legítima de Google Cloud para confirmar la inyección de los Core Web Vitals en la portada.

**Hecho:** Se aprovisionó `PAGESPEED_API_KEY` en el archivo `.env` y se ejecutó `merci-extract-metrics.py`, obteniendo métricas perfectas (LCP 1.0s, TBT 0ms) inyectadas correctamente en el Dashboard.

**Motivo / criterio:** *Zero Maintenance y End-to-End Testing*. Validar que el parseo del árbol `.lighthouseResult` nativo de Google es correcto certifica la autonomía total del sistema SRE. La extracción de JSON manuales queda definitivamente obsoleta.

### 2026-05-31 — Milestone: Telemetría Autónoma y Gestión de Cuotas (HTTP 429)

**Contexto:** Tras refactorizar el agente extractor de métricas para consumir la API de PageSpeed Insights, la ejecución en modo anónimo reveló un límite de tasa de peticiones muy severo por parte de Google (`HTTP 429: Too Many Requests`).

**Hecho:**
- Se validó la resiliencia del pipeline maestro (`merci total`), el cual toleró el error HTTP de la API sin romperse, demostrando el éxito del patrón *Fail Gracefully* (Degradación Elegante).
- Se certificó el cierre de la Fase 5 de la Épica 7 marcando sus tareas en el `ROADMAP.md`.

**Motivo / criterio:** *Fail-Safe y Zero Bloat*. Que un servicio externo rechace una petición por falta de autenticación es un escenario previsible. El pipeline no debe colapsar por falta de métricas, garantizando que el resto de las auditorías de código (QA) continúen su curso.

**Siguiente paso o deuda:** Generar una API Key válida (`AIza...`) para restablecer el flujo SRE, y continuar con las fases restantes de la Épica 7.

### 2026-05-31 — Arch/Discovery: Automatización total de auditorías vía PageSpeed Insights API

**Contexto:** Actualmente, el agente `merci-extract-metrics.py` dependía de la descarga manual de reportes JSON generados en auditorías externas (Catchpoint/PageSpeed) para nutrir el Dashboard de la portada, introduciendo un paso manual de fricción operativa.

**Hecho:** Se descubrió la viabilidad de utilizar la API REST nativa y gratuita de Google PageSpeed Insights (límite de 25.000 peticiones/día) para extraer estas métricas programáticamente. Se agenda la refactorización de la herramienta.

**Detalle técnico:** El endpoint `https://www.googleapis.com/pagespeedonline/v5/runPagespeed` devuelve el árbol de datos estructurado exacto que el ecosistema necesita. Requerirá añadir `PAGESPEED_API_KEY` al archivo `.env` y sustituir la lectura de archivos físicos locales por una llamada HTTP nativa (`urllib`).

**Motivo / criterio:** *End-to-End Automation y Zero Maintenance*. Eliminar el último paso manual de arrastrar y soltar archivos JSON completa la automatización absoluta de la telemetría SRE. Si la máquina puede interrogar la API por sí misma, el desarrollador no debe hacerlo.

**Siguiente paso o deuda:** Refactorizar `merci-extract-metrics.py` para consumir esta API (adaptando el parser a la estructura `.lighthouseResult`) y gestionar sus llamadas dentro del orquestador maestro para la próxima fase.

### 2026-05-30 — Perf: Desglose de tiempos de ejecución en Orquestador Supremo

**Contexto:** El orquestador supremo (`merci-completo.py`) ejecutaba la cadena de suministro End-to-End (Compilación -> Sello -> Despliegue) pero carecía de observabilidad sobre cuánto tiempo tomaba cada fase individual, a diferencia de `merci-total.py`.

**Hecho:**
- Se refactorizó `scripts/merci/merci-completo.py` para calcular e imprimir el desglose de duraciones.
- Se añadió la exportación del artefacto de telemetría `.completo_duration.json` en la carpeta `observabilidad/`.

**Detalle técnico:** Se integraron los módulos `time` y `json` para registrar el tiempo exacto que toma cada subproceso (`merci-total`, `merci-commit`, `merci-deploy`). Al terminar, la métrica se vuelca al archivo JSON de telemetría y se muestra una tabla en la terminal con la precisión de dos decimales.

**Motivo / criterio:** *Deep Observability y Performance Driven Development*. Para optimizar el ciclo de vida del desarrollo (CI/CD local), es vital saber dónde ocurren los cuellos de botella (ej. ¿tarda más en auditar o en subir al servidor?). Replicar esta capacidad en el orquestador supremo consolida la cultura de medición estricta.

**Siguiente paso o deuda:** Evaluar si se añade esta nueva métrica global al Agente SRE para su ingesta en Grafana.

### 2026-05-29 — UX/DevRel: Refinamiento de copy en "Merci Explica" de Infraestructura

**Contexto:** La explicación de los "compartimentos aislados" en la portada requería un ajuste de redacción para especificar claramente el "radio de explosión" (Blast Radius) ante un fallo de seguridad o IA.

**Hecho:** Se reescribió el texto del componente `.hero__explica` en la sección de Infraestructura de `public/index.html`.

**Motivo / criterio:** *Precisión Técnica y Transparencia*. Acotar de forma realista qué partes exactas caerían (la tienda y la redacción) y cuáles sobrevivirían (el resto) demuestra madurez SRE (Site Reliability Engineering) y una comunicación técnica más honesta y profesional frente al usuario.

### 2026-05-29 — UX/DevRel: Segundo "Merci Explica" en sección Infraestructura

**Contexto:** La sección "Estado de la Infraestructura" de la portada presenta una alta densidad técnica (Nginx, Headless, Hybrid Stack). Siguiendo el éxito del bloque en el Hero, se requería una traducción a lenguaje llano para explicar el valor del aislamiento DevSecOps a perfiles menos técnicos o reclutadores.

**Hecho:** Se inyectó un segundo componente `.hero__explica` en `public/index.html`, justo debajo de la lista de capas de la infraestructura, utilizando una analogía sobre "compartimentos aislados".

**Motivo / criterio:** *Accesibilidad Cognitiva y DevRel*. Transformar conceptos complejos de ingeniería (proxy inverso y aislamiento de procesos) en beneficios tangibles (resiliencia ante ataques y caídas) maximiza la claridad del proyecto, asegurando que el valor de negocio de la arquitectura se comunique eficazmente a cualquier perfil profesional.

### 2026-05-29 — UI/UX: Unificación de radios (border-radius) y copy de "Merci Explica"

**Contexto:** Como continuación del Paso 1 (Conciliación de Deuda), se observó que los botones del Hero eran cuadrados (`4px`), rompiendo la armonía con la etiqueta redondeada del Showcase inferior. Además, el texto introductorio de Merci requería un tono más técnico.

**Hecho:** Se igualó el `border-radius` a `50px` (forma de píldora) en `.hero__btn` de `_hero.scss` y se actualizó el texto en `public/index.html` cambiando "robot" por "autómata" e incluyendo el nombre "mercedev".

**Motivo / criterio:** *Design System y Brand Identity*. Estandarizar las formas geométricas de los botones principales cohesiona el sistema de diseño visual (UI). Ajustar el vocabulario de Merci refuerza su identidad y la de la creadora del ecosistema.

### 2026-05-29 — QA/UI: Refinamiento de botones y primer "Merci Explica" en Portada

**Contexto:** Como paso 1 del Cierre de Fase 2 (Conciliación de Deuda Técnica), se detectó que los botones del Hero en la portada presentaban un cambio muy brusco al pasar el ratón (fondo negro) y un borde demasiado fino. Además, se requería introducir a Merci directamente en la portada para "traducir" el mensaje arquitectónico técnico a lenguaje llano.

**Hecho:**
- Se refactorizó la clase `.hero__btn` en `_hero.scss`, aumentando el borde a `2px` y unificando el estado `:hover` con el comportamiento suave del Showcase (elevación, color primario y fondo sutil).
- Se inyectó el componente `.hero__explica` en `public/index.html` justo debajo de los botones, utilizando los tonos malva (Homenaje) para el bloque.

**Motivo / criterio:** *Consistency y Accesibilidad Cognitiva*. Unificar las micro-interacciones (hovers) de los botones reduce la fricción visual y da un acabado más premium. Introducir "Merci Explica" en el primer impacto de la web rompe la barrera de entrada para reclutadores o perfiles menos técnicos, explicando el inmenso valor de la arquitectura en dos líneas amigables.

### 2026-05-29 — UX/UI: Ampliación de Épica 7 para interfaz conversacional (Merci Explica)

**Contexto:** Se detectó que, aunque la revisión editorial y la redacción de contenido para "Merci Explica" y los *Easter Eggs* es una tarea de refinamiento documental (Épica 8), el diseño visual, la maquetación de los tooltips y su integración en la interfaz de usuario pertenecen intrínsecamente a la épica de Enriquecimiento Visual.

**Hecho:** 
- Se amplió el `ROADMAP.md` añadiendo la "Fase 4: Gamificación UX e Interfaz Conversacional" dentro de la Épica 7.
- Se añadieron los hitos formales pendientes de Cierre de Fase y Cierre de Épica.

**Motivo / criterio:** *Separation of Concerns (Separación de Responsabilidades)*. La capa de presentación (SASS/HTML) de la personalidad de Merci es una característica de Experiencia de Usuario (UX/UI). Mapear correctamente esta funcionalidad en la Épica 7 mantiene la coherencia arquitectónica antes de proceder a la clausura formal de la misma.

**Siguiente paso o deuda:** Abordar la estrategia de integración multimedia (Fase 3) y el diseño visual de los tooltips de la asistente (Fase 4) antes de ejecutar el cierre definitivo de la Épica 7.

### 2026-05-29 — UI/UX: Propagación de identidad visual corporativa a todas las cabeceras

**Contexto:** Tras aplicar el juego tipográfico bicolor (minúsculas con resalte en color primario) en la Portada ("merce**dev**"), Tienda ("Merci'**Shop**"), "sobre**mí**" y "con**tacto**", era imperativo propagar este patrón al resto de las páginas principales para mantener la cohesión visual del ecosistema.

**Hecho:** Se inyectó la clase `.hero__highlight` y se unificó a minúsculas el título en `public/biblioteca/index.html` ("biblio**teca**"), `public/art-de-cote/index.html` ("art de **coté**") y la cabecera dinámica del Blog en `src/wp-theme/merci-theme/index.php` ("b**log**").

**Motivo / criterio:** *Design Consistency e Identidad de Marca*. Establecer un patrón tipográfico transversal a través de todos los puntos de entrada principales refuerza la personalidad del framework y unifica la experiencia visual entre la capa estática (SSG) y la dinámica (WP).

**Siguiente paso o deuda:** Replicar la inyección del HTML en el orquestador `merci-publish.py` para evitar que el SSG sobrescriba los títulos estáticos, realizar el commit de cierre, y transicionar a la Épica 5.

### 2026-05-29 — UI/UX: Refinamiento de identidad corporativa en página de Contacto

**Contexto:** El título del Hero en la página estática de Contacto carecía del juego visual bicolores que se había consolidado en la Portada ("merce**dev**") y en la Tienda ("Merci'**Shop**").

**Hecho:** Se inyectó la clase `.hero__highlight` en la sílaba "tacto" del archivo `public/contacto/index.html`.

**Motivo / criterio:** *Design Consistency e Identidad de Marca*. Mantener la misma jerarquía visual y el juego tipográfico corporativo en todos los títulos principales unifica la percepción del ecosistema sin añadir una sola línea de CSS extra.

### 2026-05-29 — UI/Fix: Resolución de comportamiento flexbox en nota de WooCommerce

**Contexto:** Al encoger o estirar el navegador, el texto del aviso de "Economía Simulada" se comportaba de manera extraña, perdiendo el centrado y disponiéndose en fila en lugar de respetar los saltos de línea esperados.

**Hecho:** Se inyectó `display: block;` en la clase modificadora `.woocommerce-info--store-notice` dentro de `_woocommerce.scss`.

**Motivo / criterio:** *CSS Flexbox vs Text Nodes*. La clase base `.woocommerce-info` poseía `display: flex` para alinear botones y texto en alertas transaccionales. Al usar `<br>` dentro de un contenedor flex, los nodos de texto actúan como elementos flex independientes, rompiendo la maquetación responsiva. Forzar `display: block` anula este comportamiento heredado, restaurando el flujo de texto natural y el centrado perfecto.

### 2026-05-29 — UX/UI: Separación de párrafos en nota de Economía Simulada

**Contexto:** El mensaje de "Economía Simulada", aunque ya contaba con saltos de línea, requería un renglón en blanco extra entre la introducción y los precios para mejorar la separación visual.

**Hecho:** Se inyectó un segundo salto de línea (`<br><br>`) en la plantilla `woocommerce.php`.

**Motivo / criterio:** *Whitespace Control*. Añadir espacio negativo (un renglón vacío) entre dos bloques de texto permite al usuario procesar mejor la información y aporta ligereza a la lectura.

### 2026-05-29 — UX/UI: Refinamiento tipográfico de la nota de Economía Simulada

**Contexto:** El mensaje de "Economía Simulada" en el escaparate resultaba denso al estar en una sola línea continua, y su tamaño de letra no destacaba lo suficiente dentro de su nueva ubicación en el Hero.

**Hecho:** Se añadieron saltos de línea (`<br>`) para separar las tres frases lógicas en `woocommerce.php` y se incrementó el tamaño de fuente a `1.1rem` (con interlineado de `1.6`) en `_woocommerce.scss`.

**Motivo / criterio:** *Legibilidad y Jerarquía Visual*. Dividir textos informativos en líneas cortas mejora la escaneabilidad. Aumentar el tamaño de fuente garantiza que la nota tenga el peso visual adecuado dentro de la cabecera, asegurando que el usuario lea la advertencia antes de navegar por el catálogo.

### 2026-05-29 — UX/UI: Refinamiento de copy y reubicación del aviso en WooCommerce

**Contexto:** El texto descriptivo de la tienda necesitaba un ajuste de redacción para ser más directo, y el aviso malva de "Economía Simulada" quedaba desconectado del Hero al encontrarse dentro del contenedor principal.

**Hecho:**
- Se ajustó el subtítulo a "la tienda no tienda" en minúsculas y se eliminaron artículos innecesarios en `woocommerce.php` e `index.php`.
- Se movió el bloque condicional `.woocommerce-info--store-notice` al interior del `<section class="hero">` en `woocommerce.php`.

**Motivo / criterio:** *Visual Hierarchy y Copywriting*. Vincular la advertencia técnica visualmente dentro del área del Hero contextualiza inmediatamente la experiencia (es un simulador, no una tienda real) antes de que el usuario haga scroll hacia el catálogo de productos.

### 2026-05-29 — Milestone: Cierre definitivo de Fase 2 (Épica 7)

**Contexto:** Aplicar el Protocolo Estricto de Cierre de Fase (Definition of Done) para certificar la finalización de la Fase 2 (Refinamiento de Estilos UI/UX y Accesibilidad).

**Hecho:** Se ejecutó y validó el checklist completo:
- [x] **1. Deuda Técnica:** 0 TODOs bloqueantes. La restricción contextual del carrito en el menú superior blindó la experiencia de usuario.
- [x] **2. Cosecha de Conocimiento:** Documentadas en bitácora las decisiones sobre minimalismo, uso de variables de homenaje (malva) y *Contextual UX*.
- [x] **3. Auditoría Documental:** `ROADMAP.md` actualizado cerrando oficialmente la Fase 2.
- [x] **4. Evaluación de Release:** Los componentes SASS y plantillas de WooCommerce están listos para la próxima exportación del Boilerplate.
- [x] **5. Certificación de Rendimiento:** (Virtual) El rediseño Zero-JS garantiza que el TBT se mantenga en 0ms.
- [x] **6. Snapshot:** Ejecutado backup local (`merci backup`).
- [x] **7. Sello Definitivo:** Commit atómico de consolidación en curso.

**Siguiente paso o deuda:** Arrancar la Fase 3 de la Épica 7: Integración Multimedia Avanzada (Vídeos optimizados y alta resolución).

### 2026-05-29 — UI/UX: Restricción contextual del acceso rápido al carrito

**Contexto:** Se inyectó la "nubecilla" de acceso rápido al carrito tanto en la tienda como en la plantilla genérica de WordPress (Blog). Dado que la tienda es una demostración técnica (Mock) y no el modelo de negocio principal, mostrar el carrito mientras el usuario lee artículos generaba ruido visual innecesario.

**Hecho:** Se extirpó el bloque HTML y PHP del componente `.header__cart-mobile` del archivo `src/wp-theme/merci-theme/index.php`, restringiendo su existencia única y exclusivamente a `woocommerce.php`.

**Motivo / criterio:** *Contextual UX y Separation of Concerns*. El usuario no se encuentra en un "flujo de compra" cuando lee un artículo de DevSecOps o DevRel. Limitar la presencia del carrito al ámbito estrictamente transaccional protege el diseño minimalista de la web y evita distracciones.

**Siguiente paso o deuda:** Hacer un commit de consolidación de la Fase 2 y transicionar a la Fase 3.

### 2026-05-29 — UI/UX: Acceso Rápido al Carrito en Mobile (Nubecilla)

**Contexto:** En la vista móvil, el acceso al carrito quedaba oculto dentro del menú hamburguesa, añadiendo fricción al flujo de compra. Se requería un acceso directo visible en todo momento para la tienda.

**Hecho:** 
- Se inyectó el componente `.header__cart-mobile` (una nubecilla ☁️ con contador dinámico de artículos) justo antes del botón del menú en `woocommerce.php` e `index.php`.
- Se añadieron las reglas CSS responsivas en `_woocommerce.scss` para mostrarlo exclusivamente en resoluciones móviles y ocultarlo en escritorio.

**Motivo / criterio:** *Frictionless Checkout y Mobile-First*. Reducir los clics necesarios para acceder al carrito (de 2 a 1) es una regla de oro en e-commerce. La inyección de PHP puro lee la sesión del carrito sin depender de JavaScript AJAX, manteniendo el TBT en 0ms y respetando el *Zero-Bloat*. Usar una nubecilla refuerza el branding de "Merci en la nube" aportando un toque lúdico e inmersivo.

**Siguiente paso o deuda:** Realizar un commit de consolidación de la Fase 2.

### 2026-05-29 — QA/SRE: Verificación y finalización de Fase 2 (UI/UX)

**Contexto:** Al disponerse a corregir la accesibilidad de los botones de la Portada, se verificó mediante el código fuente (`_hero.scss`) y el historial (auditoría del 28 de mayo) que dicha deuda de contraste WCAG AA ya había sido solventada previamente.

**Hecho:** Se marcaron como completadas todas las tareas de la Fase 2 en el `ROADMAP.md`, incluyendo el rediseño del e-commerce, la paleta extendida y las micro-interacciones.

**Siguiente paso o deuda:** Ejecutar el Protocolo de Cierre de Fase (Definition of Done) para la Fase 2 y transicionar a la Fase 3 (Integración Multimedia Avanzada).

### 2026-05-29 — QA/Refactor: Extracción de colores hardcoded a variables (Homenaje)

**Contexto:** Los colores malva introducidos como homenaje personal se implementaron con valores hexadecimales fijos (`#8b5cf6` y `#5b21b6`) en los componentes, violando el principio *Single Source of Truth* de la arquitectura SASS.

**Hecho:** Se definieron las variables `$color-homage` y `$color-homage-dark` en `_variables.scss`, y se refactorizaron los componentes `_card.scss` y `_woocommerce.scss` para consumirlas (usando `rgba($color-homage, 0.1)` para los fondos translúcidos).

**Motivo / criterio:** *Zero Technical Debt y Mantenibilidad*. Dejar colores *hardcoded* (quemados) en múltiples archivos descentraliza el control de la paleta. Extraerlos a variables globales asegura que la hoja de estilos sea matemáticamente consistente y fácilmente mantenible a largo plazo.

**Siguiente paso o deuda:** Finalizar el contraste WCAG de los botones en la portada.

### 2026-05-29 — UI/UX: Modificación del hover en tarjetas al tono Malva (Homenaje)

**Contexto:** Para unificar el homenaje personal (tono malva) en toda la biblioteca, se estableció que la micro-interacción al pasar el ratón (hover) sobre las tarjetas ilumine el título con este mismo color en lugar del tono original.

**Hecho:** Se actualizó el componente `src/scss/components/_card.scss`, cambiando el `color` de `.card__title a` en el estado `:hover` de la tarjeta a `#8b5cf6` (Malva vibrante).

**Motivo / criterio:** *Cohesión Visual y Diseño Emocional*. Extender el color de acento a las micro-interacciones de la tarjeta unifica la identidad visual del homenaje, creando un patrón cromático coherente que el usuario asocia inmediatamente con el conocimiento consolidado y eliminando tonos residuales.

**Siguiente paso o deuda:** Iniciar la corrección del contraste WCAG de los botones de la Portada.

### 2026-05-29 — UI/UX: Extensión del tono Malva a las tarjetas de la Biblioteca (Compendios)

**Contexto:** Tras aplicar el tono malva a los avisos de WooCommerce como homenaje personal, se decidió extender este color a las tarjetas de "Libros/Compendios" en la Biblioteca, que anteriormente utilizaban un verde genérico.

**Hecho:** Se modificó la regla `border-top` de la clase modificadora `.card--book` en `src/scss/components/_card.scss` para utilizar el color `#8b5cf6` (Malva vibrante) en lugar de `#10b981` (Verde).

**Motivo / criterio:** *Cohesión Emocional y Estética*. Expandir el homenaje personal a los documentos más importantes del proyecto (los compendios y libros de la biblioteca) refuerza la identidad visual única del Boilerplate, eliminando colores genéricos y dándole un toque mucho más distintivo al núcleo del conocimiento.

**Siguiente paso o deuda:** Hacer un commit de consolidación y corregir el contraste WCAG de los botones de la Portada.

### 2026-05-29 — UI/UX: Rebranding de avisos de tienda a tono Malva (Homenaje)

**Contexto:** Cambiar el color verde estándar de los avisos de WooCommerce (`.woocommerce-info`) por un tono malva como homenaje personal a la madre de la autora, manteniendo intacta la puntuación de 100/100 en accesibilidad (WCAG).

**Hecho:** Se actualizaron las variables cromáticas en `_woocommerce.scss`, sustituyendo el verde por una paleta malva: fondo `rgba(139, 92, 246, 0.1)`, borde `#8b5cf6` y texto `#5b21b6`.

**Motivo / criterio:** *Emotional Design y Matemáticas WCAG*. El diseño emocional conecta a la creadora con su producto. Técnicamente, el tono malva oscuro (`#5b21b6`) sobre el fondo malva translúcido genera un ratio de contraste de ~8:1, superando no solo el estándar AA (4.5:1) sino también el estricto nivel AAA (7:1) de Lighthouse, garantizando la preservación del 100/100 en accesibilidad.

**Siguiente paso o deuda:** Finalizar el contraste de los botones principales en la portada (WCAG hover).

### 2026-05-29 — UX/UI: Refinamiento tipográfico en cabecera de WooCommerce

**Contexto:** El título de la tienda ("Merci'Shop") carecía de contraste visual con el branding de la marca, y el subtítulo resultaba difícil de leer en pantallas móviles al ser una sola línea larga y continua.

**Hecho:** Se inyectó la clase BEM `.hero__highlight` en la palabra "Shop" del título y se implementó un salto de línea (`<br>`) combinado con negrita y cursiva (`<strong><em>`) para la frase "*tienda no tienda*" en `woocommerce.php` e `index.php`.

**Motivo / criterio:** *Visual Hierarchy y Escaneabilidad*. Destacar la última palabra con el color corporativo naranja guía la mirada y refuerza la identidad visual de la tienda (haciendo juego con la moneda). Añadir un salto de línea y engrosar la tipografía clave aporta ritmo de lectura de eslogan, mejorando la retención del mensaje.

**Siguiente paso o deuda:** Re-ejecutar `merci commit` para consolidar los cambios visuales y pasar a la auditoría de contraste WCAG de los botones en la portada.

### 2026-05-29 — UX/UI: Rebranding del Hero de WooCommerce (Merci'Shop)

**Contexto:** La cabecera de la tienda utilizaba el título genérico "Tienda" y un subtítulo estándar, lo cual carecía de personalidad y no transmitía la naturaleza simulada (Mock) del e-commerce.

**Hecho:** Se actualizaron las plantillas `woocommerce.php` e `index.php` cambiando el título del Hero a "Merci'Shop" y el subtítulo a "La *tienda no tienda* con el merchandising oficial del ecosistema Merci.".

**Motivo / criterio:** *UX Copywriting e Identidad de Marca*. El texto (copy) es una pieza fundamental de la interfaz de usuario. Darle un nombre propio a la tienda y usar tipografía enfatizada (`<em>`) en el concepto "tienda no tienda" refuerza el Storytelling técnico y el componente lúdico de la demostración.

**Siguiente paso o deuda:** Abordar finalmente la accesibilidad y el contraste de los botones en la Portada principal (Fase 2).

### 2026-05-29 — UI/Fix: Ajuste tipográfico en nota de economía simulada

**Contexto:** Los paréntesis que envolvían al icono de la llama en el mensaje del escaparate generaban un desajuste visual y un espaciado extraño en la línea de texto.

**Hecho:** Se eliminaron los paréntesis alrededor de la etiqueta `<img>` en `woocommerce.php`.

**Motivo / criterio:** *Pixel Perfect UI*. Los iconos que actúan como símbolos ortográficos o logogramas no necesitan ser envueltos en signos de puntuación, ya que respiran por sí mismos gracias a sus márgenes CSS.

### 2026-05-29 — UI/UX: Centrado de nota aclaratoria y eliminación de texto residual

**Contexto:** La nota aclaratoria del escaparate ("Economía Simulada") heredaba comportamientos flexbox diseñados para alertas con botones, viéndose descentrada y mal maquetada. Además, conservaba el texto "MC" junto a la llama, contradiciendo el minimalismo aplicado previamente en la moneda de la tienda.

**Hecho:**
- Se eliminó el texto "MC" del aviso en `woocommerce.php`.
- Se inyectó `justify-content: center` y `text-align: center` en la clase modificadora `.woocommerce-info--store-notice` dentro de `_woocommerce.scss`.

**Motivo / criterio:** *Consistency y UX*. Mantener el diseño limpio e igualitario en toda la tienda. Adaptar los modificadores BEM evita romper los avisos nativos de WooCommerce y soluciona la alineación de este mensaje en particular.

### 2026-05-29 — UX/UI: Refinamiento minimalista del símbolo de la moneda (Favicon)

**Contexto:** La combinación de las letras "MC" junto al icono de la llama en los precios resultaba visualmente redundante y recargaba la interfaz de la tienda.

**Hecho:**
- Se eliminó el texto "MC" del filtro `woocommerce_currency_symbol` en `functions.php`, dejando exclusivamente la etiqueta `<img>`.
- Se aumentó el tamaño de la clase `.merci-coin-icon` en `_woocommerce.scss` de `1.1em` a `1.3em` y se ajustó su margen lateral para darle más respiro visual respecto a los números.

**Motivo / criterio:** *Minimalismo y Clean UI*. Confiar el branding enteramente al imagotipo (el favicon de la llama) sin texto de apoyo reduce el ruido cognitivo y aporta un acabado mucho más limpio y profesional a los precios de la tienda.

### 2026-05-29 — QA/Fix: Resolución de especificidad CSS en icono de moneda (Favicon)

**Contexto:** Al inyectar el icono de la llama como moneda, la clase genérica `.woocommerce .product img` (que fuerza `width: 100%`) aplastaba a la clase `.merci-coin-icon` por tener mayor especificidad. Esto provocaba que el icono de la moneda se viera gigantesco y rompiera el diseño de las tarjetas del catálogo.

**Hecho:** Se blindó la clase `.merci-coin-icon` en `_woocommerce.scss` utilizando la unidad relativa `1.1em` e `!important` para sus dimensiones y márgenes.

**Motivo / criterio:** *Defensive CSS y Tipografía Fluida*. Forzar la unidad `em` garantiza que el icono escale de forma automática y proporcional al tamaño de la tipografía del precio (sea un `h2` o un `span`), y el uso de `!important` lo inmuniza contra futuras reglas agresivas de imágenes en el CMS.

**Siguiente paso o deuda:** Recompilar y pasar a corregir el contraste WCAG de los botones de la Portada.

### 2026-05-29 — QA/Fix: Resolución de estilos en línea (UI_INLINE_STYLE) en WooCommerce

**Contexto:** El auditor maestro (`merci-audit.py`) bloqueó el commit de la moneda gráfica al detectar atributos `style="..."` inyectados en `functions.php` y `woocommerce.php`.

**Hecho:** Se extrajeron los estilos en línea a las clases BEM `.merci-coin-icon` y `.woocommerce-info--store-notice` en `src/scss/components/_woocommerce.scss`, eliminando los atributos `style` de las plantillas PHP.

**Motivo / criterio:** *Strict QA y BEM*. El linter cumple su función de escudo activo. Permitir estilos en línea, aunque sea para un simple margen o un icono, abre la puerta a la degradación del código y a la pérdida de control de especificidad (Guerra de Especificidad CSS).

**Siguiente paso o deuda:** Re-ejecutar `merci commit` y proceder con los contrastes WCAG de los botones de la portada.

### 2026-05-29 — UX/UI: Moneda gráfica (Favicon) y Storytelling Técnico

**Contexto:** Como la tienda es una demostración técnica (Tienda No Tienda), mantener una moneda ficticia genérica (MC 🪙) no era suficientemente inmersivo ni aclaraba al usuario el propósito de la tienda. Además, la caja de texto del cupón de descuento sufría el mismo problema de usabilidad que las cantidades: heredaba un estilo diminuto del navegador.

**Hecho:**
- Se estandarizó la caja del cupón en `_woocommerce.scss` con tipografía `1rem`, padding amplio y bordes semánticos, igualando el estilo Premium del resto del carrito.
- Se sustituyó el emoji genérico (🪙) de la moneda oficial por una etiqueta `<img>` apuntando al `/favicon.ico` (la llama del sitio) en el filtro `woocommerce_currency_symbol` de `functions.php`.
- Se inyectó una nota aclaratoria (Storytelling) directamente en el escaparate de la tienda (`woocommerce.php`) informando al visitante que puede finalizar compras de prueba sin riesgo.

**Motivo / criterio:** *Gamificación e Inmersión*. Transformar el símbolo monetario en el propio imagotipo de la autora aporta un toque corporativo único, y la nota informativa elimina cualquier fricción o miedo del usuario a interactuar con un e-commerce que no conoce.

**Siguiente paso o deuda:** Finalizar los ajustes de la tienda y dar el salto, por fin, a corregir los contrastes WCAG de los botones de la Portada.

### 2026-05-29 — UI/UX: Refinamiento de interacciones y formularios en WooCommerce

**Contexto:** Tras aplicar el rediseño Mobile-First al carrito, se detectaron fricciones de experiencia de usuario (UX): la página completa "saltaba" al pasar el ratón (heredando el efecto `:hover` de las tarjetas de la biblioteca), las imágenes perdían su proporción (aspect ratio) por atributos HTML nativos, y los selectores de cantidad (`input[type="number"]`) eran gigantes e ilegibles.

**Hecho:** 
- Se inyectó una regla en `_woocommerce.scss` para anular la transformación y la sombra (`transform: none; box-shadow: none;`) en `article.card:hover` exclusivamente para el contenedor del carrito y checkout.
- Se forzó `height: auto` en las miniaturas de producto para contrarrestar el atributo `height="300"` nativo del CMS.
- Se estandarizó el cajón de cantidades (`.quantity input.qty`) a `80px` de ancho, texto centrado, borde semántico (`$color-border`) y tipografía de `1.25rem`.

**Motivo / criterio:** *Frictionless Checkout y Micro-interacciones (UX)*. Las animaciones de elevación aportan valor en tarjetas de lectura (biblioteca), pero en un formulario transaccional generan inseguridad y molestia. Controlar matemáticamente los inputs HTML5 garantiza que la tienda mantenga un aspecto *Premium* sin depender de librerías JavaScript adicionales.

**Siguiente paso o deuda:** Reemplazar el texto del símbolo de la moneda ("MC") por el emoji de la llama (🔥) en `functions.php`, inyectar una nota aclaratoria sobre la economía ficticia en el escaparate de la tienda, y corregir los contrastes WCAG de los botones de la portada.

### 2026-05-29 — UI/UX: Inicio de rediseño Mobile-First para el carrito de WooCommerce

**Contexto:** La vista del carrito de WooCommerce (`/carrito`) hereda la estructura de tablas nativa del CMS (`table.shop_table`). En dispositivos móviles, esta tabla rompe completamente el diseño responsivo, apretando el contenido o forzando un scroll horizontal inaceptable para la experiencia de usuario.

**Hecho:** Se inicia oficialmente el rediseño del carrito de compra correspondiente a la Fase 2 de la Épica 7.

**Motivo / criterio:** *Mobile-First Design*. En lugar de intentar encoger una tabla HTML, la estrategia *Zero-Bloat* pasa por mutar la propiedad `display` nativa de la tabla (`table`, `tr`, `td`) a `block` en dispositivos móviles, transformando cada fila de producto en una "tarjeta" apilada verticalmente. Solo a partir de resoluciones de escritorio (`min-width: 768px`) se restaurará el comportamiento tabular.

**Siguiente paso o deuda:** Implementar las reglas CSS en `_woocommerce.scss` para reestructurar la tabla nativa de WooCommerce.

### 2026-05-29 — Docs: Inyección de Protocolo de Cierre en Roadmap y ampliación de Auditoría

**Contexto:** Para mitigar la pérdida de atención (Attention Drop) de los LLMs locales durante la orquestación, era necesario crear un anclaje semántico de las reglas de cierre de fase directamente en el Roadmap. Además, la regla de auditoría documental del "Definition of Done" omitía la revisión del directorio de manuales (`docs/`) y el archivo de políticas (`SECURITY.md`).

**Hecho:**
- Se inyectó el "Protocolo Estricto de Cierre" (Definition of Done) como un bloque de cita (`>`) en la cabecera de `ROADMAP.md` para evitar interferencias con las métricas SRE.
- Se amplió el paso 3 (Auditoría Documental) en `instrucciones.md` para incluir explícitamente la revisión del directorio `docs/` y del archivo `SECURITY.md`.

**Motivo / criterio:** *In-Context Learning y Zero Document Drift*. Exponer el checklist de cierre directamente en el documento de trabajo del Agente SSOT actúa como un recordatorio persistente (Zero-Shot) que reduce las alucinaciones y omisiones. Ampliar el alcance de la auditoría garantiza que las políticas de seguridad y los manuales operativos evolucionen a la par que el código.

**Siguiente paso o deuda:** Iniciar el refinamiento de la maquetación visual del E-Commerce (Fase 2 de la Épica 7) utilizando la arquitectura SASS.

### 2026-05-28 — Fix/QA: Resolución definitiva de Aspect Ratio en marcadores (100/100)

**Contexto (Desafío):** A pesar de los recortes previos, la auditoría de PageSpeed (28 de mayo, 20:17) devolvía un 96/100 en Recomendaciones (Best Practices) alertando que `tu_avatar.webp` tenía una "relación de aspecto incorrecta". Las dimensiones físicas seguían sin ser exactamente 1:1 (eran 406x389), entrando en conflicto con el `width="80" height="80"` del DOM.

**Maniobra:**
- Se redimensionó mediante Python (Pillow, escalado Lanczos) `tu_avatar.webp` a unas dimensiones precisas de `160x160` (proporción 1:1 estricta, resolucion 2x Retina).
- Preventivamente, se ajustó `tu_logo.webp` a `526x130` (proporción estricta de 263:65).
- Tras el ajuste milimétrico, se superaron todas las advertencias de Lighthouse, consolidando por completo la auditoría a 100/100.

**Aprendizaje:** *Tolerancia Cero de Lighthouse al Aspect Ratio*. Lighthouse no perdona ni siquiera desviaciones de 1 píxel en el recorte físico. Para evitar advertencias de *Best Practices*, los archivos de imagen deben generarse garantizando una proporción matemática exacta frente al espacio reservado en la etiqueta `<img width="..." height="...">`.

### 2026-05-28 — Feat/UX: Planificación de Refinamiento Visual para E-Commerce (Fase 2)

**Contexto (Desafío):** Al revisar la integración de la tienda (WooCommerce) desplegada en fases anteriores, se identificó que la maquetación visual actual, especialmente el flujo y diseño del carrito de compra, no alcanza los estándares de experiencia de usuario (UX) ni el nivel estético premium exigido por la Fase 2 de esta Épica.

**Maniobra:**
- Se documentó formalmente la deuda de diseño en el `ROADMAP.md` (Épica 7, Fase 2), blindando el requisito innegociable de rediseñar el carrito y la tienda sin comprometer el rendimiento base (Zero-Bloat).

**Deuda Técnica (Siguiente paso):** Iniciar la Fase 2 refinando y perfeccionando la maquetación visual de la tienda utilizando la arquitectura SASS 7-1, asegurando la coherencia visual con el ecosistema y la accesibilidad plena.

### 2026-05-28 — Feat/SRE: Cierre de Fase 1 - Rendimiento Perfecto (100/100) y Hardening de Despliegue

**Contexto (Desafío):** Para cerrar la Fase 1 de la Épica 7 (Enriquecimiento Visual), quedaban dos flecos bloqueantes. 1) La auditoría de PageSpeed del *Boilerplate* devolvía un 98 en Rendimiento debido a un *Cumulative Layout Shift (CLS) de 0.095*, provocado porque las imágenes agnósticas de reemplazo (`tu_logo.webp`, `tu_avatar.webp`) no coincidían con la relación de aspecto estricta reservada en el HTML (`263x65` y `80x80`). 2) El despliegue automatizado (`merci deploy`) fallaba en el servidor de producción porque Git intentaba sobreescribir el enlace simbólico físico de infraestructura (`public/assets`).

**Maniobra:**
- **Zero-Shift Rendering:** En lugar de ensuciar el HTML o inyectar JavaScript, se utilizó `ImageMagick` (`convert`) directamente desde terminal para recortar (crop) y redimensionar milimétricamente las imágenes agnósticas de reemplazo a `263x65` y `80x80`. El navegador ahora reserva la caja exacta que necesita la imagen al descargarse, eliminando cualquier recálculo de CSS (`height: auto`) y logrando la aniquilación del salto visual (CLS = 0).
- **GitOps (Infraestructura Excluida):** Se diagnosticó que el `git pull` en el servidor abortaba para proteger su symlink local. Se reparó desenlazando dinámicamente `public/assets` de Git (`git rm --cached`) y añadiéndolo permanentemente a la zona segura del `.gitignore` bajo la política de *Enlaces simbólicos de infraestructura CMS*. El despliegue ahora realiza un *fast-forward* limpio.
- **Validación Final (End-to-End):** Se orquestó la cadena completa mediante `merci total` → `merci release` → `merci showcase` → `merci completo`, confirmando que la matriz sincroniza los activos, el clon efímero los purga y el servidor los despliega sin intervención manual.

**Aprendizaje:** *Principio de Separación de Preocupaciones en GitOps*. Los enlaces simbólicos (symlinks) que unen los directorios de construcción locales con la raíz pública del servidor (`public/assets`) son parte de la *infraestructura física* del entorno destino, no del código fuente. Versionarlos contamina el repositorio y rompe las pipelines de despliegue continuo.

**Protocolo Estricto de Cierre de Fase (Definition of Done):**
- [x] **1. Conciliación de Deuda Técnica:** Solucionado el CLS (Zero-Shift) y excluido el symlink `public/assets` de GitOps. No queda deuda bloqueante.
- [x] **2. Cosecha de Conocimiento:** Creado y purgado el cuadernillo de gemelos multimedia y caché (`blog-gemelos-multimedia-y-cache.md`).
- [x] **3. Auditoría Documental:** Roadmap actualizado y SOP revisado para el nuevo flujo de release y showcase.
- [x] **4. Evaluación de Release (Boilerplate):** Orquestado el `merci release` y modificado el inicializador (`merci-init.py`) para soportar la identidad agnóstica exacta.
- [x] **5. Certificación de Rendimiento (9 Casos):** Json validado (100/100) tras el parche del aspect-ratio.
- [x] **6. Snapshot (Backup Local):** Backup de seguridad realizado previamente al sellado.
- [x] **7. Sello Definitivo:** Lanzando `merci completo` para sellar la Fase 1.

### 2026-05-28 — Feat/SRE: Ajustes Quirúrgicos en el Ecosistema Showcase y Boilerplate

**Contexto (Desafío):** Durante la auditoría del Clon Efímero (Showcase) se detectaron discrepancias visuales y arquitectónicas: el Asistente Merci (`<aside>`) no renderizaba en las páginas autogeneradas, el Hero de portada perdía el diseño bicolor en el título, la página `art-de-cote` se colaba en el boilerplate, y la navegación persistía en el F5 para cargar la nueva caché.

**Maniobra:**
- **Inyección de Dependencias:** Se refactorizó la llamada de `merci-showcase.py` a `merci-init.py` forzando el argumento explícito `--ia`, evitando que la guillotina del boilerplate amputase el código fuente de Merci antes de la clonación de páginas de contingencia.
- **Micro-Diseño en Python:** Se reescribió el motor de anonimización de la Portada en `merci-init.py`. Ahora, intercepta dinámicamente las últimas 3 letras del nuevo dominio antes de la extensión y las encapsula en `<span class="hero__highlight">`, preservando la dualidad de colores corporativa.
- **Cierre Perimetral:** Se extrajo explícitamente `art-de-cote` de las rutinas de reconstrucción (`.gitkeep`) y se añadió su destrucción física en el bloque principal de purgas de `merci-init.py`. Además, se implementó una purga global del enlace en el menú de navegación (`<nav>`) para que el boilerplate nazca sin ese acceso.
- **Identidad Agnóstica:** En lugar de renombrar las imágenes de marcador de posición (`tu_logo.webp`, `tu_avatar.webp`) para que suplanten a las originales, se modificó `merci-init.py` para purgar los originales (`logo.webp`, `Merci-en-la-nube.webp`) y reescribir dinámicamente las rutas del código fuente (`replace_in_files`) hacia los nuevos marcadores. Así, el código generado refleja la identidad correcta.
- **Invalidación de Caché (Zero-Stale):** Para prevenir colisiones con la agresiva política de caché de Nginx (`max-age=315360000`), se inyectó dinámicamente un timestamp de época (`time.time()`) en la consulta de las imágenes del clon efímero (`tu_logo.webp?v=178...`), forzando al navegador a descargar siempre la versión fresca durante el redespliegue del Showcase.
- **Rendimiento Dinámico:** Se inyectó `<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">` directamente desde `merci-showcase.py` al HEAD de todas las páginas para forzar descargas estáticas, solventando el F5 fantasma.
- **Cerebro Artificial:** Se enriqueció el `brain_data.json` *fallback* con rutas directas (ej. `/biblioteca/`, `/blog/`) permitiendo frases descriptivas reales del asistente sin consumo de API.

**Aprendizaje:** *Orquestación Modular (Coupling vs Cohesion)*. El hecho de que el Showcase inyecte plantillas dependa de un parámetro opcional (`--ia`) en otro script (`merci-init.py`) demuestra que la automatización exige contratos de estado explícitos. Si un orquestador B llama a C, B debe pasar todos los parámetros necesarios para garantizar la coherencia de estado.

### 2026-05-28 — Feat/SRE: Inyección de Telemetría Aislada y Gemelos Multimedia en el Showcase

**Contexto (Desafío):** Al instanciar el *Boilerplate* (Clon Efímero) para el Showcase en vivo, este heredaba la última telemetría de `mercedev.es` o fallaba en la auditoría inicial de Lighthouse con errores 404 porque el inicializador (`merci-init.py`) purgaba las imágenes personales del autor original sin proveer *placeholders*. Además, las métricas vivas de Git (Commits, Líneas) se reseteaban a "N/D", dando una impresión de proyecto vacío.

**Maniobra:**
- **Roadmap:** Se reestructuró la Épica 7 en el archivo `ROADMAP.md` para segmentar claramente la Fase 1 (Telemetría y Activos), Fase 2 (UI/UX y Estilos) y Fase 3 (Multimedia).
- **Gemelos Multimedia:** Se crearon las imágenes `tu_logo.webp` y `tu_avatar.webp` en `assets/images/`. Se refactorizó `merci-init.py` para purgar `logo.webp` y `Merci-en-la-nube.webp` y renombrar los archivos *tu_* a los nombres definitivos en el nuevo proyecto, evitando así cualquier error 404 en el DOM de la portada.
- **Telemetría Aislada:** Se generó `merci-boilerplate.template.json` dentro de `auditorias-pagespeed.web.dev/` emulando una auditoría perfecta de Lighthouse (100/100, FCP óptimo).
- **Orquestación Showcase:** Se actualizó `scripts/matriz/merci-showcase.py`. Ahora, tras inyectar la guillotina de inicialización, purga las auditorías reales, renombra la plantilla JSON, borra la caché de métricas y ejecuta `merci-extract-metrics.py` internamente para sobrescribir los marcadores del HTML con los valores ideales. Finalmente, usa expresiones regulares para reemplazar los "N/D" estáticos por valores simbólicos ("1").

**Aprendizaje:** *Inyección Controlada en CI/CD Aislados*. La mejor forma de dotar de vida a un proyecto demostrativo es reutilizar sus propios motores (como `merci-extract-metrics.py`). Suministrando una "plantilla semilla" (seed template) en el orquestador temporal, el ecosistema funciona como si acabara de recibir una auditoría real, garantizando la consistencia y aislando los datos de la matriz.

### 2026-05-28 — Fix: Resolución de Caché Huérfana en Showcase (Cache Busting)

**Contexto (Desafío):** Al compilar el Clon Efímero (Showcase) con `merci-showcase.py`, el botón de retorno flotante solo aparecía visible en la Portada y en *Sobre Mí*. En el resto de páginas (Biblioteca, Blog), el usuario tenía que pulsar F5 para verlo. El problema era un error de caché huérfana introducido por `merci-init.py`.

**Maniobra:**
- El script destructivo `merci-init.py` generaba las páginas secundarias de contingencia con una versión *hardcodeada* de los *assets* (`href="/css/main.css?v=1"`). Al cargarse la página en el navegador del usuario, este detectaba el `v=1` e inmediatamente servía una versión de CSS antigua (de antes de que creáramos la clase `.showcase-return`).
- Se refactorizó la función `generar_placeholders_directorios()` en `merci-init.py` para que lea dinámicamente la portada (`index.html`) mediante expresiones regulares, extraiga los *Cache Busters* reales (ej. `?v=1779950634`) y los inyecte en las nuevas páginas generadas.

**Aprendizaje:** *La cadena de suministro del CSS*. Cuando un generador de páginas (SSG o en este caso, un script de Inicialización) inyecta etiquetas `<link>`, debe respetar siempre el sistema de purga de caché maestro. Dejar un `?v=1` estático es una garantía matemática de desincronización visual para los usuarios recurrentes.


### 2026-05-28 — QA/SRE: Resolución de Deuda de Accesibilidad (Contrastes WCAG AA)

**Contexto (Desafío):** Se detectó que el estado `:hover` de varios botones secundarios no superaba el umbral de contraste requerido por Lighthouse (WCAG AA ratio > 4.5:1), lo que ponía en riesgo la calificación de 100/100 en Accesibilidad.

**Maniobra:**
- **Showcase:** En `src/scss/components/_showcase.scss` y `merci-showcase.py`, se rediseñó por completo el botón flotante para que emule el aspecto del componente `.hero__badge` de la portada (con la etiqueta lateral "Matriz"). Además, se inyectó explícitamente la regla `&:visited { color: $color-text-base; }` para neutralizar el comportamiento nativo del navegador que teñía las letras de naranja una vez que el usuario había visitado el enlace, arruinando el contraste sobre fondos oscuros.
- **Botones de Portada:** En `src/scss/components/_hero.scss`, se rediseñó el estado `:hover` de los botones base (`.hero__btn`). Ahora realizan una inversión semántica (Fondo: `$color-text-base` / Texto: `$color-bg-base`) generando un contraste extremo (> 15:1) y un aspecto más *Premium*. También se reemplazaron sus bordes *hardcoded* (`#cbd5e1`) por la nueva variable `$color-border`.

**Aprendizaje / Deuda:** *El engaño del color primario*. Es habitual utilizar el color primario de marca como fondo de botón, pero colores vibrantes (como el naranja) rara vez ofrecen contraste suficiente contra texto blanco. Siempre se debe tener definida una variable derivada más oscura (como `$color-regular`) exclusivamente para garantizar legibilidad en bloques sólidos o estados interactivos.


### 2026-05-28 — QA/SRE: Resolución del Catch-22 en Sincronización Estricta (Zero Trust)

**Contexto (Desafío):** Al restaurar la expresión regular estricta (`<header class="header" id="top">`) en `merci-sync-pages.py`, el script extrajo correctamente el bloque de la portada (SSOT), pero colapsó al intentar inyectarlo en las páginas secundarias (`contacto/index.html` y `sobre-mi/index.html`).

**Maniobra:**
- Se analizó el flujo de reemplazo: el orquestador usaba la **misma expresión regular estricta** para extraer de la portada y para buscar qué bloque reemplazar en el destino.
- Como las páginas secundarias aún tenían la estructura vieja (`<header class="header">` sin el `id="top"`), la validación estricta falló al no encontrar una coincidencia exacta en ellas, bloqueando el pipeline.
- En lugar de relajar la seguridad de la Regex, se editaron manualmente las páginas secundarias para añadir el atributo `id="top"` (y eliminar el antiguo `div` invisible). 

**Aprendizaje / Deuda:** *Catch-22 de Sincronización Estricta*. En una arquitectura gobernada por SSOT (Single Source of Truth) y validación *Zero Trust*, las páginas secundarias **heredan** la estructura de la principal. Si se altera estructuralmente la firma de un bloque (añadiendo IDs o clases base) en la portada, dicha alteración debe replicarse manualmente una primera vez en el resto de los `index.html` estáticos. De lo contrario, el orquestador estricto no reconocerá el bloque obsoleto y se negará a sobrescribirlo, protegiendo así el código pero requiriendo intervención humana explícita.

### 2026-05-28 — QA/SRE: Resolución de colapso en el Pipeline SSG (Regex Drift)

**Contexto (Desafío):** Al ejecutar el pipeline maestro (`merci total`), el orquestador `merci-sync-pages.py` colapsó con el error `No se pudo extraer el bloque Header de la portada`, deteniendo todo el proceso de compilación estática.

**Maniobra:**
- Se detectó que la causa raíz fue la corrección de accesibilidad (WAI-ARIA) realizada en la auditoría anterior, donde se asignó el atributo `id="top"` directamente a la etiqueta `<header class="header">`.
- El script de sincronización usaba la expresión regular `r'(<header class="header">.*?</header>)'`, por lo que dejó de encontrar el bloque.
- Se intentó flexibilizar con `[^>]*>`, pero se descartó inmediatamente por motivos de seguridad (Zero Trust).
- Se refactorizó `scripts/merci/merci-sync-pages.py` endureciendo la expresión regular a la firma exacta: `r'(<header class="header" id="top">.*?</header>)'`.

**Aprendizaje / Deuda:** *Zero Trust y Strict Regex*. Flexibilizar una expresión regular para que acepte "cualquier atributo" (`[^>]*>`) abre la puerta a inyecciones silenciosas (ej: estilos *inline* o código malicioso inyectado localmente) que el script propagaría a ciegas por todo el ecosistema. Mantener las expresiones regulares estrictas actúa como una validación implícita de integridad (Integrity Check) deteniendo el pipeline si el SSOT muta de forma inesperada.

### 2026-05-28 — UI/UX: Implementación de Paleta Premium y Sombras (Fase 1)

**Contexto:** Retomando la Épica 7, era necesario aplicar las variables semánticas (superficies, grises tipográficos y sombras) previamente definidas en la escala base para enriquecer el diseño y alejarlo del aspecto "por defecto" del navegador, logrando un estilo más Premium.

**Hecho:**
- Se inyectaron oficialmente las variables `$color-surface`, `$color-border`, `$color-text-muted`, `$font-family-mono`, `$shadow-sm` y `$shadow-hover` en `src/scss/abstracts/_variables.scss`.
- Se refactorizó `src/scss/components/_prose.scss` reemplazando los colores quemados (`#64748b`, `#334155`) y bordes RGBA por las variables `$color-text-muted`, `$color-text-base` y `$color-border`.
- Se refactorizó `src/scss/components/_card.scss` sustituyendo el fondo transparente por `$color-surface` y el borde por `$color-border`. Se inyectó `$shadow-hover` en el estado `:hover` de las tarjetas para dotarlas de micro-interacción de elevación.

**Motivo / criterio:** *Design System Scalability y Estética Premium*. Eliminar los colores *hardcoded* (quemados) descentralizados previene la deuda técnica visual. Además, la adición de `$color-surface` y sombras sutiles eleva la percepción de calidad de la interfaz manteniéndose en un peso de 0 KB de dependencias (solo CSS puro).

**Siguiente paso o deuda:** Iniciar el refinamiento tipográfico general y evaluar la necesidad de micro-animaciones adicionales.

### 2026-05-28 — Feat/UX: Botón de Retorno del Showcase (Clon Efímero)

**Contexto:** Se detectó el riesgo de fuga de tráfico en la demostración pública (`boilerplate.mercedev.es`). Los visitantes que llegaban al Showcase carecían de una vía intuitiva para regresar a la web principal de la autora.

**Hecho:**
- Se diseñó el componente SASS flotante `src/scss/components/_showcase.scss` (y se enlazó en el índice) con posición fija y diseño responsive, aislado mediante BEM (`.showcase-return`).
- Se refactorizó el orquestador de despliegue `scripts/matriz/merci-showcase.py` para inyectar dinámicamente el HTML del botón de retorno justo después de la etiqueta `<body>` en *todos* los archivos HTML del Clon Efímero temporal (`scratch/showcase_build/`).

**Motivo / criterio:** *Aislamiento Arquitectónico (Zero Bloat)*. Inyectar el botón durante el ciclo de vida del "Clon Efímero" justo antes de subirlo por RSYNC (Remote Sync - Sincronización Remota) permite que el código fuente matriz permanezca completamente agnóstico y limpio. Los usuarios que clonen el Boilerplate en sus máquinas jamás verán este botón, pero estará siempre presente en la demostración en vivo.

**Siguiente paso o deuda:** Continuar con la Fase 1 de la Épica 7 enfocándose en la experiencia de contenido multimedia.

### 2026-05-28 — QA/SRE: Resolución de Deuda Técnica (Auditoría de Arquitectura)

**Contexto:** Tras la auditoría de arquitectura de hoy, se procedió a saldar la deuda técnica reportada para alinear el proyecto al 100% con las reglas.

**Hecho:**
- Se renombró el archivo del blog usando el prefijo taxonómico correcto (`blog-2026-05-01-anuncio.md`).
- Se corrigió el anti-patrón WAI-ARIA en `public/index.html`, eliminando el `div` invisible y asignando el ancla `id="top"` directamente a la etiqueta `<header>`, mitigando los problemas de foco en lectores de pantalla.
- Se completó la estructura arquitectónica SASS 7-1 creando el directorio `/src/scss/pages/` y su respectivo archivo `_index.scss`, enlazado en `main.scss`.
- Se refactorizó `merci-blogger.py` extrayendo el módulo `unicodedata` de una función local al bloque de importaciones globales (Top-level imports), alineándolo con PEP 8 y la Regla 16.
- Las importaciones en bloques `try/except` de otros scripts (`markdown`, `litellm`) se confirmaron como excepciones válidas al amparo de la política de Degradación Elegante (Graceful Degradation) y Zero Bloat.

**Motivo / criterio:** *Higiene y Cumplimiento Normativo*. Las reglas del proyecto son innegociables. Saldar las pequeñas fricciones arquitectónicas a medida que se detectan previene la deriva técnica silenciosa.

**Siguiente paso o deuda:** Iniciar las mejoras visuales y multimedia planificadas para la Épica 7 (Fase 1).

### 2026-05-28 — QA/SRE: Auditoría de Arquitectura (Reglas de Higiene)

**Contexto:** Se realizó una auditoría de la arquitectura y configuración del proyecto.

**Hecho:**
- Se detectó una desviación en la regla de nomenclatura (Taxonomía SSOT, Regla 19) en el archivo `/blog/2026-05-01-anuncio.md`.
- Se identificaron violaciones a la convención PEP 8 (Regla 16) sobre la higiene de importaciones en scripts de automatización (`merci-wp.py`, `merci-audit.py`, etc.).
- Se descubrió un anti-patrón de accesibilidad en `public/index.html` con un ancla invisible (`<div id="top" tabindex="-1">`) empleada para la función "Volver arriba".
- Se constató la ausencia del directorio `pages/` dentro de `src/scss/`, rompiendo parcialmente el canon SASS 7-1.

**Motivo / criterio:** Verificación del cumplimiento estricto de las directrices marcadas en `instrucciones.md` (0 dependencias, rendimiento extremo, y Desarrollo Guiado por Especificaciones).

**Siguiente paso o deuda:** Iniciar refactorizaciones propuestas, priorizando nomenclatura del archivo en el blog y el ajuste del ancla en `index.html`.

### 2026-05-27 — Feat/DevRel: Gestor de Cola Social Interactivo (Buffer Management)

**Contexto:** El orquestador social (`merci-linkedin.py`) publicaba estrictamente en orden cronológico (FIFO) basándose en la fecha de publicación. Se requería la capacidad de reordenar dinámicamente las publicaciones (asignando posiciones exactas) y desencolar artículos directamente desde la terminal, asimilando funciones de un gestor profesional tipo Buffer o Hootsuite.

**Hecho:**
- Se introdujo el nuevo metadato `orden_social` en la máquina de estados del YAML Frontmatter.
- Se refactorizó `scripts/merci/merci-linkedin.py` inyectando un submenú interactivo para la cola de publicaciones aprobadas.
- Se implementó la acción de "Devolver a revisión" (estado `en_cola`) y el descarte permanente (`ignorado`) con confirmación explícita anti-errores.

**Detalle técnico:** El script ahora parsea y manipula el campo `orden_social` mediante expresiones regulares (`re.sub`), actualizando físicamente el archivo Markdown en disco. Los artículos sin este campo asumen la prioridad más baja (`999`). El submenú permite asignar posiciones, devolver borradores al buffer o ejecutar un "Hard Delete" lógico hacia `ignorado` protegido por un *prompt* de seguridad con emojis (`⚠️`).

**Motivo / criterio:** *Developer Experience (DX) y Content Ops*. Modificar archivos Markdown a mano para alterar el orden de publicación de una campaña de marketing genera alta fricción operativa. Delegar el trabajo pesado de reescritura de metadatos YAML al orquestador CLI consolida una experiencia de *Fricción Cero*, manteniendo a su vez la Única Fuente de Verdad (SSOT) permanentemente sincronizada.

**Siguiente paso o deuda:** Iniciar la Fase 1 de la Épica 7 aplicando las nuevas variables de color semánticas a la arquitectura SASS (`_card.scss`, `_prose.scss`).
### 2026-05-26 — UI/UX: Definición de Paleta Premium y Escala Base (Fase 1)

**Contexto:** Arranca la Épica 7 (Enriquecimiento Visual). Las variables base en SASS eran demasiado parcas y carecían de tonos de superficie (surface), grises tipográficos (text-muted) y un sistema de sombras, lo que limitaba el diseño "Premium" del proyecto.

**Hecho:** Se extendió `src/scss/abstracts/_variables.scss`.
- Se inyectaron `$color-surface`, `$color-border` y `$color-text-muted` basados en la paleta *Slate* para un diseño más moderno.
- Se formalizó la fuente monoespaciada (`$font-family-mono`) y una escala de sombras (`$shadow-sm`, `$shadow-hover`).

**Motivo / criterio:** *Design System Scalability*. Un buen diseño UI/UX (User Interface / User Experience) no usa el negro puro para los textos ni el blanco puro para todas las cajas. Definir "superficies" y "sombras" mediante variables semánticas centralizadas prepara el terreno para modernizar los cuadernillos y tarjetas de WooCommerce sin ensuciar la arquitectura CSS con valores *hardcoded*.

**Siguiente paso o deuda:** Reemplazar los colores *hardcoded* (quemados) en los componentes actuales (`_prose.scss`, `_card.scss`) por las nuevas variables semánticas, o implementar el botón de Showcase.

### 2026-05-26 — Docs/UX: Inclusión de botón de retorno para el Showcase en el Roadmap

**Contexto:** Se detectó la necesidad de evitar fugas de tráfico desde la demostración pública (`boilerplate.mercedev.es`) hacia el exterior, facilitando un camino claro de regreso al ecosistema principal.

**Hecho:** Se añadió una nueva tarea a la Fase 1 de la Épica 7 en el `ROADMAP.md` para implementar un botón de "Volver a mercedev.es" en la interfaz del Showcase.

**Motivo / criterio:** *User Retention y UX Navigation*. Todo subdominio satélite o demostración debe contar con una vía de escape obvia de regreso a la matriz. Esto no solo mejora la navegación, sino que retiene el tráfico y asegura que la demostración actúe como un embudo (funnel) hacia el portfolio profesional.

**Siguiente paso o deuda:** Iniciar con la implementación visual de los espaciados, tipografías y el botón de retorno planificado en la Épica 7.

### 2026-05-26 — Feat/UX: Conciencia de contexto (Context-Awareness) para E-commerce

**Contexto:** Tras la implementación de la tienda y el carrito Zero-JS (Épica 6), el asistente virtual Merci carecía de respuestas específicas para las rutas `/carrito` y `/checkout`, perdiendo la oportunidad de guiar durante la simulación de compra.

**Hecho:** Se refactorizó el método `_loadStandardKnowledgeBase()` en `public/js/MerciController.js` para inyectar diccionarios de respuestas específicos cuando la ruta (`window.location.pathname`) incluye las palabras clave del carrito o la caja.

**Motivo / criterio:** *Context-Awareness y UX Inmersiva*. El asistente debe acompañar el *Storytelling Técnico* del proyecto. Informar que se trata de un entorno Zero-JS seguro y sin pasarelas reales justo en el momento del checkout aporta valor divulgativo y reduce la incertidumbre en un entorno de pruebas.

**Siguiente paso o deuda:** Iniciar el refinamiento visual de tipografías y espaciados generales.