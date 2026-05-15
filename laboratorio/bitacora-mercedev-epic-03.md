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

### 2026-05-14 — UX/UI: Separadores editoriales dinámicos (Pseudo-elementos)

**Contexto:** La vista de lectura continua (`.prose`) presentaba una carga visual densa entre secciones. Se sugirió envolver las secciones en `<div>` o utilizar cajas (cards) para añadir líneas divisorias, lo cual habría roto el flujo de generación estándar desde Markdown puro.

**Hecho:** Se implementaron líneas horizontales automáticas mediante pseudo-elementos (`::before`) en `src/scss/components/_prose.scss`.

**Detalle técnico:** Se anclaron las líneas al selector `> h2 ~ h2`. En móvil, se utiliza `border-top`. En escritorio (patrón *Side-Heading* con floats), se proyecta un pseudo-elemento con posicionamiento absoluto y un ancho calculado (`calc(250px + 4rem + 65ch)`) que atraviesa ambas columnas visuales justo en medio del margen superior de separación.

**Motivo / criterio:** *Markdown Purity y Zero HTML Bloat*. Envolver el contenido en `<div>` obliga a escribir HTML crudo en los artículos, arruinando la experiencia de redacción. Extraer la responsabilidad de los separadores 100% a la capa SASS mantiene los documentos limpios y genera una estética editorial (estilo Stripe/Vercel) sin deuda técnica.

### 2026-05-14 — UX/UI: Reescritura fundacional de la Portada (Home)

**Contexto:** El texto de la página de inicio (`public/index.html`) había quedado obsoleto y no reflejaba la magnitud operativa del ecosistema tras las integraciones de IA y Observabilidad, ni proyectaba la autoridad técnica del *Spec-Driven Development*.

**Hecho:** Se reescribió y maquetó la portada integrando el patrón *Editorial Breakout* (`.prose`). Se reubicó el "Engineering Dashboard" como elemento central de la sección superior para maximizar el impacto visual (First Fold).

**Motivo / criterio:** *Product Marketing y Autoridad Empírica*. La portada de un Boilerplate o de un perfil técnico no debe ser un simple saludo; debe ser una demostración de poder. Listar los agentes, las métricas y la filosofía arquitectónica inmediatamente establece el tono DevSecOps del repositorio, diferenciándolo de los portfolios tradicionales.

### 2026-05-14 — Fix: Resolución de colapso de márgenes en Side-Heading

**Contexto:** En la composición a dos columnas (Side-Heading), cuando un `h2` iba seguido inmediatamente de un `h3` (como en "Próximo Destino -> Épica 4"), la línea divisoria se desfasaba y atravesaba el texto. Esto ocurría porque los elementos flotados (`h2`) no colapsan sus márgenes con el contenido previo, mientras que el flujo normal (`h3`) sí lo hace, provocando un desalineamiento vertical en el que el `h2` quedaba más bajo que el `h3`.

**Hecho:** Se sustituyó `margin-top` por `padding-top` en los bloques de separación de la cuadrícula en `src/scss/components/_prose.scss`.

**Detalle técnico:** Se anuló el margen superior (`margin-top: 0`) para `> h2` y su hermano adyacente `> h2 + *`, aplicando en su lugar `padding-top: 4.5rem`. El pseudo-elemento de la línea divisoria se ajustó a `top: 2.25rem` para ubicarse exactamente en medio del *padding*.

**Motivo / criterio:** *CSS Box Model & Margin Collapsing*. Reemplazar márgenes por padding (relleno interno) erradica matemáticamente el fenómeno de colapso de márgenes. Al obligar a ambos elementos (flotado y flujo normal) a utilizar padding para su separación vertical, garantizamos que arranquen exactamente en el mismo píxel de la pantalla, manteniendo la línea divisoria perfectamente centrada y la alineación inquebrantable independientemente de qué etiqueta siga al titular.

### 2026-05-14 — UX/UI: Ajuste de espaciado en Engineering Dashboard

**Contexto:** Existía un hueco visual excesivo entre el Hero de la portada y el bloque de métricas, generado por la suma del padding de la sección y un margen superior desproporcionado (`5rem`) en el componente del dashboard.

**Hecho:** Se redujo el `margin-top` del modificador `.hero__dashboard--standalone` a `1.5rem` en el archivo `src/scss/components/_hero.scss`.

**Motivo / criterio:** *Visual Hierarchy y Whitespace Control*. Un exceso de espacio negativo desconecta semánticamente dos secciones. Reducir la brecha visual agrupa orgánicamente el Hero y el Dashboard como una única entidad informativa (First Fold).

### 2026-05-14 — UX/UI: Sincronización de alineación superior en Side-Heading

**Contexto:** En el patrón de *Side-Heading* (Titulares flotados), el ajuste óptico (`padding-top: 0.3rem`) del `h2` provocaba un desfase visual en la parte superior. Además, los `h3` mantenían márgenes superiores (`2.5rem`) que los desalineaban verticalmente respecto al flujo de los párrafos adjuntos.

**Hecho:** Se refactorizaron los márgenes en `src/scss/components/_prose.scss`.
- Se eliminó el `padding-top: 0.3rem` de los `h2` para que coincidan en el borde absoluto superior con su contenido adyacente.
- Se igualó el modelo de caja de `h3` al de los párrafos (`margin-top: 0; margin-bottom: 1.75rem; padding: 0;`).

**Motivo / criterio:** *Alignment & Typography Flow*. Para que un sistema de rejilla asimétrica funcione visualmente, los ejes "top" y "left" deben ser inquebrantables. Obligar a que los subtítulos (`h3`) se comporten estructuralmente como párrafos asegura que la caja delimitadora (Bounding Box) siempre coincida con el titular desplazado (`h2`), logrando un acabado de ingeniería visual perfecto independientemente de cómo comience la sección.

