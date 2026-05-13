# Bitácora del proyecto mercedev.es — Épica 3: DevRel & Observabilidad Avanzada

## Para qué sirve este archivo

Bitácora activa a partir del cierre de la Épica 2 (Orquestación con IA, sellada el 2026-05-13).
Registra exclusivamente las decisiones, experimentos y aprendizajes de la Épica 3 (DevRel & Observabilidad Avanzada) documentada en el `ROADMAP.md` maestro.

Los historiales anteriores viven en sus respectivas bitácoras (`bitacora-mercedev-epic-01.md` y `bitacora-mercedev-epic-02.md`).

No sustituye a `instrucciones.md` (directrices y rol del asistente). Complementa el día a día con **hechos, comandos y lecciones**.

---

## Cómo mantenerlo (acuerdo simple)

1. **Añadir entradas al principio** de la sección "Registro cronológico" (orden cronológico inverso: lo más reciente arriba).
2. **Una entrada por sesión o por tema cerrado**.
3. Si algo fue un error o una vulnerabilidad evitada, usar los **tres átomos** del proyecto (Desafío → Maniobra → Aprendizaje/Deuda).
4. **Correcciones excepcionales**: editar solo el fragmento necesario; no borrar entradas sin motivo documentado.

### Plantilla para nuevas entradas

```markdown
### AAAA-MM-DD — Título corto del cambio o sesión

**Contexto:** (objetivo a lograr o problema surgido)

**Hecho:** (lista breve: archivos, fases del roadmap, PR/commit si aplica)

**Detalle técnico:** (comandos, rutas, flags; datos necesarios para el registro)

**Motivo / criterio:** (justificación de la decisión arquitectónica tomada)

**Siguiente paso o deuda:** (acciones pendientes o próximos hitos)
```

---

## Registro cronológico

### 2026-05-14 — Docs: Clarificación del SOP de Despliegue para Contenido Dinámico

**Contexto:** Tras una ejecución exitosa del pipeline local, se detectó que los nuevos artículos del blog no aparecían en el servidor de producción. Se diagnosticó una omisión en el procedimiento operativo estándar (SOP) de despliegue.

**Hecho:** Se actualizó `docs/flujo-publicacion-sop.md` para incluir el paso explícito de "conmutar entornos" en el archivo `.env` antes de ejecutar `merci wp` para el despliegue a producción.

**Detalle técnico:** El flujo ahora exige comentar las credenciales de `localhost` y activar las de producción en el `.env` antes de la sincronización Headless. Se documentó la necesidad de revertir este cambio tras el despliegue para mantener `localhost` como el entorno de trabajo por defecto.

**Motivo / criterio:** *Dev/Prod Parity y Fricción Cero*. La arquitectura de aislamiento funciona, pero el proceso manual de despliegue debe ser inequívoco. Documentar el "cambio de vías" en el SOP previene la confusión y asegura que el contenido local se propague a producción de forma controlada y deliberada.

### 2026-05-14 — Docs: Establecimiento de Anclaje Semántico para el Agente SSOT

**Contexto:** El Agente SSOT (Qwen 2.5 Coder) fallaba al marcar tareas completadas en el Roadmap si la redacción de la bitácora difería del texto original de la tarea, demostrando que opera principalmente por coincidencia de cadenas (*String Matching*) y no por inferencia semántica abstracta.

**Hecho:** Se establece la norma metodológica de "Anclaje Semántico": al documentar el cierre de un hito en la bitácora, el bloque "Hecho" debe incluir textualmente las palabras clave o la frase exacta de la tarea listada en el Roadmap.

**Detalle técnico:** Los SLMs locales carecen de la capacidad de deducción profunda de los modelos de frontera en la nube. Para evitar reescribir el historial o alterar el prompt masivamente, la autora adaptará la descripción del logro para que sirva de baliza (ancla) directamente reconocible por la IA.

