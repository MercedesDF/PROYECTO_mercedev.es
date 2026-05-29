# Bitácora del proyecto mercedev.es — Épica 8: Refactorización y Buenas Prácticas

## Para qué sirve este archivo
Bitácora activa para registrar las decisiones, refactorizaciones y limpiezas de código correspondientes a la Épica 8 del Roadmap maestro (Refactorización, mejora y revisión de buenas prácticas de los scripts).

---

## Registro cronológico

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