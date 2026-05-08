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

### 2026-05-08 — QA: Diagnóstico profundo de red local con tcpdump

**Contexto (Desafío):** Era necesario inspeccionar el tráfico exacto entre el orquestador Python y el motor de IA local (LM Studio) para entender por qué los modelos fallan devolviendo respuestas vacías o truncadas a pesar de los ajustes en el código.

**Hecho (Maniobra):** Se utilizó el comando de rastreo de paquetes de red: `sudo tcpdump -i lo -A port 1234`.

**Motivo / criterio (Aprendizaje):** *Deep Observability*. El comando `tcpdump` escuchando en la interfaz *loopback* (`lo`) en formato texto (`-A`) es la herramienta forense definitiva. Al analizar el payload, reveló que el modelo Qwen 3.5 9B agotaba el límite de contexto físico de 4096 tokens (1785 prompt + 2311 completion = 4096). Además, demostró que la IA ignoraba la orden de "no razonar", gastando 2310 tokens en un monólogo interno (`reasoning_tokens`) y dejando 0 tokens para escribir el documento real.

**Siguiente paso o deuda:** Aceptar que los modelos locales con razonamiento interno forzado no son aptos para tareas de reescritura de documentos largos bajo restricciones severas de RAM (4096 tokens). Asumir la dependencia de Gemini Flash para el Agente SSOT.

### 2026-05-08 — Test: Evaluación de Qwen 3.5 (9B) como motor local para SSOT

**Contexto (Desafío):** En la búsqueda del motor local óptimo para tareas lógicas complejas (como la sincronización del Roadmap) que no agote la memoria del sistema anfitrión, se seleccionó el modelo `qwen/qwen3.5-9b`.

**Hecho (Maniobra):** Se cargó el modelo en LM Studio mediante CLI asegurando el límite estricto de contexto (`lms load qwen/qwen3.5-9b -c 4096`) para compensar el mayor peso de sus 9 billones de parámetros en la RAM.

**Motivo / criterio (Aprendizaje):** *Agnosticismo de Modelos*. Gracias a la capa de abstracción de LiteLLM configurada con el alias universal `"openai/local-model"`, el ecosistema puede pivotar entre diferentes motores de IA locales al instante sin requerir refactorización de código en los scripts de Python. El modelo de 9B ofrece un salto cualitativo en razonamiento deductivo manteniendo la viabilidad en hardware local gracias al *Resource Budgeting* previo.

**Siguiente paso o deuda:** Ejecutar `merci ssot` para certificar que el modelo de 9B es capaz de actualizar el Roadmap respetando las reglas de formato sin saturar el sistema.

### 2026-05-08 — Perf: Prevención de OOM (Out of Memory) en inferencia local

**Contexto (Desafío):** Forzar el tamaño de contexto de LM Studio a 8192 tokens para evitar truncamientos provocaba que el ordenador anfitrión se colgara (OOM - Out of Memory) por agotamiento de RAM/VRAM con el modelo Qwen 7B.

**Hecho (Maniobra):** Se instruyó cargar el modelo localmente vía CLI con un contexto conservador (`lms load <modelo> -c 4096`). En `scripts/merci/merci-ssot.py`, se redujo el parámetro `max_tokens` de 4000 a 2500.

**Motivo / criterio (Aprendizaje):** *Resource Budgeting*. El tamaño de la ventana de contexto exige reserva de RAM inmediata. Si la memoria requerida por los pesos del modelo + el contexto excede la física disponible, el sistema operativo usa *swap* y colapsa. Balancear `max_tokens` en el script (2500 es suficiente para el Roadmap) libera tokens para el prompt dentro de un límite de contexto seguro (4096), evitando que el PC se congele.

**Siguiente paso o deuda:** Levantar el servidor con 4096 tokens, ejecutar `merci ssot` y validar la actualización sin bloqueos de sistema.

### 2026-05-08 — QA: Diagnóstico profundo con tcpdump (Token Limits y Reasoning)

**Contexto (Desafío):** El Agente SSOT con IA local seguía siendo bloqueado por el Escudo Anti-Destrucción. La salida de consola no daba suficiente información sobre la causa raíz del fallo en la API de LM Studio.

**Hecho (Maniobra):** Se ejecutó una captura de red (`sudo tcpdump -i lo -A port 1234`) para interceptar el tráfico HTTP entre el script y el servidor local de IA. Se actualizó el *System Prompt* en `merci-ssot.py` para prohibir explícitamente las cadenas de pensamiento (*Chain of Thought*).

**Detalle técnico:** El comando de monitorización `sudo tcpdump -i lo -A port 1234` intercepta en texto plano (`-A`) todo el tráfico de la interfaz *loopback* (`lo`) en el puerto especificado. Es la herramienta definitiva para auditar el payload JSON exacto (entradas y salidas) que viaja entre los scripts de Python y los motores locales (LM Studio/Ollama) cuando los logs estándar no son suficientes.

**Motivo / criterio (Aprendizaje):** *Deep Observability*. El volcado de red reveló datos espectaculares: el modelo agotó el límite duro de la ventana de contexto (1797 prompt + 2299 completion = 4096 `total_tokens`), abortando por `"finish_reason": "length"`. Además, los 2298 tokens generados fueron consumidos enteramente por el monólogo interno de la IA (`reasoning_tokens`), devolviendo un `content` vacío (`""`). Combinar la ampliación estricta de memoria en la terminal/GUI de LM Studio (8192) con una prohibición de razonamiento en el prompt asegura la entrega íntegra del documento.

