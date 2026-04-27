# Bitácora del proyecto mercedev.es

## Para qué sirve este archivo

- **Yo futuro:** recuperar en minutos qué se decidió, por qué, y cómo se ejecutó algo técnico sin rebuscar en el chat o en commits sueltos.
- **Biblioteca (al cerrar el proyecto):** aquí vive el borrador narrativo y técnico; luego se depura y se traslada a `biblioteca/` como piezas definitivas (por estantería o tema), siguiendo la idea de “activo de conocimiento” del proyecto.

No sustituye a `instrucciones.md` (directrices y rol del asistente). Complementa el día a día con **hechos, comandos y lecciones**.

---

## Cómo mantenerlo (acuerdo simple)

1. **Añadir entradas al principio** de la sección “Registro cronológico”, con la plantilla de abajo. El registro es **acumulativo**: lo ya escrito forma parte del historial y **no se reemplaza** por nuevas sesiones (así no se pierde contexto ni fechas).
2. **Una entrada por sesión o por tema cerrado** (lo que resulte más claro al escribir).
3. Si algo fue un error o una vulnerabilidad evitada, opcionalmente usar los **tres átomos** del proyecto (Desafío → Maniobra → Aprendizaje/Deuda) en el cuerpo de la entrada.
4. **Correcciones excepcionales** (typo, dato incorrecto, redacción de un solo párrafo, retirada de información sensible): editar solo el fragmento necesario o añadir una línea aclaratoria bajo la entrada; evitar reescribir todo el archivo o borrar entradas enteras sin motivo documentado.

### Plantilla para nuevas entradas

Copia el bloque y rellénalo.

```markdown
### AAAA-MM-DD — Título corto del cambio o sesión

**Contexto:** (qué querías lograr o qué problema apareció)

**Hecho:** (lista breve: archivos, fases del roadmap, PR/commit si aplica)

**Detalle técnico:** (comandos, rutas, flags; solo lo que necesites recordar)

**Motivo / criterio:** (por qué esta opción y no otra)

**Siguiente paso o deuda:** (qué queda pendiente)
```

---
## Registro cronológico

### 2026-04-27 — Fix: Expansión de acrónimos en Shadow Docs (Boilerplate)

**Contexto:** Al ejecutar la auditoría (`merci total`) en el repositorio clonado del Boilerplate, el linter de accesibilidad cognitiva emitió advertencias (WARN) por acrónimos no expandidos (como BEM). Esto ocurrió porque al purgar la biblioteca y el laboratorio, el recuento global de dichos términos cayó por debajo del umbral de consolidación (>3).

**Hecho:** Se expandió explícitamente el acrónimo BEM (Block, Element, Modifier - Modificador de Elemento de Bloque) en `README-merci.md`, `instrucciones-merci.md` e `instrucciones.md`.

**Detalle técnico:** Se aplicó la convención de expansión `ACRÓNIMO (Inglés - Español)` directamente en las documentaciones "en la sombra", garantizando que el texto base del Boilerplate cumpla con el análisis estático de `merci-audit.py` por sí mismo.

**Motivo / criterio:** *Standalone Compliance*. Una plantilla agnóstica debe ser 100% autosuficiente y superar su propia auditoría con 0 advertencias desde el commit inicial, sin depender de la densidad documental del proyecto matriz del que fue extraída.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-27 — Fix: Expansión de acrónimo SEO en plantilla de proyecto

**Contexto:** Tras el simulacro de instanciación del Boilerplate, el auditor `merci-audit.py` levantó una advertencia por el acrónimo "SEO" no expandido. El diagnóstico reveló que el término residía en los comentarios del YAML Frontmatter del archivo `docs/plantilla-proyecto.md`.

**Hecho:** Se expandió el acrónimo SEO (Search Engine Optimization - Optimización para Motores de Búsqueda) directamente en la plantilla base del repositorio.

**Motivo / criterio:** *Standalone Compliance*. Al igual que ocurrió con los Shadow Docs, las plantillas fundacionales que sobreviven al script de inicialización (`merci-init.py`) deben ser semánticamente autosuficientes para no heredar advertencias de linter al nuevo usuario.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-27 — Feat: Automatización de la fecha de última revisión en bitácora

**Contexto:** La línea final del archivo de bitácora (`*Última revisión de la bitácora: 2026-04-27.*`) contenía una fecha obsoleta (2026-04-14) porque dependía de la actualización manual por parte de la autora en cada sesión.

**Hecho:** Se implementó una rutina de actualización automática en `scripts/merci/merci-commit.py` mediante expresiones regulares.

**Detalle técnico:** Justo antes de ejecutar el `git add .`, el script lee el contenido completo de la bitácora, localiza la cadena de texto de la última revisión y sustituye la fecha por el día actual (`datetime.now()`), sobrescribiendo el archivo para que se empaquete con el dato exacto.

**Motivo / criterio:** *Fricción Cero*. Eliminar tareas repetitivas y propensas al error humano. Si el orquestador de commits ya lee la bitácora para extraer el mensaje, es el lugar arquitectónicamente perfecto para actualizar sus metadatos internos de forma transparente.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-27 — Docs: Versionado Semántico en Shadow Docs (v1.0.0)

**Contexto:** El documento en la sombra `README-merci.md` (que asciende a README oficial tras la instanciación) carecía de la declaración explícita de la versión del motor, dificultando la trazabilidad para los usuarios del Boilerplate.

**Hecho:** Se inyectó la etiqueta de versión `v1.0.0` en el encabezado principal de `README-merci.md`.

**Motivo / criterio:** *Semantic Versioning* (Versionado Semántico). El archivo maestro de un proyecto agnóstico debe indicar claramente en qué punto de madurez se encuentra. Al estar integrado en el Release Pipeline Agile (Regla 14), este número se incrementará manualmente en el proyecto matriz justo antes de empaquetar futuras *releases* (ej. `v1.1.0`).

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-27 — Perf: Optimización de peso en copias de seguridad (Backup Local)

**Contexto:** El script de copias de seguridad locales (`merci-backup.py`) estaba generando archivos ZIP de casi 47 MB, un peso desproporcionado para un repositorio de código y texto. El diagnóstico reveló que estaba comprimiendo los binarios de la carpeta `evidencias/` y los PDFs generados en `descargas/`.

**Hecho:** Se añadieron los directorios `evidencias` y `descargas` al conjunto (set) de exclusión `EXCLUDE_DIRS` en el script de backup.

**Detalle técnico:** Al ignorar estas carpetas en el recorrido `os.walk()`, se evita procesar y comprimir archivos multimedia pesados o artefactos dinámicos que pueden ser regenerados a voluntad mediante el orquestador SSG.

**Motivo / criterio:** *Performance y Eficiencia*. Una herramienta de *Disaster Recovery* local debe ser ultrarrápida y generar instantáneas ligeras. Excluir binarios que no forman parte del código fuente matriz garantiza que el backup se ejecute en milisegundos y consuma un espacio residual en el disco.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-27 — Feat: Bloqueo activo de evidencias y assets pesados (Shift-Left)

**Contexto:** Para asegurar que el historial de Git no se vuelva a contaminar con archivos binarios (vídeos, capturas) tras los incidentes con la carpeta `evidencias/`, el uso de `.gitignore` resultó ser insuficiente por su naturaleza pasiva frente a archivos previamente rastreados.

**Hecho:** Se implementó la regla `BANNED_TRACKED_FILE` en `scripts/merci/merci-audit.py` (auditor maestro).

**Detalle técnico:** Se creó la función `audit_banned_tracked_files` que consulta directamente a Git (`git ls-files` o `git diff --cached`). Si detecta que cualquier archivo (excepto `.gitkeep`) bajo `laboratorio/evidencias/` o `.assets-raw/` está a punto de ser comiteado o ya está siendo rastreado, inyecta un `ERROR` bloqueante en el estado de la auditoría.

**Motivo / criterio:** *Shift-Left Security*. Delegar la higiene del repositorio a la memoria humana o a un `.gitignore` pasivo genera fugas de datos. Un escudo activo (Linter) que bloquea el commit atómico previene físicamente la subida de archivos pesados al servidor remoto.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-27 — Fix: Erradicación de evidencias rastreadas heredadas

**Contexto:** Tras resolver un conflicto de fusión masivo, la carpeta `laboratorio/evidencias/` volvió a subirse al repositorio remoto a pesar de estar incluida en el `.gitignore`.

**Hecho:** Se ejecutó `git rm -r --cached laboratorio/evidencias/` para forzar a Git a "olvidar" los archivos sin borrarlos del disco duro local, y se generó un nuevo commit para purgar el servidor.

**Detalle técnico:** El archivo `.gitignore` previene que archivos *nuevos* sean añadidos al índice (`staged`), pero **no tiene efecto** sobre archivos que ya estaban siendo rastreados (tracked) en el historial previo. Al fusionar la rama remota, Git recuperó la memoria de esos archivos. Para aplicar un gitignore retroactivamente, es obligatorio eliminar los archivos de la caché de Git explícitamente.

**Motivo / criterio:** Higiene del repositorio. Comprender la diferencia entre archivos *tracked* y *untracked* es vital. La eliminación de la caché es la única maniobra válida para forzar a Git a soltar archivos que ya había asimilado en el pasado.

**Siguiente paso o deuda:** Inyectar una regla de validación en `merci-audit.py` para bloquear atómicamente cualquier commit que contenga archivos en esta carpeta.

### 2026-04-27 — Fix: Restauración de clase estructural para menú móvil

**Contexto:** En el entorno de producción, el menú hamburguesa no se desplegaba en las páginas de la Biblioteca ni en las vistas dinámicas de WordPress, aislando al usuario en móvil.

**Hecho:** Se inyectó la clase `.page` en las etiquetas `<body>` del orquestador `merci-publish.py` y del archivo `index.php` del Child Theme. También se corrigió la inyección del ancla invisible `#top` en el índice de la biblioteca.

**Detalle técnico:** El análisis del código Vanilla JS (`main.js`) reveló que estaba perfectamente estructurado con Cláusulas de Guarda (Guard Clauses), por lo que no había colapsos por `TypeError`. El fallo era exclusivamente CSS: las reglas de visualización del menú dependían del contexto `.page` en el `body`, el cual fue omitido durante la generación dinámica del HTML.

**Motivo / criterio:** Paridad de Entornos (Dev/Prod Parity). El núcleo estático base (`public/index.html`) poseía el atributo `class="page"` que habilitaba ciertas reglas SASS en cascada. Todo motor de renderizado (SSG o PHP) que reutilice el mismo CSS debe emitir exactamente la misma estructura de contenedores padre para evitar roturas visuales.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-27 — Fix: Resolución de conflicto de sobreescritura en `git pull`

**Contexto:** Al ejecutar `git pull` tras configurar la estrategia de fusión, Git abortó la operación con el error: "Los cambios locales de los siguientes archivos serán sobrescritos al fusionar". Esto ocurrió porque existían modificaciones locales en `laboratorio/bitacora-mercedev.md` que aún no habían sido empaquetadas en un commit.

**Hecho:** Se empaquetaron los cambios locales pendientes mediante `merci-commit.py` antes de volver a intentar la sincronización.

**Detalle técnico:** Git se niega a ejecutar un `pull` si este va a sobrescribir trabajo local no guardado (uncommitted). El flujo de trabajo correcto es siempre: 1) Guardar el trabajo local (`git add .` y `git commit`) y 2) Sincronizar con el servidor (`git pull`).

**Motivo / criterio:** *Integridad de datos*. Es un mecanismo de seguridad fundamental de Git para prevenir la pérdida de trabajo. Nunca se debe forzar una sincronización sobre cambios locales no guardados. La solución es siempre confirmar el estado local antes de integrar el estado remoto.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).


### 2026-04-27 — Fix: Configuración de reconciliación para ramas divergentes (Git)

**Contexto:** Al ejecutar `git pull` para resolver un error de `non-fast-forward`, Git bloqueó la operación indicando que las ramas habían divergido (existían commits distintos tanto en local como en remoto) y requería especificar una estrategia de reconciliación explícita.