### 2026-05-14 — UX/UI: Refactorización Side-Heading a Floats (Bug de filas Grid)

**Contexto:** Se detectó un efecto indeseado ("H3 solitario") al utilizar CSS Grid Auto-Placement para el patrón *Side-Heading*. Si el titular desplazado (`h2`) ocupaba varias líneas, Grid bloqueaba la altura de toda esa fila, empujando los párrafos siguientes excesivamente hacia abajo y creando grandes vacíos visuales bajo los subtítulos.

**Hecho:** Se reemplazó CSS Grid por un patrón de "Floats Asimétricos" en `src/scss/components/_prose.scss`.

**Detalle técnico:** Se aplicó `margin-left: auto` y `max-width: 65ch` a todos los hijos directos para desplazarlos a la derecha, dejando el canal izquierdo libre. Se aplicó `float: left` y `clear: left` a los `h2` para anclarlos en dicho canal. Se sincronizó el espaciado vertical (`margin-top: 4.5rem`) entre los `h2` y su hermano adyacente (`h2 + *`).

**Motivo / criterio:** *DOM Flow & Component Decoupling*. Los elementos flotados son extraídos del flujo normal de bloques. A diferencia de CSS Grid, que fuerza restricciones horizontales (filas), flotar los encabezados permite que la columna de lectura se empaquete verticalmente de forma compacta y natural, garantizando una lectura fluida independientemente de la longitud del titular izquierdo.

### 2026-05-14 — UX/UI: Evolución a composición "Side-Heading" mediante Grid Auto-Placement

**Contexto:** El patrón "Editorial Breakout" (alineación izquierda a 850px) en la página del CV no equilibraba visualmente el menú superior de 1200px. El texto se sentía largo, estrecho y demasiado escorado a la izquierda, dejando un vacío visual masivo a la derecha en la vista de escritorio.

**Hecho:** Se implementó el patrón *Side-Heading* (Titulares Desplazados) refactorizando el componente `.prose__content` en `src/scss/components/_prose.scss` y actualizando el dashboard en `_hero.scss`.

**Detalle técnico:** Se aplicó `display: grid` a la clase `.prose__content` con `grid-template-columns: 250px minmax(0, 65ch)` y alineación de línea base (`align-items: baseline`). Mediante auto-posicionamiento CSS (`> * { grid-column: 2; }` y `> h2 { grid-column: 1; }`), se forzó a que los títulos `h2` ocupen la columna izquierda y los párrafos la derecha, sin necesidad de alterar una sola línea del marcado HTML.

**Motivo / criterio:** *Semantic UI y Modernidad*. Esta es la composición estándar de las documentaciones corporativas de élite (ej. Stripe, Vercel). Ocupa 1000px para equilibrar el *header*, pero respeta los 65ch de lectura ergonómica. Resolver esto exclusivamente con el motor CSS Grid sin inyectar contenedores `<div>` adicionales preserva un DOM ultraligero y semánticamente puro.

### 2026-05-14 — UX/UI: Transición al patrón "Editorial Breakout"

**Contexto:** Se detectó el "Síndrome de la columna solitaria" en la vista de escritorio. El componente `.prose` constreñía todo el artículo (títulos, imágenes y metadatos) a `65ch`, dejando márgenes laterales masivos respecto al ancho del menú global (`1200px`), generando un diseño largo, estrecho y desconectado de la navegación.

**Hecho:** Se implementó el patrón *Editorial Breakout* en `_prose.scss` y se alineó el dashboard independiente en `_hero.scss`.

**Detalle técnico:** El contenedor `.prose` se expandió a `850px` con alineación izquierda estricta para títulos y cabeceras. La restricción de lectura de `65ch` se movió mediante CSS a los selectores hijos directos (`> p, > ul, > ol`), permitiendo que imágenes y líneas divisorias "rompan" el margen del texto para ocupar los 850px completos. El dashboard `--standalone` se ensanchó también a 850px.

**Motivo / criterio:** *Modern Editorial Design*. Alinear los textos a la izquierda crea un eje visual ordenado y riguroso. Permitir que los elementos estructurales y multimedia ocupen más ancho que la columna de lectura soluciona el desequilibrio de proporciones en PC (Desktop), aportando un acabado *Premium* e ingenieril.

### 2026-05-14 — Refactor: Abstracción semántica del componente de lectura (Prose)

**Contexto:** Se detectó que la página estática del currículum ("Sobre Mí") utilizaba el componente BEM `.blog-post` para renderizar el texto. Aunque reutilizar los estilos de lectura ligera cumplía el principio DRY, el nombre del componente acoplaba semánticamente el diseño al dominio del blog, generando fricción cognitiva.

**Hecho:** Se abstrajo el componente `.blog-post` renombrándolo a `.prose` (Prosa/Texto continuo).
- Se creó `src/scss/components/_prose.scss` y se eliminó `_blog-post.scss`.
- Se refactorizaron las etiquetas HTML en `index.php` y `sobre-mi/index.html` para usar las nuevas clases `.prose`, `.prose__content`, etc.

**Motivo / criterio:** *Semantic UI y Agnosticismo de Componentes*. En la metodología BEM estricta, el nombre de un bloque debe describir su función estructural o visual, no su contenido o contexto. Llamarlo `.prose` permite que la ergonomía de lectura perfecta (65ch) pueda reutilizarse en blogs, currículums, manuales o políticas legales sin disonancia semántica.

### 2026-05-14 — UX/UI: Establecimiento de la norma de contención visual (Regla de los 65ch)

