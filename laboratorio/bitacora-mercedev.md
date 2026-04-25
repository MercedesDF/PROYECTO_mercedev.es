# Bitácora del proyecto mercedev.es

## Para qué sirve este archivo

- **Yo futuro:** recuperar en minutos qué se decidió, por qué, y cómo se ejecutó algo técnico sin rebuscar en el chat o en commits sueltos.
- **Biblioteca (al cerrar el proyecto):** aquí vive el borrador narrativo y técnico; luego se depura y se traslada a `biblioteca/` como piezas definitivas (por estantería o tema), siguiendo la idea de “activo de conocimiento” del proyecto.

No sustituye a `instrucciones.md` (directrices y rol del asistente). Complementa el día a día con **hechos, comandos y lecciones**.

---

## Cómo mantenerlo (acuerdo simple)

1. **Añadir entradas al principio** de la sección “Registro cronológico”, con la plantilla de abajo. El registro es **acumulativo**: lo ya escrito forma parte del historial y **no se reemplaza** por nuevas sesiones (así no se pierde contexto ni fechas).
2. **Una entrada por sesión o por tema cerrado** (lo que resulte más claro al escribir).
3. Si algo fue un error o una vulnerabilidad evitada, opcionalmente usar los **tres átomos** del proyecto (Desafío → Maniobra → Aprendizaje/Deuda) en el cuerpo de la entrada.
4. **Correcciones excepcionales** (typo, dato incorrecto, redacción de un solo párrafo, retirada de información sensible): editar solo el fragmento necesario o añadir una línea aclaratoria bajo la entrada; evitar reescribir todo el archivo o borrar entradas enteras sin motivo documentado.

### Plantilla para nuevas entradas

Copia el bloque y rellénalo.

```markdown
### AAAA-MM-DD — Título corto del cambio o sesión

**Contexto:** (qué querías lograr o qué problema apareció)

**Hecho:** (lista breve: archivos, fases del roadmap, PR/commit si aplica)

**Detalle técnico:** (comandos, rutas, flags; solo lo que necesites recordar)

**Motivo / criterio:** (por qué esta opción y no otra)

**Siguiente paso o deuda:** (qué queda pendiente)
```

---
## Registro cronológico

### 2026-04-25 — Refactor: Arquitectura documental en 4 volúmenes (Saga mercedev)

**Contexto:** La bitácora del laboratorio crecía exponencialmente. Se requería trazar una línea divisoria clara entre la creación del motor (Fases 1-6) y las etapas posteriores, planificando el futuro de la identidad del proyecto.

**Hecho:**
- Se definió la arquitectura de conocimiento en 4 volúmenes: Vol I (Nacimiento del Boilerplate), Vol II (Construcción y automatización), Vol III (Vida oculta de Merci) y Vol IV (Vida pública de Merci).
- Se refactorizó el archivo del Volumen I en la biblioteca.
- Se purgó el historial antiguo de Fases 1 a 6 del laboratorio activo mediante un script de truncamiento.

**Motivo / criterio:** *Information Architecture* y escalabilidad cognitiva. Un documento infinito es inmanejable. Tratar el conocimiento técnico como una "Saga Literaria" encaja perfectamente con el pilar pedagógico, permitiendo que el laboratorio actual sea exclusivamente el borrador en vivo del Volumen II.

**Siguiente paso o deuda:** Iniciar la Fase 7.4 y redactar el prólogo del Volumen I cuando se considere oportuno.

### 2026-04-25 — Refactor: Establecimiento de regla pedagógica para bitácoras (Libro Presentación)

**Contexto:** Un extracto crudo del historial (Fases 1 a 6) fue promovido a producción automáticamente por un script, violando el pilar pedagógico del proyecto al presentar un volcado de logs sin narrativa introductoria.

**Hecho:**
- Se despublicó (`estado: "borrador"`) el archivo `biblioteca/bitacora-merci-boilerplate.md`.
- Se inyectó un esqueleto de "Prólogo" obligatorio.
- Se asienta la regla arquitectónica: Los datos crudos (logs) nunca se publican sin un marco de presentación didáctico.

**Motivo / criterio:** *Information Architecture* (Arquitectura de la Información) y UX Pedagógica. Un listado cronológico de commits no constituye un activo de conocimiento por sí solo si carece de contexto. Envolver el "ruido" técnico en un prólogo humano y estructurado transforma el historial en un verdadero "Libro".

**Siguiente paso o deuda:** Escribir el prólogo del Boilerplate y proceder con la planificación de la Fase 7.4.

### 2026-04-25 — Refactor: Escaneo dual y prevención de borradores zombis (merci-promote)

**Contexto:** Los documentos en `biblioteca/` que eran despublicados manualmente (pasando a `estado: "borrador"`) se convertían en "Dark Data" (datos invisibles), ya que el asistente de promoción solo escaneaba el `laboratorio/`. Esto forzaba a la edición manual del YAML para republicarlos, rompiendo el flujo.

**Hecho:**
- Se refactorizó `merci-promote.py` para realizar un escaneo dual (Laboratorio + Biblioteca).
- Se añadió el campo interactivo de `fecha` para permitir mantener la fecha original de publicación.
- Se dividió la lógica final para soportar traslados físicos (`unlink()`) y actualizaciones *in-place*.

**Motivo / criterio:** *Content Lifecycle Management* (Gestión del Ciclo de Vida del Contenido). Centralizar en una única herramienta CLI la transición de cualquier estado inmaduro o despublicado hacia la publicación definitiva elimina la fricción técnica. Pre-rellenar los inputs interactivos con los metadatos preexistentes maximiza la velocidad de republicación sin comprometer las validaciones de calidad estricta.

**Siguiente paso o deuda:** Con el ciclo de contenidos perfeccionado, abordar formalmente la planificación de la Fase 7.4 (Mantenimiento y Mejora Continua).

### 2026-04-25 — Fix: Despublicación activa de artefactos huérfanos en SSG

**Contexto:** Se detectó una fisura en el ciclo de vida del dato. Al cambiar manualmente un documento en `biblioteca/` de estado `publicado` a `borrador`, el orquestador lo saltaba y lo excluía del índice, pero los archivos HTML y PDF generados previamente quedaban huérfanos en `public/`, permaneciendo accesibles mediante su URL directa (fuga de información).