**Hecho:** Se configuró la estrategia de fusión por defecto (`git config pull.rebase false`) y se completó la sincronización (`git pull` seguido de `git push`).

**Detalle técnico:** Las ramas divergen cuando el historial local y el remoto se bifurcan (por ejemplo, al crear commits locales tras haber modificado el repositorio en la nube). Configurar `pull.rebase false` instruye a Git para que resuelva estas colisiones creando un "commit de fusión" (Merge Commit) estándar, preservando la cronología exacta de ambas líneas temporales sin reescribir el historial.

**Motivo / criterio:** Gobernanza del repositorio. Definir explícitamente la estrategia de fusión es una buena práctica de ingeniería que previene comportamientos erráticos o destructivos al sincronizar código en entornos de desarrollo distribuidos.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-27 — Fix: Restauración del scroll en el ancla "Volver arriba"

**Contexto:** El enlace "Volver arriba" (`#top`) en el footer dejó de realizar el desplazamiento (scroll) físico esperado. El script `merci-linkcheck.py` no auditó este error porque, por estándar técnico, los rastreadores ignoran los fragmentos de ancla (`#`).

**Hecho:** Se separó el identificador de ancla del contenedor visual `<header>`.

**Detalle técnico:** Se eliminó el `id="top"` y `tabindex="-1"` del `<header>` en `public/index.html` (y derivados) y se inyectó un `<div>` vacío (`position: absolute; top: 0; left: 0;`) con el `id="top"` justo después de abrir la etiqueta `<body>`. Se replicó la inyección en las plantillas f-string de `scripts/merci/merci-publish.py`.

**Motivo / criterio:** *Separation of Concerns* (Separación de responsabilidades). Al trasladar el `id="top"` al `<header>` (que es fijo o se encuentra siempre visible arriba) en la Fase 2, el navegador asumía que ya estaba en el *viewport* y omitía el scroll. Crear un ancla independiente restaura el scroll a la coordenada absoluta `0,0` manteniendo la puntuación WAI-ARIA 100/100.

**Siguiente paso o deuda:** Aplicar el mismo parche en la plantilla de WordPress (`src/wp-theme/merci-theme/index.php`) para mantener la paridad entre entornos.

### 2026-04-27 — Fix: Resolución de error `non-fast-forward` en `git push`

**Contexto:** Al intentar subir cambios al repositorio remoto (`git push`), la operación fue rechazada con el error `non-fast-forward`. Esto indica que el historial del servidor (GitHub) contenía commits que no existían en el repositorio local, creando una divergencia.

**Hecho:** Se ejecutó `git pull` para descargar los cambios remotos y fusionarlos con la rama local. Tras la fusión, se pudo ejecutar `git push` con éxito.

**Detalle técnico:** El comando `git pull` es un atajo para `git fetch` (descargar el historial del servidor) seguido de `git merge origin/main` (integrar los cambios remotos en la rama local). Si no hay conflictos, Git crea automáticamente un "merge commit" para unir las dos líneas de historial.

**Motivo / criterio:** *Integridad del Historial*. Git bloquea los `push` "non-fast-forward" como un mecanismo de seguridad para prevenir la sobreescritura accidental de trabajo que ya existe en el servidor. La solución canónica es siempre integrar los cambios remotos (`pull`) antes de empujar los locales (`push`), garantizando que no se pierda ningún commit.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-27 — Docs: Cuadernillo sobre recuperación de datos y peligros de GUI en Git

**Contexto:** Tras un incidente donde la interfaz gráfica del editor (VS Code) indujo a la eliminación física accidental de una carpeta no versionada (`evidencias/`), surgió la necesidad de documentar la vulnerabilidad operativa de depender de herramientas visuales para el control de versiones.

**Hecho:** Se redactó el activo de conocimiento `laboratorio/Recuperación de datos y el peligro de los comandos destructivos en Git-cuadernillo` detallando el incidente y la maniobra forense de rescate.

**Detalle técnico:** El cuadernillo expone cómo la regla `.gitignore` oculta elementos en la vista del editor, provocando ilusiones ópticas de borrado, y documenta la recuperación de los archivos desde la papelera del sistema anfitrión, reafirmando el uso de `ls -la` en terminal nativa como diagnóstico definitivo.

**Motivo / criterio:** *Knowledge Management* (Gestión del conocimiento). Transformar un accidente operativo en documentación fundacional mitiga el riesgo de que futuros desarrolladores repitan el error. Asienta la directriz de que la terminal es la única fuente de verdad y justifica la obligatoriedad de la herramienta de backups locales.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-27 — Feat: Herramienta de copias de seguridad locales (Backup)

**Contexto:** El uso de interfaces gráficas o comandos complejos de Git conlleva el riesgo inherente de pérdida accidental de archivos locales no rastreados (ej. eliminación accidental al descartar cambios). Se requería un mecanismo "salvavidas" local antes de operar ramas o historiales.

**Hecho:** Se desarrolló `scripts/merci/merci-backup.py` y se añadió el directorio `backups/` al archivo `.gitignore`.

**Detalle técnico:** El script utiliza la librería estándar `zipfile` para empaquetar el árbol del proyecto de forma iterativa, excluyendo activamente directorios de infraestructura pesados (`.git`, `.venv`, `.assets-raw`) para garantizar una compresión rápida (Zip Deflated) y ligera.

**Motivo / criterio:** *Disaster Recovery* (Recuperación ante desastres). Proveer una herramienta CLI estandarizada que genere instantáneas locales (Snapshots) otorga confianza al desarrollador para realizar maniobras destructivas o refactorizaciones profundas sin depender exclusivamente del control de versiones remoto.

**Siguiente paso o deuda:** Iniciar el desarrollo de la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-27 — Fix: Purga profunda de evidencias en el historial de Git

**Contexto:** Aunque `.gitignore` prevenía la adición de nuevos archivos multimedia, si algún binario pesado en `laboratorio/evidencias/` había sido comiteado accidentalmente en el pasado, este seguiría existiendo en el historial profundo de Git, inflando el peso del repositorio y reapareciendo al restaurar versiones antiguas.

**Hecho:** Se ejecutó una reescritura completa del historial de Git (`filter-branch`) para erradicar cualquier rastro de los archivos de la carpeta de evidencias en todos los commits anteriores.

**Detalle técnico:** Se utilizó un filtro de índice en Git (`--index-filter`) para recorrer todo el árbol de commits y ejecutar `git rm --cached --ignore-unmatch` sobre la carpeta objetivo, seguido de un recolector de basura agresivo (`git gc --prune=now`) y un `git push --force` para sobrescribir el repositorio remoto.

**Motivo / criterio:** *Repository Hygiene* (Higiene del Repositorio). Git es un sistema inmutable por defecto. Para eliminar una fuga de datos o un binario pesado de forma retroactiva, es obligatorio reescribir la historia. Esto garantiza clones rápidos y protege las cuotas de almacenamiento del servidor.

**Siguiente paso o deuda:** Programar el script de copias de seguridad (Backup Local) en Python.

### 2026-04-27 — Fix: Exclusión estricta de evidencias del control de versiones

**Contexto:** La carpeta `laboratorio/evidencias/`, destinada a almacenar material multimedia pesado (vídeos, capturas) para futuros montajes, corría el riesgo de ser rastreada por Git y subida al servidor remoto, inflando el peso del repositorio.

**Hecho:** Se implementó una regla de exclusión estricta en `.gitignore` para `laboratorio/evidencias/*`, preservando únicamente el archivo `.gitkeep`.

**Detalle técnico:** Al igual que con el directorio `.assets-raw/`, esta regla permite que la estructura de carpetas persista en el proyecto mientras vuelve a Git completamente "ciego" ante los binarios que se depositen en su interior.

**Motivo / criterio:** Rigor de infraestructura. El sistema de control de versiones está diseñado para código, no para almacenamiento de archivos brutos o pesados. Aislar este contenido garantiza clones rápidos y evita alcanzar las cuotas de almacenamiento de las plataformas Git.

**Siguiente paso o deuda:** Definir y desarrollar la estrategia técnica para la publicación de estos contenidos visuales en el futuro (evaluar la incrustación de vídeos optimizados vs. GIFs animados simulando vídeos dentro de la documentación).

### 2026-04-27 — Feat: Auto-nombrado (Slugificación) de URLs en SSG

**Contexto:** Existía un acoplamiento rígido entre el nombre físico del archivo `.md` y la URL pública final (`.html`). Si el autor utilizaba nombres descriptivos o prefijos numéricos para organizar su entorno local, estos ensuciaban las rutas SEO de producción.

**Hecho:** Se implementó una función de `slugify` nativa en `scripts/merci/merci-publish.py` para generar los nombres de archivo de salida basándose estrictamente en el atributo `titulo` del YAML Frontmatter.

**Detalle técnico:** Se empleó la librería estándar `unicodedata` (`NFKD`) para normalizar y despojar al texto de acentos o diacríticos del español, y expresiones regulares (`re.sub`) para reemplazar espacios por guiones y eliminar caracteres inválidos para URLs.

**Motivo / criterio:** *Separation of Concerns* (Separación de Responsabilidades). Desacoplar la estructura del sistema de archivos local de la topología de URLs públicas mejora drásticamente la Developer Experience (DX). Permite reorganizar, renombrar y prefijar archivos `.md` localmente sin alterar enlaces indexados ni romper la arquitectura de la información web.

**Siguiente paso o deuda:** Desarrollar el script de copias de seguridad (Backup Local) en Python.

### 2026-04-27 — docs: Reestructuración nombres documentos a publicar

**Contexto:** Dificultad para relacionar visualmente los archivos compilados (`.html` / `.pdf`) con sus documentos origen (`.md`) en el editor debido a discrepancias o abreviaturas en los nombres físicos.

**Hecho:** Renombrar los archivos `.md` de la biblioteca para que coincidan exactamente con el título del documento, facilitando su localización a medida que el repositorio crece.

**Detalle técnico:** Modificación manual del nombre físico de los archivos directamente en el directorio local de la biblioteca.

**Motivo / criterio:** Ejecución manual justificada por el bajo volumen actual de archivos. Se asume la deuda técnica de automatizar el renombrado (slugificación) basado en el YAML Frontmatter en el futuro.

**Siguiente paso o deuda:** Estructurar la `biblioteca/` en subcarpetas temáticas (ej. `DevSecOps y Gobernanza/`) y refactorizar `merci-publish.py` para soportar lectura recursiva y auto-nombrado.

### 2026-04-27 — Feat: Clean Build automático en orquestador SSG

**Contexto:** Si un documento Markdown en la `biblioteca/` era renombrado o eliminado, el orquestador generaba la nueva versión pero los archivos `.html` y `.pdf` antiguos permanecían para siempre en `public/` como "archivos zombis". Requerir que el usuario ejecutara `rm -rf` manualmente era peligroso y propenso a errores.

**Hecho:** Se implementó el patrón de "Clean Build" (Compilación limpia) creando la función `limpiar_directorio_salida()` en `scripts/merci/merci-publish.py`.

**Detalle técnico:** Al iniciar el pipeline, el script escanea los directorios de destino (`public/biblioteca` y `public/descargas`) y ejecuta un `unlink()` estrictamente filtrado por las extensiones `.html` y `.pdf`. Esto garantiza que marcadores como `.gitkeep` u otros assets permanezcan intactos.

**Motivo / criterio:** *Zero Dead Code / DX (Developer Experience)*. El directorio de salida (public) debe ser un reflejo exacto y efímero del estado actual del directorio de origen (código fuente). Automatizar la purga antes de la compilación asegura esta paridad sin depender de comandos destructivos manuales por parte del desarrollador.

**Siguiente paso o deuda:** Crear el script Python para copias de seguridad locales (Backups) o avanzar a la Fase 9 (Inteligencia).

### 2026-04-27 — Fix: Restauración de lógica visual dinámica en SSG

