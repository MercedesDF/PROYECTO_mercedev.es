# Bitácora del proyecto mercedev.es

## Para qué sirve este archivo

- **Yo futuro:** recuperar en minutos qué se decidió, por qué, y cómo se ejecutó algo técnico sin rebuscar en el chat o en commits sueltos.
- **Biblioteca (al cerrar el proyecto):** aquí vive el borrador narrativo y técnico; luego se depura y se traslada a `biblioteca/` como piezas definitivas (por estantería o tema), siguiendo la idea de “activo de conocimiento” del proyecto.

No sustituye a `instrucciones.md` (directrices y rol del asistente). Complementa el día a día con **hechos, comandos y lecciones**.

---

## Cómo mantenerlo (acuerdo simple)

1. **Añadir entradas al final** de la sección “Registro cronológico”, con la plantilla de abajo. El registro es **acumulativo**: lo ya escrito forma parte del historial y **no se reemplaza** por nuevas sesiones (así no se pierde contexto ni fechas).
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

### 2026-04-15 — Restauración integral de archivos y estabilización modular

**Contexto:** Pérdida de contenido en archivos tras renombrados y reorganización de carpetas.

**Hecho:**
- Reconstruir `public/robots.txt` y `public/sitemap.xml`.
- Restaurar `merci_ingestor.py` y el arnés de pruebas en `/tests`.
- Preservar el experimento de grabación en `/laboratorio/art-de-cote`.

**Detalle técnico:**
- Se asegura que los scripts utilicen nombres de archivo con guion bajo (`merci_sitemap.py`) para ser importables.
- Los archivos pesados de vídeo permanecen excluidos en `.gitignore`.

**Motivo / criterio:** Garantizar la integridad del repositorio antes de avanzar a la Fase 3.

**Siguiente paso o deuda:** Iniciar el desarrollo de estilos SASS.

### 2026-04-15 — Reorganización modular de la carpeta Merci

**Contexto:** Evitar la dispersión de archivos en la carpeta de automatización separando los scripts operativos de las pruebas y los experimentos.

**Hecho:**
- Creación de las subcarpetas `tests/` y `experimental/` en `scripts/merci/`.
- Reubicación de `test_sitemap.py` y el aviso de deprecación de `merci-recorder.py`.

**Detalle técnico:**
- Ajuste de `sys.path` en los tests para localizar módulos en el directorio padre (`parents[1]`).

**Motivo / criterio:** Modularidad y limpieza. Mantener la carpeta raíz de Merci enfocada únicamente en scripts productivos y validados.

**Siguiente paso o deuda:** Migrar futuros tests a la nueva carpeta y mover scripts en desarrollo a la zona experimental.

### 2026-04-15 — Preservación de Merci Recorder como pieza de Art de Coté

**Contexto:** Aplicación de la filosofía del proyecto para no descartar código experimental valioso tras el cambio de estrategia hacia el Ingestor.

**Hecho:**
- Trasladar la lógica funcional de grabación a `laboratorio/art-de-cote/recorder_experiment.py`.
- Mantener `scripts/merci/merci-recorder.py` como un stub de aviso (deprecación).

**Detalle técnico:**
- La lógica preservada incluye la corrección del flag `-nostdin` y el uso de `x11grab` (X Window System - Sistema de Ventanas X).
- Se categoriza como "Artefacto de Laboratorio" para consulta futura.

**Motivo / criterio:** El script falló para el flujo de producción diario pero es un activo de conocimiento sobre automatización multimedia con Python y FFmpeg.

**Siguiente paso o deuda:** Validar el funcionamiento del Ingestor en una sesión real.

### 2026-04-15 — Cambio de estrategia: Ingesta de evidencias en lugar de grabación directa

**Contexto:** El script `merci-recorder.py` no funcionaba correctamente y la necesidad de gestionar evidencias existentes (capturas de pantalla, vídeos) de forma más flexible.

**Hecho:**
- Deprecación de `scripts/merci/merci-recorder.py`.
- Creación de `scripts/merci/merci_ingestor.py` para escanear carpetas de usuario y mover archivos recientes a `.assets-raw/`.
- Actualización de `README.md` e `instrucciones.md` para reflejar la nueva estrategia.

