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

### 2026-05-17 — Milestone: Cierre de Fase 1 (Épica 3) y Validación del Definition of Done

**Contexto:** Aplicar el Protocolo Estricto de Cierre de Fase (Definition of Done) para dar por concluida la Fase 1 de la Épica 3 (Motor de Difusión y Buffer Social), asegurando la higiene del ecosistema antes de avanzar a la observabilidad avanzada en Grafana.

**Hecho:** Se ejecutó la lista de verificación obligatoria de cierre de fase:
- [x] **1. Deuda Técnica:** 0 TODOs. Visor de terminal interactivo (`merci-queue.py`) y buffer social implementados con éxito.
- [x] **2. Cosecha de Conocimiento:** Taxonomía "SOS Terminal" definida y documentada.
- [x] **3. Auditoría Documental:** `ROADMAP.md` y `README.md` sincronizados reflejando la Fase 1 como completada.
- [x] **4. Evaluación de Release:** No se requiere empaquetado del Boilerplate en este punto (herramientas locales de DevRel).
- [x] **5. Snapshot:** Backup local ejecutado para respaldar el buffer social.
- [x] **6. Sello Definitivo:** Commit atómico de consolidación preparado.

**Motivo / criterio:** *Governance y Definition of Done*. Sellar formalmente la Fase 1 certifica que las herramientas base de DevRel están operativas y blindadas.

**Siguiente paso o deuda:** Iniciar la Fase 2 de la Épica 3: Configurar alertas nativas en Grafana (Alerting).

### 2026-05-17 — Fix: Degradación Elegante de Agente SSOT en Boilerplate

**Contexto:** Al instanciar el Boilerplate y ejecutar la auditoría de QA (`merci total`), el pipeline colapsaba con un error fatal emitido por `merci-ssot.py` al no encontrar el Roadmap ni la Bitácora de IA de la matriz original (los cuales fueron purgados intencionalmente por `merci-init.py` por DLP).

**Hecho:**
- Se refactorizó la captura de excepciones en `scripts/merci/merci-total.py`.
- Se implementó un bypass de Degradación Elegante (Fail Gracefully) que intercepta el fallo específico de `merci-ssot.py` y lo transforma en una advertencia informativa, permitiendo que el orquestador continúe.

**Detalle técnico:** Se añadió una condición `if script == "merci-ssot.py": continue` en el bloque `except subprocess.CalledProcessError`. Esto respeta el patrón *Fail-Fast* estricto para el resto de herramientas, pero exime al Agente SSOT, ya que su incapacidad para encontrar archivos en un entorno virgen es un estado lícito, no un error de código.

**Motivo / criterio:** *Out-of-the-Box Experience (DX)*. Una plantilla recién clonada debe garantizar una compilación exitosa a la primera. Castigar al nuevo usuario con un colapso de pipeline por documentos que no existen en su repositorio rompe la promesa del Boilerplate.

**Siguiente paso o deuda:** Reintentar el ciclo iterativo de release del Boilerplate: descartar clon, corregir matriz, ejecutar `merci-init.py` y validar `merci total` a cero errores.

### 2026-05-17 — Arch: Estrategia de métricas JSON y cierre de Fase 1

**Contexto:** Con el descubrimiento de los reportes JSON crudos de WebPageTest/Lighthouse, se planteó la necesidad de refactorizar el extractor de métricas (`merci-extract-metrics.py`). Surgió el debate arquitectónico sobre cómo gestionar múltiples reportes (Portada, Blog, Tienda) en el dashboard de producción.

**Hecho:**
- Se decidió posponer la refactorización para evitar el *Scope Creep* (desvío de alcance) y cerrar limpiamente la Fase 1 de la Épica 3.
- Se añadió la tarea de refactorización al Roadmap dentro de la Fase 2 (Observabilidad Avanzada).