**Hecho:**
- Se refactorizó la máquina de estados en `scripts/merci/merci-publish.py`.
- Se implementó una lógica de "Despublicación Activa" (Kill-Switch).

**Detalle técnico:** Antes de abortar el procesamiento de un archivo que no sea `publicado`, el script resuelve las rutas de salida (`html_target.exists()`) y ejecuta un `unlink()` para purgar físicamente los activos del servidor si existen, emitiendo una alerta `🗑️ Despublicando` por consola.

**Motivo / criterio:** *State Synchronization* (Sincronización de Estado). El estado `borrador` no debe ser solo una omisión de compilación, sino una orden destructiva en el entorno de producción que garantice que el frontend refleje exactamente la intención actual del origen de datos, previniendo artefactos zombis.

**Siguiente paso o deuda:** Iniciar la planificación de la Fase 7.4 (Mantenimiento y mejora continua).

### 2026-04-25 — Feat: Asistente interactivo de promoción (merci-promote.py)

**Contexto:** Existía un hueco operativo (Fase 7.3) entre la redacción de un borrador en el `laboratorio/` y su publicación en la `biblioteca/`. Hacer este traslado manualmente era propenso a errores (olvidos de metadatos, fechas incorrectas o estados inconsistentes).

**Hecho:**
- Se creó el script interactivo CLI `scripts/merci/merci-promote.py`.
- Se marcaron los hitos de la Fase 7.3 como completados en el `README.md`.
- Se validó la promoción del primer borrador de prueba (`test-borrador.md`).

**Detalle técnico:** El script escanea el directorio efímero, parsea el YAML sin dependencias externas (`re` y manipulación de cadenas), solicita la curación interactiva de campos críticos (bloqueando si falta el `alt_portada` para WAI-ARIA), sella la fecha actual, cambia el `estado` a `publicado` y mueve físicamente el archivo al directorio definitivo.

**Motivo / criterio:** *Fricción Cero y Shift-Left Data Quality*. Proveer una herramienta de consola (CLI) para "curar" el documento antes de moverlo previene que archivos incompletos contaminen el entorno de producción. La interactividad actúa como un *checklist* guiado que garantiza el cumplimiento estricto de la accesibilidad y el SEO estructural.

**Siguiente paso o deuda:** Comenzar la planificación de la Fase 7.4 (Mantenimiento y mejora continua) y Fase 7.5, aprovechando que el ejecutor inteligente `merci promote` ya lo reconoce automáticamente.

### 2026-04-25 — Fix: Retrocompatibilidad YAML y validación WAI-ARIA

**Contexto:** Al implementar la máquina de estados y la validación WAI-ARIA estricta en el orquestador (`merci-publish.py`), el documento heredado `cuadernillo-alias-absolutos.md` fue bloqueado y excluido de la compilación por carecer de los campos obligatorios `estado` y `alt_portada`.

**Hecho:**
- Se parcheó manualmente `biblioteca/cuadernillo-alias-absolutos.md` inyectando `estado: "publicado"` y una descripción detallada en `alt_portada`.
- Se ejecutó `merci-publish.py`, confirmando que el orquestador compila el documento y genera el PDF correctamente.

**Motivo / criterio:** Principio "Fail-Fast" y cero tolerancia a la deuda técnica. Que el orquestador bloquee un archivo antiguo demuestra que el escudo de accesibilidad funciona empíricamente. Parchear el origen de datos (el Markdown) es la única vía permitida para integrarlo, garantizando que el HTML resultante mantenga la puntuación 100/100 en Core Web Vitals (Accesibilidad).

**Siguiente paso o deuda:** Diseñar e implementar la herramienta de promoción interactiva (`merci-promote.py`) para la Fase 7.3.

### 2026-04-25 — Feat: Máquina de estados y validación de accesibilidad en orquestador

**Contexto:** Se requería que el orquestador de publicación (`merci-publish.py`) discriminara entre borradores y documentos definitivos listos para compilar, además de blindar la accesibilidad exigiendo la presencia del atributo `alt_portada`. Paralelamente, surgió el dilema de si optimizar el motor introduciendo un sistema de caché basado en hashes de archivos.

**Hecho:**
- Se implementó una máquina de estados (Feature Toggle) basada en la clave YAML `estado` en `merci-publish.py`.
- Se introdujo una aserción estricta WAI-ARIA que bloquea el parseo si el YAML carece de `alt_portada`.
- Se descartó deliberadamente la implementación de caché por hashes.

**Detalle técnico:** El script ahora realiza retornos tempranos (`return False`) de forma silenciosa para archivos que no posean explícitamente `estado: "publicado"`. Asimismo, si el campo `alt_portada` está vacío, aborta la compilación de ese archivo lanzando un error en consola.

**Motivo / criterio:** *Premature Optimization* (Optimización Prematura). Procesar Markdown a HTML en Python es extremadamente rápido. Introducir una caché estática impediría que los artículos antiguos heredaran instantáneamente los cambios en el menú o el pie de página globales (Single Source of Truth) extraídos de la portada, provocando inconsistencia visual. Además, la aserción de la portada blinda mecánicamente la métrica de accesibilidad 100/100 de Lighthouse sin depender de la memoria del autor.

**Siguiente paso o deuda:** Desarrollar el flujo de promoción (Fase 7.3) mediante un script interactivo (`merci-promote.py`) para trasladar y estandarizar borradores desde el laboratorio hacia la biblioteca.

### 2026-04-25 — Refactor: Optimización de metadatos YAML para accesibilidad y pipeline

**Contexto:** Antes de diseñar el script de promoción de contenidos (Fase 7.3), era imperativo auditar la estructura de datos YAML para asegurar que soportara los requisitos de accesibilidad estricta (Core Web Vitals) y el control de flujo del orquestador.

**Hecho:**
- Se añadieron los campos `estado` y `alt_portada` a `docs/plantilla-cuadernillo.md`.
- Se refactorizó retroactivamente `biblioteca/auditoria-rendimiento.md` para cumplir con el nuevo esquema.