**Motivo / criterio:** *AI Governance y SLM Psychology*. Aceptar las limitaciones cognitivas de la IA local y compensarlas con disciplina humana (redactando de forma predecible) es un patrón DevSecOps maduro que garantiza la sincronización documental (SSOT) sin sobreingeniería.

### 2026-05-14 — Docs: Expansión del Roadmap (Épica 5 - Showcase del Boilerplate)

**Contexto:** Surgió la necesidad de proveer a los futuros usuarios del `merci-boilerplate` una demostración en vivo (Live Demo) para que puedan visualizar el estado inmaculado y purista de la plantilla base antes de clonarla.

**Hecho:** Se inyectó la "Épica 5: Showcase y Distribución del Boilerplate" en el archivo `ROADMAP.md`.

**Detalle técnico:** Se planificó la evaluación de entornos de despliegue estático gratuitos (como GitHub Pages o un subdominio) para alojar la demostración, delegándolo a una fase futura para no saturar el trabajo actual.

**Motivo / criterio:** *Product Marketing y Prevención de Olvidos*. Un repositorio open-source adquiere mucho más valor si posee una representación visual activa. Registrar esta idea formalmente como una nueva Épica evita el "Scope Creep" (añadir tareas no planificadas al sprint actual) y asegura que no se pierda en el olvido.

### 2026-05-14 — Feat: Buffer de Publicación y Aprobación Asíncrona (LinkedIn)

**Contexto:** Publicar inmediatamente desde la terminal rompía la filosofía del "Buffer Social" programado. Se requería una cola asíncrona donde la autora revisa y aprueba los borradores, y un robot independiente los publica poco a poco sin intervención humana.

**Hecho:** Se refactorizó `scripts/merci/merci-linkedin.py` implementando dos modos de ejecución e inyectando un nuevo estado intermedio `estado_social: "aprobado"`.

**Detalle técnico:** Ejecutar `merci linkedin` (Modo Interactivo) ahora itera sobre los posts `en_cola`, los muestra por pantalla y pregunta si se aprueban, cambiando su estado a `aprobado`. Ejecutar `merci linkedin --auto` (Modo Cron) busca el post `aprobado` más antiguo, lo publica silenciosamente en LinkedIn y lo sella como `publicado_linkedin`. Se actualizó la métrica en `merci-sre.py` para sumar tanto lo pendiente de revisión como lo aprobado.

**Motivo / criterio:** *Asynchronous Operations y Fricción Cero*. Separar el momento de la "Curación" del momento de la "Emisión" es la piedra angular del marketing de contenidos. La autora aprueba un lote de artículos rápidamente, y una tarea en segundo plano puede encargarse de disparar el modo `--auto` periódicamente garantizando presencia continua en redes sociales sin carga cognitiva.

### 2026-05-14 — Docs: Actualización de SOP y Arquitectura de Agentes en manuales

**Contexto:** Tras la profunda reestructuración del flujo de trabajo (introducción de la bandeja unificada `incubacion/`, el enrutamiento inteligente por tema en `merci-promote` y el *Agent Chaining* con `merci-blogger.py`), los documentos fundacionales (`README.md`, `instrucciones.md` y `flujo-publicacion-sop.md`) habían quedado obsoletos (Document Drift).

**Hecho:** Se actualizaron los tres documentos maestros añadiendo a `merci-blogger.py` al inventario del ecosistema y reescribiendo el SOP para reflejar las nuevas mecánicas de incubación unificada, validación cruzada y Buffer Social de LinkedIn.

**Motivo / criterio:** *Single Source of Truth (SSOT)*. Una arquitectura brillante no sirve de nada si el manual de operaciones describe un sistema obsoleto. Reflejar el encadenamiento de agentes y las nuevas mecánicas de promoción en el "Runbook" oficial consolida la madurez de la Épica 3 y prepara el terreno para automatizaciones futuras.

### 2026-05-14 — Fix: Contextualización de prompts en orquestador de promoción

**Contexto:** Al promover artículos del Blog, el asistente interactivo (`merci-promote.py`) solicitaba metadatos innecesarios para un flujo cronológico (como "Tema/Estantería", "Alt de la portada" y "Fase del Roadmap"), generando fricción operativa y bloqueos (por la regla estricta de `alt_portada`).