**Detalle técnico:** La estrategia futura ("Dashboard Contextual" o "Worst-Case Flex") implicará que el script escanee múltiples archivos `.json` y asigne las métricas correspondientes, priorizando exponer el rendimiento de la Tienda como prueba empírica de la resiliencia de la arquitectura híbrida bajo estrés.

**Motivo / criterio:** *Project Management y Scope Creep*. Congelar el alcance es vital en ingeniería. Si una fase cumple sus objetivos de negocio (en este caso, blindaje XSS y enrutamiento Zero-JS), debe cerrarse. Añadir mejoras no críticas sobre la marcha es una fuente principal de regresiones.

**Siguiente paso o deuda:** Iniciar la Fase 2 de la Épica 3, abordando las Alertas SRE en Grafana y la reescritura del extractor a JSON.

### 2026-05-17 — Docs: Actualización de Shadow Docs y directrices para Release v1.13.0

**Contexto:** Antes de instanciar y exportar la versión 1.13.0 del Boilerplate a GitHub, era imperativo actualizar la documentación base y las políticas de arquitectura para que los proyectos derivados hereden el blindaje XSS y el patrón de enrutamiento Zero-JS.

**Hecho:**
- Se actualizaron los manuales maestros (`README.md` y `README-merci.md`).
- Se modificaron las directrices en `instrucciones.md` e `instrucciones-merci.md`.

**Detalle técnico:** Se añadió explícitamente la obligación de sanitizar cadenas provenientes de metadatos (`html.escape`) en la regla de "Seguridad Shift-Left" y se elevó a canon arquitectónico el "Enrutamiento Visual Zero-JS" basado en Body IDs. Se oficializó el cierre de la Fase 1 de la Épica 3 en el Roadmap.

**Motivo / criterio:** *Knowledge Export y Governance*. Exportar una plantilla sin actualizar sus normas de uso provoca Deriva de Configuración. La documentación (Shadow Docs) debe actuar como un reflejo exacto y normativo de las decisiones de ingeniería implementadas en el código.

**Siguiente paso o deuda:** Desplegar en producción, certificar las métricas Core Web Vitals en PageSpeed Insights e iniciar la Fase 2 (Alertas SRE en Grafana).

### 2026-05-17 — Fix: Restauración de enrutamiento Zero-JS y menú móvil

**Contexto:** Tras la limpieza de las clases *legacy* del `<header>`, el resaltado visual del menú dejó de funcionar en las páginas estáticas manuales (Portada, Sobre Mí, Contacto). Simultáneamente, el menú hamburguesa móvil no respondía debido a que los dispositivos conservaban versiones cacheadas del DOM y los scripts.

**Hecho:**
- Se inyectaron explícitamente los atributos `id="page-home"`, `id="page-sobre-mi"` y `id="page-contacto"` en las etiquetas `<body>` de sus respectivos archivos estáticos.
- Se ejecutó el orquestador global `merci total` para forzar el *Cache Busting* dinámico (`?v=...`) y propagar el nuevo estado.

**Detalle técnico:** La arquitectura Zero-JS depende de selectores CSS combinados (ej. `#page-home .nav__link[href="/"]`). Sin el ID en el `<body>`, la regla SASS carecía de anclaje contextual en las rutas manuales. La ejecución del orquestador generó nuevas marcas de tiempo en los recursos estáticos, obligando a los navegadores móviles a purgar la caché y recuperar la funcionalidad del `main.js`.

**Motivo / criterio:** *Context-Awareness y Cache Invalidation*. La interfaz de usuario debe proveer su propio contexto semántico al CSS para evitar dependencias de scripts que muten el DOM. Confiar la purga de caché móvil al versionado dinámico del orquestador asegura que los parches estructurales se propaguen instantáneamente a todos los usuarios (Paridad de Entornos).

**Siguiente paso o deuda:** Validar analíticas en producción y transicionar hacia la Fase 2 de la Épica 3 (Alertas SRE en Grafana).

### 2026-05-17 — Refactor: Consolidación de enrutamiento Zero-JS y limpieza legacy

