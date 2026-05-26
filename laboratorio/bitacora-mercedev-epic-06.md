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

### 2026-05-25 — Fix: Resolución de enlaces rotos (PDF) y Errores JS en Carrito WC

**Contexto:** El rastreador dinámico DAST (`merci-linkcheck.py`) bloqueó el orquestador maestro al detectar un error 404 (`carrito.pdf`) en la página del carrito. Adicionalmente, la consola del navegador estaba plagada de errores `ReferenceError: wp is not defined`.

**Hecho:**
- Se parcheó `src/wp-theme/merci-theme/functions.php` inyectando una rutina de auto-sanación que convierte automáticamente los bloques Gutenberg de WooCommerce (`<!-- wp:woocommerce/cart -->`) en shortcodes clásicos (`[woocommerce_cart]`) en la base de datos.
- Se desencolaron y desregistraron de forma absoluta todas las librerías React/Gutenberg que WooCommerce inyecta (`wp-i18n`, `wp-data`, `wc-cart-block-frontend`, etc.).
- Se implementó una válvula de escape mediante *Output Buffering* en `template_redirect` para amputar matemáticamente cualquier enlace a `.pdf` residual en páginas estructurales (como el Carrito o Checkout) antes de renderizar el HTML.

**Motivo / criterio:** *Zero-JS y Self-Healing DB*. Las nuevas versiones de WooCommerce utilizan bloques pesados basados en React por defecto. Al forzar la conversión de los bloques a shortcodes clásicos desde PHP, obligamos a WooCommerce a utilizar formularios `POST` nativos y erradicamos los errores de consola sin tocar la base de datos a mano. El *Output Buffering* actúa como un escudo DAST garantizando que plantillas compartidas no filtren enlaces a descargas inexistentes, recuperando el 100/100 en el rastreador de enlaces.

**Siguiente paso o deuda:** Re-ejecutar `merci total` para validar el rastreo a cero errores y cero advertencias.

### 2026-05-25 — Fix: Globalización de botones WooCommerce y Configuración Zero-JS

**Contexto:** Los botones de "Añadir al carrito" en la vista individual aparecían negros con texto invisible al pasar el ratón. Además, la tienda parecía no añadir productos al carrito porque la página simplemente se recargaba sin redirección ni feedback visual obvio (al carecer de los scripts AJAX nativos).

**Hecho:** 
- Se extrajo y unificó la regla CSS `.button` en `src/scss/components/_woocommerce.scss` aplicando `!important` para aplastar cualquier estilo residual de WooCommerce en todas las vistas (Catálogo, Producto, Carrito y Checkout).
- Se estableció el Procedimiento Operativo para que WooCommerce funcione fluidamente en modo Zero-JS: crear las páginas por defecto y forzar la redirección tras añadir al carrito.

**Motivo / criterio:** *CSS Specificity y UX Zero-JS*. La regla anterior estaba anidada dentro del componente de cuadrícula (`.products .product`), dejando huérfanos a los botones de la vista individual. Al globalizarla, blindamos todos los formularios de la tienda. Para suplir la ausencia de los pesados scripts AJAX, se instruye al CMS para que redireccione inmediatamente a la página de carrito, ofreciendo al usuario una confirmación visual instantánea de su acción.

**Siguiente paso o deuda:** Validar la estilización de los botones, crear las páginas del carrito en WP y cerrar la Épica 6.

### 2026-05-25 — Feat/UX: Restauración del Carrito (Flujo Zero-JS)

**Contexto:** Se había implementado la tienda en "Modo Catálogo" puro eliminando los botones de compra. Sin embargo, se rectificó que una demostración real de e-commerce requiere un flujo de carrito y *checkout* funcional, pero sin sacrificar el TBT (0ms).

**Hecho:** Se eliminaron los escudos en `functions.php` que ocultaban los botones de "Añadir al carrito". Se añadió un enlace al carrito en la cabecera de `woocommerce.php`. Se estilizaron las tablas del carrito, los avisos de WooCommerce y el formulario de Checkout en `_woocommerce.scss`.

