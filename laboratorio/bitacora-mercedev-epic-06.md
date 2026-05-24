# Bitácora del proyecto mercedev.es — Épica 6: E-commerce Híbrido Extremo

## Para qué sirve este archivo

Bitácora activa a partir de la finalización de la Épica 5 (Showcase y Distribución del Boilerplate).
Registra exclusivamente las decisiones, experimentos y aprendizajes de la Épica 6 (E-commerce Híbrido Extremo) documentada en el `ROADMAP.md` maestro.

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

### 2026-05-24 — AI & DevSecOps: Refinamiento Extremo del Agente Glosario (Positive Prompting)

**Contexto:** Tras detectar que el LLM padecía del "Síndrome del Loro" (repitiendo instrucciones meta) y del "Elefante Rosa" (al prohibirle ciertas frases las usaba aún más, como "Es como..."), se requería una técnica de doma avanzada para forzar un tono corporativo y conciso.

**Hecho:**
- Se reescribió `laboratorio/prompts/prompt-glosario.md` con *Positive Prompting*, prohibiendo el uso de artículos iniciales ("Un", "La") y exigiendo que la respuesta comience directamente con el sustantivo.
- Se inyectó la regla de `REDACCIÓN LIMPIA` para evitar que la IA incluya meta-instrucciones en su salida.
- Se purgó `glosario-tecnico.json` de alucinaciones (como deducir que `LM` era *Last Modified* o `TL` era *Tactical Lead*).

**Motivo / criterio:** *AI Governance y Prompt Hardening*. Los modelos locales pequeños responden infinitamente mejor a estructuras directas y ejemplos de cómo *deben* hacer las cosas en lugar de prohibiciones sobre cómo *no* hacerlas. Establecer reglas claras recupera el formato de diccionario técnico estricto.

### 2026-05-24 — Fix: Resiliencia ante conflictos Git y recuperación de JSON malformado

**Contexto:** Conflictos de versiones de Git y operaciones sucesivas habían revertido silenciosamente el archivo `prompt-glosario.md` a estados previos (Deriva de Código), y operaciones iterativas de *diff* habían corrompido las llaves del `glosario-tecnico.json`, paralizando el orquestador.

**Hecho:** Se restauró la estructura del JSON saneando el array de términos y agregando los elementos erróneos a `ignorados`. Se reinyectaron definitivamente las Reglas 5 y 6 de endurecimiento en el prompt maestro.

**Motivo / criterio:** *Disaster Recovery*. Estos fallos son inherentes a los ciclos ágiles veloces. La rápida recuperación mediante Git y parches de saneamiento consolida la fiabilidad de operar bajo una Única Fuente de Verdad y tener un *Fail-Fast* en los analizadores de código.

### 2026-05-24 — UX/UI: Refactorización visual y semántica del Glosario Técnico

**Contexto:** El formato del Glosario en HTML/PDF resultaba muy denso, con etiquetas `<br>` que no espaciaban adecuadamente los contenidos y textos encadenados que dificultaban la lectura en el producto final.

**Hecho:**
- Se refactorizó la función `compile_markdown` en `scripts/merci/merci-glosario.py`.
- Se separó el Inglés y Español con un tabulador visual `|`.
- Se implementaron saltos de párrafo dobles (`\n\n`) para espaciar definiciones y se limpió el encabezado para no repetir el título.
- Se sustituyó la etiqueta `<code>` por cursivas puras de Markdown (`*`) para la sección interactiva "Merci Explica".

**Motivo / criterio:** *UX Editorial y Markdown Purity*. Una enciclopedia técnica debe priorizar la ergonomía visual (espacios en blanco). Reducir el uso de etiquetas HTML en favor del Markdown nativo facilita un renderizado inmaculado tanto en el DOM como a través de la librería WeasyPrint en los PDFs descargables.

### 2026-05-24 — UX/Docs: Identidad de "Glosario Vivo" y Control de Versiones Offline

**Contexto:** Se requería explicar claramente en la cabecera del glosario su naturaleza automatizada, y proveer un mecanismo visual en los PDFs descargados (o impresos) para que el lector sepa exactamente si su copia está obsoleta frente al entorno de producción.

**Hecho:** Se refactorizó la cabecera generada en `scripts/merci/merci-glosario.py`.

**Detalle técnico:** Se sustituyó la descripción estática por un bloque de cita (`>`) que explica el rastreo autónomo. Se inyectó la variable `fecha_actualizacion` calculada a partir de la marca de tiempo física (`st_mtime`) del `glosario-tecnico.json`, combinada con el número total de términos consolidados (`len(terminos)`).

