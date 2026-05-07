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
