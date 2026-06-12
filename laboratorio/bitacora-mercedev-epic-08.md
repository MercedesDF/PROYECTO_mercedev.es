# Bitácora del proyecto mercedev.es — Épica 8: Refactorización y Buenas Prácticas

## Para qué sirve este archivo
Bitácora activa para registrar las decisiones, refactorizaciones y limpiezas de código correspondientes a la Épica 8 del Roadmap maestro (Refactorización, mejora y revisión de buenas prácticas de los scripts).

---

## Registro cronológico

### 2026-06-12 — Refactor/QA: PEP 8, tipado, docstrings e higiene de imports en merci-init.py

**Contexto:** (Desafío) El inicializador del Boilerplate `merci-init.py` contenía importaciones internas prohibidas por la regla 16 de `instrucciones.md` (importación de `time` en medio del cuerpo de una función) y carecía de una declaración ordenada de imports, anotaciones de tipo estático y docstrings estructurados según las directrices del proyecto. Asimismo, errores imprevistos de I/O en la purga de directorios podían lanzar volcados de pila sin una salida controlada.

**Hecho:** (Maniobra)
- Se movió la importación del módulo `time` de la función `main()` al bloque superior del archivo y se ordenaron alfabéticamente todas las importaciones de la biblioteca estándar de Python.
- Se inyectó tipado estático a las firmas de todas las funciones (ej. `list[str] | None`, `bool`, `Path`, `None`).
- Se ampliaron y estructuraron los docstrings explicativos (*QUÉ HACE* y *POR QUÉ*) para las funciones que carecían de ellos (`configure_ai_module()`, `main()`).
- Se introdujo un capturador genérico de excepciones `except Exception as e` en el bloque de inicio de la aplicación para reportar de forma legible fallos destructivos (como permisos de escritura en la purga de carpetas) antes de salir con código `1`.
- Se validó la sintaxis del script mediante compilación estática y auditoría local sin detectar incidencias bloqueantes.

**Motivo / criterio:** (Aprendizaje) *Higiene PEP 8 y Prevención de Colapsos Silentes*. Evitar importaciones en caliente reduce el riesgo de errores de importación en tiempo de ejecución. El control elegante de excepciones al final de la aplicación previene la exposición de tracebacks innecesarios durante fallos operativos de I/O.

**Siguiente paso o deuda:** Continuar con la refactorización de `merci-completo.py` (el orquestador supremo DevSecOps) en la Fase 1 de la Épica 8.

### 2026-06-12 — Refactor/QA: Tipado, docstrings y robustez en merci-commit.py

**Contexto:** (Desafío) El script de commits atómicos `merci-commit.py` carecía de anotaciones de tipo estático y docstrings estructurados bajo la metodología del proyecto. Además, las llamadas a Git para comprobar cambios podían arrojar tracebacks no controlados si `git` no estaba disponible en el sistema.

**Hecho:** (Maniobra)
- Se clasificaron y ordenaron alfabéticamente las importaciones de la biblioteca estándar de Python conforme a PEP 8.
- Se inyectaron anotaciones de tipo estático (parámetros y retornos como `list[Path]`, `bool`, `tuple[str, str, str]` y `Path | None`) en todas las funciones.
- Se agregaron docstrings descriptivos con estructura de *QUÉ HACE* y *POR QUÉ*.
- Se robusteció `check_repo_changes()` envolviendo la llamada a Git en un bloque `try...except` para devolver `False` con seguridad en caso de fallos del subproceso o ausencia de ejecutable.
- Se añadió un manejador `except Exception as e` genérico al final de `main()` para interceptar y notificar de forma limpia fallos del sistema sin mostrar trazas de error.
- Se depuró un bloque de ejecución principal (`__main__`) duplicado al final del archivo.

**Motivo / criterio:** (Aprendizaje) *Especificación como Fuente y Resiliencia en Scripts*. Alinear el tipado y documentar sistemáticamente la intención de las rutinas de Git previene fallos silenciosos de integración y facilita la validación estática de tipos en pre-commit.

**Siguiente paso o deuda:** Continuar con la refactorización de `merci-init.py` (instanciador de repositorios) dentro de la Fase 1 de la Épica 8.

### 2026-06-12 — Refactor/QA: Control de excepciones y PEP 8 en merci-total.py

**Contexto:** (Desafío) El script orquestador `merci-total.py` carecía de control de excepciones genéricas al lanzar subprocesos, lo que podía provocar volcados de pila crudos (tracebacks) en la terminal si ocurrían errores de sistema (como fallos de permisos o archivos no ejecutables), vulnerando la regla de "Fail Gracefully". Además, no contaba con tipado ni docstring estructurado en la función principal.

