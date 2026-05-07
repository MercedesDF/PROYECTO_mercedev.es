# Bitácora del proyecto mercedev.es — Fase: Orquestación con IA

## Para qué sirve este archivo

Bitácora activa a partir del cierre arquitectónico fundacional (Fases 1–11, selladas el 2026-05-06).
Registra exclusivamente las decisiones, experimentos y aprendizajes del nuevo roadmap de Inteligencia Artificial y Orquestación (`ROADMAP-AI-ORQUESTACION-SELF-HEALING-SYSTEM.md`).

El historial anterior (Fases 1–11) vive íntegramente en `laboratorio/bitacora-mercedev.md`.
El archivo histórico archivado (2026-04-12 a 2026-04-23) está en `laboratorio/bitacora-mercedev-260412-260423.md`.

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

**Contexto:** (qué querías lograr o qué problema apareció)

**Hecho:** (lista breve: archivos, fases del roadmap, PR/commit si aplica)

**Detalle técnico:** (comandos, rutas, flags; solo lo que necesites recordar)

**Motivo / criterio:** (por qué esta opción y no otra)

**Siguiente paso o deuda:** (qué queda pendiente)
```

---

## Registro cronológico

### 2026-05-08 — Fix: Inyección de fecha dinámica en Agente Bibliotecario y Promoción

**Contexto:** Los cuadernillos generados por la IA mantenían la fecha literal `AAAA-MM-DD` porque el modelo local no tenía conciencia temporal, y el asistente de promoción (`merci-promote.py`) conservaba ese *placeholder* asumiéndolo como valor válido.

**Hecho:**
- Se refactorizó `scripts/merci/merci-promote.py` para detectar y sobrescribir el placeholder `AAAA-MM-DD` con la fecha actual.
- Se inyectó `datetime.now()` en el prompt dinámico de `scripts/merci/merci-librarian.py`.
- Se actualizó `prompt-bibliotecario.md` para exigir el uso de la fecha inyectada.

**Motivo / criterio:** *Context Awareness*. Los LLM locales no tienen reloj interno. Proveer la fecha como contexto dinámico en tiempo de ejecución (Run-time) y asegurar que el orquestador de promoción sepa sanitizar *placeholders* cierra la brecha de automatización temporal.

**Siguiente paso o deuda:** Validar la automatización de *Single Source of Truth* (SSOT) para el `README.md` (Siguiente hito de la Fase 3).

### 2026-05-08 — Docs: Creación del prompt maestro para el Agente Bibliotecario

**Contexto:** Antes de programar la lógica del agente en Python, era necesario asentar las reglas editoriales y de formato que domarán a la IA local para que convierta notas crudas en "Cuadernillos" listos para la biblioteca.

**Hecho:** Se redactó el archivo `/laboratorio/prompts/prompt-bibliotecario.md`.

**Detalle técnico:** El prompt exige *Zero-Shot formatting* (solo salida de código Markdown), inyecta la regla de los 3 átomos (Desafío, Maniobra, Aprendizaje) y fuerza campos fijos de Gobernanza como `estado: "borrador"` y el bloque HTML `<!-- linkedin: ... -->`.

**Motivo / criterio:** *Spec-Driven Development*. Diseñar primero el "molde mental" del agente asegura que las respuestas del LLM sean predecibles. Obligar al agente a pre-redactar el post de LinkedIn anidado en el documento prepara el terreno y agiliza el flujo de la automatización social.

**Siguiente paso o deuda:** Desarrollar el script de Python `merci-librarian.py` para procesar el directorio de notas e invocar este prompt vía LiteLLM.

### 2026-05-08 — Feat: Inicio de Fase 3 (El Agente Bibliotecario)

**Contexto:** Con el ecosistema "Self-Healing" operativo (Fase 2 sellada), el siguiente cuello de botella operativo es la redacción técnica. Se requiere reducir a cero la fricción de documentar, permitiendo que la autora vuelque notas en crudo y la IA las convierta en "Cuadernillos" inmaculados.

**Hecho:** Se inauguró la Fase 3 del Roadmap de IA y se comenzó el diseño arquitectónico del Agente Bibliotecario.

**Motivo / criterio:** *Docs-as-Code y Zero Friction*. Documentar consume energía cognitiva. Delegar la aplicación de la regla de los 3 átomos (Desafío, Maniobra, Aprendizaje) y la generación del YAML Frontmatter a un agente LLM local asegura que la biblioteca crezca constantemente manteniendo un estándar editorial perfecto.

**Siguiente paso o deuda:** Diseñar el script del Agente Bibliotecario (`merci-librarian.py`) y definir su prompt especializado.

### 2026-05-07 — Milestone: Cierre de Fase 2 (Auto-Healing System)

**Contexto:** Abordar el último hito de la Fase 2 creando un flujo de reparación automática en la nube (CI/CD) ante fallos del linter, aplicando la estrategia de *Hybrid Stack* diseñada en la Fase 1.

**Hecho:**
Se ejecutó el Protocolo Estricto de Cierre de Fase (Definition of Done):
- [x] **1. Deuda Técnica:** 0 TODOs. El patrón *Fail Gracefully* protege el pipeline; si falla la API o falta el token, los agentes se apagan sin romper la compilación base.
- [x] **2. Cosecha de Conocimiento:** Consolidado el framework mental de "Desafío, Maniobra y Código" para los prompts del sistema.
- [x] **3. Auditoría Documental:** Fase 2 marcada como completada en el Roadmap de IA.
- [x] **4. Evaluación de Release:** El ecosistema de agentes (Self-Healing y WebP Automation) justifica la elevación a la **Release v1.9.0** del Boilerplate.
- [x] **5. Snapshot:** Ejecutado backup local para respaldar el ecosistema con sus nuevas capacidades cognitivas.
- [x] **6. Sello Definitivo:** Commit atómico de cierre consolidado.

**Detalle técnico:** El agente en la nube invoca a `merci-audit.py` para interceptar el primer error bloqueante. Si lo encuentra, delega la reparación al modelo `gemini-1.5-flash` a través de LiteLLM. El workflow instala las dependencias de IA, expone el secreto `GEMINI_API_KEY`, ejecuta la reparación y hace un *auto-commit* de vuelta.

**Motivo / criterio:** *Self-Healing Cloud y Zero Latency Local*. Utilizar Ollama en local ahorra costes y asegura privacidad, pero los contenedores de GitHub Actions no pueden cargar modelos locales pesados. Usar la API de Gemini como modelo de contingencia (Fallback) en la nube demuestra la brillantez de haber utilizado LiteLLM como capa de abstracción universal (Agnosticismo de Modelos).

### 2026-05-07 — Feat: Agente Vigilante de Assets (WebP Automation)

**Contexto:** Eliminar la fricción de tener que ejecutar manualmente el optimizador de imágenes o esperar a correr el orquestador global cada vez que se añade material multimedia en bruto al proyecto.

**Hecho:** Se implementó `scripts/merci/merci-assets-watcher.py` y se marcó el hito *WebP Automation* en la Fase 2 del Roadmap de IA como completado.

**Detalle técnico:** El script actúa como un agente en segundo plano. Escanea `.assets-raw/` cada 2 segundos comparando el estado de modificación física (`st_mtime`). Al detectar diferencias, invoca automáticamente a `merci-optimizer.py`. Mantiene la política estricta de 0 dependencias externas.

**Motivo / criterio:** *Fricción Cero y Developer Experience (DX)*. Un ecosistema maduro no espera a que el humano recuerde optimizar las imágenes. El agente reacciona en tiempo real, garantizando que el desarrollador pueda centrarse en el contenido mientras el sistema se auto-regula visualmente.

**Siguiente paso o deuda:** Validar el agente copiando una imagen de prueba a `.assets-raw/` y proceder al cierre final de la Fase 2 (IA-Fix Workflow).

### 2026-05-07 — Milestone: El Agente Auditor (Self-Healing MVP) Operativo

**Contexto:** Validar empíricamente que la inyección de LiteLLM y Ollama en el orquestador de calidad (`merci-audit.py`) intercepta correctamente los errores de código y devuelve sugerencias de reparación contextualizadas respetando el *System Prompt*.

**Hecho:**
- Se ejecutó `merci audit` provocando un error sintáctico (`PY_SYNTAX`) deliberado.
- El Agente analizó el fragmento y escupió en consola una maniobra de corrección estructurada (Desafío, Maniobra, Código).
- Se marcó el primer hito de la Fase 2 en el `ROADMAP-AI-ORQUESTACION-SELF-HEALING-SYSTEM.md` como completado.

**Detalle técnico:** El patrón *Fail Gracefully* funcionó a la perfección. La IA operó sobre un entorno aislado (`.venv`) consultando el modelo local `phi3` en `localhost:11434`, manteniendo una fricción nula en el pipeline maestro y respetando la filosofía DevSecOps.

**Motivo / criterio:** *Self-Healing Base*. Un orquestador que propone la solución exacta en la misma terminal donde reporta el error reduce drásticamente el tiempo de depuración (Developer Experience). Esto sella la base de la Fase 2.

**Siguiente paso o deuda:** Abordar el siguiente agente del Roadmap (IA-Fix Workflow o WebP Automation).

### 2026-05-07 — Fix: El Agente Auditor estaba ciego a los archivos Python

**Contexto:** Al ejecutar la prueba de validación del Agente Auditor con un archivo Python de sintaxis errónea (`falla_prueba.py`), el script no reportó ningún error, permaneciendo en silencio.

**Hecho:** Se diagnosticó un bug en `scripts/merci/merci-audit.py`. La lista de extensiones de archivo a escanear (`TEXT_SUFFIXES`) omitía la extensión `.py`.

**Detalle técnico:** El auditor solo aplicaba sus reglas de sintaxis Python a los archivos que pasaban el filtro de extensiones. Al no estar `.py` en la lista, el archivo de prueba era ignorado por completo durante el escaneo del repositorio. Se añadió `.py` al `frozenset` `TEXT_SUFFIXES`.

**Motivo / criterio:** *Regresión y QA sobre QA*. Un linter que no es capaz de ver los archivos que se supone que debe auditar es una herramienta inútil. Este tipo de regresiones silenciosas son las más peligrosas. La prueba de humo con un error provocado ha sido crucial para detectar esta ceguera.

**Siguiente paso o deuda:** Re-ejecutar la auditoría para confirmar que el Agente ahora sí detecta el error y sugiere la reparación.

### 2026-05-07 — Feat: Inicio de Fase 2 (El Agente Auditor)

**Contexto:** Con la infraestructura de la Fase 1 sellada y el Boilerplate v1.8.0 exportado, se requiere dotar al auditor maestro (`merci-audit.py`) de capacidades de Inteligencia Artificial local para sugerir correcciones en consola.

**Hecho:** Se inició el diseño arquitectónico para la inyección de `litellm` y la ingesta del `prompt-sistema-base.md` dentro de las funciones de reporte de errores del linter.

**Motivo / criterio:** *Self-Healing System y Fricción Cero*. Un orquestador que solo reporta errores aporta valor, pero un agente que analiza el fallo en contexto y propone la maniobra de reparación exacta reduce la fricción cognitiva a cero y acelera la iteración segura (Shift-Left).

**Siguiente paso o deuda:** Refactorizar `scripts/merci/merci-audit.py` implementando la conexión local con Ollama bajo un patrón de Degradación Elegante.

### 2026-05-07 — Fix: Degradación Elegante en extractor de métricas (Fail Gracefully)

**Contexto:** Al ejecutar la instanciación y prueba del Boilerplate (`merci total`), el orquestador se detuvo porque `merci-extract-metrics.py` exigía la librería `pypdf` con un error fatal (`sys.exit(1)`). Esto rompía la política de "0 dependencias bloqueantes".

**Hecho:** Se modificó `scripts/merci/merci-extract-metrics.py` para aplicar el patrón *Fail Gracefully*.

**Detalle técnico:** Si la librería no está instalada, el script ahora emite un mensaje informativo (`ℹ️ [Merci Info]`) y sale con `sys.exit(0)`, permitiendo que el pipeline maestro continúe con la ejecución de los siguientes scripts.

**Motivo / criterio:** *Out-of-the-Box Experience*. Una utilidad accesoria (como leer un PDF para actualizar el dashboard) no debe detener la cadena de compilación principal de un nuevo usuario que solo quiere levantar el proyecto base.

**Siguiente paso o deuda:** Reanudar la exportación del Boilerplate v1.8.0 y proceder con la inyección de IA en `merci-audit.py`.

### 2026-05-07 — Milestone: Cierre de Fase 1 (Cimientos y Conectividad IA)

**Contexto:** Aplicar el *Definition of Done* para la Fase 1 del Roadmap de IA, asegurando que la infraestructura base (Ollama + LiteLLM), los directorios estructurales y las reglas rectoras están consolidados antes de desarrollar el primer agente autónomo.

**Hecho:**
Se ejecutó el Protocolo Estricto de Cierre de Fase (Definition of Done):
- [x] **1. Deuda Técnica:** 0 TODOs. La conexión local de IA está validada y es 100% privada (telemetría apagada).
- [x] **2. Cosecha de Conocimiento:** Creado `prompt-sistema-base.md` con las reglas de arquitectura innegociables para futuros agentes.
- [x] **3. Auditoría Documental:** Hitos de la Fase 1 marcados como completados en `ROADMAP-AI-ORQUESTACION-SELF-HEALING-SYSTEM.md`.
- [x] **4. Evaluación de Release:** Los cambios en orquestadores (`merci-commit`, `merci-publish`, `merci-total`) justifican la nueva **Release v1.8.0** del Boilerplate.
- [x] **5. Snapshot:** Ejecutado backup local para asegurar el ecosistema inmaculado antes de inyectar IA en el núcleo.
- [x] **6. Sello Definitivo:** Commit atómico.

**Motivo / criterio:** *Governance y Definition of Done (DoD)*. Sellar formalmente la fase garantiza que la plataforma de orquestación es estable, privada (Zero Trust) y tiene límites arquitectónicos estrictos antes de inyectar capacidad generativa a los scripts del núcleo.

**Siguiente paso o deuda:** Iniciar la Fase 2 (El Agente Auditor), dotando a `merci-audit.py` de capacidades de sugerencia y reparación de código mediante IA.

### 2026-05-07 — Docs: Estandarización del Prompt Sistema Base para agentes IA

**Contexto:** Con el directorio de prompts creado, se requería asentar las "Instrucciones Base" (System Prompt) para asegurar que cualquier agente de IA (como el futuro Agente Auditor) respete la filosofía de cero dependencias y rendimiento extremo del proyecto.

**Hecho:**
- Se redactó `/laboratorio/prompts/prompt-sistema-base.md`.
- Se marcaron como completados los tres primeros hitos de la Fase 1 en el `ROADMAP-AI-ORQUESTACION-SELF-HEALING-SYSTEM.md`.

**Motivo / criterio:** *Governance AI*. Los LLMs tienden a alucinar soluciones usando frameworks populares (React, Tailwind). Inyectar un "Prompt de Sistema" estricto en cada llamada al modelo local actúa como un escudo arquitectónico, forzando a la IA a pensar y codificar exclusivamente bajo los paradigmas de Vanilla JS y Python puro.

**Siguiente paso o deuda:** Iniciar la Fase 2 (El Agente Auditor), dotando a `merci-audit.py` de capacidades de sugerencia de comandos de reparación.

### 2026-05-07 — Test: Validación exitosa del motor local (Ollama + LiteLLM)

**Contexto:** Validar empíricamente que el entorno Python (vía LiteLLM) puede comunicarse con el modelo local `phi3` sin salida a Internet, confirmando la viabilidad de la arquitectura *Zero Latency*.

**Hecho:** Se ejecutó con éxito la sonda `test_ia.py`, obteniendo respuesta directa del modelo local. Se establecieron los directorios estructurales `/merci-brain/` y `/laboratorio/prompts/`.

**Detalle técnico:** LiteLLM enrutó correctamente la petición al puerto `11434` local con la telemetría desactivada. El modelo `phi3` devolvió una respuesta coherente sobre DevSecOps, confirmando la operatividad del *Hybrid Stack*.

**Motivo / criterio:** *Fail-Fast y Zero Trust*. Antes de acoplar la IA al orquestador maestro, esta prueba de conectividad garantiza que el puente de red local es estable, blindando la privacidad del código fuente y evitando dependencias bloqueantes de terceros (APIs caídas o cuotas excedidas).

**Siguiente paso o deuda:** Redactar el primer prompt base en `/laboratorio/prompts/` para estandarizar la forma en que la IA auditará el proyecto.

### 2026-05-07 — Feat: Soporte multi-bitácora en orquestador de commits

**Contexto:** Al inaugurar la nueva bitácora exclusiva para la Fase de Orquestación IA, el script de empaquetado atómico (`merci-commit.py`) quedó ciego, ya que tenía la ruta de la bitácora original hardcodeada.

**Hecho:** Se refactorizó `scripts/merci/merci-commit.py` para soportar múltiples bitácoras activas.

**Detalle técnico:** Se implementó la función `obtener_bitacora_activa()` que lee las fechas de modificación física (`st_mtime`) de una lista permitida de bitácoras. El script asume como "bitácora activa" aquella que haya sido guardada más recientemente y extrae de ella el mensaje para Git.

**Motivo / criterio:** *Separation of Concerns y Fricción Cero*. Unificar las bitácoras destruiría el trabajo de segregación documental que acabamos de hacer. Volver el script inteligente para que sepa en qué archivo estás trabajando actualmente mantiene el pipeline ágil sin sacrificar la organización.

**Siguiente paso o deuda:** Validar el empaquetado atómico y reanudar el setup de IA.

### 2026-05-07 — Feat: Integración de extracción de métricas en orquestador maestro

**Contexto:** La actualización de los datos del Engineering Dashboard en la portada dependía de la ejecución manual del script de extracción de PDFs, generando riesgo de olvido y desincronización (Data Drift).

**Hecho:** Se promovió `merci-extract-metrics.py` de script temporal a herramienta oficial del núcleo (`scripts/merci/`) y se inyectó en el pipeline de `merci-total.py`. Se actualizó la documentación en `requirements.txt`.

**Detalle técnico:** El script se ejecuta en la fase de Construcción (Build), justo antes del lóbulo frontal de IA, automatizando la inyección de los datos de PageSpeed en el frontend.

**Motivo / criterio:** *Fricción Cero y Pipeline as Code*. Todo proceso recurrente debe formar parte del orquestador. Elevar el script al directorio principal legitima su uso como dependencia clave para mantener las métricas 100/100 certificadas empíricamente y actualizadas.

**Siguiente paso o deuda:** Iniciar el script de prueba para Ollama y LiteLLM.

### 2026-05-07 — Perf: Automatización de Cache Busting dinámico en núcleo estático

**Contexto:** Se estaba actualizando manualmente el parámetro `?v=X` en el archivo `public/index.html` cada vez que había un cambio en SASS o JS para forzar la purga de caché, lo cual introducía fricción operativa repetitiva.

**Hecho:** Se refactorizó `scripts/merci/merci-publish.py` para auto-inyectar la marca de tiempo (timestamp) en la portada estática.

**Detalle técnico:** El script ahora lee la fecha de modificación (`st_mtime`) de los archivos CSS y JS, y utiliza expresiones regulares (`re.sub`) para buscar y reemplazar los parámetros `?v=...` directamente en el código de `public/index.html` antes de extraer el header y footer.

**Motivo / criterio:** *Fricción Cero y Single Source of Truth*. Al actualizar la portada estáticamente durante la fase de Build (`merci publish`), el archivo queda versionado en Git automáticamente con la versión más reciente. Posteriormente, `merci-sync-pages.py` propaga este HTML actualizado al resto de las páginas estáticas (como Contacto), cerrando el ciclo de automatización sin intervención humana.

**Siguiente paso o deuda:** Finalizar instalación local de Inteligencia Artificial (Ollama y LiteLLM) de la Fase 1.

### 2026-05-07 — Feat: Instalación exitosa de motor IA local (Ollama)

**Contexto:** Tras el fallo de conexión SSL documentado anteriormente, se requería reintentar la instalación del motor Ollama en el sistema anfitrión para asentar la base del Hybrid Stack.

**Hecho:** Se instaló Ollama correctamente en Ubuntu y se procedió a descargar el modelo de lenguaje `phi3`.

**Detalle técnico:** El modelo `phi3` fue seleccionado por su alta relación capacidad/peso, ideal para tareas de DevSecOps en entornos de desarrollo local. Se configuró un script puente con `litellm` para validar la conexión a través del puerto 11434.

**Motivo / criterio:** *Zero Latency y Privacidad*. Disponer del motor ejecutándose nativamente aísla nuestro flujo de orquestación de caídas de red o límites de cuota de APIs externas (Gemini), permitiendo procesar código fuente de forma 100% privada.

**Siguiente paso o deuda:** Ejecutar el script `test_ia.py` para validar la conexión Python-Ollama e iniciar la estandarización de Prompts.

### 2026-05-07 — Fix: Error de instalación de Ollama (SSL_ERROR_SYSCALL)

**Contexto:** Al intentar instalar Ollama en el sistema anfitrión como parte de la Fase 1 del Roadmap de IA, el script de instalación falló con errores de conexión SSL y corrupción de archivo.

**Hecho:** El comando `curl -fsSL https://ollama.com/install.sh | sh` devolvió `OpenSSL SSL_connect: SSL_ERROR_SYSCALL` y `zstd: unexpected end of file`, indicando una descarga incompleta del binario de Ollama.