**Detalle técnico:**
- `merci_ingestor.py` busca archivos modificados en los últimos 30 minutos en `~/Pictures`, `~/Videos`, `~/Desktop` (configurable).
- Ofrece al usuario la opción de mover todos, algunos o ninguno de los archivos encontrados a `.assets-raw/`.

**Motivo / criterio:** Priorizar la funcionalidad de ingesta de evidencias existentes, que es más robusta y menos propensa a problemas de entorno que la grabación en tiempo real, y alinear con la gestión de `.assets-raw/`.

**Siguiente paso o deuda:** Probar `merci_ingestor.py` con archivos de prueba y documentar su uso en el `README.md`.

### 2026-04-15 — Resolución definitiva para visualización de vídeos de evidencias

**Contexto:** Fallo persistente en la instalación de extensiones de vídeo en VS Code, incluso usando el CLI y IDs de extensiones válidos.

**Hecho:**
- Confirmar que la instalación de `b-ryan.vscode-video` vía CLI también falla.
- Decidir utilizar reproductores externos (sistema o navegador web) para visualizar los archivos `.mp4` de `laboratorio/evidencias/`.

**Detalle técnico:**
- El problema parece ser una limitación del entorno de VS Code o su acceso al Marketplace, no de la existencia de las extensiones.
- La visualización externa es una solución robusta que no bloquea el flujo de trabajo.

**Motivo / criterio:** Priorizar el avance del proyecto y la generación de evidencias sobre la resolución de un problema de configuración del IDE que consume tiempo.

**Siguiente paso o deuda:** Iniciar la grabación de 30 minutos y proceder con la Fase 3 (Ingeniería de Estilos).

### 2026-04-15 — Incidencia persistente con el Marketplace de VS Code

**Contexto:** No es posible localizar extensiones de vídeo por ID en el Marketplace de la instancia local de VS Code.

**Hecho:**
- Intentar instalación de `moshfeu.video-player` y `frenco.vs-code-media-preview` sin éxito.
- Proponer instalación vía **CLI** (Command Line Interface - Interfaz de Línea de Comandos) de la extensión `b-ryan.vscode-video`.

**Detalle técnico:**
- Comando de rescate: `code --install-extension b-ryan.vscode-video`.
- Alternativa de visualización: uso del navegador host para validar evidencias MP4 si falla el IDE.

**Motivo / criterio:** Evitar la dispersión en problemas de configuración del entorno y priorizar el avance hacia la Fase 3 del Roadmap.

**Siguiente paso o deuda:** Validar visualización de la primera sesión de 30 min y proceder con SASS.

### 2026-04-15 — Clarificación sobre la extensión de visualización de video

**Contexto:** Dificultad para localizar la extensión "Video Player" (`moshfeu.video-player`) en el Marketplace de VS Code.

**Hecho:**
- Reconfirmar la existencia y disponibilidad de la extensión.
- Proporcionar instrucciones precisas para la búsqueda por ID (`moshfeu.video-player`).

**Detalle técnico:**
- La búsqueda por ID es más robusta que por nombre, evitando ambigüedades o errores de tipografía.

**Motivo / criterio:** Asegurar que el desarrollador pueda instalar la herramienta necesaria para revisar las evidencias de video sin interrupciones.

**Siguiente paso o deuda:** Confirmar la instalación y reproducción de un video de prueba.

### 2026-04-15 — Corrección de herramienta: Extensión de visualización de video

**Contexto:** La extensión recomendada anteriormente (`frenco.vs-code-media-preview`) no se encuentra disponible en el Marketplace.

**Hecho:** Sustituir la recomendación por la extensión "Video Player" de moshfeu (`moshfeu.video-player`).

**Detalle técnico:**
- La nueva extensión permite la previsualización de archivos `.mp4` y `.webm` directamente en el **IDE** (Integrated Development Environment - Entorno de Desarrollo Integrado).