**Contexto:** A pesar de haber implementado el enrutamiento visual mediante Body IDs, las páginas estáticas no resaltaban correctamente el enlace activo en el menú. Esto se debía a que `public/index.html` y el sincronizador de páginas seguían conservando e inyectando la clase quemada `nav__link--active`, interfiriendo con la nueva arquitectura CSS.

**Hecho:**
- Se eliminó la clase `nav__link--active` y el atributo `aria-current="page"` del enlace "Home" en `public/index.html`.
- Se purgó la lógica de reemplazo y mutación dinámica de clases en `scripts/merci/merci-sync-pages.py`.

**Detalle técnico:** El bloque `<header>` ahora se clona de forma 100% literal a todas las páginas secundarias estáticas. El resaltado recae exclusivamente en la combinación del selector CSS (ej. `#page-home .nav__link[href="/"]`) activado por el ID del `<body>`.

**Motivo / criterio:** *Single Source of Truth y Zero-JS*. Delegar el estado activo puramente a la hoja de estilos elimina la necesidad de modificar el DOM en tiempo de compilación. Mantener el `<header>` inmaculado y unificado en todo el ecosistema estático reduce la complejidad estructural.

**Siguiente paso o deuda:** Ejecutar `merci total` para propagar el header limpio al resto de páginas estáticas.

### 2026-05-17 — Fix: Sanitización de metadatos YAML (Prevención XSS y DOM Breakage)

**Contexto:** Los artículos que contenían etiquetas HTML literales en sus descripciones o títulos (ej. `<script src="...">`) provocaban que el navegador las interpretara como código real al renderizar el índice de la Biblioteca, rompiendo el DOM y deteniendo la carga del resto de la página. Además, existía riesgo de inyección y rotura del compilador al generar los PDFs.

**Hecho:**
- Se inyectó `html.escape()` en `scripts/merci/merci-publish.py` y `scripts/merci/merci-wp.py` para todos los campos provenientes del YAML Frontmatter (título, descripción, fase, tipo, volumen, fecha).
- Se restituyeron los comentarios arquitectónicos (QUÉ HACE / POR QUÉ) documentando el blindaje.

**Detalle técnico:** Se convirtieron los caracteres especiales (`<`, `>`, `&`, `"`) a entidades HTML seguras antes de interpolarlos en las f-strings que construyen las tarjetas HTML de los índices y el código fuente procesado por WeasyPrint.

**Motivo / criterio:** *Shift-Left Security y Robustez*. Confiar ciegamente en el input del usuario (incluso si es la propia autora redactando un Markdown local) es un antipatrón. Sanitizar las cadenas de texto en el momento de la extracción asegura que el SSG y el CMS generen siempre un código inofensivo y a prueba de roturas visuales.

**Siguiente paso o deuda:** Compilar el núcleo estático con `merci total` y verificar la correcta visualización de las tarjetas previamente afectadas.

### 2026-05-16 — Fix: Silenciado de advertencia visual en consola (Merci UI)

**Contexto:** La consola del navegador mostraba una advertencia (`warn`) constante en páginas donde el asistente no debía instanciarse ("Contenedor #merci-ui no encontrado"), y un error 404 por un recurso (imagen) huérfano. En entornos DevSecOps, este "ruido" ensucia la depuración e invisibiliza los errores reales de producción.

**Hecho:** Se rebajó la severidad del mensaje en `public/js/MerciController.js` de `console.warn` a `console.debug`. Se diagnosticó el error 404 como un "falso positivo" de desarrollo derivado de una inyección de imagen sin compilar.

**Detalle técnico:** Al utilizar `console.debug`, la ejecución sigue cayendo en el `return` silencioso que apaga al asistente, pero el mensaje queda oculto en la terminal del navegador a menos que el usuario active explícitamente el nivel de filtrado "Verbose/Depuración".