**Hecho:** Se refactorizó la lógica interactiva en `scripts/merci/merci-promote.py` para adaptar los campos solicitados basándose en el metadato `tema`.

**Detalle técnico:** Se implementó el booleano `es_blog` evaluando si `"blog" in tema_actual.lower()`. Si es verdadero, el script oculta las preguntas estructurales de la biblioteca y puentea el bloqueo innegociable de WAI-ARIA para las portadas, solicitando exclusivamente la descripción y la fecha de publicación.

**Motivo / criterio:** *Fricción Cero y Arquitectura de la Información*. Un blog es un flujo cronológico, no estructural. Exigir estanterías o imágenes obligatorias a un contenido que por naturaleza suele ser de texto rápido añade burocracia innecesaria. Adaptar el orquestador al contexto del documento purifica la Experiencia del Desarrollador (DX).

### 2026-05-14 — Feat: Escudo de Referencias Cruzadas en Promoción (Shift-Left DAST)

**Contexto:** Al encadenar agentes, el Blogger genera posts de marketing que enlazan a cuadernillos técnicos. Si la autora promovía el post del blog antes que el cuadernillo original, el publicador Headless subiría un artículo a WordPress con un enlace roto (404), rompiendo la experiencia de usuario.

**Hecho:** Se inyectó un validador de referencias cruzadas en `scripts/merci/merci-promote.py`.

**Detalle técnico:** El script escanea el cuerpo del documento en busca de URLs internas (`https://mercedev.es/biblioteca/...`). Si encuentra alguna, calcula dinámicamente todos los slugs (`slugify`) de los documentos actualmente en producción (`biblioteca/` y `art-de-cote/`). Si el enlace destino no existe en producción, aborta la promoción con un mensaje de bloqueo didáctico.

**Motivo / criterio:** *Shift-Left Quality y Dependency Enforcing*. Prevenir un error antes de que se compile es mejor que detectarlo después. Forzar el orden cronológico de promoción (primero el documento base, luego el marketing) garantiza que WordPress nunca reciba un enlace hacia un recurso estático inexistente.

### 2026-05-14 — Test: Validación End-to-End de Máquina de Estados y Agent Chaining

**Contexto:** Tras implementar el encadenamiento de agentes (Bibliotecario -> Blogger) y la métrica de SRE, era vital confirmar que la cadena completa funcionaba sin fricciones y respetando la máquina de estados documental.

**Hecho:** Se ejecutó una prueba limpia partiendo de una nota cruda. El Bibliotecario generó el cuadernillo, el Blogger generó el post de marketing, y se validó que los documentos nacen en `incubacion`.

**Motivo / criterio:** *State Machine Integrity*. Confirmar empíricamente que los documentos en incubación son invisibles para la telemetría de Grafana y la cola de LinkedIn demuestra que la arquitectura es sólida. Un documento solo entra en la cola social cuando la autora lo promueve explícitamente a `publicado`, previniendo la publicación de enlaces rotos (404) hacia la web matriz.

### 2026-05-14 — Fix: Resolucion de fallos End-to-End en encadenamiento (Blogger)

**Contexto:** Al validar el "Agent Chaining" entre el Bibliotecario y el Blogger, el pipeline colapsó con `UnboundLocalError`. Además, la reescritura de los metadatos YAML inyectaba comillas residuales corrompiendo el parser.

**Hecho:** Se refactorizaron las expresiones regulares (`.*?` cambiado por `[^"'\n]*`) en `scripts/merci/merci-blogger.py` y se corrigió el alcance del mensaje de consola para archivar notas.

**Detalle técnico:** La expresión regular *non-greedy* con captura opcional en los extremos provocaba que el reemplazo no consumiera la última comilla escrita por Ollama, concatenando el estado forzado (`"incubacion"incubacion"`). Colocar el mensaje de éxito fuera del ámbito exclusivo de las notas crudas provocaba la llamada a una variable inexistente.