**Motivo / criterio:** Garantizar que el flujo de revisión de evidencias en el laboratorio sea funcional con herramientas existentes y verificadas.

**Siguiente paso o deuda:** Validar la apertura de un vídeo de sesión de 30 minutos con esta nueva extensión.

### 2026-04-15 — Instalación de extensión para visualización de evidencias

**Contexto:** Necesidad de revisar los vídeos generados por `merci-recorder.py` sin romper el flujo de trabajo saliendo del editor.

**Hecho:** Seleccionar e instalar la extensión Media Preview (`frenco.vs-code-media-preview`).

**Detalle técnico:**
- La extensión permite renderizar binarios de vídeo y audio en pestañas del **IDE** (Integrated Development Environment - Entorno de Desarrollo Integrado).

**Motivo / criterio:** Mantener la concentración en el entorno de desarrollo y facilitar la validación rápida de las capturas de pantalla antes de documentar en la bitácora.

**Siguiente paso o deuda:** Iniciar la grabación de 30 minutos y verificar la reproducción fluida dentro del editor.

### 2026-04-15 — Validación final y mejora de Merci Recorder

**Contexto:** Realizar prueba de humo del grabador y mejorar la flexibilidad para pruebas cortas.

**Hecho:**
- Añadir soporte para argumentos de duración en `merci-recorder.py`.
- Ejecutar prueba de 10 segundos exitosamente.

**Detalle técnico:**
- Uso de `argparse` para parametrizar la duración.
- Confirmación de que el flag `-nostdin` evita colisiones con la entrada de terminal.
- Validación de `.gitignore`: los binarios generados no son trackeados por Git.

**Motivo / criterio:** Robustez y facilidad de prueba sin sacrificar la configuración por defecto de 30 min.

### 2026-04-15 — Corrección de error interactivo en Merci Recorder

**Contexto:** `ffmpeg` reportó un "Parse error" durante la grabación, causado por entrada inesperada del usuario en la terminal.

**Hecho:**
- Identificar la causa del error como interacción accidental con el modo interactivo de `ffmpeg`.
- Modificar `scripts/merci/merci-recorder.py` para añadir el flag `-nostdin`.

**Detalle técnico:**
- El flag `-nostdin` evita que `ffmpeg` intente leer de la entrada estándar, previniendo errores de parseo por comandos no intencionados.

**Motivo / criterio:** Mejorar la robustez del script y la experiencia de usuario, evitando interrupciones por entradas accidentales.

**Siguiente paso o deuda:** Validar el comportamiento del script con el nuevo flag.

### 2026-04-15 — Prueba de humo y validación de Merci Recorder

**Contexto:** Verificar que el script de captura de pantalla funciona correctamente y que la exclusión en Git es efectiva.

**Hecho:**
- Ejecución de prueba de `scripts/merci/merci-recorder.py`.
- Verificación de salida en `laboratorio/evidencias/`.

**Detalle técnico:**
- El script genera el contenedor `.mp4` usando el códec `libx264`.
- `git status` confirma que los binarios de vídeo son ignorados por el sistema de control de versiones.

**Motivo / criterio:** Garantizar la trazabilidad visual de las sesiones de 30 min sin comprometer el peso del repositorio remoto.

### 2026-04-15 — Implementación de infraestructura de pruebas (QA)

**Contexto:** Ausencia de validación automatizada para los scripts de automatización de Merci.

**Hecho:**
- Creación de `scripts/merci/test_sitemap.py`.
- Definición de estrategia de pruebas unitarias usando la librería estándar de Python.

**Detalle técnico:**
- Uso de `unittest.mock` para simular el sistema de archivos y evitar escrituras reales durante los tests.
- Implementación de **TDD** (Test Driven Development - Desarrollo Dirigido por Pruebas) incipiente para los scripts de sistema.

**Motivo / criterio:** Garantizar la integridad de los metadatos de indexación y la estabilidad de las herramientas de automatización antes de avanzar a fases de diseño visual.

**Siguiente paso o deuda:** Ampliar la cobertura de pruebas a `merci-audit.py`.

### 2026-04-15 — Consolidación del flujo de grabación y protección de repositorio