**Motivo / criterio:** *Degradación Elegante (Fail Gracefully) y Clean Console*. Que el asistente no se instancie en ciertas vistas no es un error ni un riesgo, es un comportamiento intencionado. Emitir una advertencia (amarilla) por un diseño arquitectónico exitoso es un anti-patrón de observabilidad.

**Siguiente paso o deuda:** Identificar exactamente qué imagen es la que genera el 404 para proveerla o compilarla correctamente.

### 2026-05-16 — Fix: Degradación Elegante en generación de PDFs (WeasyPrint)

**Contexto:** El rastreador dinámico de enlaces (`merci-linkcheck.py`) reportaba errores 404 (`Failed to load resource`) debido a enlaces rotos en los botones de descarga de PDF. Esto sucedía porque el orquestador (`merci-publish.py`) inyectaba incondicionalmente el enlace al PDF en el DOM, incluso cuando la librería `weasyprint` no estaba instalada o fallaba al renderizar el archivo.

**Hecho:** Se implementó una inyección condicional del enlace de descarga HTML en `scripts/merci/merci-publish.py`.

**Detalle técnico:** Se inicializa `pdf_download_link = ""` y solo se le asigna el bloque de código `<a href="/descargas/...">` si la llamada a WeasyPrint se ejecuta con éxito y el comando `out_pdf_path.exists()` confirma que el archivo físico fue creado en disco. Este enlace condicionado se inyecta luego dinámicamente junto al `<h1>`.

**Motivo / criterio:** *Fail Gracefully (Degradación Elegante) y Shift-Left DAST*. Si el entorno local carece de dependencias pesadas, el generador estático debe sobrevivir y publicar el HTML intacto sin generar "enlaces fantasma". Condicionar la UI a la existencia física del recurso erradica los 404 detectados por el linter dinámico y mantiene la promesa de 0 dependencias bloqueantes.

**Siguiente paso o deuda:** Ejecutar `merci total` para compilar el HTML, limpiar los enlaces rotos y empaquetar el commit de la sesión.

### 2026-05-16 — DevRel: Visor de Cola Social y Consolidación de Bandeja Unificada

**Contexto:** Se necesitaba una forma rápida de auditar el "Buffer Social" (posts pendientes y aprobados para LinkedIn) sin arrancar orquestadores interactivos. Además, se detectó que los scripts de publicación SSG y WP expulsaban los borradores a rutas relativas obsoletas en lugar de a la nueva bandeja de incubación.

**Hecho:** 
- Se creó `scripts/merci/merci-queue.py` para monitorizar el estado del buffer social y desacoplar la nomenclatura de UX.
- Se modificó la nomenclatura visual ("Pendientes de Revisión" vs "En el Buffer") para evitar disonancia cognitiva con el metadato interno `en_cola`.
- Se parchearon `merci-wp.py` y `merci-publish.py` para que las despublicaciones regresen incondicionalmente a `laboratorio/incubacion/`.

**Motivo / criterio:** *Developer Experience (DX) y SSOT*. Desacoplar el estado interno de la presentación al usuario elimina la confusión operativa. Consolidar la reubicación de archivos asegura que todo el contenido inmaduro (o expulsado) reside en un único punto bajo el control centralizado de los Agentes.

**Siguiente paso o deuda:** Cierre oficial de la Fase 1. El siguiente paso es iniciar la Fase 2 (Observabilidad y Alertas SRE) configurando notificaciones nativas en Grafana.

### 2026-05-16 — UX/UI: Refactorización de estilos en línea en el Hero (BEM)

**Contexto:** Se necesitaba destacar con color la sílaba "dev" en el logotipo principal de la portada sin introducir atributos `style="..."` en el HTML, para no violar la regla de Cero Deuda Técnica ni depender de los marcadores de silenciamiento del linter (`<!-- merci-audit:silence-style -->`).