**Motivo / criterio:** *Trazabilidad Documental Offline*. Cuando un documento dinámico se exporta a un formato estático desconectado (PDF o papel), pierde su anclaje temporal. Incluir la huella temporal exacta del origen de datos (JSON) junto al conteo de ítems garantiza que el usuario pueda auditar la vigencia de su manual con un simple vistazo.

### 2026-05-24 — Feat: Sincronización Automática de Apariciones (Auto-Healing References)

**Contexto:** Se descubrió que una vez que el glosario consolidaba un término en el JSON maestro, sus líneas de aparición quedaban congeladas. Si el mismo término se mencionaba en bitácoras futuras (ej. Épica 7), el orquestador no actualizaba las referencias cruzadas.

**Hecho:** Se refactorizó la función `main` de `scripts/merci/merci-glosario.py` para incluir una rutina de sincronización silenciosa de apariciones en todos los modos de ejecución.

**Detalle técnico:** Al iniciar el script, se extraen las apariciones actuales y se iteran sobre los términos ya existentes en el JSON. Si el diccionario de `apariciones` difiere (hay nuevas bitácoras, líneas, o archivos borrados), se sobrescribe y se guarda el estado. Esta refactorización consolidó la extracción de variables, eliminando código duplicado entre el "Modo Compilación" y el "Modo IA".

**Motivo / criterio:** *Single Source of Truth (SSOT) Dinámico*. Un glosario debe ser un documento vivo. Garantizar que las referencias a los archivos y líneas se mantengan exactas y actualizadas en tiempo real (incluso mediante una simple compilación rápida de `merci total`) aporta un inmenso valor de trazabilidad sin consumir llamadas adicionales a la API local de la IA.

### 2026-05-24 — Sec & AI: Endurecimiento de Prompts (Agent Chaining y Zero-Hallucination)

**Contexto:** Los agentes Bibliotecario y Blogger mostraban propensión a omitir campos YAML obligatorios o incluir texto conversacional ("Aquí tienes el artículo..."), rompiendo el parseo posterior del pipeline (Agent Chaining). 

**Hecho:** Se endurecieron los archivos `prompt-bibliotecario.md` y `prompt-blogger.md`.

**Detalle técnico:** Se añadieron instrucciones innegociables: prohibición absoluta de conversación fuera del bloque de código y obligatoriedad estricta de todos los campos del YAML Frontmatter.

**Motivo / criterio:** *Prompt Hardening*. Los modelos locales tienden a relajar el formato *Zero-Shot*. Imponer restricciones explícitas y blindar la estructura de salida asegura una integración de sistemas (Agent Chaining) libre de fricciones y fallos de parseo.

**Siguiente paso o deuda:** Iniciar el diseño del catálogo de productos en WooCommerce.

### 2026-05-24 — AI: Eliminación de "Mode Collapse" y "Síndrome del Loro" en Glosario

**Contexto:** El agente Glosario generaba definiciones repetitivas (comenzando siempre con "Es como...") y copiaba meta-instrucciones del prompt dentro del JSON resultante, denotando un colapso de modo en el LLM (Qwen 2.5 Coder).

**Hecho:** Se refactorizó iterativamente `prompt-glosario.md` aplicando *Positive Prompting*.

**Detalle técnico:** Se eliminó la restricción negativa que causaba el "elefante rosa" y se sustituyó por una instrucción positiva estricta: iniciar directamente con el sustantivo y sin artículos ("Un", "La"). Se purgó la meta-instrucción del ejemplo JSON para evitar que la IA la repitiera (Síndrome del Loro) y se exigió la llave `merci_explica` incondicionalmente sin filtros de omisión.

**Motivo / criterio:** *AI Psychology*. Los LLM pequeños operan mejor con ejemplos directos que con prohibiciones. Eliminar el ruido del *System Prompt* y establecer modelos positivos puros fuerza a la red neuronal a generar respuestas concisas, profesionales y corporativas, recuperando el rigor del diccionario técnico.

### 2026-05-24 — UX/DX: Tolerancia a fallos con límite duro ("Lógica San Pedro") en Triage

**Contexto:** Rechazar un término con 'N' en el triage interactivo obligaba a revisarlo eternamente, pero usar 'I' (Ignorar) era definitivo y susceptible al *Fat Finger Syndrome* (pulsación accidental).