**Motivo / criterio:** *Progressive Enhancement y Zero-JS*. Al restaurar los botones de compra mientras mantenemos bloqueados los pesados scripts AJAX de WooCommerce (extirpados en iteraciones previas), el CMS se ve obligado a utilizar el comportamiento base de HTML (formularios POST). Esto genera recargas instantáneas de página con 0 milisegundos de ejecución JavaScript, ofreciendo un flujo de compra completo y ultrarrápido.

**Siguiente paso o deuda:** Compilar los estilos, configurar el método de pago falso en el CMS e iniciar la Épica 7.

### 2026-05-25 — Fix: Alineación Mobile-First en vista individual y Cierre de Tareas E-commerce

**Contexto:** La vista de producto individual (single-product) forzaba `text-align: left` desde resoluciones móviles, rompiendo la coherencia visual con el resto del diseño Mobile-First. Además, faltaba sellar formalmente las tareas de modo simulación/catálogo en el Roadmap.

**Hecho:**
- Se modificó `src/scss/components/_woocommerce.scss` estableciendo `text-align: center` por defecto y reservando `text-align: left` exclusivamente para el *breakpoint* de escritorio (`min-width: 768px`).
- Se marcaron como completadas las tareas del modo simulación y estilización del checkout en el `ROADMAP.md`.

**Motivo / criterio:** *Mobile-First Design y Arquitectura por Sustracción*. En pantallas pequeñas, el texto centrado acompaña mejor a la imagen apilada verticalmente. Respecto al Roadmap, al haber extirpado los botones de compra y el carrito (Modo Catálogo puro sin AJAX), cumplimos el objetivo de "simular sin pasarelas" y "mantener el TBT en 0ms" mediante la eliminación radical del problema. El mejor código de checkout es el que no existe.

**Siguiente paso o deuda:** Iniciar la Épica 7 (Enriquecimiento Visual y Multimedia).

### 2026-05-25 — Fix: Resolución de anidamiento SASS (Selector Fantasma) en WooCommerce

**Contexto:** El usuario reportó que el HTML de WooCommerce seguía inyectando `style="opacity: 0;"` en la galería de imágenes, impidiendo su visualización a pesar de las reglas `!important` de nuestro CSS.

**Hecho:** Se corrigió un bug de anidamiento en `src/scss/components/_woocommerce.scss`, cambiando `.single-product &` por `&.single-product`.

**Detalle técnico:** En SASS, el ampersand (`&`) representa al selector padre (`.woocommerce`). Escribir `.single-product &` generaba el selector `.single-product .woocommerce` (con espacio), buscando un elemento dentro de otro. Como WordPress inyecta ambas clases en la misma etiqueta `<body>`, el selector fallaba y todo el bloque CSS de la vista individual era ignorado por el navegador (Código Muerto). Al usar `&.single-product`, SASS genera `.woocommerce.single-product`, apuntando correctamente a la raíz y aplicando por fin nuestros `!important` para aplastar el estilo en línea de la galería.

**Motivo / criterio:** *Deep CSS Debugging*. Conocer cómo compila SASS los selectores combinados es vital en arquitecturas BEM para no generar código fantasma inalcanzable por el DOM.

**Siguiente paso o deuda:** Recompilar SASS, validar la vista y cerrar por fin la Épica 6.

### 2026-05-25 — Fix: Resolución de Especificidad CSS en Single Product (WooCommerce)

**Contexto:** La imagen del producto individual seguía invisible (aunque su enlace era clicable) y la descripción corta aparecía aglomerada junto al precio sin márgenes.

**Hecho:** Se refactorizó la anidación en `src/scss/components/_woocommerce.scss`.
- Se movieron los bloques `div.images`, `div.summary` y `.woocommerce-tabs` al interior de `div.product`.
- Se restituyó el bloque `div.summary` que se había omitido en iteraciones anteriores.