**Hecho:** (Maniobra)
- Se reordenaron las importaciones del orquestador alfabéticamente siguiendo la guía de estilo PEP 8.
- Se añadió tipado de retorno `-> None` y un docstring explicativo estructurado (*QUÉ HACE* y *POR QUÉ*) a la función `main()`.
- Se introdujo un bloque de captura `except Exception as e` en el bucle de ejecución de subprocesos para atrapar fallos inesperados de infraestructura (ej. `OSError`, `PermissionError`) y salir limpiamente con código `1` y un mensaje inteligible en lugar de un traceback crudo.
- Se verificó la sintaxis del script compilándolo y se ejecutó la auditoría local confirmando la ausencia de hallazgos bloqueantes.

**Motivo / criterio:** (Aprendizaje) *Higiene y Robustez DevSecOps*. Todo script de automatización en un pipeline debe comportarse como un binario de calidad de software, proporcionando salidas limpias ante cualquier error de sistema para preservar la DX (Developer Experience) y alinearse con las pautas de estilo.

**Siguiente paso o deuda:** Continuar con la refactorización y revisión de buenas prácticas del resto de scripts de la Fase 1 de la Épica 8, tales como `merci-commit.py` o `merci-init.py`.

### 2026-06-08 — Feat/Arch: Enrutamiento dinámico y Modo In-Place en merci-styles.py

**Contexto:** (Desafío) El compilador de SASS (`merci-styles.py`) dependía de las rutas rígidas de la matriz (`src/scss/main.scss` a `public/css/main.css`), impidiendo compilar hojas de estilo en repositorios de clientes externos.

**Hecho:** (Maniobra)
- Se refactorizó `scripts/merci/merci-styles.py` introduciendo el enrutamiento dinámico con `os.getcwd()` y la bandera `IS_EXTERNAL`.
- En Modo Externo, el script escanea el directorio objetivo buscando el primer `main.scss` o `style.scss` disponible, y lo compila "in-place" depositando el archivo `.css` resultante en el mismo directorio.
- El binario pesado de Dart Sass se sigue descargando y aislando en la matriz (`scripts/merci/bin`), protegiendo el entorno del cliente.

**Motivo / criterio:** (Aprendizaje) *Compilación Standalone Zero-Bloat*. Separar el motor de compilación del código fuente permite utilizar herramientas locales pesadas para procesar código ajeno sin contaminar su infraestructura. El cliente obtiene un `.css` minificado impecable sin instalar ecosistemas completos de preprocesadores (Node.js/NPM).

**Siguiente paso o deuda:** Validar la compilación SASS en un proyecto externo.

### 2026-06-08 — Feat/Arch: Modo Externo en orquestador de commits (merci-commit.py)

**Contexto:** (Desafío) El script `merci-commit.py` dependía de la lectura obligatoria de la bitácora en la carpeta `laboratorio/` de la matriz, lo que impedía utilizarlo para empaquetar código y realizar *Conventional Commits* en repositorios de clientes o directorios externos de forma nativa.

**Hecho:** (Maniobra)
- Se refactorizó `scripts/merci/merci-commit.py` inyectando enrutamiento dinámico (`os.getcwd()`).
- Se introdujo el flag de contexto `IS_EXTERNAL`.
- Si se invoca en un repositorio ajeno, el orquestador desactiva la búsqueda de bitácoras del laboratorio y provee un prompt interactivo limpio para registrar un commit manual estandarizado, aplicando el empaquetado (`git add .`) directamente en la carpeta del cliente.

**Motivo / criterio:** (Aprendizaje) *Universalidad DevSecOps*. La disciplina de *Conventional Commits* y el empaquetado atómico no deben ser exclusivos del proyecto público. Dotar al orquestador de commits de capacidades externas permite estandarizar el historial de Git en cualquier auditoría o proyecto ajeno sin acoplarse a la estructura de archivos de la matriz.

**Siguiente paso o deuda:** Validar el commit en el entorno del cliente y proceder con la refactorización de `merci-styles.py`.

### 2026-06-08 — Arch/AI: Diseño de 'Context Bridge' (Puente de Conocimiento entre IAs)

**Contexto:** (Desafío) Las IAs de los entornos de desarrollo (como Gemini Code Assist) operan bajo el problema de "Ceguera de Área de Trabajo" (Workspace Siloing), limitándose a leer únicamente los archivos de la carpeta abierta. Esto impedía que el asistente del repositorio privado (`~/auditorias`) conociera el estado actualizado de las herramientas públicas del ecosistema matriz.

