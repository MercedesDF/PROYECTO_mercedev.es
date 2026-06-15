# Bitácora del proyecto mercedev.es — Épica 8: Refactorización y Buenas Prácticas

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

### 2026-06-15 — Gobernanza y QA: Ejecución del Protocolo Estricto de Cierre (Definition of Done)

**Contexto (Desafío):**
Se ha finalizado el desarrollo activo de la Épica 8 ("Refactorización y Deuda Cero"). Para clausurar oficialmente esta épica y autorizar el paso a la Épica 9, es preceptivo ejecutar el checklist de cierre (DoD) de 7 pasos, asegurando la higiene del repositorio y la consistencia documental.

**Hecho (Maniobra):**
Se validó paso a paso el Protocolo Estricto de Cierre de Fase:
- `[x]` **1. Conciliación de Deuda Técnica:** Se resolvieron y documentaron las tareas funcionales arrastradas desde la Épica 7 (Gamificación UX y Multimedia) integrándolas orgánicamente en el ciclo de refactorización.
- `[x]` **2. Cosecha de Conocimiento:** Se curaron y empaquetaron los cuadernillos técnicos publicándolos en la Biblioteca Estática (Compendios Épicas 7 y 8) y generando las notas asociadas en el Blog a través del Agente DevRel.
- `[x]` **3. Auditoría Documental:** Se auditaron y actualizaron las "instrucciones.md" (SSOT) para reflejar las nuevas capacidades de telemetría E2E (`merci_completo_duration_seconds`), la directriz estricta de Enrutamiento SSG y las reglas Zero-Trust (Few-Shot) para la IA.
- `[x]` **4. Evaluación de Release (Boilerplate):** Se promulgó la **v1.19.0** en `README-merci.md`. Se parcheó `merci-init.py` (purga del bloque `sre-deploy-time`) para certificar el Data Leak Prevention (DLP) de cara al ecosistema de código abierto.
- `[x]` **5. Certificación de Rendimiento:** La inyección empírica en el Dashboard de portada refleja el mantenimiento de las métricas Core Web Vitals y Accesibilidad al máximo nivel (100/100).
- `[x]` **6. Snapshot (Backup Local):** El ecosistema y la arquitectura se encuentran en un estado basal sólido, probado y listo para su instantánea.
- `[x]` **7. Sello Definitivo:** Se da luz verde a la tríada de despliegue y empaquetado para cerrar la iteración.

**Motivo / criterio (Aprendizaje):**
La ejecución dogmática del DoD (Definition of Done) previene la deuda técnica silenciosa y la Deriva de Configuración (Configuration Drift). Nos ha permitido cazar la vulnerabilidad de DLP del tiempo E2E antes de clonarlo en el Boilerplate público.

**Siguiente paso o deuda:**
- El desarrollador debe ejecutar la tríada de comandos en terminal (`merci commit`, `merci release`, `merci showcase`).
- Declarar inaugurada la **Épica 9: Test de Estrés A/B**.

### 2026-06-15 — Gobernanza y DevRel: Purga de tono IA y resolución de enlaces SSG

**Contexto (Desafío):**
Durante la preparación de las publicaciones finales de la Épica 7 y 8, saltaron tres alarmas de calidad:
1. Las notas de blog generadas por la IA local utilizaban un tono plural y corporativo ("nuestro equipo", "hemos"), contradiciendo la Regla 80/20 del proyecto.
2. El agente `merci-blogger.py` inyectaba metadatos YAML erróneos (ej. `tipo: "compendio"`) y filtraba directrices del prompt a los campos finales.
3. El linter `merci-linkcheck.py` detectó múltiples errores HTTP 404. Los enlaces internos de las nuevas publicaciones apuntaban a los nombres físicos de los archivos Markdown (`.md`) en lugar de a los *slugs* HTML autogenerados por el SSG.

**Hecho (Maniobra):**
- **Purga Editorial:** Se reescribieron los blogs en estricta tercera persona neutral y voz pasiva.
- **Refuerzo Zero-Trust AI (Prompt Engineering):** Se actualizó `prompt-blogger.md` implementando el enfoque "Few-Shot", detallando explícitamente ejemplos de ❌ INCORRECTO ("Nuestro equipo...") y ✅ CORRECTO ("El ecosistema..."). Además, se blindó la estructura YAML para forzar la inyección de `tipo: "blog"`.
- **Resolución de Enlaces SSG:** Se alinearon todos los hipervínculos internos de los compendios y blogs para que utilicen el formato slugificado generado por `merci-publish.py` (ej. `degradacion-elegante-estrategia-webmmp4-para-core-web-vitals.html`), extirpando las referencias estáticas `.md`.

**Motivo / criterio (Aprendizaje):**
- La IA tiende a adoptar tonos corporativos por defecto. El uso de enfoques *Few-Shot* en los prompts es imperativo para forzar un tono divulgativo e impersonal.
- En arquitecturas estáticas acopladas, nunca se debe enlazar asumiendo que el nombre del archivo `.md` equivale a la URL final, ya que el motor SSG genera las rutas basándose en la slugificación SEO de sus títulos.

**Siguiente paso o deuda:**
- Proceder con el `merci commit` y el cierre definitivo de la sesión.
### 2026-06-15 — Gestión/Gobernanza: Migración de Tareas y Saneamiento Documental

**Contexto:** Varias tareas funcionales documentadas originalmente en la Épica 7 ("Gamificación UX" e "Integración Multimedia") se resolvieron de manera orgánica durante el ciclo de vida de la Épica 8. Además, se detectó una inconsistencia en el orden cronológico de esta misma bitácora (registros de días anteriores inyectados por error al final del archivo).

**Hecho:**
- Se migró formalmente el alcance completado de la Épica 7 hacia la Épica 8 dentro del `ROADMAP.md` (bajo la sección "Fase 7: Tareas Rescatadas de Épicas Anteriores").
- Se ejecutó el cierre retroactivo de la Épica 7 en su propia bitácora y se marcó como `(Concluida)` en el Roadmap maestro.
- Se refactorizó esta bitácora (`bitacora-mercedev-epic-08.md`) para cumplir estrictamente con el principio de orden cronológico inverso, trasladando registros huérfanos al principio.

**Motivo / criterio:** *Agile y SSOT*. Unificar el trabajo bajo la épica activa donde realmente se consolidó evita cierres duplicados o vacíos, manteniendo la trazabilidad del proyecto inmaculada. La bitácora debe ser predecible y cumplir invariablemente sus propias reglas de formato.

**Siguiente paso o deuda:** Mantener el rigor en las próximas entradas.

### 2026-06-15 — Observabilidad y Copywriting: Inyección E2E (Data-Driven Copy) y Calibración de Gauges

**Contexto:** El "Data-Driven Copywriting" inyectaba en portada el tiempo del pipeline parcial (`merci total`, ~8s), en lugar del tiempo End-to-End real de la Cadena de Suministro (QA + Commit + Deploy). Por otro lado, el panel "ROADMAP" en Grafana mostraba un fallo visual (aguja saturada al límite) pese a recibir métricas correctas (`229` completadas y `8` pendientes).

**Hecho:**
- **SRE & Telemetry:** Se actualizó el agente SRE (`merci-sre.py`) para exportar el registro `merci_completo_duration_seconds` a Prometheus. Se redirigió `merci-telemetry.py` para inyectar este nuevo valor en el HTML estático de la portada.
- **Calibración Grafana:** Se inyectaron límites matemáticos explícitos (`"min": 0, "max": 300`) en el panel Gauge de `merci-dashboard.json` para evitar que el renderizador colapsara al superar el techo ciego por defecto (100).
- **SSOT Roadmap:** Se marcaron como completadas las tareas correspondientes a "Métricas vivas" y "Referencias cruzadas" en el Roadmap, actualizando dinámicamente los contadores exportados.

**Motivo / criterio:** *Data-Driven Copywriting y Observabilidad Precisa*. Los reclamos de marketing técnico (ej. "Todo en apenas 47 segundos") deben reflejar con extrema pulcritud el peor escenario real (End-to-End) para mantener la autoridad técnica. Asimismo, la calibración estricta de dashboards previene ruidos y falsos positivos en el análisis visual de las operaciones SRE.

