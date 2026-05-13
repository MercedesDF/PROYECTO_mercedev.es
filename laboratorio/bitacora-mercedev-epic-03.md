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

**Hecho:** Se refactorizó `scripts/merci/merci-linkedin.py` como un "Gatekeeper" y se inyectó el metadato `estado_social: "en_cola"` en las plantillas Markdown base (`plantilla-blog.md`, `plantilla-art-de-cote.md`).

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