**Hecho:** (Maniobra)
- Se diseñó la arquitectura de un Contrato de Datos (Data Contract) mediante un puente físico.
- El repositorio público utilizará su carpeta `.privado/` para exportar un manifiesto (ej. `merci-capabilities.md`) con el listado actualizado de su arsenal.
- El repositorio comercial ejecutará un agente puente (`merci-bridge.py`) para ingerir este manifiesto en su propio espacio de trabajo, alimentando a su IA local.

**Motivo / criterio:** (Aprendizaje) *Inter-Process Communication para IAs y DLP*. Resolver la ceguera de contexto mediante un archivo de intercambio de texto unidireccional protege la barrera de fuga de datos (Data Leak Prevention) mientras dota a la IA privada de un mapa exacto de las capacidades públicas, permitiéndole sugerir herramientas transversales para auditar clientes.

**Siguiente paso o deuda:** Crear el agente puente en el repositorio comercial e integrarlo en las directrices.

### 2026-06-08 — Docs/QA: Sincronización de capacidades universales en manuales

**Contexto:** (Desafío) Tras dotar al optimizador de imágenes y al auditor de código de capacidades de enrutamiento dinámico y "Modo Externo", su descripción en los manuales públicos de la matriz quedó obsoleta (Deriva Documental), definiéndolos únicamente como herramientas locales.

**Hecho:** (Maniobra)
- Se actualizaron `README.md` e `instrucciones.md` para reflejar el "Modo Externo" agnóstico de `merci-audit.py` y el "Modo In-Place" recursivo de `merci-optimizer.py`.
- Se marcó la refactorización de `merci-audit.py` como completada en la Fase 1 de la Épica 8 en el `ROADMAP.md`.

**Motivo / criterio:** (Aprendizaje) *Single Source of Truth y Marketing de Autoridad*. Exponer públicamente que el ecosistema Merci contiene herramientas capaces de auditar y reparar de forma agnóstica proyectos ajenos eleva el prestigio del repositorio (DevRel). La documentación siempre debe estar alineada con el verdadero potencial de la arquitectura.

**Siguiente paso o deuda:** Iniciar la refactorización de `merci-styles.py` para otorgarle capacidades de compilación universal de SASS.

### 2026-06-08 — Docs/Gov: Mapeo de contexto cruzado para IAs (Cross-Context)

**Contexto:** (Desafío) Al dividir el ecosistema en un repositorio público (Boilerplate) y uno privado (Pro-Tools), la IA del repositorio público quedó "ciega" respecto a las herramientas de facturación, impidiendo que sugiriera sinergias o ideas de negocio.

**Hecho:** (Maniobra)
- Se inyectó la nueva sección "2.4. Ecosistema Comercial Privado (Pro-Tools)" en `instrucciones.md`.
- Se definió una "Interfaz de Conocimiento": el repositorio público no contiene el código privado, pero lista las "firmas" o capacidades de las herramientas comerciales (ej. `merci-webp-injector.py`).

**Motivo / criterio:** (Aprendizaje) *AI Cross-Pollination*. Las IAs operan aisladas por ventana/proyecto. Si queremos que el asistente arquitectónico (público) alimente de ideas al asistente hacker (privado), debemos proveerle un "mapa conceptual" de las armas disponibles en el otro lado del muro. Esto permite generar un ecosistema de ideas bidireccional sin comprometer la Prevención de Fuga de Datos (DLP).

**Siguiente paso o deuda:** Continuar con la refactorización de scripts como `merci-styles.py` para enrutamiento dinámico.

### 2026-06-08 — Feat/Security: Modo Auditoría Externa en merci-audit.py

**Contexto:** (Desafío) Se necesitaba escanear repositorios externos (clientes de auditoría) en busca de vulnerabilidades, pero aplicar el linter `merci-audit.py` en un proyecto no nativo (como un clon de WordPress) generaba miles de falsos positivos al violar las reglas estructurales del Boilerplate (uso de estilos y scripts en línea).

**Hecho:** (Maniobra)
- Se modificó el comportamiento por defecto del parámetro `--root` en `merci-audit.py` para usar el directorio de trabajo actual (`os.getcwd()`).
- Se implementó la validación contextual `is_external`.
- Si el script detecta que audita un directorio ajeno a su repositorio origen, silencia dinámicamente las reglas de purismo UI/UX (CSS/JS en línea, Assets externos) y se enfoca exclusivamente en reglas de seguridad DevSecOps y SEO (Exposición de secretos, funciones PHP peligrosas, `eval()` en JavaScript y metadatos vacíos).