**Contexto:** Asegurar que el nuevo sistema de grabación no impacte el tamaño del repositorio remoto.

**Hecho:**
- Actualizar `.gitignore` para excluir binarios de vídeo en `laboratorio/evidencias/`.
- Validar la integración de `merci-recorder.py` como herramienta de trazabilidad local.

**Detalle técnico:**
- Adición de patrones `*.mp4` y `*.mov` específicos para la carpeta de evidencias.

**Motivo / criterio:** Autonomía en la captura de evidencias sin gestión manual de archivos externos, respetando la Regla 10 de austeridad en el repo remoto.

**Siguiente paso o deuda:** Iniciar la primera sesión de grabación de 30 minutos para validar el rendimiento del sistema.

### 2026-04-15 — Implementación de sistema de captura de vídeo (Merci Recorder)

**Contexto:** Necesidad de registrar sesiones de desarrollo de 30 minutos para trazabilidad del proceso en el Laboratorio.

**Hecho:**
- Crear `scripts/merci/merci-recorder.py`.
- Integrar lógica de captura automática de pantalla con FFmpeg.

**Detalle técnico:**
- Uso de `x11grab` para la **GUI** (Graphical User Interface - Interfaz Gráfica de Usuario).
- Configuración de duración fija a 1800 segundos (30 minutos).
- Codificación en tiempo real optimizada para baja carga de **CPU** (Central Processing Unit - Unidad Central de Procesamiento).

**Motivo / criterio:** Facilitar la generación de evidencias sin interrumpir el flujo de trabajo manual, manteniendo la coherencia con la Regla 10 de gestión de archivos pesados.

**Siguiente paso o deuda:** Validar el peso de los archivos generados y ajustar el **CRF** (Constant Rate Factor - Factor de Tasa Constante) si superan los 50MB por sesión.

### 2026-04-15 — Política de gestión de evidencias pesadas en el Laboratorio

**Contexto:** Necesidad de evitar el crecimiento excesivo del repositorio Git por la inclusión de vídeos y capturas de pantalla de gran tamaño.

**Hecho:**
- Definir regla de exclusión de binarios pesados en `laboratorio/evidencias/`.
- Actualizar `instrucciones.md` con la norma de "Evidencias Pesadas".

**Detalle técnico:**
- Se establece que `merci-optimizer.py` (o extensiones futuras) se encargará de reducir el material de pruebas antes de su clasificación.
- Los archivos originales (brutos) se mantienen en la carpeta externa de capturas o en `.assets-raw/evidencias/` (fuera de Git).

**Motivo / criterio:** Mantener un repositorio ligero y profesional, evitando el bloqueo por cuotas de GitHub y asegurando clones rápidos.

**Siguiente paso o deuda:** Configurar `.gitignore` para excluir extensiones de vídeo (`.mp4`, `.mov`) dentro de la carpeta de evidencias.

### 2026-04-15 — Pruebas de visualización en navegador e hitos UX/UI (Fase 2)

**Contexto:** Validar el renderizado real del `index.html` tras la aplicación de la jerarquía semántica y la estructura BEM.

**Hecho:**
- Generar informes PDF con capturas del sitio en navegador.
- Crear carpeta `laboratorio/evidencias/` para organizar los artefactos de prueba.

**Detalle técnico:** (Aquí puedes anotar si detectaste algún error de alineación, fuentes o comportamiento responsivo en el PDF).

**Motivo / criterio:** Evitar la dispersión de archivos en la raíz del laboratorio y asegurar que las decisiones de diseño tienen un respaldo visual documentado.

**Siguiente paso o deuda:** (Anotar si hay que retocar algún margen o color tras ver el PDF).

### 2026-04-15 — Refactorización a Módulos SASS y Dart Sass Standalone (Fase 3)

**Contexto:** Se identificó que la librería Python `libsass` no soportaba las directivas modulares (`@use`, `@forward`, `_index.scss`) que permiten una arquitectura de estilos moderna y desacoplada.

