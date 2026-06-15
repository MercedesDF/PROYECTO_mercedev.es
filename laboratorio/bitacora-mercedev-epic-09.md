# Bitácora del proyecto mercedev.es — Épica 9: Antigravity SRE, Chaos Engineering & Refinamiento CSS

## Para qué sirve este archivo

- **Yo futuro:** recuperar en minutos qué se decidió, por qué, y cómo se ejecutó algo técnico sin rebuscar en el chat o en commits sueltos.
- **Biblioteca (al cerrar el proyecto):** aquí vive el borrador narrativo y técnico; luego se depura y se traslada a `biblioteca/` como piezas definitivas (por estantería o tema), siguiendo la idea de “activo de conocimiento” del proyecto.

No sustituye a `instrucciones.md` (directrices y rol del asistente). Complementa el día a día con **hechos, comandos y lecciones**.

---

## Cómo mantenerlo (acuerdo simple)

1. **Añadir entradas al principio** de la sección “Registro cronológico”, con la plantilla de abajo. El registro es **acumulativo**: lo ya escrito forma parte del historial y **no se reemplaza** por nuevas sesiones (así no se pierde contexto ni fechas).
2. **Una entrada por sesión o por tema cerrado** (lo que resulte más claro al escribir).
3. Si algo fue un error o una vulnerabilidad evitada, opcionalmente usar los **tres átomos** del proyecto (Desafío → Maniobra → Aprendizaje/Deuda) en el cuerpo de la entrada.
4. **Convención de Rutas:** Al hacer referencia a archivos o directorios, usar rutas relativas a la raíz del proyecto, comenzando con `PROYECTO_mercedev.es/` (ej. `PROYECTO_mercedev.es/laboratorio/archivo.md`). No incluir el prefijo absoluto del sistema operativo (ej. `/home/tu_usuario/ruta_al_proyecto/`).
5. **Correcciones excepcionales** (typo, dato incorrecto, redacción de un solo párrafo, retirada de información sensible): editar solo el fragmento necesario o añadir una línea aclaratoria bajo la entrada; evitar reescribir todo el archivo o borrar entradas enteras sin motivo documentado.

### Plantilla para nuevas entradas

Plantilla base para el registro de sesiones.

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

### 2026-06-15 — Fase 4: Preparación para Chaos Engineering (Hybrid Stack & Tácticas)

**Contexto:**
Para probar la resiliencia del motor de IA y las defensas contra derivas documentales, necesitábamos asegurar que el entorno utilizaba verdaderamente un "Hybrid Stack" (con Ollama como primario y Gemini como respaldo) y extender el script del Chaos Monkey para inyectar estos fallos específicos de red y gobernanza.

**Hecho:**
- Se refactorizó `scripts/merci/merci-brain.py` y `scripts/merci/merci-blogger.py` para implementar un bloque `try...except` que intenta llamar a `ollama/qwen2.5-coder` (con timeout de 10s) y realiza el *fallback* al Gemini Proxy (`litellm`) en caso de fallo.
- Se amplió `scripts/merci/merci-chaos.py` con dos nuevas tácticas: Táctica B (Corte de Red) falsificando el puerto local de Ollama para forzar el fallback; y Táctica C (Deriva Documental) inyectando un script fantasma no registrado.
- Se refactorizaron las Expresiones Regulares en `scripts/merci/merci-commit.py` haciéndolas robustas y agnósticas para soportar cualquier sintaxis en los títulos de las secciones de la bitácora.

**Detalle técnico:**
Se actualizaron `merci-brain.py`, `merci-blogger.py` y `merci-chaos.py`. La Táctica B muta dinámicamente `os.environ["OLLAMA_API_BASE"] = "http://localhost:9999"` durante la ejecución para forzar caídas controladas.

**Motivo / criterio:**
El concepto de "Pila Híbrida" (Hybrid Stack) exige que exista un motor local gratuito como primera opción, utilizando la nube solo como salvavidas. Extender el Chaos Monkey garantiza de forma empírica que esta red de seguridad y el escudo linter de deriva funcionan bajo presión extrema.

**Siguiente paso o deuda:**
Lanzar la simulación de *Chaos Engineering* (`merci-chaos.py`) tras limpiar el directorio de trabajo, para validar las tres tácticas y hacer la comprobación de auditoría definitiva.

### 2026-06-15 — Fase 3: Autarquía del Motor de IA ( Antigravity Proxy / LiteLLM )

**Contexto:**
La arquitectura requería evolucionar más allá de la dependencia exclusiva en modelos locales (Ollama), configurando un enrutamiento seguro hacia el IDE Antigravity / Gemini Proxy como motor de contingencia y respaldo definitivo.