**Motivo / criterio:** (Aprendizaje) *Universalidad y Reducción de Ruido*. Un auditor de seguridad es inútil si su salida (output) satura al ingeniero con ruido. Silenciar las aserciones de código "estéticas" al auditar un CMS ajeno convierte a este script en un escáner SAST (Static Application Security Testing) portátil, elevando su valor como herramienta pública sin sacrificar la rigurosidad en el propio proyecto matriz.

**Siguiente paso o deuda:** Lanzar la herramienta de auditoría desde la carpeta del cliente y buscar brechas de seguridad ocultas.

### 2026-06-08 — Docs/Arch: Estrategias de entrega WebP In-Place (Servidor vs Estático)

**Contexto:** (Desafío) Tras optimizar las imágenes de un WordPress ajeno "in-place" (junto a los originales), surgió el desafío de cómo forzar al frontend a consumir los nuevos archivos `.webp` sin romper la web original ni instalar plugins pesados.

**Hecho:** (Maniobra)
- Se documentaron y evaluaron dos vías de integración "Zero-Bloat" para clientes:
  1. **Vía Servidor (Nginx / Apache):** Uso de reescritura condicional (`try_files` / `mod_rewrite`) evaluando la cabecera `Accept: image/webp` para servir el archivo optimizado de forma transparente (Cero fricción HTML).
  2. **Vía Estática (Agente Python):** Creación de un script reemplazador propietario privado (`merci-webp-injector.py`) para auditorías estáticas, que busca y sustituye las extensiones de imagen en archivos HTML/CSS de volcados estáticos.

**Motivo / criterio:** (Aprendizaje) *Infrastructure Agnosticism*. Dependiendo de si se audita un servidor vivo (donde tocar el código o DB es peligroso) o un volcado HTML estático, la ingeniera DevSecOps debe contar con estrategias de inyección flexibles que no dependan de herramientas de terceros (plugins de WP) para demostrar el 100/100 de rendimiento.

**Siguiente paso o deuda:** Proveer el script de reemplazo estático en la carpeta privada `~/auditorias/` y aplicar las reglas de Nginx/Apache en los servidores de los clientes correspondientes.

### 2026-06-08 — Arch/Gov: Segregación de herramientas Pro y datos de clientes

**Contexto:** (Desafío) Al convertir los scripts locales en herramientas de auditoría universal para clientes externos, surgió la duda sobre dónde almacenar los scripts propietarios y los repositorios auditados para no exponer la ventaja competitiva (Propiedad Intelectual) ni vulnerar la privacidad de los clientes en el GitHub público de `mercedev.es`.

**Hecho:** (Maniobra)
- Se estableció la política de "Doble Repositorio" (Open-Core): herramientas base como `merci-optimizer.py` se mantienen públicas como demostración de autoridad técnica (DevRel), pero herramientas futuras de explotación, orquestación masiva o facturación se aislarán en un repositorio privado (ej. `merci-pro-tools`).
- Se determinó que los datos de clientes (clones de WordPress, volcados de DB) vivirán en un directorio físico completamente ajeno al árbol del proyecto (ej. `~/auditorias/`), nunca dentro del repositorio local para evitar riesgos críticos de fuga de datos.

**Motivo / criterio:** (Aprendizaje) *Data Leak Prevention Extremo y Modelos de Negocio*. Mezclar datos de clientes en una carpeta de un proyecto Open Source es un riesgo crítico (un fallo en `.gitignore` podría filtrar una web ajena). Retener scripts "Enterprise" protege el modelo de negocio, mientras que regalar la infraestructura base genera autoridad.

**Siguiente paso o deuda:** Establecer el directorio `~/auditorias` en el sistema anfitrión y continuar utilizando los alias globales de Zsh para invocar las herramientas públicas sobre estos directorios privados.

### 2026-06-08 — Test: Validación End-to-End de optimización recursiva "In-Place"

**Contexto:** (Desafío) Tras dotar a `merci-optimizer.py` de recursividad y agnosticismo de directorios, era imperativo certificar que la herramienta podía comprimir un repositorio ajeno real (un clon de WordPress) sin alterar su delicada arquitectura de carpetas.

**Hecho:** (Maniobra)
- Se ejecutó `merci optimizer` directamente sobre la carpeta `wp-content/uploads/` de una auditoría externa.
- El script procesó recursivamente subcarpetas y generó copias `.webp` ultraligeras de 20 imágenes (PNG y JPG) conservando exactamente la misma ubicación que sus originales.