**Siguiente paso o deuda:** Recargar el modelo en LM Studio con el nuevo límite de contexto y ejecutar `merci ssot` para validar la escritura del Roadmap.

### 2026-05-08 — Fix: Reducción de contexto y Timeout extendido para IA Local

**Contexto (Desafío):** Al ejecutar el Agente SSOT contra LM Studio (Qwen), el modelo devolvió un texto truncado (activando el escudo anti-destrucción) o generó un `ReadTimeoutError`. Esto ocurrió porque el contexto enviado (Roadmap + 5 entradas de bitácora) saturó la "Context Length" por defecto de LM Studio, y el tiempo de inferencia local superó el tiempo de espera de LiteLLM.

**Hecho (Maniobra):** Se refactorizó `scripts/merci/merci-ssot.py` para limitar la extracción de la bitácora a únicamente las 2 últimas entradas (`entradas[1:3]`). Se inyectó el parámetro `timeout=600` (10 minutos) en las llamadas a `completion()` para soportar hardware más lento.

**Motivo / criterio (Aprendizaje):** *Context Window Management*. Enviar exceso de historial a modelos locales satura su memoria de trabajo (RAM/VRAM), provocando truncamientos catastróficos. Reducir la carga de entrada otorga margen para que el modelo genere la salida completa. Extender los *timeouts* adapta el orquestador a la latencia real de la inferencia local.

**Siguiente paso o deuda:** Validar la escritura completa del Roadmap por parte de Qwen y compilar el proyecto.

### 2026-05-08 — Fix: Prevención de truncamiento y resúmenes en LM Studio

**Contexto (Desafío):** Al ejecutar el Agente SSOT contra LM Studio usando el modelo Qwen 2.5 Coder, el escudo anti-alucinaciones detuvo la ejecución porque la respuesta devuelta por la IA era un resumen o estaba incompleta (`< 50%` del original).

**Hecho (Maniobra):** Se inyectaron los parámetros `temperature=0.0` y `max_tokens=4000` en las llamadas a `completion()` en `scripts/merci/merci-ssot.py`. Además, se reforzó el *System Prompt* con la instrucción explícita: "COPIA EL ROADMAP ORIGINAL DE PRINCIPIO A FIN Y APLICA LOS CAMBIOS. NO RESUMAS."

**Motivo / criterio (Aprendizaje):** *Determinismo y Límites de Inferencia*. Los modelos locales cargados a través de endpoints compatibles con OpenAI a menudo asumen límites de tokens muy bajos por defecto (ej. 256 o 512 tokens), cortando la generación de documentos largos. Forzar el límite máximo (`4000`) asegura la extracción del documento completo, y la temperatura `0.0` anula la "creatividad" destructiva del modelo obligándole a ceñirse al formato.

**Siguiente paso o deuda:** Validar nuevamente la reescritura del Roadmap con `merci ssot` y proceder al `merci total`.

### 2026-05-08 — Fix: Resolución de artefactos GGUF en LM Studio (Hugging Face)

**Contexto (Desafío):** Al intentar descargar el modelo Qwen 2.5 Coder con el ID `lmstudio-community/Qwen2.5-Coder-7B-Instruct-GGUF`, el CLI de LM Studio devolvió el error `Failed to resolve artifact`. Esto ocurre porque el CLI exige una correspondencia exacta con un repositorio existente en Hugging Face, y el repositorio sugerido no existía o había sido renombrado.

**Hecho (Maniobra):** Se instruyó utilizar los repositorios oficiales o los repositorios de cuantizadores verificados en Hugging Face (ej. `Qwen/Qwen2.5-Coder-7B-Instruct-GGUF`).

**Motivo / criterio (Aprendizaje):** *Supply Chain & Dependency Resolution*. Cuando se operan motores de inferencia locales (Headless), la cadena de suministro de modelos es tan crítica como la de paquetes Python (PyPI). Depender de repositorios comunitarios genéricos puede causar fallos de resolución (404). Apuntar directamente a los repositorios oficiales (Qwen) o cuantizadores consolidados garantiza la disponibilidad inmutable del artefacto.

**Siguiente paso o deuda:** Descargar el modelo oficial, arrancar el servidor `lms` y verificar que el comando `merci ssot` se ejecute en la raíz del proyecto.

### 2026-05-08 — Fix: Corrección de comando fantasma en LM Studio (Alucinación)

**Contexto (Desafío):** Al intentar descargar un modelo de IA en modo *Headless*, el CLI devolvió el error `unknown command 'download'`. Se constató que el comando `lms download` sugerido previamente era una alucinación (tanto de Gemini Web como asimilada erróneamente en esta misma bitácora).

**Hecho (Maniobra):** Se corrigió la instrucción operativa al comando oficial y real de LM Studio: `lms get <modelo>`. Adicionalmente, se constató que si el alias corto no es un "staff pick", se debe proveer el ID exacto del repositorio (ej. `lmstudio-community/Qwen2.5-Coder-7B-Instruct-GGUF`) o usar `lms search` previamente. Se ha enmendado retrospectivamente la entrada inferior de la bitácora para purgar el comando fantasma.

**Motivo / criterio (Aprendizaje):** *Verificación Empírica vs. LLM Output*. Las IAs generativas comerciales a menudo alucinan comandos basándose en patrones lógicos (`download`) en lugar de leer la documentación real. En LM Studio CLI, el comando de adquisición sigue el estándar POSIX `get` (como `apt-get`). Confiar ciegamente en un output de chat sin validación empírica en terminal genera deuda de documentación.