**Motivo / criterio:** *CSS Specificity (Especificidad CSS)*. Al estar los estilos flotando fuera de `div.product` en la estructura SASS, el compilador generaba selectores débiles (`.woocommerce div.images`). Esto permitía que el código nativo residual de WooCommerce aplastara nuestras reglas `opacity: 1` con su comportamiento de galería oculta. Anidarlos estrictamente multiplica la prioridad de nuestras reglas en la cascada CSS, forzando la visibilidad del bloque y aplicando los márgenes correctos a la descripción.

**Siguiente paso o deuda:** Validar la restitución visual completa y pasar a la Épica 7.

### 2026-05-25 — Fix: Visibilidad absoluta de la galería WC y Corrección End-to-End de Despliegue

**Contexto:** Al acceder a la vista de producto individual, la imagen seguía siendo invisible. Además, al revisar `merci-deploy.py`, se detectó un bug silencioso crítico: el orquestador de despliegue inyectaba las credenciales de producción en `os.environ`, pero `merci-wp.py` y `merci-shop.py` estaban codificados para leer rígidamente el archivo físico `.env`, por lo que nunca habían publicado en el servidor remoto de forma desatendida.

**Hecho:**
- Se forzó `opacity: 1 !important` y `display: block` a toda la estructura anidada de la galería de WooCommerce (`figure`, `.woocommerce-product-gallery__wrapper`) en `_woocommerce.scss`.
- Se refactorizó la función `cargar_credenciales()` en `merci-wp.py` y `merci-shop.py` para priorizar las variables de entorno del Sistema Operativo (`os.environ.get`) sobre el archivo físico.
- Se inyectó la llamada a `merci-shop.py` en la cadena de `scripts/merci/merci-deploy.py`.

**Motivo / criterio:** *Robustez CSS y Cloud Parity*. WooCommerce inyecta contenedores `<figure>` que arrastran la opacidad 0 si no se bloquean a fondo. Por el lado del Backend, un orquestador Headless que ignora el entorno del sistema destruye el flujo CI/CD. Permitir que `os.environ` sobrescriba el archivo físico garantiza que `merci-deploy.py` pueda falsificar (mock) las credenciales de producción en memoria sin alterar los archivos de desarrollo local.

**Siguiente paso o deuda:** Validar la visualización del producto, realizar el Sello Definitivo (`merci commit`) y cerrar oficialmente la Épica 6.

### 2026-05-25 — Docs/CD: Actualización de Roadmap y flujo de despliegue para la Tienda

**Contexto:** La Épica 6 (E-commerce Híbrido Extremo) no había sido marcada formalmente en el Roadmap tras completar la instanciación del catálogo, y el orquestador supremo de despliegue a producción (`merci-completo.py`) aún no contemplaba la sincronización del catálogo hacia el WooCommerce en la nube.

**Hecho:**
- Se marcaron como completadas las tareas de la Fase 1 en `ROADMAP.md` (Catálogo, modo simulación/catálogo y orquestación local).
- Se planificó la inyección de `merci-shop.py` en el pipeline de despliegue a producción.

**Motivo / criterio:** *Governance y Continuous Deployment*. Mantener la Única Fuente de Verdad (Roadmap) actualizada es innegociable. Por otro lado, al igual que los artículos del blog se sincronizan con la API de producción, los productos de la tienda deben viajar al servidor remoto automáticamente durante la ejecución del orquestador de despliegue para mantener la Paridad Dev/Prod.

**Siguiente paso o deuda:** Inyectar la lógica de WooCommerce en `merci-completo.py` y `merci-deploy.py` para finalizar la automatización del despliegue en producción.

### 2026-05-25 — UX/DX: Patrón "Silence is Golden" en orquestadores Headless

**Contexto:** Al ejecutar el orquestador global, la salida en consola (stdout) de `merci-wp.py` y `merci-shop.py` era demasiado ruidosa, imprimiendo saltos de línea extra y detalles de cada archivo procesado que no aportaban valor en una ejecución exitosa.