**Motivo / criterio:** (Aprendizaje) *Empirical QA Assurance*. Comprobar con fuego real que el script respeta el patrón *In-Place* certifica su validez como herramienta de SRE y auditoría externa. La infraestructura de compresión ya no depende de la matriz `mercedev.es` para funcionar, alcanzando un grado de utilidad universal.

**Siguiente paso o deuda:** Proveer el mecanismo (mediante reescritura HTML o reglas de servidor Nginx/Apache) para que el frontend del proyecto externo consuma los nuevos archivos WebP en lugar de los pesados JPG/PNG originales.

### 2026-06-08 — Feat/Arch: Recursividad y Modo In-Place en merci-optimizer.py

**Contexto:** (Desafío) Al intentar auditar repositorios de terceros estructurados (como un `wp-content/uploads/`), el optimizador generaba la carpeta sesgada `assets/images/` y no encontraba archivos debido a que no buceaba recursivamente en las subcarpetas del año/mes de WordPress.

**Hecho:** (Maniobra)
- Se refactorizó `scripts/merci/merci-optimizer.py` reemplazando los métodos `.glob()` por `.rglob()` para habilitar la exploración recursiva infinita.
- Se introdujo la bandera de contexto `IS_EXTERNAL` en el motor lógico.
- Si se detecta un directorio externo (Caso 3), el orquestador ahora activa el modo "In-Place": omite la creación de la carpeta `assets/`, guarda las variantes WebP directamente junto a sus respectivos archivos originales en cualquier subcarpeta, y silencia la generación de tamaños responsivos extra para evitar contaminar ecosistemas ajenos.

**Motivo / criterio:** (Aprendizaje) *Agnosticismo Radical*. Eliminar los sesgos del Boilerplate (Boilerplate Bias) en los scripts utilitarios los convierte en verdaderas armas DevSecOps portátiles. Una herramienta de optimización debe ser capaz de entrar a cualquier laberinto de carpetas en cualquier CMS del mundo, optimizar de forma invisible, y salir sin romper la infraestructura que acaba de curar.

**Siguiente paso o deuda:** Ejecutar la auditoría en la carpeta de WordPress descargada para certificar la conversión "in-place" y continuar afinando los scripts SRE.

### 2026-06-08 — Fix/UX: Modo genérico para directorios externos en merci-optimizer.py

**Contexto:** (Desafío) Al intentar optimizar imágenes de un proyecto WordPress descargado directamente en su carpeta `wp-content/uploads/`, el orquestador seguía forzando la búsqueda de un subdirectorio `.assets-raw/`, devolviendo cero resultados.

**Hecho:** (Maniobra)
- Se refactorizó el motor de deducción de contexto en `scripts/merci/merci-optimizer.py`.
- Se implementó una lógica de 3 casos: si la ruta es `.assets-raw`, si es un proyecto tipo Merci (contiene el subdirectorio), o si es una carpeta genérica externa (se asume y escanea la carpeta directamente).

**Motivo / criterio:** (Aprendizaje) *Out-of-the-Box Experience y Fricción Cero*. Un script verdaderamente agnóstico no debe imponer la topología de su ecosistema nativo a repositorios externos. Si el usuario apunta a una carpeta de imágenes y no existe la estructura de Merci, el script debe ser inteligente y escanear el directorio en crudo sin exigir reestructuraciones manuales.

**Siguiente paso o deuda:** Validar la optimización de imágenes en el proyecto de WordPress externo.

### 2026-06-08 — Refactor: Enrutamiento dinámico en merci-optimizer.py

**Contexto:** (Desafío) El script de optimización de imágenes (`merci-optimizer.py`) estaba rígidamente acoplado a la raíz del proyecto matriz mediante `Path(__file__).resolve().parents[2]`. Esto impedía su ejecución nativa para optimizar activos multimedia en directorios de otros proyectos externos desde la misma terminal sin copiar el script físicamente.

**Hecho:** (Maniobra)
- Se refactorizó la resolución de la constante `REPO_ROOT` en `scripts/merci/merci-optimizer.py`.
- Se implementó la captura dinámica del directorio de trabajo mediante argumentos pasados por terminal (`sys.argv`) o como respaldo el directorio de trabajo actual (`os.getcwd()`).
- Se incluyó filtrado de banderas (`-v`, `--verbose`) para evitar colisiones en las rutas.
- Se actualizó la Fase 5 de la Épica 8 en el `ROADMAP.md`.

**Motivo / criterio:** (Aprendizaje) *Portabilidad y Standalone Compliance*. Un script utilitario de optimización de imágenes no debe estar acoplado a la topología de su repositorio origen si su función es puramente algorítmica y agnóstica. Dotarlo de enrutamiento dinámico lo convierte en una utilidad transversal, maximizando el Retorno de la Inversión (ROI) del código creado.

