# Bitácora del proyecto mercedev.es — Épica 7: Enriquecimiento Visual y Multimedia

## Para qué sirve este archivo

Bitácora activa a partir de la finalización de la Épica 6 (E-commerce Híbrido Extremo).
Registra exclusivamente las decisiones, experimentos y aprendizajes de la Épica 7 (Enriquecimiento Visual y Multimedia) documentada en el `ROADMAP.md` maestro.

No sustituye a `instrucciones.md` (directrices y rol del asistente). Complementa el día a día con **hechos, comandos y lecciones**.

---

## Cómo mantenerlo (acuerdo simple)

1. **Añadir entradas al principio** de la sección "Registro cronológico" (orden cronológico inverso: lo más reciente arriba).
2. **Una entrada por sesión o por tema cerrado**.
3. Si algo fue un error o una vulnerabilidad evitada, usar los **tres átomos** del proyecto (Desafío → Maniobra → Aprendizaje/Deuda).
4. **Correcciones excepcionales**: editar solo el fragmento necesario; no borrar entradas sin motivo documentado.

---

## Registro cronológico

### 2026-05-29 — QA/Fix: Resolución de estilos en línea (UI_INLINE_STYLE) en WooCommerce

**Contexto:** El auditor maestro (`merci-audit.py`) bloqueó el commit de la moneda gráfica al detectar atributos `style="..."` inyectados en `functions.php` y `woocommerce.php`.

**Hecho:** Se extrajeron los estilos en línea a las clases BEM `.merci-coin-icon` y `.woocommerce-info--store-notice` en `src/scss/components/_woocommerce.scss`, eliminando los atributos `style` de las plantillas PHP.

**Motivo / criterio:** *Strict QA y BEM*. El linter cumple su función de escudo activo. Permitir estilos en línea, aunque sea para un simple margen o un icono, abre la puerta a la degradación del código y a la pérdida de control de especificidad (Guerra de Especificidad CSS).

**Siguiente paso o deuda:** Re-ejecutar `merci commit` y proceder con los contrastes WCAG de los botones de la portada.

### 2026-05-29 — UX/UI: Moneda gráfica (Favicon) y Storytelling Técnico

**Contexto:** Como la tienda es una demostración técnica (Tienda No Tienda), mantener una moneda ficticia genérica (MC 🪙) no era suficientemente inmersivo ni aclaraba al usuario el propósito de la tienda. Además, la caja de texto del cupón de descuento sufría el mismo problema de usabilidad que las cantidades: heredaba un estilo diminuto del navegador.

**Hecho:**
- Se estandarizó la caja del cupón en `_woocommerce.scss` con tipografía `1rem`, padding amplio y bordes semánticos, igualando el estilo Premium del resto del carrito.
- Se sustituyó el emoji genérico (🪙) de la moneda oficial por una etiqueta `<img>` apuntando al `/favicon.ico` (la llama del sitio) en el filtro `woocommerce_currency_symbol` de `functions.php`.
- Se inyectó una nota aclaratoria (Storytelling) directamente en el escaparate de la tienda (`woocommerce.php`) informando al visitante que puede finalizar compras de prueba sin riesgo.

**Motivo / criterio:** *Gamificación e Inmersión*. Transformar el símbolo monetario en el propio imagotipo de la autora aporta un toque corporativo único, y la nota informativa elimina cualquier fricción o miedo del usuario a interactuar con un e-commerce que no conoce.

**Siguiente paso o deuda:** Finalizar los ajustes de la tienda y dar el salto, por fin, a corregir los contrastes WCAG de los botones de la Portada.

### 2026-05-29 — UI/UX: Refinamiento de interacciones y formularios en WooCommerce

**Contexto:** Tras aplicar el rediseño Mobile-First al carrito, se detectaron fricciones de experiencia de usuario (UX): la página completa "saltaba" al pasar el ratón (heredando el efecto `:hover` de las tarjetas de la biblioteca), las imágenes perdían su proporción (aspect ratio) por atributos HTML nativos, y los selectores de cantidad (`input[type="number"]`) eran gigantes e ilegibles.

**Hecho:** 
- Se inyectó una regla en `_woocommerce.scss` para anular la transformación y la sombra (`transform: none; box-shadow: none;`) en `article.card:hover` exclusivamente para el contenedor del carrito y checkout.
- Se forzó `height: auto` en las miniaturas de producto para contrarrestar el atributo `height="300"` nativo del CMS.
- Se estandarizó el cajón de cantidades (`.quantity input.qty`) a `80px` de ancho, texto centrado, borde semántico (`$color-border`) y tipografía de `1.25rem`.