**Motivo / criterio:** *End-to-End QA*. Testear flujos aislados es engañoso. La orquestación revela los límites del código de integración. Estos parches garantizan que la cadena de montaje asuma documentos generados dinámicamente sin bloqueos.

### 2026-05-14 — Refactor: Estandarización de nomenclatura para artículos del Blog

**Contexto:** Los artículos generados por el Agente Blogger (`merci-blogger.py`) se guardaban en la incubadora únicamente con el título slugificado, rompiendo la consistencia visual y de nomenclatura establecida por el Agente Bibliotecario (que usa prefijos como `cuadernillo-`, `compendio-`, `art-de-cote-`).

**Hecho:** Se parcheó `scripts/merci/merci-blogger.py` para inyectar automáticamente el prefijo `blog-` al generar el nombre del archivo físico (`filename = "blog-" + slugify(titulo) + ".md"`).

**Motivo / criterio:** *Consistency y Fricción Cero*. Mantener un estándar de nomenclatura estricto en la bandeja de entrada unificada (`incubacion/`) permite a la autora identificar instantáneamente la tipología y el destino de un documento con solo mirar su nombre de archivo en el IDE.

### 2026-05-14 — Fix: Enlaces relativos a la raíz en Agent Chaining (Dev/Prod Parity)

**Contexto:** Los artículos promocionales generados por el Blogger incluían una URL absoluta (`https://mercedev.es/...`) hacia el documento técnico original. Esto rompía la experiencia de desarrollo local, ya que al hacer clic en el entorno de pruebas, el usuario era redirigido al servidor de producción donde el documento aún no existía (Error 404).

**Hecho:** Se refactorizó la generación de la variable `url_promocion` en `scripts/merci/merci-blogger.py` para utilizar rutas relativas a la raíz (ej. `/biblioteca/slug.html`).

**Motivo / criterio:** *Agnosticismo de Entorno y Dev/Prod Parity*. El contenido en formato Markdown debe ser independiente del dominio donde se aloje. Utilizar rutas relativas a la raíz garantiza que el enlace resuelva perfectamente a `localhost:8000` durante el desarrollo y a `mercedev.es` en producción, sin necesidad de modificar el código fuente.

### 2026-05-14 — UX/UI: Rediseño del Blog a formato cronológico puro (Limpieza de index.php)

**Contexto:** La plantilla de WordPress (`index.php`) agrupaba visualmente los posts por categorías, emulando las estanterías de la Biblioteca. Esto rompía el paradigma de un blog tradicional, que debe mostrar un flujo de lectura vertical y cronológico, añadiendo ruido visual a las publicaciones de marketing.

**Hecho:** Se refactorizó drásticamente el archivo `src/wp-theme/merci-theme/index.php`.

**Detalle técnico:** Se extirpó el bucle de agrupación por `$tema`, la generación del menú interno (`library-nav`) y la envoltura en cuadrícula (`home-grid`). En su lugar, se implementó un bucle estándar `while (have_posts())` que renderiza las tarjetas apiladas verticalmente en una sola columna con `max-width: 800px` para una legibilidad óptima. También se eliminó el condicional huérfano de `Art de Coté`, puesto que dicha sección ahora es servida al 100% por el motor SSG.

**Motivo / criterio:** *Separation of Concerns* (Separación de responsabilidades). La Biblioteca ordena el conocimiento; el Blog emite novedades. Diferenciar la UI de ambos espacios clarifica la intención de la lectura. Reducir la lógica PHP en el tema acelera el TTFB y simplifica el mantenimiento.

### 2026-05-14 — Feat: Métrica SRE para Buffer de LinkedIn en Grafana

**Contexto:** Era necesario vigilar la cantidad de posts disponibles ("munición") en la cola de LinkedIn para configurar futuras alertas SRE cuando el buffer se estuviera agotando.

**Hecho:** Se instrumentó `scripts/merci/merci-sre.py` inyectando la métrica `merci_linkedin_queue_total`.

