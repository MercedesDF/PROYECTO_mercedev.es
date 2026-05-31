# Bitácora del proyecto mercedev.es — Épica 8: Refactorización y Buenas Prácticas

## Para qué sirve este archivo
Bitácora activa para registrar las decisiones, refactorizaciones y limpiezas de código correspondientes a la Épica 8 del Roadmap maestro (Refactorización, mejora y revisión de buenas prácticas de los scripts).

---

## Registro cronológico

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