**Motivo / criterio:** *Shift-Left Data Design*. Añadir `alt_portada` garantiza desde el origen que el SSG (Static Site Generation) genere etiquetas `<img>` 100% compatibles con WAI-ARIA, evitando penalizaciones de Lighthouse. El campo `estado` (`borrador` vs `publicado`) dota al orquestador de una máquina de estados sencilla para filtrar documentos incompletos durante el proceso de compilación, protegiendo el entorno de producción.

**Siguiente paso o deuda:** Diseñar el flujo operativo y el script de Python para la promoción automatizada de contenidos (Fase 7.3).

### 2026-04-24 — Fix: Resolución de conflicto de enlace simbólico en producción

**Contexto:** Al ejecutar `git pull` en el servidor de producción (CloudPanel), Git abortó la sincronización alertando que los cambios locales en `public/blog` serían sobrescritos. Esto ocurrió porque el enlace simbólico había sido eliminado del índice del repositorio (`git rm --cached`) en una sesión anterior para aislarlo del control de versiones.

**Hecho:**
- Se eliminó temporalmente el enlace simbólico físico en el servidor de producción.
- Se ejecutó la actualización del repositorio (`git pull`) integrando el nuevo `.gitignore`.
- Se reconstruyó manualmente el enlace simbólico (`ln -s`) apuntando al directorio aislado de WordPress.

**Detalle técnico:** Comandos ejecutados secuencialmente en el servidor: `rm public/blog`, seguido de `git pull`, y finalmente `ln -s /home/mercedev-php/htdocs/wordpress /home/mercedev-php/htdocs/mercedev.es/public/blog`.

**Motivo / criterio:** Git implementa mecanismos de seguridad (Fail-Safe) para no destruir archivos locales sin seguimiento que colisionan con el árbol entrante. Destruir y recrear este puente de infraestructura tras aplicar el `.gitignore` actualizado vuelve a Git "ciego" ante el enlace, garantizando que los futuros despliegues fluyan con cero fricción.

**Siguiente paso o deuda:** Iniciar el diseño del flujo de promoción de contenidos (Fase 7.3).

### 2026-04-24 — Feat: Estandarización de plantillas de conocimiento (Fase 7.2)

**Contexto:** Para agilizar el flujo de creación de contenido y asegurar que todas las futuras publicaciones de la Biblioteca cumplan con los requisitos del orquestador (`merci-publish.py`), era necesario establecer una plantilla reutilizable.

**Hecho:**
- Se creó el archivo `docs/plantilla-cuadernillo.md`.
- Se consolidó la estructura obligatoria de metadatos (YAML Frontmatter) y la arquitectura de la información basada en 5 átomos (Contexto, Hecho, Detalle técnico, Motivo, Fuentes).

**Motivo / criterio:** Fricción Cero y Consistencia Editorial. Extraer el formato a una plantilla estática en el directorio de documentación evita que el autor dependa de la memoria o tenga que copiar archivos antiguos, garantizando que el pipeline SSG (Static Site Generation) y la inyección SEO no fallen por atributos omitidos.

**Siguiente paso o deuda:** Empaquetar el commit atómico, definir el flujo de movimiento Laboratorio -> Biblioteca (Fase 7.3) y continuar el roadmap.

### 2026-04-24 — QA: Falsos positivos de accesibilidad por extensiones del navegador

**Contexto:** Durante la auditoría manual de accesibilidad por teclado (tabulación), se detectó que el foco caía en un "agujero negro" de múltiples saltos (tabs fantasma) antes de retornar a la navegación de la web.

**Hecho:**
- Se inyectó un rastreador de eventos JS en la consola del navegador (`document.addEventListener('focusin', ...)`).
- El registro (log) reveló que el foco estaba siendo secuestrado por el elemento `<chatgpt-sidebar>`, el cual es inyectado de forma invisible por una extensión instalada en el navegador del usuario.

**Motivo / criterio:** Aislamiento del entorno de pruebas. Las extensiones del navegador inyectan Shadow DOM y elementos en el código fuente de las páginas visitadas, alterando el árbol de accesibilidad real. Las auditorías manuales (WAI-ARIA) y automáticas (Lighthouse) deben ejecutarse siempre en ventanas de Incógnito/InPrivate puras para evitar depurar "código fantasma" ajeno al proyecto.

**Siguiente paso o deuda:** Realizar el commit atómico de este aprendizaje y avanzar a la Fase 7.2.

### 2026-04-24 — Fix: Purgado de "Tabs Fantasma" y botón de salto a contenido

**Contexto:** Realizando pruebas de accesibilidad, se detectaron dos comportamientos indeseados durante la navegación por teclado: 1) el botón de accesibilidad "Saltar al contenido principal" resultaba redundante según los nuevos criterios, y 2) tras sobrepasar el footer con la tecla tabulador, el foco caía en unos 10 "tabs fantasma" antes de retornar al navegador web.

**Hecho:**
- Se eliminó completamente la etiqueta `<a href="#main" class="skip-link">` de la portada estática (`public/index.html`) y de la plantilla dinámica de WordPress (`src/wp-theme/merci-theme/index.php`).
- Se purgó el bloque CSS `.skip-link` de la arquitectura SASS (`_header.scss`) y se retiró el `tabindex="-1"` del contenedor `<main>`.
- Se añadió el filtro `add_filter('show_admin_bar', '__return_false');` en `functions.php`.
- Se ejecutó el pipeline completo de validación y compilación (`merci-total.py`).

**Motivo / criterio:** Los "tabs fantasma" en la ruta dinámica (`/blog`) eran provocados por los enlaces ocultos de la *Admin Bar* inyectada por WordPress mediante `wp_footer()` para usuarios logueados. Dado que el frontend está desacoplado (estilo Headless/Boilerplate), mantener la barra generaba conflictos de foco. Ocultarla purga estos enlaces invisibles del DOM y restaura la paridad entre las capas estática y dinámica.

**Siguiente paso o deuda:** Validar la limpieza de la navegación con tabulador sin los enlaces fantasma.

### 2026-04-24 — Fix: Refactorización arquitectónica de foco WAI-ARIA (Eliminación de tabindex en body)

**Contexto:** Se detectó que inyectar `tabindex="-1"` en la etiqueta `<body>` constituía un anti-patrón de accesibilidad. Hacer que el contenedor global del DOM fuera enfocable causaba que los lectores de pantalla reiniciaran la lectura desde el principio al activar el enlace "Volver arriba", abría vectores de "secuestro de foco" por clics inadvertidos y provocaba bugs visuales (Tap Highlight) en navegadores WebKit como iOS Safari.