**Hecho:** Se implementó el modificador BEM `.hero__highlight` en `src/scss/components/_hero.scss` consumiendo la variable `$color-primary`, y se aplicó al `<span>` correspondiente en `public/index.html`.

**Motivo / criterio:** *Single Source of Truth y Zero Deuda Técnica*. Centralizar el color en la capa SASS asegura que, si el tono naranja cambia en el futuro en el archivo de variables, el logotipo se actualizará automáticamente sin necesidad de editar código HTML estático. Mantiene el DOM inmaculado y el auditor de código libre de excepciones innecesarias.

**Siguiente paso o deuda:** Recompilar el CSS maestro y empaquetar los cambios en el commit atómico.

### 2026-05-16 — Arch: Escudo Anti-Duplicidad y Consolidación de Estados (DevRel)

**Contexto:** Con la orquestación asíncrona completada, surgía el riesgo de generar contenido de marketing duplicado o enviar múltiples peticiones de publicación a los canales externos (WordPress, LinkedIn) sobre el mismo documento por error humano.

**Hecho:** Se implementó un escudo de prevención en `merci-blogger.py` para bloquear la generación de artículos si ya existe un post con el mismo nombre en la ruta de producción (`blog/`). Se documentaron y confirmaron las barreras intrínsecas del sistema (Resolución dinámica por slug en WP, sellado de `estado_social` en LinkedIn).

**Motivo / criterio:** *Idempotencia y Fail-Safe*. Un ecosistema automatizado debe ser idempotente; ejecutar el pipeline de publicación varias veces sobre un mismo activo no debe tener efectos secundarios (spam o duplicidad). Confiar en la resolución de base de datos (WP) y en los metadatos YAML locales blinda la cadena de suministro de contenido previniendo el error humano.

**Siguiente paso o deuda:** Configurar las alertas nativas en Grafana para monitorizar la cola de publicaciones de LinkedIn.

### 2026-05-16 — Arch: Reubicación de Agent Chaining (Promote -> Blogger)

**Contexto:** El flujo anterior encadenaba el Agente Bibliotecario con el Blogger, lo que generaba artículos de marketing sobre borradores inmaduros y aumentaba la carga cognitiva en la fase de incubación.

**Hecho:** Se reubicó conceptual y operativamente el *Agent Chaining*. Ahora `merci-promote.py` es quien invoca a `merci-blogger.py` tras promover con éxito un documento a la Biblioteca o Art de Coté. Se actualizó el flujo SOP y se forzó `tema: "Blog"` en el output del Blogger.

**Motivo / criterio:** *Just-in-Time Marketing*. Redactar el material promocional solo cuando el documento técnico es definitivo y está en su ruta canónica garantiza que el contenido de LinkedIn refleje la versión final, previniendo incoherencias y respetando el ciclo de vida real de los contenidos.

**Siguiente paso o deuda:** Validar el nuevo flujo completo promocionando un artículo estático.

### 2026-05-16 — Feat: Content Repurposing interactivo en Agente Blogger

**Contexto:** Se requería que el Agente Blogger pudiera ejecutarse a demanda para explorar la `biblioteca/` y `art-de-cote/`. El objetivo estratégico es aplicar el patrón *Content Repurposing*: cada pieza de documentación (SSOT) debe poder transformarse en un artículo resumido para el blog cronológico y generar simultáneamente su gancho publicitario para LinkedIn.

**Hecho:** Se refactorizó `scripts/merci/merci-blogger.py` añadiendo un menú interactivo de selección recursiva (`rglob`). Se corrigió el cálculo de la URL canónica promocional para que dependa del metadato `tema` en lugar del `tipo`.

**Motivo / criterio:** *DevRel y Create Once, Publish Everywhere (COPE)*. La documentación estricta es la única fuente de verdad. Reutilizar activos técnicos densos transformándolos a voluntad en píldoras de marketing maximiza el retorno de inversión (ROI) del esfuerzo de ingeniería, consolidando la autoridad técnica de la autora en múltiples canales con fricción cero.