**Detalle técnico:** El agente escanea los directorios de producción (`blog`, `biblioteca`, `art-de-cote`) y cuenta cuántos archivos poseen simultáneamente `estado: "publicado"` y `estado_social: "en_cola"`, exponiendo el valor como un *Gauge* a Prometheus.

**Motivo / criterio:** *Observabilidad y DevRel*. Mantener una métrica en tiempo real permite delegar la preocupación de publicar a los sistemas de alerta (Grafana Alerting). Esto concluye formalmente la infraestructura de la Fase 2 (Observabilidad y Alertas SRE).

### 2026-05-14 — Fix: Enrutamiento Dinámico por Tema (SSOT) en Promote

**Contexto:** Los artículos generados por la IA o creados en la nueva bandeja unificada (`laboratorio/incubacion/`) perdieron la capacidad de enrutarse correctamente al ser promovidos. El orquestador `merci-promote.py` decidía el destino basándose en la carpeta de origen, lo que provocaba que todo acabara en la `biblioteca/`.

**Hecho:** Se refactorizó la lógica de enrutamiento en `scripts/merci/merci-promote.py`.

**Detalle técnico:** El destino (`blog/`, `art-de-cote/` o `biblioteca/`) se deduce ahora leyendo el campo `tema:` extraído dinámicamente del YAML Frontmatter.

**Motivo / criterio:** *SSOT (Single Source of Truth)*. La estructura de carpetas local es efímera, pero el metadato es inmutable. Confiar el destino de producción a lo que dicte el YAML Frontmatter permite unificar toda la redacción en una única bandeja de entrada (`incubacion/`) sin fricción operativa.

### 2026-05-14 — Feat: Ruta directa de Marketing en Agente Bibliotecario (Fast Track)

**Contexto:** Se requería una opción para publicar notas rápidas directamente en el Blog y en LinkedIn sin la obligación de generar un documento técnico denso en la Biblioteca (Cuadernillo o Compendio).

**Hecho:** Se implementó una cuarta opción en el menú interactivo de `scripts/merci/merci-librarian.py` para invocar a `merci-blogger.py` de forma directa con la nota cruda. Se modificó el prompt y la lógica del Blogger para que adapte dinámicamente su texto de cierre.

**Detalle técnico:** Si el Blogger recibe un archivo procesado (`.md` fuera de `notas_rapidas`), inyecta la URL canónica y anima a leer la Biblioteca. Si recibe una nota cruda (`.txt` o `.md` desde `notas_rapidas`), omite la URL, no genera errores por falta de metadatos y redacta una conclusión directa. El prompt maestro fue flexibilizado para soportar ambas vías sin alucinaciones.

**Motivo / criterio:** *Fricción Cero y Content Ops*. No toda la actividad de la autora resulta en un manual técnico. Algunas ideas son reflexiones sueltas que merecen un altavoz social. Ofrecer un carril rápido (*Fast Track*) para la generación de marketing puro consolida a los agentes como un equipo de DevRel ágil y desacoplado.

### 2026-05-14 — Feat: Agent Chaining y cálculo dinámico de URLs (Bibliotecario → Blogger)

**Contexto:** Se requería crear una verdadera "Cadena de Montaje" de contenidos. El Bibliotecario redactaba el documento técnico, pero la difusión requería intervención manual para llamar al Blogger y carecía de enlaces automáticos a la obra original.

**Hecho:** Se implementó el encadenamiento de agentes (Agent Chaining) entre `merci-librarian.py` y `merci-blogger.py`. El Blogger ahora calcula la URL canónica de destino y obliga a la IA a incluirla.

**Detalle técnico:** Al finalizar la creación de un documento en la incubadora, el Bibliotecario pregunta si se desea promocionar. Si la respuesta es afirmativa, invoca a `merci-blogger.py` pasándole el archivo generado. El Blogger lee el YAML Frontmatter, calcula la URL final (`/biblioteca/...` o `/art-de-cote/...`), inyecta el enlace en el prompt para la IA y finalmente encola el post para LinkedIn.