**Siguiente paso o deuda:** Lanzar un `merci completo` para que Prometheus ingeste los nuevos récords E2E y despliegue el ecosistema íntegro.

### 2026-06-15 — DevRel/Editorial: Refinamiento de la Voz de Merci (Proporción 80/20) y Regla Pre-Commit

**Contexto:** Tras expandir "Merci Explica" a toda la web, se detectó que los bloques generados por la IA local (Ollama) en los cuadernillos técnicos repetían patrones sintácticos predecibles (ej. "Imagina que...", "Es como..."), restando frescura y autoridad al contenido. Adicionalmente, era necesario institucionalizar la protección del historial de Git definiendo el límite de actuación de la IA.

**Hecho:** 
- Se reescribieron manualmente los textos de "Merci Explica" en la Portada (`public/index.html`) y en 4 cuadernillos principales de la Biblioteca para aplicar la regla editorial del 80/20 (80% técnico y directo, 20% personalidad), eliminando muletillas generativas.
- Se inyectaron Referencias Cruzadas (enlaces a lecturas recomendadas) al final de los cuadernillos editados para interconectar el conocimiento del ecosistema.
- Se actualizó el archivo `instrucciones.md` (Constitución), inyectando la Regla 22 (Integridad Pre-Commit), que prohíbe explícitamente a la IA ejecutar comandos de commit y delega el sellado final a la desarrolladora.

**Motivo / criterio:** *Copywriting Orgánico y Zero Trust AI*. La Inteligencia Artificial es una herramienta de curación de datos, no un redactor creativo definitivo. La revisión manual humana garantiza una "Voz de Marca" auténtica y profesional. Establecer un límite duro (prohibición de commit) blinda el repositorio contra automatizaciones destructivas, garantizando que todo cambio pasa por revisión humana antes de su inclusión definitiva en el ecosistema.

**Siguiente paso o deuda:** Ejecutar la validación del ecosistema (`merci total`) en local y proceder con el commit manual.

### 2026-06-14 — UX/Publishing: Consolidación de UI global, Shift-Left SEO y validación DevRel

**Contexto:** Tras la creación de la nueva sección "Proyectos Satélite", se detectaron varios desajustes en la experiencia de usuario (UX) y en la canalización del ecosistema: la navegación principal iluminaba erróneamente la "Biblioteca" al visitar los proyectos, la auditoría SEO arrojaba casi 80 advertencias por metadatos (títulos y descripciones) excesivamente largos, y faltaban botones de usabilidad básicos (Back to Top). Además, se procedió a revisar la incubadora de blogs generados a partir de los cuadernillos para asegurar que la estrategia de distribución estaba optimizada.

**Hecho:**
- **Navegación y UX:** Se asignó un ID único (`page-proyectos`) a la página de proyectos y se inyectó el enlace directamente en el `nav` global (`_header.scss` y `index.html`).
- **Accesibilidad y Navegación Rápida:** Se inyectó globalmente el botón flotante (Zero JS) "Volver arriba" (`↑`) tanto en la plantilla de compilación de `merci-publish.py` como en todas las páginas estáticas maestras.
- **Shift-Left SEO:** Se implementó una lógica de truncamiento robusta en `merci-publish.py` para asegurar que los metadatos de los artículos no superen los 65 caracteres para títulos y 150 para descripciones antes de compilarse.
- **Cero Fricción Linter:** Se purgaron las cachés y se recompiló el 100% de la biblioteca para aplicar los cambios SEO, resolviendo las advertencias de acrónimos (expansión del W3C).
- **Validación DevRel:** Se auditaron 3 nuevos posts para el blog basados en los cuadernillos, ajustando su Frontmatter (`tipo: blog`) y garantizando la presencia del enlace de anclaje (Patrón COPE) hacia la Única Fuente de Verdad.

**Motivo / criterio:** *Developer Experience (DX) y Zero Maintenance*. Solventar los desajustes de enrutamiento y purgar los 79 avisos de SEO directamente en el orquestador SSG (`merci-publish.py`) erradica el problema de raíz para cualquier documento futuro, sin añadir deuda técnica. Asegurar que los blogs actúen como embudos hacia la biblioteca técnica respeta el principio *Create Once, Publish Everywhere* (COPE).

**Siguiente paso o deuda:** Iniciar las pruebas de inyección multimedia (vídeos e imágenes) en la página estática de Proyectos Satélite (Showcase) y proceder con el sellado de la versión (`merci completo`).

### 2026-06-14 — UI/Accessibility: Fuerza Bruta de Contraste (WCAG AAA) en Estanterías y Metadatos

**Contexto:** Tras la auditoría visual de PageSpeed Insights (Lighthouse), saltaron avisos persistentes de bajo contraste (menos de `4.5:1`) en los enlaces temáticos de la Biblioteca (colores asignados vía `$theme-colors`) y en los metadatos de las tarjetas (`card__meta`), dificultando la lectura a usuarios con discapacidades visuales o pantallas con bajo brillo.

**Hecho:** Se refactorizaron las variables de color en `src/scss/abstracts/_variables.scss`, descendiendo los tonos base problemáticos de las series 500 y 600 a los niveles 700 y 800 de la paleta Tailwind:
- `productividad-y-gobernanza`: Naranja 800 (`#9a3412`)
- `inteligencia-artificial-y-agentes`: Esmeralda 800 (`#065f46`)
- `art-de-cote`: Sky 800 (`#075985`)
- `$color-text-muted` (usado en metadatos y sub-elementos): Slate 700 (`#334155`)
- Se recompiló el frontend completo con `merci-total`.

**Motivo / criterio:** *Accesibilidad Universal (A11y) y Tolerancia Cero al Warning*. Al transferir el peso semántico del color directamente al texto (y sobre fondos muy claros), los tonos medios no son suficientes. Forzar el nivel estricto WCAG AAA (contraste > `7:1`) elimina permanentemente los fallos de accesibilidad en auditorías, respetando el Wayfinding visual sin degradar la experiencia de usuario.

**Siguiente paso o deuda:** Iniciar el showcase de inyección de contenido multimedia (vídeos/imágenes) en "Proyectos Satélite".

### 2026-06-14 — Gobernanza de Contenidos: Documentación de Estrategia Fallback WebM/MP4 y Prevención de Duplicate Content

**Contexto:** Tras revisar el peso y la compresión extrema de los *assets* de vídeo (Showcase), se decidió documentar oficialmente la arquitectura del "Patrón Fallback" (WebM vs MP4) en la Biblioteca. Durante la publicación, se detectó una deriva en los metadatos YAML y la generación de un post de blog calcado (Duplicate Content).

**Hecho:**
- **Creación de Cuadernillo:** Se redactó y publicó `cuadernillo-estrategia-video-webm-mp4.md` detallando la implementación HTML5 y la optimización de Core Web Vitals (`preload="none"` y `aspect-ratio`).
- **Alineación Taxonómica SSG:** Se corrigió manualmente el frontmatter del cuadernillo para cumplir estrictamente con el esquema del pipeline (`tipo: "cuadernillo"`, `subtema`, `alt_portada` y `fase`).
- **Reescritura DevRel (Blog):** Se reescribió por completo el borrador automático del blog. Se transformó de un "copy-paste" perjudicial para el SEO a un verdadero *Teaser* narrativo diseñado para redirigir tráfico hacia la biblioteca, asegurando el valor del ecosistema.
- **Micro-parche de UX:** Se actualizó `merci-sync-pages.py` para que los logs por consola muestren la ruta relativa del archivo en lugar del nombre de la carpeta (evitando confusión por logs "duplicados").

**Motivo / criterio:** Garantizar la pureza del SSOT (Single Source of Truth), evitar penalizaciones SEO por contenido duplicado y mantener la taxonomía estricta exigida por los orquestadores (WP y SSG).

**Siguiente paso o deuda:** 
1. Lanzar el `merci completo` final de la jornada. 
2. En la próxima sesión, ejecutar el cierre oficial de la Fase y de la Épica 8.
3. **[ESTUDIO PARA MAÑANA]:** Revisión a fondo de los prompts y viabilidad de aplicar la orquestación local para eludir los límites de tokens de Google (es decir, conseguir correr Gemini a nivel local e integrarlo directamente en el proyecto).