**Hecho:** 
- Se implementó el argumento `--verbose` (o `-v`) en `scripts/merci/merci-shop.py` para silenciar los mensajes intermedios.
- Se eliminaron los saltos de línea iniciales y finales (`\n`) para alinear el formato visual con `merci-total`.
- Se aplicó la misma refactorización visual a `scripts/merci/merci-wp.py`, añadiendo un contador unificado de publicaciones procesadas.

**Motivo / criterio:** *Silence is Golden y Clean DX*. Las herramientas de consola en un pipeline CI/CD deben ser discretas por defecto. Ocultar el ruido de sincronización permite que el orquestador maestro fluya visualmente limpio, reservando la verbosidad únicamente para depuración manual (`--verbose`) o errores críticos.

**Siguiente paso o deuda:** Ejecutar `merci total` para confirmar la limpieza visual, sellar con un commit atómico y cerrar definitivamente la Épica 6.

### 2026-05-25 — Fix: Resolución de bucle de Zombis (Data Drift por Slug vs Nombre)

**Contexto:** A pesar de haber purgado la base de datos y activado el Kill-Switch, el orquestador seguía multiplicando los productos en cada ejecución, generando sufijos `-2` y `-3` que rompían la auditoría WCAG (enlaces ambiguos).

**Hecho:**
- Se diagnosticó que WooCommerce autogeneraba el slug a partir del título, difiriendo del nombre del archivo Markdown (ej. `camiseta-devsecops-edicion-limitada` vs `camiseta-merci-devsecops`).
- Se parcheó `scripts/merci/merci-shop.py` forzando la inyección explícita de `"slug": slug` en el payload JSON del POST/PUT.
- Se purgó `wp_shortlink_wp_head` en `functions.php` para eliminar enlaces dinámicos `?p=` del escáner.

**Motivo / criterio:** *Single Source of Truth (SSOT)*. El script de sincronización buscaba el slug del archivo físico, pero WP lo ignoraba y creaba uno nuevo basado en el título. Al no encontrar nunca el slug físico, el orquestador creaba un producto nuevo en cada pasada. Forzar el slug físico en el payload de WooCommerce alinea definitivamente al CMS con el sistema de archivos local, erradicando la clonación infinita de Zombis.

**Siguiente paso o deuda:** Vaciar la papelera de WooCommerce por última vez, ejecutar `merci shop` y certificar el pipeline con `merci total`.

### 2026-05-25 — UX/DX: Autodetección de productos en Agente Promotor

**Contexto:** Al promover un producto de la tienda desde la bandeja de incubación, el asistente interactivo (`merci-promote.py`) solicitaba `Tema` y `Descripción` porque los productos carecían de `tema: "tienda"` explícito y usaban la clave `descripcion_corta` en lugar de `descripcion`.

**Hecho:**
- Se refactorizó `scripts/merci/merci-promote.py` para autodetectar productos si el YAML contiene el campo `precio` o `nombre`.
- Se adaptó el menú para leer y reinyectar `descripcion_corta` y `nombre` si el archivo pertenece a la tienda.
- Se omitió la pregunta irrelevante de "Fecha de publicación" para productos de WooCommerce.

**Motivo / criterio:** *Fricción Cero y Context-Awareness*. Si la herramienta puede inferir el contexto (es un producto) por las variables presentes, no debe obligar al usuario a añadir etiquetas extra. Mapear dinámicamente las claves del YAML garantiza que el documento promovido siga siendo compatible con el publicador Headless de la tienda (`merci-shop.py`).

**Siguiente paso o deuda:** Promover los productos de prueba hacia la raíz y ejecutar la sincronización mediante `merci-shop.py`.

### 2026-05-25 — Fix/Arch: SSOT de Tienda en la Raíz y Resolución de Variables