**Motivo / criterio:** *Agentic Workflows y Fricción Cero*. Separar roles (Ingeniero vs DevRel) evita alucinaciones en modelos locales. Encadenar su ejecución automatiza todo el proceso (redacción técnica -> redacción marketing -> encolado social) con una sola interacción inicial de la autora y garantiza que los enlaces cruzados sean matemáticamente exactos.

### 2026-05-14 — Feat: Agente Redactor DevRel (merci-blogger.py)

**Contexto:** Se necesitaba automatizar la creación de artículos y anuncios para LinkedIn a partir de notas crudas, manteniendo la separación de roles (Technical Writer vs Copywriter/DevRel) para evitar alucinaciones en modelos locales.

**Hecho:** Se desarrolló `scripts/merci/merci-blogger.py` y su cerebro rector `laboratorio/prompts/prompt-blogger.md`. Se extirpó la dependencia de APIs externas para obligarlo a usar exclusivamente Ollama (`qwen2.5-coder`).

**Detalle técnico:** El script lee una nota cruda, utiliza a Ollama para redactar un post entretenido con un bloque HTML de LinkedIn inyectado y el estado `estado_social: "en_cola"`. Luego guarda el resultado en `incubacion/` y mueve la nota original a `_procesadas/`.

**Motivo / criterio:** *Local AI Content Ops*. Dividir la responsabilidad entre el Bibliotecario (técnico) y el Blogger (marketing) especializa el contexto del SLM. Forzar el uso local (Ollama) garantiza la privacidad total del borrador y coste cero de generación.

### 2026-05-14 — Perf: Minimalismo y patrón "Silence is Golden" en orquestadores

**Contexto:** La ejecución del orquestador maestro (`merci total`) saturaba la consola imprimiendo un mensaje de éxito por cada archivo procesado en SSG (`merci-publish.py`) y WordPress (`merci-wp.py`), generando ruido visual excesivo (45+ líneas).

**Hecho:** Se refactorizaron `scripts/merci/merci-publish.py` y `scripts/merci/merci-wp.py` para suprimir los mensajes individuales de éxito si el proceso transcurre con normalidad.

**Detalle técnico:** Se reemplazó el `print` iterativo por un contador de éxito que emite un único mensaje resumen al finalizar el proceso (ej. `✅ 45 artículos sincronizados masivamente`).

**Motivo / criterio:** *Silence is Golden y Clean DX*. Las herramientas de terminal deben ser silenciosas cuando triunfan y ruidosas solo cuando fallan. Reducir el ruido consolida la visualización de métricas críticas en herramientas de observabilidad como Grafana.

### 2026-05-14 — Fix: API Drift de Gemini y Validación de Fallback Local en SSOT

**Contexto:** Google modificó la nomenclatura de sus modelos en la API v1beta (forzando sufijos `-latest`), lo que provocó errores HTTP 404 en el Agente SSOT al intentar conectarse a la nube.

**Hecho:** Se extirpó la función `auto_descubrir_modelo` de `scripts/merci/merci-ssot.py` anclando el script explícitamente a `gemini-1.5-flash-latest`.

**Detalle técnico:** El incidente validó empíricamente el patrón de Degradación Elegante (Fail Gracefully). Al devolver la API de Google un error 404, el orquestador atrapó la excepción, delegó la tarea a Ollama local (`qwen2.5-coder`) y salvó la compilación del pipeline sin detenerse.

**Motivo / criterio:** *SaaS Volatility y Local Resilience*. Las APIs de IA cambian sus endpoints sin previo aviso. Mantener la resiliencia mediante fallbacks locales asegura que los caprichos de terceros no paralicen el ecosistema de integración continua (CI/CD).

### 2026-05-14 — Fix: Patrón Fail-Fast y Autodescubrimiento en Agente SSOT

**Contexto:** Tras la reestructuración de las bitácoras, el Agente SSOT quedó ciego, pero el orquestador maestro (`merci total`) reportaba "Pipeline completado con éxito". El script estaba tragándose los errores silenciosamente.