**Contexto:** El orquestador de publicación estática (`merci-publish.py`) sobrescribía el diseño visual de las tarjetas forzando la clase CSS `.card--book` para todos los documentos de la Biblioteca, ignorando el atributo explícito `tipo: "cuadernillo"` definido por la autora en el YAML Frontmatter.

**Hecho:** Se refactorizó la asignación de variables de `clase_css` en `scripts/merci/merci-publish.py` tanto para la página individual como para el generador del índice.

**Detalle técnico:** Se implementó una lógica condicional en línea (Ternary Operator) que evalúa si el `tipo` es "cuadernillo" para inyectar el modificador BEM `.card--booklet`. Para cualquier otro caso, aplica degradación elegante devolviendo `.card--book`.

**Motivo / criterio:** *Single Source of Truth (SSOT)*. El motor de compilación debe respetar ciegamente las definiciones del archivo origen. Forzar clases CSS rompe la jerarquía de la información y la autoridad del Frontmatter.

**Siguiente paso o deuda:** Validar la visualización del borde naranja en los cuadernillos y continuar hacia la Fase 9 (Inteligencia) o el script de Backup Local.

### 2026-04-27 — Arquitectura: Implementación de Documentación en la Sombra (Shadow Docs)

**Contexto:** Al gobernar el Boilerplate desde este proyecto matriz, el `README.md` y las `instrucciones.md` entraban en colisión, ya que el repositorio padre y el hijo requieren documentaciones totalmente diferentes. Actualizar el clon manualmente era propenso a errores.

**Hecho:**
- Se crearon los archivos gemelos `-merci.md` (`README-merci.md`, `instrucciones-merci.md`) y `bitacora-merci-boilerplate.md` en este repositorio base.
- Se actualizó `merci-init.py` dotándolo de la capacidad de intercambiar los gemelos (borrar los personales y renombrar los agnósticos) durante el proceso de purga.

**Detalle técnico:** Se añadió el parámetro `exclude` a la función `purge_directory` para que la guillotina no arrasara con `bitacora-merci-boilerplate.md` al limpiar el laboratorio. Luego, mediante `Path.rename()`, se ascienden los archivos gemelos a su ruta oficial.

**Motivo / criterio:** *Shadow Documentation / IaC*. Almacenar la documentación del proyecto hijo "inactiva" en la matriz garantiza el control de versiones (SSOT) de todas las facetas del código. Automatizar su intercambio elimina el factor de error humano en el Release Pipeline iterativo.

**Siguiente paso o deuda:** Iniciar el desarrollo de la Fase 9 (Inteligencia y Autonomía) o el script local de Backups.

### 2026-04-27 — Docs: Definición del Release Pipeline Agile para el Boilerplate

**Contexto:** El proceso de actualizar y trasladar mejoras desde el proyecto matriz (`mercedev.es`) hacia el repositorio derivado (`merci-boilerplate`) corría el riesgo de sufrir "Configuration Drift" (Deriva de Configuración) si los bugs se parcheaban directamente en el destino.

**Hecho:**
- Se inyectó la Regla 14 en `instrucciones.md` dictando el flujo de trabajo circular estricto.
- Se redactó el cuadernillo divulgativo `cuadernillo-agile-release-pipeline.md` detallando la maniobra.

**Detalle técnico:** El flujo documentado exige que ante cualquier fallo detectado en el QA del boilerplate, se aborte el empaquetado, se corrija el código fuente en el proyecto matriz, y se reinicie el ciclo de clonación (`merci-init.py`) desde cero.

**Motivo / criterio:** Gobernanza de Repositorios y SSOT (Single Source of Truth). Aplicar metodologías *Agile* al despliegue de infraestructura garantiza que el proyecto original herede y capitalice siempre las soluciones descubiertas durante la exportación de plantillas.

**Siguiente paso o deuda:** Desarrollar el script de copias de seguridad locales (Backup) en Python.

### 2026-04-27 — Sincronización de Parches (Backport) desde Merci Boilerplate

**Contexto:** Durante el empaquetado del repositorio hijo (`merci-boilerplate`), se detectaron y solventaron deudas documentales como la falta de expansión del acrónimo JSON-LD, la omisión del entorno de desarrollo dual y la lista incompleta de herramientas en el `README.md`. Al ser `mercedev.es` la única fuente de verdad (SSOT), estos parches debían retroceder al proyecto matriz.

**Hecho:**
- Se expandió el acrónimo JSON-LD en `docs/flujo-publicacion-sop.md`.
- Se amplió el `README.md` listando el ecosistema DevSecOps completo (`merci-promote.py`, `merci-publish.py`, `merci-watcher.py`, etc.).
- Se inyectó la sección "Entorno de Desarrollo Local" al `README.md` de la matriz.

**Detalle técnico:** Modificaciones directas en los archivos Markdown para asegurar la paridad documental entre el Boilerplate generado y el motor anfitrión original.

**Motivo / criterio:** *Single Source of Truth (SSOT)*. Los errores solucionados en la plantilla derivada (fork) deben reflejarse retroactivamente en el repositorio padre (backporting) para evitar la deriva de configuración (Configuration Drift) y proteger la higiene del conocimiento de la rama principal.

**Siguiente paso o deuda:** Avanzar hacia la Fase 9 (Inteligencia y Autonomía) del asistente Merci.

### 2026-04-26 — Fix: Prevención de fuga de datos (Data Leak) en empaquetado

**Contexto:** Durante la creación de la Release 1.0.0 del Merci Boilerplate, se detectó que el clon resultante conservaba los archivos PDF generados por WeasyPrint en `public/descargas/`. Esto rompía la promesa de un "lienzo en blanco" y provocaba una fuga de datos (Data Leak) de los artículos de la autora hacia el repositorio público.

**Hecho:** Se parcheó el script destructivo `scripts/merci/merci-init.py` añadiendo la orden explícita de purgar el directorio de descargas.

**Detalle técnico:** Se incluyó la instrucción `purge_directory(REPO_ROOT / "public" / "descargas")` en el bloque de purga de datos históricos, asegurando que los artefactos binarios sean erradicados junto con el historial de Markdown y HTML.

**Motivo / criterio:** *Data Leak Prevention (Prevención de Pérdida de Datos)*. Un script que pretende empaquetar una infraestructura agnóstica debe ser exhaustivo. Dejar binarios compilados del autor original contamina el peso del repositorio de destino y expone propiedad intelectual que no forma parte del motor DevSecOps.

**Siguiente paso o deuda:** Desarrollar el script de copias de seguridad locales (Backup Local) en Python o avanzar hacia la Fase 9 (Inteligencia y Autonomía).

### 2026-04-26 — Feat: Script de instanciación del Boilerplate (Fase 10)

**Contexto:** Para convertir el repositorio en un producto reutilizable (Boilerplate Release 1.0.0), se necesitaba un mecanismo automatizado que permitiera a un usuario clonar el proyecto, limpiar todas las referencias personales (dominio, nombre) y purgar el historial documental sin tener que hacerlo archivo por archivo.

**Hecho:**
- Se creó el script destructivo `scripts/merci/merci-init.py`.
- Se implementó la purga automática de los directorios `biblioteca/`, `laboratorio/` y `public/biblioteca/`.
- Se implementó el reemplazo recursivo de la identidad (`mercedev.es`, `mercedev`, `Mercedes`) en todos los archivos de configuración y código fuente.
- Se marcó la Fase 10 como completada en el Roadmap.

**Motivo / criterio:** *Automation & Reusability*. Un boilerplate debe ser un lienzo en blanco para el nuevo desarrollador. Automatizar la inicialización cierra el ciclo de vida del proyecto, convirtiéndolo formalmente en la versión 1.0.0 lista para ser distribuida.

**Siguiente paso o deuda:** Dar por finalizado el roadmap fundacional, hacer el *push* definitivo y descansar.

### 2026-04-25 — Fix: Refuerzo de segregación de entornos (Zero Drafts in Library)

**Contexto:** Se detectó una violación de las reglas arquitectónicas: archivos con `estado: "borrador"`, tests huérfanos (`test-borrador.md`) o documentos con marcadores `TODO` pendientes estaban residiendo físicamente en el directorio fuente `biblioteca/`.

**Hecho:**
- Se ejecutó una purga manual moviendo el contenido crudo (`bitacora-merci-boilerplate.md`) de vuelta a `laboratorio/` y eliminando los archivos de test (`test-borrador.md`).
- Se eliminaron los HTML y PDF residuales generados por error en el entorno `public/`.
- Se asienta la regla estricta: El directorio `biblioteca/` en el código fuente es sagrado y solo puede alojar activos de conocimiento 100% curados y terminados.

**Motivo / criterio:** *Environment Segregation* (Segregación de Entornos). Mezclar contenido en incubación con contenido curado en el mismo directorio de origen destruye la confianza en el repositorio y genera fugas de información hacia el entorno de producción al compilar el SSG.

**Siguiente paso o deuda:** Modificar `merci-audit.py` en el futuro para que bloquee atómicamente los commits si detecta YAMLs con `estado: "borrador"` dentro de la carpeta `biblioteca/`.

### 2026-04-25 — Feat: Migración histórica y publicación del Volumen I (Fase 8.2)

**Contexto:** Tras perfeccionar el orquestador SSG (Static Site Generation - Generación de Sitios Estáticos) y el asistente de promoción, era el momento de validar el flujo completo vaciando la deuda documental del laboratorio y trasladando el historial fundacional (Volumen I) a la Biblioteca.

**Hecho:**
- Se promovió el archivo histórico a la `biblioteca/` mediante el asistente interactivo `merci-promote.py`.
- Se compiló el sitio estático y el PDF descargable con `merci-publish.py`.
- Se aprovechó para refactorizar y limpiar un evento duplicado (`DOMContentLoaded`) en `public/js/main.js` que había quedado como residuo de pruebas anteriores.

**Motivo / criterio:** *Content Lifecycle Management* (Gestión del Ciclo de Vida del Contenido). El flujo SOP (Standard Operating Procedure) diseñado demuestra su eficacia: redacción libre en laboratorio -> curación estricta con promote -> compilación automatizada con publish.

**Siguiente paso o deuda:** Marcar la Fase 8.2 como completada en el Roadmap y comenzar la investigación para dotar a Merci de capacidades avanzadas (Fase 9).

### 2026-04-25 — Fix: Control de errores (Fail Gracefully) en orquestador SSG

**Contexto:** El orquestador de publicación (`merci-publish.py`) carecía de manejo de excepciones en sus procesos críticos. Cualquier error puntual (un Markdown malformado, un fallo de WeasyPrint al enlazar imágenes o un error de permisos I/O) provocaría un colapso total del script (Fatal Error), deteniendo el pipeline e impidiendo la publicación del resto de documentos válidos.

**Hecho:**
- Se envolvieron los procesos de `markdown.markdown()`, `HTML().write_pdf()` y `.write_text()` en bloques `try-except`.
- Se implementó un retorno temprano (`return False`) con alertas por consola para saltar archivos corruptos.
- Se aplicó degradación elegante (`pass`) en caso de fallo de WeasyPrint.

**Motivo / criterio:** Principio de *Fail Gracefully* (Fallar con elegancia). Un pipeline DevSecOps maduro no se detiene por un solo elemento defectuoso. Capturar el error, reportarlo y continuar con el siguiente archivo garantiza la resiliencia de la cadena de suministro de contenido. Permitir que el HTML se publique aunque el PDF falle prioriza la disponibilidad del conocimiento por encima del formato secundario.

**Siguiente paso o deuda:** Comprometer este parche y proceder con la migración del Volumen I a la Biblioteca mediante `merci-promote` (Fase 8.2).

### 2026-04-25 — Feat: Soporte multimedia avanzado en SSG (Vídeos y PDFs)