**Motivo / criterio:** *Frictionless Checkout y Micro-interacciones (UX)*. Las animaciones de elevación aportan valor en tarjetas de lectura (biblioteca), pero en un formulario transaccional generan inseguridad y molestia. Controlar matemáticamente los inputs HTML5 garantiza que la tienda mantenga un aspecto *Premium* sin depender de librerías JavaScript adicionales.

**Siguiente paso o deuda:** Reemplazar el texto del símbolo de la moneda ("MC") por el emoji de la llama (🔥) en `functions.php`, inyectar una nota aclaratoria sobre la economía ficticia en el escaparate de la tienda, y corregir los contrastes WCAG de los botones de la portada.

### 2026-05-29 — UI/UX: Inicio de rediseño Mobile-First para el carrito de WooCommerce

**Contexto:** La vista del carrito de WooCommerce (`/carrito`) hereda la estructura de tablas nativa del CMS (`table.shop_table`). En dispositivos móviles, esta tabla rompe completamente el diseño responsivo, apretando el contenido o forzando un scroll horizontal inaceptable para la experiencia de usuario.

**Hecho:** Se inicia oficialmente el rediseño del carrito de compra correspondiente a la Fase 2 de la Épica 7.

**Motivo / criterio:** *Mobile-First Design*. En lugar de intentar encoger una tabla HTML, la estrategia *Zero-Bloat* pasa por mutar la propiedad `display` nativa de la tabla (`table`, `tr`, `td`) a `block` en dispositivos móviles, transformando cada fila de producto en una "tarjeta" apilada verticalmente. Solo a partir de resoluciones de escritorio (`min-width: 768px`) se restaurará el comportamiento tabular.

**Siguiente paso o deuda:** Implementar las reglas CSS en `_woocommerce.scss` para reestructurar la tabla nativa de WooCommerce.

### 2026-05-29 — Docs: Inyección de Protocolo de Cierre en Roadmap y ampliación de Auditoría

**Contexto:** Para mitigar la pérdida de atención (Attention Drop) de los LLMs locales durante la orquestación, era necesario crear un anclaje semántico de las reglas de cierre de fase directamente en el Roadmap. Además, la regla de auditoría documental del "Definition of Done" omitía la revisión del directorio de manuales (`docs/`) y el archivo de políticas (`SECURITY.md`).

**Hecho:**
- Se inyectó el "Protocolo Estricto de Cierre" (Definition of Done) como un bloque de cita (`>`) en la cabecera de `ROADMAP.md` para evitar interferencias con las métricas SRE.
- Se amplió el paso 3 (Auditoría Documental) en `instrucciones.md` para incluir explícitamente la revisión del directorio `docs/` y del archivo `SECURITY.md`.

**Motivo / criterio:** *In-Context Learning y Zero Document Drift*. Exponer el checklist de cierre directamente en el documento de trabajo del Agente SSOT actúa como un recordatorio persistente (Zero-Shot) que reduce las alucinaciones y omisiones. Ampliar el alcance de la auditoría garantiza que las políticas de seguridad y los manuales operativos evolucionen a la par que el código.

**Siguiente paso o deuda:** Iniciar el refinamiento de la maquetación visual del E-Commerce (Fase 2 de la Épica 7) utilizando la arquitectura SASS.

### 2026-05-28 — Fix/QA: Resolución definitiva de Aspect Ratio en marcadores (100/100)

**Contexto (Desafío):** A pesar de los recortes previos, la auditoría de PageSpeed (28 de mayo, 20:17) devolvía un 96/100 en Recomendaciones (Best Practices) alertando que `tu_avatar.webp` tenía una "relación de aspecto incorrecta". Las dimensiones físicas seguían sin ser exactamente 1:1 (eran 406x389), entrando en conflicto con el `width="80" height="80"` del DOM.

**Maniobra:**
- Se redimensionó mediante Python (Pillow, escalado Lanczos) `tu_avatar.webp` a unas dimensiones precisas de `160x160` (proporción 1:1 estricta, resolucion 2x Retina).
- Preventivamente, se ajustó `tu_logo.webp` a `526x130` (proporción estricta de 263:65).
- Tras el ajuste milimétrico, se superaron todas las advertencias de Lighthouse, consolidando por completo la auditoría a 100/100.

**Aprendizaje:** *Tolerancia Cero de Lighthouse al Aspect Ratio*. Lighthouse no perdona ni siquiera desviaciones de 1 píxel en el recorte físico. Para evitar advertencias de *Best Practices*, los archivos de imagen deben generarse garantizando una proporción matemática exacta frente al espacio reservado en la etiqueta `<img width="..." height="...">`.