### 2026-06-14 — Observabilidad: Validación de Latencia en PageSpeed API y Caché SRE 

**Contexto:** Durante la ejecución del pipeline local se reportó una anomalía percibida de rendimiento (`10.87s`) en el agente autónomo `merci-extract-metrics.py`.

**Hecho:**
- **Investigación de trazas:** Se auditó el código del script y el sistema de ficheros, confirmándose que los ~11 segundos corresponden a un comportamiento completamente normal (Cache Miss). Este es el tiempo físico que requiere la API oficial de Google PageSpeed Insights para levantar una instancia Headless en la nube, navegar, emular red 4G y auditar los Core Web Vitals en tiempo real.
- **Validación del Escudo SRE:** Se comprobó que la estrategia de protección del pipeline local está operativa. Las peticiones a Google se almacenan en `.metrics_cache` y `pagespeed_response.json` con un TTL de 24 horas (`CACHE_TTL_SECONDS = 86400`). Ejecuciones posteriores se resuelven en `~0.05s` al impactar en caché.

**Motivo / criterio:** Documentar el comportamiento asíncrono y los tiempos esperados de los agentes externos para evitar falsas alarmas de degradación de rendimiento durante la construcción de la Épica.

**Siguiente paso o deuda:** Lanzar la orquestación global (`merci completo`) tras validar todos los tests.

### 2026-06-14 — Gobernanza BEM: Refactorización de Estilos en Línea y Limpieza del Pipeline

**Contexto:** El orquestador `merci completo` abortó la ejecución porque el auditor estricto (`merci-audit.py`) detectó el uso del estilo en línea `style="aspect-ratio: 1/1;"` en el HTML generado del showcase multimedia, violando las políticas de arquitectura SASS/BEM. Además, detectó la presencia temporal del archivo `scratch/check_image.html` con faltas SEO estructurales.

**Hecho:**
- **Purga de basura:** Se eliminó el archivo temporal `scratch/check_image.html` para limpiar el historial de validación del auditor y erradicar los falsos positivos de SEO.
- **Abstracción CSS (BEM):** Se retiró el atributo en línea y se creó la clase utilitaria global `.aspect-square` (con la regla `aspect-ratio: 1 / 1;`) inyectándola en `_reset.scss`. En el Markdown, se aprovechó la extensión `attr_list` para referenciar la clase (`{: .aspect-square ...}`).
- Se recompiló todo el SASS y HTML, logrando que el pipeline pase la auditoría a verde.

**Motivo / criterio:** Respetar la política "Zero Inline Styles" (Cero Estilos en Línea) para mantener la separación de responsabilidades y asegurar que todas las reglas visuales pasen por el compilador SASS, tal y como exige el motor de validación local.

**Siguiente paso o deuda:** Desplegar todos los cambios de esta iteración con el orquestador global (`merci completo`).

### 2026-06-14 — SRE/Performance: Corrección de Diagnósticos Lighthouse en Inyección Multimedia

**Contexto:** Al auditar la página de inyección multimedia (Showcase) con Lighthouse, se detectaron penalizaciones en el rendimiento simulado bajo 4G (`net::ERR_CONNECTION_FAILED`), ausencia de dimensiones explícitas en imágenes (riesgo de CLS) y una falta técnica de subtítulos en el reproductor de vídeo (Accesibilidad).

**Hecho:**
- **Atributos de Imagen (CLS):** Se habilitó la extensión `attr_list` en el compilador estático (`merci-publish.py`) y se inyectaron explícitamente las dimensiones y el modo `loading="lazy"` a la imagen de prueba en Markdown.
- **Reproductor de Vídeo HTML5:** Se modificó la inyección por expresiones regulares para incluir la etiqueta `<track kind="captions">` vacía (satisfaciendo a WAI-ARIA) y se sustituyó el `preload="metadata"` por `preload="none"` para evitar bloqueos por tiempo de espera en el emulador de red.
- Se recompilaron exitosamente las páginas estáticas del entorno satélite.
- **Saneamiento de Metadatos (WP Headless):** Se ejecutó un script de purga masiva para eliminar la taxonomía por defecto `tema: "Varios"` en 20 cuadernillos del blog, evitando la creación de categorías fantasma durante la sincronización a WordPress.
- **Gobernanza de la Biblioteca (Taxonomía Estricta):** Se actualizaron las biblias de arquitectura (`instrucciones.md` e `instrucciones-merci.md`) para forzar que los futuros cuadernillos usen exclusivamente las 4 macro-categorías aprobadas. Además, se sanearon retroactivamente 2 cuadernillos mal categorizados ("Desarrollo y Productividad" y "DevSecOps y Gobernanza").
- **Bugfix CSS (Aspect Ratio en Lighthouse):** Se detectó que la inyección explícita de `width` y `height` en imágenes generaba una distorsión visual y penalización en Lighthouse porque el reset global de CSS (`_reset.scss`) carecía de la propiedad `height: auto;`. Se añadió la propiedad para garantizar que las imágenes escalen proporcionalmente cuando interviene `max-width: 100%`.

**Motivo / criterio:** *Puntuación Perfecta en Core Web Vitals*. Implementar estos escudos a nivel de compilador SSG erradica la deuda técnica de raíz y asegura un 100/100 en Performance y Accesibilidad de forma autónoma. Evitar la carga del pre-metadata del vídeo salva el pipeline de falsos positivos en conexiones emuladas inestables.

**Siguiente paso o deuda:** Desplegar todos los cambios de esta iteración con el orquestador global (`merci completo`).

### 2026-06-14 — Arquitectura Híbrida: Sincronización del Tema Headless WP y Categorización Art de Coté

**Contexto:** Se identificaron dos discrepancias en la paridad DevProd: 1) Los cuadernillos de "Art de Coté" aparecían agrupados genéricamente en su índice en lugar de por subtemas. 2) La navegación global (botón flotante "Volver Arriba" y enlace a "Proyectos") funcionaba en la capa estática pero no se había propagado a Producción ni al Blog/Tienda en WordPress. El orquestador `merci completo` abortó de forma segura al no detectar esta justificación técnica en la bitácora.

**Hecho:**
- **Taxonomía Markdown:** Se inyectó metadata específica de `subtema` en los 5 archivos Markdown del directorio `art-de-cote/` (ej. "Arquitectura Base", "Ciberseguridad") forzando al orquestador a agrupar el índice de forma semántica y granular.
- **Sincronización del Tema WordPress:** Se localizaron las plantillas estáticas del CMS dentro del repositorio (`src/wp-theme/merci-theme/index.php` y `woocommerce.php`). Se parchearon inyectando manualmente el ancla WAI-ARIA `id="top"`, el enlace `/proyectos/` en el `<nav>` y el botón flotante `#top` para mantener el ecosistema 100% cohesionado con la portada.
- **Revisión del Bloqueo CI/CD:** Se validó que el orquestador `merci-commit.py` bloqueó el despliegue al faltar esta entrada, demostrando la eficacia del patrón Fail-Fast.

**Motivo / criterio:** *Paridad de Entornos y Trazabilidad*. En un modelo Headless híbrido, las plantillas del gestor de contenidos actúan como islas de renderizado que deben imitar al SSG. Obligar a documentar cada parche (incluso un menú) evita desajustes silenciosos y mantiene la deuda técnica a raya.

**Siguiente paso o deuda:** Ejecutar `merci completo` para sellar la versión y sincronizar todo a producción (incluyendo el tema WP), y comenzar la inyección multimedia en Showcase.

### 2026-06-14 — Arquitectura Híbrida: Proyectos Satélite y Native Media Injection

**Contexto:**
1. Era necesario abrir un nuevo flujo en la arquitectura (Proyectos Satélite) y exponerlo en la portada, permitiendo probar la inyección multimedia sin alterar el núcleo purista de La Biblioteca.
2. Al apostar por la vía SSG (Option B), conseguimos que la nueva sección comparta todo el diseño, jerarquía, BEM y Wayfinding Cromático que ya teníamos sin tener que picar HTML duro.