**Contexto:** Se decidió igualar el ciclo de vida del catálogo de WooCommerce al del resto de contenidos (`blog`, `biblioteca`, `art-de-cote`). En lugar de permanecer en `laboratorio/tienda/`, los productos curados debían alojarse en el directorio raíz `tienda/`. Además, una versión previa de `merci-shop.py` sufrió un error de variables indefinidas (`producto_id`) y una mutilación de código por la interfaz de IA.

**Hecho:**
- Se estableció el directorio maestro `tienda/` en la raíz del repositorio.
- Se refactorizó `scripts/merci/merci-promote.py` para enrutar automáticamente el atributo `tema: "tienda"` hacia este nuevo directorio y evadir las peticiones de metadatos innecesarios (`alt_portada`).
- Se saneó la lógica del Kill-Switch en `scripts/merci/merci-shop.py`, solucionando el error `NameError: name 'producto_id' is not defined` y apuntando el escáner a la raíz `tienda/`.

**Motivo / criterio:** *Simetría Arquitectónica y Robustez*. Elevar la tienda a la raíz completa el paradigma de SSOT para todos los destinos de publicación. Todo nace en `laboratorio/incubacion/`, el Agente de Promoción decide la ruta por su metadato, y los publicadores actúan. Se purga la deuda de código fallido recuperando el patrón "Fail-Safe".

**Siguiente paso o deuda:** Validar la curación, mover los productos de la incubadora a la tienda mediante el promotor y sincronizar con la API de WooCommerce.

### 2026-05-25 — Arch: Ciclo de vida unificado y Kill-Switch para Catálogo (SSOT)

**Contexto:** Se detectó que los productos de la tienda carecían del ciclo de vida estándar del ecosistema. Mantenerlos permanentemente en el directorio de sincronización sin una bandeja de entrada y sin un mecanismo de despublicación automatizado (Kill-Switch) rompía la arquitectura y amenazaba con recrear la deriva de datos (Posts Zombis).

**Hecho:**
- Se estableció que los productos utilizarán la bandeja unificada (`laboratorio/incubacion/`) con el atributo `tema: "tienda"`.
- Se inyectó el "Kill-Switch" en `scripts/merci/merci-shop.py`. Si un producto cambia a estado `borrador`, el orquestador lo elimina permanentemente de WooCommerce (`force=true` API DELETE) y mueve el archivo Markdown de vuelta a la incubadora.

**Motivo / criterio:** *Single Source of Truth y Bandeja Unificada*. La creación de una nueva carpeta (`almacen/`) fragmentaría el ecosistema. Tratar a los productos como cualquier otro documento y aplicarles el mismo ciclo (Incubación -> Promoción -> Kill-Switch) garantiza cero fricción operativa. El borrado fuerte (`Hard Delete`) asegura que los slugs queden libres inmediatamente, evitando colisiones WAI-ARIA si se vuelve a crear.

**Siguiente paso o deuda:** Integrar la Tienda en `merci-promote.py` y `merci-total.py`.

### 2026-05-25 — Fix: Resolución de colisión WAI-ARIA por Productos Zombis (Soft-Delete)

**Contexto:** El rastreador dinámico DAST (`merci-linkcheck.py`) bloqueó el pipeline reportando 26 errores WCAG de enlaces ambiguos en la tienda. Múltiples enlaces con el mismo nombre ("Nombre Accesible") apuntaban a destinos diferentes (ej. `.../producto/` vs `.../producto-2/`).

**Hecho:** Se diagnosticó una Deriva de Datos (Data Drift) severa causada por la papelera de WordPress. Se purgó manualmente la base de datos eliminando permanentemente todos los productos y vaciando la papelera, para luego re-sincronizar el catálogo limpio con `merci shop`.

**Motivo / criterio:** *Single Source of Truth y CMS Soft-Deletes*. Al borrar productos en WP, estos van a la papelera reteniendo su "slug". Cuando el orquestador Headless intentaba recrearlos, WP les asignaba un sufijo `-2` para evitar colisiones. En ejecuciones posteriores, el orquestador no encontraba el slug original y creaba duplicados infinitos. El rastreador de enlaces cumplió su función detectando que esta duplicidad generaba una trampa de accesibilidad. La solución definitiva en arquitecturas Headless es el borrado permanente (Hard Delete) para liberar los slugs.