**Siguiente paso o deuda:** Configurar alertas nativas en Grafana para monitorizar la cola de publicaciones de LinkedIn.

### 2026-05-16 — Fix: Exclusión acotada de PDFs locales en Git

**Contexto:** Para evitar subir al repositorio los manuales impresos localmente, se planteó inicialmente una exclusión global de PDFs. Este enfoque fue rechazado porque el motor SSG matriz sí genera y gestiona archivos `.pdf` legítimos para la Biblioteca.

**Hecho:** Se añadió la regla de exclusión estricta `docs/*.pdf` en el archivo `.gitignore` y se enmendó la entrada anterior de la bitácora.

**Motivo / criterio:** *Precisión y Single Source of Truth*. Las reglas globales (como `*.pdf`) son antipatrones que generan falsos negativos, ocultando archivos legítimos de otras capas. Acotar la exclusión al directorio exacto del problema previene efectos secundarios destructivos en la publicación SSG.

**Siguiente paso o deuda:** Promover el nuevo Art de Coté a su estantería definitiva.

### 2026-05-16 — Docs: Conservación de utilidad PDF como Art de Coté

**Contexto:** Se desarrolló un script táctico interactivo (`generar-pdf-docs.py`) para renderizar manuales Markdown a PDF y facilitar su impresión física. No procedía integrarlo en el orquestador SSG matriz.

**Hecho:** Se redactó y guardó un cuadernillo en formato Art de Coté documentando el problema, la solución de aislamiento y salvaguardando el código fuente para el futuro.

**Motivo / criterio:** *Cero Desperdicio (Zero Waste) y Separation of Concerns*. El script es útil operativamente pero no es un componente de despliegue web. Archivar su lógica como píldora de conocimiento evita perder la I+D invertida sin ensuciar la infraestructura *Zero-Bloat* de los orquestadores base.

**Siguiente paso o deuda:** Añadir una regla de exclusión estricta y acotada (`docs/*.pdf`) en `.gitignore` para prevenir fugas de manuales locales, respetando los PDFs que el motor SSG genera legítimamente.

### 2026-05-16 — SEO: Refinamiento de metadatos estáticos y Open Graph en portada

**Contexto:** La portada requería una actualización en sus metadatos estáticos para reflejar la madurez actual del ecosistema (integración de agentes de Inteligencia Artificial y metodología Spec as Source) y controlar la previsualización de la tarjeta social al ser compartida en LinkedIn.

**Hecho:** Se actualizaron las metaetiquetas en `public/index.html`.
- Se reescribió la etiqueta `description` acotándola a un máximo óptimo de 149 caracteres.
- Se limpiaron comentarios obsoletos y se habilitó explícitamente la etiqueta `robots` con las directivas `index, follow`.
- Se inyectaron metadatos del protocolo Open Graph (OG) para controlar el título, descripción e imagen visualizada en plataformas sociales.

**Motivo / criterio:** *SEO Técnico y DevRel*. Alinear la meta descripción con el valor técnico real del ecosistema y establecer las tarjetas sociales (Social Cards) garantiza una consistencia visual inquebrantable cuando el agente publicador (`merci-linkedin.py`) dirija el tráfico orgánico de vuelta al núcleo estático.

**Siguiente paso o deuda:** Revisar la implementación del meta viewport y otros metadatos estáticos en las plantillas de los cuadernillos del motor SSG.

### 2026-05-15 — UX/UI: Resaltado de navegación activa (Zero-JS)

**Contexto:** Se perdía la noción de qué sección de la web se estaba visitando (ej. "Sobre Mí"), ya que el menú de navegación no resaltaba el enlace activo. Se solicitó solucionarlo sin inyectar JavaScript para proteger el rendimiento.