**Siguiente paso o deuda:** Evaluar la refactorización de otros scripts aislados (como `merci-styles.py` o `merci-audit.py`) para dotarlos de la misma portabilidad.

### 2026-05-31 — UI/UX: Eliminación de Hero compacto en el Blog

**Contexto:** Al navegar entre la portada, la biblioteca y el blog, se producía un salto visual molesto debido a que la cabecera del blog utilizaba un modificador de altura reducida (`.hero--compact`), rompiendo la consistencia de la interfaz.

**Hecho:** Se eliminó la lógica de inyección de la variable `$hero_modifier` en `src/wp-theme/merci-theme/index.php`, estandarizando el bloque a `<section class="hero">`.

**Motivo / criterio:** *Design Consistency y Pixel Perfect UI*. Todas las páginas principales del ecosistema deben compartir las mismas dimensiones de cabecera (`min-height: 40vh` con centrado Flexbox) para que la navegación entre la capa estática (SSG) y la dinámica (WP) se perciba unificada, fluida y sin saltos de contenido.

### 2026-05-31 — UX/Fix: Refinamiento de textos y corrección visual en índices SSG

**Contexto:** El índice autogenerado de la Biblioteca requería actualizar su *copy* para alinear la narrativa ("El conocimiento inmutable del ecosistema"). Además, se detectó un bug visual heredado: el generador estático usaba la variable incorrecta para el subtítulo y perdía el formato bicolor corporativo al intentar limpiar la etiqueta `<title>` para el SEO.

**Hecho:** Se refactorizó `scripts/merci/merci-publish.py` inyectando los nuevos textos (incluyendo la mención a "metodología Spec as Source"). Se separó la variable `title_html` de `titulo_seo` para preservar la clase `.hero__highlight` y se inyectó la variable `hero_subtitle_html` correctamente en el DOM de la cabecera.

**Motivo / criterio:** *Copywriting y Pixel Perfect UI*. Las páginas generadas dinámicamente por el motor SSG deben proyectar la misma madurez editorial y visual que las páginas estáticas. Separar el marcado HTML de la lógica SEO resuelve la deuda técnica visual sin penalizar a los rastreadores web.

### 2026-05-31 — UX/DevRel: Refinamiento del storytelling en "Sobre Mí"

**Contexto:** La introducción de la transición profesional en el currículum semántico sonaba poco natural y desconectada de la metáfora de la ingeniería civil ("aprendí a ejecutar cualquier proceso").

**Hecho:** Se reescribieron las dos primeras frases en `public/sobre-mi/index.html` para enfocar la narrativa en la proyección y construcción de infraestructuras físicas.

**Motivo / criterio:** *Storytelling Técnico y Coherencia*. Conectar explícitamente la creación de infraestructuras físicas con la metáfora de los "cimientos" de software aporta mucha más fuerza narrativa y naturalidad al texto.

### 2026-05-31 — UX/Fix: Corrección de copy sobre comandos de actualización (Boilerplate)

**Contexto:** La portada indicaba erróneamente que "un solo comando" generaba tanto el repositorio del Boilerplate como la demo pública (Showcase), cuando en realidad la arquitectura actual delega esta responsabilidad en dos orquestadores distintos (`merci release` y `merci showcase`).

**Hecho:** Se corrigió la frase en `public/index.html` cambiando "un solo comando" por "dos comandos".

**Motivo / criterio:** *Precisión Técnica*. En un proyecto donde la documentación es código (Spec as Source), el copy editorial y de marketing no puede contradecir la realidad operativa de la infraestructura local.

### 2026-05-31 — UX/DevRel: Refinamiento de Copywriting en Portada y Sobre mí

**Contexto:** La Épica 8 exige una revisión y mejora de los textos del ecosistema para alinearlos con el tono editorial definitivo, mejorando el "Storytelling Técnico" sin romper la UI.

**Hecho:** Se actualizaron los textos de `public/index.html` y `public/sobre-mi/index.html` conservando íntegramente la estructura HTML, las clases BEM y los Dashboards dinámicos de métricas.

**Detalle técnico:** Se eliminó la antigua sección "La Evolución" de la portada a favor del nuevo copy introductorio. En la página "Sobre Mí", se sustituyeron los apartados antiguos por los nuevos epígrafes (`La transición estructural`, `Cómo trabajo`, `Sobre Merci`), preservando el cuadro de mandos dinámico (`.hero__dashboard--standalone`).