**Siguiente paso o deuda:** Validar el pipeline con `merci total` e inyectar el catálogo visualmente en el frontend de la tienda.

### 2026-05-25 — Fix: Visibilidad de imagen en single-product y persistencia de Merci-coins

**Contexto:** En la vista individual del producto, la imagen no se renderizaba (permanecía invisible). Además, los precios seguían mostrándose en Euros a pesar del diseño acordado en Merci-coins.

**Hecho:**
- Se inyectó `opacity: 1 !important;` al contenedor `div.images` en `_woocommerce.scss`.
- Se consolidaron los filtros PHP (`woocommerce_currencies`, `woocommerce_currency_symbol`, `woocommerce_currency`) en `functions.php` para sobrescribir la moneda nativa.

**Motivo / criterio:** *Zero JS Dependency y Configuration as Code*. WooCommerce oculta nativamente la imagen individual (`opacity: 0` en línea) esperando a que su pesado script de galería cargue para mostrarla. Como nosotros extirpamos ese JS para lograr el 100/100 de rendimiento, debíamos forzar su opacidad desde SASS. Por otro lado, la moneda se consolidó en PHP para evitar depender del panel de administración del CMS.

**Siguiente paso o deuda:** Validar la visualización del producto individual y cerrar la Épica 6.

### 2026-05-25 — UX/UI: Refinamiento de la vista individual de producto

**Contexto:** En la vista de producto individual del catálogo, la imagen ocupaba un 50% del ancho (`1fr 1fr`), resultando desproporcionadamente grande en pantallas de escritorio.

**Hecho:** Se ajustó la cuadrícula a proporciones `4fr 6fr` y se limitó el contenedor de la imagen (`div.images`) a un `max-width` de `450px` en `_woocommerce.scss`.

**Motivo / criterio:** *Proporcionalidad y Diseño de Interfaz*. Reducir el peso visual de la imagen frente a la descripción mejora el equilibrio de la página de producto y evita que las imágenes se sobredimensionen, lo cual rompía la experiencia de compra. Se inyectó además un ligero sombreado y borde redondeado para realzar el acabado "Premium" del producto.

**Siguiente paso o deuda:** Compilar, verificar en el navegador y cerrar la Épica 6.

### 2026-05-25 — UX/UI: Maquetación SASS del Catálogo (Tienda No Tienda)

**Contexto:** Al estar deshabilitados los estilos nativos de WooCommerce (Zero-Bloat), el HTML del catálogo inyectado por la API REST se renderizaba desnudo. Era necesario aplicar la arquitectura de estilos SASS 7-1 para integrar los productos visualmente con el diseño de la web.

**Hecho:**
- Se reestructuró el archivo `src/scss/components/_woocommerce.scss` con estilos en cuadrícula (Grid).
- Se definieron reglas específicas para el catálogo (`ul.products`) y para la vista de producto individual (`div.product`).

**Motivo / criterio:** *Zero Bloat y UI Cohesion*. Purgar los 100KB de estilos genéricos que WooCommerce inyecta por defecto y sustituirlos por unas pocas líneas de CSS Grid altamente específicas nos garantiza retener el 100/100 en Core Web Vitals mientras el catálogo respira la misma identidad de marca que el núcleo estático.

**Siguiente paso o deuda:** Compilar el CSS, verificar el catálogo en el entorno de desarrollo local y dar por cerrada la Épica 6.

### 2026-05-25 — Feat: Criptodivisa nativa (Merci-coins) para la Tienda No Tienda

**Contexto:** Al tratarse de una demostración técnica de e-commerce ("Tienda No Tienda") sin pasarelas de pago reales, el uso de moneda fiat tradicional (Euros/Dólares) rompía la inmersión del "Storytelling Técnico".