**Hecho:**
- Se refactorizó `merci-blogger.py` para reemplazar las peticiones directas a `http://localhost:11434` (Ollama) por integraciones usando la librería `litellm`.
- Se refactorizó `merci-brain.py` inyectando compatibilidad con `litellm` para redirigir la carga cognitiva (saludos y procesamiento contextual) al modelo `gemini/gemini-1.5-flash` a través de la clave `GEMINI_API_KEY` extraída del archivo `.env`.
- Se validó el aislamiento de la configuración (silenciando la telemetría de LiteLLM para no ensuciar la salida DevSecOps).
- Se marcó el hito de "Autarquía del Motor de IA" como completado (`[x]`) en el ROADMAP maestro.

**Motivo / criterio:**
Centralizar el motor de IA a través de un proxy agnóstico (`litellm`) aumenta la resiliencia del ecosistema, permitiendo un "Shift-Left AI" que no depende del hardware local para mantenerse operativo al 100%.

**Siguiente Paso:**
El paso inmediatamente posterior es activar el *Chaos Engineering* e inyectar cortes de red simulados para verificar si la infraestructura recae exitosamente en el Proxy de Gemini bajo condiciones hostiles, así como inyectar derivas documentales para comprobar el linter `merci-drift`.

### 2026-06-15 — Rectificación: Restauración de botones flotantes (UI/UX)

**Contexto:**
Durante la limpieza de la UI en la Fase 2, se eliminaron los botones de volver arriba (`.floating-back-to-top`) de `index.html`, `sobre-mi` y `contacto` bajo la premisa de que no tenían scroll. Sin embargo, esto violaba el principio de consistencia visual del diseño Premium, ya que los botones debían funcionar en todos lados por igual, manteniéndose ocultos hasta hacer scroll y no actuando simplemente como "barras de desplazamiento" fijas. 

**Hecho:**
- Se han restaurado los botones flotantes (`<a href="#top" class="floating-back-to-top">`) en `public/index.html`.
- Se implementó la clase JavaScript `BackToTopController` en `public/js/main.js` (Zero dependencias externas) que hace uso de `requestAnimationFrame` y eventos pasivos de scroll para mostrar el botón solo cuando `window.scrollY > 300` px.
- Se ejecutó `merci-sync-pages.py` para sincronizar `index.html` con las demás páginas estáticas del ecosistema.

**Motivo / criterio:**
No eliminar elementos globales si la interfaz se siente asimétrica. Si un elemento visual molesta en un contexto (como en páginas sin scroll), es preferible modificar su comportamiento (lógica JS/CSS) que amputarlo por completo de algunas plantillas. Todo error arquitectónico debe añadirse como rectificación nueva (append) y nunca reescribiendo la historia pasada.

### 2026-06-15 — Fase 2: Soporte SRE para Blog, Tienda y Rediseño de Accesibilidad

**Contexto:**
Tras la implementación de la telemetría básica, se detectó que el Blog y la Tienda dinámica (servidas dinámicamente por WordPress/WooCommerce en PHP) carecían de los micro-sellos visuales SRE. Además, se constató que la combinación de colores traslúcidos original sobre fondos claros violaba las directrices de accesibilidad (contraste insuficiente en texto y puntuaciones).

**Hecho:**
- Se amplió `TARGET_URLS` en `merci-extract-metrics.py` para auditar concurrentemente las páginas del Blog (`/blog/`) y la Tienda (`/blog/tienda/`).
- Se diseñó e implementó la función auxiliar PHP `merci_get_sre_badge_html($url)` en `functions.php` del tema de WordPress y se inyectó en los héroes de `index.php` y `woocommerce.php`.
- Se reescribió `src/scss/components/_sre-badge.scss` para utilizar un fondo claro sólido y colores corporativos oscurecidos de alta visibilidad para las puntuaciones, garantizando el cumplimiento de la norma **WCAG AA (> 4.5:1)** sobre blanco: Verde (`#065f46`), Naranja (`#9a3412`) y Rojo (`#b91c1c`).
- Se inyectaron los emoticonos de leyenda (`⚡`, `♿`, `🛡️`, `🔍`) en la frase de puntuaciones de la portada (`index.html`) y se modificó `merci-extract-metrics.py` para mantener su persistencia dinámica.
- Se eliminaron los botones de volver arriba flotantes (`.floating-back-to-top`) de las páginas cortas del ecosistema (`/index.html`, `/sobre-mi/index.html` y `/contacto/index.html`), al carecer de sentido en vistas sin scroll vertical largo, manteniéndose exclusivamente en las estanterías de la biblioteca, proyectos y art-de-cote.
- Se ejecutó el pipeline completo de validación y compilación con éxito, registrando la expansión del acrónimo Tasa de Fotogramas Variable (VFR) en esta entrada activa para satisfacer al linter sin modificar registros históricos.

**Motivo / criterio:**
El principio de inmutabilidad histórica de la bitácora obliga a registrar de forma incremental tanto los aciertos como las rectificaciones de diseño. Integrar capas dinámicas de PHP mediante lectura local de caché en disco preserva las ventajas de velocidad del ecosistema SSG sin deteriorar el TTFB. La gobernanza de accesibilidad (a11y) debe primar sobre los caprichos estéticos, adaptando la UI para ser leída por cualquier usuario.