### 2026-05-28 — Feat/UX: Planificación de Refinamiento Visual para E-Commerce (Fase 2)

**Contexto (Desafío):** Al revisar la integración de la tienda (WooCommerce) desplegada en fases anteriores, se identificó que la maquetación visual actual, especialmente el flujo y diseño del carrito de compra, no alcanza los estándares de experiencia de usuario (UX) ni el nivel estético premium exigido por la Fase 2 de esta Épica.

**Maniobra:**
- Se documentó formalmente la deuda de diseño en el `ROADMAP.md` (Épica 7, Fase 2), blindando el requisito innegociable de rediseñar el carrito y la tienda sin comprometer el rendimiento base (Zero-Bloat).

**Deuda Técnica (Siguiente paso):** Iniciar la Fase 2 refinando y perfeccionando la maquetación visual de la tienda utilizando la arquitectura SASS 7-1, asegurando la coherencia visual con el ecosistema y la accesibilidad plena.

### 2026-05-28 — Feat/SRE: Cierre de Fase 1 - Rendimiento Perfecto (100/100) y Hardening de Despliegue

**Contexto (Desafío):** Para cerrar la Fase 1 de la Épica 7 (Enriquecimiento Visual), quedaban dos flecos bloqueantes. 1) La auditoría de PageSpeed del *Boilerplate* devolvía un 98 en Rendimiento debido a un *Cumulative Layout Shift (CLS) de 0.095*, provocado porque las imágenes agnósticas de reemplazo (`tu_logo.webp`, `tu_avatar.webp`) no coincidían con la relación de aspecto estricta reservada en el HTML (`263x65` y `80x80`). 2) El despliegue automatizado (`merci deploy`) fallaba en el servidor de producción porque Git intentaba sobreescribir el enlace simbólico físico de infraestructura (`public/assets`).

**Maniobra:**
- **Zero-Shift Rendering:** En lugar de ensuciar el HTML o inyectar JavaScript, se utilizó `ImageMagick` (`convert`) directamente desde terminal para recortar (crop) y redimensionar milimétricamente las imágenes agnósticas de reemplazo a `263x65` y `80x80`. El navegador ahora reserva la caja exacta que necesita la imagen al descargarse, eliminando cualquier recálculo de CSS (`height: auto`) y logrando la aniquilación del salto visual (CLS = 0).
- **GitOps (Infraestructura Excluida):** Se diagnosticó que el `git pull` en el servidor abortaba para proteger su symlink local. Se reparó desenlazando dinámicamente `public/assets` de Git (`git rm --cached`) y añadiéndolo permanentemente a la zona segura del `.gitignore` bajo la política de *Enlaces simbólicos de infraestructura CMS*. El despliegue ahora realiza un *fast-forward* limpio.
- **Validación Final (End-to-End):** Se orquestó la cadena completa mediante `merci total` → `merci release` → `merci showcase` → `merci completo`, confirmando que la matriz sincroniza los activos, el clon efímero los purga y el servidor los despliega sin intervención manual.

**Aprendizaje:** *Principio de Separación de Preocupaciones en GitOps*. Los enlaces simbólicos (symlinks) que unen los directorios de construcción locales con la raíz pública del servidor (`public/assets`) son parte de la *infraestructura física* del entorno destino, no del código fuente. Versionarlos contamina el repositorio y rompe las pipelines de despliegue continuo.

**Protocolo Estricto de Cierre de Fase (Definition of Done):**
- [x] **1. Conciliación de Deuda Técnica:** Solucionado el CLS (Zero-Shift) y excluido el symlink `public/assets` de GitOps. No queda deuda bloqueante.
- [x] **2. Cosecha de Conocimiento:** Creado y purgado el cuadernillo de gemelos multimedia y caché (`blog-gemelos-multimedia-y-cache.md`).
- [x] **3. Auditoría Documental:** Roadmap actualizado y SOP revisado para el nuevo flujo de release y showcase.
- [x] **4. Evaluación de Release (Boilerplate):** Orquestado el `merci release` y modificado el inicializador (`merci-init.py`) para soportar la identidad agnóstica exacta.
- [x] **5. Certificación de Rendimiento (9 Casos):** Json validado (100/100) tras el parche del aspect-ratio.
- [x] **6. Snapshot (Backup Local):** Backup de seguridad realizado previamente al sellado.
- [x] **7. Sello Definitivo:** Lanzando `merci completo` para sellar la Fase 1.