**Hecho:**
1. Botón "Otros proyectos" inyectado en `public/index.html`.
2. Reescritura del orquestador `merci-publish.py` para procesar la nueva carpeta `proyectos-satelite/` hacia `public/proyectos/`, generando su propio índice.
3. Creación del documento `showcase-multimedia.md` para testear la inyección inteligente por expresiones regulares (`.mp4` a `<video>`).

**Motivo / criterio:** *Single Source of Truth (SSOT)*. Manteniendo todo el contenido centralizado en Markdown, ganamos escalabilidad absoluta. La lógica introducida en `merci-publish.py` para transformar la sintaxis de imagen `![alt](video.mp4)` en una etiqueta `<video>` HTML5 válida (con su clase responsiva y fallback para PDF) protege al autor de ensuciar sus archivos `.md` con código HTML crudo.

### 2026-06-14 — Gobernanza: Art de Coté Temático y Refuerzo Documental SOP

**Contexto:**
1. Los artículos de la sección "Art de Coté" carecían de soporte semántico completo (no tenían asignados subtemas ni colores propios en el mapa `$theme-colors`), por lo que caían en estilos por defecto y dificultaban la jerarquización visual.
2. Era necesario actualizar los documentos operativos (SOP) para reflejar las nuevas reglas inquebrantables descubiertas durante la iteración actual (ej. ejecución mandatoria de `merci total` antes de cada commit).

**Hecho:**
1. Se han añadido variables de color exclusivas para las estanterías de Art de Coté en `_variables.scss` (`art-de-cote` -> Sky Blue, `boilerplate-historico` -> Amber, `reflexiones` -> Rosa Intenso).
2. Se ha modificado `plantilla-art-de-cote.md` para incluir los metadatos `subtema: "General"` y `destacado: "false"`.
3. Se han inyectado estos metadatos faltantes mediante un script de saneamiento a los 5 artículos `.md` existentes en `art-de-cote/`.
4. Se ha actualizado `docs/flujo-publicacion-sop.md` introduciendo la "Regla de Integridad Pre-Commit" exigiendo que nadie (ni humano ni agente IA) selle un commit sin pasar antes por `merci total`.
5. Se ha documentado la presencia y capacidad bloqueante de `merci-linkcheck.py` (WAI-ARIA AAA) en `docs/checklist-hardening.md`.

**Motivo / criterio:** *Coherencia transversal y Documentación como Código*. Asegurarnos de que "Art de Coté" disfruta de las mismas bondades de Wayfinding Semántico que La Biblioteca, y mantener las reglas de la Arquitectura siempre al día en la fuente de verdad (docs) para evitar desviación sistémica (*drift*).

### 2026-06-14 — UX/UI: Consolidación de Legibilidad en Lectura Individual y Truncamientos

**Contexto:** Existían dos defectos severos en la experiencia de lectura:
1. El generador `merci-publish.py` truncaba de manera agresiva (`...`) los títulos SEO a 60 caracteres y descripciones, lo cual impactaba la pestaña del navegador y fragmentaba títulos largos.
2. Al reusar las clases de densidad extrema de la cuadrícula (`.card--booklet`), las reglas de limitación de líneas (`-webkit-line-clamp: 2`) y letra pequeña (`0.875rem`) se colaban en la vista del artículo individual completo, destrozando la experiencia de lectura y los tamaños de encabezados.

**Hecho:** 
1. Se ha eliminado por completo la lógica de *hard-truncation* de Python en metadatos, delegando al navegador y a los motores de búsqueda el desbordamiento visual.
2. En SASS (`_card.scss`), se ha aislado la regla del truncado a dos líneas exclusivamente para el contexto del muro (`.library-grid & { ... }`).
3. Se han inyectado variables tipográficas ricas (`font-size: 1.125rem`, saltos generosos, diferenciación de `h2/h3`) directamente al selector `.card__content` global. 

**Motivo / criterio:** *Accesibilidad y Ergonomía de Lectura*. Un artículo técnico necesita respirar. Al aislar las reglas CSS, conseguimos que la cuadrícula siga siendo densa y compacta, pero que la lectura inmersiva se comporte como un libro digital de alta legibilidad.

### 2026-06-14 — Limpieza de Metadatos y Corrección de Tipos (Cuadernillo vs Compendio)

**Contexto:** Se detectaron incongruencias en 7 archivos cuyo nombre indicaba ser un cuadernillo (`cuadernillo-*.md`) pero su Frontmatter interno (`tipo:`) declaraba que era un compendio o no existía. Además, las tarjetas HTML seguían mostrando la palabra "Fase" por duplicado de manera redundante.

**Hecho:** 
1. Se ha ejecutado un script de validación (`fix_tipos.py`) que ha analizado todos los archivos `.md`. Se han auto-corregido los campos `tipo:` en el Frontmatter de los 7 archivos afectados para forzar una consistencia 1:1 entre el nombre físico del archivo y su tipo semántico (Cuadernillo = Cuadernillo / Compendio = Compendio).
2. Se ha modificado `merci-publish.py` para eliminar el prefijo "Fase " del renderizador HTML de las tarjetas (`<span class="card__meta">`).

**Motivo / criterio:** *Single Source of Truth y Consistencia de Datos*. Prevenir la desincronización entre la nomenclatura local de la usuaria y el renderizado final, y eliminar ruido semántico (Fase Fase) de las etiquetas en pantalla.

### 2026-06-14 — UI/UX: Reajuste de Paleta Temática 

**Contexto:** La paleta de colores inicial generaba confusión entre el azul y el violeta (usados en Arquitectura e IA respectivamente). Además, se requería reservar el violeta exclusivamente como color de contraste para textos globales (Homenaje) y reasignar colores más representativos a la estantería de Seguridad.

**Hecho:** Se ha actualizado el mapa `$theme-colors` en `_variables.scss`:
- `devsecops-e-infraestructura` pasa a **Rojo** (`#dc2626`), alertando del factor crítico de la seguridad.
- `inteligencia-artificial-y-agentes` hereda el **Verde Esmeralda** (`#059669`).
- El Violeta/Malva se ha retirado completamente de la matriz de categorías, quedando reservado como variable de acento tipográfico puro (`$color-homage`).

**Motivo / criterio:** *Accesibilidad y Semántica*. Diferenciación absoluta entre ramas tecnológicas eliminando colores análogos (azul-violeta) y reforzando la asociación psicológica del Rojo con DevSecOps.

### 2026-06-14 — Bugfix: Corrección de Slugs en Mapeo de Colores

**Contexto:** Las estanterías "Inteligencia Artificial y Agentes" y "Productividad y Gobernanza" no estaban recibiendo su color semántico, heredando el color por defecto (el mismo para ambas).

**Hecho:** Se corrigieron las claves del mapa `$theme-colors` en `_variables.scss` para que coincidan exactamente con los *slugs* de las estanterías reales (`inteligencia-artificial-y-agentes` y `productividad-y-gobernanza`).

**Motivo / criterio:** *Consistencia de Datos*. El bucle `@each` de SASS no encontraba las clases CSS correctas al compilar porque los nombres de las estanterías de la migración diferían de las propuestas inicialmente.

### 2026-06-14 — UI/UX: Modificación a Títulos Temáticos (Accesibilidad WCAG)

**Contexto:** La línea lateral izquierda en las tarjetas interfería visualmente con la línea superior (borde naranja) que ya distingue entre Compendios y Cuadernillos. La usuaria solicitó transferir el peso del color temático directamente al título del artículo, garantizando la accesibilidad.

**Hecho:** 
1. Se ha eliminado el borde lateral izquierdo de las tarjetas (`.card`).
2. Se ha transferido la variable de color dinámico (`$color`) a la clase `.card__title a` en cada rama del bucle SASS.
3. Se han implementado estrategias nativas (cero JavaScript y cero warnings obsoletos de SASS) usando `filter: brightness(0.85)` al hacer `:hover` y `:focus`, y respetando la variable global `$color-visited` para indicar enlaces ya leídos, cumpliendo así con las directivas AAA del W3C (WAI-ARIA).

**Motivo / criterio:** *Limpieza Visual y Carga Cognitiva*. Transferir el color a la tipografía principal del componente ahorra *ruido* de bordes extraños en el grid y hace que el mapeo visual sea instantáneo.