**Hecho:** Se refactorizó `scripts/merci/merci-ssot.py` inyectando el autodescubrimiento de bitácoras mediante `glob` y sustituyendo los retornos funcionales (`return`) por salidas fatales (`sys.exit(1)`).

**Detalle técnico:** En Python, usar `return` en el bloque principal devuelve código de salida `0` (éxito). Al mutarlos a `sys.exit(1)`, el orquestador (que usa `subprocess.run(check=True)`) ahora sí atrapa el fallo, colapsa el pipeline inmediatamente y muestra el mensaje rojo de alerta.

**Motivo / criterio:** *Pipeline Integrity*. Un pipeline de integración no puede tolerar fallos silenciosos. Aplicar el patrón Fail-Fast (Fallar rápido) obliga a reparar las deudas técnicas en el momento en que se originan, impidiendo despliegues parciales o rotos.

### 2026-05-14 — Feat: Máquina de Estados para Buffer Social (LinkedIn)

**Contexto:** Se necesitaba desacoplar la generación de artículos de su difusión social para evitar inundar de Spam la red profesional, creando un sistema que dosifique los contenidos asíncronamente (Buffer).

**Hecho:** 
- Se refactorizó `scripts/merci/merci-linkedin.py` como un "Gatekeeper".
- Tarea completada: Añadir el campo `estado_social: "en_cola"` al YAML Frontmatter en las plantillas Markdown base (`plantilla-blog.md`, `plantilla-art-de-cote.md`).

**Detalle técnico:** El orquestador social escanea ahora la máquina de estados YAML de todos los documentos, filtra solo los que están `en_cola`, los ordena por antigüedad y extrae únicamente el más antiguo. Tras mostrar una previsualización, exige confirmación humana (`s/N`). Si se publica, sella el YAML actualizándolo a `publicado_linkedin`.

**Motivo / criterio:** *Content Ops y Fricción Cero*. Programar un "Hootsuite" en Python puro dentro del propio código fuente elimina herramientas externas, mantiene control absoluto sobre la cadencia y protege el feed de LinkedIn mediante barreras de confirmación humana.

**Siguiente paso o deuda:** Desarrollar el Agente de Relaciones Públicas (`merci-blogger.py`) para generar los posts de la cola a partir de notas crudas, y configurar la telemetría SRE en Grafana para vigilar la cantidad de munición disponible.

### 2026-05-14 — Refactor: Reestructuración de bitácoras por Épicas

**Contexto:** Validar el autodescubrimiento del nuevo orquestador de commits tras dividir el historial en múltiples archivos de Épica y organizar la documentación de I+D.

**Hecho:** Se renombraron las bitácoras antiguas (`epic-01` y `epic-02`) y se creó esta nueva bitácora estructurada para la Épica 3. Se refactorizó `merci-commit.py` para usar `glob` en el autodescubrimiento.

**Motivo / criterio:** *Zero Maintenance y Clean DX*. Separar los logs por Épica evita archivos infinitos y saturación visual. Refactorizar el orquestador maestro para que detecte las bitácoras automáticamente previene la rotura de la automatización CI/CD local en el futuro.

### 2026-05-14 — Docs: Creación de la estantería SOS Terminal (Píldoras de Conocimiento)

**Contexto:** Registrar micro-lecciones y comandos de terminal críticos que no requieren el formato extenso de un cuadernillo, pero que son vitales para la resolución rápida de incidentes operativos.

**Hecho:** Se definió la nueva taxonomía `tema: "SOS Terminal"` en el Frontmatter de los artículos y se publicó el primer documento resolviendo la deriva del archivo `requirements.txt` en el repositorio público.

**Motivo / criterio:** *Knowledge Harvesting y Fricción Cero*. No toda la documentación debe ser un manual exhaustivo. Aislar los "comandos salvavidas" en su propia estantería dentro de *Art de Coté* acelera la respuesta ante crisis y mantiene la biblioteca libre de "ruido" táctico.