**Contexto:** El motor SSG (`merci-publish.py`) parseaba correctamente el texto, pero el formato Markdown no soporta la etiqueta `<video>` nativamente, convirtiendo los archivos `.mp4` en etiquetas `<img>` rotas. Además, el generador de PDFs (WeasyPrint) no lograba renderizar las imágenes porque no lograba resolver las rutas estáticas (`/assets/`).

**Hecho:**
- Se implementó un pre-procesador *Regex* en Python que intercepta la sintaxis `!alt` y la transforma en un `<video>` HTML5 accesible.
- Se añadió el parámetro `base_url` a WeasyPrint apuntando a la raíz `/public`.
- Se implementó un patrón "Fallback" en SASS (`.video-fallback`) que oculta un mensaje de advertencia en la web, pero lo muestra en el PDF para indicar que hay un vídeo no imprimible.

**Motivo / criterio:** Robustez del ciclo de contenidos. Al resolver el `base_url`, los PDFs descargables ahora contendrán todas las capturas y esquemas integrados por el autor. Al usar Expresiones Regulares para el vídeo, ampliamos las capacidades de Markdown manteniendo las "0 dependencias" sin usar plugins externos que ralenticen la compilación.

**Siguiente paso o deuda:** Iniciar el ciclo de migración con la herramienta `merci-promote` (Fase 8.2) probando a publicar el primer Volumen que contendrá estos assets.

### 2026-04-25 — Feat: Enrutamiento por contexto para el cerebro de Merci (Fase 8.1)

**Contexto:** Tras integrar a Merci en todas las vistas (Fase 7.5), el asistente requería "conciencia de contexto" (saber en qué página está el usuario) para ofrecer respuestas útiles, sin sacrificar la velocidad ni requerir conexiones a una base de datos en tiempo real.

**Hecho:**
- Se refactorizó la clase `MerciController` en `public/js/MerciController.js`.
- Se implementó el método `_loadKnowledgeBase()` que lee `window.location.pathname`.
- Se añadieron diccionarios de respuestas específicos para `/biblioteca`, `/blog`, `/art-de-cote` y `/contacto`.
- Se abrió oficialmente la Fase 8 en el `README.md` y las instrucciones.

**Motivo / criterio:** *Context Routing* (Enrutamiento por Contexto) en Vanilla JS. En lugar de realizar peticiones `fetch` lentas a un backend, inyectar el conocimiento directamente en la clase y filtrarlo por la URL actual mantiene la latencia en 0 milisegundos y respeta la política de 0 dependencias externas.

**Siguiente paso o deuda:** Comprometer el código y planificar la migración de los cuadernillos antiguos a la biblioteca definitiva (Fase 8.2).

### 2026-04-25 — Feat: Implementación del asistente interactivo Merci (Fase 7.5)

**Contexto:** Era el momento de dar vida pública al asistente "Merci" en la interfaz web (Fase 7.5). El código original propuesto utilizaba bucles continuos (`setInterval`) para calcular posiciones y mover la imagen por la pantalla, lo que destrozaba el rendimiento (Layout Thrashing) y violaba las directrices de accesibilidad WAI-ARIA. Además, se requería organizar la carpeta de multimedia previendo el crecimiento futuro.

**Hecho:**
- Se reorganizó el directorio multimedia moviendo el avatar a la nueva ruta escalable `/assets/images/`.
- Se desarrolló el componente estructural BEM `_merci.scss` fijando al asistente mediante CSS.
- Se creó la clase `MerciController` en Vanilla JS (Programación Orientada a Objetos) actuando como máquina de estados.
- Se inyectó el componente HTML accesible en `public/index.html`, `public/contacto/index.html`, `src/wp-theme/merci-theme/index.php` y en el orquestador `merci-publish.py`.

**Detalle técnico:** En lugar de manipular el DOM y las coordenadas con JavaScript, el controlador interacciona estrictamente alternando atributos semánticos (`aria-hidden`, `aria-expanded`). Es el CSS el que reacciona a estos cambios de estado ARIA ejecutando transiciones suaves por GPU (`opacity`, `transform`). Esto garantiza un coste de CPU del 0% cuando el asistente está inactivo y asegura que los usuarios de teclado puedan tabular hacia él mediante el uso de un `<button>` nativo.

**Motivo / criterio:** *Rendimiento Extremo y Accesibilidad Universal*. Al anclar visualmente al asistente y delegar las animaciones al motor de hojas de estilo, erradicamos el temido Cumulative Layout Shift (CLS) y evitamos secuestrar el hilo principal (Main Thread) del navegador, manteniendo intacta nuestra puntuación de 100/100 en Core Web Vitals sin usar librerías externas de terceros.

**Siguiente paso o deuda:** Ejecutar el orquestador maestro (`merci-total`), confirmar que ninguna regla SEO ni de rendimiento ha sido penalizada, y ejecutar el commit atómico.

### 2026-04-25 — DevSecOps: Diagnóstico de fallo de suspensión (System Sleep)

**Contexto:** El entorno de desarrollo (Ubuntu) experimentó un "pantallazo gris" que forzó un reinicio abrupto tras la carga de pestañas pesadas en el navegador, sospechando inicialmente de una fuga de memoria (OOM).

**Hecho:**
- Se aisló el navegador abriéndolo mediante terminal (`google-chrome --incognito --restore-last-session=false`).
- Se auditaron los registros críticos del núcleo anterior mediante `journalctl -b -1 -p err`.

**Detalle técnico:** Los logs revelaron `Freezing user space processes failed` y `Failed to put system to sleep. System resumed again: Device or resource busy`. El colapso no fue por RAM, sino porque un proceso de usuario (posiblemente la aceleración de hardware del navegador o un hilo de Bluetooth) se negó a ceder el control al Kernel (ACPI) durante un intento de suspensión, bloqueando la interfaz gráfica.

**Motivo / criterio:** Trazabilidad estricta. Leer los logs del sistema desmiente suposiciones y revela la causa raíz de las inestabilidades. Esto valida empíricamente la necesidad de construir arquitecturas web ligeras (0 dependencias) que no saturen los manejadores de recursos (threads/GPU) del cliente.

### 2026-04-25 — Refactor: Purga de lógica de cuadernillos en SSG

**Contexto:** Tras pivotar la Arquitectura de la Información y delegar los "Cuadernillos" a WordPress (Art de Coté), el orquestador de publicación estática (`merci-publish.py`) y las plantillas conservaban código heredado y condicionales inútiles (deuda técnica).

**Hecho:**
- Se eliminaron las bifurcaciones condicionales para `.card--booklet` en `merci-publish.py`.
- Se actualizaron los textos de la página índice generada para reflejar la taxonomía de "Proyectos" y "Libros".
- Se refactorizó la plantilla base y se renombró de `plantilla-cuadernillo.md` a `plantilla-proyecto.md`.
- Se actualizó la publicación existente de alias absolutos cambiando su tipo a `bitacora`.

**Motivo / criterio:** *Zero Dead Code* (Cero Código Muerto). El código que no se usa es un lastre de mantenimiento. Si la biblioteca solo alberga proyectos y bitácoras fundacionales, el orquestador SSG debe simplificarse eliminando las comprobaciones innecesarias, cumpliendo así con la Navaja de Ockham.

**Siguiente paso o deuda:** Iniciar la Fase 7.5 subiendo el código JavaScript experimental de "Merci" al laboratorio.

### 2026-04-25 — Refactor: Pivote de Arquitectura de la Información (Libros vs Cuadernillos)

**Contexto:** Tras la reescritura de la portada (`public/index.html`) para alinearla con la realidad operativa del proyecto, se detectó que mantener dos tipos de contenido (Cuadernillos y Bitácoras/Libros) dentro de la Biblioteca estática generaba complejidad innecesaria en el mantenimiento.

**Hecho:**
- Se redefinió la taxonomía del contenido: "Proyectos / Libros" residirán exclusivamente en la **Biblioteca** (Núcleo Estático).
- "Cuadernillos / Exploraciones" residirán exclusivamente en la taxonomía **Art de Coté** (Capa Dinámica CMS/WordPress).
- Se actualizó el *copy* de la portada para reflejar esta nueva frontera arquitectónica.

**Motivo / criterio:** *Separation of Concerns* (Separación de Responsabilidades) y Arquitectura de la Información. Delegar el contenido divulgativo, efímero o exploratorio al entorno dinámico (WordPress) reduce la fricción de publicación. Reservar el motor de Generación de Sitios Estáticos (SSG) únicamente para manuales fundacionales pesados optimiza el uso de la herramienta de compilación a PDF y simplifica el pipeline a futuro.

**Siguiente paso o deuda:** (Opcional) Renombrar `docs/plantilla-cuadernillo.md` a `plantilla-proyecto.md` y limpiar la lógica heredada en `merci-publish.py` si se desea erradicar el concepto de "cuadernillo" del núcleo estático.

### 2026-04-25 — QA: Auditoría de Deuda Técnica y cierre de Fase 7.4

**Contexto:** Como parte del ciclo de mantenimiento y mejora continua (Fase 7.4), se procedió a escanear el repositorio en busca de marcadores `TODO` y deuda técnica acumulada en código o infraestructura.

**Hecho:**
- Se constató la ausencia de deuda técnica bloqueante en el código fuente (Python, SASS, JS).
- El único `TODO` restante es de carácter literario (Prólogo del Vol. I) y se encuentra correctamente aislado en el `laboratorio/`.
- Se verificó la sincronía total entre `README.md`, `instrucciones.md` y el `flujo-publicacion-sop.md`.
- Se marcó la Fase 7.4 como oficialmente completada.

**Motivo / criterio:** *Shift-Left Quality*. La ausencia de deuda técnica es el resultado directo de no haber tolerado integraciones a medias durante el desarrollo. Al solucionar la accesibilidad WAI-ARIA, los enlaces rotos y los artefactos huérfanos de forma inmediata, la fase de auditoría se convierte en una simple verificación de higiene.

**Siguiente paso o deuda:** Iniciar la Fase 7.5 (Producto Merci) para abordar la vida pública y la lógica de backend del asistente.

### 2026-04-25 — Docs: Estandarización del Runbook de Publicación (SOP)

**Contexto:** Al iniciar la Fase 7.4 y ante la proliferación de herramientas de consola creadas para el sistema Merci, la bitácora recogía un resumen escueto del orden de ejecución del pipeline, insuficiente para un proyecto de esta envergadura. Existía el riesgo de fricción cognitiva o fallos en cadena (ej. actualizar sitemap antes de compilar HTML).

**Hecho:**
- Se definió y documentó el Standard Operating Procedure (SOP) básico en el `README.md`.
- Se creó el documento de arquitectura detallado `docs/flujo-publicacion-sop.md` explicando el ciclo de vida del conocimiento.
- Se estableció el pipeline secuencial: `pull` -> `promote` -> `publish` -> `total` -> `commit` -> `push`.
- Se marcó el hito de mantenimiento del Roadmap como completado.

**Detalle técnico:** El nuevo documento especifica el porqué de cada paso. Por ejemplo, `merci publish` (compilación SSG) debe ejecutarse obligatoriamente *antes* que `merci total` (QA y Sitemap), ya que el escáner de enlaces (`linkcheck`) y el generador de `sitemap.xml` dependen de la existencia previa de los archivos HTML finales en la carpeta `public/` para funcionar correctamente.

**Motivo / criterio:** *Developer Experience (DX), Knowledge Management y Pipeline As Code*. Documentar el "Runbook" detallado transforma un conjunto de scripts sueltos en una verdadera cadena de montaje (CI/CD local). Delegar esta explicación profunda a un documento dedicado en `docs/` en lugar de saturar la bitácora respeta el principio de Separación de Responsabilidades Documentales.

**Siguiente paso o deuda:** Auditar la deuda técnica pendiente de las fases anteriores para dar por concluida la Fase 7.4.

### 2026-04-25 — Fix: Reubicación de borradores al entorno de incubación (Laboratorio)

**Contexto:** Tras extraer el Volumen I de la bitácora, el archivo resultante fue ubicado en la carpeta `biblioteca/` con estado `borrador` y tareas pendientes (Prólogo). Esto violaba el flujo del ciclo de vida del contenido de la Fase 7.3.