**Contexto:** Se detectó una disonancia visual en la página "Sobre Mí". El dashboard de métricas (`max-width: 800px`) era sustancialmente más ancho que los bloques de texto superior e inferior (`max-width: 65ch`), rompiendo la cuadrícula de lectura y dando la sensación de "caja desbordada".

**Hecho:** Se corrigió el archivo `_hero.scss` moviendo el modificador `.hero__dashboard--standalone` a su bloque correspondiente y ajustando su ancho máximo a `65ch`.

**Motivo / criterio:** *Design Consistency (Consistencia de Diseño)*. Se establece la norma de que ningún componente hijo o hermano anidado debe superar el ancho de su contenedor de lectura principal. Alinear todos los elementos centrales a `65ch` garantiza un flujo de lectura armónico y mantiene la atención del usuario sin forzar movimientos oculares periféricos.

### 2026-05-14 — UX/UI: Mejora visual del Dashboard de métricas

**Contexto:** Las métricas del dashboard no destacaban lo suficiente dentro de sus contenedores, restando impacto visual a los logros técnicos.

**Hecho:** Se actualizaron las reglas del componente `.hero__metric` en `_hero.scss` para centrar el contenido y aumentar significativamente el tamaño, peso y color de los valores.

**Motivo / criterio:** *Jerarquía visual*. Los números son el dato duro que demuestra la autoridad técnica. Deben ser el punto focal de la interfaz para que el usuario o reclutador los asimile instantáneamente de un solo vistazo.

### 2026-05-14 — Docs: Refinamiento de veracidad histórica en CV Semántico

**Contexto:** La primera iteración del CV Semántico contenía abstracciones excesivas sobre la experiencia previa de la autora ("enseñando a máquinas a ser precisas"). Era necesario alinear el texto exactamente con el historial laboral real (Ingeniería Técnica, control de obra civil, refinerías, delineación y gestión de proyectos).

**Hecho:** Se actualizó el HTML y el JSON-LD de `public/sobre-mi/index.html` para reflejar la experiencia real en dirección de obra, dosieres de calidad y estructuras industriales.

**Motivo / criterio:** *Transparencia y Autoridad Empírica*. La experiencia real gestionando infraestructuras físicas complejas y elaborando planos "As Built" es la metáfora perfecta para justificar la filosofía *Spec-Driven Development* y el control de calidad estricto (DevSecOps) en el software. La verdad histórica es siempre más potente y vendible que la ficción.

### 2026-05-14 — Fix: Erradicación de estilo en línea en CV Semántico

**Contexto:** Al inyectar el dashboard de métricas en la página estática "Sobre Mí", se incluyó temporalmente un atributo `style="..."` (CSS en línea) que habría violado la regla estricta `UI_INLINE_STYLE`, provocando el bloqueo del pipeline.

**Hecho:** Se extrajo el estilo a un modificador BEM (`.hero__dashboard--standalone`) en `_hero.scss` y se purgaron los atributos `style` del HTML en `public/sobre-mi/index.html`.

**Motivo / criterio:** *QA Assurance y Zero Deuda Técnica*. El pipeline DevSecOps no debe romperse por un fallo de formato visual introducido accidentalmente en un nuevo HTML. Pagar la deuda antes de lanzar el orquestador global protege el flujo de Integración Continua y respeta la arquitectura SASS.

### 2026-05-14 — UX/UI: Reescritura del CV Semántico y proyección de telemetría dinámica

**Contexto:** El texto de la página estática "Sobre Mí" (`public/sobre-mi/index.html`) requería una reescritura para alinearse con el tono autoritario de "Performance Engineer" y reflejar las métricas exactas logradas en la Release v1.13.0 (agentes Python, líneas de documentación, CWV 100/100).

**Hecho:** Se maquetó el nuevo texto utilizando los componentes de lectura ligera (`.blog-post`) y se reutilizó el componente `.hero__dashboard` para exponer las métricas en un formato visual asimilable. Se registró en el Roadmap la tarea de automatizar estos números.

**Detalle técnico:** Se documentó la viabilidad de crear un inyector (SSOT) que escanee el tamaño de las bitácoras (`wc -l`) y el conteo de scripts para rellenar el HTML en tiempo de compilación.

**Motivo / criterio:** *Marketing de Autoridad y SSOT*. Un CV técnico no debe ser un texto estático; debe ser un *dashboard* del profesional. Maquetarlo con las clases del blog asegura legibilidad (65ch) y prepararlo para recibir datos automáticos convierte la página "Sobre Mí" en un artefacto verdaderamente DevSecOps.

### 2026-05-14 — UX/UI: Purga de tarjetas en Blog Feed y Hero Compacto

**Contexto:** En la vista de listado del blog (`localhost/blog`), los artículos seguían apareciendo con el diseño pesado de cuadernillos ("cartelones") debido a clases CSS residuales en el bucle PHP. Además, el Hero del blog ocupaba demasiado espacio vertical (`40vh`) para el texto que contenía, empujando el contenido útil fuera de la pantalla.

**Hecho:** Se limpió el HTML del listado en `index.php` erradicando las clases `.card` y delegando el diseño puro a `.blog-feed__article`. Se creó el modificador `.hero--compact` para el banner del blog.

**Detalle técnico:** Se refinaron los estilos en `_blog-feed.scss` aplicando un separador minimalista `border-bottom` en lugar de cajas cerradas. En `_hero.scss`, el modificador `--compact` reduce el `min-height` a `20vh` y optimiza los márgenes.

**Motivo / criterio:** *UI Consistency y Mobile-First*. Si extraemos la vista individual del blog de las tarjetas para aligerar la lectura, el listado general (feed) también debe desprenderse del diseño de "cuadernillo técnico" para mantener la consistencia de marca (DevRel). Un Hero gigante sin dashboard ni llamadas a la acción es peso muerto en la pantalla y daña la UX.