**Motivo / criterio:** *Copywriting y Autoridad Técnica*. Los textos son parte integral de la interfaz (UI). Alinear la narrativa hacia el rigor de la ingeniería estructural consolida el mensaje y mejora radicalmente la percepción de madurez técnica del producto, justificando el trabajo de infraestructura subyacente.

### 2026-05-29 — Docs: Expansión del alcance en Refinamiento de Textos (Fase 6)

**Contexto:** Se detectó la necesidad de modificar y unificar los textos y el tono editorial no solo en la página principal, sino en el 100% de las vistas del ecosistema (Biblioteca, Tienda, Art de Coté, etc.).

**Hecho:** Se actualizó el `ROADMAP.md` (Épica 8, Fase 6) para ampliar explícitamente el alcance de la tarea "Revisión y mejora de los textos" a *todas* las páginas del ecosistema.

**Motivo / criterio:** *Consistency (Consistencia de Marca)*. Modificar los textos de la portada sin actualizar el resto de las páginas generaría una disonancia cognitiva y un tono editorial fragmentado. Agrupar toda la reescritura en la Fase 6 de la Épica 8 garantiza que se aborde como una tarea de *Copywriting* integral, sin mezclarla con las tareas de diseño puramente visuales de la Épica 7.

**Siguiente paso o deuda:** Mantener en pausa la Épica 8 para iniciar la Fase 3 de la Épica 7 (Integración Multimedia Avanzada).

### 2026-05-29 — UX/DevRel: Expansión global de "Merci Explica" y personalidad de la IA (Easter Eggs)

**Contexto:** El concepto "Merci Explica" (acompañado del icono 💡) nació inicialmente vinculado al Glosario Técnico, pero limitarlo a esa sección reducía su impacto. Era necesario expandir esta funcionalidad para que las traducciones a "lenguaje llano" y los apuntes de la asistente pudieran aparecer en cualquier parte de la web. Además, se buscaba dotar a Merci de una identidad propia, menos robótica y más cercana a la audiencia.

**Hecho:** 
- Se redefine el alcance de "Merci Explica": deja de ser exclusivo del Glosario Técnico para convertirse en un recurso transversal que puede inyectarse en cualquier página, artículo o sección de la web.
- Se aprobó conservar ciertas "alucinaciones" (idas de olla) divertidas generadas por la IA en sus explicaciones, oficializando una personalidad "picaresca y gamberra" para la asistente virtual.
- Se actualizaron las referencias en el Roadmap (Fase 6) asumiendo estas tareas como cumplidas bajo este nuevo paradigma global.

**Motivo / criterio:** *Gamificación y Accesibilidad Cognitiva*. Expandir las aclaraciones a toda la web derriba la barrera de entrada para perfiles no técnicos directamente durante la lectura. Mantener los "Easter Eggs" humorísticos de la IA rompe la monotonía corporativa y sirve como una trampa benigna para comprobar empíricamente si los reclutadores realmente leen la documentación técnica.

**Siguiente paso o deuda:** Mantener en pausa la Épica 8 para iniciar la Fase 3 de la Épica 7 (Integración Multimedia Avanzada).

### 2026-05-29 — UI/Bug: Registro de desbordamiento en bloques de código (Viewport y PDF)

**Contexto:** Se ha detectado que los fragmentos de código (`<pre>`, `<code>`) dentro de los cuadernillos de la Biblioteca no respetan los límites del contenedor, provocando un desbordamiento horizontal que ensancha el área de visualización (viewport) en dispositivos móviles y trunca el texto en las exportaciones a PDF (WeasyPrint).

**Hecho:** Se ha documentado la deuda técnica y se ha añadido la tarea de corrección al `ROADMAP.md` dentro de la Épica 8, Fase 6 (Refinamiento de Textos y Experiencia Documental).

**Motivo / criterio:** *Deferred Maintenance y Scope Creep Prevention*. Siguiendo la metodología Agile, los bugs visuales no críticos descubiertos mientras se trabaja en otra funcionalidad (WooCommerce) se deben registrar en el backlog para no interrumpir el estado de flujo de la épica actual. Resolver el CSS del código encaja perfectamente en la futura fase de refinamiento documental.

**Siguiente paso o deuda:** Mantener en pausa la Épica 8 y arrancar el diseño del carrito de WooCommerce en la Épica 7.

### 2026-05-29 — Arch/UI: Ideación de enlazado a Proyectos Satélite (Spin-offs)

**Contexto:** Tras idear futuros proyectos (Gemelo Digital, Merci CLI, Cerebro Local) que heredarán la metodología de `mercedev.es` pero vivirán en repositorios independientes, surge la necesidad de integrarlos visualmente en el ecosistema principal sin mezclar su documentación.