**Hecho:**
- Se reubicó físicamente el archivo `bitacora-mercedev-vol-I.md` de vuelta al `laboratorio/` mediante `git mv`.
- Se asienta la directriz de que ningún documento "en construcción" debe residir en la biblioteca.

**Motivo / criterio:** *Separación estricta de entornos (Environment Segregation).* La `biblioteca/` es un directorio exclusivo para activos de conocimiento finalizados. El `laboratorio/` es el entorno de incubación. Un borrador solo transiciona a la biblioteca en el momento exacto en que es "curado" y promovido a `publicado` mediante la herramienta `merci promote`.

**Siguiente paso o deuda:** Iniciar la Fase 7.4 (Mantenimiento y mejora continua).

### 2026-04-25 — Refactor: Arquitectura documental en 4 volúmenes (Saga mercedev)

**Contexto:** La bitácora del laboratorio crecía exponencialmente. Se requería trazar una línea divisoria clara entre la creación del motor (Fases 1-6) y las etapas posteriores, planificando el futuro de la identidad del proyecto.

**Hecho:**
- Se definió la arquitectura de conocimiento en 4 volúmenes: Vol I (Nacimiento del Boilerplate), Vol II (Construcción y automatización), Vol III (Vida oculta de Merci) y Vol IV (Vida pública de Merci).
- Se refactorizó el archivo del Volumen I en la biblioteca.
- Se purgó el historial antiguo de Fases 1 a 6 del laboratorio activo mediante un script de truncamiento.

**Motivo / criterio:** *Information Architecture* y escalabilidad cognitiva. Un documento infinito es inmanejable. Tratar el conocimiento técnico como una "Saga Literaria" encaja perfectamente con el pilar pedagógico, permitiendo que el laboratorio actual sea exclusivamente el borrador en vivo del Volumen II.

**Siguiente paso o deuda:** Iniciar la Fase 7.4 y redactar el prólogo del Volumen I cuando se considere oportuno.

### 2026-04-25 — Refactor: Establecimiento de regla pedagógica para bitácoras (Libro Presentación)

**Contexto:** Un extracto crudo del historial (Fases 1 a 6) fue promovido a producción automáticamente por un script, violando el pilar pedagógico del proyecto al presentar un volcado de logs sin narrativa introductoria.

**Hecho:**
- Se despublicó (`estado: "borrador"`) el archivo `biblioteca/bitacora-merci-boilerplate.md`.
- Se inyectó un esqueleto de "Prólogo" obligatorio.
- Se asienta la regla arquitectónica: Los datos crudos (logs) nunca se publican sin un marco de presentación didáctico.

**Motivo / criterio:** *Information Architecture* (Arquitectura de la Información) y UX Pedagógica. Un listado cronológico de commits no constituye un activo de conocimiento por sí solo si carece de contexto. Envolver el "ruido" técnico en un prólogo humano y estructurado transforma el historial en un verdadero "Libro".

**Siguiente paso o deuda:** Escribir el prólogo del Boilerplate y proceder con la planificación de la Fase 7.4.

### 2026-04-25 — Refactor: Escaneo dual y prevención de borradores zombis (merci-promote)

**Contexto:** Los documentos en `biblioteca/` que eran despublicados manualmente (pasando a `estado: "borrador"`) se convertían en "Dark Data" (datos invisibles), ya que el asistente de promoción solo escaneaba el `laboratorio/`. Esto forzaba a la edición manual del YAML para republicarlos, rompiendo el flujo.

**Hecho:**
- Se refactorizó `merci-promote.py` para realizar un escaneo dual (Laboratorio + Biblioteca).
- Se añadió el campo interactivo de `fecha` para permitir mantener la fecha original de publicación.
- Se dividió la lógica final para soportar traslados físicos (`unlink()`) y actualizaciones *in-place*.

**Motivo / criterio:** *Content Lifecycle Management* (Gestión del Ciclo de Vida del Contenido). Centralizar en una única herramienta CLI la transición de cualquier estado inmaduro o despublicado hacia la publicación definitiva elimina la fricción técnica. Pre-rellenar los inputs interactivos con los metadatos preexistentes maximiza la velocidad de republicación sin comprometer las validaciones de calidad estricta.

**Siguiente paso o deuda:** Con el ciclo de contenidos perfeccionado, abordar formalmente la planificación de la Fase 7.4 (Mantenimiento y Mejora Continua).

### 2026-04-25 — Fix: Despublicación activa de artefactos huérfanos en SSG

**Contexto:** Se detectó una fisura en el ciclo de vida del dato. Al cambiar manualmente un documento en `biblioteca/` de estado `publicado` a `borrador`, el orquestador lo saltaba y lo excluía del índice, pero los archivos HTML y PDF generados previamente quedaban huérfanos en `public/`, permaneciendo accesibles mediante su URL directa (fuga de información).

**Hecho:**
- Se refactorizó la máquina de estados en `scripts/merci/merci-publish.py`.
- Se implementó una lógica de "Despublicación Activa" (Kill-Switch).

**Detalle técnico:** Antes de abortar el procesamiento de un archivo que no sea `publicado`, el script resuelve las rutas de salida (`html_target.exists()`) y ejecuta un `unlink()` para purgar físicamente los activos del servidor si existen, emitiendo una alerta `🗑️ Despublicando` por consola.

**Motivo / criterio:** *State Synchronization* (Sincronización de Estado). El estado `borrador` no debe ser solo una omisión de compilación, sino una orden destructiva en el entorno de producción que garantice que el frontend refleje exactamente la intención actual del origen de datos, previniendo artefactos zombis.

**Siguiente paso o deuda:** Iniciar la planificación de la Fase 7.4 (Mantenimiento y mejora continua).

### 2026-04-25 — Feat: Asistente interactivo de promoción (merci-promote.py)

**Contexto:** Existía un hueco operativo (Fase 7.3) entre la redacción de un borrador en el `laboratorio/` y su publicación en la `biblioteca/`. Hacer este traslado manualmente era propenso a errores (olvidos de metadatos, fechas incorrectas o estados inconsistentes).

**Hecho:**
- Se creó el script interactivo CLI `scripts/merci/merci-promote.py`.
- Se marcaron los hitos de la Fase 7.3 como completados en el `README.md`.
- Se validó la promoción del primer borrador de prueba (`test-borrador.md`).

**Detalle técnico:** El script escanea el directorio efímero, parsea el YAML sin dependencias externas (`re` y manipulación de cadenas), solicita la curación interactiva de campos críticos (bloqueando si falta el `alt_portada` para WAI-ARIA), sella la fecha actual, cambia el `estado` a `publicado` y mueve físicamente el archivo al directorio definitivo.

**Motivo / criterio:** *Fricción Cero y Shift-Left Data Quality*. Proveer una herramienta de consola (CLI) para "curar" el documento antes de moverlo previene que archivos incompletos contaminen el entorno de producción. La interactividad actúa como un *checklist* guiado que garantiza el cumplimiento estricto de la accesibilidad y el SEO estructural.

**Siguiente paso o deuda:** Comenzar la planificación de la Fase 7.4 (Mantenimiento y mejora continua) y Fase 7.5, aprovechando que el ejecutor inteligente `merci promote` ya lo reconoce automáticamente.

### 2026-04-25 — Fix: Retrocompatibilidad YAML y validación WAI-ARIA

**Contexto:** Al implementar la máquina de estados y la validación WAI-ARIA estricta en el orquestador (`merci-publish.py`), el documento heredado `cuadernillo-alias-absolutos.md` fue bloqueado y excluido de la compilación por carecer de los campos obligatorios `estado` y `alt_portada`.

**Hecho:**
- Se parcheó manualmente `biblioteca/cuadernillo-alias-absolutos.md` inyectando `estado: "publicado"` y una descripción detallada en `alt_portada`.
- Se ejecutó `merci-publish.py`, confirmando que el orquestador compila el documento y genera el PDF correctamente.

**Motivo / criterio:** Principio "Fail-Fast" y cero tolerancia a la deuda técnica. Que el orquestador bloquee un archivo antiguo demuestra que el escudo de accesibilidad funciona empíricamente. Parchear el origen de datos (el Markdown) es la única vía permitida para integrarlo, garantizando que el HTML resultante mantenga la puntuación 100/100 en Core Web Vitals (Accesibilidad).

**Siguiente paso o deuda:** Diseñar e implementar la herramienta de promoción interactiva (`merci-promote.py`) para la Fase 7.3.

### 2026-04-25 — Feat: Máquina de estados y validación de accesibilidad en orquestador

**Contexto:** Se requería que el orquestador de publicación (`merci-publish.py`) discriminara entre borradores y documentos definitivos listos para compilar, además de blindar la accesibilidad exigiendo la presencia del atributo `alt_portada`. Paralelamente, surgió el dilema de si optimizar el motor introduciendo un sistema de caché basado en hashes de archivos.

**Hecho:**
- Se implementó una máquina de estados (Feature Toggle) basada en la clave YAML `estado` en `merci-publish.py`.
- Se introdujo una aserción estricta WAI-ARIA que bloquea el parseo si el YAML carece de `alt_portada`.
- Se descartó deliberadamente la implementación de caché por hashes.

**Detalle técnico:** El script ahora realiza retornos tempranos (`return False`) de forma silenciosa para archivos que no posean explícitamente `estado: "publicado"`. Asimismo, si el campo `alt_portada` está vacío, aborta la compilación de ese archivo lanzando un error en consola.

**Motivo / criterio:** *Premature Optimization* (Optimización Prematura). Procesar Markdown a HTML en Python es extremadamente rápido. Introducir una caché estática impediría que los artículos antiguos heredaran instantáneamente los cambios en el menú o el pie de página globales (Single Source of Truth) extraídos de la portada, provocando inconsistencia visual. Además, la aserción de la portada blinda mecánicamente la métrica de accesibilidad 100/100 de Lighthouse sin depender de la memoria del autor.

**Siguiente paso o deuda:** Desarrollar el flujo de promoción (Fase 7.3) mediante un script interactivo (`merci-promote.py`) para trasladar y estandarizar borradores desde el laboratorio hacia la biblioteca.

### 2026-04-25 — Refactor: Optimización de metadatos YAML para accesibilidad y pipeline

**Contexto:** Antes de diseñar el script de promoción de contenidos (Fase 7.3), era imperativo auditar la estructura de datos YAML para asegurar que soportara los requisitos de accesibilidad estricta (Core Web Vitals) y el control de flujo del orquestador.

**Hecho:**
- Se añadieron los campos `estado` y `alt_portada` a `docs/plantilla-cuadernillo.md`.
- Se refactorizó retroactivamente `biblioteca/auditoria-rendimiento.md` para cumplir con el nuevo esquema.

**Motivo / criterio:** *Shift-Left Data Design*. Añadir `alt_portada` garantiza desde el origen que el SSG (Static Site Generation) genere etiquetas `<img>` 100% compatibles con WAI-ARIA, evitando penalizaciones de Lighthouse. El campo `estado` (`borrador` vs `publicado`) dota al orquestador de una máquina de estados sencilla para filtrar documentos incompletos durante el proceso de compilación, protegiendo el entorno de producción.

**Siguiente paso o deuda:** Diseñar el flujo operativo y el script de Python para la promoción automatizada de contenidos (Fase 7.3).

### 2026-04-24 — Fix: Resolución de conflicto de enlace simbólico en producción

**Contexto:** Al ejecutar `git pull` en el servidor de producción (CloudPanel), Git abortó la sincronización alertando que los cambios locales en `public/blog` serían sobrescritos. Esto ocurrió porque el enlace simbólico había sido eliminado del índice del repositorio (`git rm --cached`) en una sesión anterior para aislarlo del control de versiones.

**Hecho:**
- Se eliminó temporalmente el enlace simbólico físico en el servidor de producción.
- Se ejecutó la actualización del repositorio (`git pull`) integrando el nuevo `.gitignore`.
- Se reconstruyó manualmente el enlace simbólico (`ln -s`) apuntando al directorio aislado de WordPress.