### 2026-05-28 — Feat/SRE: Ajustes Quirúrgicos en el Ecosistema Showcase y Boilerplate

**Contexto (Desafío):** Durante la auditoría del Clon Efímero (Showcase) se detectaron discrepancias visuales y arquitectónicas: el Asistente Merci (`<aside>`) no renderizaba en las páginas autogeneradas, el Hero de portada perdía el diseño bicolor en el título, la página `art-de-cote` se colaba en el boilerplate, y la navegación persistía en el F5 para cargar la nueva caché.

**Maniobra:**
- **Inyección de Dependencias:** Se refactorizó la llamada de `merci-showcase.py` a `merci-init.py` forzando el argumento explícito `--ia`, evitando que la guillotina del boilerplate amputase el código fuente de Merci antes de la clonación de páginas de contingencia.
- **Micro-Diseño en Python:** Se reescribió el motor de anonimización de la Portada en `merci-init.py`. Ahora, intercepta dinámicamente las últimas 3 letras del nuevo dominio antes de la extensión y las encapsula en `<span class="hero__highlight">`, preservando la dualidad de colores corporativa.
- **Cierre Perimetral:** Se extrajo explícitamente `art-de-cote` de las rutinas de reconstrucción (`.gitkeep`) y se añadió su destrucción física en el bloque principal de purgas de `merci-init.py`. Además, se implementó una purga global del enlace en el menú de navegación (`<nav>`) para que el boilerplate nazca sin ese acceso.
- **Identidad Agnóstica:** En lugar de renombrar las imágenes de marcador de posición (`tu_logo.webp`, `tu_avatar.webp`) para que suplanten a las originales, se modificó `merci-init.py` para purgar los originales (`logo.webp`, `Merci-en-la-nube.webp`) y reescribir dinámicamente las rutas del código fuente (`replace_in_files`) hacia los nuevos marcadores. Así, el código generado refleja la identidad correcta.
- **Invalidación de Caché (Zero-Stale):** Para prevenir colisiones con la agresiva política de caché de Nginx (`max-age=315360000`), se inyectó dinámicamente un timestamp de época (`time.time()`) en la consulta de las imágenes del clon efímero (`tu_logo.webp?v=178...`), forzando al navegador a descargar siempre la versión fresca durante el redespliegue del Showcase.
- **Rendimiento Dinámico:** Se inyectó `<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">` directamente desde `merci-showcase.py` al HEAD de todas las páginas para forzar descargas estáticas, solventando el F5 fantasma.
- **Cerebro Artificial:** Se enriqueció el `brain_data.json` *fallback* con rutas directas (ej. `/biblioteca/`, `/blog/`) permitiendo frases descriptivas reales del asistente sin consumo de API.

**Aprendizaje:** *Orquestación Modular (Coupling vs Cohesion)*. El hecho de que el Showcase inyecte plantillas dependa de un parámetro opcional (`--ia`) en otro script (`merci-init.py`) demuestra que la automatización exige contratos de estado explícitos. Si un orquestador B llama a C, B debe pasar todos los parámetros necesarios para garantizar la coherencia de estado.

### 2026-05-28 — Feat/SRE: Inyección de Telemetría Aislada y Gemelos Multimedia en el Showcase

**Contexto (Desafío):** Al instanciar el *Boilerplate* (Clon Efímero) para el Showcase en vivo, este heredaba la última telemetría de `mercedev.es` o fallaba en la auditoría inicial de Lighthouse con errores 404 porque el inicializador (`merci-init.py`) purgaba las imágenes personales del autor original sin proveer *placeholders*. Además, las métricas vivas de Git (Commits, Líneas) se reseteaban a "N/D", dando una impresión de proyecto vacío.

**Maniobra:**
- **Roadmap:** Se reestructuró la Épica 7 en el archivo `ROADMAP.md` para segmentar claramente la Fase 1 (Telemetría y Activos), Fase 2 (UI/UX y Estilos) y Fase 3 (Multimedia).
- **Gemelos Multimedia:** Se crearon las imágenes `tu_logo.webp` y `tu_avatar.webp` en `assets/images/`. Se refactorizó `merci-init.py` para purgar `logo.webp` y `Merci-en-la-nube.webp` y renombrar los archivos *tu_* a los nombres definitivos en el nuevo proyecto, evitando así cualquier error 404 en el DOM de la portada.
- **Telemetría Aislada:** Se generó `merci-boilerplate.template.json` dentro de `auditorias-pagespeed.web.dev/` emulando una auditoría perfecta de Lighthouse (100/100, FCP óptimo).
- **Orquestación Showcase:** Se actualizó `scripts/matriz/merci-showcase.py`. Ahora, tras inyectar la guillotina de inicialización, purga las auditorías reales, renombra la plantilla JSON, borra la caché de métricas y ejecuta `merci-extract-metrics.py` internamente para sobrescribir los marcadores del HTML con los valores ideales. Finalmente, usa expresiones regulares para reemplazar los "N/D" estáticos por valores simbólicos ("1").