### 2026-05-14 — UX/UI: Refinamiento semántico del mensaje de error en orquestador maestro

**Contexto:** Cuando el auditor (`merci-audit.py`) u otra herramienta detectaba una infracción y devolvía un código de salida distinto de cero, el orquestador maestro (`merci-total.py`) mostraba el mensaje "El script ha fallado". Semánticamente es incorrecto: el script no falló, sino que cumplió su función de interceptar el error y detener el pipeline.

**Hecho:** Se modificó el mensaje de excepción en `scripts/merci/merci-total.py` para indicar que el proceso "reportó errores y bloqueó la ejecución".

**Motivo / criterio:** *Developer Experience (DX) y Precisión Semántica*. Un auditor que detiene un commit por deuda técnica es un caso de éxito del escudo DevSecOps, no un cuelgue del sistema. Ajustar el lenguaje evita falsas alarmas y refuerza la idea de que el pipeline actúa como un guardián activo.

### 2026-05-14 — Fix: Resolución de falso positivo en auditor de scripts y purga de estilo residual

**Contexto:** Al elevar a crítico el linter de estilos y auditar los archivos PHP, el pipeline `merci total` colapsó. Detectó un falso positivo de `UI_INLINE_SCRIPT` en `functions.php` y un estilo en línea real en el botón de retroceso de `woocommerce.php`.

**Hecho:**
- Se modificó un comentario en `src/wp-theme/merci-theme/functions.php` reemplazando `<script>` por `etiquetas script`.
- Se purgó el atributo `style="..."` del enlace `↑ Volver arriba` en `src/wp-theme/merci-theme/woocommerce.php`.

**Detalle técnico:** La expresión regular del auditor (`<script([^>]*)>(.*?)</script>`) capturaba accidentalmente la palabra exacta dentro de un comentario PHP y cerraba el grupo de captura docenas de líneas después en el bloque JSON-LD, simulando un script en línea gigante. Por otro lado, la etiqueta de WooCommerce conservaba estilos en línea que ya habían sido extraídos a `_footer.scss` en sesiones previas.

**Motivo / criterio:** *QA Assurance y Clean Code*. Evitar el uso de sintaxis HTML estricta dentro de los comentarios de PHP previene los falsos positivos en analizadores estáticos basados en expresiones regulares (RegEx). Purgar el estilo en WooCommerce homogeneiza las plantillas y permite al linter dar luz verde.

### 2026-05-14 — Fix: Resolución de ceguera del auditor sobre archivos PHP

**Contexto:** Al probar la nueva regla crítica de estilos en línea (`UI_INLINE_STYLE`) inyectando un estilo trampa en `index.php`, el pipeline `merci total` pasó con éxito sin detectar la infracción, revelando un punto ciego masivo.

**Hecho:** Se añadió la extensión `.php` a la constante global `TEXT_SUFFIXES` en `scripts/merci/merci-audit.py`.

**Detalle técnico:** Las funciones específicas de auditoría (`audit_php_smells`, `audit_inline_styles`) estaban correctamente programadas para evaluar archivos `.php`, pero el motor de recolección de archivos del repositorio (`iter_repo_files`) los ignoraba por completo al no estar incluidos en el listado de extensiones de texto permitidas. El auditor nunca abría los archivos de la capa dinámica.

**Motivo / criterio:** *QA Assurance*. Un linter ciego a ciertas extensiones genera un falso sentido de seguridad. Registrar y corregir este "punto ciego" garantiza que la capa dinámica (WordPress) vuelva a estar bajo la protección del escudo activo DevSecOps.

### 2026-05-14 — Refactor: Saneamiento BEM y erradicación de estilos en línea en WordPress

**Contexto:** Una revisión manual reveló la presencia de atributos `style="..."` (Inline CSS) inyectados en la vista de listado del blog (`index.php`), lo cual habría provocado un fallo bloqueante (`UI_INLINE_STYLE`) en la próxima auditoría de pre-commit. Además, existía acoplamiento de clases BEM (`.home-card__title--highlight` usado dentro de `.card`).

**Hecho:** Se limpió el HTML de `index.php` abstrayendo los estilos a un nuevo componente BEM (`_blog-feed.scss`) y se corrigieron los modificadores de las tarjetas en `_card.scss`.

**Detalle técnico:** Se creó el componente `.blog-feed` para controlar la cuadrícula vertical y el espaciado del listado. En las tarjetas, se sustituyó el modificador ajeno por `.card__title--highlight` y se proveyó la clase `.card__header` para mantener la semántica intacta y delegar toda la presentación al compilador SASS.

**Motivo / criterio:** *Shift-Left Quality y BEM estricto*. Mezclar clases de otros bloques (`.home-card`) rompe la encapsulación. Mantener estilos en línea ensucia el DOM y rompe la política estricta de "Cero Advertencias". Pagar esta pequeña deuda técnica antes del commit salva el pipeline de integración continua.

### 2026-05-14 — Refactor: Desacoplamiento arquitectónico BEM para el Blog

**Contexto:** Se detectó un antipatrón en la arquitectura SASS. El modificador `.card--blog` anulaba por completo todas las propiedades visuales de su bloque padre `.card` (bordes, fondos, sombras y padding).

**Hecho:** Se extrajo el diseño ligero del blog a su propio componente atómico `.blog-post`.

