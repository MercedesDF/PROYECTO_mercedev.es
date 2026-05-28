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

**Motivo / criterio:** *Aislamiento Arquitectónico (Zero Bloat)*. Inyectar el botón durante el ciclo de vida del "Clon Efímero" justo antes de subirlo por RSYNC permite que el código fuente matriz permanezca completamente agnóstico y limpio. Los usuarios que clonen el Boilerplate en sus máquinas jamás verán este botón, pero estará siempre presente en la demostración en vivo.

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