**Siguiente paso o deuda:** Descargar el modelo con su ID exacto (ej. `lms get lmstudio-community/Qwen2.5-Coder-7B-Instruct-GGUF`) y levantar el servidor con `lms server start`.

### 2026-05-08 — Conf: Despliegue de LM Studio en modo Headless (CLI-first)

**Contexto (Desafío):** Al migrar a LM Studio, se constató que la versión instalada en el entorno era exclusivamente de terminal (`lms`), sin Interfaz Gráfica de Usuario (GUI). Esto requería adaptar el flujo de trabajo para aprovisionar y servir modelos de IA de forma completamente desatendida.

**Hecho (Maniobra):** Se estandarizó el uso de LM Studio CLI para el ecosistema. Los comandos operativos son: `lms download <modelo>` para descargar el binario, y `lms server start` para levantar el *endpoint* compatible con OpenAI en el puerto 1234.
**Hecho (Maniobra):** Se estandarizó el uso de LM Studio CLI para el ecosistema. Los comandos operativos son: `lms get <modelo>` para descargar el binario, y `lms server start` para levantar el *endpoint* compatible con OpenAI en el puerto 1234.

**Motivo / criterio (Aprendizaje):** *Headless Operations & CLI-First*. Depender de una GUI rompe la automatización. Operar el motor de inferencia local exclusivamente a través de la terminal certifica que el entorno DevSecOps puede ser portado en el futuro a servidores remotos (VPS) sin entorno de escritorio, garantizando la resiliencia de la infraestructura.

**Siguiente paso o deuda:** Mantener el servidor `lms` corriendo en una terminal en segundo plano y ejecutar `merci ssot` para validar la corrección del Roadmap.

### 2026-05-08 — Feat: Migración de motor local a LM Studio y restauración de Fallback

**Contexto (Desafío):** La dependencia de la API de Gemini (nube) bloqueaba el pipeline por frecuentes errores de cuota (404/429). El uso previo de Ollama limitaba la flexibilidad para intercambiar modelos de forma visual. Se necesitaba un motor de inferencia local más robusto para tareas de redacción y código sin límites.

**Hecho (Maniobra):** Se adoptó LM Studio como motor de inferencia local. Se restauró la lógica de Degradación Elegante (Fallback) en `scripts/merci/merci-ssot.py`, configurando LiteLLM para enrutar las peticiones al servidor compatible con OpenAI de LM Studio (`http://localhost:1234/v1`).

**Motivo / criterio (Aprendizaje):** *Infrastructure Flexibility*. LM Studio levanta una API nativa de OpenAI, lo que encaja perfectamente con nuestra capa de abstracción LiteLLM sin necesidad de reescribir los scripts. Esto permite al usuario cambiar de modelo gráficamente (ej. Qwen para código, Mistral para cuadernillos) dependiendo de la tarea, devolviendo la operatividad local al ecosistema DevSecOps.

**Siguiente paso o deuda:** Mantener el servidor local de LM Studio encendido al ejecutar los agentes y evaluar la recuperación del Agente Bibliotecario con modelos locales más avanzados.

### 2026-05-08 — Chore: Auditoría y trazabilidad de scripts temporales (Deuda Técnica)

**Contexto (Desafío):** El directorio `laboratorio/scripts_temporales/` almacenaba scripts experimentales o deprecados (`merci-wc-mock.py`, `merci_ingestor.py`, `merci_sitemap.py`, `pre-commit.sh`) que carecían de trazabilidad formal, convirtiéndose en "código zombi" sin contexto de por qué fueron descartados.

**Hecho (Maniobra):** Se inyectaron cabeceras `# TODO(Fase X):...` en la primera línea de los 4 scripts temporales, justificando su estado actual y el motivo de su preservación (Art de Coté) o deprecación.

**Motivo / criterio (Aprendizaje):** *Code Provenance* (Procedencia del Código). Nunca se debe almacenar código sin documentar su propósito o el motivo de su rechazo. Al etiquetarlos explícitamente, se salda la deuda técnica de mantenimiento y se asegura que futuros desarrolladores no intenten integrarlos por error en el orquestador principal.

**Siguiente paso o deuda:** Ejecutar `merci total` para validar la estabilidad del repositorio y empaquetar el commit de cierre de sesión.

### 2026-05-08 — Arch: Erradicación del Fallback Local en Agentes de Gobernanza

**Contexto (Desafío):** Al ejecutar el Agente SSOT con Llama 3 (8B) como fallback, el modelo superó el "Escudo Anti-Destrucción" (Sanity Checks) devolviendo el Roadmap entero, pero falló en el razonamiento semántico: no marcó ninguna tarea como completada y añadió una nota conversacional en inglés al final del documento (`Note: No changes were made...`).

**Hecho (Maniobra):** Se editó manualmente el Roadmap para marcar las tareas completadas y eliminar el ruido del bot. Se eliminó por completo el bloque `try-except` de Degradación Elegante en `scripts/merci/merci-ssot.py`, forzando a que el agente solo opere con Gemini Flash en la nube o falle bloqueando la ejecución.

**Motivo / criterio (Aprendizaje):** *Cloud-Only for Governance*. Tareas de sincronización documental (SSOT) exigen inferencia lógica precisa (conectar "deprecación" en bitácora con `[x]` en roadmap). Los modelos locales pequeños no sirven para gobernanza documental. Fallar estrepitosamente deteniendo el pipeline (Fail-Fast) es infinitamente superior a que un agente "tonto" contamine archivos oficiales creyendo que está ayudando.