**Detalle técnico:** Se creó el archivo `src/scss/components/_blog-post.scss` y se eliminaron las reglas residuales en `_card.scss`. En `src/wp-theme/merci-theme/index.php`, se separó el renderizado del HTML mediante un condicional `if ( $es_blog_individual )` para aplicar las nuevas clases BEM (`blog-post__header`, `blog-post__content`) sin interferir con la estructura de las tarjetas de la biblioteca.

**Motivo / criterio:** *Single Responsibility Principle (SOLID) y BEM*. Si un modificador tiene que "resetear" el bloque original para funcionar, significa que conceptualmente no es una variación, sino un bloque distinto. Separarlo en su propio componente mejora la mantenibilidad, evita la guerra de especificidad y mantiene el código PHP limpio de lógicas de "toggle" de clases.

### 2026-05-14 — UX/UI: Rediseño ligero para la vista individual del Blog

**Contexto:** Las entradas del blog compartían la misma densidad visual y estructura pesada (cajas, bordes) que los cuadernillos técnicos, lo que contradecía su naturaleza de lectura rápida y marketing.

**Hecho:** Se implementó el modificador BEM `.article--blog` y se inyectó dinámicamente en la plantilla de WordPress.

**Detalle técnico:** Se limitó el ancho del contenedor a `65ch` (el estándar ergonómico para lectura), se eliminaron los bordes duros y se aumentó el interlineado (`1.8`). En WordPress (`index.php`), se aplicó la clase condicionalmente verificando `is_singular() && has_category('blog')`.

**Motivo / criterio:** *Design Follows Function* (El diseño sigue a la función). Un artículo de DevRel debe emular la experiencia de plataformas optimizadas para la lectura: minimalismo, foco en la tipografía y nula fricción cognitiva.

### 2026-05-14 — Docs: Registro de tarea pendiente (Comunicaciones Cifradas PGP)

**Contexto:** Se recuperó una deuda técnica olvidada: la página de contacto estática ya contaba con un bloque reservado para alojar la clave de comunicación. Era necesario registrar formalmente la implementación del sistema de comunicaciones cifradas (PGP) para no dejar ese aspecto de la plataforma incompleto.

**Hecho:** Se registró la tarea "Comunicaciones Cifradas (PGP)" en el `ROADMAP.md` inaugurando la Fase 3 de la Épica actual.

**Motivo / criterio:** *Zero Trust y Privacidad*. En un entorno DevSecOps, la confidencialidad en la comunicación con la autora es tan vital como la seguridad de la infraestructura. Convertirlo en una tarea rastreable evita que la idea quede en el olvido.

### 2026-05-14 — Docs: Planificación de telemetría y logging privado para Chaos Engineering

**Contexto:** Se detectó que los resultados de resiliencia del Agente Chaos (`merci-chaos.py`) eran efímeros (solo visibles en consola). Para madurar la postura SRE, se requería un registro persistente y visualización en tiempo real de los simulacros de ataque.

**Hecho:** Se registraron nuevas tareas en la Fase 2 de la Épica 3 del `ROADMAP.md` para implementar un log privado y exponer las métricas de Chaos hacia Prometheus/Grafana a través de `merci-sre.py`.

**Detalle técnico:** La bitácora privada de auditoría de resiliencia se alojará en `.privado/` (directorio protegido por la regla DLP del auditor maestro) para evitar exponer los vectores de ataque (payloads de la IA) en el repositorio público.

**Motivo / criterio:** *Deep Observability y Audit Trail*. Un sistema de Chaos Engineering pierde su valor estratégico si sus resultados no se auditan a lo largo del tiempo. Unir estos datos al agente SRE transformará a Grafana en un panel de "Salud y Resiliencia" real.

### 2026-05-14 — Conf: Despliegue de Tarea Cron para Buffer Social

**Contexto:** Tras validar el flujo de aprobación interactiva de posts (`estado_social: "aprobado"`), era necesario automatizar la emisión espaciada hacia LinkedIn sin intervención manual.

**Hecho:** Se configuró una tarea programada nativa en Ubuntu (`crontab`) para ejecutar `merci-linkedin.py --auto` cada 3 días a las 10:00 AM.

**Detalle técnico:** La instrucción `0 10 */3 * *` delega al sistema operativo la ejecución desatendida del script, el cual consume el entorno virtual local de forma absoluta (`.venv/bin/python`) y registra su actividad silenciosamente en un archivo de log (`/tmp/merci_linkedin.log`).

**Motivo / criterio:** *Automation y Fire-and-Forget*. Delegar la ejecución periódica al demonio `cron` del sistema es la vía más robusta y de menor consumo de recursos para tareas programadas (Batch), liberando completamente a la autora de la carga mental de publicar en redes sociales.

### 2026-05-14 — Feat: Autoinyección de enlaces canónicos en LinkedIn (Call to Action)

**Contexto:** Era necesario definir hacia dónde apuntar el tráfico de LinkedIn (web vs. repositorio) e incluir automáticamente el enlace en la publicación para maximizar la visibilidad del proyecto y la autoridad técnica.

**Hecho:** Se refactorizó `scripts/merci/merci-linkedin.py` para calcular e inyectar dinámicamente el enlace canónico del artículo en el texto del post, si este no contenía ya una URL.

**Detalle técnico:** El script evalúa si el texto en el bloque `<!-- linkedin: -->` contiene "http". Si no lo tiene, deduce la ruta de producción basándose en el YAML Frontmatter (resolviendo `/blog/slug/` para WordPress o `/biblioteca/slug.html` para el motor SSG) y añade un "Call to Action" estandarizado (`🔗 Lee el artículo completo aquí: ...`).

**Motivo / criterio:** *Traffic Routing y Single Source of Truth*. Redirigir el tráfico a `mercedev.es` en lugar de a GitHub demuestra empíricamente el rendimiento extremo (100/100) y la UX, convirtiendo la web en el activo central de marca personal. Automatizar la inserción de la URL garantiza enlaces perfectos sin requerir que la IA o la autora los escriban a mano en la nota original.