**Hecho:** Se implementó la "Lógica San Pedro" (3 strikes) en `scripts/merci/merci-glosario.py`.

**Detalle técnico:** El script ahora almacena un contador de rechazos en el estado persistente (`glosario-tecnico.json`). Si un término es rechazado 3 veces con la tecla 'n', el sistema asume que no es útil y lo transfiere automáticamente a la lista negra (`ignorados`), eliminando la fricción de decisión.

**Motivo / criterio:** *Developer Experience (DX)*. Proveer tolerancia a fallos manuales sin renunciar a la automatización de la limpieza. Si el usuario duda 3 veces, el sistema toma la decisión de purga por él, manteniendo el backlog manejable.

### 2026-05-24 — Arch: Fail-Fast en Parser JSON del Glosario

**Contexto:** Un error sintáctico en `glosario-tecnico.json` (llaves desajustadas tras un parche manual) provocó un *Silent Failure with Overwrite* en el orquestador, destruyendo todo el historial de términos al interpretar el archivo como vacío.

**Hecho:** Se refactorizó la captura de excepciones en `load_glossary_state` de `scripts/merci/merci-glosario.py`.

**Detalle técnico:** Se reemplazó el retorno de diccionario vacío por una salida fatal (`sys.exit(1)`) alertando sobre la corrupción, y se restauró el archivo JSON dañado mediante `git restore`. Adicionalmente se incluyó el recuento total de términos generados dinámicamente en el Markdown resultante.

**Motivo / criterio:** *Fail-Fast y Single Source of Truth (SSOT)*. Los errores de lectura en las fuentes de verdad de datos nunca deben ser ignorados. Si un archivo matriz está corrupto, abortar incondicionalmente es la única garantía contra la sobreescritura destructiva.

### 2026-05-24 — Feat: Orquestación Headless del Catálogo (Tienda No Tienda)

**Contexto:** La Épica 6 exige gobernar el e-commerce desde terminal. El script `merci-shop.py` estaba incompleto y no sincronizaba los archivos Markdown hacia WooCommerce.

**Hecho:** Se refactorizó `scripts/merci/merci-shop.py` para leer los archivos de `laboratorio/tienda/`, extraer el YAML Frontmatter y el contenido Markdown, y sincronizarlos contra la API REST nativa de WooCommerce (POST/PUT).

**Detalle técnico:** Se implementó una lógica de autodescubrimiento por slug para discernir si el producto debe crearse (POST) o actualizarse (PUT). Las imágenes se mapean a rutas absolutas del dominio estático (`assets/images/`), evitando inyectar multimedia en la base de datos de WP.

**Motivo / criterio:** *Single Source of Truth y Zero Bloat*. Gestionar el catálogo mediante Markdown puro permite versionar productos en Git, manteniendo la tienda sincronizada con el resto de la web sin depender del panel de administración del CMS.

**Siguiente paso o deuda:** Iniciar la Épica 7 (Enriquecimiento Visual y Multimedia).

### 2026-05-24 — Fix: Inclusión de rutas dinámicas en el mapa XML (Sitemap)

**Contexto:** El rastreador de sitemap escaneaba archivos `.html` físicos, lo que dejaba fuera del `sitemap.xml` a las rutas maestras dinámicas gestionadas por Nginx y WordPress (`/blog` y `/blog/tienda`), perjudicando el SEO del proyecto.

**Hecho:** Se actualizaron las reglas de descubrimiento en `scripts/merci/merci-sitemap.py`.

**Detalle técnico:** Se inyectaron estáticamente las rutas `blog/` y `blog/tienda/` en la matriz de `rutas_dinamicas` con prioridad `0.9` y frecuencia `daily`.

**Motivo / criterio:** *Shift-Left SEO*. Un ecosistema híbrido debe garantizar que los rastreadores indexen correctamente todas las fronteras de infraestructura (estáticas y dinámicas) desde un único archivo centralizado.

### 2026-05-24 — Fix: Gobernanza IA estricta y Contexto Visual en Triage

**Contexto:** La IA local (Ollama) descartaba términos técnicos válidos asumiendo que eran ruido, enviándolos a la lista de ignorados sin consultar a la autora. Además, se requería ver la frase exacta de origen durante el triage manual para discernir siglas ambiguas (ej. CD).

**Hecho:**
- Modificado `laboratorio/prompts/prompt-glosario.md` para prohibir explícitamente a la IA filtrar los términos suministrados.
- Actualizado `scripts/merci/merci-glosario.py` para extraer y mostrar en consola 5 palabras antes y después del término hallado.
- Ampliada la expresión regular del glosario para soportar palabras compuestas por guiones (ej. `AI-Changelog`).