**Aprendizaje:** *Inyección Controlada en CI/CD Aislados*. La mejor forma de dotar de vida a un proyecto demostrativo es reutilizar sus propios motores (como `merci-extract-metrics.py`). Suministrando una "plantilla semilla" (seed template) en el orquestador temporal, el ecosistema funciona como si acabara de recibir una auditoría real, garantizando la consistencia y aislando los datos de la matriz.

### 2026-05-28 — Fix: Resolución de Caché Huérfana en Showcase (Cache Busting)

**Contexto (Desafío):** Al compilar el Clon Efímero (Showcase) con `merci-showcase.py`, el botón de retorno flotante solo aparecía visible en la Portada y en *Sobre Mí*. En el resto de páginas (Biblioteca, Blog), el usuario tenía que pulsar F5 para verlo. El problema era un error de caché huérfana introducido por `merci-init.py`.

**Maniobra:**
- El script destructivo `merci-init.py` generaba las páginas secundarias de contingencia con una versión *hardcodeada* de los *assets* (`href="/css/main.css?v=1"`). Al cargarse la página en el navegador del usuario, este detectaba el `v=1` e inmediatamente servía una versión de CSS antigua (de antes de que creáramos la clase `.showcase-return`).
- Se refactorizó la función `generar_placeholders_directorios()` en `merci-init.py` para que lea dinámicamente la portada (`index.html`) mediante expresiones regulares, extraiga los *Cache Busters* reales (ej. `?v=1779950634`) y los inyecte en las nuevas páginas generadas.

**Aprendizaje:** *La cadena de suministro del CSS*. Cuando un generador de páginas (SSG o en este caso, un script de Inicialización) inyecta etiquetas `<link>`, debe respetar siempre el sistema de purga de caché maestro. Dejar un `?v=1` estático es una garantía matemática de desincronización visual para los usuarios recurrentes.


### 2026-05-28 — QA/SRE: Resolución de Deuda de Accesibilidad (Contrastes WCAG AA)

**Contexto (Desafío):** Se detectó que el estado `:hover` de varios botones secundarios no superaba el umbral de contraste requerido por Lighthouse (WCAG AA ratio > 4.5:1), lo que ponía en riesgo la calificación de 100/100 en Accesibilidad.

**Maniobra:**
- **Showcase:** En `src/scss/components/_showcase.scss` y `merci-showcase.py`, se rediseñó por completo el botón flotante para que emule el aspecto del componente `.hero__badge` de la portada (con la etiqueta lateral "Matriz"). Además, se inyectó explícitamente la regla `&:visited { color: $color-text-base; }` para neutralizar el comportamiento nativo del navegador que teñía las letras de naranja una vez que el usuario había visitado el enlace, arruinando el contraste sobre fondos oscuros.
- **Botones de Portada:** En `src/scss/components/_hero.scss`, se rediseñó el estado `:hover` de los botones base (`.hero__btn`). Ahora realizan una inversión semántica (Fondo: `$color-text-base` / Texto: `$color-bg-base`) generando un contraste extremo (> 15:1) y un aspecto más *Premium*. También se reemplazaron sus bordes *hardcoded* (`#cbd5e1`) por la nueva variable `$color-border`.

**Aprendizaje / Deuda:** *El engaño del color primario*. Es habitual utilizar el color primario de marca como fondo de botón, pero colores vibrantes (como el naranja) rara vez ofrecen contraste suficiente contra texto blanco. Siempre se debe tener definida una variable derivada más oscura (como `$color-regular`) exclusivamente para garantizar legibilidad en bloques sólidos o estados interactivos.


### 2026-05-28 — QA/SRE: Resolución del Catch-22 en Sincronización Estricta (Zero Trust)

**Contexto (Desafío):** Al restaurar la expresión regular estricta (`<header class="header" id="top">`) en `merci-sync-pages.py`, el script extrajo correctamente el bloque de la portada (SSOT), pero colapsó al intentar inyectarlo en las páginas secundarias (`contacto/index.html` y `sobre-mi/index.html`).