### 2026-05-14 — Docs: Registro de deuda técnica visual para el Blog

**Contexto:** Se ha observado que las entradas individuales del Blog tienen un aspecto visual demasiado denso, asemejándose a los Cuadernillos técnicos de la Biblioteca, lo que contradice el propósito de lectura ligera y marketing (DevRel).

**Hecho:** Se ha registrado la tarea de rediseño UI/UX en la Fase 1 de la Épica 3 del `ROADMAP.md`.

**Motivo / criterio:** *User Experience (UX)*. El diseño debe seguir a la función. Un artículo de marketing o reflexión rápida debe presentar una interfaz con menos carga cognitiva que un manual técnico.

**Siguiente paso o deuda:** Maquetar un estilo más ligero para la vista individual del blog en la próxima sesión.

### 2026-05-14 — Docs: Clarificación del SOP de Despliegue para Contenido Dinámico

**Contexto:** Tras una ejecución exitosa del pipeline local, se detectó que los nuevos artículos del blog no aparecían en el servidor de producción. Se diagnosticó una omisión en el procedimiento operativo estándar (SOP) de despliegue.

**Hecho:** Se actualizó `docs/flujo-publicacion-sop.md` para incluir el paso explícito de "conmutar entornos" en el archivo `.env` antes de ejecutar `merci wp` para el despliegue a producción.

**Detalle técnico:** El flujo ahora exige comentar las credenciales de `localhost` y activar las de producción en el `.env` antes de la sincronización Headless. Se documentó la necesidad de revertir este cambio tras el despliegue para mantener `localhost` como el entorno de trabajo por defecto.

**Motivo / criterio:** *Dev/Prod Parity y Fricción Cero*. La arquitectura de aislamiento funciona, pero el proceso manual de despliegue debe ser inequívoco. Documentar el "cambio de vías" en el SOP previene la confusión y asegura que el contenido local se propague a producción de forma controlada y deliberada.

### 2026-05-14 — Docs: Establecimiento de Anclaje Semántico para el Agente SSOT

**Contexto:** El Agente SSOT (Qwen 2.5 Coder) fallaba al marcar tareas completadas en el Roadmap si la redacción de la bitácora difería del texto original de la tarea, demostrando que opera principalmente por coincidencia de cadenas (*String Matching*) y no por inferencia semántica abstracta.

**Hecho:** Se establece la norma metodológica de "Anclaje Semántico": al documentar el cierre de un hito en la bitácora, el bloque "Hecho" debe incluir textualmente las palabras clave o la frase exacta de la tarea listada en el Roadmap.

**Detalle técnico:** Los SLMs locales carecen de la capacidad de deducción profunda de los modelos de frontera en la nube. Para evitar reescribir el historial o alterar el prompt masivamente, la autora adaptará la descripción del logro para que sirva de baliza (ancla) directamente reconocible por la IA.

**Motivo / criterio:** *AI Governance y SLM Psychology*. Aceptar las limitaciones cognitivas de la IA local y compensarlas con disciplina humana (redactando de forma predecible) es un patrón DevSecOps maduro que garantiza la sincronización documental (SSOT) sin sobreingeniería.

### 2026-05-14 — Docs: Expansión del Roadmap (Épica 5 - Showcase del Boilerplate)

**Contexto:** Surgió la necesidad de proveer a los futuros usuarios del `merci-boilerplate` una demostración en vivo (Live Demo) para que puedan visualizar el estado inmaculado y purista de la plantilla base antes de clonarla.

**Hecho:** Se inyectó la "Épica 5: Showcase y Distribución del Boilerplate" en el archivo `ROADMAP.md`.

**Detalle técnico:** Se planificó la evaluación de entornos de despliegue estático gratuitos (como GitHub Pages o un subdominio) para alojar la demostración, delegándolo a una fase futura para no saturar el trabajo actual.

**Motivo / criterio:** *Product Marketing y Prevención de Olvidos*. Un repositorio open-source adquiere mucho más valor si posee una representación visual activa. Registrar esta idea formalmente como una nueva Épica evita el "Scope Creep" (añadir tareas no planificadas al sprint actual) y asegura que no se pierda en el olvido.

### 2026-05-14 — Feat: Buffer de Publicación y Aprobación Asíncrona (LinkedIn)

**Contexto:** Publicar inmediatamente desde la terminal rompía la filosofía del "Buffer Social" programado. Se requería una cola asíncrona donde la autora revisa y aprueba los borradores, y un robot independiente los publica poco a poco sin intervención humana.

**Hecho:** Se refactorizó `scripts/merci/merci-linkedin.py` implementando dos modos de ejecución e inyectando un nuevo estado intermedio `estado_social: "aprobado"`.

**Detalle técnico:** Ejecutar `merci linkedin` (Modo Interactivo) ahora itera sobre los posts `en_cola`, los muestra por pantalla y pregunta si se aprueban, cambiando su estado a `aprobado`. Ejecutar `merci linkedin --auto` (Modo Cron) busca el post `aprobado` más antiguo, lo publica silenciosamente en LinkedIn y lo sella como `publicado_linkedin`. Se actualizó la métrica en `merci-sre.py` para sumar tanto lo pendiente de revisión como lo aprobado.

**Motivo / criterio:** *Asynchronous Operations y Fricción Cero*. Separar el momento de la "Curación" del momento de la "Emisión" es la piedra angular del marketing de contenidos. La autora aprueba un lote de artículos rápidamente, y una tarea en segundo plano puede encargarse de disparar el modo `--auto` periódicamente garantizando presencia continua en redes sociales sin carga cognitiva.