**Hecho:**
- Reconfiguración de `src/scss/` incluyendo archivos `_index.scss` que reexportan las partes.
- `main.scss` simplificado a sólo incluir los índices de cada subcarpeta.
- Eliminación de `libsass` de `requirements.txt`.
- Modificación estructural de `scripts/merci/merci-styles.py`: ya no es un script de Python que importe librerías, sino un autómata que descarga la release oficial del binario _Dart Sass_ para Linux, extrae el compilador localmente sin impactar el sistema operativo host, y procesa los estilos.

**Detalle técnico:**
- Almacenaje de los binarios locales de SASS en `scripts/merci/bin/dart-sass/sass`.
- Se llama al proceso aisladamente con `subprocess` de la librería estándar de Python.

**Motivo / criterio:**
- Dar soporte al mejor estilo posible de escritura SASS modular pero evadir a toda costa la necesidad de forzar la instalación global de Node.js o NPM para usar un compilador web, protegiendo así el Paradigma base de "0 dependencias externas host".

**Siguiente paso o deuda:** Validar rendimiento continuo del compilador e iniciar implementación de hojas visuales para nuevos componentes.
### 2026-04-15 — Implementación de la Fase 3: SASS, BEM y Merci Optimizer

**Contexto:** Desplegar el sistema de estilos escalable (SASS) y preparar la automatización para multimedia.

**Hecho:**
- Creación de la arquitectura 7-1 en `src/scss/` con punto de entrada único (`main.scss`).
- Refactorización de `public/index.html` asimilando la metodología BEM.
- Creación de dos piezas fundamentales para Merci: `merci-styles.py` (compilador con libsass) y `merci-optimizer.py` (escalado WebP con Pillow).
- `requirements.txt` ajustado para compilar localmente con Python.

**Detalle técnico:**
- `merci-styles.py` invoca a libsass asilando su función y ahorrando uso manual de consola.
- `.assets-raw/` será escrutado por Merci procesando imágenes WebP hacia `assets/` a medidas predeterminadas.

**Motivo / criterio:** Se eligió `libsass` de Python para unificar el DevSecOps de Merci sin depender de un entorno NodeJS global adicional en Ubuntu, en línea con la filosofía de austeridad tecnológica externa.

**Siguiente paso o deuda:** Validar la instalación con pip y hacer un chequeo de `index.html` estéticamente en navegador.
### 2026-04-14 — Validación de jerarquía de encabezados y landmarks (Fase 2.1)

**Contexto:** Asegurar la accesibilidad y la estructura semántica correcta en la página de inicio.

**Hecho:**
- Añadir encabezado `<h2>` a la sección `#ecosistema` para evitar saltos de nivel.
- Incorporar `aria-label` al elemento `<nav>`.
- Actualizar hitos en `README.md`.

**Detalle técnico:**
- Se garantiza que el árbol de encabezados sea secuencial: `h1` > `h2` > `h3`.
- El uso de **Landmarks** (Puntos de referencia) facilita la navegación a usuarios con tecnologías de asistencia.

**Motivo / criterio:** Cumplir con los estándares de **WAI-ARIA** (Web Accessibility Initiative - Accessible Rich Internet Applications - Iniciativa de Accesibilidad Web - Aplicaciones de Internet Enriquecidas Accesibles) y SEO técnico.

**Siguiente paso o deuda:** Iniciar la Fase 3 (Ingeniería de Estilos).

### 2026-04-14 — Integración de merci-sitemap.py en el hook de pre-commit

**Contexto:** Automatizar la actualización de la fecha `<lastmod>` en `sitemap.xml` cada vez que se realicen cambios en la carpeta `public/`.

**Hecho:** Modificar `scripts/merci/pre-commit`.

**Detalle técnico:**
- Se añadió lógica para detectar archivos staged en `public/`.
- Si se detectan cambios, se ejecuta `python3 scripts/merci/merci-sitemap.py`.
- Se añade `public/sitemap.xml` al índice de Git (`git add public/sitemap.xml`) para incluir su modificación en el commit actual.

**Motivo / criterio:** Asegurar que `sitemap.xml` refleje siempre la fecha de la última modificación de contenido relevante, mejorando la precisión del SEO técnico.