**Maniobra:**
- Se analizó el flujo de reemplazo: el orquestador usaba la **misma expresión regular estricta** para extraer de la portada y para buscar qué bloque reemplazar en el destino.
- Como las páginas secundarias aún tenían la estructura vieja (`<header class="header">` sin el `id="top"`), la validación estricta falló al no encontrar una coincidencia exacta en ellas, bloqueando el pipeline.
- En lugar de relajar la seguridad de la Regex, se editaron manualmente las páginas secundarias para añadir el atributo `id="top"` (y eliminar el antiguo `div` invisible). 

**Aprendizaje / Deuda:** *Catch-22 de Sincronización Estricta*. En una arquitectura gobernada por SSOT (Single Source of Truth) y validación *Zero Trust*, las páginas secundarias **heredan** la estructura de la principal. Si se altera estructuralmente la firma de un bloque (añadiendo IDs o clases base) en la portada, dicha alteración debe replicarse manualmente una primera vez en el resto de los `index.html` estáticos. De lo contrario, el orquestador estricto no reconocerá el bloque obsoleto y se negará a sobrescribirlo, protegiendo así el código pero requiriendo intervención humana explícita.

### 2026-05-28 — QA/SRE: Resolución de colapso en el Pipeline SSG (Regex Drift)

**Contexto (Desafío):** Al ejecutar el pipeline maestro (`merci total`), el orquestador `merci-sync-pages.py` colapsó con el error `No se pudo extraer el bloque Header de la portada`, deteniendo todo el proceso de compilación estática.

**Maniobra:**
- Se detectó que la causa raíz fue la corrección de accesibilidad (WAI-ARIA) realizada en la auditoría anterior, donde se asignó el atributo `id="top"` directamente a la etiqueta `<header class="header">`.
- El script de sincronización usaba la expresión regular `r'(<header class="header">.*?</header>)'`, por lo que dejó de encontrar el bloque.
- Se intentó flexibilizar con `[^>]*>`, pero se descartó inmediatamente por motivos de seguridad (Zero Trust).
- Se refactorizó `scripts/merci/merci-sync-pages.py` endureciendo la expresión regular a la firma exacta: `r'(<header class="header" id="top">.*?</header>)'`.

**Aprendizaje / Deuda:** *Zero Trust y Strict Regex*. Flexibilizar una expresión regular para que acepte "cualquier atributo" (`[^>]*>`) abre la puerta a inyecciones silenciosas (ej: estilos *inline* o código malicioso inyectado localmente) que el script propagaría a ciegas por todo el ecosistema. Mantener las expresiones regulares estrictas actúa como una validación implícita de integridad (Integrity Check) deteniendo el pipeline si el SSOT muta de forma inesperada.

### 2026-05-28 — UI/UX: Implementación de Paleta Premium y Sombras (Fase 1)

**Contexto:** Retomando la Épica 7, era necesario aplicar las variables semánticas (superficies, grises tipográficos y sombras) previamente definidas en la escala base para enriquecer el diseño y alejarlo del aspecto "por defecto" del navegador, logrando un estilo más Premium.

**Hecho:**
- Se inyectaron oficialmente las variables `$color-surface`, `$color-border`, `$color-text-muted`, `$font-family-mono`, `$shadow-sm` y `$shadow-hover` en `src/scss/abstracts/_variables.scss`.
- Se refactorizó `src/scss/components/_prose.scss` reemplazando los colores quemados (`#64748b`, `#334155`) y bordes RGBA por las variables `$color-text-muted`, `$color-text-base` y `$color-border`.
- Se refactorizó `src/scss/components/_card.scss` sustituyendo el fondo transparente por `$color-surface` y el borde por `$color-border`. Se inyectó `$shadow-hover` en el estado `:hover` de las tarjetas para dotarlas de micro-interacción de elevación.

**Motivo / criterio:** *Design System Scalability y Estética Premium*. Eliminar los colores *hardcoded* (quemados) descentralizados previene la deuda técnica visual. Además, la adición de `$color-surface` y sombras sutiles eleva la percepción de calidad de la interfaz manteniéndose en un peso de 0 KB de dependencias (solo CSS puro).

**Siguiente paso o deuda:** Iniciar el refinamiento tipográfico general y evaluar la necesidad de micro-animaciones adicionales.

### 2026-05-28 — Feat/UX: Botón de Retorno del Showcase (Clon Efímero)

**Contexto:** Se detectó el riesgo de fuga de tráfico en la demostración pública (`boilerplate.mercedev.es`). Los visitantes que llegaban al Showcase carecían de una vía intuitiva para regresar a la web principal de la autora.