**Hecho:**
- Se eliminó el atributo `tabindex="-1"` de la etiqueta `<body>` en `public/index.html`, `src/wp-theme/merci-theme/index.php` y `scripts/merci/merci-publish.py`.
- Se trasladó el identificador `id="top"` y su respectivo `tabindex="-1"` al elemento `<header>`, siendo este el primer bloque lógico y semántico de la estructura.
- Se recompilaron los activos estáticos de la biblioteca mediante `.venv/bin/python scripts/merci/merci-publish.py`.

**Motivo / criterio:** WAI-ARIA estricto y Focus Management. El foco de teclado nunca debe viajar al elemento raíz del documento (`<body>`). Al delegar la recepción del foco al `<header>`, el usuario que activa "Volver arriba" queda correctamente posicionado al inicio del contenido semántico, listo para interactuar con la navegación principal sin efectos colaterales indeseados.

**Siguiente paso o deuda:** Validar la restitución del comportamiento esperado del tabulador y proceder a empaquetar el commit atómico.

### 2026-04-24 — Fix: Resolución de foco en enlaces ancla WAI-ARIA (Tabindex)

**Contexto:** Tras implementar los enlaces de accesibilidad ("Saltar al contenido" y "Volver arriba"), se reportó que la navegación por teclado (Tabulador) seguía desfasada. Al hacer clic en los enlaces ancla, el navegador desplazaba la pantalla, pero el foco interno del teclado no viajaba al destino, obligando al usuario a tabular múltiples veces por la interfaz del navegador.

**Hecho:**
- Se inyectó el atributo `tabindex="-1"` en los contenedores destino (`<main id="main">` y `<body id="top">`) en todos los archivos estructurales (`index.html`, `merci-publish.py`, `index.php`).
- Se añadió la regla CSS `[tabindex="-1"]:focus { outline: none; }` en `_header.scss` para prevenir bordes de foco antiestéticos al activarse.
- Se aprovecharon los cambios para inyectar las anclas faltantes en la capa dinámica (`index.php`) que habían sido omitidas.

**Motivo / criterio:** Gestión estricta del foco (Focus Management). Los navegadores modernos no mueven automáticamente el cursor de tabulación a elementos semánticos (como `<main>` o `<body>`) al resolver un enlace ancla a menos que se declaren explícitamente como enfocables mediante `tabindex="-1"`. Este atributo permite recibir foco vía enlace sin alterar el orden natural de tabulación.

**Siguiente paso o deuda:** Validar la experiencia de tabulación, ejecutar un commit atómico y continuar con la Fase 7.2.

### 2026-04-24 — Fix: Resolución de conflicto de dependencias (Pillow 12 vs WeasyPrint)

**Contexto:** Al intentar instalar `weasyprint==63.0`, el gestor de paquetes `pip` arrojó un error de resolución imposible (`ResolutionImpossible`). Se diagnosticó que la versión `63.0` de WeasyPrint limitaba estrictamente su compatibilidad a `Pillow < 11`, colisionando frontalmente con `Pillow==12.2.0` (actualizado recientemente por motivos de seguridad).

**Hecho:**
- Se actualizó el anclaje en `requirements.txt` de `weasyprint==63.0` a la versión moderna `weasyprint==68.1`.

**Motivo / criterio:** Supply Chain Security. En ecosistemas DevSecOps, retroceder una librería base (Pillow) a una versión antigua con vulnerabilidades conocidas (CVE) para satisfacer a una herramienta de exportación secundaria es un antipatrón inaceptable. La solución arquitectónica correcta es avanzar la herramienta secundaria (WeasyPrint) hasta la versión (`68.1`) que dé soporte oficial a la librería parcheada.

**Siguiente paso o deuda:** Ejecutar la instalación de dependencias, validar la generación del PDF y dar por concluida la Fase 7.1.

### 2026-04-24 — Fix: Resolución de incompatibilidad de WeasyPrint (Supply Chain)

**Contexto:** Durante la generación del PDF en el orquestador de publicación (`merci-publish.py`), la ejecución colapsó con el error `AttributeError: 'super' object has no attribute 'transform'`. El diagnóstico reveló una incompatibilidad entre la versión anclada `weasyprint==62.1` y la actualización reciente de una de sus subdependencias internas (`pydyf`) en entornos con Python 3.12.

**Hecho:**
- Se actualizó la dependencia en `requirements.txt` de `weasyprint==62.1` a `weasyprint==63.0`.

**Motivo / criterio:** Mantenimiento de la cadena de suministro de software (Supply Chain). En DevSecOps, cuando una subdependencia transitiva rompe la librería principal, la maniobra correcta es dar el salto a la siguiente *release* estable del paquete anfitrión que haya mitigado la incompatibilidad, en lugar de intentar parchear el código fuente o degradar módulos individuales.

**Siguiente paso o deuda:** Re-instalar dependencias, validar la generación exitosa de los PDFs y dar por cerrada la funcionalidad.

### 2026-04-24 — Feat: Generación automatizada de artefactos PDF (WeasyPrint)

**Contexto:** Se requería dotar a la Biblioteca de la capacidad de generar y ofrecer versiones descargables en PDF de cada artículo para facilitar el consumo offline, la preservación del conocimiento y el formato de "libro/cuadernillo".

**Hecho:**
- Se integró la librería `weasyprint` en el pipeline de publicación.
- Se actualizó `merci-publish.py` para compilar un diseño específico de impresión (con portada generada dinámicamente usando metadatos YAML y saltos de página).
- Se inyectó un botón de descarga (`.card__download`) en las páginas HTML generadas apuntando a la nueva ruta `public/descargas/`.

**Motivo / criterio:** SSG Avanzado y Cero Fricción. Generar el PDF en el mismo instante de la compilación asegura que la versión web y la descargable jamás estén desincronizadas. Se utilizó WeasyPrint por ser el estándar más robusto y moderno en Python para interpretar HTML/CSS hacia PDF nativo sin depender de binarios de navegadores pesados.