**Detalle técnico:** Comandos ejecutados secuencialmente en el servidor: `rm public/blog`, seguido de `git pull`, y finalmente `ln -s /home/mercedev-php/htdocs/wordpress /home/mercedev-php/htdocs/mercedev.es/public/blog`.

**Motivo / criterio:** Git implementa mecanismos de seguridad (Fail-Safe) para no destruir archivos locales sin seguimiento que colisionan con el árbol entrante. Destruir y recrear este puente de infraestructura tras aplicar el `.gitignore` actualizado vuelve a Git "ciego" ante el enlace, garantizando que los futuros despliegues fluyan con cero fricción.

**Siguiente paso o deuda:** Iniciar el diseño del flujo de promoción de contenidos (Fase 7.3).

### 2026-04-24 — Feat: Estandarización de plantillas de conocimiento (Fase 7.2)

**Contexto:** Para agilizar el flujo de creación de contenido y asegurar que todas las futuras publicaciones de la Biblioteca cumplan con los requisitos del orquestador (`merci-publish.py`), era necesario establecer una plantilla reutilizable.

**Hecho:**
- Se creó el archivo `docs/plantilla-cuadernillo.md`.
- Se consolidó la estructura obligatoria de metadatos (YAML Frontmatter) y la arquitectura de la información basada en 5 átomos (Contexto, Hecho, Detalle técnico, Motivo, Fuentes).

**Motivo / criterio:** Fricción Cero y Consistencia Editorial. Extraer el formato a una plantilla estática en el directorio de documentación evita que el autor dependa de la memoria o tenga que copiar archivos antiguos, garantizando que el pipeline SSG (Static Site Generation) y la inyección SEO no fallen por atributos omitidos.

**Siguiente paso o deuda:** Empaquetar el commit atómico, definir el flujo de movimiento Laboratorio -> Biblioteca (Fase 7.3) y continuar el roadmap.

### 2026-04-24 — QA: Falsos positivos de accesibilidad por extensiones del navegador

**Contexto:** Durante la auditoría manual de accesibilidad por teclado (tabulación), se detectó que el foco caía en un "agujero negro" de múltiples saltos (tabs fantasma) antes de retornar a la navegación de la web.

**Hecho:**
- Se inyectó un rastreador de eventos JS en la consola del navegador (`document.addEventListener('focusin', ...)`).
- El registro (log) reveló que el foco estaba siendo secuestrado por el elemento `<chatgpt-sidebar>`, el cual es inyectado de forma invisible por una extensión instalada en el navegador del usuario.

**Motivo / criterio:** Aislamiento del entorno de pruebas. Las extensiones del navegador inyectan Shadow DOM y elementos en el código fuente de las páginas visitadas, alterando el árbol de accesibilidad real. Las auditorías manuales (WAI-ARIA) y automáticas (Lighthouse) deben ejecutarse siempre en ventanas de Incógnito/InPrivate puras para evitar depurar "código fantasma" ajeno al proyecto.

**Siguiente paso o deuda:** Realizar el commit atómico de este aprendizaje y avanzar a la Fase 7.2.

### 2026-04-24 — Fix: Purgado de "Tabs Fantasma" y botón de salto a contenido

**Contexto:** Realizando pruebas de accesibilidad, se detectaron dos comportamientos indeseados durante la navegación por teclado: 1) el botón de accesibilidad "Saltar al contenido principal" resultaba redundante según los nuevos criterios, y 2) tras sobrepasar el footer con la tecla tabulador, el foco caía en unos 10 "tabs fantasma" antes de retornar al navegador web.

**Hecho:**
- Se eliminó completamente la etiqueta `<a href="#main" class="skip-link">` de la portada estática (`public/index.html`) y de la plantilla dinámica de WordPress (`src/wp-theme/merci-theme/index.php`).
- Se purgó el bloque CSS `.skip-link` de la arquitectura SASS (`_header.scss`) y se retiró el `tabindex="-1"` del contenedor `<main>`.
- Se añadió el filtro `add_filter('show_admin_bar', '__return_false');` en `functions.php`.
- Se ejecutó el pipeline completo de validación y compilación (`merci-total.py`).

**Motivo / criterio:** Los "tabs fantasma" en la ruta dinámica (`/blog`) eran provocados por los enlaces ocultos de la *Admin Bar* inyectada por WordPress mediante `wp_footer()` para usuarios logueados. Dado que el frontend está desacoplado (estilo Headless/Boilerplate), mantener la barra generaba conflictos de foco. Ocultarla purga estos enlaces invisibles del DOM y restaura la paridad entre las capas estática y dinámica.

**Siguiente paso o deuda:** Validar la limpieza de la navegación con tabulador sin los enlaces fantasma.

### 2026-04-24 — Fix: Refactorización arquitectónica de foco WAI-ARIA (Eliminación de tabindex en body)

**Contexto:** Se detectó que inyectar `tabindex="-1"` en la etiqueta `<body>` constituía un anti-patrón de accesibilidad. Hacer que el contenedor global del DOM fuera enfocable causaba que los lectores de pantalla reiniciaran la lectura desde el principio al activar el enlace "Volver arriba", abría vectores de "secuestro de foco" por clics inadvertidos y provocaba bugs visuales (Tap Highlight) en navegadores WebKit como iOS Safari.

**Hecho:**
- Se eliminó el atributo `tabindex="-1"` de la etiqueta `<body>` en `public/index.html`, `src/wp-theme/merci-theme/index.php` y `scripts/merci/merci-publish.py`.
- Se trasladó el identificador `id="top"` y su respectivo `tabindex="-1"` al elemento `<header>`, siendo este el primer bloque lógico y semántico de la estructura.
- Se recompilaron los activos estáticos de la biblioteca mediante `.venv/bin/python scripts/merci/merci-publish.py`.

**Motivo / criterio:** WAI-ARIA estricto y Focus Management. El foco de teclado nunca debe viajar al elemento raíz del documento (`<body>`). Al delegar la recepción del foco al `<header>`, el usuario que activa "Volver arriba" queda correctamente posicionado al inicio del contenido semántico, listo para interactuar con la navegación principal sin efectos colaterales indeseados.

**Siguiente paso o deuda:** Validar la restitución del comportamiento esperado del tabulador y proceder a empaquetar el commit atómico.

### 2026-04-24 — Fix: Resolución de foco en enlaces ancla WAI-ARIA (Tabindex)

**Contexto:** Tras implementar los enlaces de accesibilidad ("Saltar al contenido" y "Volver arriba"), se reportó que la navegación por teclado (Tabulador) seguía desfasada. Al hacer clic en los enlaces ancla, el navegador desplazaba la pantalla, pero el foco interno del teclado no viajaba al destino, obligando al usuario a tabular múltiples veces por la interfaz del navegador.

**Hecho:**
- Se inyectó el atributo `tabindex="-1"` en los contenedores destino (`<main id="main">` y `<body id="top">`) en todos los archivos estructurales (`index.html`, `merci-publish.py`, `index.php`).
- Se añadió la regla CSS `[tabindex="-1"]:focus { outline: none; }` en `_header.scss` para prevenir bordes de foco antiestéticos al activarse.
- Se aprovecharon los cambios para inyectar las anclas faltantes en la capa dinámica (`index.php`) que habían sido omitidas.

**Motivo / criterio:** Gestión estricta del foco (Focus Management). Los navegadores modernos no mueven automáticamente el cursor de tabulación a elementos semánticos (como `<main>` o `<body>`) al resolver un enlace ancla a menos que se declaren explícitamente como enfocables mediante `tabindex="-1"`. Este atributo permite recibir foco vía enlace sin alterar el orden natural de tabulación.

**Siguiente paso o deuda:** Validar la experiencia de tabulación, ejecutar un commit atómico y continuar con la Fase 7.2.

### 2026-04-24 — Fix: Resolución de conflicto de dependencias (Pillow 12 vs WeasyPrint)

**Contexto:** Al intentar instalar `weasyprint==63.0`, el gestor de paquetes `pip` arrojó un error de resolución imposible (`ResolutionImpossible`). Se diagnosticó que la versión `63.0` de WeasyPrint limitaba estrictamente su compatibilidad a `Pillow < 11`, colisionando frontalmente con `Pillow==12.2.0` (actualizado recientemente por motivos de seguridad).

**Hecho:**
- Se actualizó el anclaje en `requirements.txt` de `weasyprint==63.0` a la versión moderna `weasyprint==68.1`.

**Motivo / criterio:** Supply Chain Security. En ecosistemas DevSecOps, retroceder una librería base (Pillow) a una versión antigua con vulnerabilidades conocidas (CVE) para satisfacer a una herramienta de exportación secundaria es un antipatrón inaceptable. La solución arquitectónica correcta es avanzar la herramienta secundaria (WeasyPrint) hasta la versión (`68.1`) que dé soporte oficial a la librería parcheada.

**Siguiente paso o deuda:** Ejecutar la instalación de dependencias, validar la generación del PDF y dar por concluida la Fase 7.1.

### 2026-04-24 — Fix: Resolución de incompatibilidad de WeasyPrint (Supply Chain)

**Contexto:** Durante la generación del PDF en el orquestador de publicación (`merci-publish.py`), la ejecución colapsó con el error `AttributeError: 'super' object has no attribute 'transform'`. El diagnóstico reveló una incompatibilidad entre la versión anclada `weasyprint==62.1` y la actualización reciente de una de sus subdependencias internas (`pydyf`) en entornos con Python 3.12.

**Hecho:**
- Se actualizó la dependencia en `requirements.txt` de `weasyprint==62.1` a `weasyprint==63.0`.

**Motivo / criterio:** Mantenimiento de la cadena de suministro de software (Supply Chain). En DevSecOps, cuando una subdependencia transitiva rompe la librería principal, la maniobra correcta es dar el salto a la siguiente *release* estable del paquete anfitrión que haya mitigado la incompatibilidad, en lugar de intentar parchear el código fuente o degradar módulos individuales.

**Siguiente paso o deuda:** Re-instalar dependencias, validar la generación exitosa de los PDFs y dar por cerrada la funcionalidad.

### 2026-04-24 — Feat: Generación automatizada de artefactos PDF (WeasyPrint)

**Contexto:** Se requería dotar a la Biblioteca de la capacidad de generar y ofrecer versiones descargables en PDF de cada artículo para facilitar el consumo offline, la preservación del conocimiento y el formato de "libro/cuadernillo".

**Hecho:**
- Se integró la librería `weasyprint` en el pipeline de publicación.
- Se actualizó `merci-publish.py` para compilar un diseño específico de impresión (con portada generada dinámicamente usando metadatos YAML y saltos de página).
- Se inyectó un botón de descarga (`.card__download`) en las páginas HTML generadas apuntando a la nueva ruta `public/descargas/`.

**Motivo / criterio:** SSG Avanzado y Cero Fricción. Generar el PDF en el mismo instante de la compilación asegura que la versión web y la descargable jamás estén desincronizadas. Se utilizó WeasyPrint por ser el estándar más robusto y moderno en Python para interpretar HTML/CSS hacia PDF nativo sin depender de binarios de navegadores pesados.

**Siguiente paso o deuda:** Validar la visualización del PDF, actualizar la portada con los últimos artículos (si aplica) y dar por cerrada la Fase 7.1.

### 2026-04-24 — Refactor: Paridad WAI-ARIA en WP y corrección arquitectónica SASS 7-1

**Contexto:** Tras implementar el patrón de accesibilidad (skip-link y anclas de retorno) en el núcleo estático, la capa dinámica (WordPress) quedó desincronizada. Además, se detectó que los estilos del bloque principal (`.header`) debían ubicarse estrictamente según el patrón SASS 7-1.