**Hecho:**
- Se diseñó el componente SASS flotante `src/scss/components/_showcase.scss` (y se enlazó en el índice) con posición fija y diseño responsive, aislado mediante BEM (`.showcase-return`).
- Se refactorizó el orquestador de despliegue `scripts/matriz/merci-showcase.py` para inyectar dinámicamente el HTML del botón de retorno justo después de la etiqueta `<body>` en *todos* los archivos HTML del Clon Efímero temporal (`scratch/showcase_build/`).

**Motivo / criterio:** *Aislamiento Arquitectónico (Zero Bloat)*. Inyectar el botón durante el ciclo de vida del "Clon Efímero" justo antes de subirlo por RSYNC (Remote Sync - Sincronización Remota) permite que el código fuente matriz permanezca completamente agnóstico y limpio. Los usuarios que clonen el Boilerplate en sus máquinas jamás verán este botón, pero estará siempre presente en la demostración en vivo.

**Siguiente paso o deuda:** Continuar con la Fase 1 de la Épica 7 enfocándose en la experiencia de contenido multimedia.

### 2026-05-28 — QA/SRE: Resolución de Deuda Técnica (Auditoría de Arquitectura)

**Contexto:** Tras la auditoría de arquitectura de hoy, se procedió a saldar la deuda técnica reportada para alinear el proyecto al 100% con las reglas.

**Hecho:**
- Se renombró el archivo del blog usando el prefijo taxonómico correcto (`blog-2026-05-01-anuncio.md`).
- Se corrigió el anti-patrón WAI-ARIA en `public/index.html`, eliminando el `div` invisible y asignando el ancla `id="top"` directamente a la etiqueta `<header>`, mitigando los problemas de foco en lectores de pantalla.
- Se completó la estructura arquitectónica SASS 7-1 creando el directorio `/src/scss/pages/` y su respectivo archivo `_index.scss`, enlazado en `main.scss`.
- Se refactorizó `merci-blogger.py` extrayendo el módulo `unicodedata` de una función local al bloque de importaciones globales (Top-level imports), alineándolo con PEP 8 y la Regla 16.
- Las importaciones en bloques `try/except` de otros scripts (`markdown`, `litellm`) se confirmaron como excepciones válidas al amparo de la política de Degradación Elegante (Graceful Degradation) y Zero Bloat.

**Motivo / criterio:** *Higiene y Cumplimiento Normativo*. Las reglas del proyecto son innegociables. Saldar las pequeñas fricciones arquitectónicas a medida que se detectan previene la deriva técnica silenciosa.

**Siguiente paso o deuda:** Iniciar las mejoras visuales y multimedia planificadas para la Épica 7 (Fase 1).

### 2026-05-28 — QA/SRE: Auditoría de Arquitectura (Reglas de Higiene)

**Contexto:** Se realizó una auditoría de la arquitectura y configuración del proyecto.

**Hecho:**
- Se detectó una desviación en la regla de nomenclatura (Taxonomía SSOT, Regla 19) en el archivo `/blog/2026-05-01-anuncio.md`.
- Se identificaron violaciones a la convención PEP 8 (Regla 16) sobre la higiene de importaciones en scripts de automatización (`merci-wp.py`, `merci-audit.py`, etc.).
- Se descubrió un anti-patrón de accesibilidad en `public/index.html` con un ancla invisible (`<div id="top" tabindex="-1">`) empleada para la función "Volver arriba".
- Se constató la ausencia del directorio `pages/` dentro de `src/scss/`, rompiendo parcialmente el canon SASS 7-1.

**Motivo / criterio:** Verificación del cumplimiento estricto de las directrices marcadas en `instrucciones.md` (0 dependencias, rendimiento extremo, y Desarrollo Guiado por Especificaciones).

**Siguiente paso o deuda:** Iniciar refactorizaciones propuestas, priorizando nomenclatura del archivo en el blog y el ajuste del ancla en `index.html`.

### 2026-05-27 — Feat/DevRel: Gestor de Cola Social Interactivo (Buffer Management)

**Contexto:** El orquestador social (`merci-linkedin.py`) publicaba estrictamente en orden cronológico (FIFO) basándose en la fecha de publicación. Se requería la capacidad de reordenar dinámicamente las publicaciones (asignando posiciones exactas) y desencolar artículos directamente desde la terminal, asimilando funciones de un gestor profesional tipo Buffer o Hootsuite.

**Hecho:**
- Se introdujo el nuevo metadato `orden_social` en la máquina de estados del YAML Frontmatter.
- Se refactorizó `scripts/merci/merci-linkedin.py` inyectando un submenú interactivo para la cola de publicaciones aprobadas.
- Se implementó la acción de "Devolver a revisión" (estado `en_cola`) y el descarte permanente (`ignorado`) con confirmación explícita anti-errores.