**Siguiente paso o deuda:** Realizar un commit de prueba que incluya cambios en `public/` para validar el funcionamiento del hook.

### 2026-04-14 — Automatización de metadatos de indexación (Sitemap)

**Contexto:** Evitar la actualización manual de la fecha de última modificación en el sitemap.xml para mejorar el SEO técnico.

**Hecho:** Crear script `scripts/merci/merci-sitemap.py` para la gestión automática de fechas en archivos XML.

**Detalle técnico:**
- Uso de la librería `datetime` para obtener la fecha del sistema.
- Empleo de `re.sub` para manipular el contenido del XML sin necesidad de parsers pesados.

**Motivo / criterio:** Mantener la consistencia entre los cambios reales y lo que se informa a los motores de búsqueda de forma automatizada.

**Siguiente paso o deuda:** Integrar la ejecución de este script en el flujo de publicación o en un hook de post-commit.

### 2026-04-14 — Cierre de Fase 1 y creación de activos de indexación (Fase 2.3)

**Contexto:** Finalización formal de la infraestructura base y configuración de la visibilidad para buscadores del núcleo estático.

**Hecho:** 
- Actualizar `README.md` para reflejar la Fase 1 como completada.
- Crear `public/robots.txt` y `public/sitemap.xml`.

**Detalle técnico:** 
- `robots.txt`: Configurado para permitir el rastreo total y apuntar al mapa del sitio.
- `sitemap.xml`: Generado con la URL canónica raíz y prioridad máxima.

**Motivo / criterio:** Cumplir con los estándares de **SEO** (Search Engine Optimization - Optimización para Motores de Búsqueda) técnico definidos en el roadmap.

**Siguiente paso o deuda:** Validar la jerarquía de encabezados (Fase 2.1) para asegurar accesibilidad.

### 2026-04-14 — Validación de Fase 2 (HTML y SEO Técnico) con Merci Audit

**Contexto:** Verificación del primer documento semántico del núcleo estático frente a las reglas de auditoría.

**Hecho:** Ejecutar `merci-audit.py --strict-json-ld` sobre `public/index.html`.

**Detalle técnico:**
- El archivo cumple con los requisitos de metadatos, charset y lenguaje.
- Se valida el bloque JSON-LD (JavaScript Object Notation for Linked Data - Notación de Objetos JavaScript para Datos Enlazados) usando el esquema de `schema.org`.

**Motivo / criterio:** Garantizar que el sitio es indexable y cumple con los estándares de rendimiento y SEO (Search Engine Optimization - Optimización para Motores de Búsqueda) desde la primera línea de código.

**Siguiente paso o deuda:** Implementar navegación (Fase 2.1) y generar `robots.txt` / `sitemap.xml` (Fase 2.3).

### 2026-04-14 — Creación de proyecto y obtención de API Key vía AI Studio

**Contexto:** El error 404 inicial no era solo de configuración de software, sino de falta de infraestructura (proyecto) en el lado de Google.

**Hecho:** Generar una API Key a través de Google AI Studio vinculada a un proyecto nuevo creado automáticamente por la plataforma.

**Detalle técnico:** 
- Acceso a `aistudio.google.com`.
- Uso de la opción "Create API key in new project" para evitar la configuración manual en GCP (Google Cloud Platform - Plataforma en la Nube de Google) Console.

**Motivo / criterio:** Vía más rápida para habilitar `gemini-1.5-pro` sin gestionar capas de facturación o cuotas complejas de Google Cloud de entrada.

**Siguiente paso o deuda:** Probar la conexión en Continue una vez la API Key esté activa y propagada.

### 2026-04-14 — Corrección de error 404 en Continue (Gemini 1.5 Pro)

**Contexto:** Fallo en la conexión con la API de Google al usar gemini-1.5-pro en Continue, con un error 404.

**Hecho:** Identificar que el `provider` en el archivo `/home/hildegahr/.continue/config.yaml` estaba configurado incorrectamente como `gemini`.

**Detalle técnico:** Modificar el `provider` de `gemini` a `google-generative-ai` para el modelo `gemini-1.5-pro` en la configuración de Continue.