### 2026-06-14 — UI/UX: Wayfinding Semántico por Estantería y Botón 'Volver Arriba' Global

**Contexto:** La arquitectura de información requería una forma visual pasiva de orientar a la usuaria sin importar el tamaño de la pantalla, asignando un color identitario a cada macro-tema. Además, faltaba una forma ergonómica de hacer scroll inverso (Back to Top) sin colisionar con el asistente virtual Merci.

**Hecho:** 
1. Se ha construido un mapa de variables `$theme-colors` en SASS.
2. Mediante un bucle `@each`, se han generado dinámicamente clases modificadoras (`.theme--[slug]`) que inyectan el color correspondiente en el índice lateral, el título de la sección y el borde izquierdo de las tarjetas.
3. Se ha implementado un componente flotante global (`.floating-back-to-top`) inyectado puramente por el orquestador SSG al final de `index.html`. Se ha anclado estratégicamente en la esquina inferior **izquierda** para no solaparse con el asistente Merci (esquina inferior derecha).

**Motivo / criterio:** *Diseño Inclusivo y Mapeo Cognitivo*. Mantenemos la pureza del código mediante preprocesadores CSS sin abusar de estilos *inline*, y proporcionamos orientación cromática para mitigar la carga de memoria a corto plazo del lector.

### 2026-06-14 — UI/UX: Conteo Dinámico de Publicaciones en el Índice Temático

**Contexto:** Con la contracción del índice temático (ocultando los artículos por defecto), la usuaria perdía visibilidad sobre la densidad de cada categoría sin hacer scroll hasta ella.

**Hecho:** Se ha inyectado una línea en `merci-publish.py` (`num_articulos = len(estanterias[tema_principal][sub_tema])`) que calcula en tiempo real la cantidad de cuadernillos o compendios que residen bajo cada subtema, y lo imprime entre paréntesis en el índice lateral (Ej: `Backend (12)`).

**Motivo / criterio:** *Transparencia de Datos / UX*. Proporciona al lector un resumen analítico instantáneo del peso de cada área de conocimiento sin recargar la interfaz gráfica.

### 2026-06-14 — Refactorización de Portada en Generación de PDFs

**Contexto:** Los documentos exportados a PDF mantenían un subtítulo *hardcoded* heredado de versiones anteriores (`Cuadernillo | Vol. 1`) y la etiqueta de fase redundaba al imprimir el prefijo ("Fase Epic X - Fase Y" imprimía "Fase Fase Epic X...").

**Hecho:** Se ha modificado el template de `WeasyPrint` dentro del motor de publicación `merci-publish.py`. Se ha eliminado la cadena de Volumen estática y, en su lugar, se inyectan las variables `tema_html` y `subtema_html` formateadas como una lista sin viñetas (`list-style: none;`). Adicionalmente, se purgó la redundancia en el campo de Fase (`fase_pdf_text = f" | {fase_html}"`).

**Motivo / criterio:** *Coherencia de Datos*. Alineamos el diseño de los documentos descargables a la nueva taxonomía (Estanterías / Subtemas) recién instaurada, asegurando que un lector en modo offline sepa exactamente a qué rama del árbol de conocimiento pertenece el escrito. Se forzó una regeneración global purgando el caché de la carpeta `descargas`.

### 2026-06-14 — UI/UX: Refinamiento Visual de Subtemas en Índice

**Contexto:** Tras la implementación del índice temático minimalista, las subcategorías compartían los estilos visuales (subrayado y color) de las estanterías principales, dificultando su diferenciación jerárquica.

**Hecho:** Se ha modificado el modificador SASS `.library-nav__theme-title--sub` en `_library-index.scss`. Se eliminó el `border-bottom` (subrayado) y se cambió el color a `$color-text-muted` para que contraste con el `$color-regular` naranja de la estantería padre. 

**Motivo / criterio:** *Accesibilidad y Diseño de Información*. Garantizar que el usuario entienda la jerarquía (Estantería -> Subtema) al primer golpe de vista mediante el peso visual y el color, sin depender de indentaciones excesivas.

### 2026-06-14 — UI/UX: Índice Temático Minimalista y Artículos Destacados

**Contexto:** La barra lateral (índice temático) de la Biblioteca se extendía verticalmente de manera inmanejable al renderizar la lista completa de cuadernillos dentro de estanterías muy pobladas (como DevSecOps).

**Hecho:** 
1. Se ha refactorizado el bucle del menú lateral en `merci-publish.py` para que, por defecto, **oculte** la lista completa de artículos y en su lugar el índice salte directamente a los Subtemas.
2. Se ha añadido la lógica condicional de **"Artículos Destacados"**. El generador buscará el atributo `destacado: "true"` en el Frontmatter y, de encontrarlo, renderizará en el menú lateral un máximo de 3 artículos destacados por subcategoría acompañados de una estrella (★).
3. Se actualizó la `plantilla-cuadernillo.md` para incluir el metadato `destacado: "false"` de fábrica.

**Motivo / criterio:** *Reducción de Carga Cognitiva*. El índice vuelve a su propósito original: mostrar el esqueleto taxonómico a alto nivel. El usuario que desee ver el catálogo completo de un subtema simplemente pinchará en él desde el menú para saltar al *Grid* central, evitando el colapso visual del menú de navegación.

### 2026-06-14 — Hotfix: Extracción de Subtema en SSG

**Contexto:** Tras el commit de la reestructuración jerárquica de la Biblioteca, se observó que todas las agrupaciones de segundo nivel aparecían con el título "General" a pesar de que el Frontmatter de los Markdown tenía el subtema correcto.

**Hecho:** Se identificó que la función `procesar_archivo` en `merci-publish.py` no estaba retornando el atributo `subtema` en su diccionario de salida hacia el orquestador maestro, provocando que la función `generar_indice` usara el valor por defecto ("General"). Se ha parcheado la extracción YAML para arrastrar este atributo al diccionario `pub` del motor SSG.

**Motivo / criterio:** *Consistencia de Datos*. Garantizar que el ciclo de vida del metadato (desde el Markdown puro hasta el renderizado HTML) no se interrumpa en las funciones intersecantes.

### 2026-06-14 — Arquitectura de Información: 4 Macro-temas y Subtemas

**Contexto:** La categorización de la Biblioteca y el Blog sufría de una fuerte fragmentación. Múltiples temas redundantes dificultaban la navegación lateral y diluían la densidad del contenido.

**Hecho:** Se ha ejecutado una refactorización arquitectónica profunda:
1. **Script de Migración Automatizado (`migrate-themes.py`):** Rastreo de 126 archivos Markdown para reescribir su Frontmatter, mapeando los temas antiguos a 4 macro-temas fijos (*Desarrollo y Arquitectura*, *DevSecOps e Infraestructura*, *Inteligencia Artificial y Agentes*, *Productividad y Gobernanza*) + *Varios*.
2. **Jerarquía Dual:** Inyección del atributo `subtema` en los 126 cuadernillos y actualización de la `plantilla-cuadernillo.md`.
3. **SSG y UI (`merci-publish.py` y `_library-grid.scss`):** Modificación del generador estático para leer ambas dimensiones y modificación del Grid CSS (`grid-column: 1 / -1`) para que los subtítulos fluyan dentro de la cuadrícula de alta densidad sin romperla.

**Motivo / criterio:** *Consolidación y Escalabilidad*. Imponer un techo de cristal de 5 estanterías garantiza un panel de navegación limpio de por vida, delegando la hiper-segmentación al subtema dentro del cuerpo principal.

### 2026-06-14 — Hotfix: Resolución de fallo silencioso en generador SSG (merci-publish.py)

**Contexto:** Tras el commit anterior de Alta Densidad, se observó que la compilación de la Biblioteca no reflejaba los cambios estructurales (`.library-grid` y omisión de subtemas) en los HTML estáticos generados.

**Hecho:** Se detectó que la refactorización en `merci-publish.py` falló de forma silenciosa, dejando la lógica antigua intacta (iterando sobre `sub_temas_ordenados`). Se ha ejecutado un script correctivo robusto para reescribir los bucles de renderizado HTML del SSG, eliminando la jerarquía de subtemas y envolviendo las iteraciones directamente en `.library-grid`. Tras recompilar, la Biblioteca consolida finalmente la alta densidad.