**Siguiente paso o deuda:** Mantener `merci-ssot.py` exclusivamente dependiente de la API y auditar los scripts temporales pendientes.

### 2026-05-08 — Fix: Escudo anti-destrucción (Sanity Checks) en Agente SSOT

**Contexto (Desafío):** Al ejecutar el Agente SSOT en local, Llama 3 (8B) sufrió de "Chatbot Syndrome". En lugar de devolver el documento Markdown completo, generó un resumen conversacional en inglés (`After evaluating...`). Como el script carecía de validación de longitud, sobrescribió y destruyó físicamente el Roadmap.

**Hecho (Maniobra):** Se restauró el archivo mediante Git. Se inyectó un "Escudo Anti-Alucinaciones" en `scripts/merci/merci-ssot.py` que bloquea la escritura en disco si la salida de la IA es inferior al 50% del tamaño original o si carece del formato Markdown (`# `). Se endureció el prompt para prohibir frases de relleno.

**Motivo / criterio (Aprendizaje):** *Fail-Safe File I/O*. Ningún agente de Inteligencia Artificial debe tener permisos de escritura ciegos sobre el sistema de archivos. Validar matemáticamente que el *output* mantiene proporciones y firmas estructurales similares al *input* es la barrera DevSecOps definitiva contra la destrucción de datos por alucinaciones.

**Siguiente paso o deuda:** Validar que el agente no destruya el archivo y delegar tareas SSOT complejas exclusivamente a modelos de frontera si Llama 3 persiste en resumir.

### 2026-05-08 — Fix: Fallback a Llama 3 y sanitización en Agente SSOT

**Contexto (Desafío):** Al ejecutar el Agente SSOT, Gemini devolvió un error `HTTP 404`, bloqueando la sincronización del Roadmap. Además, el script carecía de un fallback local (Degradación Elegante) y presentaba un bug en la lectura de la respuesta de LiteLLM (`choices.message` en lugar de `choices[0].message`).

**Hecho (Maniobra):** Se refactorizó `scripts/merci/merci-ssot.py` para implementar un bloque `try-except` que delega la tarea a `llama3` local si Gemini falla. Se corrigió el acceso al array de respuestas (`choices[0]`) y se robusteció `clean_markdown()` para amputar el texto conversacional de los modelos locales.

**Motivo / criterio (Aprendizaje):** *Resiliencia de Agentes*. Todo agente autónomo debe tener una vía de escape local si la nube falla. Una tarea simple como cambiar un `[ ]` por un `[x]` está perfectamente dentro de las capacidades lógicas de Llama 3 (8B), haciendo innecesario el bloqueo operativo por caídas de API.

**Siguiente paso o deuda:** Ejecutar `merci ssot` para validar que Llama 3 sincroniza el Roadmap con éxito.

### 2026-05-08 — Feat: Creación del Agente Sync SSOT (Self-Healing Docs)

**Contexto (Desafío):** Al avanzar rápido en el desarrollo, a menudo se documentan logros o deprecaciones en la bitácora, pero se olvida marcar la casilla `[x]` correspondiente en el Roadmap, generando "Deriva Documental" (Document Drift) y pérdida de la Única Fuente de Verdad (SSOT).

**Hecho (Maniobra):** Se desarrolló `scripts/merci/merci-ssot.py`. El agente extrae los últimos registros de la bitácora y el estado actual del Roadmap, enviándolos a Gemini Flash con la orden estricta de auto-completar las tareas logradas o deprecadas reescribiendo el archivo Markdown.

**Motivo / criterio (Aprendizaje):** *Document as Code & Self-Healing*. La sincronización de estados no debe depender de la memoria humana ni de scripts locales limitados. Delegar el análisis semántico a un modelo de frontera garantiza que nuestro plan de proyecto refleje fielmente la realidad del código en todo momento, curando la documentación automáticamente.

**Siguiente paso o deuda:** Ejecutar el Agente SSOT para que detecte la deprecación del Bibliotecario y actualice el Roadmap.

### 2026-05-08 — Arch: Deprecación del Agente Bibliotecario (RAG Local) a Art de Coté

**Contexto (Desafío):** A pesar de la agresiva sanitización de salida y la optimización del contexto, el modelo local Llama 3 (8B) continuaba fallando en la generación consistente de cuadernillos con formato YAML estricto (*Context Window Stuffing* y *Recency Bias*). El esfuerzo de domar la IA local añadía más fricción operativa que la redacción manual.

**Hecho (Maniobra):** Se decidió abortar el uso del Agente Bibliotecario en local. El script `scripts/merci/merci-librarian.py` fue modificado con un marcador `TODO` y desplazado a `laboratorio/scripts_temporales/merci-librarian.py`. Se redactó el cuadernillo explicativo en `laboratorio/art-de-cote/`.

**Motivo / criterio (Aprendizaje):** *Fail-Fast y ROI*. Si una herramienta diseñada para eliminar fricción se convierte en un sumidero de tiempo de depuración, debe ser descartada. Los modelos locales <14B aún no poseen la atención sostenida para combinar RAG denso y *Zero-Shot formatting* simultáneamente. Preservar el script como *Art de Coté* guarda las lecciones de Prompt Engineering sin contaminar el núcleo operativo.

**Siguiente paso o deuda:** Auditar los scripts en `laboratorio/scripts_temporales/` para añadir notas de estado y proceder con el Agente Sync SSOT.