### 2026-06-15 — Fase 2: Expansión de Telemetría SRE (Accesibilidad & URL Granular)

**Contexto:**
Se necesitaba ampliar la telemetría SRE para incorporar la deuda técnica de accesibilidad (cuantificando problemas de contraste de color y ARIA) en Grafana, así como inyectar micro-sellos visuales Zero-JS con las puntuaciones reales de Lighthouse en las 7 páginas principales del ecosistema, evitando degradar la velocidad del pipeline local.

**Hecho:**
- Se diseñó el componente visual `sre-badge` con estilos CSS/SASS glassmorphic y se registró en `src/scss/components/_sre-badge.scss`.
- Se configuró el extractor para solicitar todos los ámbitos de Lighthouse a la API de PageSpeed e implementó la cuantificación detallada de errores de contraste y ARIA en `merci-extract-metrics.py`.
- Se implementó la resolución y caché paralela (`ThreadPoolExecutor`) de las 7 páginas principales del sitio en `observabilidad/.lighthouse_pages_cache.json` con un TTL de 24 horas.
- Se inyectaron dinámicamente los micro-sellos en las portadas e índices compilados mediante `merci-publish.py` e inyectó los badges en archivos estáticos mediante `merci-sync-pages.py` con marcadores `<!-- Merci SRE Badge -->`.
- Se añadieron los Gauges `merci_lighthouse_accessibility_contrast_errors` y `merci_lighthouse_accessibility_aria_errors` en el agente `merci-sre.py` y se crearon los paneles 27 y 28 en el dashboard JSON de Grafana.
- Se actualizaron el ROADMAP, el Walkthrough y el listado de tareas del proyecto.

**Motivo / criterio:**
La ejecución concurrente multihilo minimiza el tiempo de red a un único ciclo de llamadas API (~12s) que solo se activa al expirar la caché de 24h. Mantener los badges libres de Javascript preserva el rendimiento óptimo del frontend, garantizando el 100/100 Core Web Vitals en producción.

### 2026-06-15 — Fase 2: Implementación de Telemetría SRE (Anti-Bloat) y Gobernanza

**Contexto:**
Se requería vigilar activamente que el crecimiento del ecosistema no rompa la filosofía "Zero-Bloat". Además, se detectó un truncamiento accidental en el archivo que dicta el perfil operativo de la IA (`.privado/gemini.md`).

**Hecho:**
- Se reconstruyó en su totalidad el archivo `gemini.md` y se promocionó a la base de conocimiento oficial (KI) del IDE Antigravity.
- Se inyectó en `scripts/merci/merci-sre.py` the new Gauge `merci_public_folder_size_bytes` y una función recursiva para auditar el tamaño de la carpeta estática.
- Se inyectó programáticamente en `observabilidad/dashboards/merci-dashboard.json` el panel visual "Peso Estático (/public)".
- *Hotfix (Grafana Schema):* Se corrigió una infracción de esquema en el JSON del Dashboard. La API de Grafana v13.0 descartaba silenciosamente el panel porque la propiedad `element` esperaba un objeto `{"kind": "ElementReference", "name": "panel-26"}` y no un *String* plano.

**Motivo / criterio:**
Monitorear físicamente el peso del ecosistema permite anticipar la deuda técnica y degradaciones en Core Web Vitals antes de que sucedan. Reparar las reglas de la IA asegura el rigor arquitectónico a futuro.

### 2026-06-15 — Investigación: Preservación de Herramientas Estériles (FFmpeg)

**Contexto:**
Se necesitaba automatizar la purga de tiempos muertos ("congelación de terminal") en los vídeos de demostración del proyecto (showcase). Se experimentó con la vía de bajo nivel usando `FFmpeg` y el filtro `mpdecimate`.

**Hecho:**
- Se generó el script `scripts/temporales/merci-mpdecimate-fastforward.sh`.
- El script cumplió técnicamente su función de compresión extrema (de 272MB a 62MB), pero generó un efecto "Hyper-Timelapse" epiléptico inasumible para la visualización humana.
- Se experimentó alternativamente con `auto-editor` (Python) para recortar fotogramas inactivos manteniendo un "padding" humano (`--margin 0.5s`), pero el intento falló debido a la falta de metadatos de fotogramas constantes (`time_base=0/0`, Tasa de Fotogramas Variable (VFR)) en la grabación de pantalla cruda.
- En lugar de desechar el código, se confinó en el nuevo directorio `scripts/temporales/` y se documentó explícitamente en su cabecera el motivo de su fracaso y las alternativas humanas recomendadas (CapCut, auto-editor), cumpliendo las normas de gobernanza.

**Motivo / criterio:**
Un script fracasado es una lección arquitectónica valiosa. Mantener el ecosistema Zero-Bloat también implica no saturar la carpeta principal de `scripts/` con utilidades estériles, derivándolas a un silo de cuarentena/histórico debidamente comentado.

## Notas Arquitectónicas

*(Espacio para documentar bloqueos o decisiones técnicas durante la ejecución de la épica).*