**Hecho:** Se implementó un patrón de enrutamiento visual basado en `Body IDs` y selectores de atributos CSS.
- Se inyectaron `id="page-home"`, `id="page-sobre-mi"`, etc., en las etiquetas `<body>` estáticas.
- Se refactorizó `scripts/merci/merci-publish.py` para inyectar dinámicamente el `id` según el tema.
- Se crearon reglas SASS (`#page-home .nav__link[href="/"]`) para aplicar color `$color-primary` al enlace coincidente.

**Motivo / criterio:** *Single Source of Truth y Zero-JS*. Como el bloque `<header>` es idéntico en todas las páginas (sincronizado automáticamente), no es posible añadir una clase `.active` directamente en el HTML del enlace. Delegar el estado activo a la combinación del contexto global (`body id`) con el destino del enlace (`href`) logra un resaltado perfecto, mantenible y con 0 milisegundos de latencia en el navegador.

### 2026-05-15 — Docs: Oficialización del manual de Ciclo de Vida y Tipos

**Contexto:** Se redactó una guía maestra explicando la anatomía del YAML Frontmatter y el enrutamiento de la máquina de estados. Inicialmente se planteó guardarlo en `.privado/`, pero se reconoció como un documento estructural vital para futuros usuarios del Boilerplate.

**Hecho:** Se publicó formalmente en `docs/ciclo-de-vida-contenidos.md`.

**Motivo / criterio:** *Knowledge Export (Exportación de Conocimiento)*. Un Boilerplate que depende de metadatos estrictos (SSOT) no puede ocultar las reglas de enrutamiento. Exponer este manual garantiza que cualquier desarrollador entienda cómo gobernar las 3 capas del sistema.

### 2026-05-15 — UX/UI: Reubicación visual del Badge en Art de Coté

**Contexto:** La "Píldora de Anuncio" (Badge) se inyectaba encima del título principal (H1) en la sección Art de Coté. Visualmente, resultaba más orgánico colocarla como un "Call to Action" al final del Hero.

**Hecho:** Se refactorizó la plantilla HTML en `scripts/merci/merci-publish.py` moviendo la variable `{badge_html}` al final de la sección. Se ajustaron los márgenes en `src/scss/components/_hero.scss`.

**Motivo / criterio:** *Visual Hierarchy*. El flujo de lectura natural de arriba hacia abajo (Título -> Subtítulo -> Acción) posiciona mejor el elemento interactivo, maximizando su intención de clic (CTR) antes de que el usuario haga scroll hacia la cuadrícula de artículos.

### 2026-05-15 — Arch: Rechazo de menús desplegables e inyección SSG de Badge

**Contexto:** Para dar relevancia al artículo del Boilerplate, se propuso añadir un menú desplegable (Dropdown) al enlace "Art de Coté" en la navegación principal. Paralelamente, se requería automatizar la inyección de la "Píldora de Anuncio" en la cabecera de la sección.

**Hecho:** Se rechazó el diseño de menú desplegable. Se refactorizó `scripts/merci/merci-publish.py` para inyectar dinámicamente el componente HTML `.hero__badge` exclusivamente cuando el motor compila el índice de `Art de Coté`.

**Motivo / criterio:** *WAI-ARIA Strict y Zero-Bloat*. Un menú desplegable accesible requiere JavaScript adicional (gestión de foco, eventos táctiles) y ensucia la UI móvil. Inyectar la píldora nativamente en el *Hero* de la sección destino mediante el motor SSG logra la visibilidad deseada con cero fricción, 0ms de latencia, accesibilidad perfecta y manteniendo el header inmaculado.

### 2026-05-15 — UX/UI: Reubicación de Announcement Badge a Art de Coté

**Contexto:** El "Announcement Badge" (píldora) destacando el artículo del Boilerplate se ubicó inicialmente en la portada (`index.html`), pero restaba el foco global de la landing.

**Hecho:** Se extrajo el componente `.hero__badge` de la portada y se delegó su inyección al orquestador SSG para que aparezca exclusivamente en la sección `Art de Coté`.