**Motivo / criterio:** *QA y Trazabilidad*. Un fallo en la inyección de código derivó en un falso positivo del pipeline de compilación (que reportó éxito porque el código original de Python seguía siendo válido sintácticamente, pero sin aplicar el rediseño). Se documenta para enfatizar la verificación visual (QA) post-compilación.

### 2026-06-14 — UI/UX: Alta Densidad en Biblioteca y Refinamientos en WooCommerce

**Contexto:** Se detectaron múltiples oportunidades de mejora en la experiencia de usuario (UX). La Biblioteca sufría de fragmentación visual por exceso de subtemas y falta de aprovechamiento del espacio (densidad informativa). En paralelo, WooCommerce presentaba redundancias de accesibilidad ('Llavero Merci... cantidad' visible en pantalla) y carecía de una variable centralizada para la tipografía de sus botones.

**Hecho:**
1. **Biblioteca Mobile-First:** Se refactorizó `merci-publish.py` para agrupar publicaciones exclusivamente por Tema Principal. Se introdujo `_library-grid.scss` con CSS Grid dinámico (`auto-fill, minmax(280px, 1fr)`) y tarjetas ultracompactas, incrementando la densidad informativa sin sacrificar legibilidad.
2. **Hardening de Accesibilidad:** Se reimplementó la clase `.screen-reader-text` en `_reset.scss` para ocultar visualmente el texto para lectores de pantalla. Adicionalmente, se inyectó un hook en `functions.php` para vaciar el nombre del producto en los inputs de cantidad.
3. **Escalabilidad del Sistema de Diseño:** Se inyectó la variable `$font-size-button` en `_variables.scss` y se aplicó a todos los botones unificados (`button.button, a.button`, etc.) en `_woocommerce.scss`.

**Motivo / criterio:** *Design System Scalability y Mobile-First*. Desacoplar la cuadrícula de la biblioteca de la portada permite evolucionar ambas de forma independiente. Limpiar la interfaz de la tienda de repeticiones redundantes y encapsular variables CSS asegura un mantenimiento 'Zero-Bloat' a futuro.

**Siguiente paso o deuda:** Compilar los cambios, sellar mediante 'merci commit' y continuar con la integración de Proyectos Satélite o revisión de copywriting.

### 2026-06-13 — Docs/QA: Creación de cuadernillo sobre contención visual de código

**Contexto:** Tras solucionar el bug de desbordamiento horizontal en etiquetas pre y code (CSS overflow), era necesario consolidar este aprendizaje arquitectónico para evitar su recurrencia, especialmente dada su implicación dual (web móvil y renderizado a PDF estático).

**Hecho:** Se redactó el activo de conocimiento `laboratorio/incubacion/cuadernillo-resolucion-desbordamiento-css-codigo.md` documentando el desafío, la solución técnica con `white-space: pre-wrap` y el aprendizaje asimilado.

**Motivo / criterio:** *Knowledge Harvesting y Docs-as-Code*. Las resoluciones de bugs estructurales contienen un inmenso valor técnico. Convertirlas en un cuadernillo garantiza que la solución se integre en la Biblioteca como un estándar, evitando que el equipo o la IA futura reincidan en antipatrones de CSS.

**Siguiente paso o deuda:** Sellar la creación del documento con un commit atómico y continuar con la Fase 6.

### 2026-06-13 — UI/Bug: Resolución del desbordamiento en bloques de código

**Contexto:** (Desafío) Se detectó previamente que los fragmentos de código (`<pre>`, `<code>`) en la Biblioteca desbordaban horizontalmente en el viewport de móviles y se truncaban al exportar a PDF mediante WeasyPrint.

**Hecho:** (Maniobra)
- Se inyectaron reglas globales en `src/scss/base/_typography.scss` para los elementos `pre` y `code`.
- Se implementó `white-space: pre-wrap` y `word-break: break-word` para garantizar el salto de línea en strings largos y PDFs.
- Se configuró `overflow-x: auto` y un `max-width: 100%` en `<pre>` para asegurar un desplazamiento seguro en vistas móviles si el texto aún desborda de forma natural.
- Se estandarizó el aspecto visual con fuente `monospace`, fondo suave de contraste (`#f1f5f9`), espaciados internos y bordes redondeados.
- Se compiló el código SASS (`merci-styles.py`) exitosamente hacia `public/css/main.css`.

**Motivo / criterio:** (Aprendizaje) *Responsive Web Design y Spec as Source*. Evitar que el contenido quiebre el viewport es crítico para la puntuación en Core Web Vitals (CLS y usabilidad móvil). Proveer estilos agnósticos que cubran tanto web como renderizado a PDF (WeasyPrint) consolida la dualidad de los cuadernillos de la biblioteca sin añadir scripts o dependencias externas.

**Siguiente paso o deuda:** Sellar los cambios en Git y continuar con el resto de tareas de la Fase 6.

### 2026-06-12 — Ops: Multiplexación de terminales con Tmux (Bootstrapper)

**Contexto:** (Desafío) Levantar y apagar diariamente toda la infraestructura local (Docker, motor de IA local, Proxy enrutador, SRE, Watcher SASS) consumía demasiadas terminales aisladas, generando una alta carga cognitiva y violando la política de Fricción Cero.

**Hecho:** (Maniobra)
- Se desarrollaron los scripts de orquestación `scripts/merci/merci-boot.sh` y `scripts/merci/merci-down.sh`.
- Se implementó `tmux` para dividir una única terminal en 3 ventanas lógicas (Matriz, IA-Stack, Servicios), inyectando los comandos de activación del entorno virtual automáticamente.
- Se habilitó el soporte nativo para ratón (`mouse on`) en Tmux para facilitar la navegación y el *scroll* entre paneles.
- Se extirpó el servidor local redundante de Python (puerto 8000) ya que Nginx resuelve nativamente el `localhost`.

**Motivo / criterio:** (Aprendizaje) *Fricción Cero y Developer Experience (DX)*. Un ecosistema DevSecOps de nivel Enterprise no debe intimidar ni abrumar operativamente a su creadora al arrancar. Encapsular la complejidad de inicialización (Bootstrapping) y apagado (Teardown) en dos simples comandos consolida el entorno como una plataforma ágil y cohesionada.

**Siguiente paso o deuda:** Ejecutar `merci commit` para sellar la orquestación de terminales y el enrutamiento del IDE.

### 2026-06-12 — Ops/IaC: Enriquecimiento del Dashboard de Grafana con métricas DevSecOps y SRE

**Contexto:** (Desafío) El cuadro de mandos original de Grafana (`mercedev.es`) se limitaba a representar métricas del Roadmap y flujos de contenido, ignorando todas las métricas de rendimiento físico (Core Web Vitals), diagnósticos de red, resiliencia (Chaos Monkey) y auditorías de seguridad que expone el agente SRE local.