**Hecho:** Se añadió al `ROADMAP.md` (Épica 8, Fase 6) la planificación de una nueva sección en la portada para enlazar a "Proyectos Satélite" mediante tarjetas visuales.

**Motivo / criterio:** *Separation of Concerns y Ecosistema Expandido*. Mantener los repositorios separados protege la filosofía *Zero-Bloat* de cada producto. Enlazarlos desde la portada de `mercedev.es` centraliza el portfolio de la autora, convirtiendo la matriz en un "Hub" de proyectos interconectados sin contaminar la Biblioteca original.

**Siguiente paso o deuda:** Aparcar temporalmente la Épica 8 y arrancar con el diseño UI de WooCommerce (Fase 2, Épica 7).

### 2026-05-29 — Arch/Docs: Ideación de Validación Contextual para Deriva Documental (merci-drift)

**Contexto:** Surge la idea arquitectónica de mejorar la inteligencia del agente de deriva documental (`merci-drift.py`). Actualmente busca la presencia de scripts en los manuales maestros, pero en un futuro sería óptimo que cruzara la validación con los manuales específicos de la carpeta `docs/` según la categoría del script (ej. no tiene sentido que exija que `merci-audit.py` figure en un SOP de publicación).

**Hecho:** Se inyectó la tarea de investigación y posible refactorización de `merci-drift.py` en la Fase 2 de la Épica 8 dentro del `ROADMAP.md`.

**Motivo / criterio:** *Brainstorming y Trazabilidad*. Anotar las hipótesis de mejora en el Roadmap a medida que fluyen permite liberar carga cognitiva y asegura que no se pierdan. Cuando llegue el momento de abordar la Épica 8, se evaluará la viabilidad técnica: si mapear scripts por contexto añade una sobreingeniería excesiva, se descartará y se documentará el motivo como aprendizaje, manteniendo intacto el ciclo DevSecOps.

**Siguiente paso o deuda:** Aparcar temporalmente la Épica 8 y retomar las tareas visuales de la Fase 2 de la Épica 7 (Refinamiento de botones y contrastes WCAG de WooCommerce).

### 2026-05-28 — Docs: Planificación de Épica 8 (Refactorización global)

**Contexto:** Tras culminar la construcción táctica de la infraestructura, orquestación de Inteligencia Artificial y e-commerce, el ecosistema de scripts en Python ha crecido orgánicamente. Se hace necesario un ciclo intensivo de consolidación y limpieza para garantizar la máxima calidad del código base antes de considerarlo un producto final cerrado.

**Hecho:** Se formaliza la inclusión de la Épica 8 en el Roadmap maestro y se abre esta bitácora dedicada para documentar la depuración sistemática del ecosistema DevSecOps local.

**Detalle técnico:** La Épica 8 abordará la revisión de buenas prácticas (adherencia estricta a PEP 8), eliminación del patrón WET en favor de DRY cuando la arquitectura "Zero-Bloat" lo permita sin añadir dependencias bloqueantes, y la optimización de flujos en todos los scripts categorizados (Core Pipeline, IA & Gobernanza, Publishing, Seguridad).

**Motivo / criterio:** *Zero Technical Debt (Cero Deuda Técnica)*. Una vez que la funcionalidad de un ecosistema complejo está demostrada empíricamente, es una obligación arquitectónica volver sobre el código, refactorizarlo y pulirlo. Esto asegura que la plantilla distribuida (Boilerplate) no solo funcione, sino que sea un estándar de excelencia en ingeniería de software.

**Siguiente paso o deuda:** Iniciar la revisión sistemática de los scripts comenzando por la Fase 1 (Core Pipeline) en cuanto la Épica 7 alcance su cierre definitivo.

### 2026-05-28 — Docs: Ampliación de Épica 8 (UX Documental y Textos)

**Contexto:** Además de la refactorización de código, se ha identificado la necesidad de refinar el contenido y la forma de presentarlo. La Biblioteca contiene una alta densidad de información técnica que requiere ser más "digerible".

**Hecho:** Se añadió la "Fase 6: Refinamiento de Textos y Experiencia Documental" al Roadmap de la Épica 8.

**Motivo / criterio:** *Accesibilidad Cognitiva y DevRel*. De nada sirve un sistema avanzado si la documentación es impenetrable. Limpiar los anglicismos, enlazar al glosario, reestructurar visualmente la biblioteca y expandir las analogías ("Merci Explica") garantizará que el conocimiento técnico se transmita con claridad a cualquier lector.