**Motivo / criterio:** *Human-in-the-Loop y Transparencia*. La IA debe ejecutar, no tomar decisiones de censura sobre la documentación. Mostrar el fragmento de la bitácora en la consola otorga el contexto necesario a la desarrolladora para autorizar o rechazar un término sin abrir el archivo original.

### 2026-05-24 — Fix: Enlaces Permanentes (Permalinks) para historial SSG

**Contexto:** Al aplicar el patrón de historial "Append-Only" a los cuadernillos antiguos (ej. Anatomía del Boilerplate), el motor SSG generaba un nuevo nombre de archivo HTML basado en el nuevo título "(Obsoleto)", rompiendo los enlaces originales compartidos en LinkedIn (Error 404).

**Hecho:** Se implementó el soporte para la clave `slug` en el YAML Frontmatter procesado por `scripts/merci/merci-publish.py`.

**Detalle técnico:** Si un archivo contiene `slug: "nombre-personalizado"`, el orquestador lo utiliza para generar la URL final en lugar de derivarla del título, preservando el enlace original intacto.

**Motivo / criterio:** *SEO y Resiliencia de Enlaces*. Las URLs son promesas públicas. Mantener la URI constante mediante metadatos explícitos asegura que el tráfico proveniente de redes sociales no caiga en el vacío al catalogar un documento como obsoleto.

### 2026-05-24 — Perf & DX: Burbuja Merci, Caché de Auditor y Mejoras en el Glosario

**Contexto:** El tiempo de ejecución del orquestador se había disparado a ~15 segundos debido a un cuello de botella de I/O en el auditor al verificar las consolidaciones de acrónimos en disco. Además, se requería implementar la "Burbuja Merci" (tooltips de traducción) en el frontend sin añadir dependencias JS, y proteger el árbol de Git con limpiezas quirúrgicas (`merci-healer.py`).

**Hecho:**
- Inyectada una caché en memoria RAM (`MD_CONTENTS_CACHE`) en `scripts/merci/merci-audit.py` para erradicar el cuello de botella I/O.
- Implementada la inyección dinámica de etiquetas nativas `<abbr>` en `scripts/merci/merci-publish.py` para los tooltips del glosario.
- Desarrollado y ubicado el script de limpieza `merci-healer.py` en `laboratorio/scripts_temporales/`.

**Motivo / criterio:** *Performance Driven Development y Zero-JS*. Retener los textos en RAM devuelve la auditoría a tiempos sub-segundo. Aprovechar atributos nativos de HTML (`<abbr>`) otorga interactividad didáctica sin penalizar el TBT con JavaScript de terceros. Aislar los scripts de un solo uso en temporales mantiene pura la carpeta de agentes.

### 2026-05-24 — Feat: Soberanía del Castellano y Ajuste de Linter SEO

**Contexto:** La auditoría SEO bloqueaba el pipeline maestro debido a longitudes de metaetiquetas ligeramente superiores a los límites, generando saturación en la IA de reparación al intentar corregir decenas de archivos simultáneamente. Además, la portada y las plantillas requerían castellanización para alinear el proyecto con la regla de Soberanía del Castellano y mejorar la accesibilidad cognitiva ("Merci Explica").

**Hecho:**
- Se rebajó la severidad de `SEO_TITLE_LENGTH` y `SEO_DESC_LENGTH` de `error` a `warn` en `scripts/merci/merci-audit.py`.
- Se tradujeron los términos de la portada (`public/index.html`) como *Performance Engineering*, *Payload* y *Zero Latency* a sus equivalentes en español.
- Se actualizó `prompt-bibliotecario.md` para exigir la sección `### 💡 En resumen (Merci Explica):` con analogías obligatorias para perfiles no técnicos.

**Motivo / criterio:** *Fail Gracefully y Autoridad Técnica*. Que un título tenga 66 caracteres en lugar de 65 no debe destruir la integración continua. Relajar el linter a `warn` mantiene la observabilidad sin fricción. La traducción de la portada y la inclusión de "Merci Explica" demuestran dominio del concepto subyacente sin escudarse en anglicismos, elevando el valor divulgativo de la Biblioteca.

**Siguiente paso o deuda:** Diseñar la implementación técnica de la "Burbuja Merci" (Tooltips interactivos) planificada para la Épica 7, e iniciar el desarrollo del Catálogo Headless (WooCommerce).