### 2026-05-08 — Fix: Extracción quirúrgica de YAML y neutralización de Recency Bias

**Contexto (Desafío):** El modelo Llama 3 generaba archivos rotos al inyectar relleno conversacional (`Here is the output:`) antes del YAML. Además, sufría de *Recency Bias* (Sesgo de Recencia): al leer la bitácora en el RAG local, ignoraba la nota del usuario y se dedicaba a resumir la última entrada histórica que encontraba.

**Hecho (Maniobra):** Se refactorizó `clean_markdown` en `merci-librarian.py` usando `text.find("---\n")` para amputar matemáticamente cualquier texto previo al Frontmatter. Se invirtió la estructura del Prompt, colocando la nota cruda como "Tema Principal" y la bitácora como "Apoyo Secundario" con instrucciones estrictas de exclusión.

**Motivo / criterio (Aprendizaje):** *Aggressive Output Sanitization*. No se puede confiar en que los LLMs (especialmente los entrenados para chat) respeten el formato *Zero-Shot* de forma consistente. La validación no debe ser pasiva (comprobar si empieza por "```"), sino activa (buscar la firma del código y destruir el resto). Controlar el foco de atención mitigando el sesgo de recencia salva la viabilidad del RAG local.

**Siguiente paso o deuda:** Limpiar el archivo corrupto y validar que Llama 3 ahora obedece y redacta sobre el *bug* del linter.

### 2026-05-08 — Feat: Optimización de RAG (Filtrado Semántico) para LLM Local

**Contexto (Desafío):** El sistema RAG anterior enviaba 6000 caracteres ciegos de historial al modelo local (Llama 3), saturando su ventana de atención (*Context Window Stuffing*) y provocando alucinaciones. Un modelo ligero no puede gestionar un contexto masivo al mismo nivel que un modelo de frontera en la nube (Gemini 1.5 Flash).

**Hecho (Maniobra):** Se refactorizó `get_bitacora_context` en `merci-librarian.py`. El script ahora extrae palabras clave (>4 letras) de la nota cruda y las utiliza para escanear y enviar únicamente las entradas de bitácora que contengan esas palabras, limitando el tamaño a 3000 caracteres.

**Motivo / criterio (Aprendizaje):** *Garbage In, Garbage Out*. Extraer solo las "páginas exactas" en lugar de enviar "toda la estantería" desbloquea la capacidad del RAG en hardware local modesto. Esto robustece el comportamiento de contingencia (Fallback) cuando la IA en la nube no está disponible.

**Siguiente paso o deuda:** Validar la promoción del cuadernillo generado por Gemini y avanzar al Agente Sync SSOT.

### 2026-05-08 — Test: Evaluación de Context Window Stuffing y RAG con Gemini

**Contexto (Desafío):** Al ejecutar el RAG local inyectando 6000 caracteres de bitácora + plantillas + nota corta en el modelo local Llama 3 (8B), el modelo colapsó por exceso de contexto (*Context Window Stuffing*), alucinando una reescritura de las instrucciones de la bitácora en inglés.

**Hecho (Maniobra):** Se delegó la misma carga cognitiva al modelo de frontera en la nube (Gemini 1.5 Flash), el cual procesó el RAG de forma inmaculada, conectando los puntos entre la nota corta y el log histórico, redactando un cuadernillo impecable. Se purgó la alucinación del laboratorio.

**Motivo / criterio (Aprendizaje):** *Model Routing & Cognitive Load*. Los modelos locales ligeros (<14B) son excelentes para tareas de formato Zero-Shot o código delimitado, pero su atención se degrada catastróficamente al saturar su ventana de contexto (RAG denso). El enrutamiento de agentes debe derivar tareas de "compresión semántica densa" hacia modelos de frontera (Cloud), reservando el modelo local solo para contingencias simples o análisis de sintaxis corta.

**Siguiente paso o deuda:** Validar este cuadernillo perfecto con `merci promote` y avanzar al siguiente Agente del Roadmap: Sync SSOT.

### 2026-05-08 — Feat: Inyección de contexto histórico (RAG Local) en Agente Bibliotecario

**Contexto (Desafío):** El modelo local (Llama 3) estructuraba bien las notas cortas gracias a las plantillas (*One-Shot Prompting*), pero el contenido redactado carecía de profundidad técnica. La IA no podía expandir una nota de tres líneas sin inventar datos, ya que desconocía los detalles técnicos subyacentes del incidente.

**Hecho (Maniobra):** Se implementó un sistema RAG (Retrieval-Augmented Generation) primitivo en `scripts/merci/merci-librarian.py`. El script ahora lee los primeros 6000 caracteres de las bitácoras activas y los inyecta en el prompt, instruyendo a la IA a cruzar la nota cruda con el registro histórico para extraer el contexto técnico ampliado.

**Motivo / criterio (Aprendizaje):** *Context Enrichment & Single Source of Truth*. Una IA redactora sin contexto solo puede parafrasear. Al alimentar a Llama 3 con el historial de desarrollo reciente, le otorgamos la "memoria" del proyecto. Esto permite que el flujo DevSecOps fluya: la autora anota un recordatorio mínimo y la IA usa la bitácora para redactar el documento técnico definitivo, logrando fricción cero.

**Siguiente paso o deuda:** Re-ejecutar `merci librarian` para validar que Llama 3 es capaz de relacionar la nota corta del linter con su entrada detallada en la bitácora.