**Detalle técnico:** El error `SSL_ERROR_SYSCALL` sugiere una interrupción de la conexión segura (HTTPS) con el servidor de descarga de GitHub (`release-assets.githubusercontent.com`). Esto puede ser causado por problemas de red, un firewall restrictivo o un proxy. La corrupción del archivo (`zstd`, `tar`) es una consecuencia directa de la descarga fallida.

**Motivo / criterio:** *Resiliencia de Infraestructura*. La instalación de herramientas de bajo nivel puede verse afectada por factores externos al código. Es crucial diagnosticar la causa raíz de los fallos de red para asegurar una base sólida para el entorno de IA.

**Siguiente paso o deuda:** Solucionar el problema de descarga de Ollama, verificar la conectividad de red y reintentar la instalación.

### 2026-05-07 — Arch: Diseño del Hybrid Stack (LiteLLM + Ollama)

**Contexto:** Arrancar la Fase 1 estableciendo la conectividad base de la Inteligencia Artificial con la premisa de no depender exclusivamente de APIs de terceros (Gemini) tras sufrir bloqueos por cuota (Rate Limits).

**Hecho:** Se decide implementar una arquitectura híbrida inyectando `litellm` en el entorno virtual local y preparando `Ollama` en el sistema anfitrión.

**Detalle técnico:** LiteLLM actuará como un traductor universal (proxy) dentro de nuestros scripts de Python (`merci-brain.py`). Esto permite cambiar de proveedor (de un modelo Llama 3 local a Gemini en la nube) modificando solo una cadena de texto, sin reescribir la lógica de la API.