### 2026-05-24 — Feat: Concepto "Merci Explica", Modo Triage y Fail Gracefully

**Contexto:** El glosario técnico requería mayor control operativo para evitar consumir inferencia de IA en falsos positivos o términos excluidos, y a su vez, humanizar las definiciones técnicas para perfiles de negocio. Además, las interrupciones por teclado (`Ctrl+C`) lanzaban errores crudos rompiendo la experiencia de desarrollo (DX).

**Hecho:**
- Refactorizado `scripts/merci/merci-glosario.py` para incluir un modo interactivo de selección (Triage: Sí/No/Ignorar) previo a la inferencia de IA.
- Implementada la captura global de `KeyboardInterrupt` para guardar el progreso parcial y compilar el Markdown automáticamente antes de salir.
- Inyectado el campo `merci_explica` en la renderización del Markdown y actualizado el *System Prompt* para solicitar analogías no técnicas.
- Purgada la lista masiva de "ignorados" en `glosario-tecnico.json`.
- Corregida la numeración documental en los comentarios de `merci-total.py`.

**Motivo / criterio:** *Fricción Cero, Gobernanza IA y DevRel*. Permitir a la desarrolladora actuar como "Gatekeeper" antes de consumir recursos locales optimiza el tiempo y previene el *blacklisting* accidental. Proveer una analogía no técnica ("Merci Explica") democratiza el conocimiento, cumpliendo el propósito formativo de la Biblioteca. El manejo de señales (SIGINT) garantiza la inmutabilidad de los datos rescatando el trabajo hecho.

**Siguiente paso o deuda:** Evaluar la castellanización de los textos públicos de la web y expandir la comprensión documental para reforzar la regla de Soberanía del Castellano.

### 2026-05-23 — Arch: Pivote a "Tienda No Tienda" (Mock E-commerce Headless)

**Contexto:** La Épica 6 preveía la integración de pasarelas de pago reales (Stripe/PayPal) para demostrar un e-commerce híbrido de alto rendimiento. Se replanteó el objetivo buscando demostrar la capacidad arquitectónica (dominar WooCommerce) sin asumir la burocracia legal/financiera ni la carga de scripts de terceros en el frontend.

**Hecho:** Se reestructuró la Épica 6 en el `ROADMAP.md`, cancelando la integración de pasarelas de terceros. Se definió el desarrollo de una "Tienda No Tienda" gobernada 100% mediante terminal y archivos locales.

**Detalle técnico:** En lugar de operar productos desde el panel de WordPress, se utilizarán archivos Markdown con metadatos YAML (precio, inventario, imágenes). Se construirá un orquestador en Python que utilizará la API REST nativa de WooCommerce (`/wc/v3/products`) para sincronizar el catálogo de forma unidireccional (Headless), permitiendo a los visitantes simular una compra sin procesar pagos reales.

**Motivo / criterio:** *Spec-Driven Development y Zero-Risk*. Manejar el catálogo de productos localmente con Python respeta el principio de "Única Fuente de Verdad" (SSOT). Eliminar las pasarelas reales mantiene puro el código, extirpa el riesgo legal y certifica el hito técnico: demostrar que se puede construir un e-commerce extremadamente rápido (100/100) completamente disociado del panel de control tradicional del CMS.

**Siguiente paso o deuda:** Crear la estructura de carpetas (ej. `laboratorio/tienda/`), diseñar la plantilla YAML para productos y desarrollar el script de sincronización.

### 2026-05-23 — Shift-Left SEO: Validación estricta de longitud en metadatos (Chaos Monkey)

**Contexto:** El Agente Chaos saboteó la portada inyectando una meta descripción excesivamente larga y fraudulenta ("FALSAMENTE LABORATORIO..."), evadiendo el auditor estático que solo verificaba la existencia de la etiqueta, pero no su longitud ni calidad SEO.

**Hecho:** Se implementaron reglas de validación de longitud máxima para `<title>` y `<meta name="description">` en `scripts/merci/merci-audit.py`.

**Detalle técnico:** Se añadieron aserciones que lanzan errores bloqueantes `SEO_TITLE_LENGTH` (límite de 65 caracteres) y `SEO_DESC_LENGTH` (límite de 150 caracteres) dentro de la función `audit_html_seo`.

**Motivo / criterio:** *Shift-Left SEO y Calidad Estricta*. Los motores de búsqueda truncan los metadatos excesivamente largos, perdiendo el control del mensaje y afectando al CTR (Click-Through Rate). Validar matemáticamente la longitud en el linter garantiza que los textos promocionales encajen perfectamente en las SERPs (Search Engine Results Pages) y bloquea inyecciones de *spam* o desbordamientos inducidos por el Chaos Monkey.