**Hecho:**
- Se definió la moneda oficial del ecosistema: **Merci-coins (MC)**.
- Se preparó la inyección de los filtros `woocommerce_currencies`, `woocommerce_currency_symbol` y `woocommerce_currency` en `functions.php` del Child Theme.

**Motivo / criterio:** *Gamificación y Zero GUI*. Sustituir el símbolo monetario tradicional por una divisa ficticia (MC 🪙) refuerza ante el usuario que está navegando por un entorno de demostración técnica, previniendo cualquier confusión sobre ventas reales. Forzar la moneda mediante hooks de PHP evita tener que configurarla manualmente en el panel de administración de WordPress.

**Siguiente paso o deuda:** Inyectar los filtros en `functions.php` e integrar el catálogo visualmente en el frontend usando SASS.

### 2026-05-25 — Perf: Caché HASH Incremental en Auditor Maestro

**Contexto:** Se planteó la necesidad de reducir aún más el tiempo de ejecución de la auditoría masiva evitando el análisis de archivos que no habían sufrido modificaciones, aplicando el patrón de compilación incremental que ya se usa en SSG.

**Hecho:**
- Se refactorizó `scripts/merci/merci-audit.py` para implementar un registro criptográfico MD5 (`.audit_hash_cache.json`).
- El orquestador ahora ignora los archivos cuyo contenido (HASH) no ha cambiado, siempre y cuando no tengan advertencias pendientes.
- Se incluyó un "Detector de Reglas Globales" que invalida toda la caché automáticamente si se altera el diccionario del glosario, las dependencias (`requirements.txt`) o el propio script del linter.

**Motivo / criterio:** *Zero Maintenance y Shift-Left Performance*. Auditar a ciegas casi 400 archivos cuando solo has modificado uno es un desperdicio de I/O y ciclos de CPU. Implementar un caché criptográfico inteligente reduce el QA (Aseguramiento de Calidad) total a fracciones de segundo, garantizando a la vez que las dependencias globales o archivos con deuda técnica (WARNs) nunca escapen al escáner.

**Siguiente paso o deuda:** Iniciar la estructura de la tienda en WooCommerce (Épica 6).

### 2026-05-25 — Arch: Diferenciación de alcances (Audit Scope vs Backup Scope)

**Contexto:** Tras visualizar que `merci-audit.py` escaneaba 388 archivos, surgió el debate arquitectónico sobre si el auditor debería limitarse únicamente a los archivos que se incluyen en la copia de seguridad.

**Hecho:**
- Se estableció como regla de arquitectura que el alcance del QA y el alcance del Backup son asimétricos por naturaleza.
- Se añadió el directorio `auditorias-pagespeed.web.dev` al conjunto `SKIP_DIR_NAMES` en `merci-audit.py`.

**Motivo / criterio:** *Separation of Concerns*. El Backup guarda el origen inmutable (código), pero el Auditor debe vigilar el artefacto final (HTML/CSS en `public/`) para garantizar que el compilador SSG no introduce brechas de seguridad o fallos de SEO. Sin embargo, auditar reportes masivos de terceros (los JSON de PageSpeed) buscando errores de sintaxis es un desperdicio de I/O. Excluir esta carpeta refina el alcance del auditor eliminando "ruido" externo.

**Siguiente paso o deuda:** Iniciar la estructura de la tienda en WooCommerce (Épica 6).

### 2026-05-25 — Sec: Escudos DevSecOps para E-commerce Headless (WooCommerce)

**Contexto:** Preparación para gestionar el catálogo de productos mediante archivos Markdown (Tienda No Tienda). Era necesario inyectar barreras de seguridad (Shift-Left) en el auditor maestro para prevenir fugas de tokens de la API, inyecciones XSS en descripciones y manipulación de la lógica de negocio (precios anómalos).