### 2026-05-14 — Docs: Actualización de SOP y Arquitectura de Agentes en manuales

**Contexto:** Tras la profunda reestructuración del flujo de trabajo (introducción de la bandeja unificada `incubacion/`, el enrutamiento inteligente por tema en `merci-promote` y el *Agent Chaining* con `merci-blogger.py`), los documentos fundacionales (`README.md`, `instrucciones.md` y `flujo-publicacion-sop.md`) habían quedado obsoletos (Document Drift).

**Hecho:** Se actualizaron los tres documentos maestros añadiendo a `merci-blogger.py` al inventario del ecosistema y reescribiendo el SOP para reflejar las nuevas mecánicas de incubación unificada, validación cruzada y Buffer Social de LinkedIn.

**Motivo / criterio:** *Single Source of Truth (SSOT)*. Una arquitectura brillante no sirve de nada si el manual de operaciones describe un sistema obsoleto. Reflejar el encadenamiento de agentes y las nuevas mecánicas de promoción en el "Runbook" oficial consolida la madurez de la Épica 3 y prepara el terreno para automatizaciones futuras.

### 2026-05-14 — Fix: Contextualización de prompts en orquestador de promoción

**Contexto:** Al promover artículos del Blog, el asistente interactivo (`merci-promote.py`) solicitaba metadatos innecesarios para un flujo cronológico (como "Tema/Estantería", "Alt de la portada" y "Fase del Roadmap"), generando fricción operativa y bloqueos (por la regla estricta de `alt_portada`).

**Hecho:** Se refactorizó la lógica interactiva en `scripts/merci/merci-promote.py` para adaptar los campos solicitados basándose en el metadato `tema`.

**Detalle técnico:** Se implementó el booleano `es_blog` evaluando si `"blog" in tema_actual.lower()`. Si es verdadero, el script oculta las preguntas estructurales de la biblioteca y puentea el bloqueo innegociable de WAI-ARIA para las portadas, solicitando exclusivamente la descripción y la fecha de publicación.

**Motivo / criterio:** *Fricción Cero y Arquitectura de la Información*. Un blog es un flujo cronológico, no estructural. Exigir estanterías o imágenes obligatorias a un contenido que por naturaleza suele ser de texto rápido añade burocracia innecesaria. Adaptar el orquestador al contexto del documento purifica la Experiencia del Desarrollador (DX).

### 2026-05-14 — Feat: Escudo de Referencias Cruzadas en Promoción (Shift-Left DAST)

**Contexto:** Al encadenar agentes, el Blogger genera posts de marketing que enlazan a cuadernillos técnicos. Si la autora promovía el post del blog antes que el cuadernillo original, el publicador Headless subiría un artículo a WordPress con un enlace roto (404), rompiendo la experiencia de usuario.

**Hecho:** Se inyectó un validador de referencias cruzadas en `scripts/merci/merci-promote.py`.

**Detalle técnico:** El script escanea el cuerpo del documento en busca de URLs internas (`https://mercedev.es/biblioteca/...`). Si encuentra alguna, calcula dinámicamente todos los slugs (`slugify`) de los documentos actualmente en producción (`biblioteca/` y `art-de-cote/`). Si el enlace destino no existe en producción, aborta la promoción con un mensaje de bloqueo didáctico.

**Motivo / criterio:** *Shift-Left Quality y Dependency Enforcing*. Prevenir un error antes de que se compile es mejor que detectarlo después. Forzar el orden cronológico de promoción (primero el documento base, luego el marketing) garantiza que WordPress nunca reciba un enlace hacia un recurso estático inexistente.

### 2026-05-14 — Test: Validación End-to-End de Máquina de Estados y Agent Chaining

**Contexto:** Tras implementar el encadenamiento de agentes (Bibliotecario -> Blogger) y la métrica de SRE, era vital confirmar que la cadena completa funcionaba sin fricciones y respetando la máquina de estados documental.

**Hecho:** Se ejecutó una prueba limpia partiendo de una nota cruda. El Bibliotecario generó el cuadernillo, el Blogger generó el post de marketing, y se validó que los documentos nacen en `incubacion`.

**Motivo / criterio:** *State Machine Integrity*. Confirmar empíricamente que los documentos en incubación son invisibles para la telemetría de Grafana y la cola de LinkedIn demuestra que la arquitectura es sólida. Un documento solo entra en la cola social cuando la autora lo promueve explícitamente a `publicado`, previniendo la publicación de enlaces rotos (404) hacia la web matriz.

### 2026-05-14 — Fix: Resolucion de fallos End-to-End en encadenamiento (Blogger)

**Contexto:** Al validar el "Agent Chaining" entre el Bibliotecario y el Blogger, el pipeline colapsó con `UnboundLocalError`. Además, la reescritura de los metadatos YAML inyectaba comillas residuales corrompiendo el parser.

**Hecho:** Se refactorizaron las expresiones regulares (`.*?` cambiado por `[^"'\n]*`) en `scripts/merci/merci-blogger.py` y se corrigió el alcance del mensaje de consola para archivar notas.

**Detalle técnico:** La expresión regular *non-greedy* con captura opcional en los extremos provocaba que el reemplazo no consumiera la última comilla escrita por Ollama, concatenando el estado forzado (`"incubacion"incubacion"`). Colocar el mensaje de éxito fuera del ámbito exclusivo de las notas crudas provocaba la llamada a una variable inexistente.

**Motivo / criterio:** *End-to-End QA*. Testear flujos aislados es engañoso. La orquestación revela los límites del código de integración. Estos parches garantizan que la cadena de montaje asuma documentos generados dinámicamente sin bloqueos.