**Hecho:**
- Se ubicó la regla `.skip-link` y los estilos de cabecera en `src/scss/layout/_header.scss` (reafirmando la arquitectura 7-1).
- Se inyectaron los identificadores `#top`, `#main` y el enlace de retroceso (`↑ Volver arriba`) en `src/wp-theme/merci-theme/index.php`.

**Motivo / criterio:** Paridad Dev-Prod y Arquitectura Estricta. En SASS 7-1, los contenedores estructurales (`header`, `footer`) pertenecen al directorio `layout/`, reservando `components/` para widgets reusables (`cards`, `buttons`). Mantener la accesibilidad sincronizada entre Nginx y PHP garantiza una experiencia unificada.

**Siguiente paso o deuda:** Validar la capa dinámica, empaquetar el commit atómico y comenzar la generación de artefactos PDF (Fase 7.1).

### 2026-04-24 — Feat: Patrones de accesibilidad WAI-ARIA (Skip-link y Volver arriba)

**Contexto:** Al auditar la navegación por teclado (Tab), se detectó que tras interactuar con la última publicación (segunda entrada), el foco escapaba a la interfaz del navegador, requiriendo unas 10 pulsaciones para dar la vuelta y reingresar a la web. Además, se forzaba al usuario a tabular por todo el menú principal en cada carga de página.

**Hecho:**
- Se inyectó un enlace oculto `.skip-link` (`Saltar al contenido principal`) al inicio del `<header>`, que se hace visible al recibir el foco.
- Se implementó un enlace de ancla (`↑ Volver arriba`) en el footer.
- Se actualizaron las etiquetas `<body>` y `<main>` en `public/index.html` y `merci-publish.py` añadiendo los anclajes de ID (`#top`, `#main`).

**Motivo / criterio:** WAI-ARIA y Experiencia de Usuario (UX) inclusiva. Un usuario de teclado no debe caer en un "bucle ciego" al llegar al final de la página, ni verse obligado a recorrer menús repetitivos para leer el contenido.

**Siguiente paso o deuda:** Compilar, verificar el funcionamiento con el tabulador, empaquetar el commit atómico y proceder con los PDFs.

### 2026-04-24 — Feat: Enlace de retroceso (UX) en publicaciones individuales

**Contexto:** Las páginas individuales generadas por `merci-publish.py` carecían de un método rápido y contextual para regresar al índice temático de la Biblioteca, obligando al usuario a usar el botón "Atrás" del navegador o buscar en el menú principal.

**Hecho:**
- Se añadió la clase BEM `.card__back-link` en `src/scss/components/_card.scss`.
- Se actualizó el orquestador `scripts/merci/merci-publish.py` para inyectar dinámicamente este enlace (`← Volver a la Biblioteca`) en la cabecera de cada artículo renderizado.

**Motivo / criterio:** Experiencia de Usuario (UX) y navegabilidad. Proveer enlaces de retroceso contextuales reduce la fricción cognitiva, retiene al usuario en el flujo de la aplicación y fomenta la exploración de otras estanterías temáticas.

**Siguiente paso o deuda:** Empaquetar el commit atómico y proceder con la investigación para la generación de los PDFs.

### 2026-04-24 — Fix: Resolución de advertencia SEO (JSON-LD) en el índice de la Biblioteca

**Contexto:** El orquestador local (`merci-total`) reportó una advertencia (`WARN SEO_JSONLD`) indicando que el índice principal de la Biblioteca carecía de datos estructurados, lo cual penaliza el SEO técnico y rompe el estándar de la Fase 2.

**Hecho:**
- Se actualizó la función `generar_indice_biblioteca()` en `scripts/merci/merci-publish.py`.
- Se inyectó dinámicamente un bloque `<script type="application/ld+json">` utilizando el esquema `@type: CollectionPage`.

**Motivo / criterio:** Al migrar la página principal de la Biblioteca a un modelo auto-generado (SSG - Static Site Generation), el archivo HTML perdió sus metadatos estáticos originales. Reintegrar la generación del JSON-LD en el orquestador asegura el cumplimiento de la política estricta de SEO y silencia la advertencia del linter local de manera definitiva.

**Siguiente paso o deuda:** Empaquetar el commit atómico y proceder con la investigación para la generación de los PDFs.

### 2026-04-24 — Feat: Patrón "Stretched Link" en tarjetas de Biblioteca

**Contexto:** En el índice autogenerado de la Biblioteca, solo el texto del título era interactivo. Se requería que toda la superficie de la tarjeta (`.card`) fuera clicable para mejorar la experiencia de usuario (UX) sin ensuciar la semántica HTML5.

**Hecho:**
- Se añadió `position: relative;` al bloque base `.card` en `src/scss/components/_card.scss`.
- Se implementó el pseudoelemento `::after` con `inset: 0;` en el enlace del título (`.card__title a`).
- Se vinculó el cambio de color (`:hover`) del título al estado hover de la tarjeta completa.

**Motivo / criterio:** Semántica y Accesibilidad. Envolver bloques enteros (`<article>`, `<header>`, `<p>`) dentro de una etiqueta `<a>` es válido en HTML5, pero entorpece a los lectores de pantalla. El patrón *Stretched Link* (Enlace Estirado) expande el área clicable del título principal mediante CSS para cubrir su contenedor, manteniendo un DOM limpio, ligero y 100% accesible.

**Siguiente paso o deuda:** Empaquetar el commit atómico y proceder a la investigación para la generación de los PDFs.

### 2026-04-24 — Refactor: Reestructuración temática del índice de Biblioteca (Estanterías)

**Contexto:** La generación del sitio estático para la Biblioteca (`merci-publish.py`) organizaba el contenido cronológicamente (como un blog). Esto violaba la filosofía fundacional de la "Biblioteca", que define el contenido como conocimiento inmutable ordenado por "estanterías" temáticas, delegando la presentación cronológica a la capa dinámica de WordPress (`/blog`).

**Hecho:**
- Se añadió el campo `tema` en el bloque de metadatos YAML de todas las publicaciones de la biblioteca.
- Se refactorizó la función `generar_indice_biblioteca()` en `merci-publish.py` para agrupar los artículos por tema (diccionarios) y renderizarlos en secciones separadas (`<section>`).

**Motivo / criterio:** Arquitectura de la Información y Gestión del Conocimiento. Separar la estructura mental del usuario. El Blog es un flujo temporal (novedades, anuncios); la Biblioteca es un índice de consulta directa agrupado semánticamente (Arquitectura, DevSecOps, SASS).

**Siguiente paso o deuda:** Empaquetar el cambio en un commit atómico y proceder a la investigación para la generación de los PDFs.

### 2026-04-24 — Feat: Auto-generación del índice de la Biblioteca (SSG)

**Contexto:** Se generaban las publicaciones individuales en HTML, pero la página principal de la Biblioteca (`public/biblioteca/index.html`) no existía o no enlazaba dinámicamente el nuevo contenido, obligando a añadir los enlaces manualmente.

**Hecho:**
- Se refactorizó `scripts/merci/merci-publish.py` para recolectar los metadatos de las publicaciones procesadas.
- Se implementó la función `generar_indice_biblioteca()` para compilar automáticamente el `index.html` con una cuadrícula de tarjetas ordenadas por fecha descendente.

**Motivo / criterio:** Fricción Cero y SSG (Static Site Generation - Generación de Sitios Estáticos). Automatizar la creación del índice elimina la necesidad de editar HTML manualmente, protegiendo el diseño y evitando el error humano de publicar un artículo y olvidar enlazarlo.

**Siguiente paso o deuda:** Empaquetar el commit atómico y proceder a la investigación sobre generación de PDFs.

### 2026-04-24 — Fix: Resolución de auditoría SEO en orquestador de publicación

**Contexto:** El orquestador maestro (`merci-total`) abortó el pipeline al detectar que las páginas HTML generadas por `merci-publish.py` carecían de etiquetas SEO obligatorias (meta descripción, URL canónica y JSON-LD), lo cual habría provocado penalizaciones en buscadores.

**Hecho:**
- Se añadió el atributo `descripcion` en el YAML Frontmatter de los archivos Markdown de la biblioteca.
- Se actualizó `scripts/merci/merci-publish.py` para leer dicha descripción y generar dinámicamente las etiquetas `<meta>`, `<link rel="canonical">` y el bloque `<script type="application/ld+json">`.
- Se superó exitosamente la auditoría estricta de `merci-audit.py` logrando 0 errores y 0 advertencias.

**Detalle técnico:** La inyección de metadatos se realiza directamente en el orquestador de Python usando *f-strings*. El esquema de datos estructurados (JSON-LD) se configura con el `@type` `Article`, nutriéndose de los mismos metadatos del YAML para evitar que el desarrollador introduzca información redundante de forma manual.

**Motivo / criterio:** Shift-Left SEO y validación cruzada. El pipeline ha demostrado su valor al actuar como barrera protectora estricta. Solventar este error a nivel de orquestador asegura automáticamente las mejores prácticas de SEO para cualquier futuro artículo publicado.

**Siguiente paso o deuda:** Empaquetar el commit atómico y proceder a la fase de generación automática de artefactos descargables (PDF).

### 2026-04-24 — Fix: Retrocompatibilidad YAML y refinamiento tipográfico SASS

**Contexto:** Durante la ejecución del orquestador de publicación (`merci-publish`), el archivo `auditoria-rendimiento.md` (heredado de la Fase 6) fue bloqueado por carecer de metadatos YAML. Además, el HTML generado a partir de Markdown presentaba una densidad visual alta, requiriendo mayor espaciado entre capítulos para mejorar la legibilidad.

**Hecho:**
- Se inyectó el bloque estandarizado YAML Frontmatter en `auditoria-rendimiento.md`.
- Se añadieron reglas de espaciado (`margin-top`, `margin-bottom`) específicas para encabezados (`h2`, `h3`) y párrafos generados dinámicamente dentro de `.card__content` en la arquitectura SASS.
- Se validó la generación e integración exitosa de ambas publicaciones en el núcleo estático.

**Motivo / criterio:** La política de "Fail-Fast" del orquestador protege el entorno de producción al rechazar archivos malformados, obligando a actualizar la deuda técnica documental. La encapsulación de estilos de Markdown dentro de `.card__content` mantiene el SASS global limpio (Separation of Concerns).

**Siguiente paso o deuda:** Empaquetar el commit atómico e investigar la generación automatizada de artefactos PDF para la biblioteca.

### 2026-04-24 — Feat: Orquestador de publicación estática y abstracción de UI

**Contexto:** Se necesitaba un sistema para transformar los documentos Markdown curados de la biblioteca en páginas HTML estáticas, pero sin duplicar el código del menú (header) y el pie de página (footer) de la web. Además, el script reportó un fallo al intentar procesar archivos heredados (`auditoria-rendimiento.md`) que carecían de metadatos.

**Hecho:**
- Se creó `scripts/merci/merci-publish.py` para parsear Markdown con YAML Frontmatter.
- Se implementó un sistema de extracción dinámica mediante expresiones regulares que lee `public/index.html` para recortar y reutilizar las etiquetas `<header>` y `<footer>`.
- Se validó el "fail-fast" del script frente a archivos sin YAML válido.

**Motivo / criterio:** Single Source of Truth (Única Fuente de Verdad). En lugar de crear motores de plantillas complejos, el script extrae los componentes globales directamente del HTML compilado de la portada. Esto garantiza que cualquier cambio futuro en el menú de la web se propague automáticamente a las publicaciones sin tocar Python. El rechazo de archivos antiguos sin YAML protege el entorno de producción de documentos malformados.

### 2026-04-24 — Docs: Refactorización a MVP de cuadernillo con YAML Frontmatter

**Contexto:** El borrador sobre el problema de los alias y el autodescubrimiento en Python contenía volcados de consola sin procesar. Se requería estructurarlo como un "Producto Mínimo Viable" (MVP) para la biblioteca y añadir el descubrimiento sobre la retención de alias fantasma en la memoria RAM de la terminal.