### 2026-05-08 — Fix: Inyección de plantillas (One-Shot Prompting) en Agente Bibliotecario

**Contexto (Desafío):** Al escalar al modelo local Llama 3 (8B), se constató que, si bien es excelente en compresión semántica y redacción deductiva, tiende a "relajarse" con las instrucciones de formato puro (omitiendo etiquetas YAML o inventando estructuras) cuando opera en modo *Zero-Shot* (sin ejemplos previos).

**Hecho (Maniobra):** Se refactorizó `scripts/merci/merci-librarian.py` para que lea físicamente el contenido de los archivos de plantilla (`docs/plantilla-cuadernillo.md`, `plantilla-proyecto.md` y `plantilla-art-de-cote.md`) e inyecte su estructura directamente en el prompt del usuario como una "Regla Estricta de Formato".

**Motivo / criterio (Aprendizaje):** *In-Context Learning*. Los modelos LLM locales de menos de 70B de parámetros rinden infinitamente mejor si se les proporciona un molde rígido a rellenar ("enseña, no cuentes"). Inyectar la plantilla real en tiempo de compilación garantiza que Llama 3 no tenga margen para la improvisación estructural, blindando la integridad del parser YAML.

**Siguiente paso o deuda:** Re-ejecutar `merci librarian` con la nota corta para validar que ahora genera la deducción correcta pero encapsulada en el YAML estricto.

### 2026-05-08 — Test: Evaluación de Llama 3 con notas de bajo contexto

**Contexto (Desafío):** Tras validar que Llama 3 respeta (en su mayoría) la estructura de los 3 átomos, se plantea la duda de si es capaz de inferir y redactar un cuadernillo completo a partir de una nota extremadamente breve y con muy bajo contexto, actuando como un verdadero agente de expansión de conocimiento.

**Hecho (Maniobra):** Se creó una nota minimalista (`nota-corta-linter.md`) en `laboratorio/notas_rapidas/` sobre un incidente menor (ausencia de `.py` en `TEXT_SUFFIXES`) para forzar al Agente Bibliotecario a deducir el Desafío, la Maniobra y el Aprendizaje con apenas tres líneas de texto crudo.

**Motivo / criterio (Aprendizaje):** *Stress Testing the Prompt*. Un buen agente redactor no solo formatea texto, sino que "descomprime" ideas. Si Llama 3 logra estructurar un cuadernillo coherente infiriendo el aprendizaje arquitectónico a partir de un apunte apresurado, se confirmará que la arquitectura del System Prompt compensa la falta de locuacidad humana.

**Siguiente paso o deuda:** Ejecutar `merci librarian` sobre la nota corta y evaluar el nivel de abstracción del modelo.

### 2026-05-08 — Feat: Escalado del modelo local a Llama 3 (8B) en Agente Bibliotecario

**Contexto (Desafío):** La API gratuita de Google (Gemini) sigue devolviendo errores `HTTP 404` intermitentes para los alias de la rama `1.5-flash` debido a restricciones regionales o cambios no documentados. Al aplicar la Degradación Elegante, el modelo local `phi3` volvía a alucinar, demostrando ser incapaz de seguir el *System Prompt* estructural.

**Hecho (Maniobra):** Se sustituyó el modelo local de contingencia `phi3` por `llama3` (8B de parámetros) en `scripts/merci/merci-librarian.py`. Se instruyó la descarga del modelo mediante `ollama pull llama3`.

**Motivo / criterio (Aprendizaje):** *Local AI Resilience*. `phi3` es demasiado pequeño (3.8B) para seguir instrucciones de formato estricto (Zero-Shot YAML Frontmatter). Escalar a `llama3` (8B) proporciona capacidades de razonamiento muy superiores y soporte nativo para seguimiento de instrucciones en español, convirtiendo el *fallback* en una alternativa local verdaderamente operativa y no en un parche que genera más ruido. Liberarse de la tiranía de las APIs de terceros justifica el uso de recursos locales.

**Siguiente paso o deuda:** Descargar el modelo en Ollama, limpiar el cuadernillo residual y relanzar el Agente Bibliotecario.

### 2026-05-08 — Fix: Eliminación de fallback dinámico engañoso y blindaje de merci-brain

**Contexto (Desafío):** Google introdujo un nuevo modelo súper experimental (`gemini-2.5-computer-use-preview-10-2025`) al final de la lista de su API, con límite de cuota 0. La lógica de *fallback* del autodescubridor (`validos[-1]`) lo seleccionó erróneamente, rompiendo nuevamente a `merci-librarian.py`. Además, `merci-brain.py` seguía expuesto a estos mismos fallos y a la contaminación de consola por `FutureWarning`.

**Hecho (Maniobra):** Se eliminó la lógica `validos[-1]` en favor del alias estricto `"gemini-1.5-flash"` en ambos agentes. Se replicaron las políticas de silenciamiento de advertencias (`warnings`) y la exclusión de la familia `2.0-flash` en `scripts/merci/merci-brain.py`.

**Motivo / criterio (Aprendizaje):** *Fail-Safe Default*. Asumir que el último elemento de una API de terceros es una opción segura es un antipatrón. El *fallback* definitivo debe ser siempre un anclaje absoluto a la versión de producción que garantiza cuota. Mantener la paridad de parches entre todos los agentes que consumen la misma API asegura la estabilidad del ecosistema en bloque.

**Siguiente paso o deuda:** Limpiar el archivo residual, re-ejecutar `merci librarian` y auditar la orquestación global con `merci total`.