**Motivo / criterio:** *Agnosticismo de Modelos y Zero Latency*. Evitar el *Vendor Lock-in* con Google o OpenAI. Usar modelos locales reduce a cero el coste y los límites de red para tareas repetitivas de QA, dejando los modelos de frontera en la nube solo como contingencia (*Graceful Degradation*).

**Siguiente paso o deuda:** Instalar Ollama en el anfitrión, descargar el primer modelo local e instalar `litellm` en el entorno virtual.

### 2026-05-07 — Milestone: Sello Definitivo Pre-IA e Inicio de Orquestación

**Contexto:** Tras aplicar la exclusión correcta en los backups locales y reducir su peso a 1.67 MB, el ecosistema base demostró estar libre de errores (0 WARN, 0 ERROR en `merci total`).

**Hecho:** Se emite el Sello Definitivo sobre las Fases 1 a 11. Se inicia oficialmente la Fase 1 del `ROADMAP-AI-ORQUESTACION-SELF-HEALING-SYSTEM.md`.

**Detalle técnico:** El entorno base queda congelado y blindado como plataforma de despegue.

**Motivo / criterio:** *Clean Slate*. No se puede orquestar inteligencia artificial sobre un sistema con deuda técnica. Al certificar la higiene del proyecto matriz, garantizamos que los futuros agentes de IA no alucinarán intentando arreglar errores de infraestructura subyacente.

**Siguiente paso o deuda:** Crear el directorio `/merci-brain` y preparar `/laboratorio/prompts` para la estandarización de agentes.

*(Las entradas de 2026-05-06 y 2026-05-07 relativas al cierre de Fases 1–11 y al pivote de Art de Coté están registradas en `bitacora-mercedev.md`. Esta bitácora recoge únicamente los hitos del Roadmap de IA a partir de la primera sesión de trabajo en ese nuevo contexto.)*