**Motivo / criterio:** El `provider` `google-generative-ai` es el nombre correcto para interactuar con la API de Google Gemini a través de Continue.

**Siguiente paso o deuda:** Crear el proyecto en Google Cloud / AI Studio.

### 2026-04-12 — Fase 1: infraestructura, Merci Audit y primer commit

**Contexto:** Arranque del repositorio bajo las directrices de `instrucciones.md` (rendimiento, seguridad shift-left, pedagogía). Objetivo de la Fase 1: estructura de carpetas, script de auditoría local y base Git.

**Hecho:**

- Estructura aprobada en la raíz: `docs/`, `biblioteca/`, `laboratorio/`, `scripts/merci/`, `assets/`, `.assets-raw/` (las carpetas vacías se versionan con `.gitkeep` para que un `git clone` conserve el esqueleto).
- `scripts/merci/merci-audit.py`: auditoría con biblioteca estándar de Python (sin dependencias pip obligatorias en esta fase). Comprueba entre otras cosas patrones de secretos, sintaxis de `.py`, JSON, avisos en JS (`eval` / `new Function`) y reglas SEO mínimas en `.html` / `.htm`.
- `scripts/merci/pre-commit`: shell que ejecuta `merci-audit.py --git-staged` (solo lo que va al commit).
- Enlace local de Git: `.git/hooks/pre-commit` → `../../scripts/merci/pre-commit` (los hooks no viajan con el clone; hay que recrear el enlace en cada máquina o documentar un bootstrap).
- `.gitignore` para `.venv/`, cachés y artefactos de build; `requirements.txt` reservado para fases posteriores (p. ej. Pillow en optimizador).
- Commit inicial en rama `main` con mensaje tipo *chore: commit inicial — Fase 1 (estructura, Merci Audit, directrices)*.

**Detalle técnico:**

- Auditoría sobre todo el árbol: `python3 scripts/merci/merci-audit.py`
- Solo índice (staged), pensado para hook: `python3 scripts/merci/merci-audit.py --git-staged`
- Exigir JSON-LD en HTML cuando toque endurecer CI: flag `--strict-json-ld`
- Instalar hook (desde la raíz del repo): `chmod +x scripts/merci/pre-commit scripts/merci/merci-audit.py` y `ln -sf ../../scripts/merci/pre-commit .git/hooks/pre-commit`
- Saltar el hook solo si es deliberado: `git commit --no-verify`

**Motivo / criterio:** Automatizar comprobaciones antes de integrar cambios encaja con “seguridad shift-left” y con el papel de `merci-audit.py` descrito en instrucciones. Staged-only evita auditar el mundo en cada commit y acelera el flujo.

**Siguiente paso o deuda:** Fase 2 — HTML semántico, JSON-LD e indexación; primer documento público o plantilla que pase el audit sin `--no-verify`.

### 2026-04-12 — Registro cronológico acumulativo (no sustituir historial)

**Contexto:** Asegurar que la bitácora no pierda contexto al añadir sesiones nuevas.

**Hecho:** En `instrucciones.md` (regla 6) y en «Cómo mantenerlo» de este archivo quedó explícito: nuevas entradas **solo al final** del registro; no reemplazar ni borrar bloques ya escritos salvo corrección puntual o retirada de datos sensibles, con motivo claro.

**Detalle técnico:** N/A.

**Motivo / criterio:** El historial del laboratorio es activo de trazabilidad; sobrescribirlo rompería la línea temporal para el «yo futuro» y para el traslado a `biblioteca/`.

**Siguiente paso o deuda:** Seguir añadiendo entradas bajo «Registro cronológico» sin editar entradas previas salvo las excepciones acordadas.

### 2026-04-12 — `.assets-raw`: solo local, sin originales en Git

**Contexto:** Evitar que PSD, RAW, vídeos u otros brutos acaben en GitHub.

**Hecho:** `.gitignore` pasa a ignorar `.assets-raw/*` con excepción de `.assets-raw/.gitkeep`. `instrucciones.md` y `README.md` describen que la carpeta es convención de trabajo local y que lo versionado en `/assets` es lo optimizado.