**Hecho:**
- Se refactorizó `biblioteca/cuadernillo-alias-absolutos.md` eliminando el historial de consola residual.
- Se inyectaron metadatos estructurales (YAML Frontmatter) y se consolidó el contenido bajo el formato de 5 átomos (Contexto, Hecho, Detalle técnico, Motivo, Fuentes).
- Se añadió la nota de depuración sobre purga de RAM mediante `unalias`.

**Motivo / criterio:** Estandarización de la información. Para que el futuro orquestador de publicación (Fase 7.1) automatice la maquetación a HTML/PDF sin fricción, los archivos Markdown deben poseer una estructura de metadatos estricta y predecible.

**Siguiente paso o deuda:** Diseñar e implementar el script maestro de publicación automatizada (`merci-publish.py`).

### 2026-04-24 — Fix: Exclusión de enlace simbólico del CMS en control de versiones

**Contexto:** El enlace simbólico `public/blog` (que conecta el núcleo estático con la instalación aislada de WordPress) corría el riesgo de ser rastreado por Git. Versionar un enlace simbólico que apunta a una ruta absoluta del sistema anfitrión rompe la portabilidad del proyecto al clonarlo en entornos con topologías diferentes.

**Hecho:**
- Se añadió `public/blog` al archivo `.gitignore`.
- Se definió la ejecución de `git rm --cached public/blog` para eliminar el rastro del índice de Git sin destruir el enlace físico en el servidor local.

**Motivo / criterio:** Portabilidad y aislamiento (Shift-Left). El código fuente debe ser universal y agnóstico a la infraestructura. Los enlaces simbólicos son configuraciones exclusivas del servidor (estado) y, al igual que la base de datos o el archivo `wp-config.php`, nunca deben viajar a través del control de versiones.

**Siguiente paso o deuda:** Ejecutar la limpieza del caché de Git, revisar el estado del árbol y realizar el commit de saneamiento mediante `merci-commit.py`.

### 2026-04-24 — Milestone: Bifurcación arquitectónica (Merci Boilerplate vs mercedev.es)

**Contexto:** Tras alcanzar la madurez técnica absoluta (100/100) y purgar la deuda técnica al cierre de la Fase 6, se determinó que las Fases 1-6 conforman un motor de infraestructura agnóstico (DevSecOps, SASS, CSP, Híbrido WP), mientras que la Fase 7 (publicación automatizada, biblioteca) contiene la lógica de negocio específica del proyecto.

**Hecho:**
- Se aprueba la bifurcación (Fork) del proyecto actual en dos entidades separadas.
- Se decide extraer el estado actual del código hacia un nuevo repositorio plantilla (`merci-boilerplate`) abstrayendo los datos personales.
- El repositorio actual (`PROYECTO_mercedev.es`) transiciona oficialmente para convertirse en el primer producto real derivado de dicha plantilla.

**Detalle técnico:** La extracción al nuevo Boilerplate implicará limpiar el `index.html` de textos específicos, establecer un logotipo neutral y sustituir las rutas absolutas por variables (`{{DOMINIO}}`). El repositorio actual mantendrá el historial completo de Git y avanzará hacia la Fase 7 asumiendo su rol de "instancia cliente".

**Motivo / criterio:** Principio de Separación de Responsabilidades (Separation of Concerns). Un *boilerplate* o *framework* no debe contener reglas de negocio ni contenido específico de una marca. Congelar el motor base ahora protege su reusabilidad para futuros proyectos, aislando el desarrollo de la Fase 7 exclusivamente en el producto final.

**Siguiente paso o deuda:** Ejecutar manualmente la copia y abstracción de la carpeta hacia el nuevo repositorio "Merci Boilerplate" e iniciar el diseño de la Fase 7 en el repositorio actual.

### 2026-04-24 — Refactor: Micro-optimización de SEO Técnico (JSON-LD Contextual)

**Contexto:** Una auditoría SEO de "hilado fino" detectó que el esquema JSON-LD inyectado dinámicamente marcaba todas las rutas de WordPress como `@type: WebSite` y usaba `home_url()` (que resuelve a `/blog`), lo cual generaba riesgo de fragmentación de la autoridad de dominio en los motores de búsqueda.

**Hecho:**
- Se refactorizó la matriz `$json_ld` dentro de la función `merci_inyectar_metadatos_seo` en `functions.php`.
- Se implementó condicionalidad semántica (`is_singular()`) para emitir `@type: Article` en páginas de lectura.
- Se forzó el uso de la raíz absoluta del dominio para el esquema `WebSite`.

**Detalle técnico:** Se extrajo la variable `$domain_root` usando la misma expresión regular (`preg_replace`) que en el enlazador de assets. Dependiendo del contexto de la vista, el JSON-LD ahora escupe los datos específicos del post actual (`get_permalink()`, `get_the_title()`) o los datos base del índice, cumpliendo con la especificación estricta de `schema.org`.

**Motivo / criterio:** Consultoría SEO Avanzada. Evitar la canibalización de entidades (que Google interprete `/blog` como un sitio web independiente a la portada). Etiquetar correctamente los posts como "Artículos" habilita la aparición en fragmentos enriquecidos (Rich Snippets).

**Siguiente paso o deuda:** Iniciar el diseño del flujo de la Fase 7.1 (Automatización de publicación).

### 2026-04-24 — Refactor: Auditoría arquitectónica externa y purga de deuda técnica

**Contexto:** Una auditoría externa de código mediante inteligencia artificial detectó cuatro deudas técnicas críticas en el ecosistema: un antipatrón de rendimiento en WordPress, uso de código heredado (legacy), inconsistencia SEO entre frontales y la violación del paradigma de programación orientada a objetos en JavaScript.

**Hecho:**
- Se modificó el hook de aprovisionamiento de base de datos de `init` a `after_switch_theme` en `functions.php`.
- Se eliminó la etiqueta `<title>` deprecada explícita en `index.php` y se activó `add_theme_support('title-tag')`.
- Se inyectó un bloque mínimo de metadatos estructurados (JSON-LD) en el ecosistema dinámico de WordPress.
- Se refactorizó `public/js/main.js` encapsulando la lógica procedimental en la clase `NavigationController`.

**Detalle técnico:** El hook `init` provocaba consultas inútiles a la base de datos en cada petición HTTP (N+1 query problem). La función `wp_title()` está deprecada desde WP 4.4; delegar el título al núcleo limpia el archivo HTML y cumple el estándar moderno. La refactorización a Vanilla JS con paradigma POO (Programación Orientada a Objetos) aísla el comportamiento del menú cumpliendo el Principio de Responsabilidad Única (SOLID).

**Motivo / criterio:** Prácticas estrictas de *Quality Assurance* (QA - Aseguramiento de Calidad) y validación cruzada. El código no solo debe funcionar, sino que debe alinearse perfectamente con la filosofía fundacional del proyecto (rendimiento, arquitectura y cero deuda técnica), sin admitir tolerancias al código "suficientemente bueno".

**Siguiente paso o deuda:** Ejecutar el orquestador de validación y comprometer el código para iniciar la Fase 7.1 (Automatización de publicación).

### 2026-04-23 — Fix: Actualización mayor de Pillow a 12.2.0 (Dependabot)

**Contexto:** Dependabot emitió nuevas alertas y forzó la actualización de su rama (pull request) indicando la necesidad de dar un salto mayor en la versión de `Pillow` hasta la `12.2.0` para mitigar vulnerabilidades encadenadas.

**Hecho:**
- Se actualizó la dependencia en `requirements.txt` de `Pillow==10.4.0` a `Pillow==12.2.0`.

**Detalle técnico:** El salto a una versión mayor (de 10.x a 12.x) incluye importantes parches de seguridad. Dado que `merci-optimizer.py` solo utiliza funciones estándar y consolidadas de apertura, redimensionado y guardado en WebP, la actualización se considera segura y no introduce alteraciones lógicas (*breaking changes*) en la automatización del proyecto.

**Motivo / criterio:** Mantenimiento proactivo y "Zero Trust". Las alertas de seguridad se persiguen hasta su erradicación total. Dar el salto a la última versión estable recomendada por GitHub blinda el entorno local y silencia el ruido operativo en el repositorio.

**Siguiente paso o deuda:** Realizar el push para cerrar definitivamente los hilos de Dependabot e iniciar el diseño del flujo de la Fase 7.

### 2026-04-23 — Fix: Actualización crítica de Pillow a 10.4.0 (Dependabot)

**Contexto:** Tras el último `git push`, GitHub Dependabot reportó dos nuevas vulnerabilidades de severidad alta. Dado que `requirements.txt` solo contiene la dependencia `Pillow`, se deduce que la versión 10.3.0 seguía expuesta a CVEs recientes.

**Hecho:**
- Se actualizó la dependencia en `requirements.txt` de `Pillow==10.3.0` a `Pillow==10.4.0`.
- Se revisó la integridad y sincronización de toda la documentación del directorio `docs/` y el `README.md` confirmando el cierre inmaculado de la Fase 6.

**Detalle técnico:** Las vulnerabilidades descubiertas en procesamiento de imágenes en las versiones anteriores a la 10.4.0 de Pillow pueden permitir ataques o denegación de servicio. Fijar la versión a `10.4.0` parchea estos vectores. La documentación arquitectónica (`docs/`) ha sido validada y refleja el estado exacto de producción (incluyendo el hash CSP y el enrutamiento).

**Motivo / criterio:** La seguridad perimetral no es negociable. En DevSecOps, mantener las dependencias de Python actualizadas es obligatorio, incluso si el script que las usa (`merci-optimizer.py`) se ejecuta únicamente en el entorno local.

**Siguiente paso o deuda:** Desplegar el cambio y comenzar el diseño del script de publicación automatizada (Fase 7.1).

### 2026-04-23 — Fix: Resolución de vulnerabilidad (Dependabot) y sincronización documental

**Contexto:** Al realizar el `git push` de cierre de la Fase 6, GitHub Dependabot reportó una vulnerabilidad de severidad alta (CVE) en las dependencias del proyecto. Además, era necesario alinear los manuales de despliegue (`docs/`) con las últimas configuraciones de seguridad en Nginx (CSP, HSTS) antes de avanzar a la Fase 7.

**Hecho:**
- Se identificó que la librería `Pillow` anclada en `requirements.txt` poseía una vulnerabilidad conocida, por lo que se actualizó a la versión segura `10.3.0`.
- Se actualizaron los manuales `docs/deployment-playbook.md` y `docs/integracion-wordpress.md` para incluir el bloque de Hardening de cabeceras HTTP inyectado en CloudPanel.

**Detalle técnico:** En arquitecturas DevSecOps, las dependencias de Python (utilizadas por `merci-optimizer.py`) deben ser auditadas continuamente. Actualizar la versión estricta en `requirements.txt` soluciona la alerta de GitHub manteniendo la reproducibilidad. Por otro lado, la documentación arquitectónica se sincronizó para reflejar la inyección de la cabecera `Content-Security-Policy` con el *whitelist* criptográfico (Hash SHA-256) y el `preload` de HSTS en el VHost del puerto 8080.

**Motivo / criterio:** Tolerancia cero frente a deuda técnica y brechas de seguridad. Una vulnerabilidad "High", aunque afecte solo al entorno local de automatización, rompe la confianza en el repositorio. Mantener la documentación sincronizada con la realidad del servidor garantiza la reproducibilidad (Infrastructure as Code).

**Siguiente paso o deuda:** Iniciar la Fase 7: Automatización y Clasificación.

---

## Cuando pases esto a la biblioteca

1. **Releer** entradas y quitar ruido (intentos fallidos, datos personales, tokens aunque sean falsos).
2. **Partir por tema:** por ejemplo una ficha “Sistema Merci — auditoría pre-commit” vs “Estructura del repositorio”.
3. **Añadir los tres átomos** donde haya una decisión difícil o un incidente (síntoma, solución, lección o deuda).
4. **Enlazar** al código estable (rutas a `scripts/merci/`, no copiar bloques enormes en la biblioteca salvo que aporten lectura autónoma).

---

*Última revisión de la bitácora: 2026-04-27.*