### 2026-05-14 — Refactor: Estandarización de nomenclatura para artículos del Blog

**Contexto:** Los artículos generados por el Agente Blogger (`merci-blogger.py`) se guardaban en la incubadora únicamente con el título slugificado, rompiendo la consistencia visual y de nomenclatura establecida por el Agente Bibliotecario (que usa prefijos como `cuadernillo-`, `compendio-`, `art-de-cote-`).

**Hecho:** Se parcheó `scripts/merci/merci-blogger.py` para inyectar automáticamente el prefijo `blog-` al generar el nombre del archivo físico (`filename = "blog-" + slugify(titulo) + ".md"`).

**Motivo / criterio:** *Consistency y Fricción Cero*. Mantener un estándar de nomenclatura estricto en la bandeja de entrada unificada (`incubacion/`) permite a la autora identificar instantáneamente la tipología y el destino de un documento con solo mirar su nombre de archivo en el IDE.

### 2026-05-14 — Fix: Enlaces relativos a la raíz en Agent Chaining (Dev/Prod Parity)

**Contexto:** Los artículos promocionales generados por el Blogger incluían una URL absoluta (`https://mercedev.es/...`) hacia el documento técnico original. Esto rompía la experiencia de desarrollo local, ya que al hacer clic en el entorno de pruebas, el usuario era redirigido al servidor de producción donde el documento aún no existía (Error 404).

**Hecho:** Se refactorizó la generación de la variable `url_promocion` en `scripts/merci/merci-blogger.py` para utilizar rutas relativas a la raíz (ej. `/biblioteca/slug.html`).

**Motivo / criterio:** *Agnosticismo de Entorno y Dev/Prod Parity*. El contenido en formato Markdown debe ser independiente del dominio donde se aloje. Utilizar rutas relativas a la raíz garantiza que el enlace resuelva perfectamente a `localhost:8000` durante el desarrollo y a `mercedev.es` en producción, sin necesidad de modificar el código fuente.

### 2026-05-14 — UX/UI: Rediseño del Blog a formato cronológico puro (Limpieza de index.php)

**Contexto:** La plantilla de WordPress (`index.php`) agrupaba visualmente los posts por categorías, emulando las estanterías de la Biblioteca. Esto rompía el paradigma de un blog tradicional, que debe mostrar un flujo de lectura vertical y cronológico, añadiendo ruido visual a las publicaciones de marketing.

**Hecho:** Se refactorizó drásticamente el archivo `src/wp-theme/merci-theme/index.php`.

**Detalle técnico:** Se extirpó el bucle de agrupación por `$tema`, la generación del menú interno (`library-nav`) y la envoltura en cuadrícula (`home-grid`). En su lugar, se implementó un bucle estándar `while (have_posts())` que renderiza las tarjetas apiladas verticalmente en una sola columna con `max-width: 800px` para una legibilidad óptima. También se eliminó el condicional huérfano de `Art de Coté`, puesto que dicha sección ahora es servida al 100% por el motor SSG.

**Motivo / criterio:** *Separation of Concerns* (Separación de responsabilidades). La Biblioteca ordena el conocimiento; el Blog emite novedades. Diferenciar la UI de ambos espacios clarifica la intención de la lectura. Reducir la lógica PHP en el tema acelera el TTFB y simplifica el mantenimiento.

### 2026-05-14 — Feat: Métrica SRE para Buffer de LinkedIn en Grafana

**Contexto:** Era necesario vigilar la cantidad de posts disponibles ("munición") en la cola de LinkedIn para configurar futuras alertas SRE cuando el buffer se estuviera agotando.

**Hecho:** Se instrumentó `scripts/merci/merci-sre.py` inyectando la métrica `merci_linkedin_queue_total`.

**Detalle técnico:** El agente escanea los directorios de producción (`blog`, `biblioteca`, `art-de-cote`) y cuenta cuántos archivos poseen simultáneamente `estado: "publicado"` y `estado_social: "en_cola"`, exponiendo el valor como un *Gauge* a Prometheus.

**Motivo / criterio:** *Observabilidad y DevRel*. Mantener una métrica en tiempo real permite delegar la preocupación de publicar a los sistemas de alerta (Grafana Alerting). Esto concluye formalmente la infraestructura de la Fase 2 (Observabilidad y Alertas SRE).

### 2026-05-14 — Fix: Enrutamiento Dinámico por Tema (SSOT) en Promote

**Contexto:** Los artículos generados por la IA o creados en la nueva bandeja unificada (`laboratorio/incubacion/`) perdieron la capacidad de enrutarse correctamente al ser promovidos. El orquestador `merci-promote.py` decidía el destino basándose en la carpeta de origen, lo que provocaba que todo acabara en la `biblioteca/`.

**Hecho:** Se refactorizó la lógica de enrutamiento en `scripts/merci/merci-promote.py`.

**Detalle técnico:** El destino (`blog/`, `art-de-cote/` o `biblioteca/`) se deduce ahora leyendo el campo `tema:` extraído dinámicamente del YAML Frontmatter.

**Motivo / criterio:** *SSOT (Single Source of Truth)*. La estructura de carpetas local es efímera, pero el metadato es inmutable. Confiar el destino de producción a lo que dicte el YAML Frontmatter permite unificar toda la redacción en una única bandeja de entrada (`incubacion/`) sin fricción operativa.

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

**Hecho:** 
- Se refactorizó `scripts/merci/merci-linkedin.py` como un "Gatekeeper".
- Tarea completada: Añadir el campo `estado_social: "en_cola"` al YAML Frontmatter en las plantillas Markdown base (`plantilla-blog.md`, `plantilla-art-de-cote.md`).

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