**Detalle técnico:** Patrón en `.gitignore`: `!.assets-raw/.gitkeep` tras `.assets-raw/*`.

**Motivo / criterio:** Repositorio ligero y reproducible; los originales viven fuera del remoto (disco, NAS, etc.).

**Siguiente paso o deuda:** En Fase 3, documentar el flujo concreto `merci-optimizer.py` de `.assets-raw` → `assets/`.

### 2026-04-12 — Documentación pública sin notas personales al mantenedor

**Contexto:** Evitar frases tipo “cuando lo tengas claro añade LICENSE” en el README u otros textos versionados para GitHub.

**Hecho:** `README.md` (Licencia y otras frases) redactado en tono neutro. Nueva regla 7 en `instrucciones.md`: recordatorios al autor fuera del repo; en Git, texto útil para visitantes o colaboradores.

**Detalle técnico:** N/A.

**Motivo / criterio:** El remoto es documentación de producto/proyecto, no la libreta personal.

**Siguiente paso o deuda:** Revisar futuros `docs/` públicos con el mismo criterio.

### 2026-04-12 — Fase 2: carpeta `public/` como raíz del documento

**Contexto:** Inicio de la Fase 2 por la estructura antes del primer HTML.

**Hecho:** Directorio `public/` en el repo con `.gitkeep`; entrada en §3 de `instrucciones.md` y fila en `README.md`. Convención: aquí vive el núcleo estático servido como documento raíz; WP fuera hasta Fase 4.

**Detalle técnico:** Nombre elegido: `public/` (convención habitual de “document root” en despliegues estáticos).

**Motivo / criterio:** Separar claramente sitio servido, automatización, conocimiento y brutos locales.

**Siguiente paso o deuda:** `public/index.html` semántico + JSON-LD + `robots.txt` / `sitemap.xml` en la misma raíz cuando toque.

---

### 2026-04-15 — Refactorización para resolver descoordinación de archivos

**Contexto:** Conflicto de convenciones de nombres y pérdida de coordinación de los scripts locales (`merci_sitemap.py` vs `merci-sitemap.py`) y pérdida de la compilación CSS (`main.scss`).

**Hecho:**
- Restaurar explícitamente `@use 'index';` en `src/scss/main.scss` garantizando compilación exitosa a `public/css/main.css`.
- Traspasar duplicidades experimentales (`merci_ingestor.py`, `merci_sitemap.py`, `pre-commit.sh`) a `laboratorio/scripts_temporales/` para mantener limpio el entorno y respetar la no eliminación de código.
- Restaurar el script `scripts/merci/pre-commit` con la llamada correcta a `merci-sitemap.py`.
- Actualizar el `README.md` para asentar todos los apuntes con las rutas veraces.

**Detalle técnico:**
- Se confirma visualmente la reaparición de `main.css`.
- Se limpia la carpeta `scripts/merci/` manteniéndola con `-` en lugar de `_` como convención primaria.
- Movimiento realizado: `mv scripts/merci/merci_ingestor.py scripts/merci/merci_sitemap.py scripts/merci/pre-commit.sh laboratorio/scripts_temporales/`

**Motivo / criterio:** Consistencia y correspondencia con "lo que existe". Todo el proyecto ya está nuevamente compilando y acoplado.

**Siguiente paso o deuda:** Ninguno, el lío de archivos quedó resuelto.

---

## Cuando pases esto a la biblioteca

1. **Releer** entradas y quitar ruido (intentos fallidos, datos personales, tokens aunque sean falsos).
2. **Partir por tema:** por ejemplo una ficha “Sistema Merci — auditoría pre-commit” vs “Estructura del repositorio”.
3. **Añadir los tres átomos** donde haya una decisión difícil o un incidente (síntoma, solución, lección o deuda).
4. **Enlazar** al código estable (rutas a `scripts/merci/`, no copiar bloques enormes en la biblioteca salvo que aporten lectura autónoma).

---

*Última revisión de la bitácora: 2026-04-14.*
