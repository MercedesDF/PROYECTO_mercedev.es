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