**Siguiente paso o deuda:** Validar la visualización del PDF, actualizar la portada con los últimos artículos (si aplica) y dar por cerrada la Fase 7.1.

### 2026-04-24 — Refactor: Paridad WAI-ARIA en WP y corrección arquitectónica SASS 7-1

**Contexto:** Tras implementar el patrón de accesibilidad (skip-link y anclas de retorno) en el núcleo estático, la capa dinámica (WordPress) quedó desincronizada. Además, se detectó que los estilos del bloque principal (`.header`) debían ubicarse estrictamente según el patrón SASS 7-1.

**Hecho:**
- Se ubicó la regla `.skip-link` y los estilos de cabecera en `src/scss/layout/_header.scss` (reafirmando la arquitectura 7-1).
- Se inyectaron los identificadores `#top`, `#main` y el enlace de retroceso (`↑ Volver arriba`) en `src/wp-theme/merci-theme/index.php`.

**Motivo / criterio:** Paridad Dev-Prod y Arquitectura Estricta. En SASS 7-1, los contenedores estructurales (`header`, `footer`) pertenecen al directorio `layout/`, reservando `components/` para widgets reusables (`cards`, `buttons`). Mantener la accesibilidad sincronizada entre Nginx y PHP garantiza una experiencia unificada.

**Siguiente paso o deuda:** Validar la capa dinámica, empaquetar el commit atómico y comenzar la generación de artefactos PDF (Fase 7.1).

### 2026-04-24 — Feat: Patrones de accesibilidad WAI-ARIA (Skip-link y Volver arriba)

**Contexto:** Al auditar la navegación por teclado (Tab), se detectó que tras interactuar con la última publicación (segunda entrada), el foco escapaba a la interfaz del navegador, requiriendo unas 10 pulsaciones para dar la vuelta y reingresar a la web. Además, se forzaba al usuario a tabular por todo el menú principal en cada carga de página.

**Hecho:**
- Se inyectó un enlace oculto `.skip-link` (`Saltar al contenido principal`) al inicio del `<header>`, que se hace visible al recibir el foco.
- Se implementó un enlace de ancla (`↑ Volver arriba`) en el footer.
- Se actualizaron las etiquetas `<body>` y `<main>` en `public/index.html` y `merci-publish.py` añadiendo los anclajes de ID (`#top`, `#main`).

**Motivo / criterio:** WAI-ARIA y Experiencia de Usuario (UX) inclusiva. Un usuario de teclado no debe caer en un "bucle ciego" al llegar al final de la página, ni verse obligado a recorrer menús repetitivos para leer el contenido.

**Siguiente paso o deuda:** Compilar, verificar el funcionamiento con el tabulador, empaquetar el commit atómico y proceder con los PDFs.

### 2026-04-24 — Feat: Enlace de retroceso (UX) en publicaciones individuales

**Contexto:** Las páginas individuales generadas por `merci-publish.py` carecían de un método rápido y contextual para regresar al índice temático de la Biblioteca, obligando al usuario a usar el botón "Atrás" del navegador o buscar en el menú principal.

**Hecho:**
- Se añadió la clase BEM `.card__back-link` en `src/scss/components/_card.scss`.
- Se actualizó el orquestador `scripts/merci/merci-publish.py` para inyectar dinámicamente este enlace (`← Volver a la Biblioteca`) en la cabecera de cada artículo renderizado.

**Motivo / criterio:** Experiencia de Usuario (UX) y navegabilidad. Proveer enlaces de retroceso contextuales reduce la fricción cognitiva, retiene al usuario en el flujo de la aplicación y fomenta la exploración de otras estanterías temáticas.

**Siguiente paso o deuda:** Empaquetar el commit atómico y proceder con la investigación para la generación de los PDFs.

### 2026-04-24 — Fix: Resolución de advertencia SEO (JSON-LD) en el índice de la Biblioteca

**Contexto:** El orquestador local (`merci-total`) reportó una advertencia (`WARN SEO_JSONLD`) indicando que el índice principal de la Biblioteca carecía de datos estructurados, lo cual penaliza el SEO técnico y rompe el estándar de la Fase 2.

**Hecho:**
- Se actualizó la función `generar_indice_biblioteca()` en `scripts/merci/merci-publish.py`.
- Se inyectó dinámicamente un bloque `<script type="application/ld+json">` utilizando el esquema `@type: CollectionPage`.

**Motivo / criterio:** Al migrar la página principal de la Biblioteca a un modelo auto-generado (SSG - Static Site Generation), el archivo HTML perdió sus metadatos estáticos originales. Reintegrar la generación del JSON-LD en el orquestador asegura el cumplimiento de la política estricta de SEO y silencia la advertencia del linter local de manera definitiva.

**Siguiente paso o deuda:** Empaquetar el commit atómico y proceder con la investigación para la generación de los PDFs.

### 2026-04-24 — Feat: Patrón "Stretched Link" en tarjetas de Biblioteca

**Contexto:** En el índice autogenerado de la Biblioteca, solo el texto del título era interactivo. Se requería que toda la superficie de la tarjeta (`.card`) fuera clicable para mejorar la experiencia de usuario (UX) sin ensuciar la semántica HTML5.

**Hecho:**
- Se añadió `position: relative;` al bloque base `.card` en `src/scss/components/_card.scss`.
- Se implementó el pseudoelemento `::after` con `inset: 0;` en el enlace del título (`.card__title a`).
- Se vinculó el cambio de color (`:hover`) del título al estado hover de la tarjeta completa.

**Motivo / criterio:** Semántica y Accesibilidad. Envolver bloques enteros (`<article>`, `<header>`, `<p>`) dentro de una etiqueta `<a>` es válido en HTML5, pero entorpece a los lectores de pantalla. El patrón *Stretched Link* (Enlace Estirado) expande el área clicable del título principal mediante CSS para cubrir su contenedor, manteniendo un DOM limpio, ligero y 100% accesible.

**Siguiente paso o deuda:** Empaquetar el commit atómico y proceder a la investigación para la generación de los PDFs.

### 2026-04-24 — Refactor: Reestructuración temática del índice de Biblioteca (Estanterías)