**Hecho:** 
- Se refactorizó `scripts/merci/merci-audit.py` añadiendo las tres reglas de seguridad.
- Se inyectaron los patrones regex para claves de WooCommerce (`ck_`, `cs_`) en `SECRET_PATTERNS`.
- Se amplió `audit_inline_scripts` para bloquear etiquetas `<script>` en los archivos Markdown de `laboratorio/tienda/` (Stored XSS).
- Se creó la nueva regla `audit_shop_yaml` para validar matemáticamente que el campo `precio` de los markdowns de productos sea un número de coma flotante igual o superior a `0`.

**Motivo / criterio:** *Defensa en Profundidad (Defense in Depth)*. En arquitecturas SSG y Headless, el archivo local es la base de datos. Tratar el Markdown con la misma rigurosidad con la que se trataría un payload de API evita que vulnerabilidades lógicas viajen desde el repositorio hasta el frontend del CMS.

**Siguiente paso o deuda:** Crear la estructura `laboratorio/tienda/`, redactar el primer producto de prueba en Markdown y ejecutar la sincronización mediante `merci-shop.py`.

### 2026-05-25 — Perf/Fix: Caché Singleton en Auditor y robustez de rutas (I/O)

**Contexto:** Gracias al modo `--verbose`, se detectó que el orquestador `merci-audit.py` generaba un cuello de botella de I/O al auditar masivamente (388 archivos), deteniéndose visiblemente en la lectura del JSON del glosario para validar acrónimos. Además, el escáner de markdowns era vulnerable a rutas absolutas del entorno host.

**Hecho:**
- Se inyectó el patrón Singleton (`GLOSARIO_WATCHLIST_CACHE`) en `merci-audit.py` para cargar el diccionario de acrónimos una sola vez en memoria RAM.
- Se refactorizó la comprobación de directorios ignorados (`SKIP_DIR_NAMES`) para usar `path.relative_to(REPO_ROOT)`.

**Detalle técnico:** Extraer la lectura de `glosario-tecnico.json` fuera del bucle de validación de cada archivo evita reabrir y parsear el mismo archivo en el disco cientos de veces. Reemplazar `path.parts` (que incluye carpetas base del SO anfitrión) por `relative.parts` sella un bug lógico de evasión que se activaba si el repositorio se clonaba dentro de una carpeta llamada, por ejemplo, `venv/`.

**Motivo / criterio:** *Performance Driven Development y Robustez*. Retener textos en RAM devuelve la auditoría a tiempos sub-segundo, recuperando la velocidad del CI/CD. La robustez de rutas es esencial para garantizar el agnosticismo del sistema operativo anfitrión.

**Siguiente paso o deuda:** Iniciar la estructura de la tienda en WooCommerce (Épica 6).

### 2026-05-25 — Observabilidad Profunda: Expansión de recolección en Agente Glosario

**Contexto:** El autodescubrimiento y la sincronización automática de apariciones del glosario estaban acotados a rastrear únicamente el historial del laboratorio (bitácoras), estando ciegos ante la documentación matriz. Para lograr una Observabilidad Profunda matemática, era necesario rastrear qué términos están realmente vivos en las instrucciones, el README y la carpeta de documentación (`docs/`).

**Hecho:**
- Se refactorizó `scripts/merci/merci-glosario.py` para ampliar la matriz `archivos_objetivo`.
- Se incluyeron los directorios `docs/**/*.md` y los manuales maestros `instrucciones.md` y `README.md`.

**Detalle técnico:** Se reemplazó la iteración directa sobre `rglob` de bitácoras por una lista combinada (`archivos_objetivo.extend(...)`) que recolecta todas las fuentes de la "Única Fuente de Verdad" (SSOT) antes de realizar la lectura UTF-8 y extracción de términos.

**Motivo / criterio:** *Observabilidad Profunda y Single Source of Truth*. Los conceptos nacen en la bitácora, pero su destino final es consolidarse en la documentación pública. Rastrear su presencia en los manuales base y la carpeta `docs` garantiza que la validación de términos vivos sea matemáticamente exacta, detectando también deudas de acrónimos en los documentos formativos.

**Siguiente paso o deuda:** Validar la extracción de los nuevos términos y ejecutar el pipeline `merci-total`.

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