### 2026-05-08 — Fix: Exclusión de Gemini 2.0 (Límite 0) y silenciamiento de warnings

**Contexto (Desafío):** Al ejecutar el Agente Bibliotecario, el autodescubridor seleccionó el modelo experimental `gemini-2.0-flash`. Sin embargo, Google impone una cuota de 0 peticiones (Free Tier) para este modelo en nuestra región, provocando un `HTTP 429` inmediato y forzando una degradación inútil a `phi3`. Además, la terminal se ensució con un `FutureWarning` de `litellm`.

**Hecho (Maniobra):** Se eliminó `2.0-flash` de la matriz de preferencias en `scripts/merci/merci-librarian.py` para anclar la resolución a la rama estable `1.5-flash`. Se inyectó el módulo `warnings` nativo de Python para silenciar las alertas inofensivas de la librería.

**Motivo / criterio (Aprendizaje):** *Estabilidad sobre Novedad & Clean DX*. Consumir el último modelo disponible es un antipatrón si el proveedor no garantiza cuota operativa. Forzar la rama 1.5 asegura las 1500 peticiones diarias. Ocultar los *warnings* de librerías de terceros (Supply Chain) protege la experiencia de desarrollo (DX) manteniendo la salida de la terminal enfocada en los procesos del proyecto.

**Siguiente paso o deuda:** Limpiar el cuadernillo alucinado y re-ejecutar el Agente Bibliotecario.

### 2026-05-08 — Fix: Resolución de alias 404 en modelo Gemini (Agente Bibliotecario)

**Contexto (Desafío):** Al ejecutar el Agente Bibliotecario, LiteLLM devolvió un error `HTTP 404 (Not Found)` al intentar conectar con `gemini-1.5-flash`. Google AI Studio no reconocía este alias base en la versión `v1beta` de la API requerida por la librería. Se produjo también un `FutureWarning` inofensivo sobre la librería subyacente.

**Hecho (Maniobra):** Se parcheó `scripts/merci/merci-librarian.py` cambiando el modelo objetivo a `gemini/gemini-1.5-flash-latest`.

**Motivo / criterio (Aprendizaje):** *API Resilience & Alias Routing*. Las plataformas de IA en la nube rotan o exigen sufijos explícitos (`-latest`, `-001`) para sus modelos más recientes. Anclar el orquestador al alias `latest` garantiza la resolución del *endpoint* sin importar los cambios en la nomenclatura base de la capa gratuita, estabilizando el *Hybrid Stack*.

**Siguiente paso o deuda:** Re-ejecutar el Agente Bibliotecario para generar definitivamente el cuadernillo.

### 2026-05-08 — Fix: Resolución de dependencia faltante para Gemini (google-generativeai)

**Contexto (Desafío):** Al ejecutar el Agente Bibliotecario, el script falló al intentar conectar con `gemini-1.5-flash` debido a la falta de la librería nativa de Google (`Importing google.generativeai failed`). La Degradación Elegante funcionó, pero el modelo local (`phi3`) sufrió una alucinación severa, inventando contenido sobre Docker, GoLang y JWT al final del documento.

**Hecho (Maniobra):** Se añadió la dependencia `google-generativeai` al archivo `requirements.txt` para que LiteLLM pueda interactuar correctamente con la API de Google en futuras ejecuciones.

**Motivo / criterio (Aprendizaje):** *Supply Chain & Fallback Testing*. LiteLLM es una capa de abstracción, pero requiere los SDKs nativos de los proveedores para funcionar. Este fallo validó empíricamente que nuestra lógica de `try/except` (Fail Gracefully) funciona, protegiendo el orquestador de colapsos absolutos, pero también re-confirmó la falta de fiabilidad de los modelos locales pequeños para tareas de redacción complejas.

**Siguiente paso o deuda:** Instalar la dependencia en el entorno virtual, borrar el cuadernillo alucinado y re-ejecutar `merci librarian`.

### 2026-05-08 — Fix: Migración del Agente Bibliotecario a Gemini Flash (Calidad vs. Rendimiento)

**Contexto (Desafío):** La evaluación empírica del Agente Bibliotecario con el modelo local `phi3` reveló una "caída de atención" significativa, resultando en alucinaciones, incumplimiento de la estructura de los 3 átomos y errores en el Frontmatter YAML. Esto comprometía la calidad del conocimiento de la Biblioteca.

**Hecho (Maniobra):** Se ha decidido modificar `scripts/merci/merci-librarian.py` para que utilice el modelo de frontera `gemini-1.5-flash` a través de LiteLLM como modelo por defecto para la generación de cuadernillos.

**Detalle técnico:** Esta decisión prioriza la calidad del output sobre la latencia mínima. Aunque `gemini-1.5-flash` es una API en la nube (lo que introduce latencia de red), ofrece una capacidad superior para seguir instrucciones complejas y adherirse a formatos estrictos. Las cuotas gratuitas de 1500 peticiones diarias y 15 RPM son significativamente más generosas que las de modelos experimentales anteriores, mitigando el riesgo de bloqueos por consumo de tokens para un uso normal. No obstante, se mantendrá la Degradación Elegante ante posibles `HTTP 429`.

**Motivo / criterio (Aprendizaje):** *Quality over Latency & Strategic Model Selection*. En tareas de redacción técnica que exigen alta fidelidad a la estructura y contenido, la calidad del output es innegociable. La experiencia previa con `merci-brain.py` demostró que `gemini-1.5-flash` ofrece un equilibrio óptimo entre coste (gratuito para límites razonables) y rendimiento cognitivo, siendo la mejor opción para la "Cosecha de Conocimiento". El Agnosticismo de Modelos de LiteLLM nos permite pivotar con fricción cero.