**Contexto:** La generación del sitio estático para la Biblioteca (`merci-publish.py`) organizaba el contenido cronológicamente (como un blog). Esto violaba la filosofía fundacional de la "Biblioteca", que define el contenido como conocimiento inmutable ordenado por "estanterías" temáticas, delegando la presentación cronológica a la capa dinámica de WordPress (`/blog`).

**Hecho:**
- Se añadió el campo `tema` en el bloque de metadatos YAML de todas las publicaciones de la biblioteca.
- Se refactorizó la función `generar_indice_biblioteca()` en `merci-publish.py` para agrupar los artículos por tema (diccionarios) y renderizarlos en secciones separadas (`<section>`).

**Motivo / criterio:** Arquitectura de la Información y Gestión del Conocimiento. Separar la estructura mental del usuario. El Blog es un flujo temporal (novedades, anuncios); la Biblioteca es un índice de consulta directa agrupado semánticamente (Arquitectura, DevSecOps, SASS).

**Siguiente paso o deuda:** Empaquetar el cambio en un commit atómico y proceder a la investigación para la generación de los PDFs.

### 2026-04-24 — Feat: Auto-generación del índice de la Biblioteca (SSG)

**Contexto:** Se generaban las publicaciones individuales en HTML, pero la página principal de la Biblioteca (`public/biblioteca/index.html`) no existía o no enlazaba dinámicamente el nuevo contenido, obligando a añadir los enlaces manualmente.

**Hecho:**
- Se refactorizó `scripts/merci/merci-publish.py` para recolectar los metadatos de las publicaciones procesadas.
- Se implementó la función `generar_indice_biblioteca()` para compilar automáticamente el `index.html` con una cuadrícula de tarjetas ordenadas por fecha descendente.

**Motivo / criterio:** Fricción Cero y SSG (Static Site Generation - Generación de Sitios Estáticos). Automatizar la creación del índice elimina la necesidad de editar HTML manualmente, protegiendo el diseño y evitando el error humano de publicar un artículo y olvidar enlazarlo.

**Siguiente paso o deuda:** Empaquetar el commit atómico y proceder a la investigación sobre generación de PDFs.

### 2026-04-24 — Fix: Resolución de auditoría SEO en orquestador de publicación

**Contexto:** El orquestador maestro (`merci-total`) abortó el pipeline al detectar que las páginas HTML generadas por `merci-publish.py` carecían de etiquetas SEO obligatorias (meta descripción, URL canónica y JSON-LD), lo cual habría provocado penalizaciones en buscadores.

**Hecho:**
- Se añadió el atributo `descripcion` en el YAML Frontmatter de los archivos Markdown de la biblioteca.
- Se actualizó `scripts/merci/merci-publish.py` para leer dicha descripción y generar dinámicamente las etiquetas `<meta>`, `<link rel="canonical">` y el bloque `<script type="application/ld+json">`.
- Se superó exitosamente la auditoría estricta de `merci-audit.py` logrando 0 errores y 0 advertencias.

**Detalle técnico:** La inyección de metadatos se realiza directamente en el orquestador de Python usando *f-strings*. El esquema de datos estructurados (JSON-LD) se configura con el `@type` `Article`, nutriéndose de los mismos metadatos del YAML para evitar que el desarrollador introduzca información redundante de forma manual.

**Motivo / criterio:** Shift-Left SEO y validación cruzada. El pipeline ha demostrado su valor al actuar como barrera protectora estricta. Solventar este error a nivel de orquestador asegura automáticamente las mejores prácticas de SEO para cualquier futuro artículo publicado.

**Siguiente paso o deuda:** Empaquetar el commit atómico y proceder a la fase de generación automática de artefactos descargables (PDF).

### 2026-04-24 — Fix: Retrocompatibilidad YAML y refinamiento tipográfico SASS

**Contexto:** Durante la ejecución del orquestador de publicación (`merci-publish`), el archivo `auditoria-rendimiento.md` (heredado de la Fase 6) fue bloqueado por carecer de metadatos YAML. Además, el HTML generado a partir de Markdown presentaba una densidad visual alta, requiriendo mayor espaciado entre capítulos para mejorar la legibilidad.

**Hecho:**
- Se inyectó el bloque estandarizado YAML Frontmatter en `auditoria-rendimiento.md`.
- Se añadieron reglas de espaciado (`margin-top`, `margin-bottom`) específicas para encabezados (`h2`, `h3`) y párrafos generados dinámicamente dentro de `.card__content` en la arquitectura SASS.
- Se validó la generación e integración exitosa de ambas publicaciones en el núcleo estático.

**Motivo / criterio:** La política de "Fail-Fast" del orquestador protege el entorno de producción al rechazar archivos malformados, obligando a actualizar la deuda técnica documental. La encapsulación de estilos de Markdown dentro de `.card__content` mantiene el SASS global limpio (Separation of Concerns).

**Siguiente paso o deuda:** Empaquetar el commit atómico e investigar la generación automatizada de artefactos PDF para la biblioteca.

### 2026-04-24 — Feat: Orquestador de publicación estática y abstracción de UI

**Contexto:** Se necesitaba un sistema para transformar los documentos Markdown curados de la biblioteca en páginas HTML estáticas, pero sin duplicar el código del menú (header) y el pie de página (footer) de la web. Además, el script reportó un fallo al intentar procesar archivos heredados (`auditoria-rendimiento.md`) que carecían de metadatos.

**Hecho:**
- Se creó `scripts/merci/merci-publish.py` para parsear Markdown con YAML Frontmatter.
- Se implementó un sistema de extracción dinámica mediante expresiones regulares que lee `public/index.html` para recortar y reutilizar las etiquetas `<header>` y `<footer>`.
- Se validó el "fail-fast" del script frente a archivos sin YAML válido.

**Motivo / criterio:** Single Source of Truth (Única Fuente de Verdad). En lugar de crear motores de plantillas complejos, el script extrae los componentes globales directamente del HTML compilado de la portada. Esto garantiza que cualquier cambio futuro en el menú de la web se propague automáticamente a las publicaciones sin tocar Python. El rechazo de archivos antiguos sin YAML protege el entorno de producción de documentos malformados.

### 2026-04-24 — Docs: Refactorización a MVP de cuadernillo con YAML Frontmatter