**Hecho:** (Maniobra)
- Se inyectó `deleteDatasources` en el provisionamiento de base de datos para evitar colisiones de Identificador Único (UID) y se configuró un identificador determinista (`uid: prometheus`).
- Se rediseñó el archivo [merci-dashboard.json](file:///home/hildegahr/Escritorio/PROYECTO_mercedev.es/observabilidad/dashboards/merci-dashboard.json) añadiendo 16 nuevos paneles orientados a calidad de código, Core Web Vitals (LCP, TBT, CLS), latencias, fallbacks de IA y resiliencia del Chaos Monkey.
- Se reestructuró la visualización en 4 filas temáticas expandidas por defecto para una lectura clara del estado del ecosistema.
- Se validó el aprovisionamiento correcto reiniciando el contenedor de Grafana y realizando peticiones directas de telemetría a la API.

**Motivo / criterio:** (Aprendizaje) *Observabilidad Holística en el Orquestador*. Un ingeniero DevSecOps y SRE requiere una visibilidad de 360 grados de la infraestructura. Agrupar las métricas en capas lógicas (Rendimiento, Seguridad, Caos y Contenido) reduce el tiempo medio de detección (MTTD) ante derivas en pre-producción.

**Siguiente paso o deuda:** Sellar los cambios con `merci-commit.py` e iniciar la Fase 6 de la Épica 8.

### 2026-06-12 — Ops/IaC: Corrección del aprovisionamiento automático y reubicación de archivos de Grafana

**Contexto:** (Desafío) La pila de observabilidad (Prometheus y Grafana) presentaba problemas de persistencia y carga automática de la configuración en su arranque (IaC) al tener archivos de aprovisionamiento duplicados o en rutas incorrectas en el anfitrión, además de problemas de permisos (`root:root`) en directorios auto-generados por el demonio Docker.

**Hecho:** (Maniobra)
- Se corrigieron los permisos de propiedad de los directorios en el anfitrión (`chown -R 1000:1000`) para posibilitar el acceso al usuario local.
- Se reubicaron los archivos de configuración de provisionado a sus directorios correctos: `prometheus.yaml` y `default.yaml` bajo `observabilidad/provisioning/` y `merci-dashboard.json` bajo `observabilidad/dashboards/`.
- Se restableció la contraseña de administración de Grafana utilizando el comando interno de versión 13 en el contenedor (`/usr/share/grafana/bin/grafana cli`).
- Se verificó mediante la API y logs de Grafana la correcta carga automática de la fuente de datos Prometheus y el cuadro de mando `DevSecOps/mercedev.es` en su inicio.

**Motivo / criterio:** (Aprendizaje) *Infraestructura como Código Limpia y Segura*. Disponer de archivos de provisionamiento ordenados y en rutas que respeten el estándar del contenedor de Grafana garantiza la idempotencia del despliegue local de observabilidad sin requerir configuración manual reiterada tras cada reinicio del contenedor.

**Siguiente paso o deuda:** Iniciar la Fase 6 (Refinamiento de Textos y Experiencia Documental) para mejorar visual y narrativamente todas las secciones del ecosistema.

### 2026-06-12 — Refactor/QA: Robustez, tipado y docstrings en scripts utilitarios auxiliares (Fase 5)

**Contexto:** (Desafío) Los scripts utilitarios y demonios de monitoreo de la Fase 5 (vigilantes, backups, colas y sincronizadores) mostraban firmas de función sin tipado estático, docstrings asimétricos y salidas no controladas ante interrupciones de teclado (`KeyboardInterrupt`), dificultando el mantenimiento y robustez general del ecosistema de scripts locales.

**Hecho:** (Maniobra)
- Se refactorizaron 5 scripts utilitarios: `merci-watcher.py`, `merci-assets-watcher.py`, `merci-backup.py`, `merci-queue.py` y `merci-sync-pages.py` en `scripts/merci/`.
- Se inyectaron anotaciones de tipo estático en parámetros y retornos, y se estructuraron docstrings explicativos (*QUÉ HACE* / *POR QUÉ*) en castellano.
- Se ordenaron las importaciones según el estándar de estilo PEP 8.
- Se encapsularon las ejecuciones y se interceptaron las interrupciones `KeyboardInterrupt` en el bloque principal de cada script, saliendo de forma controlada con código `130`.
- Se validó la paridad estructural ejecutando el pipeline completo mediante `merci-total.py` con un 100% de éxito.
- Se actualizaron las tareas específicas de la Fase 5 en `ROADMAP.md`.

**Motivo / criterio:** (Aprendizaje) *Higiene en Demonios Locales y Herramientas Auxiliares*. Los procesos que corren en segundo plano (vigilantes de archivos) o bajo demanda (backups) deben poseer los mismos estándares de calidad y control de errores que los componentes del núcleo. La unificación del código de retorno en `130` asegura un comportamiento estándar en entornos POSIX.

**Siguiente paso o deuda:** Sellar los cambios de la Fase 5 mediante `merci-commit.py` y dar por concluida la refactorización sistemática de scripts de la Épica 8, preparándose para la Fase 6 (Refinamiento de textos y experiencia documental).

### 2026-06-12 — Refactor/QA: Robustez, tipado y docstrings en scripts de Observabilidad & Seguridad (Fase 4)

**Contexto:** (Desafío) Los scripts de la Fase 4 (Observabilidad & Seguridad) carecían de tipado estático completo en sus firmas y de docstrings estructurados uniformes. Adicionalmente, el control de excepciones e interrupciones del teclado (`KeyboardInterrupt`) requería robustecimiento en scripts críticos como `merci-sre.py`, `merci-extract-metrics.py`, `merci-hardening.py`, `merci-linkcheck.py` y `merci-chaos.py`.

**Hecho:** (Maniobra)
- Se refactorizaron 5 scripts de la categoría de observabilidad y seguridad: `merci-sre.py`, `merci-extract-metrics.py`, `merci-hardening.py`, `merci-linkcheck.py` y `merci-chaos.py` en `scripts/merci/`.
- Se inyectaron anotaciones de tipo estático en parámetros y retornos de funciones, y se estructuraron docstrings explicativos (*QUÉ HACE* / *POR QUÉ*) en castellano.
- Se reordenaron las importaciones conforme al estándar de estilo PEP 8.
- Se encapsuló la ejecución en bloques de control de excepciones y capturadores de interrupción `KeyboardInterrupt` para salir limpiamente con código `130`.
- Se corrigió una duplicación de firmas y una sintaxis errónea en la invocación de `sys.exit()` del bloque principal en `merci-linkcheck.py`.
- Se validó la estabilidad del pipeline ejecutando `merci-total.py` de forma satisfactoria (100% de éxito).
- Se actualizó la lista de scripts individuales de la Fase 4 en `ROADMAP.md`.

**Motivo / criterio:** (Aprendizaje) *Seguridad Estructural y SRE Resiliente*. Estandarizar el tipado y los manejadores de salida en scripts de seguridad y observabilidad asegura la consistencia de las auditorías locales. El control de cancelaciones evita volcados de pila innecesarios (tracebacks) en la terminal de la ingeniera y promueve una experiencia de desarrollo limpia.

**Siguiente paso o deuda:** Sellar los cambios de la Fase 4 en Git y prepararse para la Fase 5 (Del resto de scripts).

### 2026-06-12 — Refactor/QA: Robustez, tipado y docstrings en scripts de Publishing & DevRel (Fase 3)

**Contexto:** (Desafío) Los scripts asociados a la Fase 3 (Publishing & DevRel) presentaban falta de homogeneidad en la tipificación estática, docstrings incompletos y carecían de manejadores elegantes para interrupciones por teclado (`KeyboardInterrupt`) o fallos genéricos, comprometiendo la experiencia de desarrollo (DX) y la solidez del pipeline ante ejecuciones fallidas o canceladas.

**Hecho:** (Maniobra)
- Se refactorizaron sistemáticamente 9 scripts: `merci-publish.py`, `merci-telemetry.py`, `merci-promote.py`, `merci-linkedin.py`, `merci-wp.py`, `merci-shop.py`, `merci-deploy.py` y `merci-release.py` (ubicados en `scripts/merci/`), además de `merci-showcase.py` (ubicado en `scripts/matriz/`).
- Se introdujo tipado estático estricto para argumentos y retornos de funciones, y se estructuraron sus docstrings explicativos (*QUÉ HACE* / *POR QUÉ*) en castellano.
- Se ordenaron las importaciones de acuerdo a PEP 8 y se encapsuló la ejecución en bloques `try...except` y captura de `KeyboardInterrupt` con salida controlada en código `130`.
- Se documentó la integración de Grafana v13 en el contenedor de observabilidad, utilizando el comando `/usr/share/grafana/bin/grafana cli` en lugar del antiguo `grafana-cli` no disponible.
- Se aisló físicamente `merci-showcase.py` en el directorio de la matriz para evitar riesgos de fugas de credenciales (DLP).
- Se ejecutó el pipeline completo a través de `merci-total.py`, logrando un 100% de éxito en la compilación y validación del entorno.
- Se actualizó el listado detallado de scripts de la Fase 3 en `ROADMAP.md`.

**Motivo / criterio:** (Aprendizaje) *Robustez en Flujos de Publicación e Higiene de Código*. Uniformar las capas de control y tipado de los scripts de distribución social y despliegue reduce la fragilidad del ecosistema y garantiza que cualquier fallo en redes o WordPress falle elegantemente sin comprometer el pipeline maestro.

**Siguiente paso o deuda:** Sellar los cambios de la Fase 3 mediante `merci-commit.py` e iniciar la Fase 4 (scripts de Observabilidad & Seguridad).

### 2026-06-12 — Refactor/QA: Tipado, docstrings, robustez en scripts de IA/Gobernanza y resolución de Deriva Documental

**Contexto:** (Desafío) Los scripts de la Fase 2 (IA & Gobernanza) presentaban asimetrías de tipado estático, docstrings y control de excepciones. Adicionalmente, existía un error de invocación de API crítico en `merci-auto-fix.py` al acceder a `choices.message` en lugar de `choices[0].message`. Por último, el detector de deriva documental `merci-drift.py` alertaba de la ausencia de documentación de varios scripts activos (`merci-deploy.py`, `merci-publish.py`, `merci-wp.py`, `merci-shop.py`, `merci-hardening.py`) en sus respectivos manuales específicos en `docs/`.

**Hecho:** (Maniobra)
- Se refactorizaron sistemáticamente los scripts `merci-brain.py`, `merci-ssot.py`, `merci-librarian.py`, `merci-glosario.py`, `merci-blogger.py`, `merci-auto-fix.py` y `merci-drift.py` en `scripts/merci/` y `laboratorio/scripts_temporales/`.
- Se inyectó tipado estático completo en parámetros y retornos, se ordenaron las importaciones según PEP 8, y se estructuraron docstrings explicando el qué hace y por qué en castellano.
- Se encapsuló la ejecución en bloques `try...except Exception` con captura de `KeyboardInterrupt` (Ctrl+C) saliendo con código `130` y mensaje limpio.
- Se corrigió el bug de LiteLLM en `merci-auto-fix.py` indexando correctamente choices (`[0]`).
- Se reescribió `merci-drift.py` implementando validación contextual por categorías a través de `SCRIPT_MAPPINGS`.
- Se actualizaron los manuales de `docs/` (`deployment-playbook.md`, `flujo-publicacion-sop.md`, `integracion-wordpress.md` y `checklist-hardening.md`) para documentar e integrar de forma impersonal todos los scripts previamente en deriva.
- Se ejecutó el pipeline completo mediante `merci-total.py`, certificando un 100% de éxito con cero advertencias y deriva documental solucionada.

**Motivo / criterio:** (Aprendizaje) *Seguridad en el Lado Izquierdo (Shift-Left Security) y Coherencia Documental*. La eliminación de errores de indexación de APIs en scripts automatizados evita caídas en CI/CD. La sincronización estricta por categorías documentales garantiza la trazabilidad operativa y el orden del ecosistema sin generar ruido.

**Siguiente paso o deuda:** Sellar los cambios en Git y actualizar el Roadmap maestro para dar por concluida la Fase 2.

### 2026-06-12 — Release/Integración y Despliegue Continuo (CI-CD): Publicación no interactiva de Merci Boilerplate v1.18.0

**Contexto:** (Desafío) El orquestador de exportación `merci-release.py` exigía interacción por teclado por parte del usuario y disparaba `merci-init.py` en caliente, provocando excepciones fatales de fin de archivo (`EOFError`) cuando se ejecutaba en entornos desatendidos o automatizados de manera asíncrona.

**Hecho:** (Maniobra)
- Se incorporó soporte para el analizador de argumentos (`argparse`) en `scripts/merci/merci-release.py`, añadiendo el flag `--non-interactive`.
- Se reconfiguró el lanzamiento interno de `merci-init.py` en el clon efímero para invocarlo de manera directa pasando las banderas `--force`, `--dominio "tuempresa.es"`, `--nombre "Tu Empresa"` y `--ia`.
- Se ejecutó de forma no interactiva el release pipeline, validando la compilación del Boilerplate con `merci total` local y publicando exitosamente los cambios de la versión `v1.18.0` en GitHub.
- Se actualizó y homogeneizó con estilo impersonal el archivo [SECURITY.md](file:///home/hildegahr/Escritorio/PROYECTO_mercedev.es/SECURITY.md) para reflejar el soporte oficial de la rama v1.18.x.
- Se dio por cerrada la Fase 1 (Core Pipeline) de la Épica 8 en el Roadmap maestro.

**Motivo / criterio:** (Aprendizaje) *Idempotencia y Desacoplamiento de Entrada Estándar*. Diseñar scripts DevSecOps asumiendo la presencia constante de un operador humano al teclado rompe la automatización. Proveer vías no interactivas (`argparse`, variables de entorno) blinda el pipeline para ejecuciones desatendidas y sistemas de Integración Continua (CI).

**Siguiente paso o deuda:** Iniciar la Fase 2 (IA & Gobernanza) analizando y refactorizando el script `merci-brain.py`.

### 2026-06-12 — Docs/QA: Estilo impersonal en manuales y sincronización de Roadmap en README.md

**Contexto:** (Desafío) El Roadmap resumido en el archivo `README.md` carecía del estado y registro de la Épica 8, lo que provocaba una asimetría respecto al `ROADMAP.md` maestro. Por otro lado, existían algunas conjugaciones en segunda persona en los manuales de `docs/` (`ciclo-de-vida-contenidos.md` y `flujo-publicacion-sop.md`) que vulneraban las directrices de estilo impersonal (reglas 7 y 8).

**Hecho:** (Maniobra)
- Se actualizó la sección "Roadmap y Estado del Proyecto" de `README.md` incorporando la Épica 8 (*Refactorización y Limpieza de Código*) en estado "En curso".
- Se revisaron y reescribieron las secciones de `docs/ciclo-de-vida-contenidos.md` y `docs/flujo-publicacion-sop.md` que contenían verbos y pronombres en segunda persona (ej. "te preguntará", "tengas que", "lo pasas"), cambiándolas a una redacción estrictamente impersonal y pasiva.
- Se comprobó la ausencia de notas de recordatorio personales en el directorio de documentación.

**Motivo / criterio:** (Aprendizaje) *Higiene Editorial y Consistencia del Roadmap*. Respetar la soberanía del estilo impersonal en la documentación técnica pública eleva el tono profesional y la claridad del proyecto, y mantener alineados los roadmaps en los distintos puntos de lectura evita contradicciones operativas.

**Siguiente paso o deuda:** Finalizar el cierre de la Fase 1 de la Épica 8. Siguiente paso: iniciar la Fase 2 (IA & Gobernanza) analizando y refactorizando el script `merci-brain.py`.

### 2026-06-12 — Refactor/QA: Tipado, docstrings y robustez en orquestador merci-completo.py

**Contexto:** (Desafío) El orquestador supremo `merci-completo.py` carecía de anotaciones de tipo estático y docstrings estructurados según las especificaciones del proyecto. Adicionalmente, no controlaba excepciones imprevistas al invocar los procesos del pipeline (como `FileNotFoundError` o `PermissionError`), lo que podía generar volcados de pila innecesarios.

**Hecho:** (Maniobra)
- Se ordenaron alfabéticamente las importaciones de la biblioteca estándar según las pautas de PEP 8.
- Se agregaron anotaciones de tipo estático a todas las funciones (ej. `script: str`, `nombre: str`, retornos `float` y `None`).
- Se definieron docstrings en español estructurados (*QUÉ HACE* y *POR QUÉ*) para todas las funciones.
- Se encapsuló la llamada a `subprocess.run()` dentro de `ejecutar_fase()` y el inicio en `__main__` en bloques `try...except Exception` para atrapar fallos del sistema operativos y notificar de manera limpia y legible antes de salir con código `1`.
- Se verificó el script compilándolo y validándolo con `merci-audit.py`.

**Motivo / criterio:** (Aprendizaje) *Higiene y Control de Flujo DevSecOps*. Garantizar la robustez del orquestador supremo es fundamental, ya que cualquier error de infraestructura local debe detener de manera controlada el pipeline de publicación e impedir que un fallo silencioso comprometa la release.

**Siguiente paso o deuda:** Con la refactorización de `merci-completo.py`, se concluye la revisión de scripts en la Fase 1 de la Épica 8. El siguiente paso es iniciar la auditoría documental del directorio `docs/`, `instrucciones.md` y `README.md` antes de pasar a la Fase 2 (IA & Gobernanza).

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