**Siguiente paso o deuda:** Implementar el cambio en `merci-librarian.py` y validar la calidad de los cuadernillos generados.

### 2026-05-08 — Test: Evaluación empírica de capacidades del Agente Bibliotecario (phi3)

**Contexto (Desafío):** Al revisar el resultado de `merci-librarian.py` (`cuadernillo-borrador-nota-gobernanza-ramas-force-push.md`), se constató que el modelo local (`phi3`) falló en la ejecución del *System Prompt*. Ignoró la estructura Markdown de los 3 átomos, colapsó el texto en párrafos planos y alucinó conceptos técnicos peligrosos (ej. requerir "SSH con credenciales OAuth" para proteger ramas).

**Hecho (Maniobra):** Se eliminó el archivo generado por el modelo local. Se reemplazó por la versión curada previamente por el modelo de frontera de Google (Gemini) en el laboratorio, renombrándola a su archivo definitivo (`cuadernillo-gobernanza-ramas-force-push.md`).

**Motivo / criterio (Aprendizaje):** *LLM Limitations & Prompt Engineering*. Modelos locales pequeños (como `phi3` con 3.8B parámetros) sufren de "Attention Drop" (caída de atención) cuando se enfrentan a *Prompts* densos con reglas de formato estricto (Zero-Shot formatting). Si el agente carece de la capacidad cognitiva para estructurar el documento sin inventar datos técnicos, se deberá escalar el modelo local, implementar una "Cadena de Pensamiento" (Chain of Thought), o delegar la tarea de redacción a la API de contingencia (Fallback a Gemini).

**Siguiente paso o deuda:** Evaluar si modificamos `merci-librarian.py` para que use el modelo `gemini-1.5-flash` a través de LiteLLM para tareas complejas de redacción, asegurando la calidad del contenido de la Biblioteca.

### 2026-05-08 — Fix: Endurecimiento de idioma y tipología en Agente Bibliotecario

**Contexto:** Los modelos locales tendían a generar títulos en inglés y a "alucinar" en el campo `tipo` del YAML Frontmatter (escribiendo "compendio técnico" en lugar del estricto "compendio"), lo que rompía la taxonomía del sitio estático en producción.

**Hecho:** Se inyectaron nuevas reglas innegociables en `laboratorio/prompts/prompt-bibliotecario.md`.

**Detalle técnico:** Se añadió la orden explícita de redactar en Español (Castellano) en los placeholders de título y descripción. Se incluyeron dos nuevas reglas restrictivas en la sección de Gobernanza para bloquear la modificación del campo `tipo` y prohibir el uso del inglés.

**Motivo / criterio:** *Prompt Hardening* (Endurecimiento de Prompt). Los LLMs intentan ser "demasiado útiles" expandiendo etiquetas a formatos legibles. En una arquitectura donde el YAML dirige el flujo del código SSG, la IA no tiene permitido alterar los enumeradores estructurales.

**Siguiente paso o deuda:** Re-evaluar el desempeño del Agente SSOT.

### 2026-05-08 — Feat: Enrutamiento interactivo y tipología en Agente Bibliotecario

**Contexto:** El Agente Bibliotecario generaba todos los documentos asumiendo que eran "cuadernillos" destinados a la Biblioteca, ignorando la taxonomía del proyecto que incluye "Compendios" estratégicos y "Art de Coté" (Motor SSG).

**Hecho:** Se refactorizó `scripts/merci/merci-librarian.py` añadiendo un menú interactivo previo a la generación de la IA.

**Detalle técnico:** El usuario ahora elige el tipo de documento. El script inyecta instrucciones contextuales (`instrucciones_extra`) para guiar a `phi3` en el enfoque (táctico, estratégico o experimental). Además, usa `str.replace` sobre el System Prompt para forzar el campo `tipo:` en el YAML y reubica físicamente los Art de Coté en `laboratorio/art-de-cote/` para que `merci-promote` los herede sin fricción hacia la rama estática.

**Motivo / criterio:** *AI Governance*. La IA propone, el humano dispone. Preguntar al humano antes de delegar la redacción a la máquina garantiza que el documento nazca con la topología y el marco mental correctos, evitando retrabajo manual de enrutamiento posterior.

### 2026-05-08 — Feat: Agente Sync SSOT (Single Source of Truth)

**Contexto:** Evitar la Deriva Documental (Document Drift). A menudo se cierran hitos en la bitácora pero se olvida marcar la casilla `[x]` correspondiente en el Roadmap o actualizar el README.

**Hecho:**
- Se desarrolló el agente `scripts/merci/merci-ssot.py`.
- Se marcó el hito del Agente Bibliotecario como completado en el Roadmap.

**Detalle técnico:** El script extrae dinámicamente la última entrada de la bitácora activa y el contenido del Roadmap, inyectando ambos contextos en la IA local (phi3). La IA audita si existe alguna desincronización lógica entre lo ejecutado y lo documentado, emitiendo una alerta en terminal.

**Motivo / criterio:** *Document as Code*. La documentación no puede depender exclusivamente de la memoria humana. Delegar a un LLM la comparación semántica entre el log de cambios (bitácora) y el plan de proyecto (Roadmap) garantiza la integridad de la Única Fuente de Verdad.

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