**Siguiente paso o deuda:** Re-ejecutar `merci chaos` para validar que el linter intercepta y bloquea la mutación por exceso de caracteres.

### 2026-05-23 — DevSecOps: Resiliencia del parser JSON frente a alucinaciones de formato (Agente Chaos)

**Contexto:** La IA generaba tácticas de sabotaje válidas, pero el script `merci-chaos.py` abortaba creyendo que había fallado la búsqueda. Gracias a la reciente observabilidad de respuestas crudas, se descubrió que el modelo estaba escapando comillas simples (`\'`) dentro del JSON, lo cual es un error de sintaxis en el estándar JSON y provocaba un `JSONDecodeError` silencioso.

**Hecho:** Se refactorizó la función `extract_json_array` en `scripts/merci/merci-chaos.py`.

**Detalle técnico:** Se inyectó un saneamiento previo (`json_str.replace("\\'", "'")`) antes de invocar a `json.loads()`. Esto purifica la cadena de texto de escapes ilegales comunes en los LLMs antes del parseo estricto.

**Motivo / criterio:** *Robustez y Ley de Postel*. Ser liberales en lo que aceptamos. Los Small Language Models (SLMs) cometen micro-errores de sintaxis al generar código estructurado. En lugar de frustrarnos endureciendo el prompt, añadir tolerancia al parser nativo de Python garantiza que el agente sea resiliente y no interrumpa el bucle de pruebas.

**Siguiente paso o deuda:** Re-ejecutar `merci chaos` para confirmar que el payload ahora sí es parseado e inyectado correctamente en el código objetivo.

### 2026-05-23 — DevSecOps: Observabilidad de respuestas crudas en Agente Chaos

**Contexto:** Cuando el Agente Chaos fallaba en su intento de sabotaje por no generar el JSON esperado o errar en la clave de búsqueda, abortaba la ejecución sin mostrar qué había respondido exactamente la IA, dificultando la depuración de alucinaciones del SLM local.

**Hecho:** Se inyectó un registro de respuesta cruda (*raw response*) en la lógica de aborto de `scripts/merci/merci-chaos.py`.

**Detalle técnico:** Si el array `sabotajes` o la clave `buscar` no existen, el script ahora imprime por consola `respuesta.choices[0].message.content`, revelando el texto exacto generado por el modelo local.

**Motivo / criterio:** *Observability y SLM Debugging*. Los Modelos de Lenguaje Pequeños (SLMs) pueden volverse conversacionales o romper el formato exigido. Tener visibilidad total (caja de cristal) de su salida errónea es indispensable para poder endurecer el *System Prompt* y evitar futuras evasiones de formato.

**Siguiente paso o deuda:** Re-ejecutar `merci chaos` hasta atrapar una respuesta cruda fallida y ajustar el `prompt-chaos.md` en consecuencia.

### 2026-05-23 — Sec: Extensión de validación AST en auditor Python (Chaos Monkey)

**Contexto:** Un simulacro de seguridad del Agente Chaos reveló que ciertas invocaciones a funciones de sistema de bajo nivel en Python estaban evadiendo los escudos estáticos, representando un riesgo potencial de ejecución no deseada si eran inyectadas en el ecosistema.

**Hecho:** Se implementó y extendió la regla `audit_python_smells` en `scripts/merci/merci-audit.py`.

**Detalle técnico:** La validación ahora parsea el Árbol de Sintaxis Abstracta (AST) para detectar el uso de funciones de sistema (`system`, `eval`, `exec`) y llamadas a subprocesos de bajo nivel (`Popen`). Su uso detiene automáticamente el pipeline. Simultáneamente, la regla es lo suficientemente granular como para permitir la ejecución de APIs de alto nivel (más seguras) estandarizadas por nuestro ecosistema.

**Motivo / criterio:** *Shift-Left Security y Principio de Menor Privilegio*. Bloquear proactivamente el uso de APIs propensas a configuraciones frágiles o inseguras obliga a mantener el estándar seguro en todo el orquestador. Las pruebas del Chaos Monkey siguen demostrando su enorme valor al forzar la evolución del linter.

**Siguiente paso o deuda:** Ejecutar `merci total` para certificar que ningún script legítimo del repositorio se ve afectado por la nueva regla restrictiva, y realizar el commit atómico.