**Contexto:** El borrador sobre el problema de los alias y el autodescubrimiento en Python contenía volcados de consola sin procesar. Se requería estructurarlo como un "Producto Mínimo Viable" (MVP) para la biblioteca y añadir el descubrimiento sobre la retención de alias fantasma en la memoria RAM de la terminal.

**Hecho:**
- Se refactorizó `biblioteca/cuadernillo-alias-absolutos.md` eliminando el historial de consola residual.
- Se inyectaron metadatos estructurales (YAML Frontmatter) y se consolidó el contenido bajo el formato de 5 átomos (Contexto, Hecho, Detalle técnico, Motivo, Fuentes).
- Se añadió la nota de depuración sobre purga de RAM mediante `unalias`.

**Motivo / criterio:** Estandarización de la información. Para que el futuro orquestador de publicación (Fase 7.1) automatice la maquetación a HTML/PDF sin fricción, los archivos Markdown deben poseer una estructura de metadatos estricta y predecible.

**Siguiente paso o deuda:** Diseñar e implementar el script maestro de publicación automatizada (`merci-publish.py`).

### 2026-04-24 — Fix: Exclusión de enlace simbólico del CMS en control de versiones

**Contexto:** El enlace simbólico `public/blog` (que conecta el núcleo estático con la instalación aislada de WordPress) corría el riesgo de ser rastreado por Git. Versionar un enlace simbólico que apunta a una ruta absoluta del sistema anfitrión rompe la portabilidad del proyecto al clonarlo en entornos con topologías diferentes.

**Hecho:**
- Se añadió `public/blog` al archivo `.gitignore`.
- Se definió la ejecución de `git rm --cached public/blog` para eliminar el rastro del índice de Git sin destruir el enlace físico en el servidor local.

**Motivo / criterio:** Portabilidad y aislamiento (Shift-Left). El código fuente debe ser universal y agnóstico a la infraestructura. Los enlaces simbólicos son configuraciones exclusivas del servidor (estado) y, al igual que la base de datos o el archivo `wp-config.php`, nunca deben viajar a través del control de versiones.

**Siguiente paso o deuda:** Ejecutar la limpieza del caché de Git, revisar el estado del árbol y realizar el commit de saneamiento mediante `merci-commit.py`.

### 2026-04-24 — Milestone: Bifurcación arquitectónica (Merci Boilerplate vs mercedev.es)

**Contexto:** Tras alcanzar la madurez técnica absoluta (100/100) y purgar la deuda técnica al cierre de la Fase 6, se determinó que las Fases 1-6 conforman un motor de infraestructura agnóstico (DevSecOps, SASS, CSP, Híbrido WP), mientras que la Fase 7 (publicación automatizada, biblioteca) contiene la lógica de negocio específica del proyecto.

**Hecho:**
- Se aprueba la bifurcación (Fork) del proyecto actual en dos entidades separadas.
- Se decide extraer el estado actual del código hacia un nuevo repositorio plantilla (`merci-boilerplate`) abstrayendo los datos personales.
- El repositorio actual (`PROYECTO_mercedev.es`) transiciona oficialmente para convertirse en el primer producto real derivado de dicha plantilla.

**Detalle técnico:** La extracción al nuevo Boilerplate implicará limpiar el `index.html` de textos específicos, establecer un logotipo neutral y sustituir las rutas absolutas por variables (`{{DOMINIO}}`). El repositorio actual mantendrá el historial completo de Git y avanzará hacia la Fase 7 asumiendo su rol de "instancia cliente".

**Motivo / criterio:** Principio de Separación de Responsabilidades (Separation of Concerns). Un *boilerplate* o *framework* no debe contener reglas de negocio ni contenido específico de una marca. Congelar el motor base ahora protege su reusabilidad para futuros proyectos, aislando el desarrollo de la Fase 7 exclusivamente en el producto final.

**Siguiente paso o deuda:** Ejecutar manualmente la copia y abstracción de la carpeta hacia el nuevo repositorio "Merci Boilerplate" e iniciar el diseño de la Fase 7 en el repositorio actual.

### 2026-04-24 — Refactor: Micro-optimización de SEO Técnico (JSON-LD Contextual)

**Contexto:** Una auditoría SEO de "hilado fino" detectó que el esquema JSON-LD inyectado dinámicamente marcaba todas las rutas de WordPress como `@type: WebSite` y usaba `home_url()` (que resuelve a `/blog`), lo cual generaba riesgo de fragmentación de la autoridad de dominio en los motores de búsqueda.

**Hecho:**
- Se refactorizó la matriz `$json_ld` dentro de la función `merci_inyectar_metadatos_seo` en `functions.php`.
- Se implementó condicionalidad semántica (`is_singular()`) para emitir `@type: Article` en páginas de lectura.
- Se forzó el uso de la raíz absoluta del dominio para el esquema `WebSite`.

**Detalle técnico:** Se extrajo la variable `$domain_root` usando la misma expresión regular (`preg_replace`) que en el enlazador de assets. Dependiendo del contexto de la vista, el JSON-LD ahora escupe los datos específicos del post actual (`get_permalink()`, `get_the_title()`) o los datos base del índice, cumpliendo con la especificación estricta de `schema.org`.

**Motivo / criterio:** Consultoría SEO Avanzada. Evitar la canibalización de entidades (que Google interprete `/blog` como un sitio web independiente a la portada). Etiquetar correctamente los posts como "Artículos" habilita la aparición en fragmentos enriquecidos (Rich Snippets).

**Siguiente paso o deuda:** Iniciar el diseño del flujo de la Fase 7.1 (Automatización de publicación).

### 2026-04-24 — Refactor: Auditoría arquitectónica externa y purga de deuda técnica

**Contexto:** Una auditoría externa de código mediante inteligencia artificial detectó cuatro deudas técnicas críticas en el ecosistema: un antipatrón de rendimiento en WordPress, uso de código heredado (legacy), inconsistencia SEO entre frontales y la violación del paradigma de programación orientada a objetos en JavaScript.

**Hecho:**
- Se modificó el hook de aprovisionamiento de base de datos de `init` a `after_switch_theme` en `functions.php`.
- Se eliminó la etiqueta `<title>` deprecada explícita en `index.php` y se activó `add_theme_support('title-tag')`.
- Se inyectó un bloque mínimo de metadatos estructurados (JSON-LD) en el ecosistema dinámico de WordPress.
- Se refactorizó `public/js/main.js` encapsulando la lógica procedimental en la clase `NavigationController`.