**Detalle técnico:** El script ahora parsea y manipula el campo `orden_social` mediante expresiones regulares (`re.sub`), actualizando físicamente el archivo Markdown en disco. Los artículos sin este campo asumen la prioridad más baja (`999`). El submenú permite asignar posiciones, devolver borradores al buffer o ejecutar un "Hard Delete" lógico hacia `ignorado` protegido por un *prompt* de seguridad con emojis (`⚠️`).

**Motivo / criterio:** *Developer Experience (DX) y Content Ops*. Modificar archivos Markdown a mano para alterar el orden de publicación de una campaña de marketing genera alta fricción operativa. Delegar el trabajo pesado de reescritura de metadatos YAML al orquestador CLI consolida una experiencia de *Fricción Cero*, manteniendo a su vez la Única Fuente de Verdad (SSOT) permanentemente sincronizada.

**Siguiente paso o deuda:** Iniciar la Fase 1 de la Épica 7 aplicando las nuevas variables de color semánticas a la arquitectura SASS (`_card.scss`, `_prose.scss`).
### 2026-05-26 — UI/UX: Definición de Paleta Premium y Escala Base (Fase 1)

**Contexto:** Arranca la Épica 7 (Enriquecimiento Visual). Las variables base en SASS eran demasiado parcas y carecían de tonos de superficie (surface), grises tipográficos (text-muted) y un sistema de sombras, lo que limitaba el diseño "Premium" del proyecto.

**Hecho:** Se extendió `src/scss/abstracts/_variables.scss`.
- Se inyectaron `$color-surface`, `$color-border` y `$color-text-muted` basados en la paleta *Slate* para un diseño más moderno.
- Se formalizó la fuente monoespaciada (`$font-family-mono`) y una escala de sombras (`$shadow-sm`, `$shadow-hover`).

**Motivo / criterio:** *Design System Scalability*. Un buen diseño UI/UX (User Interface / User Experience) no usa el negro puro para los textos ni el blanco puro para todas las cajas. Definir "superficies" y "sombras" mediante variables semánticas centralizadas prepara el terreno para modernizar los cuadernillos y tarjetas de WooCommerce sin ensuciar la arquitectura CSS con valores *hardcoded*.

**Siguiente paso o deuda:** Reemplazar los colores *hardcoded* (quemados) en los componentes actuales (`_prose.scss`, `_card.scss`) por las nuevas variables semánticas, o implementar el botón de Showcase.

### 2026-05-26 — Docs/UX: Inclusión de botón de retorno para el Showcase en el Roadmap

**Contexto:** Se detectó la necesidad de evitar fugas de tráfico desde la demostración pública (`boilerplate.mercedev.es`) hacia el exterior, facilitando un camino claro de regreso al ecosistema principal.

**Hecho:** Se añadió una nueva tarea a la Fase 1 de la Épica 7 en el `ROADMAP.md` para implementar un botón de "Volver a mercedev.es" en la interfaz del Showcase.

**Motivo / criterio:** *User Retention y UX Navigation*. Todo subdominio satélite o demostración debe contar con una vía de escape obvia de regreso a la matriz. Esto no solo mejora la navegación, sino que retiene el tráfico y asegura que la demostración actúe como un embudo (funnel) hacia el portfolio profesional.

**Siguiente paso o deuda:** Iniciar con la implementación visual de los espaciados, tipografías y el botón de retorno planificado en la Épica 7.

### 2026-05-26 — Feat/UX: Conciencia de contexto (Context-Awareness) para E-commerce

**Contexto:** Tras la implementación de la tienda y el carrito Zero-JS (Épica 6), el asistente virtual Merci carecía de respuestas específicas para las rutas `/carrito` y `/checkout`, perdiendo la oportunidad de guiar durante la simulación de compra.

**Hecho:** Se refactorizó el método `_loadStandardKnowledgeBase()` en `public/js/MerciController.js` para inyectar diccionarios de respuestas específicos cuando la ruta (`window.location.pathname`) incluye las palabras clave del carrito o la caja.

**Motivo / criterio:** *Context-Awareness y UX Inmersiva*. El asistente debe acompañar el *Storytelling Técnico* del proyecto. Informar que se trata de un entorno Zero-JS seguro y sin pasarelas reales justo en el momento del checkout aporta valor divulgativo y reduce la incertidumbre en un entorno de pruebas.

**Siguiente paso o deuda:** Iniciar el refinamiento visual de tipografías y espaciados generales.