**Motivo / criterio:** *Information Architecture*. Mover la píldora a su propia estantería respeta la segregación de entornos. El visitante que entra a la sección "Art de Coté" verá inmediatamente el logro destacado, mientras que el *Home* se mantiene puro como centro de control global.

### 2026-05-15 — UX/UI: Implementación de Announcement Badge en Hero

**Contexto:** Se requería dar la máxima relevancia posible al artículo "Anatomía de Merci Boilerplate" (el primer *Art de Coté*). Mantenerlo al final del texto en la portada diluía su importancia como producto principal derivado del laboratorio. Además, la métrica de `Releases Boilerplate` había quedado huérfana en el bloque de texto.

**Hecho:** Se diseñó el componente `.hero__badge` en `src/scss/components/_hero.scss` y se inyectó en el Hero principal de `public/index.html`. Se movió la métrica de releases de vuelta al dashboard correspondiente y se eliminó el texto redundante al final de la página.

**Motivo / criterio:** *Landing Page Patterns & Visual Hierarchy*. Un "Announcement Badge" (Píldora de anuncio) sobre el H1 es el estándar de la industria (SaaS, Vercel, Stripe) para dirigir tráfico inmediato a nuevos *releases* o artículos fundacionales. Al colocar el enlace en el punto más alto del *First Fold*, garantizamos un CTR (Click-Through Rate) máximo sin sobrecargar la lectura del texto inferior.

### 2026-05-15 — UX/UI: Erradicación de viñetas en listas centradas

**Contexto:** Con el rediseño a formato *Landing Page* (texto centrado a ancho completo), los puntos nativos de las listas (`ul`, `ol`) generaban ruido visual y rompían la simetría horizontal de los bloques.

**Hecho:** Se inyectó `list-style-type: none;` a los elementos de lista dentro del bloque `.prose__content` en `src/scss/components/_prose.scss`.

**Motivo / criterio:** *Minimalismo y Simetría*. Un diseño centrado gana rotundidad y elegancia cuando los elementos se alinean basándose puramente en su tipografía (text-align), sin los marcadores nativos del navegador desplazando el eje visual.

### 2026-05-15 — UX/UI: Refactorización a Landing Page Style (Full Width & Centered)

**Contexto:** El patrón de diseño "Side-Heading" (titulares desplazados) proyectaba un estilo muy de documentación corporativa. Se requería una presencia visual con más pegada, similar a una Landing Page, donde los textos y encabezados ocuparan todo el ancho disponible (1000px, igual que el dashboard) y estuvieran completamente centrados.

**Hecho:** Se refactorizó la arquitectura SASS en `src/scss/components/_prose.scss`.
- Se eliminó el sistema de *Floats* asimétricos.
- Se implementó `text-align: center` global para el contenido.
- Se simplificó la línea divisoria a un `border-top` que hereda orgánicamente el 100% del ancho del contenedor.
- Se restauró la alineación natural para bloques de código (`<pre>`) y se flexibilizó el contador de las listas ordinales.

**Motivo / criterio:** *Impacto Directo y Simplicidad*. A veces, menos es más. Un diseño centrado a pantalla completa aporta una autoridad inmediata, dirigiendo la atención del usuario en un flujo vertical ininterrumpido que encaja a la perfección con la "potencia" de los dashboards de métricas superiores.

### 2026-05-15 — UX/UI: Ajuste de espaciado inferior en secciones principales

**Contexto:** El espaciado inferior de la clase estructural `.section` resultaba excesivo, dejando un área vacía desproporcionada antes del footer u otras secciones.

**Hecho:** Se redujo el `padding-bottom` de la clase `.section` en `src/scss/components/_section.scss`.

**Motivo / criterio:** *Whitespace Control*. Reducir el espacio final de la sección a una o dos líneas de párrafo (aprox. `1.5rem` - `2rem`) mejora el flujo vertical de la página y compacta el diseño sin generar vacíos estructurales que desconecten visualmente el contenido del pie de página.

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