**Detalle técnico:** El hook `init` provocaba consultas inútiles a la base de datos en cada petición HTTP (N+1 query problem). La función `wp_title()` está deprecada desde WP 4.4; delegar el título al núcleo limpia el archivo HTML y cumple el estándar moderno. La refactorización a Vanilla JS con paradigma POO (Programación Orientada a Objetos) aísla el comportamiento del menú cumpliendo el Principio de Responsabilidad Única (SOLID).

**Motivo / criterio:** Prácticas estrictas de *Quality Assurance* (QA - Aseguramiento de Calidad) y validación cruzada. El código no solo debe funcionar, sino que debe alinearse perfectamente con la filosofía fundacional del proyecto (rendimiento, arquitectura y cero deuda técnica), sin admitir tolerancias al código "suficientemente bueno".

**Siguiente paso o deuda:** Ejecutar el orquestador de validación y comprometer el código para iniciar la Fase 7.1 (Automatización de publicación).

### 2026-04-23 — Fix: Actualización mayor de Pillow a 12.2.0 (Dependabot)

**Contexto:** Dependabot emitió nuevas alertas y forzó la actualización de su rama (pull request) indicando la necesidad de dar un salto mayor en la versión de `Pillow` hasta la `12.2.0` para mitigar vulnerabilidades encadenadas.

**Hecho:**
- Se actualizó la dependencia en `requirements.txt` de `Pillow==10.4.0` a `Pillow==12.2.0`.

**Detalle técnico:** El salto a una versión mayor (de 10.x a 12.x) incluye importantes parches de seguridad. Dado que `merci-optimizer.py` solo utiliza funciones estándar y consolidadas de apertura, redimensionado y guardado en WebP, la actualización se considera segura y no introduce alteraciones lógicas (*breaking changes*) en la automatización del proyecto.

**Motivo / criterio:** Mantenimiento proactivo y "Zero Trust". Las alertas de seguridad se persiguen hasta su erradicación total. Dar el salto a la última versión estable recomendada por GitHub blinda el entorno local y silencia el ruido operativo en el repositorio.

**Siguiente paso o deuda:** Realizar el push para cerrar definitivamente los hilos de Dependabot e iniciar el diseño del flujo de la Fase 7.

### 2026-04-23 — Fix: Actualización crítica de Pillow a 10.4.0 (Dependabot)

**Contexto:** Tras el último `git push`, GitHub Dependabot reportó dos nuevas vulnerabilidades de severidad alta. Dado que `requirements.txt` solo contiene la dependencia `Pillow`, se deduce que la versión 10.3.0 seguía expuesta a CVEs recientes.

**Hecho:**
- Se actualizó la dependencia en `requirements.txt` de `Pillow==10.3.0` a `Pillow==10.4.0`.
- Se revisó la integridad y sincronización de toda la documentación del directorio `docs/` y el `README.md` confirmando el cierre inmaculado de la Fase 6.

**Detalle técnico:** Las vulnerabilidades descubiertas en procesamiento de imágenes en las versiones anteriores a la 10.4.0 de Pillow pueden permitir ataques o denegación de servicio. Fijar la versión a `10.4.0` parchea estos vectores. La documentación arquitectónica (`docs/`) ha sido validada y refleja el estado exacto de producción (incluyendo el hash CSP y el enrutamiento).

**Motivo / criterio:** La seguridad perimetral no es negociable. En DevSecOps, mantener las dependencias de Python actualizadas es obligatorio, incluso si el script que las usa (`merci-optimizer.py`) se ejecuta únicamente en el entorno local.

**Siguiente paso o deuda:** Desplegar el cambio y comenzar el diseño del script de publicación automatizada (Fase 7.1).

### 2026-04-23 — Fix: Resolución de vulnerabilidad (Dependabot) y sincronización documental

**Contexto:** Al realizar el `git push` de cierre de la Fase 6, GitHub Dependabot reportó una vulnerabilidad de severidad alta (CVE) en las dependencias del proyecto. Además, era necesario alinear los manuales de despliegue (`docs/`) con las últimas configuraciones de seguridad en Nginx (CSP, HSTS) antes de avanzar a la Fase 7.

**Hecho:**
- Se identificó que la librería `Pillow` anclada en `requirements.txt` poseía una vulnerabilidad conocida, por lo que se actualizó a la versión segura `10.3.0`.
- Se actualizaron los manuales `docs/deployment-playbook.md` y `docs/integracion-wordpress.md` para incluir el bloque de Hardening de cabeceras HTTP inyectado en CloudPanel.

**Detalle técnico:** En arquitecturas DevSecOps, las dependencias de Python (utilizadas por `merci-optimizer.py`) deben ser auditadas continuamente. Actualizar la versión estricta en `requirements.txt` soluciona la alerta de GitHub manteniendo la reproducibilidad. Por otro lado, la documentación arquitectónica se sincronizó para reflejar la inyección de la cabecera `Content-Security-Policy` con el *whitelist* criptográfico (Hash SHA-256) y el `preload` de HSTS en el VHost del puerto 8080.

**Motivo / criterio:** Tolerancia cero frente a deuda técnica y brechas de seguridad. Una vulnerabilidad "High", aunque afecte solo al entorno local de automatización, rompe la confianza en el repositorio. Mantener la documentación sincronizada con la realidad del servidor garantiza la reproducibilidad (Infrastructure as Code).

**Siguiente paso o deuda:** Iniciar la Fase 7: Automatización y Clasificación.

---

## Cuando pases esto a la biblioteca

1. **Releer** entradas y quitar ruido (intentos fallidos, datos personales, tokens aunque sean falsos).
2. **Partir por tema:** por ejemplo una ficha “Sistema Merci — auditoría pre-commit” vs “Estructura del repositorio”.
3. **Añadir los tres átomos** donde haya una decisión difícil o un incidente (síntoma, solución, lección o deuda).
4. **Enlazar** al código estable (rutas a `scripts/merci/`, no copiar bloques enormes en la biblioteca salvo que aporten lectura autónoma).

---

*Última revisión de la bitácora: 2026-04-14.*
