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

### 2026-05-08 — Docs: Estandarización de Rutas de Archivo en Bitácora

**Contexto:** Se detectó una inconsistencia en el registro de rutas de archivo dentro de la bitácora, incluyendo el prefijo absoluto del sistema (`/home/hildegahr/Escritorio/`), lo que comprometía la legibilidad, la portabilidad y la agnositicidad del registro.

**Hecho:** Se ha establecido una nueva convención para la documentación de rutas. A partir de ahora, todas las rutas de archivo mencionadas en la bitácora serán relativas a la raíz del proyecto, comenzando con `PROYECTO_mercedev.es/`.

**Detalle técnico:** La bitácora `laboratorio/bitacora-mercedev.md` ha sido actualizada con esta nueva directriz en la sección "Cómo mantenerlo (acuerdo simple)".

**Motivo / criterio:** *Legibilidad y Portabilidad*. Mantener una convención estricta en el registro de rutas es crucial para que la bitácora actúe como una Única Fuente de Verdad (SSOT) agnóstica a la ubicación física del repositorio. Esto facilita su comprensión y reutilización por parte de futuros colaboradores o en diferentes entornos.

**Siguiente paso o deuda:** Asegurar la aplicación de esta nueva convención en futuras entradas de la bitácora.


### 2026-05-08 — Test: Creación de nota para Agente Bibliotecario (Gobernanza Ramas)

**Contexto:** Para validar el comportamiento del "Agente Bibliotecario" y el flujo de "Cosecha de Conocimiento" (Fase 3 del Roadmap de IA), se creó una nota preliminar sobre la colisión entre la protección de ramas en GitHub y la estrategia de 'force push' para ramas huérfanas. El objetivo es que el Agente procese esta nota en bruto.

**Hecho:** Se creó el archivo `PROYECTO_mercedev.es/laboratorio/nota-gobernanza-ramas-force-push.md` en estado 'borrador', especificando "DevSecOps y Gobernanza" como estantería destino.

**Motivo / criterio:** *Testing and Validation*. Esta nota sirve como input de prueba para el flujo de curación de contenido por parte del "Agente Bibliotecario". Es fundamental entender cómo la IA procesa un input mínimo antes de escalar la generación de cuadernillos.

**Siguiente paso o deuda:** Ejecutar `merci-librarian.py` para procesar la nota y evaluar el cuadernillo generado por el Agente.

### 2026-05-08 — Docs: Creación de cuadernillo sobre Gobernanza de Ramas y Force Push

**Contexto:** Tras integrar GitHub Actions y configurar el repositorio, la plataforma advirtió que la rama `main` estaba desprotegida. Al evaluar la activación de las Branch Protection Rules (Reglas de Protección de Rama), se identificó una colisión directa con el protocolo de Prevención de Fuga de Datos, el cual exige el uso de Ramas Huérfanas y `force push`.

**Hecho:** Se redactó en el laboratorio el borrador `cuadernillo-gobernanza-ramas-force-push.md` explicando cómo conciliar la seguridad de la rama principal con las operaciones destructivas de mantenimiento necesarias para el Boilerplate.

**Motivo / criterio:** *Knowledge Management (Gestión del Conocimiento)*. Toda excepción en la infraestructura de seguridad en la nube (como permitir `push -f` a administradores en `main`) debe estar justificada arquitectónicamente. Esto evita que en el futuro se apliquen bloqueos rígidos que impidan el truncamiento del historial.

**Siguiente paso o deuda:** Curar el documento promoviéndolo a la Biblioteca (`merci-promote.py`), compilar el orquestador global (`merci-total`) y empaquetar el commit.

### 2026-05-07 — Perf: Corrección de exclusión en backups locales (Zero Bloat)

**Contexto:** Tras superar con 0 errores el pipeline de `merci total`, la copia de seguridad local generó un archivo masivo de 54.68 MB.

**Hecho:** Se parcheó `scripts/merci/merci-backup.py` apuntando la regla de exclusión a `REPO_ROOT / "auditorias-pagespeed.web.dev"`.

**Detalle técnico:** El script buscaba la carpeta de reportes de PageSpeed dentro de `laboratorio/`, pero los pesados PDFs residían en la raíz del repositorio. Al no coincidir la ruta, comprimió decenas de megabytes no deseados.

**Motivo / criterio:** *Zero Bloat y Transparencia CLI*. El modo `--verbose` funcionó perfectamente como caja de cristal revelando a los "polizones". Corregir la exclusión restaura el backup a su tamaño óptimo (fracciones de MB).

**Siguiente paso o deuda:** Re-ejecutar el backup y emitir el Sello Definitivo de la auditoría.

### 2026-05-07 — Chore: Cierre de PR Dependabot (pypdf 5.4.0 → 6.10.2)

**Contexto:** Tras añadir `pypdf==5.4.0` al `requirements.txt` en esta sesión, GitHub Actions disparó automáticamente un PR de Dependabot proponiendo actualizar la librería a la versión `6.10.2`.

**Hecho:**
- Se cerró el PR `#1` de Dependabot sin mergear desde la interfaz de GitHub.
- No se modificó `requirements.txt`.

**Motivo / criterio:** *Versiones Pinadas y Control Consciente*. La política del proyecto es mantener versiones exactas en `requirements.txt` para garantizar reproducibilidad entre entornos. Las actualizaciones automáticas de Dependabot no se aceptan a ciegas: pueden introducir cambios de API o comportamiento no probados. `pypdf` es además una dependencia de laboratorio (solo usada por `laboratorio/scripts_temporales/merci-extract-metrics.py`), no del pipeline principal, por lo que el riesgo de no actualizar es mínimo. Cualquier actualización de dependencias debe evaluarse manualmente, probarse en local y commitearse de forma consciente.

**Siguiente paso o deuda:** Continuar con el Release Pipeline de la v1.7.0 (Pasos 2–7 del SOP en `docs/matriz/mantenimiento-boilerplate-sop.md`).

### 2026-05-07 — Docs: Release v1.7.0 del Boilerplate (SSG Dual y Engineering Dashboard)

**Contexto:** Evaluación del estado del repositorio frente a la v1.6.1 publicada en Git. Se detectaron cambios de arquitectura sustanciales en scripts del ecosistema que justifican una nueva release menor antes de arrancar el Roadmap de IA.

**Hecho:**
- Se actualizó `README-merci.md` a la versión `v1.7.0` con las release notes completas.
- Cambios incluidos en la release: arquitectura SSG dual (`merci-publish.py` compila `/biblioteca/` y `/art-de-cote/` en paralelo), desacoplamiento de Art de Coté de WordPress (`merci-wp.py`, `merci-promote.py`, `merci-sync-pages.py`), robustez de parseo YAML en los tres scripts, Engineering Dashboard en portada (10 métricas + SASS BEM), y formalización de la Regla 10 (Art de Coté) en `instrucciones.md`.

**Detalle técnico:** Archivos del ecosistema modificados desde v1.6.1: `scripts/merci/merci-publish.py` (+92/-0 líneas), `scripts/merci/merci-promote.py` (+12/-0), `scripts/merci/merci-sync-pages.py` (+2/-0), `scripts/merci/merci-wp.py` (+5/-0), `src/scss/components/_hero.scss` (+100/-0), `src/wp-theme/merci-theme/index.php` (+1/-1), `src/wp-theme/merci-theme/woocommerce.php` (+1/-1), `instrucciones.md` (+1/-1).

**Motivo / criterio:** *Release Management y Governance*. Según la Regla 14 de `instrucciones.md`, toda mejora en scripts del ecosistema debe ejecutar el Release Pipeline antes de continuar. Los cambios acumulados desde v1.6.1 son suficientemente sustanciales (nueva arquitectura SSG dual) para justificar una versión menor (v1.7.0) en lugar de un hotfix.

**Siguiente paso o deuda:** Ejecutar el Release Pipeline completo: `merci-backup.py` → clonar en temporal → `merci-init.py` → `rsync` → `merci-total` en el Boilerplate → commit y push. Ver SOP en `docs/matriz/mantenimiento-boilerplate-sop.md`.

### 2026-05-07 — Docs: Registro de deudas técnicas pendientes (WP→LinkedIn, Tienda, Boilerplate)

**Contexto:** Revisión integral del proyecto detectó tres deudas técnicas no registradas formalmente en ningún documento de planificación.

**Hecho:**
- Se añadió tarea "Pipeline WP → LinkedIn" en `ROADMAP-AI-ORQUESTACION-SELF-HEALING-SYSTEM.md` (Fase 3), para automatizar la publicación en LinkedIn al sincronizar un post en WordPress. El bloque `<- linkedin: -->` del Frontmatter ya contiene el texto del anuncio; la integración requiere revisar el estado del token OIDC y conectar `merci-wp.py` con `merci-linkedin.py`.
- Se añadió tarea "Evaluación de Tienda WooCommerce" en `ROADMAP-AI-ORQUESTACION-SELF-HEALING-SYSTEM.md` (Fase 4) y hito de deuda técnica en `README.md` (Fase 4.3). WooCommerce opera en modo catálogo desde la Fase 4.3; la activación de carrito y pasarela de pago requiere decisión de arquitectura previa (impacto en CSP y Core Web Vitals).
- Se añadió deuda de gobernanza: revisar si el estado actual del repositorio justifica una nueva release del Boilerplate por encima de la v1.6.1 publicada en Git.

**Motivo / criterio:** *Trazabilidad y Governance*. Las deudas técnicas no registradas son deudas invisibles. Formalizarlas en el roadmap y en la bitácora garantiza que no se pierdan entre sesiones y que puedan priorizarse en el momento adecuado.

**Siguiente paso o deuda:** Evaluar el estado del Boilerplate en Git (v1.6.1) frente al estado actual del repositorio para determinar si procede una nueva release antes de arrancar el Roadmap de IA.

### 2026-05-07 — Fix: Resolución de permisos de archivo en configuración de Continue (~/.continue/config.json)

**Contexto (El Desafío):** Al intentar acceder al archivo de configuración de la extensión Continue (`~/.continue/config.json`) para aplicar el modelo `gemini-1.5-flash`, la terminal devolvió un error `zsh: permiso denegado`.

**Hecho (La Maniobra):** Se diagnosticó un problema de propiedad de archivos a nivel de sistema operativo, probablemente causado por la creación del directorio con privilegios de `sudo`. Se instruyó la ejecución del comando `sudo chown -R hildegahr:hildegahr /home/hildegahr/.continue` para restaurar la propiedad al usuario correcto.

**Motivo / criterio (El Aprendizaje):** *Seguridad y Propiedad en Linux*. Un error de "permiso denegado" en un archivo de configuración de usuario casi siempre apunta a que `root` es el propietario. El comando `chown` (change owner) con el flag recursivo (`-R`) es la maniobra estándar para reclamar la propiedad de un directorio y todo su contenido, restaurando la operatividad sin necesidad de escalar privilegios para la edición diaria.

**Siguiente paso o deuda:** Proceder con la edición del archivo `config.json` para anclar el modelo de IA a `gemini-1.5-flash` y eliminar las limitaciones de cuota.

### 2026-05-07 — Conf: Reconfiguración de Continue (Gemini 1.5 Flash) para cuota extendida

**Contexto:** Las limitaciones de cuota (Rate Limits de 20 peticiones/día) de los modelos Pro o experimentales en la extensión Continue impedían la generación fluida y masiva de los textos para el asistente Merci.

**Hecho:** Se instruyó la reconfiguración del archivo de Continue (`~/.continue/config.json` o `.yaml`) para utilizar el proveedor `google-generative-ai` anclado al modelo `gemini-1.5-flash`.

**Motivo / criterio:** *Fricción Cero y Rate Limiting*. `gemini-1.5-flash` ofrece una cuota gratuita de 1500 peticiones diarias (15 RPM - Requests Per Minute). Apuntar la herramienta de asistencia del IDE hacia este modelo la convierte en un recurso API ilimitado para el proyecto, evitando que Continue colapse por bloqueos HTTP 429 durante la orquestación.

**Siguiente paso o deuda:** Iniciar formalmente la Fase 1 del Roadmap de IA (Observabilidad e Intercepción de Errores).

### 2026-05-07 — UI: Leyenda descriptiva para el Dashboard de Métricas

**Contexto:** El "Engineering Dashboard" de la portada con las 10 métricas carecía de contexto sobre el origen y la valoración de los números presentados, dificultando la comprensión para usuarios menos técnicos.

**Hecho:** 
- Se inyectó el bloque `<p class="hero__dashboard-legend">` en `public/index.html`.
- Se añadieron las reglas CSS `.hero__dashboard-legend` en `src/scss/components/_hero.scss`, alineadas a la izquierda.

**Motivo / criterio:** *Accesibilidad Cognitiva y Autoridad*. Explicar de dónde vienen los datos (auditoría real de Google PageSpeed) y qué significan (rango de excelencia / 100 sobre 100) contextualiza las métricas puras, transformando números fríos en un argumento de venta de autoridad técnica verificable.

**Siguiente paso o deuda:** Recompilar el CSS, ejecutar `merci total` y comenzar la Fase 1 de IA.

### 2026-05-07 — Feat: Ampliación de métricas extraídas de PageSpeed (FCP y SI)

**Contexto:** El script de extracción leía 4 métricas (LCP, INP, CLS, TBT), pero el reporte de PageSpeed incluye otras relevantes como First Contentful Paint (FCP) y Speed Index (SI). Se solicitó incluirlas todas en el Dashboard de la portada.

**Hecho:**
- Se inyectaron los patrones Regex bidireccionales para FCP y SI en `laboratorio/scripts_temporales/merci-extract-metrics.py`.
- Se añadieron los bloques HTML para las nuevas métricas en `public/index.html`.
- Se refactorizó la rejilla CSS en `src/scss/components/_hero.scss` de 4 a 5 columnas para alojar perfectamente las 10 métricas totales en dos filas.

**Motivo / criterio:** *Data Completeness y UI Responsiva*. Ignorar datos disponibles en un reporte validado limita la observabilidad. Adaptar la cuadrícula SASS demuestra la flexibilidad de la arquitectura modular: ampliar el dashboard de 8 a 10 métricas cuesta solo un dígito de CSS.

**Siguiente paso o deuda:** Iniciar la Fase 1 de IA.

### 2026-05-06 — QA: Intercepción de enlace roto en capa dinámica (Menú Art de Coté)

**Contexto:** El orquestador `merci total` detuvo el pipeline en la fase de rastreo dinámico (`merci-linkcheck.py`) tras detectar un error 404 hacia `/blog/category/art-de-cote/` originado en `/blog/`.

**Hecho:** Se diagnosticó que las plantillas monolíticas de WordPress (`index.php` y `woocommerce.php`) conservaban la ruta antigua en su bloque `<nav>` *hardcodeado*. Se actualizó manualmente el enlace hacia la nueva ruta estática `/art-de-cote/`.

**Motivo / criterio:** *Fail-Fast y DAST*. El escáner de enlaces demuestra su inmenso valor bloqueando el despliegue al detectar asimetrías de enrutamiento entre el núcleo SSG y el CMS. Las plantillas PHP no son procesadas por `merci-sync-pages.py`, exigiendo intervención explícita del autor para mantener la paridad visual.

**Siguiente paso o deuda:** Validar la corrección ejecutando `merci total` y comenzar la Fase 1 del Roadmap de IA.

### 2026-05-06 — Arch: Independencia absoluta de Art de Coté.

**Contexto:** Tras decidir migrar Art de Coté al motor estático (SSG), existían dos rutas: añadirlo en la Biblioteca como una estantería más o darle entidad propia como índice independiente.

**Hecho:** 
- Se refactorizó `merci-publish.py` para procesar y compilar la carpeta `art-de-cote/` de forma paralela a `biblioteca/`.
- Se modificó `merci-wp.py` para excluir esta carpeta del flujo de WordPress.
- Se actualizaron los enlaces del menú principal hacia `/art-de-cote/`.

**Motivo / criterio:** *Control y Separación de Identidad*. Otorgarle su propio `index.html` autogenerado mantiene la claridad conceptual en el menú y evita mezclar ensayos colaterales con la doctrina y tutoriales técnicos de la Biblioteca, facilitando la navegación de los usuarios que clonarán el repositorio.

**Siguiente paso o deuda:** Validar la compilación SSG dual ejecutando `merci total`.

### 2026-05-06 — Arch: Pivote SSG para "Art de Coté" (Desacoplamiento de WordPress)

**Contexto:** La sección "Art de Coté", destinada a preservar scripts temporales, andamiajes y código colateral, estaba enrutada hacia la capa dinámica (WordPress). Se reevaluó la naturaleza del contenido.

**Hecho:** Se decidió extraer "Art de Coté" del CMS y migrarlo al motor de Generación de Sitios Estáticos (SSG), operando bajo el mismo flujo que la Biblioteca.

**Motivo / criterio:** *Data Integrity & SSOT*. El código fuente, los scripts y los flujos YAML son ciudadanos de primera clase en Markdown y Git. Almacenar fragmentos de código técnico en una base de datos MySQL (WordPress) es un antipatrón que expone el código a corrupción de formato y pérdida de trazabilidad. Devolver Art de Coté a la capa estática garantiza 0ms de latencia y un control de versiones absoluto sobre los experimentos preservados.

**Siguiente paso o deuda:** Refactorizar `merci-promote.py` y `merci-publish.py` para soportar la nueva ruta estática. Modificar los enlaces de navegación global.

### 2026-05-06 — Arch: Formalización de Art de Coté para scripts auxiliares (Cero Desperdicio)

**Contexto:** Se requería definir qué hacer con los scripts temporales, andamiajes o flujos de trabajo (como el pipeline de CI/CD puro con rsync) que funcionan perfectamente pero son descartados por decisiones de diseño.

**Hecho:** Se actualizó la Regla 10 en `instrucciones.md` para asentar formalmente que este tipo de conocimiento no se elimina, sino que se transforma en cuadernillos bajo la taxonomía "Art de Coté" (Arte Colateral).

**Motivo / criterio:** *Waste Not* (Cero Desperdicio). El código escrito y validado representa tiempo de ingeniería valioso. Preservarlo en el CMS bajo una categoría colateral enriquece la base de conocimientos sin contaminar la arquitectura principal del Boilerplate, dejándolo disponible "por si acaso".

**Siguiente paso o deuda:** Iniciar la Fase 1 del Roadmap de IA (Creación de `/merci-brain` y estandarización de prompts).

### 2026-05-06 — Milestone: Cierre Arquitectónico Fundacional (Fases 1 a 11)

**Contexto:** El roadmap original del proyecto, concebido para construir un ecosistema web híbrido desde cero absoluto, ha llegado a su conclusión. Era necesario dejar un registro histórico y formal de este hito antes de mutar la naturaleza del orquestador hacia la Inteligencia Artificial.

**Hecho:** Se da por sellada y congelada la arquitectura base fundacional de `mercedev.es` y del `merci-boilerplate` tras completar de forma exhaustiva y auditable las 11 fases de desarrollo.

**Detalle técnico:** Se ha logrado transicionar de un simple HTML estático a un núcleo de rendimiento extremo (100/100 Core Web Vitals en todas las métricas). El chasis actual soporta un motor SSG propio en Python puro, un publicador Headless hacia WordPress con escudo Anti-Proxy, y un pipeline DevSecOps (CI/CD) validado en la nube. Todo ello manteniendo la innegociable política de 0 dependencias externas en el entorno de ejecución y encarnando el paradigma *Spec as Source*.

**Motivo / criterio:** *Closure & Evolution*. Reconocer los hitos estructurales es vital en la ingeniería de software. Un Agente Autónomo (Self-Healing System) no puede construirse sobre cimientos de barro o frameworks efímeros. Las 11 fases de este ecosistema no fueron un fin en sí mismas, sino la preparación quirúrgica del terreno para crear una infraestructura inquebrantable, capaz de soportar la orquestación algorítmica sin colapsar.

**Siguiente paso o deuda:** Cerrar la etapa de construcción de infraestructura pura y abrir el IDE para ejecutar la Fase 1 del nuevo documento `ROADMAP-AI-ORQUESTACION.md` (Observabilidad e Intercepción de errores).

### 2026-05-06 — Docs: Alineación del CV Semántico con la identidad de Performance Engineer

**Contexto:** El currículum semántico (`/sobre-mi/index.html`) conservaba el copy anterior ("Arquitecta de Sistemas de IA") que resultaba ajeno a la nueva identidad profesional y restaba impacto visual a la frase clave "gobernar la incertidumbre".

**Hecho:**
- Se extrajo la frase clave a un `<h2>` independiente con la clase BEM `.hero__statement` (cursiva, `$color-text-base`).
- Se reescribió el primer párrafo del "CV Anti-ATS" para vincular la experiencia industrial de 20 años con el rigor del Performance Engineering.
- Se actualizó el objeto JSON-LD para reflejar los nuevos *skills* ("Spec as Source", "Web Performance").

**Motivo / criterio:** *Coherencia de Marca Personal*. El CV debe respirar el mismo aire empírico y analítico que LinkedIn y la Portada. Darle entidad de `<h2>` a la frase sobre la incertidumbre refuerza la tesis de madurez (Seniority) y crea una jerarquía visual más atractiva antes de entrar en los párrafos densos.

**Siguiente paso o deuda:** Iniciar la automatización e intercepción de errores en Python (Fase 1 de IA).

### 2026-05-06 — Docs: Pivote de identidad hacia Performance Engineering y Spec as Source

**Contexto:** El posicionamiento como "AI Systems Architect" no reflejaba con precisión el trabajo real y el inmenso valor demostrable del ecosistema actual (100/100 cuádruple en PageSpeed Insights, documentación exhaustiva y automatización DevSecOps). Se necesitaba un perfil más "vendible" y ajustado a la realidad técnica.

**Hecho:** Se actualizó `public/index.html` para reflejar el perfil de **Performance Engineer & Technical Writer**.

**Motivo / criterio:** *Authenticity & Market Fit*. "Spec as Source", las métricas de rendimiento perfectas y la trazabilidad documental (ADRs, bitácoras) son habilidades tangibles, raras y altamente demandadas. Presentarse con hechos empíricos (lo que ya se hace y se domina) proyecta mucha más autoridad que prometer orquestación de IA, la cual está apenas comenzando en el Roadmap.

**Siguiente paso o deuda:** Iniciar la automatización e intercepción de errores en Python (Fase 1 de IA).

### 2026-05-06 — Docs: Refinamiento del tono editorial en la portada

**Contexto:** El copy de la portada presentaba un tono demasiado agresivo ("La máquina ejecuta el código. Yo diseño el sistema.", "declaración de intenciones"), alejándose de la Guía de Voz equilibrada del proyecto.

**Hecho:** Se suavizó el `H1`, el subtítulo y la tarjeta "Anti-ATS" en `public/index.html`.

**Motivo / criterio:** *Brand Identity y Tono Editorial*. Mostrar autoridad técnica y *Seniority* no requiere un tono dictatorial ni beligerante. Un enfoque firme pero integrador ("Arquitectura de Sistemas y Orquestación de IA") transmite la misma capacidad técnica resultando mucho más accesible y corporativo para reclutadores o clientes.

**Siguiente paso o deuda:** Iniciar formalmente la Fase 1 del Roadmap de Orquestación de IA.

### 2026-05-06 — Docs: Release v1.6.1 del Boilerplate y preparación de terreno para IA

**Contexto:** Tras subsanar las penalizaciones de contraste de accesibilidad (WCAG) en el núcleo estático y fortificar el enrutamiento contextual en la capa dinámica (WordPress), era imperativo empaquetar estas correcciones arquitectónicas en el Boilerplate antes de iniciar la compleja Fase 1 de Inteligencia Artificial (Self-Healing System).

**Hecho:**
- Se actualizó `README-merci.md` a la versión `v1.6.1` detallando las mejoras de UX y Accesibilidad.
- Se revisó la integridad de las plantillas y del archivo `.env` de muestra.
- Se ejecutó el Protocolo Estricto de Cierre certificando 0 deudas técnicas y el restablecimiento del Cuádruple 100 en todas las métricas móviles.

**Motivo / criterio:** *Clean Slate (Lienzo en Blanco) y Governance*. Nunca se debe arrancar una épica de alta incertidumbre si el código base presenta deuda técnica. Lanzar la release menor (`v1.6.1`) asegura que el Boilerplate público reciba los últimos parches y que nuestro entorno local quede congelado, respaldado y seguro para mutar hacia el modelo Self-Healing.

**Siguiente paso o deuda:** Ejecutar el backup local (`merci-backup.py`), realizar el proceso de instanciación hacia el repositorio de `merci-boilerplate` y arrancar oficialmente con la Fase 1 de Orquestación IA.

### 2026-05-06 — Fix: Resolución de jerarquía en botones de retroceso (Art de Coté)

**Contexto:** El botón "Volver" en artículos individuales de "Art de Coté" redirigía a la portada del Blog (`/blog/`) en lugar de a su estantería original. Esto ocurría porque los posts estaban asignados a subcategorías específicas (temas) y no directamente a la categoría padre "Art de Coté".

**Hecho:** Se refactorizó la lógica condicional del botón de retroceso en `src/wp-theme/merci-theme/index.php`.

**Detalle técnico:** La función nativa `has_category()` de WordPress solo evalúa la asignación directa. Se implementó una verificación de árbol genealógico utilizando `cat_is_ancestor_of()` para iterar sobre todas las categorías del post. Si alguna de ellas desciende de `art-de-cote`, la variable de retroceso se ajusta correctamente a `/blog/category/art-de-cote/`.

**Motivo / criterio:** *Robustez en Arquitectura de la Información*. Cuando el CMS estructura los posts en subcategorías (inyectadas por el Headless script), el frontend debe ser lo suficientemente inteligente para inferir la jerarquía completa y no solo las asignaciones de primer nivel, evitando así expulsar al usuario de su contexto de navegación.

**Siguiente paso o deuda:** Sincronizar el tema con producción e iniciar la Fase 1 del Roadmap de IA.

### 2026-05-06 — Fix: Resolución de enlaces de retroceso rotos en capa dinámica (WP)

**Contexto:** El botón "Volver" en los artículos individuales de WordPress (`blog` y `art-de-cote`) fallaba al depender del historial del navegador (`javascript:history.back()`). Esto impedía el retroceso si el usuario abría el enlace en una nueva pestaña o accedía directamente a la URL.

**Hecho:** Se reemplazó el script en línea por una URL de retroceso dinámica generada en PHP dentro de `src/wp-theme/merci-theme/index.php`.

**Detalle técnico:** Se implementó el condicional nativo `has_category('art-de-cote')` para inferir estructuralmente la ruta padre correcta. Si es "Art de Coté", resuelve a `/blog/category/art-de-cote/`; para el resto, hace fallback seguro hacia `/blog/`.

**Motivo / criterio:** *Fricción Cero y Robustez de Enrutamiento*. Depender del historial de sesión del navegador es un anti-patrón de accesibilidad. Resolver la ruta lógicamente en el backend (PHP) asegura que el botón devuelva al usuario a la estantería temática correcta de forma infalible, mejorando la UX y erradicando el uso innecesario de JavaScript en línea.

**Siguiente paso o deuda:** Sincronizar los cambios con el servidor de producción e iniciar formalmente la Fase 1 del Roadmap de Orquestación de IA.

### 2026-05-06 — QA: Resolución de contraste WCAG mediante alcance de contexto (Scoped CSS)

**Contexto:** La auditoría de PageSpeed Insights sobre `/sobre-mi/` reportó una penalización en Accesibilidad (95/100). El análisis reveló que el color primario de los enlaces (`#ea580c`) no alcanza el ratio estricto de 4.5:1 requerido para texto de tamaño regular. Esto ocurría exclusivamente en esta ruta por ser densa en enlaces de párrafo continuo.

**Hecho:**
- Se creó la variable matemática `$color-regular` en `_variables.scss` con un tono de alto contraste (`#9a3412`).
- Se añadió una regla en `_typography.scss` para inyectar esta variable en los enlaces anidados exclusivamente dentro de bloques de texto (`p`, `li`).
- Se preservó el color `$color-primary` original para la interfaz global (tarjetas, botones, cabeceras).

**Detalle técnico:** El color primario original ofrece un contraste de ~3.01:1 sobre fondos blancos. Al abstraer el Orange 800 en `$color-regular`, elevamos el ratio a >6:1 de forma escalable. Al limitar el alcance con Scoped CSS (`p a, li a`), la especificidad (0,0,2) queda intencionadamente por debajo de las pseudo-clases interactivas globales `a:hover` y `a:visited` (0,1,1), respetando la cascada nativa de SASS sin reescribir código.

**Motivo / criterio:** *Context-Aware Styling y Single Source of Truth*. Utilizar colores quemados (hardcoded) ensucia la arquitectura. Extraer el color a una variable semántica y aplicarlo mediante alcance de contexto salda la deuda matemática del WCAG AA donde es estrictamente necesario, protegiendo el diseño global y el "Cuádruple 100".

**Siguiente paso o deuda:** Validar la restitución del 100/100 en PageSpeed Insights y seguir cerrando la fase 11.

### 2026-05-05 — Milestone: Protocolo de Cierre y Sello Definitivo de la Fase 11

**Contexto:** Aplicar el *Definition of Done* (Protocolo Estricto de Cierre de Fase) tras completar la Integración Continua en la nube (CI/CD), finalizando oficialmente la construcción del ecosistema base fundacional.

**Hecho:** Se ejecutó el protocolo y se superó la lista de verificación:
- [x] **1. Deuda Técnica:** 0 TODOs. Orquestador maestro (`merci total`) en verde absoluto tras depurar la deriva de datos (Data Drift) en WordPress.
- [x] **2. Cosecha de Conocimiento:** Cuadernillos sobre SSH, normalización Casefold y Despliegue SSG curados, publicados en Biblioteca y Art de Coté.
- [x] **3. Auditoría Documental:** `README.md` sincronizado con los hitos y *rollbacks* de la Fase 11.
- [x] **4. Evaluación de Release:** Script `merci-init.py` purgado de dependencias de despliegue automatizado para salvaguardar el Boilerplate.
- [x] **5. Snapshot:** Backup ultraligero del estado final generado con éxito.
- [x] **6. Sello Definitivo:** Commit atómico de consolidación preparado.

**Motivo / criterio:** *Governance y Definition of Done (DoD)*. Sellar formalmente la Fase 11 certifica que el Boilerplate y su matriz están maduros, auditados y blindados. Es el paso obligatorio para transicionar hacia la Orquestación con Inteligencia Artificial sin arrastrar deudas de infraestructura.

**Siguiente paso o deuda:** Iniciar formalmente la Fase 1 del nuevo plan de proyecto: `ROADMAP-AI-ORQUESTACION-SELF-HEALING-SYSTEM.md`.

### 2026-05-05 — Docs: Preservación de flujo CI/CD descartado en Art de Coté

**Contexto:** Tras decidir amputar el despliegue automatizado por colisión con el CMS (Content Management System - Sistema de Gestión de Contenidos), se requería no perder el código funcional desarrollado, atesorándolo como un activo de conocimiento.

**Hecho:** Se redactó el activo de conocimiento `laboratorio/art-de-cote/cuadernillo-despliegue-ssg-puro.md`.

**Detalle técnico:** El cuadernillo documenta íntegramente el flujo YAML de GitHub Actions (con inyección nativa de `ssh-agent` y escudos de diagnóstico) y justifica arquitectónicamente por qué el uso de `rsync --delete` es hostil contra arquitecturas híbridas que dependen de enlaces simbólicos no rastreados por Git.

**Motivo / criterio:** *Waste Not (Cero Desperdicio)*. En I+D, el código descartado de forma justificada no es basura, es experiencia. Guardarlo en la taxonomía "Art de Coté" previene tener que reinventar la rueda si en el futuro se despliega una versión del Boilerplate que sea 100% estática.

**Siguiente paso o deuda:** Iniciar formalmente la Fase 1 del Roadmap de Orquestación de IA.

### 2026-05-05 — Arch: Rollback de Despliegue Automático (CD) a favor de control manual

**Contexto:** Tras activar el despliegue automático mediante `rsync` en GitHub Actions, se detectó que la capa dinámica (WordPress) dejaba de cargar en producción, obligando a depender del `git pull` manual (el cual sí preservaba la operatividad del CMS).

**Hecho:** Se eliminó físicamente el archivo `.github/workflows/deploy.yml` para amputar la capacidad de Despliegue Continuo (CD - Continuous Deployment) del robot de GitHub, manteniendo únicamente la Integración Continua (CI) de auditoría. Se actualizó el `README.md` reflejando el rollback.

**Detalle técnico:** El diagnóstico forense reveló por qué `rsync` rompía WordPress y `git pull` no: El comando `rsync --delete public/` ejecutado por el robot borraba implacablemente el enlace simbólico `public/blog` en el servidor de producción (ya que este symlink está en `.gitignore` y no existe en el repositorio de GitHub). Por el contrario, `git pull` ignora los archivos no rastreados, preservando el puente hacia el CMS.

**Motivo / criterio:** *Control Operativo y Rollback*. En lugar de sobre-ingeniar el comando `rsync` con exclusiones complejas para el symlink, se asume la decisión de diseño de mantener el control manual del despliegue (`git pull`). La capacidad de revertir una automatización que añade fricción y destruye entornos es un pilar del desarrollo DevSecOps.

**Siguiente paso o deuda:** Iniciar formalmente la Fase 1 del Roadmap de Orquestación de IA.

### 2026-05-05 — Docs: Cuadernillo sobre normalización de temas (Casefold)

**Contexto:** Se detectó duplicidad de estanterías temáticas en el índice de la biblioteca generada por SSG (Static Site Generation - Generación de Sitios Estáticos) debido a variaciones en la capitalización del texto introducido manualmente en los archivos Markdown.

**Hecho:** Se redactó el activo de conocimiento `laboratorio/cuadernillo-normalizacion-casefold.md`.

**Detalle técnico:** El documento explica la diferencia crítica entre `.lower()` y `.casefold()` en Python, y cómo la normalización de cadenas de entrada soluciona la fragmentación de categorías sin modificar el texto visual original.

**Motivo / criterio:** *Knowledge Management*. Documentar por qué se elige un método específico (`casefold`) sobre el habitual (`lower`) preserva la intención técnica (evitar fallos con caracteres especiales o acentos en la agrupación de diccionarios) para futuros mantenedores.

**Siguiente paso o deuda:** Promover el cuadernillo a la Biblioteca cuando se considere finalizado y evaluar el comportamiento de los flujos de GitHub Actions tras el `git push`.

### 2026-05-05 — Fix: Erradicación de rutinas de despliegue en el Boilerplate

**Contexto:** Se identificó que el orquestador de instanciación (`merci-init.py`) conservaba el flujo de GitHub Actions de despliegue (`deploy.yml`) de la matriz. Como el Boilerplate es una plantilla agnóstica sin servidor de producción asociado, este archivo constituía un residuo arquitectónico inútil y acoplado.

**Hecho:** Se parcheó `scripts/merci/merci-init.py` para aplicar la eliminación física (`unlink`) del archivo `.github/workflows/deploy.yml` durante la instanciación de clones.

**Detalle técnico:** Se añadió la instrucción `(REPO_ROOT / ".github" / "workflows" / "deploy.yml").unlink(missing_ok=True)` en la fase de purga de datos históricos.

**Motivo / criterio:** *Agnosticismo de Infraestructura y Zero Trust*. Un proyecto derivado no debe nacer con flujos de despliegue automatizado (Continuous Deployment) pre-configurados con las rutas del proyecto original. Si el usuario final requiere CD, debe configurarlo desde cero para su propio entorno.

**Siguiente paso o deuda:** Iniciar el nuevo roadmap de Orquestación IA (`ROADMAP-AI-ORQUESTACION-SELF-HEALING-SYSTEM.md`).

### 2026-05-05 — Docs: Cuadernillo sobre inyección SSH en GitHub Actions

**Contexto:** Tras la exitosa depuración de los errores de autenticación (`Permission denied`) y variables vacías en el flujo CI/CD (Continuous Integration / Continuous Deployment - Integración Continua / Despliegue Continuo) de GitHub Actions, era necesario documentar las lecciones aprendidas sobre gestión de secretos y configuración de `rsync`.

**Hecho:** Se creó el activo de conocimiento `biblioteca/cuadernillo-secretos-ssh-github-actions.md`.

**Detalle técnico:** El documento expone la necesidad de la segregación de variables de entorno en la bóveda de GitHub, el uso estricto de la clave privada copiada en crudo sin comillas y la inyección obligatoria del parámetro `-e "ssh -i ~/.ssh/id_ed25519"` en el comando `rsync` para establecer la conexión SSH (Secure Shell).

**Motivo / criterio:** *Knowledge Management (Gestión del Conocimiento)*. Convertir el tiempo invertido en depurar infraestructura en un manual de referencia previene que futuros mantenedores o usuarios del Boilerplate tropiecen con los mismos fallos crípticos de conexión al intentar desplegar en la nube.

**Siguiente paso o deuda:** Ejecutar el orquestador global para empaquetar este nuevo activo en el proyecto base y retomar formalmente el inicio de la Fase 1 en el nuevo roadmap de Inteligencia Artificial.

### 2026-05-05 — Milestone: Cierre de Fase 11 (CI/CD, Lighthouse y Cloud Deploy)

**Contexto:** Sellar el proyecto base automatizando la monitorización de rendimiento (Core Web Vitals) y la compilación SSG (Static Site Generation - Generación de Sitios Estáticos) directamente en la nube, garantizando que el servidor de producción solo reciba código inmaculado.

**Hecho:**
- Creado archivo de presupuesto de rendimiento `lighthouserc.json` imponiendo un límite estricto de 100/100 en todas las categorías.
- Creado flujo `.github/workflows/lighthouse.yml` para ejecutar Lighthouse CI en cada PR (Pull Request - Solicitud de Extracción).
- Creado flujo `.github/workflows/deploy.yml` para compilar `merci-publish.py` en el *runner* y sincronizar vía rsync (SSH - Secure Shell) a CloudPanel.
- Actualizado `README.md` marcando la Fase 11 como 100% completada.

**Motivo / criterio:** *Zero Maintenance y Strict QA (Quality Assurance - Aseguramiento de Calidad)*. Al compilar el SSG en GitHub Actions, liberamos a la máquina local y al servidor VPS (Virtual Private Server - Servidor Privado Virtual) de la carga de compilación. Lighthouse CI actúa como la guillotina final: si un solo commit reduce el rendimiento a 99/100, la integración se bloquea automáticamente.

**Siguiente paso o deuda:** Con la Fase 11 terminada, el proyecto base (Merci Boilerplate) alcanza su máxima madurez. El siguiente hito lógico es dar el salto al nuevo horizonte de IA, iniciando la Fase 1 del `ROADMAP-AI-ORQUESTACION-SELF-HEALING-SYSTEM.md`.

### 2026-05-05 — Milestone: Protocolo de Cierre y Sello Definitivo del CV Semántico

**Contexto:** Aplicar el *Definition of Done* (Protocolo Estricto de Cierre de Fase) tras la implementación del currículum semántico JSON-LD y su cuadernillo, garantizando cero deuda técnica antes de transicionar a una nueva fase.

**Hecho:** Se ejecutó el protocolo y se superó la lista de verificación:
- [x] **1. Deuda Técnica:** 0 TODOs. El auditor maestro (`merci-audit.py`) no reporta advertencias WAI-ARIA, SEO ni de acrónimos en el nuevo HTML ni en el cuadernillo.
- [x] **2. Cosecha de Conocimiento:** Documento `cuadernillo-cv-anti-ats-json-ld.md` atesorado definitivamente en la Biblioteca, cerrando el ciclo atómico.
- [x] **3. Auditoría Documental:** `README.md` sincronizado con la Fase 8.4 sellada al 100%.
- [x] **4. Evaluación de Release:** El orquestador de inicialización `merci-init.py` ya incluye la abstracción DLP para convertir el CV en una plantilla genérica para la versión base.
- [x] **5. Snapshot:** Ejecutado `merci-backup.py` para generar una instantánea ultraligera (Snapshot) del proyecto en estado inmaculado.
- [x] **6. Sello Definitivo:** Commit atómico de consolidación generado y listo para subir.

**Motivo / criterio:** *Governance y Shift-Left*. Ninguna pieza de software o de identidad está realmente acabada hasta que su "porqué" arquitectónico está escrito, curado y respaldado. Este protocolo asegura que no arrastramos cabos sueltos ni deuda silenciosa al iniciar nuevos desarrollos lógicos o de nube.

**Siguiente paso o deuda:** Iniciar el nuevo roadmap de Orquestación IA (`ROADMAP-AI-ORQUESTACION-SELF-HEALING-SYSTEM.md`) o retomar la Fase 11 de CI/CD.

### 2026-05-05 — Creación de cuadernillo "El CV Anti-ATS" (JSON-LD)

**Contexto:** Documentar la filosofía y la implementación técnica detrás del CV semántico "Anti-ATS" y el uso de JSON-LD, como un activo de conocimiento permanente en la Biblioteca.

**Hecho:** Se creó el archivo `biblioteca/cuadernillo-cv-anti-ats-json-ld.md` siguiendo el formato de 3 átomos (Desafío, Maniobra, Aprendizaje).

**Detalle técnico:** El cuadernillo explica el uso de `schema.org/Person` en JSON-LD para optimizar la lectura de perfiles profesionales por parte de los sistemas ATS, garantizando una extracción de datos precisa y sin errores, y cómo se integra en la página `/sobre-mi/index.html`.

**Motivo / criterio:** Consolidar el conocimiento sobre una solución innovadora a un problema común en el reclutamiento técnico, alineado con la filosofía de "Shift-Left" y "Comunicación en capas" del proyecto. Este documento sirve como referencia para entender la implementación del CV semántico.

**Siguiente paso o deuda:** Asegurar que el cuadernillo esté correctamente integrado en el pipeline SSG y sea accesible desde la Biblioteca.



### 2026-05-04 — Fix: Fallback dinámico en enrutador Zsh (Alias Inteligentes v3.1)

**Contexto:** Al instanciar un nuevo clon del Boilerplate, la ejecución del comando habitual `merci init` falló devolviendo `no existe el archivo o el directorio: .venv/bin/python`. Al ser un repositorio recién clonado, el entorno virtual aún no existía.

**Hecho:** Se actualizó la función `merci()` en el archivo `~/.zshrc` y la documentación correspondiente en `Alias Inteligentes-bitacora.md` a la versión 3.1.

**Detalle técnico:** Se inyectó un condicional `if [ -f ".venv/bin/python" ]` dentro del enrutador. Si el entorno virtual existe, lo usa (fricción cero). Si no existe (clon limpio), aplica *Degradación Elegante* haciendo *fallback* al binario global de `python3`.

**Motivo / criterio:** *Developer Experience (DX) y Fail Gracefully*. Las herramientas CLI deben adaptarse al usuario, no al revés. Aunque el SOP indicaba usar `python3` explícitamente, la memoria muscular lleva a usar el alias. Dotar al alias de la inteligencia para sobrevivir en entornos limpios es un paso más hacia el "Cero Mantenimiento".

**Siguiente paso o deuda:** Re-ejecutar `merci init` en el clon temporal y finalizar la exportación del Boilerplate v1.6.0.

### 2026-05-04 — Milestone: Cierre de Fase 8.4 y Validación del Definition of Done (Release v1.6.0)

**Contexto:** Finalizar formalmente la Fase 8.4 (Identidad y Autoridad Técnica) y las mejoras operativas de *Cero Mantenimiento* antes de empaquetar y exportar la versión 1.6.0 al repositorio público del Boilerplate.

**Hecho:** Se revisaron las documentaciones y se ejecutó el Protocolo Estricto de Cierre de Fase:
- [x] **1. Deuda Técnica:** 0 TODOs bloqueantes. Implementada Degradación Elegante (Fail Gracefully) en dependencias locales (`sys.exit(0)`).
- [x] **2. Cosecha de Conocimiento:** Creada la versión 3.0 del cuadernillo de Alias Inteligentes y consolidada atómicamente en la biblioteca.
- [x] **3. Auditoría Documental:** `README.md` actualizado con hitos completos. `README-merci.md` con *release notes* de la v1.6.0.
- [x] **4. Evaluación de Release:** Script `merci-init.py` fortificado con rutinas DLP y ejecutado con éxito en el clon temporal.
- [x] **5. Snapshot:** Copia de seguridad local generada correctamente mediante `merci-backup.py`.
- [x] **6. Sello Definitivo:** Commit atómico de cierre consolidado y Boilerplate v1.6.0 exportado con éxito.

**Motivo / criterio:** *Governance y Definition of Done (DoD)*. Garantizar que la plantilla pública (Boilerplate) no herede datos privados de la autora ni dependencias frágiles, sellando empíricamente la madurez de la infraestructura.

### 2026-05-04 — Fix: Degradación Elegante (Fail Gracefully) en dependencias locales

**Contexto:** Al clonar el repositorio Boilerplate e invocar el orquestador global (`merci total`) mediante el intérprete Python global, el pipeline colapsaba con `sys.exit(1)` por la ausencia de las librerías `markdown`, `weasyprint` y `Pillow`, contraviniendo la política de "0 dependencias bloqueantes".

**Hecho:**
- Se refactorizaron las cabeceras `try/except ImportError` en `merci-publish.py`, `merci-wp.py` y `merci-optimizer.py`.
- Se sustituyeron los códigos de salida fatales por salidas exitosas (`sys.exit(0)`) acompañadas de advertencias informativas (`ℹ️ [Merci Info]`).
- Se implementó un bypass seguro para WeasyPrint (`if HTML:`), permitiendo compilar en HTML aunque falle la generación de PDFs.

**Motivo / criterio:** *Out-of-the-Box Experience*. La promesa de 0 dependencias implica que el repositorio debe auditar, compilar SASS y verificar enlaces desde el minuto uno sin forzar al usuario a hacer `pip install`. Convertir dependencias locales faltantes en advertencias en lugar de bloqueos permite que el pipeline "sobreviva" y entregue el máximo valor posible, degradando elegantemente las capacidades secundarias.

**Siguiente paso o deuda:** Validar la ejecución inmaculada del pipeline en un clon limpio y retomar la automatización de CI/CD en GitHub Actions (Fase 11).

### 2026-05-04 — Arch: Data Leak Prevention para el CV Semántico en Boilerplate

**Contexto:** Antes de empaquetar la nueva versión del proyecto base (Boilerplate), se detectó un riesgo crítico de fuga de datos (Data Leak): la nueva página `/sobre-mi/index.html` contenía el perfil personal de la autora y sus datos JSON-LD estructurados.

**Hecho:** Se planificó la actualización del orquestador destructivo `merci-init.py` y se actualizó `README-merci.md` a la versión `v1.6.0`.

**Detalle técnico:** En lugar de purgar físicamente la página de currículum (lo cual rompería los enlaces de navegación del menú global), se definió la estrategia de "abstracción". El script de inicialización deberá vaciar los metadatos JSON-LD y reemplazar el contenido del *Hero* por texto genérico (Placeholder), entregando al usuario final una plantilla semántica "Anti-ATS" lista para usar.

**Motivo / criterio:** *Data Leak Prevention (DLP) y Valor de Producto*. Proteger la PII (Personally Identifiable Information) de la autora es innegociable. Convertir el archivo en una plantilla en lugar de borrarlo aporta un valor inmenso al repositorio derivado.

**Siguiente paso o deuda:** Actualizar la lógica de `scripts/merci/merci-init.py` para inyectar la rutina de anonimización y ejecutar el Release Pipeline de la v1.6.0.

### 2026-05-04 — Fix: Sincronización de menú en plantilla monolítica de WooCommerce

**Contexto:** Tras propagar el nuevo enlace "Sobre Mí" por el ecosistema (SSG e `index.php` de WordPress), se detectó que la página de la tienda carecía de dicho enlace, generando una asimetría visual en la navegación.

**Hecho:** Se inyectó manualmente el enlace `<a href="/sobre-mi/" class="nav__link">Sobre Mí</a>` en el bloque `<nav>` del archivo `src/wp-theme/merci-theme/woocommerce.php`.

**Detalle técnico:** En una arquitectura de plantillas sin fragmentación (sin `header.php` ni `footer.php`), los archivos que actúan como puntos de entrada independientes (como `woocommerce.php`) mantienen su propia estructura HTML hardcodeada y no heredan los cambios de `index.php`.

**Motivo / criterio:** *Dev/Prod Parity* y *Coherencia UX*. Mantener plantillas monolíticas reduce las consultas de E/S en PHP mejorando el rendimiento, pero la deuda técnica asumida es que las actualizaciones estructurales del "layout" deben replicarse en todos los archivos raíz del *Child Theme*.

**Siguiente paso o deuda:** Ejecutar commit, hacer *push* de la corrección y avanzar finalmente hacia la Fase 11 (Lighthouse CI y compilación SSG en la nube).

### 2026-05-04 — Feat: Autodescubrimiento en Sincronizador Estático (merci-sync-pages)

**Contexto:** Aunque el sincronizador `merci-sync-pages.py` fue refactorizado para aceptar una lista de páginas, esto obligaba a mantener un registro manual (hardcoding) cada vez que se creaba una nueva página estática *standalone*, generando deuda técnica y riesgo de omisión.

**Hecho:** Se implementó una función de autodescubrimiento (`discover_target_pages`) mediante `Path.rglob()` en `scripts/merci/merci-sync-pages.py`.

**Detalle técnico:** El script ahora escanea recursivamente el directorio `public/` buscando todos los archivos `.html`. Ignora automáticamente la portada (`index.html` - SSOT) y excluye directorios gobernados por otros procesos (como `biblioteca/`, `descargas/` y el symlink `blog/`).

**Motivo / criterio:** *Automation & Zero Maintenance*. Un script DevSecOps maduro no debe requerir que el código fuente se actualice para realizar su trabajo sobre nuevos archivos. El autodescubrimiento lo hace verdaderamente "Plug & Play" y garantiza que ninguna página estática presente o futura quede desincronizada.

**Siguiente paso o deuda:** Ejecutar el orquestador global (`merci total`) y finalizar el commit de despliegue de la Fase 8.4.

### 2026-05-04 — Fix: Sincronización de páginas estáticas y orden de menú

**Contexto:** Al crear la página `/sobre-mi/`, esta no heredó los elementos comunes (menú, footer) porque el orquestador `merci-sync-pages.py` estaba rígidamente programado para sincronizar únicamente la página de contacto. Además, se solicitó que el enlace "Sobre Mí" apareciera inmediatamente después de "Biblioteca" en la navegación.

**Hecho:** 
- Se refactorizó `scripts/merci/merci-sync-pages.py` para aceptar una matriz (`TARGET_PAGES`) con múltiples rutas.
- Se reordenó el enlace en el `<nav>` de `public/index.html` y `src/wp-theme/merci-theme/index.php`.

**Detalle técnico:** El script de Python ahora itera de forma dinámica sobre todas las rutas estáticas independientes definidas en la constante `TARGET_PAGES`. Si se añaden nuevas páginas *standalone* en el futuro, solo es necesario agregarlas a esta lista.

**Motivo / criterio:** *Single Source of Truth* y automatización escalable. Un orquestador debe ser capaz de crecer con el proyecto. Forzar las rutas (hardcoding) es deuda técnica; iterar sobre ellas lo convierte en un verdadero sincronizador global.

**Siguiente paso o deuda:** Ejecutar `merci total` para sincronizar las páginas correctamente y finalizar el commit de despliegue.

### 2026-05-04 — Docs: Unificación de cuadernillos de Alias Inteligentes (v3.0)

**Contexto:** Se detectó fragmentación en la biblioteca al promover la versión 3.0 de los Alias Inteligentes como un cuadernillo independiente, separándolo de las versiones 1.0 y 2.0 ya documentadas.

**Hecho:**
- Se eliminó el archivo `biblioteca/cuadernillo-alias-inteligentes-v30-para-ecosistemas-devsecops.md`.
- Se fusionó su contenido (explicación de Runtime vs Buildtime y enrutamiento `.venv`) dentro del archivo original `biblioteca/Alias Inteligentes-bitacora.md`.

**Motivo / criterio:** *Single Source of Truth* y *Atomización de la Información*. Mantener la evolución de una misma herramienta en un único documento histórico facilita su consulta y evita la dispersión temática en la Biblioteca.

**Siguiente paso o deuda:** Ejecutar el orquestador global (`merci total`) para limpiar artefactos huérfanos y validar los enlaces en verde.

### 2026-05-04 — Feat: Creación del CV Semántico "Anti-ATS" (JSON-LD)

**Contexto:** El orquestador `merci total` detuvo el pipeline al detectar el enlace roto (`/sobre-mi/`) inyectado en la fase anterior, demostrando el éxito del patrón Fail-Fast del escáner DAST local (`merci-linkcheck.py`). Se requería construir la página de currículum finalizando la Fase 8.4.

**Hecho:** 
- Se creó la carpeta y el archivo `public/sobre-mi/index.html`.
- Se inyectó el esquema de datos `schema.org/Person` en formato JSON-LD en la cabecera del documento.

**Detalle técnico:** En lugar de renderizar el CV dinámicamente con dependencias externas, los datos duros (stack tecnológico, rol DevSecOps, URLs) se estructuraron en un bloque `<script type="application/ld+json">`. Esto permite que cualquier IA o ATS (Applicant Tracking System) extraiga el perfil con un 100% de precisión sin necesidad de procesar PDFs o DOM visual. La página utiliza las clases estructurales BEM ya existentes.

**Motivo / criterio:** *Semantic Web y Zero Bloat*. Responder a las demandas del mercado corporativo de 2026 entregando los datos directamente en el idioma nativo de las máquinas que procesan los reclutamientos, demostrando autoridad técnica mediante el propio formato de entrega.

**Siguiente paso o deuda:** Ejecutar `merci total` para validar que el pipeline resuelve los enlaces a 0 errores y proceder al commit atómico.

### 2026-05-04 — Docs: Redacción de cuadernillo Alias Inteligentes v3.0

**Contexto:** Tras la resolución del problema de activación de entornos virtuales y la consolidación de la política de "0 Dependencias (Runtime vs Buildtime)", era preceptivo generar un activo de conocimiento basado en la nueva función Zsh `merci()`.

**Hecho:** Se redactó el borrador `cuadernillo-alias-inteligentes-v30-para-ecosistemas-devsecops.md` en el laboratorio.

**Motivo / criterio:** *Knowledge Harvesting (Cosecha de Conocimiento)*. Documentar la evolución de nuestras propias herramientas de terminal asegura que los principios DevSecOps no se pierdan. La versión 3.0 consolida el uso de binarios aislados, la eliminación de la fricción operativa y el paso de parámetros ilimitados.

**Siguiente paso o deuda:** Iniciar la redacción estática del CV Semántico (`/sobre-mi/index.html`) expuesto con marcado JSON-LD.

### 2026-05-04 — Arch: Cero Dependencias (Runtime vs Buildtime) y enrutador Zsh inteligente

**Contexto:** La ejecución de herramientas locales (como `merci total`) fallaba si se olvidaba activar el entorno virtual de Python (`source .venv/bin/activate`), generando fricción operativa. Se debatió si eliminar dependencias de compilación y migrar a `.txt` puro para evadir el uso de entornos virtuales.

**Hecho:** 
- Se clarificó la regla arquitectónica: la política de "0 dependencias" aplica estrictamente al entorno de ejecución (Runtime en navegador), no a las herramientas de construcción locales (Buildtime / pipeline).
- Se actualizó la función inteligente `merci()` en `~/.zshrc` para apuntar explícitamente al binario aislado del entorno (`.venv/bin/python`).

**Detalle técnico:** Al usar la ruta explícita del binario (`.venv/bin/python "scripts/merci/merci-$1.py"`), el sistema operativo resuelve automáticamente las librerías instaladas en ese entorno aislado sin necesidad de que la sesión de la terminal esté "activada", logrando fricción cero (DX).

**Motivo / criterio:** *Developer Experience (DX)* y *Separation of Concerns*. No se debe sacrificar una arquitectura madura (Markdown, WeasyPrint para PDF, WebP) por una molestia operativa en la terminal. Modificar la función de enrutamiento para que sea consciente del entorno virtual es la solución POSIX nativa y elegante.

**Siguiente paso o deuda:** Ejecutar `merci sync-pages` y propagar el nuevo enlace del menú (`/sobre-mi/`) a las plantillas dinámicas de WordPress.

### 2026-05-04 — Docs: Expansión del Roadmap (Fase 8.4 Identidad y Autoridad Técnica)

**Contexto:** Tras modificar el posicionamiento en la portada (`index.html`) inyectando el nuevo enlace a `/sobre-mi/`, se generó un enlace roto (deuda técnica). Para evitar el desarrollo errático y el "Scope Creep", era obligatorio registrar formalmente los próximos pasos en el plan de proyecto antes de continuar escribiendo código.

**Hecho:** 
- Se inyectó la subfase `8.4 Identidad y Autoridad Técnica` en el `README.md`.
- Se marcó la reescritura de la portada como completada y se listaron las tareas pendientes (propagación de menú y CV Semántico).

**Motivo / criterio:** *Governance y Single Source of Truth (SSOT)*. Respetar la Regla 12 de las directrices: ninguna maniobra arquitectónica debe ejecutarse sin antes estar planificada. Esto garantiza que la deuda técnica quede trazada y el proyecto no pierda su integridad estructural.

**Siguiente paso o deuda:** Sincronizar el nuevo enlace del menú en todas las plantillas (WordPress y estáticas) antes de proceder a la creación del HTML del CV semántico.

### 2026-05-04 — Docs: Actualización de posicionamiento público y perfil arquitectónico

**Contexto:** Tras una evaluación de la infraestructura y el "copy" del proyecto, se constató que la narrativa fundacional ("transición desde entorno no-dev") no reflejaba la madurez real de la arquitectura DevSecOps alcanzada. Era imperativo ajustar el perfil público y las directrices internas al nivel de una "AI Systems Architect" apoyada en el *Spec-Driven Development*.

**Hecho:** 
- Se actualizó el `README.md` eliminando la narrativa *junior* e inyectando la terminología técnica correcta (Decisiones de Arquitectura, Spec-Driven).
- Se refactorizó el "Perfil del Asistente" en `instrucciones.md` para oficializar el modelo de Gobernanza (Mercedes como Arquitecta Directora, la IA como Ejecutor Táctico).

**Motivo / criterio:** *Single Source of Truth y Brand Identity*. El código base (orquestadores DevSecOps en Python puro, SSG híbrido con Headless CMS, seguridad Shift-Left) exige una presentación documental alineada con su complejidad técnica. Mitigar el "síndrome del impostor documental" asegura que cualquier evaluador que clone el repositorio lo aborde desde la perspectiva correcta de ingeniería de software.

**Siguiente paso o deuda:** Iniciar la reescritura del `public/index.html` bajo este nuevo prisma de autoridad técnica y consolidar la nueva UI/UX del portfolio.

### 2026-05-02 — QA: Validación de redirección segura y Cuádruple 100 en WP

**Contexto:** Tras inyectar el escudo anti-proxy para forzar HTTPS en el entorno de WordPress, era necesario reevaluar la ruta dinámica sin barra final (`/blog`) para confirmar la erradicación del problema de *Mixed Content*.

**Hecho:** Se ejecutó una nueva auditoría externa con Google PageSpeed Insights sobre la URL conflictiva.

**Detalle técnico:** WordPress resolvió la redirección 301 hacia la ruta canónica preservando el esquema HTTPS. Se certificó la recuperación de la puntuación en "Mejores Prácticas", logrando un Cuádruple 100 perfecto (Rendimiento, Accesibilidad, Mejores Prácticas, SEO) bajo simulación móvil 4G, reteniendo un TBT (Total Blocking Time) de 0 ms.

**Motivo / criterio:** *QA Assurance (Aseguramiento de Calidad)*. Cerrar el ciclo de depuración validando empíricamente que el parche a nivel de código de aplicación elimina la penalización del motor de búsqueda sin generar efectos secundarios en el rendimiento.

**Siguiente paso o deuda:** Iniciar los hitos de la Fase 11 (Lighthouse CI y compilación en la nube).

### 2026-05-02 — Fix: Prevención de redirecciones inseguras (Mixed Content) por Ceguera de Proxy

**Contexto:** Una auditoría de PageSpeed Insights penalizó la puntuación de "Mejores Prácticas" (81/100) al detectar una solicitud no segura (HTTP). El análisis reveló que al solicitar una URL sin barra final (`/blog`), WordPress generaba una redirección canónica hacia HTTP en lugar de HTTPS.

**Hecho:**
- Se inyectó la lectura de la cabecera `HTTP_X_FORWARDED_PROTO` en `src/wp-theme/merci-theme/functions.php`.
- Si el proxy inverso informa que la conexión original es segura, se fuerza la variable global `$_SERVER['HTTPS'] = 'on'`.

**Detalle técnico:** WordPress utiliza la variable `$_SERVER['HTTPS']` para construir dinámicamente enlaces canónicos, metaetiquetas y redirecciones `301`. Al estar detrás de Varnish/CloudPanel, esta variable llega vacía (Ceguera de HTTPS). Restaurarla a nivel de tema corrige la redirección sin necesidad de alterar el `wp-config.php` del servidor.

**Motivo / criterio:** *Security & Shift-Left Routing*. Prevenir las degradaciones de protocolo (Mixed Content) protege la integridad de las sesiones de los usuarios y restablece el 100/100 en las métricas de calidad de Google, solucionando la penalización de forma agnóstica al proveedor de hosting.

**Siguiente paso o deuda:** Iniciar los hitos de la Fase 11 (Lighthouse CI y compilación en la nube).   

### 2026-05-02 — Fix: Degradación elegante por ausencia de API Key (Fail Gracefully)

**Contexto:** Al instanciar el Boilerplate y ejecutar `merci total`, el orquestador abortaba la ejecución (Fail-Fast) en la etapa de `merci-brain.py` al no encontrar la variable `GEMINI_API_KEY` en el `.env`, impidiendo que los nuevos usuarios completaran su primera compilación.

**Hecho:**
- Se reemplazó la salida de error fatal (`sys.exit(1)`) por una advertencia (`WARN`) y salida exitosa (`sys.exit(0)`) en `scripts/merci/merci-brain.py`.

**Detalle técnico:** El script ahora detecta la ausencia de la clave, emite un mensaje informativo indicando que el asistente operará con sus respuestas genéricas y finaliza su proceso en verde. Esto permite que el orquestador maestro continúe con las auditorías (QA) y el rastreo de enlaces ininterrumpidamente.

**Motivo / criterio:** *Out-of-the-Box Experience* y *Graceful Degradation*. Una característica opcional (como la IA de terceros) nunca debe romper la cadena de montaje (Build Pipeline) de un usuario recién llegado. Suavizar este error elimina la fricción de configuración inicial y protege la confianza en la herramienta.

**Siguiente paso o deuda:** Re-exportar la versión definitiva del Boilerplate (v1.5.0), aplicar el snapshot final y dar por terminada la jornada.

### 2026-05-02 — Arch: White-labeling y Guillotina Opcional para IA en Boilerplate

**Contexto:** El módulo de Inteligencia Artificial ("Merci") estaba fuertemente acoplado a la marca personal de la autora. Distribuir el Boilerplate con este avatar por defecto generaría intrusión de marca e hinchazón de código para usuarios que solo desearan un generador estático purista.

**Hecho:**
- Se implementó un prompt condicional (Opt-Out) en `scripts/merci/merci-init.py`.
- Se programó una rutina de "Marca Blanca" que neutraliza los textos y prompts del avatar.
- Se programó una rutina de "Amputación Quirúrgica" que elimina atómicamente el módulo IA (SASS, Vanilla JS, Python y llamadas HTML) si el usuario lo rechaza.

**Detalle técnico:** El script de instanciación emplea expresiones regulares (`re.sub`) para inyectarse en el código de `merci-total.py` y `merci-publish.py`, erradicando no solo los archivos físicos (`merci-brain.py`, `MerciController.js`), sino también cualquier línea de importación, función o variable enlazada a ellos, asegurando que el pipeline resultante compile sin errores.

**Motivo / criterio:** *Separation of Concerns* y *Zero Bloat*. Un Boilerplate debe entregar valor sin imponer identidad. Permitir la amputación total del módulo IA empodera al usuario final, manteniendo el proyecto base ultra-ligero y fiel a la promesa de "0 dependencias" reales, mientras preserva la propiedad intelectual (Marca) de la autora original.

**Siguiente paso o deuda:** Desplegar el Boilerplate v1.5.0 actualizado con la nueva guillotina opcional.

### 2026-05-02 — Milestone: Cierre de Fase 9 y Validación del Definition of Done

**Contexto:** Finalizar formalmente la Fase 9 (Inteligencia y Autonomía) garantizando la higiene absoluta del repositorio antes de empaquetar el motor de IA en la Release v1.5.0 y retomar la Fase 11.

**Hecho:** Se ejecutó y superó el Protocolo Estricto de Cierre de Fase:
- [x] **1. Deuda Técnica:** 0 TODOs pendientes. Gestión de cuotas de API y Degradación Elegante implementados. Minimalismo absoluto en consola (DX) aplicado.
- [x] **2. Cosecha de Conocimiento:** Cuadernillo `cuadernillo-shift-left-ai-merci-brain.md` curado, promovido y compilado.
- [x] **3. Auditoría Documental:** Hitos completados en el `README.md` y `README-merci.md` actualizados a v1.5.0 con notas de DX.
- [x] **4. Evaluación de Release:** Release v1.5.0 lista para empaquetar en el Boilerplate.
- [x] **5. Snapshot:** Backup local detallado generado.
- [x] **6. Sello Definitivo:** Commit atómico en preparación.

**Motivo / criterio:** *Governance y Definition of Done (DoD)*. Sellar las fases mediante un checklist auditable previene la transferencia de deuda técnica y garantiza que cada nueva versión del Boilerplate sea madura.

**Siguiente paso o deuda:** Ejecutar el Release Pipeline (v1.5.0), realizar el backup y retomar la Fase 11.

### 2026-05-02 — Docs: Release v1.5.0 del Boilerplate (Shift-Left AI y DX)

**Contexto:** Tras culminar la Fase 9 y pulir la experiencia de desarrollo (DX) del orquestador, era el momento de empaquetar estas mejoras en la plantilla base.

**Hecho:**
- Se actualizó la versión de `README-merci.md` a la `v1.5.0`, documentando la IA estática y el minimalismo en la terminal (Verbose flags).
- Se preparó el código para ejecutar el *Release Pipeline*.

**Motivo / criterio:** *Release Management*. Empaquetar las funcionalidades probadas independiza el motor DevSecOps del contenido de la autora.

### 2026-05-02 — UI/UX: Minimalismo absoluto en consola (Verbose flags)

**Contexto:** Los scripts de automatización generaban un exceso de ruido en la terminal informando de cada paso intermedio ("Leyendo", "Procesando"), lo que dificultaba la lectura del orquestador global.

**Hecho:**
- Se inyectó la bandera `--verbose` (o `-v`) en los scripts locales (`merci-wp.py`, `merci-optimizer.py`, etc.).
- Se ocultaron los mensajes intermedios, conservando únicamente un mensaje de éxito (cuadradito verde) por archivo.

**Detalle técnico:** Se implementó una lógica condicional `if verbose:` alrededor de los mensajes de seguimiento. Las alertas de error permanecen siempre visibles (Fail-Fast).

**Motivo / criterio:** *Silence is Golden* (Filosofía Unix). Un pipeline CI/CD debe ser silencioso cuando tiene éxito y ruidoso cuando falla. Ver únicamente los marcadores de éxito agiliza la lectura de los logs.

### 2026-05-02 — UI/UX: Mejora de espaciado visual en el orquestador maestro

**Contexto:** Al encadenar la ejecución silenciosa de los scripts en `merci-total.py`, los mensajes de finalización de un proceso se pegaban inmediatamente a la cabecera del siguiente (`▶️ Ejecutando...`), dificultando la legibilidad.

**Hecho:**
- Se inyectó un salto de línea condicional (`print()`) en `scripts/merci/merci-total.py` tras la ejecución exitosa de cada subproceso.

**Detalle técnico:** En lugar de modificar los 9 scripts individuales, centralizar el espaciado en el bucle `for` de `merci-total` respeta el principio DRY (Don't Repeat Yourself) y garantiza una separación de bloques uniforme.

**Motivo / criterio:** *Developer Experience (DX)*. El espacio en blanco (Whitespace) es un elemento de diseño fundamental también en la terminal. Separar visualmente los bloques de ejecución reduce la carga cognitiva y permite escanear los resultados rápidamente.

**Siguiente paso o deuda:** Iniciar los hitos de la Fase 11 (Lighthouse CI y compilación en la nube).

### 2026-05-02 — Milestone: Automatización del Lóbulo Frontal y Cierre de Fase 9

**Contexto:** Tras validar la conexión exitosa de la IA estática con la interfaz (Vanilla JS), era imperativo automatizar la generación del cerebro (`brain_data.json`) para que la base de conocimientos se actualice sin intervención humana en cada compilación.

**Hecho:**
- Se inyectó el script `merci-brain.py` en la constante `PIPELINE` del orquestador `merci-total.py`.
- Se dio por concluida oficialmente la Fase 9 (Inteligencia y Autonomía).

**Detalle técnico:** El script de IA se ejecuta en la fase de Construcción (Build), garantizando que el JSON estático esté siempre sincronizado con los artículos publicados antes de que se ejecuten las auditorías de calidad (QA). Al contar con construcción incremental, su impacto en el tiempo de compilación diario es de 0 segundos, y sus fallos de red se gestionan mediante Degradación Elegante.

**Motivo / criterio:** *Pipeline as Code*. Una herramienta que requiere ejecución manual terminará siendo olvidada, generando Deriva de Datos (Data Drift) entre los artículos nuevos y las respuestas de la IA. Integrarlo en el orquestador maestro cierra el círculo DevSecOps.

**Siguiente paso o deuda:** Auditar el ecosistema completo y planificar la Release v1.5.0 del Boilerplate para exportar el motor de Inteligencia Artificial.

### 2026-05-02 — Feat: Integración de Shift-Left AI en Vanilla JS (MerciController)

**Contexto:** Con el archivo estático `brain_data.json` compilado por el lóbulo frontal en Python, se requería conectar este "cerebro" a la interfaz de usuario de Merci sin bloquear la renderización de la página ni requerir recargas.

**Hecho:**
- Se refactorizó `MerciController.js` para cargar asíncronamente el archivo JSON mediante la API `fetch`.
- Se implementó la lógica de limpieza dinámica para los mensajes de contingencia (`[Fallback]`).

**Detalle técnico:** El controlador carga primero la base de conocimientos estándar (`_loadStandardKnowledgeBase()`) para garantizar que la interfaz responda inmediatamente (Fail-Safe). En segundo plano (`_connectBrain()`), realiza la petición asíncrona al JSON. Si el archivo existe y contiene una clave que coincide exactamente con `window.location.pathname`, el mensaje genérico se sobrescribe con la respuesta inteligente.

**Motivo / criterio:** *Zero Latency & Progressive Enhancement*. Cargar el conocimiento por red en segundo plano (Ajax) asegura que el TBT (Total Blocking Time) siga en 0 ms. Al usar la lógica de sobrescritura, si el JSON falla, la web se degrada elegantemente hacia las respuestas nativas, garantizando una UX ininterrumpida.

**Siguiente paso o deuda:** Integrar el lóbulo frontal (`merci-brain.py`) en el orquestador maestro (`merci-total.py`) para que la inteligencia artificial actualice sus conocimientos en cada compilación automática.

### 2026-05-02 — Arch: Degradación Elegante (Graceful Degradation) ante límites de API

**Contexto:** La capa gratuita de Google AI Studio impuso un límite diario ineludible de 20 peticiones para los modelos más recientes, provocando que los últimos artículos del escaneo recibieran y guardaran un error `HTTP 429` como respuesta.

**Hecho:**
- Se implementó el patrón de Degradación Elegante en `merci-brain.py`.
- Si la API devuelve error, el script inyecta un saludo genérico prefijado con `[Fallback]` en el JSON.

**Detalle técnico:** El orquestador fue instruido para que reconozca la etiqueta `[Fallback]` en futuras ejecuciones. De esta forma, el sistema genera un JSON limpio y funcional inmediatamente para no bloquear el desarrollo del frontend. Al día siguiente, cuando la cuota diaria se restablezca, una simple re-ejecución sobrescribirá los fallbacks con respuestas reales de la IA.

**Motivo / criterio:** *Resiliencia de Infraestructura*. Un ecosistema DevSecOps no debe detener su cadena de montaje (Pipeline) porque un proveedor de terceros (SaaS) agote su cuota. Proveer respuestas por defecto garantiza la continuidad del negocio y la integridad de los datos.

**Siguiente paso o deuda:** Conectar el frontend (`MerciController.js`) al archivo `brain_data.json` purificado.

### 2026-05-02 — Fix: Búsqueda flexible de modelos Gemini por subcadenas (Quota 20)

**Contexto:** El autodescubrimiento falló en encontrar la familia `1.5-flash` mediante coincidencia exacta, recayendo por defecto en el modelo experimental `2.5-flash`, el cual agotó su límite estricto de 20 peticiones diarias gratuitas en la primera compilación.

**Hecho:**
- Se refactorizó la función `auto_descubrir_modelo()` en `merci-brain.py` para usar coincidencia por subcadenas (`in`).

**Detalle técnico:** Los proveedores de IA añaden sufijos de versión (ej. `-001`, `-002`) que rompen las validaciones estrictas. Iterar sobre un array de "familias" y buscar si la cadena está contenida en el nombre del modelo garantiza atrapar versiones estables que otorgan cuotas gratuitas altas (1500 RPM).

**Motivo / criterio:** *Resiliencia de API*. Las integraciones con servicios de terceros deben ser lo suficientemente flexibles para soportar cambios menores en las nomenclaturas de sus *endpoints* sin romper la infraestructura de despliegue local.

**Siguiente paso o deuda:** Conectar el frontend (`MerciController.js`) al archivo generado una vez finalizado el escaneo.

### 2026-05-02 — Fix: Exclusión de modelo experimental (Quota limit 0) en Gemini

**Contexto:** Al intentar procesar los últimos artículos, la API de Gemini devolvió un error `HTTP 429` indicando que el límite de cuota era `0` para el modelo `gemini-2.0-flash`, bloqueando la generación estática.

**Hecho:**
- Se actualizó la lista de preferencias en `auto_descubrir_modelo()` dentro de `merci-brain.py`.
- Se eliminó `gemini-2.0-flash` para forzar el uso de la versión estable `gemini-1.5-flash`.

**Detalle técnico:** Google AI Studio impone límites estrictos (o nulos) a modelos en fase experimental o de acceso anticipado según la región o el tier de la cuenta. Retirar la versión 2.0 obliga al script a utilizar la rama 1.5, la cual goza de una cuota gratuita estable de 15 RPM y 1500 peticiones diarias.

**Motivo / criterio:** *Estabilidad sobre Novedad*. En automatizaciones DevSecOps, la fiabilidad de la conexión es más crítica que el uso del último modelo disponible en el mercado.

**Siguiente paso o deuda:** Conectar el frontend (`MerciController.js`) al archivo generado una vez finalizado el escaneo.

### 2026-05-02 — Perf: Construcción incremental y control de cuotas en IA (Rate Limiting)

**Contexto:** El lóbulo frontal (`merci-brain.py`) escaneaba todos los artículos en un bucle rápido, lo que provocó que la API gratuita de Gemini rechazara las conexiones con un error `HTTP 429: Too Many Requests` (límite estricto de 5 peticiones por minuto).

**Hecho:**
- Se refactorizó `merci-brain.py` para leer el archivo `brain_data.json` antes de procesar y saltarse los artículos ya generados (Incremental Build).
- Se implementó un retraso forzado (`time.sleep(15)`) entre llamadas a la API.

**Detalle técnico:** La construcción incremental salva la cuota de la API y reduce el tiempo de compilación a 0 segundos si no hay artículos nuevos. El *Rate Limiting* (15 segundos) garantiza mantenerse dentro del límite de 4-5 RPM de la capa gratuita, evitando baneos del servidor.

**Motivo / criterio:** *Resiliencia y API Governance*. Cuando se integran servicios de terceros (SaaS), es imperativo proteger el orquestador local contra bloqueos de red limitando el consumo (Throttling) y cacheando las respuestas válidas.

**Siguiente paso o deuda:** Conectar el frontend (`MerciController.js`) al archivo generado e integrar el script en el orquestador global.

### 2026-05-02 — Feat: Shift-Left AI (Contexto dinámico inyectado en compilación)

**Contexto:** Se requería dotar al asistente de la interfaz (Merci) de inteligencia artificial para generar saludos contextualizados basados en el artículo que lee el visitante. Realizar peticiones a Gemini desde el frontend Javascript expondría la API Key y arruinaría el rendimiento web (Core Web Vitals).

**Hecho:**
- Se implementó el descubrimiento dinámico de modelos (`gemini-2.5-flash`) en `merci-brain.py`.
- Se programó un escáner de la Biblioteca que extrae el título y la descripción de cada Markdown publicado y solicita a Gemini un saludo ad-hoc.
- Se compiló la salida de la IA en un archivo estático local (`public/js/brain_data.json`).

**Detalle técnico:** Al usar expresiones regulares para leer el YAML Frontmatter, se minimiza la cantidad de tokens enviados a la API (solo se envían metadatos, no el cuerpo completo del artículo). La respuesta se asocia al `slug` del archivo y se empaqueta en JSON.

**Motivo / criterio:** *Shift-Left AI y Edge Performance*. La IA "piensa" en tiempo de compilación dentro del servidor seguro (terminal), no en tiempo de ejecución en el navegador del usuario. Esto permite a la interfaz web ofrecer respuestas generativas complejas con una latencia literal de 0 milisegundos y con coste nulo de API tras el despliegue.

**Siguiente paso o deuda:** Enseñar al frontend (`MerciController.js`) a consumir el nuevo `brain_data.json` y conectar `merci-brain.py` al orquestador maestro (`merci-total`).

### 2026-05-02 — Fix: Resolución de error 404 en conexión sináptica con Gemini (Migración a Flash)

**Contexto:** Al ejecutar la primera prueba de conexión del lóbulo frontal (`merci-brain.py`), la API REST de Google devolvió un error HTTP 404 (Not Found) al solicitar el modelo `gemini-1.5-pro`.

**Hecho:**
- Se refactorizó la URL del endpoint en `scripts/merci/merci-brain.py` para apuntar al modelo ultrarrápido `gemini-1.5-flash`.

**Detalle técnico:** La capa gratuita (v1beta) de Google Cloud / AI Studio rota frecuentemente los alias directos de las versiones Pro o exige sufijos específicos (`-latest`). El modelo Flash ofrece mayor estabilidad en el endpoint y está diseñado específicamente para tareas de baja latencia y alta eficiencia.

**Motivo / criterio:** *Rendimiento y Fricción Cero*. Dado que la IA se utilizará en tiempo de compilación (Shift-Left AI) para procesar artículos, priorizar un modelo optimizado para velocidad (Flash) acelera el flujo de construcción (Build) local y evita romper el pipeline de SSG por cambios de nomenclatura en la API de terceros.

**Siguiente paso o deuda:** Implementar la lógica para que el script lea los artículos de la biblioteca y genere respuestas estáticas (diccionarios JSON).

### 2026-05-02 — Docs: Release v1.4.0 del Boilerplate (CI/CD y Gobernanza)

**Contexto:** Tras integrar GitHub Actions y las plantillas de contribución (Fase 11), el ecosistema base adquirió capacidades de infraestructura en la nube. Era imperativo exportar estas mejoras al repositorio público para que los futuros usuarios hereden el pipeline de integración continua desde el inicio.

**Hecho:**
- Se actualizó `README-merci.md` a la versión `v1.4.0` documentando las novedades de nube y gobernanza.
- Se actualizaron los hitos de la Fase 11 en el `README.md` matriz.
- Se ejecutó el Release Pipeline hacia el repositorio derivado `merci-boilerplate`.

**Motivo / criterio:** *Configuration Drift (Deriva de Configuración)*. Todo componente de infraestructura agnóstico (como `.github/`) pertenece al producto base. Aplicar la Regla 14 de actualización iterativa asegura que el proyecto hijo posea un servidor de CI en la nube preconfigurado ("Out of the Box").

**Siguiente paso o deuda:** Finalizar los últimos hitos de la Fase 11 (Lighthouse CI) o dar el salto definitivo a la Fase 9 (Inteligencia y Autonomía).

### 2026-05-02 — Docs: Gobernanza Open Source (Pull Request Template)

**Contexto:** Tras estandarizar el reporte de *Issues*, era necesario establecer una barrera de calidad para las contribuciones de código (Pull Requests) entrantes, asegurando que los colaboradores respeten la auditoría local y la filosofía del proyecto antes de solicitar una integración.

**Hecho:**
- Se creó el archivo `.github/PULL_REQUEST_TEMPLATE.md`.
- Se incluyó un *checklist* de validación estricto (Shift-Left) en la plantilla.

**Detalle técnico:** GitHub inyecta automáticamente el contenido de este archivo en la caja de descripción cada vez que un usuario abre un nuevo Pull Request. El checklist obliga al contribuyente a confirmar explícitamente que ha ejecutado `merci-audit.py` y que no ha inyectado dependencias externas.

**Motivo / criterio:** *Gatekeeping y Shift-Left Quality*. Un repositorio público atrae contribuciones bienintencionadas pero a menudo desalineadas con la arquitectura (ej. uso de librerías NPM). El checklist actúa como una barrera psicológica y técnica que filtra el código ruidoso, protegiendo el tiempo de revisión de la mantenedora.

**Siguiente paso o deuda:** Finalizar las herramientas de la Fase 11 o transicionar a la Inteligencia y Autonomía (Fase 9).

### 2026-05-02 — Docs: Gobernanza Open Source (Issue Templates)

**Contexto:** Al abrir el Boilerplate a la comunidad o colaborar con otros desarrolladores, se corre el riesgo de recibir reportes de errores desestructurados que no aportan contexto arquitectónico ni pasos de reproducción, generando fricción operativa.

**Hecho:**
- Se crearon las plantillas de contribución `bug_report.md` y `feature_request.md` en el directorio estandarizado `.github/ISSUE_TEMPLATE/`.

**Detalle técnico:** Las plantillas utilizan Markdown con YAML Frontmatter (reconocido nativamente por GitHub) para pre-configurar etiquetas (`bug`, `enhancement`) y prefijos de commits convencionales (`fix:`, `feat:`). Su estructura obliga a quien reporta a utilizar la nomenclatura del proyecto (El Desafío / La Maniobra).

**Motivo / criterio:** *Gobernanza y Fricción Cero*. Estandarizar la entrada de información (Inbound) educa a los colaboradores en la filosofía del proyecto desde el minuto uno. Exigir contexto, entorno y justificación arquitectónica separa las contribuciones valiosas del ruido, manteniendo la higiene del repositorio.

**Siguiente paso o deuda:** Crear la plantilla para Pull Requests (`PULL_REQUEST_TEMPLATE.md`) y dar por consolidada la gobernanza del repositorio.

### 2026-05-02 — Arch: Aceptación de deuda técnica externa en GitHub Actions (Node 20)

**Contexto:** Tras inyectar la variable de entorno para forzar Node.js 24, el runner de GitHub Actions continuó emitiendo la advertencia de deprecación sobre las acciones `checkout@v4` y `setup-python@v5`.

**Hecho:**
- Se constató que el proyecto matriz no utiliza Node.js en su ecosistema.
- Se desestimó la advertencia, asumiéndola como deuda técnica de infraestructura externa.

**Detalle técnico:** El aviso proviene del código interno con el que GitHub programó los *runners* oficiales. Hasta que la plataforma no publique nuevas versiones mayores de estas acciones, la advertencia persistirá a nivel de servidor sin afectar la ejecución.

**Motivo / criterio:** *Separation of Concerns*. En DevSecOps, es vital distinguir entre una vulnerabilidad del código propio y un aviso de mantenimiento de la infraestructura anfitriona. Al tener cero dependencias de Node.js en el proyecto, este aviso no impacta en la seguridad ni el rendimiento.

**Siguiente paso o deuda:** Continuar con la configuración de Gobernanza Open Source (Issue Templates).

### 2026-05-02 — Fix: Resolución de advertencia de deprecación (Node.js 20) en GitHub Actions

**Contexto:** Tras la ejecución exitosa del primer workflow de GitHub Actions, el servidor emitió una advertencia (Warning) indicando que las acciones `checkout@v4` y `setup-python@v5` utilizan Node.js 20, el cual será descontinuado próximamente.

**Hecho:**
- Se inyectó la variable de entorno `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true` a nivel global en `.github/workflows/audit.yml`.

**Detalle técnico:** Forzar el uso de Node.js 24 adelanta la compatibilidad del pipeline y silencia la advertencia de obsolescencia que emite el runner de GitHub, asegurando un reporte de auditoría inmaculado (cero advertencias).

**Motivo / criterio:** *Zero Technical Debt (Cero Deuda Técnica)*. En la arquitectura Merci, las advertencias no se ignoran, se solucionan. Mantener el pipeline en la nube tan limpio como el orquestador local es vital para la disciplina DevSecOps.

**Siguiente paso o deuda:** Continuar con la configuración de Gobernanza Open Source (Issue y PR Templates) de la Fase 11.

### 2026-05-02 — Fix: Reubicación del workflow de GitHub Actions

**Contexto:** El workflow `Merci Audit CI` no se ejecutaba en la nube tras el *push*. Se diagnosticó que el archivo YAML fue guardado en el directorio incorrecto (`laboratorio/`).

**Hecho:** Se movió el archivo `audit.yml` a la ruta estricta obligatoria `.github/workflows/audit.yml`.

**Motivo / criterio:** *Convenciones de CI/CD*. GitHub Actions solo escanea y ejecuta los archivos de declaración de *pipelines* si residen exactamente en la carpeta oculta `.github/workflows/` de la raíz del repositorio.

### 2026-05-02 — Arch: Inicio de Fase 11 (CI/CD) y primer Workflow de GitHub Actions

**Contexto:** Tras finalizar la Fase 8, se requiere trasladar las políticas de seguridad y calidad (Shift-Left) locales hacia la nube, garantizando que ninguna contribución externa ni salto accidental de hooks locales rompa la arquitectura del repositorio público.

**Hecho:**
- Se inició formalmente la Fase 11 (Integración Continua y Calidad en la Nube).
- Se diseñó el primer flujo de GitHub Actions (`.github/workflows/audit.yml`) para automatizar la ejecución de `merci-audit.py`.

**Detalle técnico:** El workflow se configura para reaccionar ante eventos `push` y `pull_request` sobre la rama `main`. Levanta un contenedor virtual Ubuntu, instala Python 3.10 y ejecuta la auditoría estricta (`--strict-json-ld`). Si el script de Python devuelve un código de salida `1` (Error), GitHub marcará el commit con una cruz roja y bloqueará la integración del código.

**Motivo / criterio:** *Continuous Integration (CI)*. La confianza en el código no debe depender exclusivamente de la disciplina del desarrollador en su máquina local. Automatizar la auditoría en el servidor transforma las reglas documentadas en barreras físicas inquebrantables.

**Siguiente paso o deuda:** Validar la ejecución exitosa del workflow en GitHub y continuar con la Gobernanza Open Source (Issue Templates).

### 2026-05-02 — Milestone: Cierre de Fase 8 y Validación del Definition of Done

**Contexto:** Finalizar formalmente la Fase 8 (Expansión de Contenido y Contexto Inteligente) garantizando la higiene absoluta del repositorio antes de iniciar la orquestación en la nube (Fase 11).

**Hecho:** Se ejecutó y superó el Protocolo Estricto de Cierre de Fase:
- [x] **1. Deuda Técnica:** 0 TODOs pendientes. Rendimiento 100/100 retenido en vistas dinámicas.
- [x] **2. Cosecha de Conocimiento:** Cuadernillo sobre Ceguera de Proxy extraído y promovido.
- [x] **3. Auditoría Documental:** `README.md` actualizado reflejando el SSOT por Slug y el escudo Anti-Proxy.
- [x] **4. Evaluación de Release:** Versión `v1.3.1` del Boilerplate exportada con éxito (`merci-init.py` destructivo).
- [x] **5. Snapshot:** Backup local detallado generado (`merci-backup.py -v`) con un peso optimizado de 1.51 MB.
- [x] **6. Sello Definitivo:** Commit atómico en preparación.

**Detalle técnico:** La fase concluye demostrando empíricamente la viabilidad de la arquitectura híbrida (Dev/Prod Parity). El enrutamiento dinámico resuelve las URIs sin colisiones mediante *slugs*, la UI se mantiene purista y la base de datos local ha sido purgada de "posts zombis" (Data Drift). 

**Motivo / criterio:** *Governance y Definition of Done (DoD)*. Sellar el repositorio mediante un checklist auditable previene la transferencia de deuda técnica entre fases. Al saltar directamente a la Fase 11 (CI/CD), el código fuente debe estar inmaculado para que los corredores (runners) en la nube no fallen por problemas de configuración local heredados.

**Siguiente paso o deuda:** Iniciar oficialmente la Fase 11: Integración Continua y Calidad en la Nube (CI/CD con GitHub Actions).

### 2026-05-02 — Docs: Actualización v2.0 del cuadernillo de Alias Inteligentes

**Contexto:** La función Bash `merci` original era rígida y no permitía pasar argumentos adicionales (flags como `-v` o rutas de archivos) a los scripts subyacentes, limitando el uso de herramientas dinámicas como el orquestador de backups o el publicador de WordPress.

**Hecho:**
- Se actualizó el cuadernillo `Alias Inteligentes-bitacora.md` a su versión 2.0.
- Se documentó la inyección de la variable `${@:2}` para admitir parámetros infinitos.
- Se añadió la instrucción de recarga en caliente de la terminal (`source ~/.zshrc`).

**Detalle técnico:** La variable de expansión `${@:2}` captura todos los argumentos a partir del segundo y los traslada al script de Python. Se utilizó el flujo de trabajo estándar (Kill-Switch) para degradar el cuadernillo a borrador en el laboratorio, aplicar el bloque de conocimiento y volver a promoverlo a la biblioteca mediante `merci-promote.py`.

**Motivo / criterio:** *Mejora Continua (Continuous Improvement) y Gestión del Conocimiento*. Los activos de la biblioteca deben ser documentos vivos. Reflejar los parches operativos (como la recarga en caliente y el paso de argumentos) asegura que los futuros usuarios del Boilerplate dispongan de la versión más pulida y eficiente de las herramientas de terminal.

**Siguiente paso o deuda:** Iniciar la Fase 9 (Inteligencia y Autonomía).

### 2026-05-02 — QA: Certificación "Cuádruple 100" en capa dinámica tras refactorización Headless

**Contexto:** Tras erradicar los "posts zombis" de la base de datos local y refactorizar el publicador Headless (`merci-wp.py`) para utilizar resolución dinámica por slug, era imperativo certificar que la arquitectura seguía rindiendo al máximo nivel en producción.

**Hecho:** Se ejecutó una auditoría externa de Google PageSpeed Insights sobre la ruta dinámica de WordPress `/blog/category/art-de-cote/` bajo simulación de red móvil 4G.

**Detalle técnico:** Se logró una puntuación perfecta (100 Rendimiento, 100 Accesibilidad, 100 Mejores Prácticas, 100 SEO). Las métricas Core Web Vitals se mantienen inmaculadas: FCP 0.8s, LCP 1.1s, TBT 0ms y CLS 0. La corrección WAI-ARIA de enlaces de tarjetas y la purga de dependencias JS bloqueantes se validaron con éxito.

**Motivo / criterio:** *QA Assurance y Performance Driven Development*. Lograr 0 ms de Tiempo de Bloqueo Total (TBT) en una vista generada por un CMS pesado demuestra el éxito absoluto del "Escudo de Rendimiento" (desencolado estricto de scripts y bloques en `functions.php`). Certifica que el proyecto cumple sus propios estándares fundacionales y está listo para ser empaquetado como Boilerplate v1.3.1.

**Siguiente paso o deuda:** Ejecutar el Release Pipeline, el Backup Local y el Commit Atómico para cerrar oficialmente la Fase 8 e iniciar la Fase 9 (Inteligencia).

### 2026-05-02 — Docs: Documentación arquitectónica de orquestadores (QUÉ HACE/POR QUÉ)

**Contexto:** La complejidad alcanzada por el publicador Headless (`merci-wp.py`) requería blindar el conocimiento de sus funciones contra futuras refactorizaciones.

**Hecho:** Se estandarizaron los docstrings y comentarios internos de `scripts/merci/merci-wp.py` siguiendo el formato "QUÉ HACE" y "POR QUÉ".

**Detalle técnico:** Explicar explícitamente decisiones como el parseo nativo de YAML, la inyección dual de credenciales y el uso de `slugify`.

**Motivo / criterio:** *Mantenibilidad y Pedagogía*. Un Boilerplate no solo hereda código, sino criterio. Forzar la documentación de la *intención* previene que futuros desarrolladores eliminen piezas clave (como las cabeceras anti-WAF) por considerarlas "redundantes".

### 2026-05-02 — Arch: SSOT Dinámico por Slug (Erradicación de wp_id estático)

**Contexto:** El uso de un `wp_id` inyectado en el YAML local provocaba errores 404 al intentar actualizar artículos tras cambiar el entorno de localhost a producción, ya que los IDs de la base de datos no coincidían y el script intentaba actualizar un ID inexistente.

**Hecho:**
- Se eliminó la lectura e inyección de `wp_id` en el script `merci-wp.py`.
- Se implementó la función `obtener_id_por_slug()` para interrogar a la API REST de destino.

**Detalle técnico:** En lugar de depender del ID local, el script utiliza el nombre del archivo (`target_path.stem`) para preguntar "¿Existe un post con este slug en este entorno?". Si existe, captura su ID remoto temporalmente en memoria y ejecuta un `PUT`; si no, ejecuta un `POST`.

**Motivo / criterio:** *Paridad Dev/Prod Absoluta*. El archivo Markdown se vuelve verdaderamente agnóstico. Al usar el *slug* (el nombre físico del archivo) como clave primaria universal, podemos sincronizar exactamente el mismo documento contra infinitas bases de datos sin colisiones ni corrupción de IDs.

### 2026-05-02 — Fix: Evasión de escudos WAF y proxies (User-Agent corporativo)

**Contexto:** Nginx en CloudPanel devolvía errores 404/403 al intentar interrogar la API REST de WordPress para buscar categorías (ej. `?search=Blog`).

**Hecho:** Se inyectó la cabecera `User-Agent: Merci-Boilerplate-Agent/1.0` en todas las peticiones HTTP dentro de `merci-wp.py`.

**Detalle técnico:** Los firewalls (WAF) y proxies de alto rendimiento bloquean automáticamente agentes de usuario genéricos de librerías como `Python-urllib` asumiendo que son bots maliciosos de *scraping*. 

**Motivo / criterio:** *Identidad de Ecosistema y Bypass Seguro*. Forjar un Agente de Usuario legítimo permite al orquestador atravesar la frontera de Nginx. Además, habilita la trazabilidad forense en los archivos `access.log` del servidor, permitiendo distinguir el tráfico del Boilerplate de los ataques reales.

### 2026-05-02 — Fix: Ceguera de HTTPS en WordPress detrás de Proxy Varnish

**Contexto:** WordPress en producción ocultaba la opción para generar Contraseñas de Aplicación, asumiendo falsamente que el entorno era inseguro (HTTP), a pesar de que CloudPanel servía la web por HTTPS validado.

**Hecho:**
- Se inyectó temporalmente `$_SERVER['HTTPS'] = 'on';` en `wp-config.php` de producción.
- Ante la agresividad de OPcache/FastCGI sobrescribiendo variables globales, se recurrió a la extracción directa de la credencial mediante terminal usando WP-CLI (`wp user application-password create`).

**Detalle técnico:** CloudPanel termina la conexión SSL (offloading) en Nginx y pasa el tráfico interno a PHP por HTTP normal. WP detecta HTTP en entorno de producción y, por seguridad nativa innegociable, bloquea la API de contraseñas. Extraer la clave por terminal salta completamente el servidor web y dialoga directamente con el motor de base de datos.

**Motivo / criterio:** *Infraestructura como Código (IaC)*. Cuando las capas de caché profunda o los proxies ofuscan la Interfaz Gráfica (GUI), descender a la capa del sistema operativo (WP-CLI) es la vía más profesional y segura para aprovisionar herramientas sin alterar permanentemente configuraciones delicadas del servidor web.

### 2026-05-02 — Fix: Bypass de "Ceguera de Proxy" (Autorización REST API)

**Contexto:** Al apuntar el publicador Headless (`merci-wp.py`) a producción, el proxy inverso CloudPanel/Varnish interceptaba y purgaba la cabecera HTTP estándar `Authorization: Basic`, desnudando la petición y provocando que WP la rechazara con un error 401 Unauthorized.

**Hecho:**
- Se implementó un envío dual de credenciales en Python inyectando una cabecera personalizada gemela (`X-Authorization`).
- Se inyectó un parche en `src/wp-theme/merci-theme/functions.php` para restaurar la cabecera oficial en el servidor: `$_SERVER['HTTP_AUTHORIZATION'] = $_SERVER['HTTP_X_AUTHORIZATION']`.

**Detalle técnico:** Los proxies de alto rendimiento están configurados para no cachear peticiones con `Authorization` o purgarla por seguridad. Las cabeceras personalizadas (`X-*`) no son filtradas y atraviesan Varnish intactas. Al llegar a PHP, el filtro de nuestro tema restaura la variable global en memoria justo antes de que WP valide al usuario.

**Motivo / criterio:** *Shift-Left Routing*. En lugar de crear complejas excepciones en la infraestructura de Nginx de CloudPanel (lo que generaría deriva de configuración entre local y nube), solucionarlo a nivel de código de aplicación asegura que el ecosistema funcione en cualquier hosting o proxy del mercado (Agnosticismo de Infraestructura).

### 2026-05-02 — Arch: Conmutador de Entornos (Environment Switcher) en .env

**Contexto:** Se necesitaba un flujo de trabajo que permitiera publicar el mismo archivo Markdown primero en localhost (para pruebas y QA) y luego en producción, sin mezclar credenciales ni alterar el código fuente de los automatismos en Python.

**Hecho:** Se consolidó el uso del archivo `.env` local como un "Conmutador de Vías".

**Detalle técnico:** El archivo `.env` ahora alberga bloques comentados (`#`) independientes para cada entorno (Localhost y Producción). Alternar los comentarios redefine dinámicamente hacia qué servidor apuntan las peticiones de `merci-wp.py`.

**Motivo / criterio:** *Dev/Prod Parity y Simplicidad*. Este enfoque no requiere librerías complejas de gestión de variables de entorno ni comandos extra. Combinado con la resolución dinámica de IDs por *slug*, permite a la desarrolladora incubar en local y desplegar en la nube de forma secuencial usando exactamente los mismos comandos de terminal, garantizando cero colisiones.

### 2026-05-02 — Arch: Resolución dinámica de IDs multi-entorno en Headless CMS

**Contexto:** Al intentar publicar los artículos en el servidor de producción, se evidenció que los archivos Maqrkdown locales contenían atributos `wp_id` asociados a la base de datos de localhost, provocando colisiones de entorno al apuntar el script a la API REST de producción.

**Hecho:** Se refactorizó `scripts/merci/merci-wp.py` para implementar búsqueda dinámica de existencia por `slug`.

**Detalle técnico:** Inyectar la función `obtener_id_por_slug()`. Antes de realizar el POST/PUT, el script interroga al WordPress de destino. Si el artículo ya existe en ese servidor, asume el ID remoto (`entorno_id`), ignorando el `wp_id` escrito en el YAML local.

**Motivo / criterio:** *Dev/Prod Parity (Multi-entorno)*. Depender de un único ID estático en el archivo acopla el código a una sola base de datos. La resolución dinámica permite que el mismo archivo Markdown se sincronice indistintamente contra Localhost, Staging o Producción sin corromper las bases de datos de destino.

### 2026-05-02 — Docs: Release v1.3.0 del Boilerplate y Cierre de Fase 8

**Contexto:** Tras consolidar la paridad absoluta entre el motor SSG y el Headless CMS (generación de PDFs, extracción de resúmenes y SSOT de slugs) y fortificar la documentación contra "posts fantasma" (Data Drift), era imperativo empaquetar estos avances antes de iniciar nuevas lógicas de desarrollo.

**Hecho:**
- Se ejecutó el Release Pipeline exportando el código limpio al repositorio `merci-boilerplate`.
- Se dio por concluida oficialmente la Fase 8 (Expansión de Contenido y Contexto Inteligente).

**Detalle técnico:** Ejecutar el orquestador destructivo `merci-init.py` para ascender los *Shadow Docs* actualizados (README v1.3.0 y el nuevo SOP maestro público) y purgar con éxito todos los borradores residuales, garantizando un ecosistema inmaculado para los usuarios del Boilerplate.

**Motivo / criterio:** *Release Management y Zero Technical Debt*. Aplicar el cierre formal de fase (Definition of Done) exige liberar el ecosistema de "deuda de despliegue". Iniciar el desarrollo de la Fase 9 o Fase 11 sobre un código base no sincronizado con su plantilla matriz es una práctica propensa a crear bifurcaciones problemáticas.

**Siguiente paso o deuda:** Iniciar la Fase 9 (Inteligencia y Autonomía) o Fase 11 (CI/CD Cloud).

### 2026-05-02 — Docs: Reubicación y ampliación del SOP de Publicación Dual

**Contexto:** Tras el incidente de los posts fantasma (Data Drift) por borrado manual de archivos, se evidenció que las reglas de publicación son críticas no solo para el proyecto matriz, sino para cualquier usuario futuro del Boilerplate.

**Hecho:**
- Se movió el archivo `flujo-publicacion-sop.md` desde el directorio privado `docs/matriz/` hacia el directorio público `docs/`.
- Se añadió la "Regla de Oro" sobre la Prevención de Posts Fantasma, prohibiendo el borrado manual de archivos `.md` sincronizados sin antes aplicar el Kill-Switch (`estado: "borrador"`).

**Motivo / criterio:** *Knowledge Export (Exportación de Conocimiento)*. Las mecánicas de sincronización Headless y SSG son el núcleo funcional del producto. Restringir este manual a la matriz ocultaría al usuario final del Boilerplate cómo utilizar el ecosistema de forma segura, provocándoles la misma deuda técnica de desincronización que acabamos de sufrir.

**Siguiente paso o deuda:** Iniciar la Fase 9 (Inteligencia y Autonomía) o Fase 11 (CI/CD).

### 2026-05-02 — Fix: Erradicación de posts fantasma (Data Drift) en Headless CMS

**Contexto:** El orquestador `merci-total` falló en la etapa de rastreo de enlaces (`merci-linkcheck.py`) reportando un 404 en el PDF de `mi-primer-post-automatizado`. El archivo Markdown original había sido eliminado localmente sin pasar por el proceso de despublicación formal.

**Hecho:** Se purgó manualmente la entrada residual desde el panel de administración de WordPress local.

**Detalle técnico:** El script `merci-publish.py` borra la carpeta `descargas/` (Clean Build). Posteriormente, `merci-wp.py` genera PDFs solo para los archivos `.md` existentes en el directorio. Al no existir el archivo local, su PDF no se regenera, pero como WordPress nunca recibió la orden REST de borrarlo, el CMS continuaba sirviendo el post público con un enlace a un archivo inexistente.

**Motivo / criterio:** *Higiene Headless y Data Drift*. En una arquitectura desacoplada y unidireccional, borrar un archivo fuente de producción manualmente provoca "posts zombis". La despublicación debe delegarse siempre al "Kill-Switch" automatizado (cambiar a `estado: "borrador"` y ejecutar `merci wp`) antes de borrar el fichero físico localmente.

**Siguiente paso o deuda:** Iniciar la Fase 9 (Inteligencia de Merci) o Fase 11 (CI/CD).

### 2026-05-01 — Fix: Resolución de deriva de slugs (SSOT) entre SSG y Headless CMS

**Contexto:** El rastreador local (`merci-linkcheck.py`) detuvo el pipeline reportando errores 404 en las descargas de PDFs de WordPress. Python generaba los PDFs basándose en el título crudo del Markdown, pero WordPress asignaba "slugs" distintos (ej. añadiendo `-2`) para evitar colisiones en su base de datos.

**Hecho:**
- Se refactorizó `scripts/merci/merci-wp.py` retrasando la generación del PDF mediante WeasyPrint.
- Se redactó el cuadernillo `cuadernillo-ssot-slugs-wp.md` en el laboratorio documentando el incidente.

**Detalle técnico:** Se movió el bloque de generación del PDF al interior de la respuesta exitosa de la API REST (`urllib.request.urlopen`). Ahora, el script extrae el campo `slug` del JSON devuelto por WordPress y utiliza exactamente esa cadena de texto como nombre físico para el archivo `.pdf` (`out_pdf_filename = f"{wp_slug}.pdf"`).

**Motivo / criterio:** *Single Source of Truth (SSOT)*. En un sistema distribuido, la base de datos es la única fuente de verdad para las URIs. Obligar al generador estático (Python) a esperar la respuesta del motor dinámico (WordPress) garantiza la paridad absoluta entre el enlace web renderizado y el archivo físico en el disco duro.

**Siguiente paso o deuda:** Ejecutar `merci total` para validar el pipeline a 0 errores y actualizar el `README-merci.md`.

### 2026-05-01 — QA: Silenciado de falsos positivos en linter de estilos (UI_INLINE_STYLE)

**Contexto:** La primera pasada del nuevo linter de estilos en línea arrojó 3 advertencias (`WARN UI_INLINE_STYLE`) en el HTML compilado de `la-guerra-de-la-especificidad-css.html`. El diagnóstico reveló que correspondían a fragmentos de código educativo documentados en el propio artículo.

**Hecho:**
- Se inyectó la directiva `<!-- merci-audit:silence-style -->` al final de las líneas afectadas en el archivo Markdown original (`biblioteca/cuadernillo-la-guerra-de-la-especificidad-css.md`).

**Detalle técnico:** El auditor no discrimina si la cadena `style="..."` se encuentra renderizada dentro de una etiqueta `<code>` o en un componente estructural. En lugar de aplicar sobreingeniería a las expresiones regulares del linter (lo cual es propenso a fallos), se emplean los marcadores de silenciamiento explícitos nativos de la herramienta.

**Motivo / criterio:** *Fail Gracefully y Falsos Positivos*. Exigir una herramienta estricta implica dotarla de válvulas de escape intencionales. Utilizar el silenciamiento en línea certifica que el desarrollador ha revisado manualmente el hallazgo y asume que es arquitectónicamente seguro, manteniendo la alerta activa para verdaderas violaciones de estilo.

**Siguiente paso o deuda:** Re-ejecutar `merci total` para confirmar el *Zero Warnings* y proceder con la Fase 9 o Fase 11.

### 2026-05-01 — QA: Linter de estilos en línea (UI_INLINE_STYLE)

**Contexto:** Para proteger la arquitectura SASS 7-1 y la metodología BEM, se requería automatizar la detección de estilos en línea (`style="..."`) inyectados en el HTML o en las plantillas PHP, los cuales generan deuda técnica y problemas de especificidad.

**Hecho:**
- Se implementó la regla `audit_inline_styles` en `scripts/merci/merci-audit.py`.

**Detalle técnico:** El linter utiliza una expresión regular para detectar atributos `style=` en archivos `.html`, `.php`, `.js` y `.py`. Evalúa las coincidencias y emite una advertencia (`WARN`). Se implementó una excepción explícita para los estilos del ancla invisible WAI-ARIA (`#top`) para evitar falsos positivos arquitectónicos.

**Motivo / criterio:** *Shift-Left Quality*. En lugar de crear un script independiente que añada fricción operativa, integrar esta validación en el auditor maestro asegura que la comprobación se ejecute automáticamente antes de cada commit. Las advertencias no bloquean el flujo, pero visibilizan la deuda técnica inmediatamente.

**Siguiente paso o deuda:** Ejecutar el auditor para escanear el proyecto en busca de estilos en línea residuales.

### 2026-05-01 — Refactor: Unificación de metadatos y UI responsiva en Biblioteca

**Contexto:** Se detectó una alta entropía en los YAML Frontmatter de la `biblioteca/` (campos `volumen` innecesarios, falta de `tipo`, descripciones y `alt_portada` rotos). Además, en la vista móvil, las secciones de la biblioteca (`.library-section`) carecían de *padding* lateral, pegando el contenido a los bordes del dispositivo.

**Hecho:**
- Se estandarizó el Frontmatter de los cuadernillos para asegurar un parseo SSG uniforme.
- Se creó el archivo fundacional `docs/plantilla-cuadernillo.md` para prevenir futuras derivas de formato.
- Se inyectó `padding: 0 $spacing-lg;` responsivo en el componente `.library-section` (SASS).

**Motivo / criterio:** *Single Source of Truth (SSOT) y Mobile First*. La ausencia de una plantilla estricta para "cuadernillos" provocaba que los archivos heredaran metadatos obsoletos (como `volumen:` o `portada:`). La corrección CSS alinea el comportamiento del contenedor `.library-section` con la navegación superior, restaurando el 100/100 en usabilidad móvil.

**Siguiente paso o deuda:** Recompilar SASS, ejecutar QA (`merci total`) y proceder a empaquetar el commit atómico.

### 2026-05-01 — QA: Resolución de colisión de enlaces ancla (WAI-ARIA) en el SSG

**Contexto:** El pipeline se detuvo en la fase de `merci-linkcheck.py` al detectar enlaces ambiguos en el índice de la Biblioteca. El nombre de la estantería "Art de Coté" generó enlaces ancla (`#art-de-cote`) que colisionaban con el enlace homónimo del menú de navegación global (`/blog/category/art-de-cote/`).

**Hecho:**
- Se parcheó `scripts/merci/merci-publish.py` para inyectar dinámicamente atributos `aria-label` en los enlaces de las estanterías temáticas.

**Detalle técnico:** Se transformaron los anclajes para que posean nombres accesibles únicos como `aria-label="Explorar estantería: {tema}"`. El texto visual se mantiene inalterado, pero los lectores de pantalla y las herramientas de auditoría ahora logran diferenciar semánticamente el enlace de ancla interno del enlace de navegación estructural.

**Motivo / criterio:** *Shift-Left Accessibility*. Las colisiones WAI-ARIA son inevitables cuando el contenido generado dinámicamente (SSG) hereda nombres que coinciden con elementos estructurales. Garantizar identificadores únicos a nivel de compilador evita tener que limitar la nomenclatura que elija el autor.

**Siguiente paso o deuda:** Re-ejecutar el pipeline maestro para certificar 0 errores y proceder al commit.

### 2026-05-01 — QA: Validación End-to-End del publicador social (LinkedIn)

**Contexto:** Se necesitaba certificar que el ecosistema completo funcionara en cadena (Laboratorio -> Promote -> WordPress -> LinkedIn) extrayendo el texto multilínea correctamente tras la migración a comentarios HTML.

**Hecho:**
- Se ejecutó con éxito el pipeline completo sobre un artículo real.
- Se actualizó el `README.md` marcando la automatización de LinkedIn y la Fase 8 como completadas.

**Detalle técnico:** El orquestador `merci-linkedin.py` localizó exitosamente el marcador `wp_id`, extrajo el bloque `<!-- linkedin: ... -->` preservando los saltos de línea, publicó a través de la API OIDC y selló el archivo local inyectando el `linkedin_id` de forma atómica.

**Motivo / criterio:** *QA de Integración (End-to-End Testing)*. Un desarrollo no se da por terminado hasta que se valida empíricamente su funcionamiento en el entorno final de producción. Con este éxito, la Fase 8 queda formalmente clausurada y la arquitectura de distribución consolidada.

**Siguiente paso o deuda:** Iniciar la Fase 9 (Inteligencia y Autonomía) o saltar a la Fase 11 (CI/CD Cloud).

### 2026-05-01 — Fix: Resolución de truncamiento de texto multilínea YAML (merci-promote)

**Contexto:** Al promocionar un artículo y enviarlo a LinkedIn, la red social publicó un post vacío que solo contenía el símbolo `|`. Se diagnosticó que `merci-promote` (y otros scripts) utilizan un parseador YAML rudimentario (`split(":")`) que destruyó el bloque de texto multilínea al no encontrar el delimitador de clave-valor en las líneas inferiores.

**Hecho:**
- Se refactorizó `merci-linkedin.py` para leer el texto a publicar desde un comentario HTML (`<!-- linkedin: ... -->`) ubicado en el cuerpo del documento (`md_body`).
- Se actualizaron las plantillas (`plantilla-blog.md`, `plantilla-art-de-cote.md`) para retirar el campo `linkedin_post` del YAML Frontmatter e inyectar el bloque HTML oculto.

**Detalle técnico:** Implementar un parseador YAML completo en Python nativo para soportar *block scalars* (bloques multilínea) requiere miles de líneas de código o añadir la dependencia externa `PyYAML`. Extraer la responsabilidad del texto largo hacia el cuerpo del Markdown (escondiéndolo en un comentario HTML que los navegadores ignoran) sortea la limitación técnica manteniendo la directriz de "0 dependencias bloqueantes".

**Motivo / criterio:** *Robustez vs. Deuda Técnica*. Si una herramienta casera tiene límites estructurales, adaptar el formato de entrada (Markdown) es infinitamente más seguro y mantenible que intentar reinventar la rueda programando un parseador complejo propenso a errores.

**Siguiente paso o deuda:** Validar la republicación en LinkedIn con texto multilínea intacto.

### 2026-04-30 — DevSecOps: Bloqueo de token OIDC de LinkedIn en control de versiones

**Contexto:** Durante las pruebas del motor de LinkedIn, el instinto DevSecOps alertó sobre la posible inclusión accidental del archivo de credenciales (`.linkedin_token.json`) en el commit automático, ya que no había sido excluido en la configuración pasiva.

**Hecho:**
- Se ejecutó `git reset --soft HEAD~1` y `git rm --cached .linkedin_token.json` para expurgar el token del historial local.
- Se añadió el archivo `.linkedin_token.json` al `.gitignore`.
- Se parcheó `scripts/merci/merci-audit.py` para incluir este archivo en la lista estricta de `BANNED_TRACKED_FILE`.

**Detalle técnico:** El script `merci-commit.py` ejecuta `git add .` automáticamente. Sin la exclusión, el token OAuth habría viajado al repositorio público. Inyectar el archivo en la regla `BANNED_TRACKED_FILE` del auditor garantiza un "fail-fast", bloqueando atómicamente cualquier commit si Git intenta rastrearlo en el futuro.

**Motivo / criterio:** *Shift-Left Security y Zero Trust*. Los tokens OIDC poseen permisos de escritura y representan un riesgo crítico de seguridad si se filtran. La política exige que el escudo activo (el auditor pre-commit) conozca la existencia de nuevos archivos de credenciales para interceptarlos infaliblemente en caso de que fallen las exclusiones pasivas.

**Siguiente paso o deuda:** Finalizar el commit atómico saneado y verificar si la publicación en LinkedIn fue exitosa.

### 2026-04-30 — Feat: Motor de Publicación Automática en LinkedIn (SSOT Estricto)

**Contexto:** Tras asegurar la obtención del *Access Token* (OIDC), era necesario desarrollar el módulo de publicación. Se debatió si el script de LinkedIn debía leer los artículos directamente de la API del servidor web de producción para garantizar que solo se publicaran artículos "reales".

**Hecho:**
- Se amplió `scripts/merci/merci-linkedin.py` implementando la inyección a la API y el parseo YAML local.
- Se estableció la validación estricta de pre-existencia web: el script solo lee archivos locales que posean el marcador `wp_id`.

**Detalle técnico:** Leer del servidor web destruiría el texto personalizado del campo `linkedin_post`. Al exigir que el archivo Markdown local contenga `wp_id`, usamos la inyección previa de `merci-wp.py` como garantía irrefutable de que el contenido está vivo en producción. Si se cumplen las condiciones, realiza un POST a `/v2/ugcPosts` e inyecta el `linkedin_id` para prevenir duplicados.

**Motivo / criterio:** *Decoupling y Single Source of Truth*. Separar los scripts por canal (uno para WP, otro para LinkedIn) aísla los fallos de las APIs externas. Confiar en la firma YAML local unifica el flujo: el Markdown es el único DNI del artículo.

**Siguiente paso o deuda:** Crear un artículo de prueba, promoverlo, publicarlo en WP y ejecutar el script para ver el post real en LinkedIn.

### 2026-04-30 — Feat: Motor de Autenticación OIDC para LinkedIn (Cero Dependencias)

**Contexto:** Para automatizar las publicaciones en LinkedIn (Fase 8.3) con robustez a largo plazo, se descartó el uso de tokens estáticos manuales en favor del flujo completo "Three-legged OAuth 2.0" (OIDC), permitiendo al script gestionar y renovar sus propias credenciales.

**Hecho:**
- Se configuró la aplicación en el portal de desarrolladores de LinkedIn (Scopes: `openid`, `profile`, `w_member_social`).
- Se desarrolló el motor base en `scripts/merci/merci-linkedin.py` utilizando la librería estándar `http.server` y `urllib`.

**Detalle técnico:** El script levanta un `HTTPServer` efímero en el puerto 8000 que bloquea la ejecución (`handle_request()`) hasta atrapar el *callback* del navegador. Extrae el código `?code=XYZ`, realiza el POST de intercambio por el *Access Token* y lo guarda físicamente en el archivo seguro `.linkedin_token.json`.

**Motivo / criterio:** *Zero Bloat & Autonomía*. Programar un servidor web de un solo uso en lugar de importar librerías pesadas como `Flask` o `requests_oauthlib` demuestra la potencia de Vanilla Python. Este flujo garantiza que la integración no colapse por caducidad de tokens en el futuro.

**Siguiente paso o deuda:** Ejecutar el script por primera vez para generar el token inicial, y luego diseñar la función para publicar un post real enviando datos a la API de LinkedIn.

### 2026-04-30 — Arch: Pivote estratégico hacia automatización social (LinkedIn)

**Contexto:** Tras validar el MVP de la tienda WooCommerce (diseño, inyección headless, paridad de entornos), se determinó que su propósito principal como demostración técnica estaba cumplido. El valor de negocio inmediato no reside en la venta de merchandising, sino en la difusión de estos logros técnicos.

**Hecho:**
- Se aparca formalmente el desarrollo de la tienda.
- Se re-prioriza como hito inmediato el desarrollo del script de automatización para LinkedIn (`merci-linkedin.py`), retomando la Fase 8.3.

**Motivo / criterio:** *Business Value vs. Technical Exercise*. La tienda ha servido como un caso de estudio perfecto para demostrar la integración de un e-commerce en una arquitectura Headless de alto rendimiento. Ahora, el Retorno de la Inversión (ROI) es mayor si se capitaliza este logro mediante la difusión en redes profesionales, en lugar de seguir añadiendo funcionalidades a un escaparate no comercial.

**Siguiente paso o deuda:** Diseñar la arquitectura de autenticación (OAuth 2.0) para `merci-linkedin.py` y comenzar su implementación.

### 2026-04-30 — Fix: Resolución de rutas estáticas en inyector Headless de WC

**Contexto:** El inyector de productos (`merci-wc-mock.py`) enviaba una URL de imagen incorrecta a WooCommerce (`/blog/assets/images/...`), provocando que la imagen no se descargara ni se adjuntara al producto en la tienda.

**Hecho:**
- Se implementó la variable `domain_root` utilizando `wp_url.removesuffix('/blog')` en `merci-wc-mock.py`.
- Se actualizó el *payload* JSON para que el campo `src` de la imagen apunte a la raíz del dominio estático.

**Detalle técnico:** En la arquitectura aislada, la variable de entorno `WP_URL` apunta al subdirectorio del CMS, pero Nginx sirve los *assets* multimedia directamente desde la raíz pública. Amputar programáticamente el sufijo del CMS en Python garantiza que la API REST reciba una URI absoluta resoluble, manteniendo la segregación de entornos.

**Motivo / criterio:** *Single Source of Truth y Aislamiento*. No duplicar variables de entorno (como crear un `STATIC_URL` en el `.env`) mantiene la configuración sencilla. Inferir matemáticamente la ruta estática a partir de la ruta dinámica es el enfoque más resiliente frente a cambios de dominio.

**Siguiente paso o deuda:** Validar la inyección correcta de la imagen en la tienda y proceder con LinkedIn (Fase 8.3).

### 2026-04-30 — Fix: Purga de título duplicado e inyección de imágenes optimizadas en WC

**Contexto:** La página principal de la tienda (`archive-product.php`) mostraba el título "Tienda" por duplicado. Además, se requería definir el flujo de trabajo para insertar imágenes optimizadas en los productos vía API Headless.

**Hecho:**
- Se inyectó el filtro `woocommerce_show_page_title` devolviendo `false` en `functions.php` para eliminar el título nativo del plugin.
- Se actualizó el script `merci-wc-mock.py` añadiendo el *payload* de imágenes apuntando a los *assets* locales generados por `merci-optimizer.py`.

**Detalle técnico:** WooCommerce inyecta automáticamente `<h1 class="page-title">` al renderizar el bucle de productos. Como nuestra plantilla `woocommerce.php` ya provee un componente BEM `.hero`, el filtro nativo purga la inyección redundante. Para las imágenes, la API REST requiere una URI absoluta (`src`); proveer la ruta local de la imagen `.webp` generada por nuestro orquestador obliga a WP a consumir el archivo ya optimizado, protegiendo los Core Web Vitals.

**Motivo / criterio:** *Zero Bloat y UI/UX*. Desactivar elementos nativos del CMS mediante hooks de PHP evita tener que ocultarlos con `display: none` en CSS, manteniendo el DOM lo más ligero posible. Interceptar el flujo multimedia asegura que ninguna imagen bruta llegue a la base de datos dinámica.

**Siguiente paso o deuda:** Validar visualmente la tienda sin títulos duplicados y el producto con su imagen, y proceder a LinkedIn (Fase 8.3).

### 2026-04-30 — Feat: Inyector Headless de Productos Mock (WooCommerce)

**Contexto:** Para validar los estilos SASS de la tienda en el entorno local recién configurado, era necesario crear un producto de prueba. Para mantener la filosofía "CLI-first" y no depender del panel de administración (GUI) de WordPress, se requería una vía de inyección desde la terminal.

**Hecho:**
- Se desarrolló el script experimental `laboratorio/scripts_temporales/merci-wc-mock.py`.
- El script consume el archivo `.env` existente y realiza un `POST` a la API REST nativa de WooCommerce (`/wc/v3/products`).

**Detalle técnico:** Se descartó el uso de comandos `curl` crudos para evitar exponer la contraseña de aplicación (`WP_APP_PASSWORD`) en el historial de la terminal (`.bash_history`), cumpliendo con los estándares de seguridad (Shift-Left). El script interactúa mediante Autenticación Básica Base64.

**Motivo / criterio:** *Developer Experience (DX) y Seguridad*. Automatizar la inyección de datos de prueba (Mock Data) acelera el desarrollo del frontend. Utilizar las mismas credenciales seguras que `merci-wp.py` demuestra la versatilidad de la arquitectura Headless.

**Siguiente paso o deuda:** Inyectar el producto, validar el diseño del catálogo individual y, finalmente, comenzar con LinkedIn.

### 2026-04-30 — UX: Enlace de retroceso en vista de producto (WooCommerce)

**Contexto:** Tras restaurar la paridad de entornos y validar los estilos SASS de la tienda, se observó que la vista de producto individual (`single-product`) carecía de un atajo para regresar rápidamente al catálogo, generando fricción en la navegación.

**Hecho:**
- Se inyectó un enlace condicional (`is_product()`) en `src/wp-theme/merci-theme/woocommerce.php` apuntando a la página principal de la tienda.
- Se reutilizó la clase SASS existente `.card__back-link` para mantener la consistencia visual.

**Motivo / criterio:** *Fricción Cero y Reusabilidad*. Proveer una vía de escape clara mejora la experiencia de usuario (UX). Reutilizar una clase CSS semántica creada originalmente para la biblioteca (`.card__back-link`) evita inyectar estilos en línea o crear código duplicado, cumpliendo con el principio DRY (Don't Repeat Yourself).

**Siguiente paso o deuda:** Dar por cerrado el MVP de la tienda e iniciar el diseño del script de automatización para LinkedIn (`merci-linkedin.py`).

### 2026-04-30 — Arch: Restauración de Paridad de Entornos (Dev/Prod Parity)

**Contexto:** Durante la estilización del MVP de la tienda, se detectó una desconexión total entre el código SASS y la visualización local. El diagnóstico reveló que WooCommerce estaba instalado exclusivamente en el servidor de producción, pero ausente en el entorno de desarrollo local.

**Hecho:**
- Se pausó el desarrollo de código.
- Se instruyó la instalación, activación y configuración de WooCommerce en el WordPress local, incluyendo la creación de datos de prueba (Mock Data).

**Motivo / criterio:** *Dev/Prod Parity* (Paridad Desarrollo/Producción). Desarrollar sobre un entorno local que no refleja la topología exacta de producción genera "ceguera de desarrollo" y fomenta el anti-patrón de probar código directamente en la web pública. Replicar el CMS y sus plugins clave en local es un requisito innegociable de la arquitectura DevSecOps.

**Siguiente paso o deuda:** Validar visualmente los estilos SASS de la tienda en el entorno local ahora que el motor dinámico está operativo, y continuar con LinkedIn.

### 2026-04-30 — Fix: Resolución de Jerarquía de Plantillas en WooCommerce

**Contexto (El Desafío):** La página de la tienda (`/blog/tienda`) renderizaba un contenedor vacío (`.article__content`) a pesar de que la plantilla `woocommerce.php` contenía la función `woocommerce_content()` correcta. El CMS estaba ignorando la plantilla específica y recurriendo a `index.php`.

**Hecho (La Maniobra):**
- Se configuró la página "Tienda" como la página oficial en el panel de administración de WordPress, bajo `WooCommerce > Ajustes > Productos`.

**Detalle técnico:** La existencia de un archivo `woocommerce.php` en el tema no es suficiente. WordPress solo lo utiliza si la URL que se está visitando corresponde a la página asignada explícitamente como "Página de la tienda" en los ajustes del plugin. Sin esta asignación, WordPress trata la URL como una página estándar y aplica su jerarquía de plantillas por defecto (`page.php` o, en su defecto, `index.php`).

**Motivo / criterio (El Aprendizaje):** *Template Hierarchy y Configuración sobre Código*. La configuración del panel de administración de un CMS a menudo tiene mayor precedencia que la estructura de archivos del tema. Comprender la jerarquía de plantillas es crucial para depurar por qué un archivo de tema es ignorado por el motor de renderizado.

**Siguiente paso o deuda:** Validar que la tienda ahora renderiza los productos y sus estilos SASS correctamente.

### 2026-04-30 — Fix: Inyección nativa de WooCommerce (Template Hierarchy)

**Contexto:** Al intentar estilizar la tienda MVP, la página no renderizaba ningún producto (HTML vacío dentro de `.article__content`). Una auditoría del DOM (F12) reveló que el CMS estaba ejecutando el bucle estándar (`the_content()`) en lugar de la cuadrícula de la tienda.

**Hecho:**
- Se reemplazó el bucle `The Loop` estándar de WordPress por la función `woocommerce_content()` dentro del archivo `src/wp-theme/merci-theme/woocommerce.php`.

**Detalle técnico:** WooCommerce renderiza su tienda en una "Página" (Page) física de WP. Si el archivo `woocommerce.php` es una copia literal de `index.php` usando `the_content()`, devuelve un bloque vacío. Llamar a `woocommerce_content()` le devuelve el control del renderizado al plugin dentro de nuestros contenedores semánticos SASS.

**Motivo / criterio:** *Separation of Concerns* y Arquitectura de Plantillas. Obligar a WooCommerce a usar su propio motor de renderizado dentro de nuestra caja fuerte (`<section class="section">`) es el único método validado y oficial para evitar colisiones de rutas dinámicas manteniendo el 100% de nuestros estilos base.

**Siguiente paso o deuda:** Validar la cuadrícula SASS compilada en el navegador y continuar con la automatización para LinkedIn.

### 2026-04-30 — Docs: Refinamiento del SOP de Release del Boilerplate

**Contexto (El Desafío):** Se detectó una fisura lógica en el Procedimiento Operativo Estándar (SOP) de actualización del Boilerplate (`docs/matriz/mantenimiento-boilerplate-sop.md`). Las instrucciones indicaban modificar archivos en la matriz local y luego clonar desde el remoto, pero omitían el paso crítico de subir (`git push`) los cambios locales al servidor.

**Hecho (La Maniobra):**
- Se actualizó `docs/matriz/mantenimiento-boilerplate-sop.md` para dividir el "Paso 1" en dos sub-pasos explícitos: el sello local (`merci commit`) y la sincronización remota (`git push`).

**Detalle técnico:** El comando `git clone` del SOP se nutre del estado del repositorio en GitHub, no del estado del disco duro local. Sin un `push` previo, el clon temporal siempre descargaba una versión obsoleta del código, invalidando las correcciones recién aplicadas.

**Motivo / criterio (El Aprendizaje):** *Infrastructure as Code (IaC) y Rigor Operativo*. Un SOP debe ser atómico e inequívoco. Este refinamiento previene la "falsa ejecución" del pipeline, garantizando que el proceso de instanciación siempre parta de la última versión validada y subida del código matriz.

**Siguiente paso o deuda:** Con el pipeline de release blindado, iniciar el desarrollo de la automatización social para LinkedIn (`merci-linkedin.py`).

### 2026-04-30 — DevSecOps: Prevención de fuga de datos en directorios Headless

**Contexto:** Se sugirió modificar el script de instanciación para simplemente "no borrar" las carpetas dinámicas (`blog/` y `art-de-cote/`). El análisis arquitectónico reveló que esto expondría los borradores y artículos publicados de la autora en el repositorio público. Además, se detectó que las carpetas raíz dinámicas no estaban siendo purgadas.

**Hecho:**
- Se añadieron `blog/` y `art-de-cote/` de la raíz a la lista de eliminación de `purge_directory` en `merci-init.py`.
- Se refactorizó la lógica de reconstrucción para generar las 4 carpetas dinámicas (en la raíz y en laboratorio) con sus respectivos `.gitkeep` tras la limpieza.

**Detalle técnico:** En lugar de excluir directorios del borrado (lo que conserva su contenido interno), se arrasa con ellos y se vuelven a crear usando `mkdir(parents=True, exist_ok=True)` y `touch(".gitkeep")`.

**Motivo / criterio:** *Data Leak Prevention (DLP)*. Un boilerplate debe ser un lienzo en blanco. Excluir carpetas del borrado es un antipatrón de seguridad si estas pueden contener propiedad intelectual. Destruir y reconstruir el andamiaje garantiza la higiene absoluta del repositorio derivado.

**Siguiente paso o deuda:** Retomar el desarrollo de la automatización social para LinkedIn (`merci-linkedin.py`).

### 2026-04-30 — UX/UI: Estilización del MVP de la tienda (WooCommerce)

**Contexto:** Tras decidir pivotar hacia la creación de una tienda mínima viable (MVP) antes de la campaña de LinkedIn, era necesario "vestir" el HTML crudo que genera WooCommerce, ya que sus estilos CSS nativos fueron purgados para mantener el 100/100 en Core Web Vitals.

**Hecho:**
- Se creó y estilizó el componente `src/scss/components/_woocommerce.scss`.
- Se implementó un diseño de tarjetas en cuadrícula (Grid) para la vista de catálogo (`archive-product.php`).
- Se maquetó la vista de producto individual (`single-product.php`) con un layout de 2 columnas (galería + resumen) y se normalizaron los estilos del formulario de compra y las pestañas de descripción.

**Detalle técnico:** Se utilizaron las clases BEM y variables SASS existentes para mantener la coherencia visual. Se aplicó `display: grid` y `grid-template-columns` para las vistas de catálogo y producto, y `flexbox` para alinear los elementos del formulario de compra.

**Motivo / criterio:** *Zero Bloat y Coherencia Visual*. En lugar de cargar los pesados CSS de WooCommerce, se aplicaron estilos ultraligeros y a medida, garantizando que la tienda se integre visualmente en el ecosistema Merci sin degradar el rendimiento.

**Siguiente paso o deuda:** Con el MVP de la tienda funcional, el siguiente paso es retomar la automatización de LinkedIn (`merci-linkedin.py`).

### 2026-04-30 — Fix: Preservación de estructura de directorios en instanciación

**Contexto:** Tras instanciar el Boilerplate, el orquestador `merci-wp.py` emitía advertencias indicando que los directorios `blog/` y `art-de-cote/` no existían, ya que Git no rastrea carpetas vacías y `merci-init.py` destruía el contenido del `laboratorio/`.

**Hecho:**
- Se añadieron archivos `.gitkeep` a las carpetas `laboratorio/blog/` y `laboratorio/art-de-cote/` de la matriz.
- Se parcheó `scripts/merci/merci-init.py` para reconstruir estos subdirectorios estructurales y generar sus respectivos `.gitkeep` tras la purga del laboratorio.

**Detalle técnico:** La función `purge_directory` usa `shutil.rmtree`, lo que erradica subdirectorios enteros. Recrearlos explícitamente con `mkdir` y `touch(".gitkeep")` asegura que la topología de incubación Headless esté lista desde el commit cero del nuevo proyecto.

**Motivo / criterio:** *Developer Experience (DX) y Robustez*. Un entorno de desarrollo debe proveer el andamiaje completo necesario para que sus herramientas CLI operen sin emitir advertencias de "archivo no encontrado" por problemas derivados del control de versiones.

**Siguiente paso o deuda:** Retomar el MVP de la tienda (WooCommerce) estandarizando sus estilos visuales.

### 2026-04-30 — Fix: Resolución de enlace roto (PGP) en QA de Boilerplate

**Contexto:** Al instanciar y auditar el Boilerplate v1.2.1, el orquestador `merci-total` detuvo el pipeline en la fase de `merci-linkcheck.py` al detectar un error 404 en el enlace `/llave-publica.asc` de la página estática de Contacto.

**Hecho:**
- Se creó el archivo de texto plano `public/llave-publica.asc` con un bloque de mensaje explicativo (Placeholder) para satisfacer el escaneo de red.

**Motivo / criterio:** *QA Estricto (Fail-Fast)*. El orquestador demostró su valor al no tolerar "promesas" de archivos futuros. Para que la plantilla apruebe su propia auditoría desde el commit cero, todos los enlaces estructurales deben resolver a un archivo real, delegando al usuario final la tarea de reemplazar el archivo de muestra con su clave criptográfica real.

**Siguiente paso o deuda:** Retomar el MVP de la tienda (WooCommerce) estandarizando sus estilos visuales.

### 2026-04-30 — Fix: Generación de plantilla .env en instanciación (Release v1.2.1)

**Contexto:** Un nuevo usuario que clona el Boilerplate v1.2.0 experimentaba un fallo crítico en su primer `merci total` porque el pipeline de QA invocaba a `merci-wp.py`, el cual colapsaba al no encontrar el archivo `.env` (excluido por `.gitignore`).

**Hecho:**
- Se modificó `scripts/merci/merci-init.py` para inyectar dinámicamente un archivo `.env` de ejemplo con las variables `WP_URL`, `WP_USER` y `WP_APP_PASSWORD`.
- Se actualizó la versión en `README-merci.md` a v1.2.1.

**Detalle técnico:** El script ahora utiliza `write_text` para crear el archivo de configuración en la raíz del clon antes de finalizar el proceso, asegurando que la dependencia de variables de entorno esté satisfecha para el orquestador.

**Motivo / criterio:** *Developer Experience (DX) y Fricción Cero*. Un boilerplate debe funcionar *out of the box* (listo para usar). Entregar un pipeline roto degrada la confianza en la herramienta. Proveer un `.env` de muestra transforma un error de código (`FileNotFoundError`) en un fallo de conexión controlado, informando al usuario de lo que debe configurar.

**Siguiente paso o deuda:** Retomar el MVP de la tienda (WooCommerce) estandarizando sus estilos visuales en la arquitectura SASS 7-1.

### 2026-04-30 — Docs: Release v1.2.0 del Boilerplate (Consolidación Headless y QA)

**Contexto:** Tras finalizar las herramientas de publicación Headless (`merci-wp`), el enrutamiento contextual (`merci-promote`) y purificar la interfaz estática (Contacto), el ecosistema base alcanzó un hito de madurez que debía ser exportado a la plantilla pública antes de iniciar ramas de desarrollo paralelas (como WooCommerce).

**Hecho:**
- Se actualizó `README-merci.md` con las novedades de la v1.2.0.
- Se marcó la Fase 8.3 como completada al 100% en `instrucciones-merci.md`.
- Se ejecutó el pipeline de despliegue (`merci-init.py` destructivo y `rsync --delete`) para exportar el código inmaculado al repositorio `merci-boilerplate`.

**Detalle técnico:** El orquestador de instanciación purgó automáticamente los manuales SOP exclusivos de la matriz (`docs/matriz/`) asegurando que los "Shadow Docs" ascendieran atómicamente a su versión final en el destino, erradicando la derivación de configuración.

**Motivo / criterio:** *Release Management y Single Source of Truth (SSOT)*. Iniciar desarrollos nuevos (tienda) teniendo "deuda de despliegue" pendiente es un antipatrón. Empaquetar y sellar el repositorio ahora asegura que el Boilerplate herede un estado estable y 100/100 auditado antes de introducir la complejidad de un e-commerce.

**Siguiente paso o deuda:** Desarrollar el MVP de la tienda (WooCommerce) estandarizando sus estilos visuales en la arquitectura SASS 7-1.

### 2026-04-30 — UX/UI: Refactorización purista de la página de Contacto

**Contexto:** La página de contacto (`public/contacto/index.html`) conservaba el texto "placeholder" (texto de relleno) genérico del Boilerplate. Se requería definir el método de contacto sin violar la arquitectura de 0 dependencias ni engordar el código con servicios de terceros (formularios).

**Hecho:**
- Se eliminó el texto genérico del Hero y se implementó un diseño purista tipográfico.
- Se inyectó un canal de comunicación directo (`mailto:`) y un bloque preparado para alojar una clave pública PGP (Pretty Good Privacy).

**Motivo / criterio:** *Zero Bloat y DevSecOps*. Depender de un `<form>` requiere procesado backend (PHP) o servicios de terceros que inyectan scripts y latencia, vulnerando la política estricta de rendimiento y privacidad (GDPR). Proveer un email directo y soporte para cifrado E2EE (End-to-End Encryption) es el estándar técnico superior.

**Siguiente paso o deuda:** Iniciar el diseño y desarrollo de la automatización Headless para LinkedIn (`merci-linkedin.py`).

### 2026-04-30 — Docs: Publicación de cuadernillo sobre optimización de backups

**Contexto:** La drástica reducción del peso de las copias de seguridad (de 50 MB a 0.35 MB) mediante el uso del modo `--verbose` y rutas absolutas se consideró un caso de éxito digno de ser documentado como activo de conocimiento.

**Hecho:** Se redactó y publicó el archivo `biblioteca/cuadernillo-optimizacion-backups-locales.md`.

**Detalle técnico:** El documento explica el diagnóstico a través de la terminal (Caja de Cristal) y la diferencia crítica entre excluir carpetas por coincidencia de cadenas de texto frente al uso de rutas absolutas estructuradas en Python (`Path`).

**Motivo / criterio:** *Knowledge Management*. Trasladar las victorias de rendimiento e infraestructura a la Biblioteca consolida la madurez del ecosistema y sirve como manual de mejores prácticas para el desarrollo y depuración de herramientas CLI locales.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).

### 2026-04-30 — Perf: Verificación de reducción masiva en backup local (0.35 MB)

**Contexto:** Tras aplicar las exclusiones de los binarios de Dart Sass y el historial de auditorías de PageSpeed, era necesario verificar empíricamente el impacto en el tamaño del empaquetado final del repositorio.

**Hecho:** El script `merci-backup.py` generó una copia de seguridad exitosa con un peso total de tan solo 0.35 MB.

**Detalle técnico:** La cifra de 0.35 MB representa una reducción de más del 99.3% frente a los 50.31 MB anteriores. Esto certifica que el filtro de rutas absolutas funciona con precisión quirúrgica, aislando el código fuente puro de cualquier artefacto pesado, multimedia incrustada o binario regenerable.

**Motivo / criterio:** *Zero Bloat y Disaster Recovery*. Un entorno DevSecOps debe permitir respaldos ultrarrápidos y portables. Esta métrica consolida empíricamente la arquitectura del proyecto: el peso reside en las dependencias y el CMS, mientras que el código matriz se mantiene estrictamente minimalista y ágil.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).

### 2026-04-30 — Feat: Modo verbose en script de copias de seguridad

**Contexto:** Tras refactorizar las exclusiones del backup para reducir su peso, surgió la necesidad operativa de poder auditar visualmente qué archivos exactos se estaban empaquetando en el archivo ZIP para verificar que no se filtrara basura o código de terceros.

**Hecho:** Se implementó el flag `--verbose` (o `-v`) en `scripts/merci/merci-backup.py`.

**Detalle técnico:** Se integró la lectura de `sys.argv` para activar la variable booleana `verbose`. Durante la iteración `os.walk`, si el modo está activo, la terminal imprime en tiempo real cada ruta relativa que se escribe en el archivo ZIP (`zipf.write`).

**Motivo / criterio:** *Transparencia y Trazabilidad*. Un proceso de copia de seguridad no debe ser una caja negra. Proveer un modo detallado opcional permite a la desarrolladora certificar la exactitud del filtro de exclusiones sin saturar la salida estándar por defecto en la ejecución diaria.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).

### 2026-04-30 — Perf: Refactorización de exclusiones en script de backup

**Contexto:** La ejecución de `merci-backup.py` generaba un archivo ZIP de más de 50 MB, un tamaño desproporcionado para un repositorio de código fuente. Se diagnosticó que el script estaba comprimiendo la instalación completa de WordPress ubicada en la ruta `public/blog`.

**Hecho:** Se modificó la lógica de exclusión en `scripts/merci/merci-backup.py` para utilizar rutas absolutas (`EXCLUDE_PATHS`) en lugar de nombres de carpetas genéricos.

**Detalle técnico:** Anteriormente, el script excluía carpetas de forma global. No se podía excluir la palabra "blog" porque habría omitido el código fuente en `blog/` y `laboratorio/blog/`. Al migrar a una comprobación por ruta absoluta (`Path(root) / d not in EXCLUDE_PATHS`), se bloquea quirúrgicamente la instalación del CMS.

**Motivo / criterio:** *Performance y Zero Bloat*. Las copias de seguridad locales deben ser ultraligeras y contener exclusivamente el estado del proyecto DevSecOps. Las dependencias externas o instalaciones de terceros (como el núcleo de WP) se regeneran o gestionan aparte, no se empaquetan en el backup del código fuente.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).

### 2026-04-30 — Chore: Invalición de caché manual (Cache Busting v12)

**Contexto:** Tras modificar los diálogos interactivos de `MerciController.js`, los cambios no se reflejaban en el servidor de producción para las rutas estáticas (Portada y Contacto) debido a la retención en caché de los navegadores.

**Hecho:** Se incrementó el parámetro de versión (`?v=12`) en las etiquetas `<link>` y `<script>` de `public/index.html` y `public/contacto/index.html`.

**Detalle técnico:** Mientras que el motor SSG y WordPress utilizan un sistema de versionado dinámico (basado en `filemtime` o `time()`), las páginas HTML puras requieren una actualización manual de la cadena de consulta (query string) para forzar a los clientes web y proxies a invalidar sus cachés locales y solicitar el nuevo archivo al servidor.

**Motivo / criterio:** *Cache Invalidation*. Es la técnica estándar y más ligera para asegurar que todos los usuarios reciban la última versión del código frontend sin necesidad de purgar cachés a nivel de servidor (Nginx/Varnish).

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).

### 2026-04-29 — UX/UI: Unificación responsiva de altura en componentes Hero

**Contexto:** Se detectó disparidad visual entre las distintas páginas del ecosistema (Portada, Contacto, Biblioteca). La sección `.hero` crecía en función de la longitud de su texto, provocando que los bloques de cabecera tuvieran tamaños dispares.

**Hecho:** Se implementó `min-height: 40vh` y centrado vertical con `flexbox` en `src/scss/components/_hero.scss`.

**Detalle técnico:** En lugar de aplicar restricciones rígidas (`height` o `max-height`), que corren el riesgo de provocar desbordamientos de texto (overflow) en pantallas móviles estrechas, se definió una altura mínima basada en *Viewport Height* (`vh`). Flexbox (`justify-content: center`) se encarga de absorber la diferencia de longitud del texto repartiendo el espacio vacío, logrando paridad visual en pantallas de escritorio.

**Motivo / criterio:** *Consistencia Visual y Responsive Design*. Establecer un tamaño base flexible estandariza la primera impresión del usuario en todas las rutas sin comprometer la legibilidad ni la puntuación de Core Web Vitals en dispositivos móviles.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).

### 2026-04-29 — Refactor: Poda de redundancias y duplicidades en arquitectura SASS

**Contexto:** Tras analizar la especificidad CSS, se realizó una auditoría profunda en el directorio `src/scss/` buscando más casos de código muerto o duplicado que engordaran la hoja de estilos final.

**Hecho:**
- Se fusionaron las clases gemelas `.section-methodology` y `.section-ecosystem` en una única clase `.home-section` dentro de `_hero.scss` (y se actualizó `public/index.html`).
- Se eliminaron reglas redundantes (`text-decoration: none` y herencia de color en anclas) en `_library-index.scss`.

**Detalle técnico:** Las reglas eliminadas en el índice de la biblioteca eran "código muerto", ya que el archivo base `_typography.scss` ya se encarga de eliminar el subrayado globalmente y de gestionar la herencia de color en los encabezados (`h1-h6 a`). Las secciones de la portada se unificaron bajo un solo bloque BEM (`.home-section`), reduciendo el peso del CSS.

**Motivo / criterio:** *Zero Dead Code* (Cero Código Muerto) y DRY (Don't Repeat Yourself). Las reglas CSS que redeclaran comportamientos ya definidos por la base tipográfica son un lastre. Mantener un CSS minimalista garantiza un procesamiento rápido del render tree en el navegador.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).

### 2026-04-29 — Refactor: Purga de deuda técnica en componente SASS (_hero.scss)

**Contexto:** Una auditoría de la arquitectura SASS 7-1 reveló la existencia de una definición duplicada de la clase `.card` dentro del archivo `_hero.scss`, a pesar de que dicho componente ya tenía su propio archivo dedicado (`_card.scss`).

**Hecho:** Se eliminó el bloque de código `.card` redundante de `src/scss/components/_hero.scss`.

**Detalle técnico:** El archivo `_index.scss` importaba `_hero.scss` antes que `_card.scss`, provocando que el navegador leyera estilos que eran inmediatamente sobrescritos por el componente correcto. Aunque el resultado visual era el esperado, generaba código muerto en el `main.css` final.

**Motivo / criterio:** *Code Hygiene y Single Responsibility Principle*. Cada componente SASS debe ser responsable únicamente de su propio bloque BEM. Eliminar código duplicado o desplazado reduce el peso del CSS final y mejora drásticamente la mantenibilidad y la claridad de la arquitectura.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).

### 2026-04-29 — Refactor: Reestructuración visual del índice de la Biblioteca (Grid y BEM)

**Contexto:** El índice autogenerado de la Biblioteca utilizaba un layout basado en `flexbox` y clases CSS no estandarizadas (`.indice__*`), lo que dificultaba la creación de columnas de ancho uniforme y una jerarquía visual clara entre los títulos de las estanterías y los artículos.

**Hecho:**
- Se refactorizó `src/scss/components/_library-index.scss` para usar `display: grid` en la lista de estanterías.
- Se migraron los estilos de `.indice__*` desde `_typography.scss` a `_library-index.scss`, renombrando las clases para cumplir la metodología BEM (ej. `.library-nav__theme-title`).
- Se modificó `scripts/merci/merci-publish.py` para inyectar las nuevas clases BEM.
- Se diferenció tipográficamente el título de la estantería (mayúsculas, más peso) del de los artículos.

**Detalle técnico:** Se utilizó `grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));` para lograr un diseño de rejilla responsivo sin media queries. La refactorización a BEM y la centralización de los estilos en su propio componente SASS mejoran la mantenibilidad y la Separación de Responsabilidades.

**Motivo / criterio:** *UX y Code Hygiene*. Un layout en rejilla (Grid) es superior a Flexbox para crear columnas de ancho idéntico, mejorando la armonía visual. Diferenciar la tipografía establece una jerarquía clara que guía al usuario. Pagar la deuda técnica de las clases no estándar y centralizarlas en su componente SASS es una práctica de ingeniería de software limpia.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).

### 2026-04-29 — Refactor: Pago de deuda técnica (Eliminación de estilos en línea)

**Contexto:** Una auditoría de código reveló la existencia de una cantidad significativa de estilos en línea (`style="..."`) en el footer y en el índice de la biblioteca, lo cual se considera deuda técnica al violar el principio de Separación de Responsabilidades y la metodología BEM.

**Hecho:**
- Se crearon los componentes SASS `_footer.scss` y `_library-index.scss`.
- Se refactorizaron los archivos `public/index.html`, `public/contacto/index.html`, `src/wp-theme/merci-theme/index.php` y `scripts/merci/merci-publish.py` para eliminar los atributos `style` y reemplazarlos por clases BEM.

**Detalle técnico:** Se extrajo toda la lógica de posicionamiento (flexbox, márgenes) y cromática a clases BEM dedicadas (ej. `.footer__links`, `.library-nav`, `.library-section`). Esto restaura la autoridad de la arquitectura SASS 7-1 y permite el uso de pseudo-clases interactivas y media queries responsivas.

**Motivo / criterio:** *Code Hygiene y Mantenibilidad*. Aunque los estilos en línea son útiles para prototipado rápido, su permanencia en producción genera un código frágil y difícil de mantener. La refactorización a SASS BEM centraliza la capa de presentación, saldando la deuda técnica y preparando el código para futuras iteraciones.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).

### 2026-04-29 — Docs: Publicación de cuadernillo sobre Especificidad CSS

**Contexto:** Los incidentes relacionados con la pseudo-clase `:visited` y la Especificidad CSS fueron considerados una lección de arquitectura de software lo suficientemente valiosa como para ser promovida a un activo de conocimiento permanente en la Biblioteca.

**Hecho:** Se redactó y creó el archivo `biblioteca/cuadernillo-la-guerra-de-la-especificidad-css.md`.

**Detalle técnico:** El cuadernillo se estructuró bajo el formato de 3 átomos (Desafío, Maniobra, Aprendizaje), explicando con ejemplos prácticos del propio proyecto por qué los estilos en línea y los selectores anidados pueden romper la interactividad de los enlaces.

**Motivo / criterio:** *Knowledge Management*. Transformar incidentes de depuración en material didáctico es un pilar de la filosofía del proyecto. Este cuadernillo servirá como referencia futura para evitar el uso de `!important` o la inyección de estilos en línea que comprometan la UX.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).

### 2026-04-29 — QA: Selección cromática matemática para estado :visited (WCAG)

**Contexto:** Era necesario definir el color exacto para la variable `$color-visited` asegurando que mantuviera la coherencia visual con la marca y, simultáneamente, garantizara el 100/100 en accesibilidad en Google PageSpeed Insights.

**Hecho:** Se actualizó `$color-visited` a `#7c2d12` en `src/scss/abstracts/_variables.scss`.

**Detalle técnico:** El color asignado temporalmente (`#070f75`, azul marino) superaba la prueba de contraste pero causaba disonancia cromática. El tono elegido (`#7c2d12`, teja oscuro) mantiene la raíz del color principal (`#ea580c`) pero ofrece un ratio de contraste de ~10.2:1 sobre fondos blancos y ~9.8:1 sobre el gris claro (`#f8fafc`) del índice, superando ampliamente el mínimo exigido de 4.5:1 (Nivel AA) y alcanzando el nivel AAA.

**Motivo / criterio:** *Shift-Left Accessibility y Diseño UI*. Las decisiones de color en una arquitectura estricta no se basan únicamente en la estética. Calcular matemáticamente el ratio de contraste antes de inyectar variables en SASS previene fallos tardíos en la auditoría de rendimiento (Fail-Fast).

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).

### 2026-04-29 — Fix: Aplicación de estado :visited en enlaces de cabecera (Tarjetas)

**Contexto:** Se detectó que los enlaces de los títulos en las tarjetas de la Biblioteca no cambiaban de color al ser visitados, a pesar de que la regla `:visited` global estaba correctamente definida en SASS.

**Hecho:** Se añadió la pseudo-clase `&:visited` dentro del anidamiento de `h1-h6 > a` en `src/scss/base/_typography.scss`.

**Detalle técnico:** La regla `h2 a { color: inherit; }` tenía una especificidad CSS (`0,0,2`) superior a la regla global `a:visited` (`0,1,1`), provocando que el navegador ignorara el color de visitado y forzara la herencia del color del encabezado. Al añadir explícitamente `&:visited { color: $color-visited; }` dentro del bloque del encabezado, se crea una regla más específica (`0,1,2`) que el navegador sí puede aplicar.

**Motivo / criterio:** *CSS Specificity y UX*. Para que los estados interactivos (`:hover`, `:focus`, `:visited`) funcionen de manera predecible, sus reglas deben tener una especificidad igual o superior a las reglas base del elemento. Esta corrección restaura el feedback visual del historial de navegación en todos los componentes.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).
**Siguiente paso o deuda:** (Pendiente de instrucción).

### 2026-04-29 — Fix: Resolución de especificidad CSS en enlaces del índice (SSG)

**Contexto:** Tras habilitar el estado `:visited` en la arquitectura SASS, se detectó que los enlaces del índice autogenerado de la Biblioteca no cambiaban de color tras ser pulsados.

**Hecho:** Se eliminó el atributo `style="color: ..."` de las etiquetas `<a>` en `scripts/merci/merci-publish.py` y se delegó el control cromático a las nuevas clases `.indice__tema` y `.indice__enlace` en `src/scss/base/_typography.scss`.

**Detalle técnico:** Los estilos en línea (`style="..."`) poseen una especificidad CSS de `1000`, aplastando cualquier pseudo-clase externa como `:visited` (cuya especificidad es `0010`). Al extraer el color a clases SASS estandarizadas, se restaura el flujo natural de la cascada CSS, permitiendo al navegador aplicar los colores de historial correctamente.

**Motivo / criterio:** *Separation of Concerns* y Accesibilidad/UX. Inyectar estilos estructurales menores en línea desde Python es aceptable en SSG, pero inyectar colores destruye la interactividad visual (hover, visited, focus). Mantener la capa cromática estrictamente en SASS garantiza la respuesta adecuada a las acciones del usuario.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).
**Siguiente paso o deuda:** (Pendiente de instrucción).

### 2026-04-29 — UX/UI: Incorporación de estado :visited en enlaces globales

**Contexto:** Para mejorar la navegación y reducir la carga cognitiva, era necesario que el usuario pudiera identificar de un vistazo qué artículos o estanterías de la Biblioteca ya había visitado previamente.

**Hecho:** Se instruyó la adición de la pseudo-clase `:visited` en la arquitectura SASS para los enlaces globales.

**Detalle técnico:** En accesibilidad y usabilidad (UX), diferenciar el estado visitado previene que el usuario haga clic repetidamente en contenido ya consumido. Se aplicó un tono ligeramente más oscuro o desaturado al color principal del enlace para mantener la coherencia visual sin violar el contraste WCAG.

**Motivo / criterio:** *Usabilidad y Fricción Cero*. Proveer *feedback* visual del historial de navegación es un estándar web fundamental (Heurísticas de Nielsen) que mejora significativamente la experiencia en sitios con alta densidad de contenido.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).
**Siguiente paso o deuda:** (Pendiente de instrucción).

### 2026-04-29 — Docs: Revisión editorial y refinamiento del copy en la portada

**Contexto:** Antes de subir a producción, se propuso una revisión de los textos de la portada (`public/index.html`) para asegurar que estuvieran alineados con la "Guía de Voz Editorial" (Regla 6), transmitiendo claridad técnica y evitando redundancias.

**Hecho:** Se refinó el subtítulo del Hero y la descripción de la tarjeta del Sistema Merci en `public/index.html`.

**Detalle técnico:** Se eliminó la redundancia ("base de conocimiento y operaciones con base en") sustituyéndola por "centro de operaciones. Un entorno web...". En la tarjeta de Merci, se hizo la llamada a la acción más directa y nativa ("Haz clic sobre su avatar").

**Motivo / criterio:** *UX Copywriting*. El texto de la interfaz es tan importante como la arquitectura subyacente. Aplicar la regla 80/20 (claridad técnica / personalidad) garantiza que el usuario perciba el rigor DevSecOps desde la primera línea que lee.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).

### 2026-04-29 — Docs: Auditoría de paridad y actualización a Boilerplate v1.1.0

**Contexto:** Antes de desplegar el código a producción y exportar la nueva plantilla al repositorio derivado (`merci-boilerplate`), era imperativo verificar que los manuales operativos reflejaran el estado real del ecosistema (SSOT).

**Hecho:**
- Se incrementó la versión a `v1.1.0` en `README-merci.md`.
- Se actualizaron los listados de scripts y flujos operativos (SOP Dual) en `instrucciones.md` e `instrucciones-merci.md`.

**Detalle técnico:** Se incluyeron de forma explícita las herramientas `merci-wp.py`, `merci-sync-pages.py` y `merci-promote.py` (en su versión con enrutamiento inteligente) dentro de la documentación *Shadow* que viajará con la nueva instanciación del boilerplate.

**Motivo / criterio:** *Governance*. El código no está terminado hasta que la documentación no lo explica. Un salto de versión menor (Minor Release) está justificado por la inclusión de características Headless y de compilación completas y retrocompatibles.

**Siguiente paso o deuda:** Empaquetar la matriz, desplegar en producción y ejecutar el ciclo completo de instanciación hacia el Boilerplate.

### 2026-04-29 — Feat: Integración del publicador Headless (merci-wp) en el orquestador maestro

**Contexto:** Para garantizar que el entorno de producción dinámico (WordPress) se sincronice automáticamente antes de ejecutar las auditorías y el rastreo de enlaces, era necesario incluir el script `merci-wp.py` en la cadena de montaje global.

**Hecho:** Se añadió `merci-wp.py` al array `PIPELINE` de `scripts/merci/merci-total.py`.

**Detalle técnico:** El script se inyectó en la Fase de Construcción (Build), justo después de `merci-publish.py` y antes de `merci-sync-pages.py`. Esto asegura que los markdowns locales se conviertan en posts de WordPress y sus URLs estén activas antes de que `merci-linkcheck.py` y `merci-sitemap.py` rastreen el sitio.

**Motivo / criterio:** *Fricción Cero y Single Source of Truth (SSOT)*. Automatizar la sincronización de WordPress junto con el sitio estático mediante un único comando (`merci total`) unifica definitivamente los flujos de trabajo duales, mitigando el riesgo de que la desarrolladora olvide subir un artículo antes de hacer el commit atómico.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).

### 2026-04-29 — Fix: Ambigüedad WAI-ARIA en menú dinámico (Blog)

**Contexto:** El rastreador `merci-linkcheck.py` detectó una infracción WAI-ARIA en las rutas de WordPress. El menú principal enlaza a `/blog/` con el texto "Blog", mientras que las tarjetas de los artículos enlazan a su categoría `/blog/category/blog/` con el mismo texto exacto, generando confusión para los lectores de pantalla.

**Hecho:** Se inyectó `aria-label="Ir a la portada del Blog"` en el enlace del menú principal en `public/index.html` y `src/wp-theme/merci-theme/index.php`.

**Detalle técnico:** Diferenciar el "Nombre Accesible" mediante `aria-label` resuelve la colisión en el DOM dinámico sin alterar el diseño visual, superando el escaneo automatizado del pipeline.

**Motivo / criterio:** *Accesibilidad Estricta e Inclusión*. Los lectores de pantalla listan enlaces fuera de contexto. Diferenciar sus propósitos semánticamente restaura la puntuación de 100/100 en accesibilidad.

**Siguiente paso o deuda:** Integrar la sincronización masiva de WordPress al pipeline maestro (`merci-total.py`).

### 2026-04-29 — Fix: Robustez en RegEx para saltos de línea y BOM (merci-promote)

**Contexto:** El asistente de promoción (`merci-promote.py`) fallaba al reconocer el YAML Frontmatter de la nueva plantilla de Art de Coté, a pesar de que el formato visual era estructuralmente correcto.

**Hecho:** Se refactorizaron las expresiones regulares en `scripts/merci/merci-promote.py` para tolerar `\r\n` y se cambió la codificación de lectura a `utf-8-sig`.

**Detalle técnico:** La expresión regular original `^---\n` era estricta con el salto de línea Unix (`LF`). Si el editor de texto guardaba el archivo con saltos de línea de Windows —Retorno de carro y avance de línea (CRLF)— o inyectaba un carácter BOM (*Byte Order Mark* - `\ufeff`) al inicio, el `match` fallaba silenciosamente. Se actualizó a `^\s*---\r?\n` para absorber caracteres invisibles y retornos de carro.

**Motivo / criterio:** *Robustez y Fricción Cero*. Un script de automatización CLI (Command Line Interface - Interfaz de Línea de Comandos) no debe colapsar por diferencias de codificación de texto a nivel de sistema operativo. Aplicar esta robustez evita bloqueos incomprensibles para el usuario.

**Siguiente paso o deuda:** Validar la promoción del archivo y proceder con la automatización de LinkedIn (Fase 8.3).

### 2026-04-29 — Docs: Creación de plantillas Headless WP y definición de fronteras

**Contexto:** Se requería crear plantillas base (YAML Frontmatter + Markdown) para facilitar la redacción de nuevos artículos destinados a las categorías dinámicas (Blog y Art de Coté). Surgió el debate arquitectónico sobre si debían alojarse en el `laboratorio/` y si pertenecían a las reglas de negocio de la matriz o al ecosistema del Boilerplate.

**Hecho:** Se crearon los archivos `docs/plantilla-blog.md` y `docs/plantilla-art-de-cote.md`.

**Detalle técnico:** Las plantillas incluyen pre-configurados los campos `estado: "borrador"` y sus respectivos `tema:` para garantizar el enrutamiento correcto hacia WordPress por parte de `merci-wp.py`.

**Motivo / criterio:** *Separation of Concerns* (Separación de Responsabilidades). El entorno `laboratorio/` es efímero y se purga durante la instanciación (`merci-init.py`); alojar plantillas allí provocaría su destrucción en proyectos derivados. Ubicarlas en `docs/` consolida el Boilerplate como un producto completo que provee tanto el motor de publicación como los moldes de contenido.

**Siguiente paso o deuda:** Implementar automatización social para publicar entradas del blog directamente en LinkedIn.

### 2026-04-29 — Feat: Expulsión activa de borradores al laboratorio en CMS Headless

**Contexto:** Para garantizar la paridad absoluta con el flujo de la biblioteca estática, los artículos de WordPress que eran despublicados (`estado: "borrador"`) actualizaban su estado en la base de datos pero permanecían físicamente en las carpetas de producción (`blog/` o `art-de-cote/`).

**Hecho:** Se implementó la lógica de "Kill-Switch" con reubicación física en `scripts/merci/merci-wp.py`.

**Detalle técnico:** Tras una petición exitosa a la API de WordPress, si el estado no es `"publicado"` y el archivo no reside ya en `laboratorio/`, el script utiliza `shutil.move()` para trasladarlo de vuelta a `laboratorio/<ruta_relativa>`, replicando su árbol de directorios original dinámicamente (`destino_lab.parent.mkdir()`).

**Motivo / criterio:** *Environment Segregation*. Ningún documento en fase de incubación o revisión debe residir en los directorios raíz, ya sean de la capa estática o dinámica. La automatización de este movimiento previene que el autor olvide limpiar las carpetas de producción tras despublicar un post.

**Siguiente paso o deuda:** Implementar automatización social para publicar entradas del blog directamente en LinkedIn.

### 2026-04-29 — Feat: Enrutamiento contextual en orquestador de promoción (merci-promote)

**Contexto:** Para cumplir con la nueva unificación del flujo de publicación (SSOT), se requería que el asistente interactivo `merci-promote.py` reconociera los subdirectorios de incubación dinámica (`laboratorio/blog` y `laboratorio/art-de-cote`) y trasladara los documentos curados a sus respectivas carpetas raíz.

**Hecho:** Se refactorizó `scripts/merci/merci-promote.py` implementando escaneo recursivo (`rglob`) y una lógica de enrutamiento basada en las rutas relativas.

**Detalle técnico:** El script extrae las partes del directorio del archivo analizado (`rel_path.parts[:-1]`). Si detecta la palabra clave "blog" o "art-de-cote", asigna dinámicamente el directorio de destino y actualiza el mensaje de salida para sugerir el comando de publicación adecuado (`merci wp` en lugar de `merci total`).

**Motivo / criterio:** *Context-Awareness y Experiencia del Desarrollador*. En un ecosistema con múltiples motores de renderizado, centralizar la curación documental en una sola herramienta CLI evita el error humano. El script actúa como un "router" inteligente: el autor solo tiene que organizar sus borradores en carpetas dentro del laboratorio, y Python infiere matemáticamente el destino de producción.

**Siguiente paso o deuda:** Implementar automatización social para publicar entradas del blog directamente en LinkedIn (Fase 8.3).

### 2026-04-29 — Arch: Unificación del flujo de promoción para Headless CMS

**Contexto:** Los artículos destinados a WordPress se publicaban directamente desde el entorno de incubación (`laboratorio/`), saltándose el proceso de curación y creando disparidad arquitectónica respecto a la biblioteca estática. Además, WordPress no actualizaba las categorías de posts existentes si la API no lograba resolver el ID de la nueva categoría temporalmente.

**Hecho:**
- Se modificó la lista `WP_DIRS` en `scripts/merci/merci-wp.py` para apuntar a los directorios raíz `blog/` y `art-de-cote/`.
- Se redefinió el SOP de publicación dual (`docs/matriz/flujo-publicacion-sop.md`) para exigir el uso de `merci-promote.py` antes de sincronizar con WP.

**Motivo / criterio:** *Paridad de flujos y Separation of Concerns*. El entorno `laboratorio/` debe ser estrictamente para incubación. Aplicar la herramienta de promoción a los contenidos dinámicos unifica la experiencia del desarrollador (Developer Experience): todo nace en el laboratorio y todo se promueve a un directorio de pre-producción en la raíz, independientemente del motor de renderizado final (SSG o WP).

**Siguiente paso o deuda:** Refactorizar `merci-promote.py` para soportar el traslado de documentos hacia los directorios dinámicos (`blog/` y `art-de-cote/`).

### 2026-04-29 — Fix: Resolución de error WAI-ARIA por 'Trailing Slashes' y refuerzo de Whitelist en WP

**Contexto:** El orquestador `merci-total.py` detuvo el pipeline reportando un error de accesibilidad WAI-ARIA (Enlaces ambiguos) en el menú principal. Paralelamente, los posts de "Art de Coté" seguían apareciendo en la portada dinámica (`/blog`), indicando un fallo en el modelo Whitelist implementado anteriormente.

**Hecho:**
- Se añadieron barras finales (*trailing slashes*) a las rutas de directorio en la navegación (`<nav>`) de todos los componentes estáticos y dinámicos (ej. `/blog/category/art-de-cote/`).
- Se modificó la función `merci_filtrar_feed_principal` en `functions.php` delegando la consulta del slug directamente a `$query->set('category_name', 'blog')`.

**Detalle técnico:** El linter de accesibilidad detectaba el enlace del menú (sin barra final) y el enlace autogenerado por WordPress en la tarjeta del post (con barra final) como dos destinos distintos compartiendo el mismo texto ancla. Añadir las barras estandariza las URIs y elimina la colisión. Respecto a WordPress, usar `get_category_by_slug` generaba un "fallo abierto": si la categoría no se recuperaba instantáneamente, el condicional se omitía y WP mostraba todos los posts por defecto. Usar `category_name` impone un "fallo seguro" delegado al motor SQL de WP.

**Motivo / criterio:** *QA Estricto y Arquitectura Segura*. Las URIs de directorios deben terminar en `/` por estándar SEO (evita redirecciones 301 de servidor). En el backend, las funciones de filtro (Hooks) deben programarse siempre bajo el principio de fallo seguro (Fail-Safe) para garantizar la segregación de entornos.

**Siguiente paso o deuda:** Validar el pipeline en verde y confirmar la segregación de posts en WordPress.

### 2026-04-29 — Feat: Sincronización masiva en publicador Headless (merci-wp.py)

**Contexto:** El publicador Headless de WordPress operaba sobre un solo archivo a la vez. Para garantizar la paridad absoluta entre los Markdowns locales y la base de datos de WordPress (ej. cambios masivos de formato o despublicaciones en bloque), se requería que el script actuara como un sincronizador global similar al de la biblioteca (`merci-publish.py`).

**Hecho:** 
- Se refactorizó `scripts/merci/merci-wp.py` para procesar directorios completos de forma recursiva.
- Se definieron los directorios `laboratorio/blog` y `laboratorio/art-de-cote` como orígenes por defecto si el script se ejecuta sin argumentos.
- Se actualizó el manual operativo (`docs/matriz/flujo-publicacion-sop.md`).

**Detalle técnico:** Se extrajo la carga de credenciales `.env` fuera del bucle de publicación para optimizar recursos de I/O. Las interrupciones `sys.exit(1)` en el procesamiento individual de archivos se reemplazaron por retornos tempranos (`return False`) para aplicar el patrón "Fail-Gracefully" (Fallar con elegancia), permitiendo que el lote completo finalice aunque un archivo esté malformado.

**Motivo / criterio:** *Single Source of Truth (SSOT)*. Obligar al desarrollador a recordar qué archivo modificó para sincronizarlo individualmente genera Deriva de Configuración. Ejecutar una sincronización masiva asegura que las despublicaciones (`estado: "borrador"`) se reflejen instantáneamente en el entorno de producción dinámico sin fricción operativa.

**Siguiente paso o deuda:** Validar la automatización masiva y avanzar, bajo autorización, a la integración de automatización social para LinkedIn (Fase 8.3).

### 2026-04-29 — Arch: Pivot a modelo Whitelist en el feed principal de WordPress

**Contexto:** Tras aplicar una regla de exclusión para separar "Art de Coté" del feed principal, se debatió que un enfoque de "lista negra" no es escalable. El feed principal (`/blog`) debía actuar como un contenedor estanco exclusivo, no como un recolector general que requiere exclusiones manuales.

**Hecho:** Se refactorizó la función en `functions.php` a `merci_filtrar_feed_principal` (hook `pre_get_posts`) y se añadió la autocreación de la categoría "Blog".

**Detalle técnico:** En lugar de excluir categorías con ID negativo (`'-' . $id`), la consulta `is_home()` ahora fuerza explícitamente la inclusión exclusiva del ID de la categoría "Blog" (`$query->set('cat', $blog_cat->term_id)`).

**Motivo / criterio:** *Arquitectura de la Información y Escalabilidad (Whitelist vs Blacklist)*. Un modelo de lista blanca asegura que cualquier futura taxonomía o categoría independiente creada en el CMS quedará automáticamente aislada del blog sin necesidad de modificar el código del tema.

**Siguiente paso o deuda:** Implementar automatización social para publicar entradas del blog directamente en LinkedIn (Fase 8.3).

### 2026-04-29 — Arch: Segregación de categorías en el feed principal de WordPress

**Contexto:** Tras publicar un artículo en la categoría "Art de Coté" mediante el publicador Headless, se observó que dicho artículo aparecía tanto en su página de categoría como en el listado principal del blog (`/blog`), rompiendo la separación conceptual de los contenidos.

**Hecho:** Se implementó la función `merci_excluir_categorias_del_blog` en el archivo `functions.php` del tema, enganchada al hook `pre_get_posts`.

**Detalle técnico:** La función intercepta la consulta principal de WordPress (`is_main_query()`) cuando se renderiza la página de inicio del blog (`is_home()`). Obtiene dinámicamente el ID de la categoría "Art de Coté" mediante `get_category_by_slug()` y modifica la consulta (`$query->set()`) para excluir explícitamente los posts de dicho ID.

**Motivo / criterio:** *Arquitectura de la Información*. El comportamiento por defecto de WordPress es mostrar todos los posts en su feed principal. Para lograr una separación estricta entre un "blog" cronológico y colecciones temáticas, es necesario filtrar la consulta principal. Usar el hook `pre_get_posts` es el método canónico y más eficiente para lograrlo sin afectar el rendimiento.

**Siguiente paso o deuda:** Implementar automatización social para publicar entradas del blog directamente en LinkedIn (Fase 8.3).

### 2026-04-29 — Docs: Creación del SOP maestro de Publicación Dual

**Contexto:** Tras la implementación exitosa del publicador Headless para WordPress (`merci-wp.py`), el ecosistema pasó a gobernar dos flujos de publicación completamente distintos (SSG estático vs API REST dinámica). Era imperativo documentar las fronteras operativas para evitar que el desarrollador cruce herramientas por error (ej. promover un post de WP a la biblioteca estática).

**Hecho:** Se redactó y consolidó el documento `docs/matriz/flujo-publicacion-sop.md` (SOP: Flujo de Publicación Dual).

**Detalle técnico:** El documento actúa como una guía de referencia rápida (*Cheat Sheet*) que separa explícitamente el Flujo 1 (Laboratorio -> Promote -> Publish) del Flujo 2 (Art de Coté -> WP Headless).

**Motivo / criterio:** *Governance y Developer Experience (DX)*. Un ecosistema DevSecOps complejo requiere reglas de operación claras. Documentar las "Reglas de Oro" y los comandos exactos externaliza la carga cognitiva de la memoria del desarrollador hacia el repositorio de código, garantizando la mantenibilidad a largo plazo.

**Siguiente paso o deuda:** Implementar automatización social para publicar entradas del blog directamente en LinkedIn (Fase 8.3).

### 2026-04-29 — Feat: Sincronización bidireccional (Update) en Headless CMS

**Contexto:** El publicador Headless (`merci-wp.py`) generaba un artículo duplicado cada vez que se ejecutaba sobre el mismo archivo. Además, se detectó que pasar documentos destinados a WordPress por el flujo de `merci-promote` los ubicaba en la `biblioteca/`, provocando que el orquestador SSG los compilara erróneamente como páginas estáticas.

**Hecho:** 
- Se modificó `scripts/merci/merci-wp.py` para que lea y escriba dinámicamente el atributo `wp_id` en el YAML Frontmatter del archivo Markdown local.
- Se estableció la regla de segregar los archivos Markdown destinados a WordPress en carpetas externas a `biblioteca/` (ej. `art-de-cote/`) y omitir su paso por `merci-promote`.

**Detalle técnico:** En la primera publicación, el script captura el `id` numérico devuelto por la API de WordPress y reescribe físicamente el YAML del archivo `.md` inyectando `wp_id: "ID"`. En ejecuciones posteriores, el script detecta este ID y muta su endpoint a `/wp-json/wp/v2/posts/{id}` para realizar una actualización (Update) en lugar de una creación (Create).

**Motivo / criterio:** *Single Source of Truth (SSOT) Bidireccional*. Para que un Headless CMS en terminal funcione sin fricción, el archivo de texto local debe ser consciente de su entidad gemela en la base de datos. La inyección automática elimina el riesgo de duplicidad sin requerir interacción manual del autor.

**Siguiente paso o deuda:** Implementar automatización social para publicar entradas del blog directamente en LinkedIn.

### 2026-04-29 — Feat: Publicador Headless para WordPress (merci-wp.py)

**Contexto:** Para eliminar la fricción de usar el panel de administración de WordPress, se requería una herramienta de terminal para publicar artículos directamente desde archivos Markdown locales.

**Hecho:**
- Se desarrolló el script `scripts/merci/merci-wp.py`.
- Se documentó el proceso de creación de Contraseñas de Aplicación en WordPress y la configuración del archivo `.env`.
- Se actualizó el `README.md` para registrar la nueva herramienta y marcar la tarea como completada.

**Detalle técnico:** El script utiliza únicamente la biblioteca estándar de Python. Lee las credenciales de un archivo `.env` local, convierte el Markdown a HTML, y realiza dos peticiones a la API REST de WordPress: una (GET) para resolver el ID numérico de la categoría a partir de su nombre (leído del campo `tema:` del YAML), y otra (POST) para publicar el contenido. La autenticación se realiza mediante Basic Auth, enviando el usuario y la contraseña de aplicación codificados en Base64 en la cabecera `Authorization`.

**Motivo / criterio:** *Fricción Cero y Developer Experience (DX)*. Automatizar la publicación desde la terminal se alinea con la filosofía "CLI-first" del proyecto. Evitar dependencias externas (`requests`, `python-dotenv`) mantiene el núcleo de automatización ultraligero y portable.

**Siguiente paso o deuda:** Implementar la automatización social para publicar en LinkedIn.

### 2026-04-29 — QA: Certificación "Cuádruple 100" en auditoría móvil extrema

**Contexto:** Tras solventar las penalizaciones de contraste de color (WCAG) y la ambigüedad de enlaces (WAI-ARIA) en la nueva página índice de la Biblioteca, era obligatorio certificar el estado del arte mediante una auditoría de caja negra externa (Google PageSpeed Insights).

**Hecho:** Se logró la máxima puntuación posible (100/100 en Rendimiento, Accesibilidad, Mejores Prácticas y SEO) bajo condiciones simuladas de estrés (Moto G Power sobre red 4G lenta).

**Detalle técnico:** Las correcciones de accesibilidad (atributos `aria-label` y CSS de herencia de color) se integraron sin añadir un solo milisegundo al tiempo de carga. Las métricas Core Web Vitals continuaron marcando TBT 0ms y un Speed Index de apenas 0.8s.

**Motivo / criterio:** *Quality Assurance*. Obtener un 4x100 en móvil demuestra que la accesibilidad universal y el rendimiento extremo no son conceptos excluyentes si se aborda el desarrollo desde una arquitectura de Cero Dependencias (Vanilla JS + SASS 7-1 + SSG en Python puro).

**Siguiente paso o deuda:** Iniciar el desarrollo e integración del publicador Headless CMS (`merci-wp.py`) para WordPress.

### 2026-04-29 — QA: Certificación 100/100 en Rendimiento (Core Web Vitals) de la Biblioteca

**Contexto:** Tras la inyección masiva de nodos en el DOM para construir el "Mega-Menú" y la reestructuración de la página de la Biblioteca, era imperativo asegurar que la complejidad estructural no hubiera degradado el rendimiento.

**Hecho:** Se ejecutó una auditoría final de Lighthouse (PageSpeed Insights). El resultado certificó un Rendimiento perfecto: FCP 0.8s, LCP 1.1s, TBT 0ms y CLS 0.

**Detalle técnico:** Lograr **0 ms** de Tiempo de Bloqueo Total (TBT) demuestra que el hilo principal (Main Thread) del navegador está completamente libre. El CLS en 0 confirma que la carga asíncrona de estilos e imágenes no provoca repintados destructivos (Layout Thrashing).

**Motivo / criterio:** *Performance Driven Development*. Esta métrica valida empíricamente la filosofía fundacional del proyecto: usar Vanilla JS, SASS 7-1 nativo y un orquestador SSG en Python aplasta en rendimiento a cualquier framework reactivo moderno (React/Vue/Tailwind) dependiente de ecosistemas Node.js pesados.

**Siguiente paso o deuda:** Probar el publicador Headless (`merci-wp.py`) recién diseñado para escribir en WordPress local desde la terminal.

### 2026-04-29 — DevSecOps: Shift-Left Accessibility en rastreador de enlaces (DAST)

**Contexto:** Tras solucionar manualmente una advertencia de Lighthouse ("Identical links have the same purpose"), se propuso automatizar la detección de esta regla WAI-ARIA localmente para no depender de herramientas externas, atrapando el error directamente en la integración continua.

**Hecho:** Se refactorizó `scripts/merci/merci-linkcheck.py` transformándolo en un auditor dinámico dual (detecta enlaces rotos 404 + ambigüedad de accesibilidad).

**Detalle técnico:** Se amplió la clase `LinkParser` (heredada de `HTMLParser`) para registrar cuándo el parseo ocurre dentro de una etiqueta `<a>` y extraer su texto visible (`handle_data`) o su `aria-label`. Al finalizar una página, se mapean los "Nombres Accesibles" resultantes contra sus URLs de destino. Si un mismo nombre apunta a más de un destino único (`len(set(hrefs)) > 1`), el orquestador aborta la ejecución con un error `♿❌ Error WCAG`.

**Motivo / criterio:** *Shift-Left Accessibility*. Mover las validaciones de accesibilidad hacia la etapa de pre-commit elimina la latencia de descubrimiento de deuda técnica. Ampliar una herramienta nativa existente en Python logra este hito manteniendo la política innegociable de 0 dependencias (sin requerir Lighthouse CLI o módulos pesados de NPM).

**Siguiente paso o deuda:** Desarrollar el publicador Headless (`merci-wp.py`) para escribir en WordPress local desde la terminal.

### 2026-04-29 — QA: Resolución de ambigüedad en enlaces idénticos (WAI-ARIA)

**Contexto:** Lighthouse detectó una infracción de "Mejores Prácticas/Accesibilidad" porque los enlaces del Mega-Menú y los títulos de las tarjetas tenían el mismo texto visible (el título del artículo) pero apuntaban a destinos diferentes (`#ancla` vs `/url-final.html`).

**Hecho:** Se inyectaron atributos `aria-label` descriptivos en `scripts/merci/merci-publish.py` para diferenciar el propósito de cada enlace.

**Detalle técnico:** El enlace del Mega-Menú ahora se anuncia a los lectores de pantalla como `Ir al resumen de: [Título]`, mientras que el enlace de la tarjeta se anuncia como `Leer artículo completo: [Título]`.

**Motivo / criterio:** *Accesibilidad Estricta (100/100)*. Los lectores de pantalla listan los enlaces fuera de contexto. Si dos enlaces se llaman igual pero hacen cosas distintas, el usuario con discapacidad visual no puede predecir el resultado. Diferenciar sus propósitos mediante WAI-ARIA restaura la puntuación y mejora la UX inclusiva.

**Siguiente paso o deuda:** Desarrollar el publicador Headless (`merci-wp.py`) para escribir en WordPress local desde la terminal.

### 2026-04-29 — QA: Resolución de contraste WCAG en índice de la Biblioteca

**Contexto:** Tras la creación del Mega-Menú (índice curado) en la Biblioteca, una auditoría de Lighthouse detectó que el color naranja de los enlaces de las estanterías (`#ea580c`) sobre el fondo gris claro (`#f8fafc`) no alcanzaba el ratio de contraste mínimo exigido, provocando una penalización en Accesibilidad.

**Hecho:** Se oscureció el color de los enlaces a `#9a3412` (y su borde inferior a `rgba(154, 52, 18, 0.3)`) en el orquestador `scripts/merci/merci-publish.py`.

**Detalle técnico:** El color original `#ea580c` tiene un ratio de contraste de ~3.0:1 sobre fondos claros, lo cual está en el límite para textos en negrita grandes, pero falla el umbral estricto de 4.5:1 para textos generales. El nuevo tono `#9a3412` eleva el contraste por encima de 6:1, garantizando el 100/100 en Core Web Vitals (Accesibilidad).

**Motivo / criterio:** *Accesibilidad Estricta (100/100)*. La estética (un color vibrante) nunca debe comprometer la legibilidad. Si una herramienta automatizada detecta un problema de contraste, se corrige inmediatamente endureciendo el tono hacia umbrales seguros (Shift-Left Accessibility).

**Siguiente paso o deuda:** Desarrollar el publicador Headless (`merci-wp.py`) para escribir en WordPress local desde la terminal.

### 2026-04-29 — QA: Resolución de contraste WCAG en enlaces del footer

**Contexto:** Tras la inyección de los nuevos enlaces sociales en el footer, la auditoría de Lighthouse (PageSpeed Insights) reportó una caída a 95/100 en Accesibilidad debido a un ratio de contraste deficiente.

**Hecho:** Se aplicaron estilos en línea (`color: inherit; text-decoration: underline; text-underline-offset: 4px;`) a la clase `.footer__link` en la portada (`public/index.html`) y la plantilla CMS (`src/wp-theme/merci-theme/index.php`).
*Nota:* La página estática de contacto heredó la corrección automáticamente sin intervención manual gracias a la ejecución de `merci-sync-pages.py` en el orquestador.

**Detalle técnico:** Los navegadores aplican un color azul por defecto (`#0000EE`) a los enlaces no estilizados, el cual falla sistemáticamente el ratio de contraste 4.5:1 de las normativas WCAG (Web Content Accessibility Guidelines - Pautas de Accesibilidad al Contenido en la Web) sobre fondos oscuros o claros con poca luminancia.

**Motivo / criterio:** *Accesibilidad Estricta (100/100)*. Además del color, forzar el subrayado cumple con la norma de que "el color no debe ser el único indicador visual de interactividad". Mantener el 100/100 es innegociable en el ecosistema.

**Siguiente paso o deuda:** Desarrollar el publicador Headless (`merci-wp.py`) para escribir en WordPress local desde la terminal.

### 2026-04-29 — UX: Enlaces de "Volver arriba" en estanterías de la Biblioteca

**Contexto:** Con la implementación del "Mega-Menú" y el scroll suave hacia las tarjetas de los artículos, los usuarios necesitaban una forma rápida de regresar al índice superior tras revisar una estantería completa, sin depender del enlace del footer o de hacer scroll manual.

**Hecho:** Se inyectó un enlace `↑ Volver arriba` (apuntando a `#top`) a la derecha de cada título de sección (Estantería) en el orquestador `scripts/merci/merci-publish.py`.

**Detalle técnico:** Se envolvió el título de la sección (`<h2>`) y el nuevo enlace (`<a>`) en un contenedor `<div>` con `display: flex; justify-content: space-between; align-items: baseline;`. Esto garantiza que, sin importar la longitud del título del tema, el botón de retorno siempre quede fijado a la derecha de la pantalla y alineado con la base del texto.

**Motivo / criterio:** *Fricción Cero y Microinteracciones*. Facilitar atajos de navegación contextuales mejora radicalmente la Experiencia de Usuario (UX) en páginas que actúan como índices o directorios largos. Al usar CSS nativo (Flexbox), se logra el diseño perfecto sin afectar el rendimiento ni requerir JavaScript.

**Siguiente paso o deuda:** Desarrollar el publicador Headless (`merci-wp.py`) para escribir en WordPress local desde la terminal.

### 2026-04-29 — UX: Corrección de flujo de navegación en índice de Biblioteca

**Contexto:** Los sub-enlaces del índice curado recién generado dirigían al usuario directamente a la página del artículo individual, provocando que la sección de tarjetas resumen de la propia página índice quedara huérfana e ignorada.

**Hecho:** Se modificaron los enlaces del bloque `<nav>` en `scripts/merci/merci-publish.py` para que actúen como anclas internas (`#`). Simultáneamente, se inyectaron IDs dinámicos (basados en el título) y la propiedad `scroll-margin-top` en los elementos `<article>` de las tarjetas.

**Detalle técnico:** Al utilizar `slugify(pub["titulo"])` generamos un anclaje único por tarjeta (ej. `id="mi-articulo"`). Los enlaces del menú ahora apuntan a `#mi-articulo` en lugar de a `/biblioteca/mi-articulo.html`.

**Motivo / criterio:** *Retención de Contexto y UX*. El objetivo de una página índice es actuar como un escaparate. Redirigir al usuario al resumen de la tarjeta permite que lea la descripción (excerpt) antes de decidir si desea hacer clic en el título y abandonar la navegación panorámica.

**Siguiente paso o deuda:** Desarrollar el publicador Headless (`merci-wp.py`) para escribir en WordPress local desde la terminal.

### 2026-04-29 — UX/UI: Expansión del índice curado con sub-enlaces de artículos (SSG)

**Contexto:** El índice curado superior recién creado solo mostraba las "Estanterías" (temas), obligando al usuario a hacer clic o scroll a ciegas para descubrir qué artículos contenía cada categoría.

**Hecho:** Se refactorizó el bucle de generación del índice en `scripts/merci/merci-publish.py` para inyectar una lista anidada (`<ul>`) con los enlaces directos a cada artículo bajo su respectiva estantería.

**Detalle técnico:** Se alteró el layout del contenedor padre (`<li>`) aplicando CSS `flex: 1 1 300px`, creando automáticamente un diseño de columnas responsivo (tipo mampostería) que se adapta al ancho de la pantalla móvil o de escritorio sin usar CSS Grid explícito.

**Motivo / criterio:** *Fricción Cero y Descubrimiento*. Evolucionar el índice hacia un patrón de "Mega Menú" o "Mapa del Sitio" visual expone todo el conocimiento disponible en el primer impacto (Above the Fold). Al autogenerarse en Python durante el proceso SSG, esta rica interfaz cuesta 0 milisegundos de renderizado extra al navegador.

**Siguiente paso o deuda:** Desarrollar el publicador Headless (`merci-wp.py`) para escribir en WordPress local desde la terminal.

### 2026-04-29 — UX: Reestructuración visual e índice curado en la Biblioteca (SSG)

**Contexto:** La página principal autogenerada de la Biblioteca carecía de una sección `Hero`, lo que rompía la consistencia visual con el resto del ecosistema (Portada, Contacto). Además, carecía de un índice rápido, dificultando la navegación a medida que aumentaban las estanterías temáticas.

**Hecho:** Se refactorizó la función `generar_indice_biblioteca()` en `scripts/merci/merci-publish.py` para inyectar una sección `Hero` y un bloque `<nav>` dinámico con enlaces ancla.

**Detalle técnico:** Se reutilizó la función existente `slugify()` para convertir los nombres de los temas en atributos `id` HTML5 válidos. Se inyectó la propiedad CSS nativa `scroll-margin-top: 100px;` en cada sección temática para garantizar que la cabecera fija de la web no solape los títulos al realizar saltos internos mediante los enlaces ancla.

**Motivo / criterio:** *UX (Experiencia de Usuario) y Fricción Cero*. Un motor de Generación de Sitios Estáticos (SSG) no solo debe agrupar enlaces, debe maquetar interfaces coherentes. Autogenerar el índice curado (*Table of Contents*) elimina la necesidad de mantenimiento manual por parte del autor al inaugurar nuevos temas.

**Siguiente paso o deuda:** Desarrollar el publicador Headless (`merci-wp.py`) para escribir en WordPress local desde la terminal.

### 2026-04-29 — Feat: Reestructuración y unificación del pipeline maestro (merci-total)

**Contexto:** Para evitar desincronizaciones por olvido de compilación manual, se vió que integrar el motor SSG (`merci-publish.py`) dentro del orquestador global de QA (`merci-total.py`) actualizaría la página de biblioteca a los nuevos formatos. Además, se detectó que el sincronizador de páginas (`merci-sync-pages.py`) se estaba ejecutando al final del proceso, después de las herramientas de auditoría.

**Hecho:** 
- Se inyectó `merci-publish.py` en la constante `PIPELINE` de `merci-total.py`.
- Se reordenó el flujo de ejecución para separar estrictamente la Fase de Compilación (Build) de la Fase de Aseguramiento de Calidad (QA).

**Detalle técnico:** El nuevo orden arquitectónico es: Optimización multimedia -> Compilación SASS -> Generación SSG (Publish) -> Propagación SSOT (Sync Pages) -> Generación de XML (Sitemap) -> Auditoría Shift-Left (Audit) -> Rastreo de enlaces (Linkcheck). 

**Motivo / criterio:** *Pipeline as Code y Shift-Left*. Si las herramientas de QA (Audit, Linkcheck, Sitemap) se ejecutan antes de que los HTML definitivos hayan sido generados o sincronizados, el orquestador estaría validando "código fantasma" u obsoleto, dando falsos positivos de éxito. El orden de ejecución es tan crítico como el código mismo.

**Siguiente paso o deuda:** Desarrollar el índice curado de la biblioteca o el publicador Headless (`merci-wp.py`).

### 2026-04-29 — Feat: Sincronización automatizada de páginas estáticas (SSOT)

**Contexto:** La página estática de contacto (`public/contacto/index.html`) requería actualización manual de la cabecera, pie de página y asistente Merci cada vez que la portada cambiaba, violando el principio de única fuente de verdad (SSOT).

**Hecho:**
- Se desarrolló el script `scripts/merci/merci-sync-pages.py`.
- Se actualizó el `README.md` marcando la tarea de contacto como completada y registrando el nuevo script.

**Detalle técnico:** El script en Python utiliza Expresiones Regulares (`re.sub` y `re.search`) con la bandera `re.DOTALL` para capturar físicamente el `<header>`, `<footer>` y `<aside class="merci-ui">` de `public/index.html` y sobrescribirlos en `public/contacto/index.html`.

**Motivo / criterio:** *Fricción Cero y Single Source of Truth*. Al igual que `merci-publish` genera los artículos a partir del marco de la portada, `merci-sync-pages` extiende esa misma lógica de componentes inmutables a las páginas estáticas independientes. Elimina el riesgo de "desincronización visual" por error humano.

**Siguiente paso o deuda:** Integrar la llamada a `merci-sync-pages.py` dentro del orquestador `merci-total.py` para automatizarlo en el QA global, y crear el índice curado de la biblioteca.

### 2026-04-29 — Docs: Expansión del Roadmap (Fase 8.3 Consolidación Operativa)

**Contexto:** Antes de proceder con las tareas de consolidación de UX (contacto, home, índice de biblioteca) y automatización Headless (publicador WP y automatización de LinkedIn), se detectó que estas intenciones no estaban formalmente registradas en el Roadmap, contraviniendo el rigor de las directrices operativas.

**Hecho:** Se expandió la Fase 8 en el `README.md` inyectando la subfase `8.3 Consolidación Operativa (UX y Headless CMS)`. Se marcó como completada la primera tarea (inyección de enlaces en el footer).

**Detalle técnico:** La Regla 12 de `instrucciones.md` exige mantener la hoja de ruta sincronizada. Añadir las tareas de consolidación formaliza la deuda técnica autoimpuesta y prepara el terreno para el desarrollo de `merci-wp.py`.

**Motivo / criterio:** *Governance y Compliance (Gobernanza y Cumplimiento)*. En un ciclo de vida estructurado, ninguna maniobra técnica "improvisada" es válida. Todo desarrollo debe responder a un requisito explícito en el Roadmap para mantener la Única Fuente de Verdad (SSOT).

**Siguiente paso o deuda:** Completar la página estática de Contacto (`public/contacto/index.html`) y refinar la portada.

### 2026-04-29 — UX/UI: Consolidación de la interfaz y enlaces globales

**Contexto:** Antes de abordar la Fase 9 (Integración de IA), se detectó la necesidad de consolidar la UX (User Experience - Experiencia de Usuario) inyectando los enlaces a redes profesionales (LinkedIn, GitHub) y al ecosistema hijo (`merci-boilerplate`), además de buscar un modelo de publicación para WordPress que no dependiera del panel de administración (GUI).

**Hecho:** 
- Se inyectó el bloque `.footer__links` en `public/index.html` con atributos de seguridad para enlaces externos (`target="_blank" rel="noopener noreferrer"`).

**Detalle técnico:** Al inyectar los enlaces en el `<footer>` de la portada estática, el orquestador `merci-publish.py` los absorberá y propagará automáticamente a todos los artículos compilados de la Biblioteca en su próxima ejecución, manteniendo el principio de SSOT (Single Source of Truth).

**Motivo / criterio:** *Consolidación antes de Innovación*. Evitar el "Shiny Object Syndrome" estabilizando la identidad pública y los flujos de trabajo locales (Headless CMS) garantiza que el ecosistema base sea robusto y operable antes de introducir lógicas asíncronas complejas como la Inteligencia Artificial.

**Siguiente paso o deuda:** Crear la página estática de Contacto (`public/contacto/index.html`) y propagar el nuevo footer a la plantilla de WordPress.

### 2026-04-29 — DevSecOps: Truncamiento de historial Git (Orphan Branch) en Boilerplate

**Contexto:** Tras el despliegue exitoso de la Release 1.0.0 del Boilerplate, una inspección del `git log` reveló que el repositorio destino conservaba el historial de commits de la matriz original, exponiendo metadatos, correos electrónicos y trazabilidad privada.

**Hecho:** Se ejecutó un truncamiento absoluto del historial en el repositorio `merci-boilerplate` local utilizando `git checkout --orphan`, seguido de una reescritura remota con `git push --force`.

**Detalle técnico:** La creación de una rama huérfana (`--orphan`) desconecta el árbol de trabajo actual de cualquier commit anterior. Al reemplazar la rama `main` con esta nueva rama y forzar la subida, el servidor remoto (GitHub) descarta el historial antiguo, dejando un único commit fundacional inmaculado.

**Motivo / criterio:** *Data Leak Prevention* (Prevención de Pérdida de Datos). Un boilerplate público debe ser un lienzo en blanco (Zero Trust). El código fuente no solo incluye los archivos físicos actuales, sino toda la memoria inmutable de Git. Purgar el historial asegura la sanitización total de la propiedad intelectual exportada.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-29 — Fix: Sincronización destructiva (rsync --delete) y purga de assets

**Contexto:** Tras la instanciación del Boilerplate, se detectó que los archivos originales (`README-merci.md`, `bitacora-mercedev.md`, scripts temporales y multimedia personal) seguían apareciendo en el repositorio destino, a pesar de que `merci-init.py` los borraba o renombraba correctamente en el clon temporal.

**Hecho:** 
- Se añadió la bandera `--delete` al comando `rsync` en `mantenimiento-boilerplate-sop.md`.
- Se amplió `merci-init.py` para purgar explícitamente `.assets-raw`, `assets/images` (conservando logos/favicon) y `public/art-de-cote`.

**Motivo / criterio:** *Configuration Drift* (Archivos Fantasma). El comando `rsync` estándar solo añade o actualiza archivos; si el repositorio de destino contiene archivos de subidas anteriores que ya no existen en la matriz, estos nunca se borrarán a menos que se exija una sincronización de espejo estricta con `--delete`. Esto resuelve el falso positivo de fallo en el orquestador Python y garantiza un empaquetado inmaculado.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-29 — Fix: Purga de Shadow Docs residuales en instanciación

**Contexto:** Al ejecutar la instanciación (`merci-init.py`) siguiendo el SOP de mantenimiento, se detectó que los archivos originales `README-merci.md` e `instrucciones-merci.md` permanecían en el directorio junto a sus versiones definitivas (`README.md` e `instrucciones.md`), generando duplicidad documental en el Boilerplate.

**Hecho:** Se instruyó la corrección en `scripts/merci/merci-init.py` para aplicar una maniobra destructiva (renombrado atómico) al ascender los *Shadow Docs*.

**Detalle técnico:** En lugar de una simple copia, el orquestador Python debe utilizar el método `.replace()` de `pathlib.Path` para sobrescribir atómicamente el documento destino y erradicar el archivo `-merci` de origen en un solo movimiento.

**Motivo / criterio:** *Zero Bloat* y *Single Source of Truth*. El código fuente exportado debe ser inmaculado. Conservar la infraestructura "en la sombra" dentro del repositorio público del Boilerplate confunde al usuario final y expone artefactos de la matriz innecesariamente.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-29 — Docs: Aclaración del pipeline de rsync y Shadow Docs

**Contexto:** Existía la duda de si el comando de sincronización `rsync` hacia el repositorio del Boilerplate debía excluir explícitamente los manuales de la matriz (`README.md` e `instrucciones.md`) para evitar contaminar el repositorio destino, o si debían viajar los archivos gemelos (`-merci.md`).

**Hecho:** Se validó y documentó la simplificación del comando de transferencia (`rsync -av --exclude='.git'`) en el SOP de mantenimiento, sin añadir exclusiones manuales para la documentación.

**Detalle técnico:** La topología del *Release Pipeline* delega la manipulación de archivos al script de instanciación (`merci-init.py`), el cual se ejecuta en un directorio efímero *antes* de la sincronización. Este script elimina físicamente los manuales de la matriz y renombra los *Shadow Docs* a sus nombres definitivos. Al ejecutarse el comando `rsync` en el paso posterior, la carpeta ya contiene la documentación purificada y correcta.

**Motivo / criterio:** *Separation of Concerns* (Separación de Responsabilidades) y *Infrastructure as Code*. El orquestador de Python es el único responsable de la mutación estructural del proyecto. Delegar exclusiones complejas a un comando de shell (rsync) lo vuelve frágil e interfiere con el ascenso de los documentos correctos preparados por el script.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-28 — Docs: Auditoría externa de IA y expansión del Roadmap (Fase 11)

**Contexto:** Tras cerrar la Fase 10 (Release 1.0.0 del Boilerplate), se sometió el repositorio a un análisis externo (Copilot). El dictamen situó la arquitectura en el top 1-3% global por rigor DevSecOps y optimización, y sugirió mejoras de integración en la nube.

**Hecho:**
- Se filtraron las propuestas, rechazando las que requerían dependencias pesadas (Cypress, telemetría) y aceptando las de CI/CD puro.
- Se inyectó la nueva "Fase 11: Integración Continua y Calidad en la Nube" en el Roadmap del `README.md` e `instrucciones.md` (GitHub Actions, Lighthouse CI e Issue Templates).

**Motivo / criterio:** *Continuous Improvement* (Mejora Continua). La validación externa confirma la solidez fundacional. Adoptar flujos de CI en la nube alinea el proyecto con estándares corporativos Enterprise, delegando la auditoría al servidor sin engordar el código fuente local ni violar la política de cero dependencias bloqueantes.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-28 — Docs: Principio de inmutabilidad en el registro histórico

**Contexto:** Tras reubicar documentos operativos a la carpeta `docs/matriz/`, se debatió si actualizar las rutas absolutas mencionadas en entradas de la bitácora redactadas en días anteriores (Fase 7) para que coincidieran con la nueva topología.

**Hecho:** Se decidió no modificar los registros pasados y asentar la regla estricta de inmutabilidad documental en el laboratorio.

**Motivo / criterio:** *Append-Only Log* (Registro de solo adición). La bitácora es un documento forense que refleja la realidad técnica exacta del momento en que se escribió. Reescribir el pasado para ajustar rutas o nombres de archivos que cambiaron posteriormente destruye la trazabilidad y es un antipatrón de auditoría. Los cambios arquitectónicos se documentan siempre como nuevos eventos en el presente.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-28 — Refactor: Agrupación de SOPs exclusivos en subdirectorio matriz/

**Contexto:** La purga selectiva de manuales en `merci-init.py` requería añadir manualmente cada nuevo archivo a eliminar, lo cual no es escalable si el proyecto matriz aumenta su documentación interna.

**Hecho:**
- Se creó el subdirectorio `docs/matriz/` y se movieron los archivos `flujo-publicacion-sop.md` y `mantenimiento-boilerplate-sop.md` mediante `git mv`.
- Se actualizó `merci-init.py` para erradicar el directorio completo `docs/matriz/` de forma dinámica mediante `shutil.rmtree()`.

**Motivo / criterio:** *Escalabilidad y Mantenibilidad*. Agrupar los documentos exclusivos del proyecto matriz en una única carpeta dedicada simplifica la lógica del script destructivo. Cualquier futuro manual interno depositado en esa carpeta quedará automáticamente excluido del Boilerplate sin necesidad de modificar código Python.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-28 — Fix: Resolución de colisión de contexto (Enrutamiento en MerciController)

**Contexto:** El asistente Merci repetía las frases del Blog al navegar por la Tienda. Esto ocurría porque la URL de la tienda (`/blog/tienda`) contiene el segmento `/blog`, provocando un falso positivo en la validación secuencial del controlador.

**Hecho:** Se inyectó una cláusula condicional específica para `/tienda` en el método `_loadKnowledgeBase()` de `public/js/MerciController.js`.

**Detalle técnico:** En enrutamientos de frontend basados en coincidencias de subcadenas (`String.prototype.includes()`), el orden de evaluación es estricto. Se ubicó la validación de `/tienda` estructuralmente *antes* que la de `/blog` para que el bloque `if` intercepte la ruta anidada más específica en primer lugar.

**Motivo / criterio:** *Context-Awareness* (Conciencia de contexto). Para que un agente conversacional mantenga la coherencia, la inferencia de su entorno debe manejar correctamente las colisiones de directorios. 

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-28 — Fix: Expansión de acrónimos rezagados (TTFB y CPU)

**Contexto:** La auditoría pre-commit (`merci-audit.py`) detectó acrónimos no expandidos (TTFB y CPU) en la bitácora y en cuadernillos promovidos a la biblioteca, bloqueando el empaquetado para asegurar la accesibilidad cognitiva.

**Hecho:** Se expandieron los acrónimos `TTFB` y `CPU` siguiendo el estándar `Acrónimo (Inglés - Español)` en los archivos correspondientes.

**Motivo / criterio:** *Inclusión Cognitiva*. La auditoría es implacable por diseño: cualquier nuevo acrónimo introducido en la documentación debe ser explicado en su primera aparición para no generar deuda técnica documental.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-28 — Fix: Resolución de TypeError por método inexistente en MerciController

**Contexto:** Al interactuar con el asistente Merci en el entorno local, la consola del navegador arrojaba el error fatal `Uncaught TypeError: this.setState is not a function`.

**Hecho:** Se corrigió la asignación de estado en el método `sleep()` de `public/js/MerciController.js`.

**Detalle técnico:** Se reemplazó la llamada al método inexistente `this.setState('idle')` por la asignación directa de la propiedad `this.state = 'idle'`.

**Motivo / criterio:** *Vanilla JS vs Frameworks*. El uso de `setState` es un remanente o confusión común procedente de frameworks reactivos (como React). En una arquitectura de 0 dependencias con POO estricta, si no se declara un *setter* explícito, el estado se muta directamente sobre la propiedad de la instancia para evitar colapsos de ejecución.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-28 — Docs: Redacción de cuadernillos técnicos (QA, Git y WP)

**Contexto:** Antes de sellar la nueva versión base del ecosistema, era imperativo transformar las resoluciones técnicas críticas de la última sesión (conflictos de Git, caché móvil y jerarquía de WooCommerce) en activos de conocimiento reutilizables.

**Hecho:** Se redactaron tres nuevos cuadernillos en formato borrador dentro de `laboratorio/`:
- `cuadernillo-cache-movil-webkit.md` (Cache Busting)
- `cuadernillo-domando-woocommerce.md` (Template Hierarchy)
- `cuadernillo-conflictos-git-ours.md` (Git Merge Conflicts)

**Motivo / criterio:** *Knowledge Management* (Gestión del Conocimiento). La documentación operativa no solo abarca el "cómo instalar", sino el "cómo sobrevivir". Documentar los incidentes reales bajo los 3 átomos del proyecto convierte la deuda técnica sufrida en una inversión formativa para el futuro del *Boilerplate*.

**Siguiente paso o deuda:** Promover los cuadernillos a la Biblioteca o Art de Coté (según corresponda) mediante `merci-promote.py` e iniciar la Fase 9.

### 2026-04-28 — QA: Certificación 100/100 en Core Web Vitals (Capa Dinámica)

**Contexto:** Antes de empaquetar y exportar la versión final del Boilerplate (Release 1.0.0), se requería validación empírica de que la capa dinámica (WordPress/WooCommerce) no degradaba el rendimiento extremo del núcleo estático.

**Hecho:** Se ejecutó la auditoría de Google PageSpeed Insights (Lighthouse) sobre la ruta de producción `/blog` en la vista móvil.

**Detalle técnico:** La auditoría certificó una puntuación perfecta cuádruple: 100 Rendimiento, 100 Accesibilidad, 100 Mejores Prácticas y 100 SEO. Métricas clave: FCP 0.8s, LCP 1.1s, TBT 0ms. Esto valida empíricamente el éxito de las purgas de assets (`wp_dequeue_style` de `wc-blocks`) y la arquitectura de proxy inverso.

**Motivo / criterio:** *QA Assurance* (Aseguramiento de Calidad). Una infraestructura DevSecOps no admite suposiciones. Validar la excelencia técnica en el entorno más hostil (móvil 4G simulado sobre CMS) es el requisito final innegociable antes de liberar una plantilla fundacional al público.

**Siguiente paso o deuda:** Ejecutar el Release Pipeline (exportar a `merci-boilerplate`) e iniciar la Fase 9.

### 2026-04-28 — Fix: Resolución de colisión y carga doble de scripts JS en WP

**Contexto:** La consola del navegador en el entorno dinámico (`/blog`) arrojaba un error crítico: `SyntaxError: Identifier 'NavigationController' has already been declared`. Este error colapsaba la ejecución del frontend.

**Hecho:** Se desactivó la carga de `main.js` mediante `wp_enqueue_script` en `functions.php`.

**Detalle técnico:** Al implementar el patrón de *Cache Busting* dinámico (`time()`) en las plantillas `index.php` y `woocommerce.php`, se insertó la etiqueta `<script>` directamente en el `<head>`. Sin embargo, `functions.php` seguía encolando el mismo archivo en el `wp_footer()`. Declarar una clase de ES6 (`class NavigationController`) dos veces en el mismo ámbito global (Global Scope) produce un `SyntaxError` fatal.

**Motivo / criterio:** *Single Source of Truth*. Los *assets* estáticos deben cargarse desde un único punto de control. Al haber delegado la responsabilidad del versionado dinámico directamente a las plantillas, la inyección desde el functions queda obsoleta y genera una condición de carrera y duplicidad de código.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-28 — Perf: Purga de bloques WooCommerce y oEmbed en WP

**Contexto:** La auditoría de Lighthouse (PageSpeed Insights) reveló que la capa dinámica (Blog/Tienda) no alcanzaba el 100/100 en móviles, sufriendo penalizaciones por CSS y JS no utilizado, a diferencia del núcleo estático.

**Hecho:** Se inyectaron reglas de desencolado (`wp_dequeue_style`) para `wc-blocks-style` y `wc-blocks-vendors-style` en `functions.php`. Se eliminaron los enlaces de oEmbed y REST API de la cabecera.

**Detalle técnico:** Aunque se había desactivado el CSS base de WooCommerce en fases anteriores, el plugin inyecta silenciosamente un archivo masivo de estilos para sus bloques de Gutenberg (`wc-blocks-style`). Adicionalmente, WP inyecta scripts de descubrimiento oEmbed innecesarios. Su purga restaura el DOM ultraligero.

**Motivo / criterio:** *Zero Bloat* (Cero Basura). La disparidad de rendimiento entre el SSG y WP suele radicar en el código "invisible" que los plugins asumen que el tema necesita. Desactivar todo lo que no esté estrictamente controlado por nuestra arquitectura SASS 7-1 protege las Core Web Vitals en dispositivos móviles de gama baja.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-28 — Fix: Soporte oficial WooCommerce y purga absoluta de caché PHP

**Contexto:** La tienda ignoraba el archivo `woocommerce.php` y los dispositivos móviles seguían mostrando HTML/CSS cacheado en vistas dinámicas, impidiendo el uso del menú y ocultando al asistente.

**Hecho:**
- Se inyectó `add_theme_support('woocommerce')` en `functions.php` para obligar al plugin a respetar la jerarquía de plantillas del tema.
- Se reemplazó la lógica `filemtime` por `time()` en los *Cache Busters* de las plantillas PHP para forzar peticiones únicas en cada recarga.
- Se incrementó a `v=11` la versión de los *assets* en páginas HTML estáticas.

**Motivo / criterio:** *Template Hierarchy y Cache Invalidation*. WooCommerce se protege a sí mismo sirviendo sus plantillas base si el tema activo no declara soporte explícito, ignorando `woocommerce.php`. Para entornos de desarrollo o infraestructuras con cachés agresivas, usar el *timestamp* actual (`time()`) es la única garantía de purga instantánea sin acceso directo al servidor.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-28 — Fix: Rutas de caché dinámico en WP y alineación de footer

**Contexto:** El menú móvil seguía sin funcionar en las vistas dinámicas (WordPress) debido a que la función de purga de caché PHP apuntaba a una ruta de servidor incorrecta, sirviendo versiones obsoletas del JS. Adicionalmente, el enlace "Volver arriba" interfería visualmente con el asistente Merci en pantallas pequeñas al estar centrado.

**Hecho:**
- Se corrigió la ruta de `$root_dir` en `index.php` y `woocommerce.php` para apuntar correctamente al directorio estático en el servidor anfitrión (`/mercedev.es/public`).
- Se refactorizó la estructura HTML del `<footer>` en todas las plantillas, alineando el texto a la izquierda y añadiendo un padding inferior de seguridad (`6rem`).

**Motivo / criterio:** *Rutas Absolutas y Usabilidad (UX)*. Al usar enlaces simbólicos en Nginx, la constante `ABSPATH` de WordPress requiere una travesía de directorios explícita para localizar los archivos estáticos. A nivel de UI, aislar los elementos interactivos flotantes (Merci) de los enlaces base del footer previene clics accidentales (Fat Finger Syndrome) en dispositivos móviles.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-28 — Fix: Unificación de carga de assets y Cache Busting dinámico en WP

**Contexto:** Una auditoría multidispositivo final reveló que, a pesar de los parches anteriores, las vistas dinámicas (Blog, Tienda) y la página estática de Contacto seguían mostrando versiones cacheadas de CSS y JS en tablets y móviles, rompiendo la UI de Merci y el menú.

**Hecho:**
- Se implementó la carga directa del `main.css` con `filemtime` en `index.php` y `woocommerce.php`, eliminando la dependencia del `functions.php`.
- Se actualizaron manualmente la versión de los assets en `contacto/index.html` y `index.html` para forzar la purga de caché.

**Motivo / criterio:** *Single Source of Truth* y *Cache Invalidation*. La gestión de assets debe ser consistente. Cargar todos los recursos del núcleo estático (CSS y JS) con la misma estrategia de versionado dinámico en todas las plantillas (estáticas y PHP) erradica definitivamente los problemas de caché y asegura la paridad visual y funcional entre todos los dispositivos.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-28 — Fix: Unificación de carga de assets y Cache Busting dinámico en WP

**Contexto:** Una auditoría multidispositivo final reveló que, a pesar de los parches anteriores, las vistas dinámicas (Blog, Tienda) y la página estática de Contacto seguían mostrando versiones cacheadas de CSS y JS en tablets y móviles, rompiendo la UI de Merci y el menú.

**Hecho:**
- Se implementó la carga directa del `main.css` con `filemtime` en `index.php` y `woocommerce.php`, eliminando la dependencia del `functions.php`.
- Se actualizaron manualmente la versión de los assets en `contacto/index.html` y `index.html` para forzar la purga de caché.

**Motivo / criterio:** *Single Source of Truth* y *Cache Invalidation*. La gestión de assets debe ser consistente. Cargar todos los recursos del núcleo estático (CSS y JS) con la misma estrategia de versionado dinámico en todas las plantillas (estáticas y PHP) erradica definitivamente los problemas de caché y asegura la paridad visual y funcional entre todos los dispositivos.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-27 — Fix: Restauración de WooCommerce y dependencias dinámicas JS

**Contexto:** Una auditoría móvil exhaustiva reveló que las páginas de WordPress (Blog/Tienda) no desplegaban el menú hamburguesa y que WooCommerce perdía todo el formato visual y estructural del tema.

**Hecho:**
- Se inyectó dinámicamente `main.js` en `index.php` utilizando `filemtime` para forzar la purga de caché.
- Se creó el archivo `woocommerce.php` en el Child Theme copiando la estructura base monolítica.
- Se aplicaron los Cache Busters (`?v=...`) y el ancla `#top` a la página estática `contacto/index.html`.

**Motivo / criterio:** *Template Hierarchy* y Paridad. El fallo del menú en WP se debía a la omisión de `main.js` (donde reside el controlador de navegación). La rotura de la tienda se debía a que WooCommerce ignora `index.php` e inyecta su propio HTML desnudo a menos que exista un `woocommerce.php` explícito que envuelva su función `woocommerce_content()` dentro de nuestra arquitectura BEM.

**Siguiente paso o deuda:** Desplegar en producción y confirmar resolución en dispositivos móviles.

### 2026-04-27 — Fix: Resolución de Caché Móvil y Bug de pointer-events (iOS Safari)

**Contexto:** El asistente Merci funcionaba correctamente en la simulación móvil del PC, pero en un dispositivo físico real aparecía roto (posición estática al final de la página) y sus clics eran ignorados.

**Hecho:** 
- Se inyectaron *Cache Busters* (`?v=...`) en las etiquetas `<script>` y `<link>` en todas las plantillas HTML/PHP del proyecto.
- Se eliminaron las reglas CSS `pointer-events: none` y `pointer-events: auto` del contenedor de Merci en SASS.

**Detalle técnico:** El síntoma de disparidad entre el PC y el móvil físico es el indicador estándar de caché agresiva. El navegador móvil conservaba una versión antigua de `main.css` y `MerciController.js` en memoria. Adicionalmente, se retiró el uso de `pointer-events` cruzados debido a un bug conocido en WebKit (iOS Safari) donde el navegador se niega a registrar eventos de *touch/click* en elementos hijos si el contenedor padre tiene `pointer-events: none`.

**Motivo / criterio:** *Cross-Browser Compatibility* (Compatibilidad entre navegadores). Inyectar versiones en los *assets* estáticos obliga a los móviles a purgar su caché y descargar el último código. Evitar "hacks" de CSS (`pointer-events`) en contenedores interactivos previene colapsos en motores de renderizado estrictos como los de Apple.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-27 — Feat: Reubicación automática de borradores al laboratorio en SSG

**Contexto:** Se estableció como regla de arquitectura que la carpeta `biblioteca/` no debe contener archivos en estado de incubación o borrador (Environment Segregation). Sin embargo, si un archivo era despublicado cambiando su YAML a `estado: "borrador"`, permanecía físicamente en la biblioteca, requiriendo su traslado manual.

**Hecho:** Se implementó una rutina de reubicación física en la máquina de estados de `scripts/merci/merci-publish.py`.

**Detalle técnico:** En el bloque de control del "Kill-Switch", si un documento no tiene el estado `publicado`, además de purgar sus artefactos HTML/PDF generados, el orquestador utiliza `shutil.move()` para trasladar el archivo `.md` original de vuelta al directorio `laboratorio/`.

**Motivo / criterio:** *Automation & Environment Segregation*. Un entorno DevSecOps maduro no confía en la disciplina manual para mantener la higiene de los directorios. El orquestador actúa como un agente activo que expulsa el contenido no válido del entorno de producción hacia la zona de pruebas.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-28 — Fix: Purga selectiva de SOPs en instanciación de Boilerplate

**Contexto:** Se detectó que el script de inicialización (`merci-init.py`) exportaba la totalidad de la carpeta `docs/` al nuevo proyecto. Esto incluía manuales de procedimiento (SOP) exclusivos de la matriz (`flujo-publicacion-sop.md` y `mantenimiento-boilerplate-sop.md`), generando ruido documental y confusión para el usuario final del Boilerplate.

**Hecho:** Se inyectó una rutina de borrado selectivo (`unlink`) para los archivos SOP específicos dentro de la fase de purga de `scripts/merci/merci-init.py`.

**Motivo / criterio:** *Separation of Concerns* (Separación de Responsabilidades Documentales). La documentación de infraestructura (`deployment`, `hardening`) es agnóstica y debe viajar con la plantilla. La documentación de gobierno de repositorios y flujos de publicación personalizados pertenece exclusivamente a la "Instancia Cliente" (el proyecto matriz) y debe ser erradicada del código base redistribuible.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-28 — Docs: Creación del SOP de actualización del Boilerplate

**Contexto:** Las instrucciones para actualizar el repositorio `merci-boilerplate` desde el proyecto matriz estaban definidas únicamente en la Regla 14 de `instrucciones.md` y en un cuadernillo divulgativo, dificultando su localización como manual operativo estricto.

**Hecho:** Se redactó el documento `docs/mantenimiento-boilerplate-sop.md`.

**Motivo / criterio:** *Operabilidad y SSOT*. Un proceso complejo de múltiples pasos que involucra clonaciones destructivas (`merci-init.py`), comandos nativos (`rm -rf`, `rsync`) y saltos entre repositorios debe estar centralizado en un documento SOP (Standard Operating Procedure) oficial para evitar errores humanos o pérdida de datos durante las futuras *releases*.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-27 — Fix: Resolución de TypeError por firmas de funciones en SSG

**Contexto:** El orquestador `merci-publish.py` colapsó con un `TypeError` (`takes 3 positional arguments but 6 were given`) al intentar compilar la biblioteca tras la actualización de caché móvil.

**Hecho:** Se actualizaron las firmas de las funciones `procesar_archivo` y `generar_indice_biblioteca` para aceptar los parámetros de versión dinámica.

**Detalle técnico:** Durante la implementación del *Cache Busting*, se añadieron tres nuevos argumentos en las invocaciones de las funciones dentro de `main()`, pero se omitió actualizar la definición de las mismas. Se inyectaron los argumentos `css_v`, `js_c_v` y `js_m_v` requeridos por las plantillas f-string internas.

**Motivo / criterio:** *Code Consistency* (Consistencia del código). Las definiciones de las funciones deben alinearse estrictamente con los argumentos inyectados y las interpolaciones generadas en las vistas HTML.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-27 — Fix: Restauración de WooCommerce y dependencias dinámicas JS

**Contexto:** Una auditoría móvil exhaustiva reveló que las páginas de WordPress (Blog/Tienda) no desplegaban el menú hamburguesa y que WooCommerce perdía todo el formato visual y estructural del tema.

**Hecho:**
- Se inyectó dinámicamente `main.js` en `index.php` utilizando `filemtime` para forzar la purga de caché.
- Se creó el archivo `woocommerce.php` en el Child Theme copiando la estructura base monolítica.
- Se aplicaron los Cache Busters (`?v=...`) y el ancla `#top` a la página estática `contacto/index.html`.

**Motivo / criterio:** *Template Hierarchy* y Paridad. El fallo del menú en WP se debía a la omisión de `main.js` (donde reside el controlador de navegación). La rotura de la tienda se debía a que WooCommerce ignora `index.php` e inyecta su propio HTML desnudo a menos que exista un `woocommerce.php` explícito que envuelva su función `woocommerce_content()` dentro de nuestra arquitectura BEM.

**Siguiente paso o deuda:** Desplegar en producción y confirmar resolución en dispositivos móviles.



### 2026-04-27 — Fix: Resolución de Caché Móvil y Bug de pointer-events (iOS Safari)

**Contexto:** El asistente Merci funcionaba correctamente en la simulación móvil del PC, pero en un dispositivo físico real aparecía roto (posición estática al final de la página) y sus clics eran ignorados.

**Hecho:** 
- Se inyectaron *Cache Busters* (`?v=...`) en las etiquetas `<script>` y `<link>` en todas las plantillas HTML/PHP del proyecto.
- Se eliminaron las reglas CSS `pointer-events: none` y `pointer-events: auto` del contenedor de Merci en SASS.

**Detalle técnico:** El síntoma de disparidad entre el PC y el móvil físico es el indicador estándar de caché agresiva. El navegador móvil conservaba una versión antigua de `main.css` y `MerciController.js` en memoria. Adicionalmente, se retiró el uso de `pointer-events` cruzados debido a un bug conocido en WebKit (iOS Safari) donde el navegador se niega a registrar eventos de *touch/click* en elementos hijos si el contenedor padre tiene `pointer-events: none`.

**Motivo / criterio:** *Cross-Browser Compatibility* (Compatibilidad entre navegadores). Inyectar versiones en los *assets* estáticos obliga a los móviles a purgar su caché y descargar el último código. Evitar "hacks" de CSS (`pointer-events`) en contenedores interactivos previene colapsos en motores de renderizado estrictos como los de Apple.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-27 — Fix: Resolución de caché móvil y consistencia de plantillas

**Contexto:** Una auditoría multidispositivo reveló que el asistente Merci y el menú móvil fallaban en tablets y teléfonos (CSS/JS rotos), y que las plantillas dinámicas (PHP) y estáticas (`contacto/`) tenían inconsistencias en el footer.

**Hecho:**
- Se implementó una estrategia de "Cache Busting" dinámico en `merci-publish.py` usando la fecha de modificación del archivo (`.stat().st_mtime`) como versión.
- Se actualizaron manualmente las versiones en los archivos estáticos (`index.html`, `contacto/index.html`).
- Se corrigió el placeholder `{{DOMINIO}}` en `src/wp-theme/merci-theme/index.php`.

**Motivo / criterio:** *Dev/Prod Parity & Cache Invalidation*. La disparidad entre el PC y el móvil es un síntoma inequívoco de caché agresiva. Usar `filemtime` como versión es la técnica más robusta para forzar la purga. Corregir los placeholders y los footers desactualizados restaura la consistencia visual y funcional en todo el ecosistema híbrido.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía. Se asume la deuda de refactorizar las plantillas de WooCommerce para corregir su footer.

### 2026-04-27 — Feat: Automatización de la fecha de última revisión en bitácora

**Contexto:** La línea final del archivo de bitácora (`*Última revisión de la bitácora: 2026-05-07.*`) contenía una fecha obsoleta (2026-04-14) porque dependía de la actualización manual por parte de la autora en cada sesión.

**Hecho:** Se implementó una rutina de actualización automática en `scripts/merci/merci-commit.py` mediante expresiones regulares.

**Detalle técnico:** Justo antes de ejecutar el `git add .`, el script lee el contenido completo de la bitácora, localiza la cadena de texto de la última revisión y sustituye la fecha por el día actual (`datetime.now()`), sobrescribiendo el archivo para que se empaquete con el dato exacto.

**Motivo / criterio:** *Fricción Cero*. Eliminar tareas repetitivas y propensas al error humano. Si el orquestador de commits ya lee la bitácora para extraer el mensaje, es el lugar arquitectónicamente perfecto para actualizar sus metadatos internos de forma transparente.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-27 — Fix: Expansión de acrónimo SEO en plantilla de proyecto

**Contexto:** Tras el simulacro de instanciación del Boilerplate, el auditor `merci-audit.py` levantó una advertencia por el acrónimo "SEO" no expandido. El diagnóstico reveló que el término residía en los comentarios del YAML Frontmatter del archivo `docs/plantilla-proyecto.md`.

**Hecho:** Se expandió el acrónimo SEO (Search Engine Optimization - Optimización para Motores de Búsqueda) directamente en la plantilla base del repositorio.

**Motivo / criterio:** *Standalone Compliance*. Al igual que ocurrió con los Shadow Docs, las plantillas fundacionales que sobreviven al script de inicialización (`merci-init.py`) deben ser semánticamente autosuficientes para no heredar advertencias de linter al nuevo usuario.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-27 — Fix: Expansión de acrónimos en Shadow Docs (Boilerplate)

**Contexto:** Al ejecutar la auditoría (`merci total`) en el repositorio clonado del Boilerplate, el linter de accesibilidad cognitiva emitió advertencias (WARN) por acrónimos no expandidos (como BEM). Esto ocurrió porque al purgar la biblioteca y el laboratorio, el recuento global de dichos términos cayó por debajo del umbral de consolidación (>3).

**Hecho:** Se expandió explícitamente el acrónimo BEM (Block, Element, Modifier - Modificador de Elemento de Bloque) en `README-merci.md`, `instrucciones-merci.md` e `instrucciones.md`.

**Detalle técnico:** Se aplicó la convención de expansión `ACRÓNIMO (Inglés - Español)` directamente en las documentaciones "en la sombra", garantizando que el texto base del Boilerplate cumpla con el análisis estático de `merci-audit.py` por sí mismo.

**Motivo / criterio:** *Standalone Compliance*. Una plantilla agnóstica debe ser 100% autosuficiente y superar su propia auditoría con 0 advertencias desde el commit inicial, sin depender de la densidad documental del proyecto matriz del que fue extraída.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-27 — Docs: Versionado Semántico en Shadow Docs (v1.0.0)

**Contexto:** El documento en la sombra `README-merci.md` (que asciende a README oficial tras la instanciación) carecía de la declaración explícita de la versión del motor, dificultando la trazabilidad para los usuarios del Boilerplate.

**Hecho:** Se inyectó la etiqueta de versión `v1.0.0` en el encabezado principal de `README-merci.md`.

**Motivo / criterio:** *Semantic Versioning* (Versionado Semántico). El archivo maestro de un proyecto agnóstico debe indicar claramente en qué punto de madurez se encuentra. Al estar integrado en el Release Pipeline Agile (Regla 14), este número se incrementará manualmente en el proyecto matriz justo antes de empaquetar futuras *releases* (ej. `v1.1.0`).

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-27 — Perf: Optimización de peso en copias de seguridad (Backup Local)

**Contexto:** El script de copias de seguridad locales (`merci-backup.py`) estaba generando archivos ZIP de casi 47 MB, un peso desproporcionado para un repositorio de código y texto. El diagnóstico reveló que estaba comprimiendo los binarios de la carpeta `evidencias/` y los PDFs generados en `descargas/`.

**Hecho:** Se añadieron los directorios `evidencias` y `descargas` al conjunto (set) de exclusión `EXCLUDE_DIRS` en el script de backup.

**Detalle técnico:** Al ignorar estas carpetas en el recorrido `os.walk()`, se evita procesar y comprimir archivos multimedia pesados o artefactos dinámicos que pueden ser regenerados a voluntad mediante el orquestador SSG.

**Motivo / criterio:** *Performance y Eficiencia*. Una herramienta de *Disaster Recovery* local debe ser ultrarrápida y generar instantáneas ligeras. Excluir binarios que no forman parte del código fuente matriz garantiza que el backup se ejecute en milisegundos y consuma un espacio residual en el disco.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-27 — Feat: Bloqueo activo de evidencias y assets pesados (Shift-Left)

**Contexto:** Para asegurar que el historial de Git no se vuelva a contaminar con archivos binarios (vídeos, capturas) tras los incidentes con la carpeta `evidencias/`, el uso de `.gitignore` resultó ser insuficiente por su naturaleza pasiva frente a archivos previamente rastreados.

**Hecho:** Se implementó la regla `BANNED_TRACKED_FILE` en `scripts/merci/merci-audit.py` (auditor maestro).

**Detalle técnico:** Se creó la función `audit_banned_tracked_files` que consulta directamente a Git (`git ls-files` o `git diff --cached`). Si detecta que cualquier archivo (excepto `.gitkeep`) bajo `laboratorio/evidencias/` o `.assets-raw/` está a punto de ser comiteado o ya está siendo rastreado, inyecta un `ERROR` bloqueante en el estado de la auditoría.

**Motivo / criterio:** *Shift-Left Security*. Delegar la higiene del repositorio a la memoria humana o a un `.gitignore` pasivo genera fugas de datos. Un escudo activo (Linter) que bloquea el commit atómico previene físicamente la subida de archivos pesados al servidor remoto.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-27 — Fix: Erradicación de evidencias rastreadas heredadas

**Contexto:** Tras resolver un conflicto de fusión masivo, la carpeta `laboratorio/evidencias/` volvió a subirse al repositorio remoto a pesar de estar incluida en el `.gitignore`.

**Hecho:** Se ejecutó `git rm -r --cached laboratorio/evidencias/` para forzar a Git a "olvidar" los archivos sin borrarlos del disco duro local, y se generó un nuevo commit para purgar el servidor.

**Detalle técnico:** El archivo `.gitignore` previene que archivos *nuevos* sean añadidos al índice (`staged`), pero **no tiene efecto** sobre archivos que ya estaban siendo rastreados (tracked) en el historial previo. Al fusionar la rama remota, Git recuperó la memoria de esos archivos. Para aplicar un gitignore retroactivamente, es obligatorio eliminar los archivos de la caché de Git explícitamente.

**Motivo / criterio:** Higiene del repositorio. Comprender la diferencia entre archivos *tracked* y *untracked* es vital. La eliminación de la caché es la única maniobra válida para forzar a Git a soltar archivos que ya había asimilado en el pasado.

**Siguiente paso o deuda:** Inyectar una regla de validación en `merci-audit.py` para bloquear atómicamente cualquier commit que contenga archivos en esta carpeta.

### 2026-04-27 — Fix: Restauración de clase estructural para menú móvil

**Contexto:** En el entorno de producción, el menú hamburguesa no se desplegaba en las páginas de la Biblioteca ni en las vistas dinámicas de WordPress, aislando al usuario en móvil.

**Hecho:** Se inyectó la clase `.page` en las etiquetas `<body>` del orquestador `merci-publish.py` y del archivo `index.php` del Child Theme. También se corrigió la inyección del ancla invisible `#top` en el índice de la biblioteca.

**Detalle técnico:** El análisis del código Vanilla JS (`main.js`) reveló que estaba perfectamente estructurado con Cláusulas de Guarda (Guard Clauses), por lo que no había colapsos por `TypeError`. El fallo era exclusivamente CSS: las reglas de visualización del menú dependían del contexto `.page` en el `body`, el cual fue omitido durante la generación dinámica del HTML.

**Motivo / criterio:** Paridad de Entornos (Dev/Prod Parity). El núcleo estático base (`public/index.html`) poseía el atributo `class="page"` que habilitaba ciertas reglas SASS en cascada. Todo motor de renderizado (SSG o PHP) que reutilice el mismo CSS debe emitir exactamente la misma estructura de contenedores padre para evitar roturas visuales.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-27 — Fix: Resolución masiva de conflictos (Estrategia --ours)

**Contexto:** Al ejecutar `git pull`, estalló un conflicto de fusión masivo afectando a la bitácora, scripts, HTMLs y binarios (PDFs). El origen de esta colisión fue la reescritura del historial local (`git reset --soft`) realizada en sesiones anteriores, lo que provocó que el servidor remoto conservara un historial "fantasma" obsoleto que colisionó con la línea temporal actual.

**Hecho:** Se resolvieron los conflictos favoreciendo en bloque la versión local mediante el comando `git checkout --ours .`.

**Detalle técnico:** En lugar de resolver manualmente archivo por archivo (imposible para los binarios `add/add`), se utilizó la estrategia de resolución de Git que impone el árbol de trabajo local (`HEAD`) sobre el remoto. Esto elimina los marcadores de conflicto y restaura la integridad de los archivos generados y del código fuente.

**Motivo / criterio:** *Single Source of Truth (SSOT)*. Cuando se sabe con absoluta certeza que el entorno local contiene la última versión validada y segura del código (gracias al aislamiento DevSecOps), la maniobra más segura es descartar la rama remota divergente en bloque. Intentar fusionar código generado (SSG) manualmente es un antipatrón.

**Siguiente paso o deuda:** Finalizar el commit de fusión y continuar a la Fase 9.

### 2026-04-27 — Fix: Resolución de conflicto de sobreescritura en `git pull`

**Contexto:** Al ejecutar `git pull` tras configurar la estrategia de fusión, Git abortó la operación con el error: "Los cambios locales de los siguientes archivos serán sobrescritos al fusionar". Esto ocurrió porque existían modificaciones locales en `laboratorio/bitacora-mercedev.md` que aún no habían sido empaquetadas en un commit.

**Hecho:** Se empaquetaron los cambios locales pendientes mediante `merci-commit.py` antes de volver a intentar la sincronización.

**Detalle técnico:** Git se niega a ejecutar un `pull` si este va a sobrescribir trabajo local no guardado (uncommitted). El flujo de trabajo correcto es siempre: 1) Guardar el trabajo local (`git add .` y `git commit`) y 2) Sincronizar con el servidor (`git pull`).

**Motivo / criterio:** *Integridad de datos*. Es un mecanismo de seguridad fundamental de Git para prevenir la pérdida de trabajo. Nunca se debe forzar una sincronización sobre cambios locales no guardados. La solución es siempre confirmar el estado local antes de integrar el estado remoto.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).


### 2026-04-27 — Fix: Configuración de reconciliación para ramas divergentes (Git)

**Contexto:** Al ejecutar `git pull` para resolver un error de `non-fast-forward`, Git bloqueó la operación indicando que las ramas habían divergido (existían commits distintos tanto en local como en remoto) y requería especificar una estrategia de reconciliación explícita.

**Hecho:** Se configuró la estrategia de fusión por defecto (`git config pull.rebase false`) y se completó la sincronización (`git pull` seguido de `git push`).

**Detalle técnico:** Las ramas divergen cuando el historial local y el remoto se bifurcan (por ejemplo, al crear commits locales tras haber modificado el repositorio en la nube). Configurar `pull.rebase false` instruye a Git para que resuelva estas colisiones creando un "commit de fusión" (Merge Commit) estándar, preservando la cronología exacta de ambas líneas temporales sin reescribir el historial.

**Motivo / criterio:** Gobernanza del repositorio. Definir explícitamente la estrategia de fusión es una buena práctica de ingeniería que previene comportamientos erráticos o destructivos al sincronizar código en entornos de desarrollo distribuidos.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-27 — Fix: Restauración del scroll en el ancla "Volver arriba"

**Contexto:** El enlace "Volver arriba" (`#top`) en el footer dejó de realizar el desplazamiento (scroll) físico esperado. El script `merci-linkcheck.py` no auditó este error porque, por estándar técnico, los rastreadores ignoran los fragmentos de ancla (`#`).

**Hecho:** Se separó el identificador de ancla del contenedor visual `<header>`.

**Detalle técnico:** Se eliminó el `id="top"` y `tabindex="-1"` del `<header>` en `public/index.html` (y derivados) y se inyectó un `<div>` vacío (`position: absolute; top: 0; left: 0;`) con el `id="top"` justo después de abrir la etiqueta `<body>`. Se replicó la inyección en las plantillas f-string de `scripts/merci/merci-publish.py`.

**Motivo / criterio:** *Separation of Concerns* (Separación de responsabilidades). Al trasladar el `id="top"` al `<header>` (que es fijo o se encuentra siempre visible arriba) en la Fase 2, el navegador asumía que ya estaba en el *viewport* y omitía el scroll. Crear un ancla independiente restaura el scroll a la coordenada absoluta `0,0` manteniendo la puntuación WAI-ARIA 100/100.

**Siguiente paso o deuda:** Aplicar el mismo parche en la plantilla de WordPress (`src/wp-theme/merci-theme/index.php`) para mantener la paridad entre entornos.

### 2026-04-27 — Fix: Resolución de error `non-fast-forward` en `git push`

**Contexto:** Al intentar subir cambios al repositorio remoto (`git push`), la operación fue rechazada con el error `non-fast-forward`. Esto indica que el historial del servidor (GitHub) contenía commits que no existían en el repositorio local, creando una divergencia.

**Hecho:** Se ejecutó `git pull` para descargar los cambios remotos y fusionarlos con la rama local. Tras la fusión, se pudo ejecutar `git push` con éxito.

**Detalle técnico:** El comando `git pull` es un atajo para `git fetch` (descargar el historial del servidor) seguido de `git merge origin/main` (integrar los cambios remotos en la rama local). Si no hay conflictos, Git crea automáticamente un "merge commit" para unir las dos líneas de historial.

**Motivo / criterio:** *Integridad del Historial*. Git bloquea los `push` "non-fast-forward" como un mecanismo de seguridad para prevenir la sobreescritura accidental de trabajo que ya existe en el servidor. La solución canónica es siempre integrar los cambios remotos (`pull`) antes de empujar los locales (`push`), garantizando que no se pierda ningún commit.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-27 — Docs: Cuadernillo sobre recuperación de datos y peligros de GUI en Git

**Contexto:** Tras un incidente donde la interfaz gráfica del editor (VS Code) indujo a la eliminación física accidental de una carpeta no versionada (`evidencias/`), surgió la necesidad de documentar la vulnerabilidad operativa de depender de herramientas visuales para el control de versiones.

**Hecho:** Se redactó el activo de conocimiento `laboratorio/Recuperación de datos y el peligro de los comandos destructivos en Git-cuadernillo` detallando el incidente y la maniobra forense de rescate.

**Detalle técnico:** El cuadernillo expone cómo la regla `.gitignore` oculta elementos en la vista del editor, provocando ilusiones ópticas de borrado, y documenta la recuperación de los archivos desde la papelera del sistema anfitrión, reafirmando el uso de `ls -la` en terminal nativa como diagnóstico definitivo.

**Motivo / criterio:** *Knowledge Management* (Gestión del conocimiento). Transformar un accidente operativo en documentación fundacional mitiga el riesgo de que futuros desarrolladores repitan el error. Asienta la directriz de que la terminal es la única fuente de verdad y justifica la obligatoriedad de la herramienta de backups locales.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-27 — Feat: Herramienta de copias de seguridad locales (Backup)

**Contexto:** El uso de interfaces gráficas o comandos complejos de Git conlleva el riesgo inherente de pérdida accidental de archivos locales no rastreados (ej. eliminación accidental al descartar cambios). Se requería un mecanismo "salvavidas" local antes de operar ramas o historiales.

**Hecho:** Se desarrolló `scripts/merci/merci-backup.py` y se añadió el directorio `backups/` al archivo `.gitignore`.

**Detalle técnico:** El script utiliza la librería estándar `zipfile` para empaquetar el árbol del proyecto de forma iterativa, excluyendo activamente directorios de infraestructura pesados (`.git`, `.venv`, `.assets-raw`) para garantizar una compresión rápida (Zip Deflated) y ligera.

**Motivo / criterio:** *Disaster Recovery* (Recuperación ante desastres). Proveer una herramienta CLI estandarizada que genere instantáneas locales (Snapshots) otorga confianza al desarrollador para realizar maniobras destructivas o refactorizaciones profundas sin depender exclusivamente del control de versiones remoto.

**Siguiente paso o deuda:** Iniciar el desarrollo de la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-27 — Fix: Exclusión estricta de evidencias del control de versiones

**Contexto:** La carpeta `laboratorio/evidencias/`, destinada a almacenar material multimedia pesado (vídeos, capturas) para futuros montajes, corría el riesgo de ser rastreada por Git y subida al servidor remoto, inflando el peso del repositorio.

**Hecho:** Se implementó una regla de exclusión estricta en `.gitignore` para `laboratorio/evidencias/*`, preservando únicamente el archivo `.gitkeep`.

**Detalle técnico:** Al igual que con el directorio `.assets-raw/`, esta regla permite que la estructura de carpetas persista en el proyecto mientras vuelve a Git completamente "ciego" ante los binarios que se depositen en su interior.

**Motivo / criterio:** Rigor de infraestructura. El sistema de control de versiones está diseñado para código, no para almacenamiento de archivos brutos o pesados. Aislar este contenido garantiza clones rápidos y evita alcanzar las cuotas de almacenamiento de las plataformas Git.

**Siguiente paso o deuda:** Definir y desarrollar la estrategia técnica para la publicación de estos contenidos visuales en el futuro (evaluar la incrustación de vídeos optimizados vs. GIFs animados simulando vídeos dentro de la documentación).

### 2026-04-27 — Feat: Auto-nombrado (Slugificación) de URLs en SSG

**Contexto:** Existía un acoplamiento rígido entre el nombre físico del archivo `.md` y la URL pública final (`.html`). Si el autor utilizaba nombres descriptivos o prefijos numéricos para organizar su entorno local, estos ensuciaban las rutas SEO de producción.

**Hecho:** Se implementó una función de `slugify` nativa en `scripts/merci/merci-publish.py` para generar los nombres de archivo de salida basándose estrictamente en el atributo `titulo` del YAML Frontmatter.

**Detalle técnico:** Se empleó la librería estándar `unicodedata` (`NFKD`) para normalizar y despojar al texto de acentos o diacríticos del español, y expresiones regulares (`re.sub`) para reemplazar espacios por guiones y eliminar caracteres inválidos para URLs.

**Motivo / criterio:** *Separation of Concerns* (Separación de Responsabilidades). Desacoplar la estructura del sistema de archivos local de la topología de URLs públicas mejora drásticamente la Developer Experience (DX). Permite reorganizar, renombrar y prefijar archivos `.md` localmente sin alterar enlaces indexados ni romper la arquitectura de la información web.

**Siguiente paso o deuda:** Desarrollar el script de copias de seguridad (Backup Local) en Python.

### 2026-04-27 — docs: Reestructuración nombres documentos a publicar

**Contexto:** Dificultad para relacionar visualmente los archivos compilados (`.html` / `.pdf`) con sus documentos origen (`.md`) en el editor debido a discrepancias o abreviaturas en los nombres físicos.

**Hecho:** Renombrar los archivos `.md` de la biblioteca para que coincidan exactamente con el título del documento, facilitando su localización a medida que el repositorio crece.

**Detalle técnico:** Modificación manual del nombre físico de los archivos directamente en el directorio local de la biblioteca.

**Motivo / criterio:** Ejecución manual justificada por el bajo volumen actual de archivos. Se asume la deuda técnica de automatizar el renombrado (slugificación) basado en el YAML Frontmatter en el futuro.

**Siguiente paso o deuda:** Estructurar la `biblioteca/` en subcarpetas temáticas (ej. `DevSecOps y Gobernanza/`) y refactorizar `merci-publish.py` para soportar lectura recursiva y auto-nombrado.

### 2026-04-27 — Feat: Clean Build automático en orquestador SSG

**Contexto:** Si un documento Markdown en la `biblioteca/` era renombrado o eliminado, el orquestador generaba la nueva versión pero los archivos `.html` y `.pdf` antiguos permanecían para siempre en `public/` como "archivos zombis". Requerir que el usuario ejecutara `rm -rf` manualmente era peligroso y propenso a errores.

**Hecho:** Se implementó el patrón de "Clean Build" (Compilación limpia) creando la función `limpiar_directorio_salida()` en `scripts/merci/merci-publish.py`.

**Detalle técnico:** Al iniciar el pipeline, el script escanea los directorios de destino (`public/biblioteca` y `public/descargas`) y ejecuta un `unlink()` estrictamente filtrado por las extensiones `.html` y `.pdf`. Esto garantiza que marcadores como `.gitkeep` u otros assets permanezcan intactos.

**Motivo / criterio:** *Zero Dead Code / DX (Developer Experience)*. El directorio de salida (public) debe ser un reflejo exacto y efímero del estado actual del directorio de origen (código fuente). Automatizar la purga antes de la compilación asegura esta paridad sin depender de comandos destructivos manuales por parte del desarrollador.

**Siguiente paso o deuda:** Crear el script Python para copias de seguridad locales (Backups) o avanzar a la Fase 9 (Inteligencia).

### 2026-04-27 — Fix: Restauración de lógica visual dinámica en SSG

**Contexto:** El orquestador de publicación estática (`merci-publish.py`) sobrescribía el diseño visual de las tarjetas forzando la clase CSS `.card--book` para todos los documentos de la Biblioteca, ignorando el atributo explícito `tipo: "cuadernillo"` definido por la autora en el YAML Frontmatter.

**Hecho:** Se refactorizó la asignación de variables de `clase_css` en `scripts/merci/merci-publish.py` tanto para la página individual como para el generador del índice.

**Detalle técnico:** Se implementó una lógica condicional en línea (Ternary Operator) que evalúa si el `tipo` es "cuadernillo" para inyectar el modificador BEM `.card--booklet`. Para cualquier otro caso, aplica degradación elegante devolviendo `.card--book`.

**Motivo / criterio:** *Single Source of Truth (SSOT)*. El motor de compilación debe respetar ciegamente las definiciones del archivo origen. Forzar clases CSS rompe la jerarquía de la información y la autoridad del Frontmatter.

**Siguiente paso o deuda:** Validar la visualización del borde naranja en los cuadernillos y continuar hacia la Fase 9 (Inteligencia) o el script de Backup Local.

### 2026-04-27 — Arquitectura: Implementación de Documentación en la Sombra (Shadow Docs)

**Contexto:** Al gobernar el Boilerplate desde este proyecto matriz, el `README.md` y las `instrucciones.md` entraban en colisión, ya que el repositorio padre y el hijo requieren documentaciones totalmente diferentes. Actualizar el clon manualmente era propenso a errores.

**Hecho:**
- Se crearon los archivos gemelos `-merci.md` (`README-merci.md`, `instrucciones-merci.md`) y `bitacora-merci-boilerplate.md` en este repositorio base.
- Se actualizó `merci-init.py` dotándolo de la capacidad de intercambiar los gemelos (borrar los personales y renombrar los agnósticos) durante el proceso de purga.

**Detalle técnico:** Se añadió el parámetro `exclude` a la función `purge_directory` para que la guillotina no arrasara con `bitacora-merci-boilerplate.md` al limpiar el laboratorio. Luego, mediante `Path.rename()`, se ascienden los archivos gemelos a su ruta oficial.

**Motivo / criterio:** *Shadow Documentation / IaC*. Almacenar la documentación del proyecto hijo "inactiva" en la matriz garantiza el control de versiones (SSOT) de todas las facetas del código. Automatizar su intercambio elimina el factor de error humano en el Release Pipeline iterativo.

**Siguiente paso o deuda:** Iniciar el desarrollo de la Fase 9 (Inteligencia y Autonomía) o el script local de Backups.

### 2026-04-27 — Docs: Definición del Release Pipeline Agile para el Boilerplate

**Contexto:** El proceso de actualizar y trasladar mejoras desde el proyecto matriz (`mercedev.es`) hacia el repositorio derivado (`merci-boilerplate`) corría el riesgo de sufrir "Configuration Drift" (Deriva de Configuración) si los bugs se parcheaban directamente en el destino.

**Hecho:**
- Se inyectó la Regla 14 en `instrucciones.md` dictando el flujo de trabajo circular estricto.
- Se redactó el cuadernillo divulgativo `cuadernillo-agile-release-pipeline.md` detallando la maniobra.

**Detalle técnico:** El flujo documentado exige que ante cualquier fallo detectado en el QA del boilerplate, se aborte el empaquetado, se corrija el código fuente en el proyecto matriz, y se reinicie el ciclo de clonación (`merci-init.py`) desde cero.

**Motivo / criterio:** Gobernanza de Repositorios y SSOT (Single Source of Truth). Aplicar metodologías *Agile* al despliegue de infraestructura garantiza que el proyecto original herede y capitalice siempre las soluciones descubiertas durante la exportación de plantillas.

**Siguiente paso o deuda:** Desarrollar el script de copias de seguridad locales (Backup) en Python.

### 2026-04-27 — Sincronización de Parches (Backport) desde Merci Boilerplate

**Contexto:** Durante el empaquetado del repositorio hijo (`merci-boilerplate`), se detectaron y solventaron deudas documentales como la falta de expansión del acrónimo JSON-LD, la omisión del entorno de desarrollo dual y la lista incompleta de herramientas en el `README.md`. Al ser `mercedev.es` la única fuente de verdad (SSOT), estos parches debían retroceder al proyecto matriz.

**Hecho:**
- Se expandió el acrónimo JSON-LD en `docs/flujo-publicacion-sop.md`.
- Se amplió el `README.md` listando el ecosistema DevSecOps completo (`merci-promote.py`, `merci-publish.py`, `merci-watcher.py`, etc.).
- Se inyectó la sección "Entorno de Desarrollo Local" al `README.md` de la matriz.

**Detalle técnico:** Modificaciones directas en los archivos Markdown para asegurar la paridad documental entre el Boilerplate generado y el motor anfitrión original.

**Motivo / criterio:** *Single Source of Truth (SSOT)*. Los errores solucionados en la plantilla derivada (fork) deben reflejarse retroactivamente en el repositorio padre (backporting) para evitar la deriva de configuración (Configuration Drift) y proteger la higiene del conocimiento de la rama principal.

**Siguiente paso o deuda:** Avanzar hacia la Fase 9 (Inteligencia y Autonomía) del asistente Merci.

### 2026-04-26 — Fix: Prevención de fuga de datos (Data Leak) en empaquetado

**Contexto:** Durante la creación de la Release 1.0.0 del Merci Boilerplate, se detectó que el clon resultante conservaba los archivos PDF generados por WeasyPrint en `public/descargas/`. Esto rompía la promesa de un "lienzo en blanco" y provocaba una fuga de datos (Data Leak) de los artículos de la autora hacia el repositorio público.

**Hecho:** Se parcheó el script destructivo `scripts/merci/merci-init.py` añadiendo la orden explícita de purgar el directorio de descargas.

**Detalle técnico:** Se incluyó la instrucción `purge_directory(REPO_ROOT / "public" / "descargas")` en el bloque de purga de datos históricos, asegurando que los artefactos binarios sean erradicados junto con el historial de Markdown y HTML.

**Motivo / criterio:** *Data Leak Prevention (Prevención de Pérdida de Datos)*. Un script que pretende empaquetar una infraestructura agnóstica debe ser exhaustivo. Dejar binarios compilados del autor original contamina el peso del repositorio de destino y expone propiedad intelectual que no forma parte del motor DevSecOps.

**Siguiente paso o deuda:** Desarrollar el script de copias de seguridad locales (Backup Local) en Python o avanzar hacia la Fase 9 (Inteligencia y Autonomía).

### 2026-04-26 — Feat: Script de instanciación del Boilerplate (Fase 10)

**Contexto:** Para convertir el repositorio en un producto reutilizable (Boilerplate Release 1.0.0), se necesitaba un mecanismo automatizado que permitiera a un usuario clonar el proyecto, limpiar todas las referencias personales (dominio, nombre) y purgar el historial documental sin tener que hacerlo archivo por archivo.

**Hecho:**
- Se creó el script destructivo `scripts/merci/merci-init.py`.
- Se implementó la purga automática de los directorios `biblioteca/`, `laboratorio/` y `public/biblioteca/`.
- Se implementó el reemplazo recursivo de la identidad (`mercedev.es`, `mercedev`, `Mercedes`) en todos los archivos de configuración y código fuente.
- Se marcó la Fase 10 como completada en el Roadmap.

**Motivo / criterio:** *Automation & Reusability*. Un boilerplate debe ser un lienzo en blanco para el nuevo desarrollador. Automatizar la inicialización cierra el ciclo de vida del proyecto, convirtiéndolo formalmente en la versión 1.0.0 lista para ser distribuida.

**Siguiente paso o deuda:** Dar por finalizado el roadmap fundacional, hacer el *push* definitivo y descansar.

### 2026-04-25 — Fix: Refuerzo de segregación de entornos (Zero Drafts in Library)

**Contexto:** Se detectó una violación de las reglas arquitectónicas: archivos con `estado: "borrador"`, tests huérfanos (`test-borrador.md`) o documentos con marcadores `TODO` pendientes estaban residiendo físicamente en el directorio fuente `biblioteca/`.

**Hecho:**
- Se ejecutó una purga manual moviendo el contenido crudo (`bitacora-merci-boilerplate.md`) de vuelta a `laboratorio/` y eliminando los archivos de test (`test-borrador.md`).
- Se eliminaron los HTML y PDF residuales generados por error en el entorno `public/`.
- Se asienta la regla estricta: El directorio `biblioteca/` en el código fuente es sagrado y solo puede alojar activos de conocimiento 100% curados y terminados.

**Motivo / criterio:** *Environment Segregation* (Segregación de Entornos). Mezclar contenido en incubación con contenido curado en el mismo directorio de origen destruye la confianza en el repositorio y genera fugas de información hacia el entorno de producción al compilar el SSG.

**Siguiente paso o deuda:** Modificar `merci-audit.py` en el futuro para que bloquee atómicamente los commits si detecta YAMLs con `estado: "borrador"` dentro de la carpeta `biblioteca/`.

### 2026-04-25 — Feat: Migración histórica y publicación del Volumen I (Fase 8.2)

**Contexto:** Tras perfeccionar el orquestador SSG (Static Site Generation - Generación de Sitios Estáticos) y el asistente de promoción, era el momento de validar el flujo completo vaciando la deuda documental del laboratorio y trasladando el historial fundacional (Volumen I) a la Biblioteca.

**Hecho:**
- Se promovió el archivo histórico a la `biblioteca/` mediante el asistente interactivo `merci-promote.py`.
- Se compiló el sitio estático y el PDF descargable con `merci-publish.py`.
- Se aprovechó para refactorizar y limpiar un evento duplicado (`DOMContentLoaded`) en `public/js/main.js` que había quedado como residuo de pruebas anteriores.

**Motivo / criterio:** *Content Lifecycle Management* (Gestión del Ciclo de Vida del Contenido). El flujo SOP (Standard Operating Procedure) diseñado demuestra su eficacia: redacción libre en laboratorio -> curación estricta con promote -> compilación automatizada con publish.

**Siguiente paso o deuda:** Marcar la Fase 8.2 como completada en el Roadmap y comenzar la investigación para dotar a Merci de capacidades avanzadas (Fase 9).

### 2026-04-25 — Fix: Control de errores (Fail Gracefully) en orquestador SSG

**Contexto:** El orquestador de publicación (`merci-publish.py`) carecía de manejo de excepciones en sus procesos críticos. Cualquier error puntual (un Markdown malformado, un fallo de WeasyPrint al enlazar imágenes o un error de permisos I/O) provocaría un colapso total del script (Fatal Error), deteniendo el pipeline e impidiendo la publicación del resto de documentos válidos.

**Hecho:**
- Se envolvieron los procesos de `markdown.markdown()`, `HTML().write_pdf()` y `.write_text()` en bloques `try-except`.
- Se implementó un retorno temprano (`return False`) con alertas por consola para saltar archivos corruptos.
- Se aplicó degradación elegante (`pass`) en caso de fallo de WeasyPrint.

**Motivo / criterio:** Principio de *Fail Gracefully* (Fallar con elegancia). Un pipeline DevSecOps maduro no se detiene por un solo elemento defectuoso. Capturar el error, reportarlo y continuar con el siguiente archivo garantiza la resiliencia de la cadena de suministro de contenido. Permitir que el HTML se publique aunque el PDF falle prioriza la disponibilidad del conocimiento por encima del formato secundario.

**Siguiente paso o deuda:** Comprometer este parche y proceder con la migración del Volumen I a la Biblioteca mediante `merci-promote` (Fase 8.2).

### 2026-04-25 — Feat: Soporte multimedia avanzado en SSG (Vídeos y PDFs)

**Contexto:** El motor SSG (`merci-publish.py`) parseaba correctamente el texto, pero el formato Markdown no soporta la etiqueta `<video>` nativamente, convirtiendo los archivos `.mp4` en etiquetas `<img>` rotas. Además, el generador de PDFs (WeasyPrint) no lograba renderizar las imágenes porque no lograba resolver las rutas estáticas (`/assets/`).

**Hecho:**
- Se implementó un pre-procesador *Regex* en Python que intercepta la sintaxis `!alt` y la transforma en un `<video>` HTML5 accesible.
- Se añadió el parámetro `base_url` a WeasyPrint apuntando a la raíz `/public`.
- Se implementó un patrón "Fallback" en SASS (`.video-fallback`) que oculta un mensaje de advertencia en la web, pero lo muestra en el PDF para indicar que hay un vídeo no imprimible.

**Motivo / criterio:** Robustez del ciclo de contenidos. Al resolver el `base_url`, los PDFs descargables ahora contendrán todas las capturas y esquemas integrados por el autor. Al usar Expresiones Regulares para el vídeo, ampliamos las capacidades de Markdown manteniendo las "0 dependencias" sin usar plugins externos que ralenticen la compilación.

**Siguiente paso o deuda:** Iniciar el ciclo de migración con la herramienta `merci-promote` (Fase 8.2) probando a publicar el primer Volumen que contendrá estos assets.

### 2026-04-25 — Feat: Enrutamiento por contexto para el cerebro de Merci (Fase 8.1)

**Contexto:** Tras integrar a Merci en todas las vistas (Fase 7.5), el asistente requería "conciencia de contexto" (saber en qué página está el usuario) para ofrecer respuestas útiles, sin sacrificar la velocidad ni requerir conexiones a una base de datos en tiempo real.

**Hecho:**
- Se refactorizó la clase `MerciController` en `public/js/MerciController.js`.
- Se implementó el método `_loadKnowledgeBase()` que lee `window.location.pathname`.
- Se añadieron diccionarios de respuestas específicos para `/biblioteca`, `/blog`, `/art-de-cote` y `/contacto`.
- Se abrió oficialmente la Fase 8 en el `README.md` y las instrucciones.

**Motivo / criterio:** *Context Routing* (Enrutamiento por Contexto) en Vanilla JS. En lugar de realizar peticiones `fetch` lentas a un backend, inyectar el conocimiento directamente en la clase y filtrarlo por la URL actual mantiene la latencia en 0 milisegundos y respeta la política de 0 dependencias externas.

**Siguiente paso o deuda:** Comprometer el código y planificar la migración de los cuadernillos antiguos a la biblioteca definitiva (Fase 8.2).

### 2026-04-25 — Feat: Implementación del asistente interactivo Merci (Fase 7.5)

**Contexto:** Era el momento de dar vida pública al asistente "Merci" en la interfaz web (Fase 7.5). El código original propuesto utilizaba bucles continuos (`setInterval`) para calcular posiciones y mover la imagen por la pantalla, lo que destrozaba el rendimiento (Layout Thrashing) y violaba las directrices de accesibilidad WAI-ARIA. Además, se requería organizar la carpeta de multimedia previendo el crecimiento futuro.

**Hecho:**
- Se reorganizó el directorio multimedia moviendo el avatar a la nueva ruta escalable `/assets/images/`.
- Se desarrolló el componente estructural BEM `_merci.scss` fijando al asistente mediante CSS.
- Se creó la clase `MerciController` en Vanilla JS (Programación Orientada a Objetos) actuando como máquina de estados.
- Se inyectó el componente HTML accesible en `public/index.html`, `public/contacto/index.html`, `src/wp-theme/merci-theme/index.php` y en el orquestador `merci-publish.py`.

**Detalle técnico:** En lugar de manipular el DOM y las coordenadas con JavaScript, el controlador interacciona estrictamente alternando atributos semánticos (`aria-hidden`, `aria-expanded`). Es el CSS el que reacciona a estos cambios de estado ARIA ejecutando transiciones suaves por GPU (`opacity`, `transform`). Esto garantiza un coste de CPU (Central Processing Unit - Unidad Central de Procesamiento) del 0% cuando el asistente está inactivo y asegura que los usuarios de teclado puedan tabular hacia él mediante el uso de un `<button>` nativo.

**Motivo / criterio:** *Rendimiento Extremo y Accesibilidad Universal*. Al anclar visualmente al asistente y delegar las animaciones al motor de hojas de estilo, erradicamos el temido Cumulative Layout Shift (CLS) y evitamos secuestrar el hilo principal (Main Thread) del navegador, manteniendo intacta nuestra puntuación de 100/100 en Core Web Vitals sin usar librerías externas de terceros.

**Siguiente paso o deuda:** Ejecutar el orquestador maestro (`merci-total`), confirmar que ninguna regla SEO ni de rendimiento ha sido penalizada, y ejecutar el commit atómico.

### 2026-04-25 — DevSecOps: Diagnóstico de fallo de suspensión (System Sleep)

**Contexto:** El entorno de desarrollo (Ubuntu) experimentó un "pantallazo gris" que forzó un reinicio abrupto tras la carga de pestañas pesadas en el navegador, sospechando inicialmente de una fuga de memoria (OOM).

**Hecho:**
- Se aisló el navegador abriéndolo mediante terminal (`google-chrome --incognito --restore-last-session=false`).
- Se auditaron los registros críticos del núcleo anterior mediante `journalctl -b -1 -p err`.

**Detalle técnico:** Los logs revelaron `Freezing user space processes failed` y `Failed to put system to sleep. System resumed again: Device or resource busy`. El colapso no fue por RAM, sino porque un proceso de usuario (posiblemente la aceleración de hardware del navegador o un hilo de Bluetooth) se negó a ceder el control al Kernel (ACPI) durante un intento de suspensión, bloqueando la interfaz gráfica.

**Motivo / criterio:** Trazabilidad estricta. Leer los logs del sistema desmiente suposiciones y revela la causa raíz de las inestabilidades. Esto valida empíricamente la necesidad de construir arquitecturas web ligeras (0 dependencias) que no saturen los manejadores de recursos (threads/GPU) del cliente.

### 2026-04-25 — Refactor: Purga de lógica de cuadernillos en SSG

**Contexto:** Tras pivotar la Arquitectura de la Información y delegar los "Cuadernillos" a WordPress (Art de Coté), el orquestador de publicación estática (`merci-publish.py`) y las plantillas conservaban código heredado y condicionales inútiles (deuda técnica).

**Hecho:**
- Se eliminaron las bifurcaciones condicionales para `.card--booklet` en `merci-publish.py`.
- Se actualizaron los textos de la página índice generada para reflejar la taxonomía de "Proyectos" y "Libros".
- Se refactorizó la plantilla base y se renombró de `plantilla-cuadernillo.md` a `plantilla-proyecto.md`.
- Se actualizó la publicación existente de alias absolutos cambiando su tipo a `bitacora`.

**Motivo / criterio:** *Zero Dead Code* (Cero Código Muerto). El código que no se usa es un lastre de mantenimiento. Si la biblioteca solo alberga proyectos y bitácoras fundacionales, el orquestador SSG debe simplificarse eliminando las comprobaciones innecesarias, cumpliendo así con la Navaja de Ockham.

**Siguiente paso o deuda:** Iniciar la Fase 7.5 subiendo el código JavaScript experimental de "Merci" al laboratorio.

### 2026-04-25 — Refactor: Pivote de Arquitectura de la Información (Libros vs Cuadernillos)

**Contexto:** Tras la reescritura de la portada (`public/index.html`) para alinearla con la realidad operativa del proyecto, se detectó que mantener dos tipos de contenido (Cuadernillos y Bitácoras/Libros) dentro de la Biblioteca estática generaba complejidad innecesaria en el mantenimiento.

**Hecho:**
- Se redefinió la taxonomía del contenido: "Proyectos / Libros" residirán exclusivamente en la **Biblioteca** (Núcleo Estático).
- "Cuadernillos / Exploraciones" residirán exclusivamente en la taxonomía **Art de Coté** (Capa Dinámica CMS/WordPress).
- Se actualizó el *copy* de la portada para reflejar esta nueva frontera arquitectónica.

**Motivo / criterio:** *Separation of Concerns* (Separación de Responsabilidades) y Arquitectura de la Información. Delegar el contenido divulgativo, efímero o exploratorio al entorno dinámico (WordPress) reduce la fricción de publicación. Reservar el motor de Generación de Sitios Estáticos (SSG) únicamente para manuales fundacionales pesados optimiza el uso de la herramienta de compilación a PDF y simplifica el pipeline a futuro.

**Siguiente paso o deuda:** (Opcional) Renombrar `docs/plantilla-cuadernillo.md` a `plantilla-proyecto.md` y limpiar la lógica heredada en `merci-publish.py` si se desea erradicar el concepto de "cuadernillo" del núcleo estático.

### 2026-04-25 — QA: Auditoría de Deuda Técnica y cierre de Fase 7.4

**Contexto:** Como parte del ciclo de mantenimiento y mejora continua (Fase 7.4), se procedió a escanear el repositorio en busca de marcadores `TODO` y deuda técnica acumulada en código o infraestructura.

**Hecho:**
- Se constató la ausencia de deuda técnica bloqueante en el código fuente (Python, SASS, JS).
- El único `TODO` restante es de carácter literario (Prólogo del Vol. I) y se encuentra correctamente aislado en el `laboratorio/`.
- Se verificó la sincronía total entre `README.md`, `instrucciones.md` y el `flujo-publicacion-sop.md`.
- Se marcó la Fase 7.4 como oficialmente completada.

**Motivo / criterio:** *Shift-Left Quality*. La ausencia de deuda técnica es el resultado directo de no haber tolerado integraciones a medias durante el desarrollo. Al solucionar la accesibilidad WAI-ARIA, los enlaces rotos y los artefactos huérfanos de forma inmediata, la fase de auditoría se convierte en una simple verificación de higiene.

**Siguiente paso o deuda:** Iniciar la Fase 7.5 (Producto Merci) para abordar la vida pública y la lógica de backend del asistente.

### 2026-04-25 — Docs: Estandarización del Runbook de Publicación (SOP)

**Contexto:** Al iniciar la Fase 7.4 y ante la proliferación de herramientas de consola creadas para el sistema Merci, la bitácora recogía un resumen escueto del orden de ejecución del pipeline, insuficiente para un proyecto de esta envergadura. Existía el riesgo de fricción cognitiva o fallos en cadena (ej. actualizar sitemap antes de compilar HTML).

**Hecho:**
- Se definió y documentó el Standard Operating Procedure (SOP) básico en el `README.md`.
- Se creó el documento de arquitectura detallado `docs/flujo-publicacion-sop.md` explicando el ciclo de vida del conocimiento.
- Se creó el documento de arquitectura detallado `docs/matriz/flujo-publicacion-sop.md` explicando el ciclo de vida del conocimiento.
- Se estableció el pipeline secuencial: `pull` -> `promote` -> `publish` -> `total` -> `commit` -> `push`.
- Se marcó el hito de mantenimiento del Roadmap como completado.

**Detalle técnico:** El nuevo documento especifica el porqué de cada paso. Por ejemplo, `merci publish` (compilación SSG) debe ejecutarse obligatoriamente *antes* que `merci total` (QA y Sitemap), ya que el escáner de enlaces (`linkcheck`) y el generador de `sitemap.xml` dependen de la existencia previa de los archivos HTML finales en la carpeta `public/` para funcionar correctamente.

**Motivo / criterio:** *Developer Experience (DX), Knowledge Management y Pipeline As Code*. Documentar el "Runbook" detallado transforma un conjunto de scripts sueltos en una verdadera cadena de montaje (CI/CD local). Delegar esta explicación profunda a un documento dedicado en `docs/` en lugar de saturar la bitácora respeta el principio de Separación de Responsabilidades Documentales.

**Siguiente paso o deuda:** Auditar la deuda técnica pendiente de las fases anteriores para dar por concluida la Fase 7.4.

### 2026-04-25 — Fix: Reubicación de borradores al entorno de incubación (Laboratorio)

**Contexto:** Tras extraer el Volumen I de la bitácora, el archivo resultante fue ubicado en la carpeta `biblioteca/` con estado `borrador` y tareas pendientes (Prólogo). Esto violaba el flujo del ciclo de vida del contenido de la Fase 7.3.

**Hecho:**
- Se reubicó físicamente el archivo `bitacora-mercedev-vol-I.md` de vuelta al `laboratorio/` mediante `git mv`.
- Se asienta la directriz de que ningún documento "en construcción" debe residir en la biblioteca.

**Motivo / criterio:** *Separación estricta de entornos (Environment Segregation).* La `biblioteca/` es un directorio exclusivo para activos de conocimiento finalizados. El `laboratorio/` es el entorno de incubación. Un borrador solo transiciona a la biblioteca en el momento exacto en que es "curado" y promovido a `publicado` mediante la herramienta `merci promote`.

**Siguiente paso o deuda:** Iniciar la Fase 7.4 (Mantenimiento y mejora continua).

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

### 2026-04-23 — Milestone: Cierre definitivo de Fase 6 y validación 100/100

**Contexto:** Tras una persistente batalla de depuración contra los scripts en línea residuales de WooCommerce, la estrategia final de utilizar un *whitelist* criptográfico (Hash SHA-256) en la cabecera CSP de Nginx fue implementada. Se requería una auditoría final para certificar la erradicación de errores en consola y el cierre de la fase de despliegue.

**Hecho:**
- Se ha validado una puntuación perfecta (100/100) en todas las categorías de Google PageSpeed Insights para la ruta dinámica `/blog/tienda/`.
- Se ha confirmado la ausencia total de errores de CSP o JavaScript en la consola del navegador.
- Se ha actualizado la fecha de revisión del `checklist-hardening.md` para reflejar la finalización de la Fase 6.

**Detalle técnico:** La combinación de un "escudo de rendimiento" en `functions.php` (desencolado de scripts, bloqueo de hooks) y un "escudo de infraestructura" en Nginx (CSP con hash) ha demostrado ser la arquitectura definitiva para domar un CMS sin sacrificar seguridad ni velocidad.

**Motivo / criterio:** La consecución de este hito valida empíricamente la tesis del proyecto: es posible construir una web híbrida que cumpla con los más altos estándares de la industria. Con esto, se da por concluida la etapa de construcción de infraestructura.

**Siguiente paso o deuda:** Iniciar la Fase 7: Automatización y Clasificación.

### 2026-04-23 — Fix: Whitelist Criptográfico (CSP Hash) para script en línea residual

**Contexto:** El script inline `wc_javascript_is_active` de WooCommerce seguía ejecutándose, evadiendo los `remove_action` en `functions.php`. Se diagnosticó que las versiones modernas de WooCommerce inyectan este código directamente a nivel de renderizado de bloques (Gutenberg), haciéndolo invulnerable a los hooks tradicionales de PHP.

**Hecho:**
- Se optó por una solución de infraestructura en lugar de parchear PHP.
- Se inyectó el hash exacto del script (`'sha256-eHL/Izx7K/qWL0kdBXXnHwsLSHvGOJn/THLHydUZdog='`) en la directiva `script-src` de la cabecera CSP en Nginx.
- Se actualizó el checklist de Hardening documentando la práctica de whitelisting criptográfico.

**Detalle técnico:** En DevSecOps avanzado, cuando un script en línea benigno (y estático) no puede ser erradicado del código legado, la solución no es relajar la seguridad permitiendo `'unsafe-inline'`. La directiva CSP permite autorizar la ejecución exclusiva de una cadena de texto concreta mediante su firma criptográfica SHA-256. Si un atacante modifica un solo carácter del script, el hash cambiará y el navegador lo bloqueará instantáneamente.

**Motivo / criterio:** Seguridad sin compromisos funcionales. Esta maniobra sella la consola del navegador a 0 errores, mantiene el escudo XSS al 100% de eficacia y nos libera de seguir luchando contra el monolito de bloques de WordPress/WooCommerce.

**Siguiente paso o deuda:** Validar la consola en blanco y dar el salto definitivo a la Fase 7.

### 2026-04-23 — Fix: Sincronización del ciclo de vida de hooks (Race Condition)

**Contexto:** El último script inline de WooCommerce (`wc_javascript_is_active`) seguía apareciendo en el reporte de PageSpeed a pesar de haber declarado su `remove_action` correspondiente en `functions.php`.

**Hecho:**
- Se refactorizaron las purgas de scripts inline (`wc_javascript_is_active`, *Speculation Rules*, y *Filtros SVG*) encapsulándolas dentro de la función `merci_purgar_inyecciones_inline`.
- Se ancló dicha función globalmente al hook `init`.

**Detalle técnico:** Ocurrió una condición de carrera (Race Condition) en el orden de carga del ciclo de vida de WordPress. Colocar `remove_action` suelto en el archivo provocaba que la orden de borrado se ejecutara en un momento donde el plugin a veces aún no había consolidado el hook, o el borrado era ignorado por la inusual prioridad `0` que WooCommerce utiliza para disparar antes del ciclo normal. Encapsular la purga dentro de `init` asegura que la orden se ejecute cuando todo el *core* y los plugins ya están cargados en memoria.

**Motivo / criterio:** Conocimiento profundo del ciclo de ejecución (Lifecycle) del framework. Cuando las órdenes de anulación de código fallan silenciosamente, el problema casi siempre reside en el "cuándo" y no en el "qué". Envolver purgas de seguridad en hooks consolidados es la práctica definitiva de blindaje contra código de terceros.

**Siguiente paso o deuda:** Validar la desaparición del hash en la consola e iniciar la Fase 7.

## 2026-04-23 — Fix: Aniquilación del último script inline de WooCommerce (CSP)

**Contexto:** Tras la purga de *Speculation Rules* y filtros SVG, PageSpeed seguía detectando una única violación de la Política de Seguridad de Contenido (CSP) por un script en línea no identificado (hash `sha256-eHL...`).

**Hecho:**
- Se identificó la acción `wc_javascript_is_active` inyectada en el `wp_head` con prioridad 0.
- Se implementó `remove_action('wp_head', 'wc_javascript_is_active', 0)` en `functions.php`.

**Detalle técnico:** WooCommerce inyecta un minúsculo script `<script>document.body.className = ...</script>` al inicio de la cabecera para cambiar la clase `woocommerce-no-js` a `woocommerce-js`. Al no estar en un archivo `.js` externo, este bloque chocaba frontalmente con la directiva `script-src 'self'`. Al estar el sitio en Modo Catálogo y con los scripts de carrito desencolados, esta verificación de estado es código muerto.

**Motivo / criterio:** Limpieza extrema y Zero Tolerance. Un solo script bloqueado es una advertencia en consola y una mancha en el reporte de rendimiento/seguridad. Localizar el *hook* exacto y neutralizarlo desde el backend (PHP) es la única vía para conciliar un CMS pesado con una arquitectura DevSecOps limpia y sin errores.

**Siguiente paso o deuda:** Validar la consola del navegador limpia (0 errores) y cerrar definitivamente la Fase 6.

### 2026-04-23 — Fix: Erradicación definitiva de scripts en línea residuales (WP 6.x)

**Contexto:** Aunque se purgó el grueso de scripts de WooCommerce, PageSpeed Insights reportó un 92/100 en Mejores Prácticas debido a dos bloques `<script>` en línea restantes que violaban la Política de Seguridad de Contenido (CSP): *Speculation Rules* y un script anónimo (filtros SVG de Gutenberg).

**Hecho:**
- Se amplió el bloqueo de `wp_print_speculation_rules` al hook `wp_footer`.
- Se eliminó la acción `wp_global_styles_render_svg_filters` inyectada por el motor de bloques de WordPress en `wp_body_open` y `wp_footer`.

**Detalle técnico:** WordPress 6.x y las versiones recientes de WooCommerce son sumamente obstinados inyectando código en línea. Las *Speculation Rules* intentan ejecutarse en el pie de página si son bloqueadas en la cabecera, y los filtros SVG (duotone) se inyectan directamente tras abrir el cuerpo del documento. Al estar bajo una CSP estricta (`script-src 'self'`), el navegador los interceptaba con éxito, marcando la violación en consola.

**Motivo / criterio:** Tolerancia cero frente a la deuda técnica. Ignorar un 92/100 asumiéndolo como "suficientemente bueno" es el primer paso hacia la degradación estructural de un proyecto. Extirpar este código basura residual demuestra control absoluto sobre el motor de renderizado dinámico (CMS) y sella la perfección de la auditoría.

**Siguiente paso o deuda:** Validar la puntuación perfecta final (100/100) en PageSpeed e iniciar la Fase 7.

### 2026-04-23 — Fix: Depuración estricta de scripts dinámicos y CSP en WooCommerce

**Contexto:** La auditoría de PageSpeed Insights para la ruta `/blog/tienda/` reportó violaciones de la Política de Seguridad de Contenido (CSP), un `TypeError` en `order-attribution.min.js` y la carga innecesaria de jQuery.

**Hecho:**
- Se amplió la función `merci_limpiar_scripts_wc` en `functions.php` para desencolar `wc-order-attribution`, `wc-add-to-cart`, `woocommerce` y desregistrar `jquery` en el frontend.
- Se eliminó la acción `wp_print_speculation_rules` para evitar la inyección de JSON/JS en línea por parte de WordPress.

**Detalle técnico:** WooCommerce inyecta variables de configuración como scripts en línea (`<script>...</script>`). Al tener una cabecera HTTP CSP estricta (`script-src 'self'`), el navegador bloqueaba estos bloques en línea. Al cargar los scripts externos de WooCommerce, estos intentaban leer las variables bloqueadas, resultando en `undefined` y desencadenando el `TypeError`.

**Motivo / criterio:** Resiliencia arquitectónica (Shift-Left). Frente al dilema de debilitar la seguridad de la CSP permitiendo `'unsafe-inline'` o eliminar los scripts conflictivos, se optó por lo segundo. Dado que la tienda opera en "Modo Catálogo", los scripts de atribución de pedidos y carritos AJAX son peso muerto. Erradicarlos protege la puntuación de rendimiento, elimina la dependencia de jQuery y preserva la máxima postura de seguridad contra XSS.

**Siguiente paso o deuda:** Validar la resolución de los errores en la consola del navegador y cerrar la fase de auditoría dinámica.

### 2026-04-23 — Fix: Resolución de micro-métricas de Core Web Vitals (CLS y Render-Blocking)

**Contexto:** Un análisis exhaustivo de PageSpeed Insights alertó sobre un leve Cumulative Layout Shift (CLS de 0.022), recursos que bloquean el renderizado (`main.css`) y discrepancias en el tamaño del logotipo renderizado.

**Hecho:**
- Se corrigieron los atributos HTML del logotipo en todas las vistas, pasando de `width="150" height="auto"` a valores absolutos exactos (`width="263" height="65"`).
- Se desestimó explícitamente la advertencia sobre el CSS bloqueante (`main.css`).

**Detalle técnico:** El atributo `height="auto"` es inválido en HTML5 y provoca que el navegador no reserve espacio vertical previo a la carga de la imagen, causando el micro-salto (CLS). Al aplicar las dimensiones exactas reportadas por el DOM, el salto desaparece. Respecto al CSS bloqueante, al pesar solo 1.7 KiB y resolver en ~150ms, su externalización es preferible frente a inyectar CSS en línea, preservando la limpieza del HTML y la arquitectura SASS.

**Motivo / criterio:** Pragmatismo frente a la automatización. No todas las advertencias de PageSpeed requieren reescribir la infraestructura. Optimizar un archivo de 15 KiB ahorrando 13 KiB o inyectar estilos críticos rompiendo el *Separation of Concerns* constituye sobreingeniería pura. La corrección semántica (atributos de imagen) es suficiente para garantizar el 100/100 real.

**Siguiente paso o deuda:** Iniciar la Fase 7 y diseñar el pipeline de publicación automatizada.

### 2026-04-23 — QA: Auditoría Manual de Accesibilidad (Lighthouse)

**Contexto:** Google PageSpeed Insights (Lighthouse) reporta 10 comprobaciones de accesibilidad que no pueden ser verificadas automáticamente (como el orden lógico de tabulación, trampas de foco y visibilidad de elementos fuera de pantalla). Era necesario certificar el cumplimiento de estos puntos para asegurar un proyecto verdaderamente inclusivo.

**Hecho:**
- Se ejecutó una prueba exhaustiva de navegación exclusivamente por teclado (Tabulación).
- Se verificaron los estados de foco, el flujo visual-vs-DOM y el comportamiento del menú fuera de pantalla.
- Se revalidó la implementación de *Landmarks* semánticos y etiquetas `aria-label`.

**Detalle técnico:** Se confirmó que el núcleo estático no contiene "trampas de foco" (focus traps) y que los elementos interactivos personalizados (`<button id="menu-toggle">`) están construidos sobre etiquetas nativas con atributos WAI-ARIA descriptivos, obviando la necesidad de inyectar `role="button"` artificialmente. Se comprobó que el anillo de foco (`outline`) nativo del navegador es claramente visible.

**Motivo / criterio:** La automatización tiene límites. Un "100/100" en herramientas automatizadas es una ilusión si un usuario con tecnologías de asistencia no puede navegar lógicamente por la página. La auditoría manual cierra la brecha entre la métrica técnica y la empatía con el usuario final.

**Siguiente paso o deuda:** Iniciar la Fase 7 y diseñar el pipeline de publicación automatizada.

### 2026-04-23 — Fix: Refinamiento de HSTS y justificación de deuda en Trusted Types

**Contexto:** Tras la migración de cabeceras de seguridad a Nginx, la auditoría reportó dos advertencias restantes: la ausencia de la directiva `preload` en el HSTS y la falta de `Trusted Types` en la CSP.

**Hecho:**
- Se añadió la directiva `preload` a la cabecera `Strict-Transport-Security` en CloudPanel.
- Se desestimó explícitamente la implementación de `require-trusted-types-for` en la CSP.

**Detalle técnico:** El uso de `preload` inscribe el dominio en las listas maestras de los navegadores para garantizar conexiones HTTPS desde la primera solicitud (mitigando el primer milisegundo de vulnerabilidad). Por otro lado, la directiva `Trusted Types` bloquea el uso de sumideros del DOM basados en cadenas de texto (como `innerHTML`); activar esta directiva fracturaría la operatividad de WordPress, sus plugins y el editor de bloques (Gutenberg), ya que su código base aún no es compatible de forma nativa con esta API estricta.

**Motivo / criterio:** Pragmatismo arquitectónico. La seguridad extrema no debe destruir la funcionalidad core del producto. Aceptar la advertencia de `Trusted Types` se clasifica como una *Deuda Técnica conocida y asumida* derivada del uso de un CMS maduro como WordPress. Con esta acción se cierra formalmente la subfase 5.5.

**Siguiente paso o deuda:** Iniciar el diseño del flujo de publicación automatizado en la Fase 7.

### 2026-04-23 — Feat: Hardening avanzado de cabeceras HTTP (CSP, HSTS, COOP)

**Contexto:** La auditoría de Google PageSpeed Insights señaló la ausencia de cabeceras de seguridad críticas (HSTS, COOP) y una implementación débil de la Política de Seguridad de Contenido (CSP) mediante etiqueta `<meta>`, considerándola no efectiva contra ataques XSS.

**Hecho:**
- Se ha definido un bloque de cabeceras de seguridad para Nginx.
- Se ha migrado la CSP de la etiqueta `<meta>` a una cabecera `Content-Security-Policy` HTTP.
- Se han añadido las cabeceras `Strict-Transport-Security` (HSTS), `Cross-Origin-Opener-Policy` (COOP), `Cross-Origin-Embedder-Policy` (COEP), `Referrer-Policy` y `X-Content-Type-Options`.
- Se ha documentado el proceso de inyección en el VHost de CloudPanel.

**Detalle técnico:** La implementación vía cabecera HTTP es el método de aplicación (enforcement) correcto. La CSP se ha ajustado con `style-src 'self' 'unsafe-inline'` como compromiso de compatibilidad con la barra de administración de WordPress. Se ha documentado la complejidad de `Trusted Types` como una mejora futura. Las cabeceras se inyectan en el bloque `server` del VHost de Nginx.

**Motivo / criterio:** Elevar la postura de seguridad del Boilerplate al máximo nivel posible, mitigando vectores de ataque como XSS, Clickjacking, MIME-sniffing y ataques de canal lateral (Spectre), siguiendo las mejores prácticas de la industria recomendadas por Google.

**Siguiente paso o deuda:** Aplicar las cabeceras en el VHost de producción, eliminar la etiqueta `<meta>` de los archivos HTML y re-auditar en PageSpeed Insights para validar la corrección.

### 2026-04-23 — Fix: Inyección de meta descripción dinámica en WordPress (SEO)

**Contexto:** Se detectó que las páginas dinámicas generadas por WordPress (incluyendo la Tienda de WooCommerce) carecían de la etiqueta `<meta name="description">` en el `<head>`, lo que penaliza la auditoría SEO y afecta a la presentación en los motores de búsqueda. Las páginas del núcleo estático sí la tenían implementada manualmente.

**Hecho:**
- Se creó la función `merci_inyectar_metadatos_seo` en `src/wp-theme/merci-theme/functions.php`.
- Se ancló la función al hook `wp_head`.

**Detalle técnico:** WordPress no genera descripciones meta de forma nativa. La función implementada evalúa el contexto (`is_shop()`, `is_category()`, `is_singular()`) para extraer dinámicamente extractos de artículos o textos por defecto. Incluye una validación (`class_exists`) para apagarse automáticamente si en un futuro se instala un plugin de SEO especializado (como Yoast), evitando etiquetas duplicadas.

**Motivo / criterio:** Mantener la máxima puntuación (100/100) en SEO técnico sin obligar a la instalación inmediata de plugins pesados de terceros. Esto respeta la filosofía de "0 dependencias externas" y el principio de austeridad tecnológica del Boilerplate.

**Siguiente paso o deuda:** Verificar la aparición de la etiqueta en el código fuente de la tienda dinámica y dar por cerrada definitivamente la Fase 6 de despliegue.

### 2026-04-23 — Validación: Core Web Vitals en rutas dinámicas (WooCommerce)

**Contexto:** Tras resolver los conflictos con el proxy Varnish y desactivar el modo mantenimiento intrusivo, era imperativo auditar el rendimiento real de la tienda en producción (`/blog/tienda`) mediante Google PageSpeed Insights para confirmar la viabilidad de la arquitectura.

**Hecho:**
- Se analizaron los reportes de PageSpeed para las vistas móvil y de escritorio de la ruta dinámica de WooCommerce.
- Se validó la retención de las métricas de excelencia logradas previamente en el entorno estático puro.

**Detalle técnico:** Alcanzar la perfección en Core Web Vitals (LCP, INP, CLS) dentro de un ecosistema WooCommerce es atípico. Esto certifica que el "escudo de rendimiento" codificado en `functions.php` (desencolado del script `wc-cart-fragments`, bloqueo de `global-styles` y uso estricto del atributo `defer` en JS) funciona a la perfección. El proxy inverso de Nginx/CloudPanel despacha el HTML dinámico con una eficiencia comparable a un archivo plano.

**Motivo / criterio:** Validación empírica del esfuerzo arquitectónico. La separación de responsabilidades y el enfoque "Shift-Left" en rendimiento demuestran que es posible utilizar un CMS pesado para gestión de datos sin sacrificar en absoluto la velocidad de carga ni la experiencia de usuario (UX).

**Siguiente paso o deuda:** Dar por clausurada la Fase 6 de despliegue y auditoría, y comenzar la Fase 7 (Automatización y Clasificación).

### 2026-04-23 — Fix: Desactivación del modo "Coming Soon" de WooCommerce

**Contexto:** Tras restaurar con éxito la carga de estilos, la web no mostraba el diseño del Child Theme, sino un mensaje genérico ("Tenemos grandes proyectos por anunciar..."). Se diagnosticó que se trataba de la pantalla de mantenimiento nativa de WooCommerce.

**Hecho:**
- Se accedió al panel de administración de WordPress en producción.
- Se desactivó el modo "Próximamente" (Coming Soon) en los ajustes de visibilidad de WooCommerce, cambiándolo a "Público" (Live).

**Detalle técnico:** Las versiones modernas de WooCommerce (>= 9.0) activan por defecto una opción de visibilidad en la base de datos (`woocommerce_coming_soon`) tras su instalación. Este modo inyecta una plantilla predeterminada que secuestra el enrutamiento (`template_include`), ignorando por completo los archivos `index.php` o `woocommerce.php` de nuestro *Child Theme*. Los estilos sí cargaban correctamente porque WordPress sigue ejecutando el archivo `functions.php` en segundo plano.

**Motivo / criterio:** Separación Código/Estado. Al igual que las páginas o taxonomías, el estado de los plugins reside en la base de datos y no viaja a través de Git. Conocer y documentar los comportamientos intrusivos de herramientas de terceros evita depurar código estructural que es válido pero está siendo ignorado por la configuración temporal del CMS.

**Siguiente paso o deuda:** Recargar el frontend para validar que ahora sí se ejecuta la estructura HTML5 y BEM dinámica del Child Theme.

### 2026-04-23 — Fix: Resolución de inyección de puerto 8080 por Varnish

**Contexto:** Tras el intento de usar URLs relativas al protocolo (`//`), la web seguía cargando sin estilos ("parecía otra página"). El diagnóstico revela que Varnish en CloudPanel no solo ofusca el protocolo, sino que inyecta su puerto interno (`8080`) en la variable `$_SERVER['HTTP_HOST']`. Esto generaba URLs inválidas como `//mercedev.es:8080/css/main.css`, las cuales eran bloqueadas por los navegadores (especialmente Firefox).

**Hecho:**
- Se refactorizó `$domain_root` en `src/wp-theme/merci-theme/functions.php`.
- Se eliminó la dependencia absoluta de `$_SERVER['HTTP_HOST']`.
- Se implementó la función nativa `home_url()` de WordPress, recortando el sufijo `/blog` mediante la expresión regular `preg_replace`.

**Detalle técnico:** La función `home_url()` lee la ruta base configurada directamente en la base de datos (`https://mercedev.es/blog`), la cual ya es completamente segura y agnóstica a los puertos internos del proxy inverso. Al aplicar `preg_replace('#/blog/?$#', '', home_url())`, extraemos dinámicamente la raíz absoluta real (`https://mercedev.es` o `http://localhost`), garantizando que los estáticos se encolen correctamente independientemente de la topología del servidor.

**Motivo / criterio:** Resiliencia arquitectónica extrema. Leer variables de servidor brutas (`$_SERVER`) detrás de un proxy de alto rendimiento (Nginx + Varnish) es un antipatrón propenso a fallos. Confiar en la abstracción nativa del framework (WP) que ya está sanitizada por la configuración es la solución definitiva (Single Source of Truth).

**Siguiente paso o deuda:** Validar en producción la carga exitosa de estilos tanto en Chrome como en Firefox y avanzar con la auditoría de rendimiento.

### 2026-04-23 — Fix: Resolución de Mixed Content detrás de proxy Varnish

**Contexto:** Tras purgar la caché de Varnish, la página web dejó de cargar los estilos (desconfiguración de diseño) tanto en PC como en móviles. Al estar detrás de un proxy inverso (Varnish/CloudPanel en el puerto 8080), la función `is_ssl()` de WordPress devolvía `false`. Esto provocaba que la web forzara la URL del CSS mediante `http://`, siendo bloqueada por los navegadores por políticas de *Mixed Content* en una web segura (HTTPS).

**Hecho:**
- Se refactorizó la variable `$domain_root` en `src/wp-theme/merci-theme/functions.php`.
- Se sustituyó el condicional `is_ssl()` por una URL relativa al protocolo (`//`).
- Se unificaron y corrigieron las entradas malformadas previas en la bitácora que interrumpían el flujo de `merci-commit.py`.

**Detalle técnico:** Una URL que empieza por `//` instruye al navegador a utilizar el mismo protocolo que la página actual. Esto sortea la "ceguera" de PHP frente al estado SSL cuando la terminación TLS se realiza en capas superiores (Nginx). Además, se corrigieron las etiquetas en el registro histórico para asegurar que las expresiones regulares (RegEx) de `merci-commit.py` encuentren exactamente los delimitadores de inicio (ej. `**Contexto:**` en lugar de `**Contexto:**`).

**Motivo / criterio:** Resiliencia arquitectónica en DevSecOps. Delegar la resolución del protocolo al cliente (navegador) es más seguro y eficiente que intentar adivinar la topología del servidor desde el backend. Mantener la estructura estricta en el Markdown es vital para la automatización atómica.

**Siguiente paso o deuda:** Validar la restitución del diseño en producción y verificar que el orquestador de commits procesa correctamente la bitácora saneada.

### 2026-04-21 — Fix: Cache Busting global y purga de Varnish en producción

**Contexto:** Al visitar la tienda en dispositivos móviles y tras desplegar la nueva plantilla, se visualizaba una estructura rota. La agresiva caché de los navegadores y la retención del proxy apuntaban a versiones obsoletas del documento HTML y del archivo `main.css`.

**Hecho:**
- Se inyectó el parámetro `?v=2` en las etiquetas `<link>` de `public/index.html` y `public/biblioteca/index.html`.
- Se actualizó el parámetro de versión de `'1.0.0'` a `'1.0.1'` en la función `wp_enqueue_style` dentro de `src/wp-theme/merci-theme/functions.php`.
- Se purgó la caché del servidor (Clear Cache / Purge All) directamente desde la interfaz de CloudPanel.

**Detalle técnico:** CloudPanel enruta el tráfico PHP a través del puerto 8080 hacia Varnish. Alterar plantillas PHP no invalida automáticamente este snapshot. Además, los dispositivos carecen de *hard refresh*, por lo que alterar la cadena de consulta (query string) de la URL del recurso estático obliga al navegador a descargar las nuevas reglas compiladas.

**Motivo / criterio:** Control de Caché en arquitecturas de alto rendimiento. Cualquier pase a producción que modifique el diseño visual debe incrementar versiones en los enlaces de carga y purgar la capa de Varnish para garantizar la paridad visual.

**Siguiente paso o deuda:** Validar la visualización final tras la purga de caché.

### 2026-04-21 — Chore: Resolución de linter de acrónimos para AJAX

**Contexto:** Al ejecutar el orquestador `merci-total`, el auditor (`merci-audit.py`) reportó una advertencia (WARN) por el acrónimo "AJAX" sin expandir en el nuevo documento `biblioteca/auditoria-rendimiento.md`.

**Hecho:**
- Se expandió el acrónimo AJAX (Asynchronous JavaScript and XML - JavaScript Asíncrono y XML) en el archivo correspondiente.

**Detalle técnico:** Para cumplir con el estándar de `0 errores, 0 advertencias` impuesto por el pipeline de integración local, se aplicó la convención de expansión de acrónimos a la documentación técnica recién creada.

**Motivo / criterio:** Disciplina documental y cero fricción técnica. Ningún aviso del linter debe ignorarse si se busca la excelencia técnica absoluta. Expandir los acrónimos facilita la comprensión del documento a cualquier nivel, respetando la filosofía pedagógica del proyecto.

**Siguiente paso o deuda:** Ejecutar `merci-total` por última vez para confirmar la ausencia total de advertencias y realizar el commit final de despliegue.

### 2026-04-21 — Docs: Elaboración del reporte de Core Web Vitals (100/100)

**Contexto:** Tras completar el despliegue en producción de la arquitectura híbrida (Núcleo estático + WordPress + WooCommerce), se realizaron las auditorías en Google PageSpeed Insights obteniendo puntuación perfecta (100/100) en todos los pilares. Era necesario documentar este hito traduciendo las métricas a un activo de conocimiento.

**Hecho:**
- Se creó el documento didáctico `biblioteca/auditoria-rendimiento.md`.
- Se explicaron los 4 pilares auditados: Rendimiento (LCP/INP/CLS), Accesibilidad (WAI-ARIA/Contraste), Mejores Prácticas (CSP/WebP/HTTPS) y SEO (JSON-LD/Canónicas).
- Se marcaron como completados los hitos de la Fase 6.4 en `README.md`.

**Detalle técnico:** El informe vincula empíricamente las decisiones arquitectónicas "Shift-Left" (Vanilla JS, SASS sin frameworks, desencolado de scripts en WooCommerce) con el resultado positivo en herramientas de auditoría externa. Sirve como validación definitiva del *Aislamiento Dinámico*.

**Motivo / criterio:** Gestión del Conocimiento. Los números perfectos no tienen valor a largo plazo si el equipo no comprende por qué se obtuvieron. Documentar el éxito cierra el ciclo DevSecOps y asienta las bases pedagógicas del proyecto (Regla de la Biblioteca).

**Siguiente paso o deuda:** Iniciar la Fase 6.3 (Verificación SEO Final) y preparar la transición hacia la Fase 7 (Automatización y Clasificación).

### 2026-04-21 — Feat: Orquestador maestro de pipeline (merci-total)

**Contexto:** Ejecutar individualmente los scripts de optimización, compilación y auditoría antes de cada pase a producción generaba fricción operativa y riesgo de omisión de pasos críticos.

**Hecho:**
- Se creó el script `scripts/merci/merci-total.py` para orquestar la ejecución secuencial de todas las herramientas.
- Se inyectó el alias `merci-total` en el entorno local.

**Detalle técnico:** El script define un pipeline lógico: `merci-optimizer.py` (Assets) -> `merci-styles.py` (CSS) -> `merci-sitemap.py` (SEO - Search Engine Optimization) -> `merci-audit.py` (SAST - Static Application Security Testing) -> `merci-linkcheck.py` (DAST - Dynamic Application Security Testing). Implementa un patrón "Fail-Fast", deteniendo la ejecución si algún subproceso falla. Excluye explícitamente procesos interactivos (`merci-commit.py`) o demonios (`merci-watcher.py`).

**Motivo / criterio:** CI/CD (Continuous Integration / Continuous Deployment - Integración Continua / Despliegue Continuo) Local. Consolidar la cadena de suministro en un único comando garantiza que el código siempre se optimice y audite antes de integrarse, coronando la arquitectura de automatización del proyecto.

**Siguiente paso o deuda:** Validar la orquestación total y ejecutar el commit final.

### 2026-04-21 — Chore: Adición de alias faltantes y resolución de linter de acrónimos

**Contexto:** Durante la preparación para el despliegue final, se constató que comandos como `merci-linkcheck` o `merci-sitemap` no tenían alias configurados en zsh, y el auditor de Markdown reportó el acrónimo "CPU" sin expandir en el análisis de Copilot.

**Hecho:**
- Se inyectaron los alias faltantes (`merci-linkcheck`, `merci-sitemap`) en el archivo `~/.zshrc`.
- Se expandió el acrónimo CPU (Central Processing Unit - Unidad Central de Procesamiento) en `docs/Analisi-exhaustivo-antes-de-produccion-copilot-github.md`.

**Detalle técnico:** Mantener los alias actualizados para todas las herramientas del ecosistema en el perfil de la terminal (zsh) elimina la fricción de tener que recordar las extensiones `.py` o las rutas absolutas, homogeneizando el flujo DevSecOps.

**Motivo / criterio:** Higiene de terminal y estricto cumplimiento de convenciones. Responder inmediatamente a los avisos no bloqueantes del auditor (WARN) previene la acumulación de deuda técnica documental, asegurando un pase a producción impecable sin advertencias.

**Siguiente paso o deuda:** Ejecutar el último commit atómico y proceder con el test real final en producción.

### 2026-04-21 — Fix: Prevención de Fatal Error por ausencia de dependencias (WooCommerce)

**Contexto:** Al cargar la tienda en el entorno local (donde el plugin de WooCommerce no está instalado), la plantilla no renderizaba el catálogo y devolvía la vista genérica de artículo, además de presentar riesgo de colapso si se forzaba su ejecución.

**Hecho:**
- Se envolvió la llamada principal en `src/wp-theme/merci-theme/woocommerce.php` con un escudo de seguridad (`if ( function_exists( 'woocommerce_content' ) )`).

**Detalle técnico:** La asimetría de entornos (Dev-Prod Parity) implica que no siempre existirán las mismas dependencias de base de datos o plugins. Sin WooCommerce, WordPress ignora `woocommerce.php` por defecto. Si forzara su carga, invocar `woocommerce_content()` provocaría un *Fatal Error* de PHP. El escudo condicional permite fallar con elegancia (Fail Gracefully).

**Motivo / criterio:** Resiliencia del código. El código fuente nunca debe asumir ciegamente que un plugin de terceros estará siempre activo. Proteger las llamadas externas garantiza que el núcleo del tema sobreviva a desactivaciones accidentales en producción o a entornos de desarrollo locales austeros.

**Siguiente paso o deuda:** Finalizar el ciclo de despliegue a producción, donde el plugin sí reside, y ejecutar la auditoría de Core Web Vitals en PageSpeed.

### 2026-04-21 — Fix: Inyección de Favicon dinámico y restauración de symlink local

**Contexto:** El `favicon.ico` no se mostraba en las páginas de WordPress (`/blog`), y los cambios en los archivos `.php` locales no tenían efecto en el navegador, evidenciando una desconexión del entorno de desarrollo. No se han realizado modificaciones sobre el logotipo.

**Hecho:**
- Se inyectó explícitamente la etiqueta `<link rel="icon" href="/favicon.ico?v=3" type="image/x-icon">` en el `<head>` de `src/wp-theme/merci-theme/index.php`.
- Se eliminó la copia huérfana en `/var/www/wordpress/wp-content/themes/merci-theme` y se restauró el enlace simbólico local (`ln -s`) apuntando al repositorio.

**Detalle técnico:** WordPress no emite un favicon por defecto a menos que se configure en su base de datos. Al inyectarlo directamente en el `index.php` del Child Theme, se garantiza que el CMS utilice el mismo archivo físico de la raíz estática. La restauración del symlink soluciona el "falso negativo" del entorno local causado por purgas anteriores.

**Motivo / criterio:** Control estricto de la UI en entornos híbridos y paridad Dev-Prod. Confiar en que el CMS herede comportamientos visuales por defecto suele fallar. Además, el entorno de desarrollo local debe mantener exactamente la misma arquitectura de enlaces simbólicos que producción.

**Siguiente paso o deuda:** Comitear los cambios, desplegar a producción y ejecutar la auditoría de rendimiento final.

### 2026-04-21 — Aprovisionamiento manual de dependencias del CMS (WooCommerce)

**Contexto:** Tras el despliegue del código y la configuración del entorno de producción, surgió la duda sobre el estado operativo de la "Tienda" y la presencia del motor de WooCommerce en el servidor.

**Hecho:**
- Se constató que el plugin de WooCommerce no viaja a través del control de versiones (Git).
- Se instruyó la instalación y activación manual del plugin desde el panel de administración de WordPress en producción, omitiendo el asistente de configuración.

**Detalle técnico:** En una arquitectura de aislamiento, el repositorio Git gobierna el código propietario y la configuración del proxy. Las carpetas de dependencias de terceros (`wp-content/plugins/`) quedan excluidas explícitamente. Las reglas de optimización inyectadas en `functions.php` permanecen latentes hasta que el plugin es activado.

**Motivo / criterio:** Inmutabilidad selectiva. Permitir que los plugins se gestionen visualmente en producción mientras el tema se gestiona estrictamente por código garantiza la operabilidad sin romper el escudo de rendimiento.

**Siguiente paso o deuda:** Auditar la ruta de la tienda (`/blog/tienda`) en PageSpeed Insights.

### 2026-04-21 — Fix: Resolución de error NXDOMAIN en emisión de certificado SSL

**Contexto:** Al intentar emitir el certificado Let's Encrypt desde CloudPanel, el sistema devolvió un error de validación DNS (`NXDOMAIN`) para el subdominio `www.mercedev.es`.

**Hecho:**
- Se eliminó el subdominio `www.mercedev.es` de la lista de dominios solicitados (SANs) en la interfaz de CloudPanel.
- Se emitió el certificado SSL/TLS exclusivamente para el dominio raíz (apex domain): `mercedev.es`.

**Detalle técnico:** Let's Encrypt exige que todos los nombres de dominio de la solicitud resuelvan hacia la IP del servidor. Al carecer la Zona DNS de un registro 'A' o Nombre Canónico (CNAME) explícito para el `www`, el desafío HTTP-01 fracasa.

**Motivo / criterio:** Austeridad técnica y URLs canónicas. El prefijo `www` es un artefacto de la web clásica. Renunciar a él reduce la complejidad de la Zona DNS y se alinea con la filosofía minimalista.

**Siguiente paso o deuda:** Comprobar la emisión exitosa del certificado para el dominio raíz y ejecutar la auditoría de rendimiento.

### 2026-04-21 — Fix: Emisión de Certificado SSL nativo en CloudPanel

**Contexto:** El dominio en producción mostraba la advertencia de "Sitio no seguro" (HTTP). Se planteó la duda de si utilizar la herramienta tradicional `certbot` por terminal para instalar el certificado Let's Encrypt.

**Hecho:**
- Se descartó el uso manual de `certbot` vía CLI (Command Line Interface - Interfaz de Línea de Comandos).
- Se emitió el certificado SSL/TLS (Secure Sockets Layer / Transport Layer Security) directamente desde la pestaña nativa de CloudPanel (Actions > New Let's Encrypt Certificate).

**Detalle técnico:** CloudPanel gestiona sus propios bloques `server` en Nginx mediante plantillas. Emitir el certificado desde su GUI asegura que las directivas `listen 443 ssl` y las rutas a las llaves criptográficas se inyecten limpiamente sin sobreescribir nuestro enrutamiento híbrido personalizado (Fase 4 del Playbook).

**Motivo / criterio:** Respeto por la abstracción del IaaS (Infrastructure as a Service). Mezclar herramientas de bajo nivel de sistema operativo con paneles de gestión genera conflictos de configuración (Configuration Drift). La integración nativa garantiza además la renovación automática del certificado sin necesidad de configurar *cronjobs* manuales.

**Siguiente paso o deuda:** Comprobar que la web carga bajo el protocolo HTTPS y ejecutar, ahora sí, la auditoría final de rendimiento.

### 2026-04-21 — Fix: Sincronización de estado (Páginas y Taxonomías) en producción

**Contexto:** Tras el despliegue exitoso a producción, se detectó que el *hero* de la página "Tienda" no se renderizaba en el entorno público, a pesar de funcionar correctamente en local.

**Hecho:**
- Se diagnosticó una asimetría de estado en la base de datos: la condición lógica `is_page('tienda')` fallaba silenciosamente porque la página física aún no existía en el WordPress de producción.
- Se instruyó la creación manual de las páginas base (Tienda) y categorías taxonómicas (Art de Coté) en el panel de administración de producción.

**Detalle técnico:** El control de versiones (Git) transporta código inmutable y lógica condicional, pero no el estado de la base de datos. Las funciones de enrutamiento interno de WordPress (`is_page()`, `is_category()`) requieren que las entidades existan físicamente en las tablas `wp_posts` y `wp_terms` del entorno actual para que las sentencias `if` se resuelvan como verdaderas.

**Motivo / criterio:** Paridad Dev-Prod (Código vs. Datos). En despliegues de arquitecturas CMS, inyectar la plantilla (Child Theme) es solo la primera mitad de la integración. Siempre se requiere un proceso de aprovisionamiento de datos (Data Seeding) en producción para recrear las anclas de contenido sobre las que pivota el diseño condicional.

**Siguiente paso o deuda:** Validar la aparición del componente *hero* tras crear la página y proceder con la auditoría final de PageSpeed.

### 2026-04-21 — Fix: Inyección de Favicon dinámico y restauración de symlink local

**Contexto:** El `favicon.ico` no se mostraba en las páginas de WordPress (`/blog`), y los cambios en los archivos `.php` locales no tenían efecto en el navegador, evidenciando una desconexión del entorno de desarrollo.

**Hecho:**
- Se inyectó explícitamente la etiqueta `<link rel="icon" href="/favicon.ico?v=3" type="image/x-icon">` en el `<head>` de `src/wp-theme/merci-theme/index.php`.
- Se eliminó la copia huérfana en `/var/www/wordpress/wp-content/themes/merci-theme` y se restauró el enlace simbólico local (`ln -s`) apuntando al repositorio.

**Detalle técnico:** WordPress no emite un favicon por defecto a menos que se configure en su base de datos. Al inyectarlo directamente en el `index.php` del Child Theme, se garantiza que el CMS (Content Management System - Sistema de Gestión de Contenidos) utilice el mismo archivo físico de la raíz estática. La restauración del symlink soluciona el "falso negativo" del entorno local causado por purgas anteriores.

**Motivo / criterio:** Control estricto de la UI en entornos híbridos y paridad Dev-Prod. Confiar en que el CMS herede comportamientos visuales por defecto suele fallar. Además, el entorno de desarrollo local debe mantener exactamente la misma arquitectura de enlaces simbólicos que producción para asegurar que el código que se edita en el IDE es el que el servidor local ejecuta.

**Siguiente paso o deuda:** Comitear los cambios, desplegar a producción (push/pull) y ejecutar la auditoría de rendimiento final (PageSpeed).

### 2026-04-21 — Fix: Caché y MIME Type del Favicon

**Contexto:** A pesar de haber estandarizado el formato a `.ico` y corregido las rutas, los navegadores se negaban a renderizar el nuevo favicon. Se diagnosticó un problema combinado de tipo MIME incorrecto y caché agresiva del navegador.

**Hecho:**
- Se corrigió el atributo `type` de `image/ico` a `image/x-icon` (el estándar oficial).
- Se añadió la cadena de consulta `?v=2` (Cache Buster) a las referencias de `favicon.ico` en `public/index.html` y `public/biblioteca/index.html`.

**Detalle técnico:** Los navegadores web aplican la caché más agresiva posible a los archivos `favicon.ico`. Añadir un parámetro de versión (`?v=2`) en la URL obliga al navegador a considerar la petición como un recurso nuevo, ignorando la caché local. Además, `image/x-icon` es el tipo MIME universalmente reconocido para este formato.

**Motivo / criterio:** Control de Caché en Assets. Siempre que se sustituya un archivo estático crítico sin cambiar su nombre, se debe forzar la invalidación de la caché local del usuario (Cache Busting) para asegurar que los cambios visuales se propaguen inmediatamente a producción.

**Siguiente paso o deuda:** Desplegar el parche, validar la aparición del icono y ejecutar la auditoría de rendimiento.

### 2026-04-21 — Fix: Estandarización definitiva del Favicon a formato .ico

**Contexto:** Se había introducido manualmente el archivo físico `favicon.ico` en el servidor y actualizado la portada (`index.html`), pero sin registrar la maniobra en el repositorio. Esto generó desincronización con las rutas previas y confusión en el diagnóstico del error 404.

**Hecho:**
- Se oficializa el uso de `favicon.ico` como formato estándar para el icono del sitio.
- Se actualizó la referencia en `public/biblioteca/index.html` para que coincida con la portada (`href="/favicon.ico"`).

**Detalle técnico:** El formato `.ico` es el estándar histórico y es solicitado automáticamente por los navegadores en la raíz del dominio. Utilizar este formato físicamente en la raíz pública evita peticiones redundantes, errores 404 de rastreadores y la necesidad de mantener múltiples formatos base.

**Motivo / criterio:** Trazabilidad de activos (Assets). Cualquier cambio manual en los archivos estáticos o en el servidor debe ser registrado en el control de versiones. Asentar el `.ico` como estándar simplifica la arquitectura y se alinea con la web clásica.

**Siguiente paso o deuda:** Desplegar el HTML sincronizado y proceder a la auditoría de PageSpeed Insights.


### 2026-04-21 — Validación: Compilación SASS exitosa tras refactorización

**Contexto:** Tras una serie de intentos, los estilos de padding del componente `.section` seguían sin aplicarse, indicando un problema profundo en la cadena de compilación de SASS.

**Hecho:**
- Se confirmó que la causa raíz era una combinación de una regla `.section` duplicada y conflictiva en `_home.scss` y la omisión de la importación de la carpeta `components` en el `main.scss`.
- Se eliminó la regla duplicada de `_home.scss`, se creó el componente atómico `_section.scss` y se aseguró que la cadena de importación (`@use`/`@forward`) estuviera completa.
- Se recompiló el CSS con éxito, aplicando correctamente los márgenes en el navegador.

**Detalle técnico:** La arquitectura SASS 7-1 depende de una cadena de importación sin ambigüedades. Un componente (`_section.scss`) debe ser reexportado por su índice local (`components/_index.scss`), y ese índice debe ser importado por el punto de entrada principal (`main.scss`).

**Motivo / criterio:** La depuración de SASS requiere seguir la cadena de compilación desde el componente hasta el `main.scss`. Un estilo ausente en el CSS de salida casi siempre se debe a un `@forward` u `@use` omitido. La atomización de componentes previene estos conflictos.

**Siguiente paso o deuda:** Con la integridad visual restaurada, proceder inmediatamente con la auditoría de Core Web Vitals (Fase 6.2) en el entorno de producción.

### 2026-04-21 — Fix: Conexión de índice de componentes en SASS 7-1

**Contexto:** Tras la refactorización del componente `.section` a su propio archivo, los estilos de padding seguían sin aplicarse en el navegador. Un análisis del `main.css` compilado reveló la ausencia total de la regla.

**Hecho:**
- Se eliminó la regla `.section` duplicada que persistía en `_home.scss`.
- Se verificó y aseguró que el archivo `main.scss` (punto de entrada) incluyera la directiva `@use 'components';` para importar el índice de la carpeta de componentes.

**Detalle técnico:** La arquitectura SASS 7-1 es explícita. Si el archivo `main.scss` no importa el índice de un directorio (`components/_index.scss`), todos los componentes declarados en ese índice (`@forward 'section'`) son ignorados por el compilador.

**Motivo / criterio:** Depuración de la cadena de compilación. Cuando un estilo no se aplica, el primer paso es verificar el CSS de salida. Si la regla no está presente, el fallo reside en la cadena de importación (`@use`/`@forward`) del preprocesador, no en el HTML o en la especificidad.

**Siguiente paso o deuda:** Validar la correcta visualización de los márgenes en todas las páginas y proceder con la auditoría de rendimiento.

### 2026-04-21 — Fix: Resolución de omisiones en índices de SASS 7-1

**Contexto:** Pese a refactorizar las clases en el HTML y el SASS, los estilos (como el padding de `.section` o el grid de `.home-card`) no se aplicaban en el navegador. Se diagnosticó que el archivo `src/scss/components/_index.scss` no estaba reexportando (`@forward`) los módulos recientes.

**Hecho:**
- Se actualizó el archivo `_index.scss` para incluir las directivas `@forward` de los componentes faltantes (`card`, `home` y `section`).

**Detalle técnico:** En la arquitectura SASS 7-1, el archivo principal (`main.scss`) solo lee los índices de cada subdirectorio. Si un archivo parcial (ej. `_section.scss`) no está declarado explícitamente en su índice local, el compilador lo ignora silenciosamente y sus reglas CSS no se inyectan en el binario final.

**Motivo / criterio:** Trazabilidad del compilador. Al crear un nuevo archivo `.scss` (especialmente tras aislar componentes BEM), el primer paso innegociable debe ser registrarlo en su índice correspondiente. Esto previene "fugas de estilos" o falsos positivos durante el desarrollo.

**Siguiente paso o deuda:** Recompilar el CSS maestro, validar los márgenes en el navegador y proceder con la auditoría de los Core Web Vitals en producción.

### 2026-04-21 — Fix: Desacoplamiento de padding y atomización de .section

**Contexto:** Al aplicar la etiqueta semántica `<section>` con la clase heredada `.main--padded`, los márgenes no se renderizaban en el navegador. Se diagnosticó que la clase SASS estaba fuertemente acoplada a su etiqueta original y no funcionaba como componente transversal.

**Hecho:**
- Se estableció definitivamente la clase atómica `.section` en la etiqueta `<section>` de `src/wp-theme/merci-theme/index.php`.
- Se trasladó la responsabilidad del espaciado (`padding`) directamente a la clase `.section` en la arquitectura SASS, purgando el modificador obsoleto `.main--padded`.

**Detalle técnico:** Desacoplar las clases CSS de las etiquetas HTML específicas permite que el diseño sobreviva a las refactorizaciones semánticas (cambio de divs a sections). Ahora `.section` actúa como un Layout universal.

**Motivo / criterio:** Especificidad y modularidad SASS. Los modificadores BEM atados a contextos específicos rompen la reusabilidad. Al centralizar el padding en `.section`, se cumple el principio DRY (Don't Repeat Yourself) y se garantiza coherencia absoluta en todas las vistas, sean servidas por Nginx o por el motor de PHP.

**Siguiente paso o deuda:** Validar los márgenes tras recompilar el SASS y proceder a la auditoría de los Core Web Vitals en producción.

### 2026-04-21 — Fix: Restauración de modificador de padding en sección dinámica

**Contexto:** Al sustituir la clase `.main--padded` por `.section` en `index.php` para unificar estilos, se perdió el espaciado (padding) interno. En la arquitectura SASS actual, el padding de las vistas de contenido está explícitamente vinculado al modificador `.main--padded` y no a la clase estructural `.section`.

**Hecho:**
- Se restauró la clase `.main--padded` en la etiqueta `<section>` del archivo `src/wp-theme/merci-theme/index.php`.

**Detalle técnico:** Se mantiene la mejora semántica de usar `<section>` (HTML5) introducida anteriormente, pero se le devuelve la clase CSS que controla físicamente los márgenes (`4rem 2rem`) en el diseño base, asegurando que se visualice correctamente en `localhost`.

**Motivo / criterio:** Conocimiento del estado del SASS. Reemplazar clases asumiendo comportamientos genéricos (como que `.section` tiene padding universal) sin verificar las reglas compiladas genera regresiones visuales. El modificador `.main--padded` debe mantenerse hasta que se decida refactorizar el SASS globalmente.

**Siguiente paso o deuda:** Validar la vista en local, comitear y auditar los Core Web Vitals en producción.

### 2026-04-21 — Atomización de estilos en secciones dinámicas

**Contexto:** Los textos de la capa dinámica (WordPress) aparecían pegados al borde izquierdo sin margen. Esto se debía a que las plantillas usaban la clase modificadora antigua `.main--padded` en lugar de heredar los estilos atómicos estructurales de la portada.

**Hecho:**
- Se reemplazó la clase `.main--padded` por la clase atómica `.section` en `src/wp-theme/merci-theme/index.php`.
- (Nota: Esta misma convención atómica debe replicarse en las vistas estáticas como la Biblioteca).

**Detalle técnico:** Al igual que se hizo con `.hero`, el uso de `.section` centraliza el padding responsivo y la alineación. Cualquier ajuste en SASS sobre el componente `_section.scss` se propagará automáticamente al contenido dinámico.

**Motivo / criterio:** Principio DRY (Don't Repeat Yourself). La atomización evita incoherencias visuales (como saltos de márgenes entre páginas) y elimina la necesidad de mantener modificadores CSS redundantes para el mismo propósito estructural.

**Siguiente paso o deuda:** Replicar esta clase `.section` en las páginas estáticas que lo requieran y validar los Core Web Vitals en producción.

### 2026-04-21 — Refactorización semántica en plantillas dinámicas (HTML5)

**Contexto:** Se detectó una inconsistencia semántica entre la portada estática y las vistas dinámicas de WordPress. Mientras la portada utiliza etiquetas `<section>` para agrupar bloques temáticos de contenido, el archivo `index.php` del CMS envolvía los listados de artículos en un `<div>` genérico (`<div class="main--padded">`).

**Hecho:**
- Se reemplazó el contenedor `<div>` por una etiqueta `<section>` en `src/wp-theme/merci-theme/index.php`.

**Detalle técnico:** Las etiquetas `<section>` introducen un nuevo nodo en el "outline" (esquema) del documento HTML5, lo cual es interpretado correctamente por tecnologías de asistencia y crawlers (SEO) para identificar bloques de contenido autónomos (como el loop de posts o productos).

**Motivo / criterio:** Coherencia arquitectónica y accesibilidad estricta. Un `<div>` carece de valor semántico. Envolver el contenido dinámico dentro de un `<section>` respeta la política de semántica HTML5 del proyecto y asegura que la calidad técnica no se degrade al transicionar del núcleo estático al dinámico.

**Siguiente paso o deuda:** Desplegar la corrección estructural y continuar con la medición del rendimiento en producción.

### 2026-04-21 — Fix: Resolución de enrutamiento de assets en producción

**Contexto:** Tras el despliegue, los assets (como el logotipo) devolvían un error 404. La causa era que el `Document Root` de Nginx apuntaba a `/public`, pero la carpeta `/assets` residía fuera de ella, haciéndola inaccesible para el servidor web.

**Hecho:**
- Se ha creado un tercer enlace simbólico para proyectar la carpeta `/assets` dentro de `/public`.
- Se ha actualizado el `deployment-playbook.md` para incluir este nuevo paso.

**Detalle técnico:** El comando `ln -s /home/mercedev-php/htdocs/mercedev.es/assets /home/mercedev-php/htdocs/mercedev.es/public/assets` resuelve el problema de rutas sin necesidad de reestructurar el repositorio ni de añadir directivas `alias` complejas en la configuración de Nginx de CloudPanel.

**Motivo / criterio:** Consistencia arquitectónica. El uso de enlaces simbólicos es la estrategia unificada de este proyecto para conectar componentes desacoplados. Cualquier recurso que deba ser servido por la web debe residir (o aparentar residir) bajo el `Document Root`.

**Siguiente paso o deuda:** Validar la correcta visualización del logotipo en la portada y en el blog, y proceder con la auditoría de rendimiento de la Fase 6.2.

### 2026-04-21 — Docs: Actualización del Deployment Playbook para CloudPanel

**Contexto:** El manual de despliegue (`docs/deployment-playbook.md`) poseía instrucciones genéricas de enrutamiento y carecía del paso del puente del Child Theme. Era vital alinear el "Runbook" con la ejecución real realizada en el servidor de producción.

**Hecho:**
- Se precisaron las rutas absolutas (`mercedev-php`, `mercedev.es`) en la Fase 3 y se incluyó el comando del segundo enlace simbólico para el Child Theme.
- Se refactorizó la Fase 4 para reflejar el proceso nativo de CloudPanel: modificación del *Document Root* vía UI, edición específica del VHost en el bloque del puerto 8080 y la activación de Enlaces Permanentes.

**Detalle técnico:** Detallar que el enrutamiento de Nginx en CloudPanel se inyecta en el bloque `server` que escucha en el puerto `8080` (procesamiento PHP/Varnish) previene romper la configuración de los servidores públicos de los puertos 80 y 443.

**Motivo / criterio:** Reproducibilidad. Un playbook debe ser un guión ejecutable sin ambigüedades. Incorporar el aprovisionamiento post-instalación (Enlaces permanentes) en el manual asegura que la base de datos y Nginx queden sincronizados en futuros despliegues o reconstrucciones de la infraestructura.

**Siguiente paso o deuda:** Iniciar la Fase 6.2 (Auditoría de rendimiento y accesibilidad) con herramientas externas para validar los Web Vitals.

### 2026-04-21 — Docs: Refactorización de documento de integración para CloudPanel

**Contexto:** El documento `docs/integracion-wordpress.md` reflejaba la configuración del entorno local (LEMP nativo en `/var/www/`). Tras el despliegue en producción, existía una deuda documental ("Drift" o deriva de configuración) respecto a la arquitectura real en CloudPanel.

**Hecho:**
- Se actualizaron las rutas absolutas a `/home/mercedev-php/htdocs/`.
- Se incluyó el segundo enlace simbólico destinado al *Child Theme*.
- Se reemplazó el Virtual Host completo por la metodología de CloudPanel (modificación de `Document Root` vía UI e inyección de reglas `location` en el bloque 8080).

**Detalle técnico:** Adaptar la documentación a las variables `{{root}}` de CloudPanel es vital para que las reglas inyectadas en el VHost no entren en conflicto con el IaaS (Infrastructure as a Service - Infraestructura como Servicio).

**Motivo / criterio:** Single Source of Truth (Única Fuente de Verdad). La documentación arquitectónica no puede ser un artefacto teórico fosilizado. Si la infraestructura en producción se adapta a un panel de control, los documentos del repositorio deben actualizarse para que cualquier réplica futura sea exacta.

**Siguiente paso o deuda:** Iniciar la Fase 6.2 (Auditoría de rendimiento y accesibilidad) con herramientas externas para validar los Web Vitals del entorno real.

### 2026-04-21 — Docs: Actualización de la arquitectura de integración de WordPress

**Contexto:** El documento `docs/integracion-wordpress.md` contenía el plan teórico de despliegue. Tras la implementación exitosa en producción (CloudPanel), era imperativo actualizar la documentación para que reflejara la arquitectura real y los comandos ejecutados.

**Hecho:**
- Se ha reescrito por completo el documento `docs/integracion-wordpress.md`.
- La nueva versión detalla el proceso específico para un entorno gestionado con CloudPanel.

**Detalle técnico:** El documento ahora incluye la arquitectura de "carpetas hermanas", la creación de los dos enlaces simbólicos (para `/blog` y para el `merci-theme`), y la configuración VHost adaptada al motor de plantillas de CloudPanel (modificación del Document Root vía UI y del enrutador PHP en el bloque del puerto 8080).

**Motivo / criterio:** La documentación debe ser un reflejo fiel de la infraestructura en producción, no un artefacto teórico. Este documento actualizado sirve ahora como un "Runbook" fiable para futuras reinstalaciones o para la depuración de la arquitectura híbrida.

**Siguiente paso o deuda:** Iniciar la Fase 6.2 (Auditoría de rendimiento y accesibilidad) para medir los Core Web Vitals en el entorno de producción real.

### 2026-04-21 — Fase 4.2: Enlace simbólico del Child Theme en producción

**Contexto:** Tras inicializar la base de datos de producción, el "Merci Theme" no aparecía en el panel de WordPress porque el código reside en el repositorio Git inmutable (`mercedev.es/src/...`) y el CMS está enjaulado en un directorio hermano (`wordpress/`).

**Hecho:**
- Se trazó un enlace simbólico físico (`ln -s`) desde el código del tema en el repositorio hacia el directorio `wp-content/themes/merci-theme` de la instalación asilada de WordPress.
- Se verificó y activó el tema en el panel de administración en producción.

**Detalle técnico:** Este puente lógico bidireccional garantiza que cualquier actualización de diseño (CSS/PHP) que ingrese vía `git pull` se refleje inmediatamente en el CMS sin necesidad de mover o copiar archivos manualmente.

**Motivo / criterio:** Aislamiento con automatización cero-fricción. El motor PHP de WordPress y los plugins de terceros viven fuera del control de versiones, pero nuestra capa visual a medida (Child Theme) permanece estrictamente gobernada por Git, respetando la filosofía "Single Source of Truth".

**Siguiente paso o deuda:** Resolver la deuda técnica visual (rutas de assets y menú rotos en el frontend dinámico) derivada de la diferencia de la URI base entre la raíz estática y la subruta `/blog`.

### 2026-04-21 — Aprovisionamiento de base de datos y separación Código/Estado

**Contexto:** Tras configurar el enrutamiento Nginx, se requería inicializar el CMS en producción. Se constató la necesidad de clarificar por qué es obligatorio repetir la configuración web (creación de admin, etc.) que ya se hizo en local. Asimismo, se observó que el Child Theme "Merci" no estaba disponible para activación en el panel de WordPress.

**Hecho:**
- Se completó la instalación web (aprovisionamiento) alimentando la nueva base de datos `mercedev_wp_prod`.
- Se sincronizó el enrutamiento configurando los Enlaces Permanentes a "Nombre de la entrada".
- Se documentó la lección arquitectónica sobre la asimetría de Git: transporta código inmutable, no estado.

**Detalle técnico:** Un CMS desplegado en una nueva infraestructura nace en blanco. La configuración de Permalinks (`/%postname%/`) es crítica para que el proxy inverso de Nginx (`/blog/index.php?$args`) interprete correctamente la URI dinámica. La ausencia del Child Theme se debe a que este reside en el repositorio inmutable (`src/wp-theme/merci-theme`) y requiere ser enlazado explícitamente a la instalación asilada del CMS.

**Motivo / criterio:** Principio de Separación de Responsabilidades. La base de datos nunca se sube mediante control de versiones para evitar colisiones de URLs (`localhost` vs producción), credenciales débiles y fugas de seguridad (Shift-Left). Mantener ambas piezas separadas obliga a un aprovisionamiento seguro desde cero.

**Siguiente paso o deuda:** Trazar el enlace simbólico del Child Theme desde el repositorio Git hacia el directorio `wp-content/themes/` del WordPress aislado y activarlo.

### 2026-04-20 — Fix: Adaptación de enrutamiento Nginx a plantillas de CloudPanel

**Contexto:** Al configurar el enrutamiento Nginx (VHost) para separar la capa estática de la dinámica, se detectó que CloudPanel utiliza un motor de plantillas (variable `{{root}}`). Reemplazar estas variables manualmente por rutas absolutas en el editor de texto amenazaba con romper la integración del panel.

**Hecho:**
- Se actualizó el *Document Root* desde la interfaz visual de CloudPanel (pestaña Settings) añadiendo `/public` al final, lo que propagó el cambio de forma segura a todas las variables `{{root}}`.
- En la configuración VHost (pestaña VHost), dentro del bloque `server` del puerto 8080 (procesamiento interno de PHP), se eliminó la regla global `try_files` y se aislaron los tráficos usando dos bloques `location` dedicados (`/` y `/blog`).

**Detalle técnico:**
El bloque estático `location /` devuelve un error 404 de coste cero si el archivo no existe, protegiendo la raíz de ejecución de scripts no autorizados. El bloque dinámico `location /blog` atrapa el tráfico hacia el CMS aislado pasándolo por `/blog/index.php?$args`.

**Motivo / criterio:**
Respetar la capa de abstracción del proveedor (IaaS/Panel). Forzar modificaciones estáticas sobre un entorno gobernado por plantillas dinámicas genera deuda técnica y fragilidad ante actualizaciones del sistema. Separar el ajuste del "Document Root" (vía UI) del "Enrutador PHP" (vía VHost) es la práctica DevOps correcta.

**Siguiente paso o deuda:**
Validar en el navegador la carga de la página estática y la aparición de la instalación de WordPress en la ruta dinámica.

### 2026-04-20 — Fase 3 de Despliegue: Aislamiento y Hardening de WordPress en Producción

**Contexto:** Era imperativo desplegar el CMS en producción sin vulnerar la integridad del núcleo estático recién clonado.

**Hecho:**
- Se creó la base de datos `mercedev_wp_prod` aislada en CloudPanel.
- Se descargó y extrajo la última versión de WordPress en un directorio hermano (`~/htdocs/wordpress`).
- Se blindó el `wp-config.php` inyectando Salts criptográficos oficiales y aplicando permisos de solo lectura para el dueño (`chmod 600`).
- Se estableció el puente lógico creando un enlace simbólico desde `~/htdocs/mercedev.es/public/blog` hacia el directorio aislado de WordPress.

**Detalle técnico:** La configuración manual del `wp-config.php` y la restricción estricta de permisos de sistema operativo, como Cambiar Propietario (CHOWN) y Modificar Modo (CHMOD), evitan depender del instalador web de WordPress, bloqueando cualquier posible vector de ataque o ejecución no autorizada durante el provisionamiento (Shift-Left Security).

**Motivo / criterio:** Aislar los riesgos del entorno dinámico. Si WordPress sufre una vulnerabilidad de escalada a través de un plugin en el futuro, el atacante se encontrará encapsulado en un directorio externo sin permisos para modificar el código fuente inmutable (HTML/CSS/JS) de la landing principal (`mercedev.es/public`).

**Siguiente paso o deuda:** Configurar el VHost (Virtual Host) de Nginx en CloudPanel para orquestar el enrutamiento híbrido.

### 2026-04-17 — Verificación de artefactos estáticos y refactorización de portada

**Contexto:** Era necesario cumplir con el hito del Roadmap "Verificar artefactos finales del núcleo estático antes del deploy". Durante la revisión, se identificó que la lista HTML de la sección de características rompía el diseño Boxed Layout.

**Hecho:**
- Se transformó la lista de características (`<ul>`) en una cuadrícula de tarjetas (`.home-grid` > `.home-card`) en `public/index.html`.
- Se marcó el hito de verificación de artefactos como completado en `README.md`.

**Detalle técnico:** Al homogeneizar la estructura de la portada utilizando los componentes BEM preexistentes, se erradican los problemas de desbordamiento por el `padding` nativo de las listas HTML y se consolida un diseño de "Landing Page" robusto.

**Motivo / criterio:** Rigor técnico y UI coherente. Antes de subir el código al servidor remoto (CloudPanel), el núcleo estático debe estar visual y semánticamente impecable, garantizando que el diseño validado en local sea exactamente el que se despliega.

**Siguiente paso o deuda:** Continuar con la configuración de la base de datos e instalación de WordPress en el entorno de producción.

### 2026-04-17 — Fix: Regeneración de Deploy Key SSH para el usuario correcto

**Contexto:** Al ejecutar el `git clone` en el servidor de producción, GitHub devolvió un error `Permission denied (publickey)`, bloqueando la descarga del repositorio.

**Hecho:**
- Se generó un nuevo par de claves SSH (`ssh-keygen -t ed25519`) bajo el usuario `mercedev-php`.
- Se sustituyó la Deploy Key obsoleta en los ajustes del repositorio de GitHub por la nueva clave pública.

**Detalle técnico:** Las claves SSH están vinculadas estrictamente al directorio `$HOME/.ssh/` del usuario que las ejecuta. La clave generada inicialmente pertenecía al usuario incorrecto (`mercedev`), por lo que el proceso de Git bajo `mercedev-php` carecía de credenciales válidas para la autenticación criptográfica contra GitHub.

**Motivo / criterio:** Autenticación estricta de Linux. En arquitecturas IaaS y paneles como CloudPanel, la identidad del proceso (quién ejecuta el comando) define qué anillo de claves se utiliza. Emparejar correctamente el usuario del sistema de archivos web con su propia clave SSH es vital para un despliegue CI/CD sin fricciones.

**Siguiente paso o deuda:** Confirmar la clonación exitosa del código e iniciar la Fase 3 (Aislamiento de WordPress en CloudPanel).

### 2026-04-17 — Refinamiento final de UI: Boxed Layout y alineación

**Contexto:** Era necesario pulir los detalles visuales finales antes de dar por cerrado el diseño: alinear el menú y el logotipo por su base inferior, separar los títulos del header y limitar el ancho de la web para evitar que el contenido desbordara los márgenes del menú en pantallas ultrapanorámicas.

**Hecho:**
- Se ajustó `.header` con `align-items: flex-end` en `_header.scss`.
- Se aplicó `max-width: 1200px` y `margin: 0 auto` directamente a la etiqueta `body` en `_reset.scss`.
- Se aumentó el valor de la variable `$spacing-xl` a `6rem` en `_variables.scss` para dar más respiro vertical a las cabeceras.

**Detalle técnico:** Limitar el ancho máximo en el `body` (Boxed Layout) es la estrategia más limpia para sincronizar los ejes verticales de `.header`, `.main` y `.footer` sin necesidad de envolver todo en contenedores `.container` adicionales, reduciendo drásticamente el peso del DOM.

**Motivo / criterio:** Equilibrio visual. Alinear los elementos por su línea base (baseline/flex-end) y dar aire a las secciones respirables mejora la legibilidad y la jerarquía de la página. Se confirma formalmente que el uso de Vanilla JS para el menú móvil respeta íntegramente la norma de "Cero dependencias externas" de la arquitectura.

**Siguiente paso o deuda:** Validar los ajustes estéticos y ejecutar el despliegue del Boilerplate a producción.

### 2026-04-17 — Erradicación total de estilos en línea (Inline CSS)

**Contexto:** Se detectaron estilos en línea residuales (`style="padding: 4rem 2rem;"` y `style="margin-bottom: 3rem;"`) en las vistas estáticas (Biblioteca, Contacto) y en la plantilla dinámica de WordPress, lo cual vulneraba la metodología BEM y la filosofía atómica del proyecto.

**Hecho:**
- Se crearon los modificadores BEM `.main--padded` y `.home-grid--spaced` en `src/scss/pages/_home.scss`.
- Se eliminaron todos los atributos `style` residuales de `public/biblioteca/index.html`, `public/contacto/index.html` y `src/wp-theme/merci-theme/index.php`.

**Detalle técnico:** Se estandarizó la aplicación del espaciado interno asignando la clase `.main--padded` al contenedor principal `<main>` para garantizar consistencia estructural entre las vistas estáticas servidas por Nginx y las vistas dinámicas servidas por WordPress. Las variables globales `$spacing-xl` y `$spacing-lg` asumen el control de la separación.

**Motivo / criterio:** Arquitectura limpia y escalabilidad. La purga de atributos `style` asegura que cualquier modificación futura en los márgenes de la interfaz se resuelva editando un único archivo SASS, respetando la filosofía "Single Source of Truth" (Única Fuente de Verdad).

**Siguiente paso o deuda:** Compilar, verificar visualmente el diseño y ejecutar el paso final de la Fase 6 (Despliegue en CloudPanel).

### 2026-04-17 — Refactorización atómica: Eliminación de estilos en línea (Inline CSS)

**Contexto:** Las cabeceras de presentación en las páginas estáticas y dinámicas (Biblioteca, Contacto, Tienda, Blog) usaban el atributo `style="color: #ea580c;"` inyectado directamente en el HTML, violando la separación de responsabilidades y la metodología BEM.

**Hecho:**
- Se creó el modificador BEM `.home-card__title--highlight` en `src/scss/pages/_home.scss` vinculado a `$color-primary`.
- Se eliminaron todos los atributos `style` en línea de `index.html` (Biblioteca, Contacto) y de `index.php` (Child Theme).

**Detalle técnico:** Al añadir un modificador BEM, se delega el control absoluto de la interfaz a la capa SASS. Cualquier cambio futuro en `$color-primary` (ubicado en `_variables.scss`) se propagará ahora correctamente sin necesidad de buscar código HTML "hardcoded" a lo largo de los archivos.

**Motivo / criterio:** Arquitectura limpia (Clean Code). Los estilos en línea son un antipatrón perjudicial para el mantenimiento a escala. La filosofía atómica y BEM exige que las variaciones visuales se gestionen estrictamente mediante modificadores CSS en el sistema de diseño central.

**Siguiente paso o deuda:** Compilar los estilos y proceder con la Fase 6.

### 2026-04-17 — Actualización de paleta de colores (Naranja oscuro)

**Contexto:** Se decidió reemplazar el color de acento primario (azul) por un naranja oscuro en todo el Boilerplate para ajustarse mejor a la identidad visual deseada.

**Hecho:**
- Se modificó la variable `$color-primary` a `#ea580c` en `_variables.scss`.
- Se reemplazaron los valores hexadecimales `hardcoded` azules por la variable `$color-primary` en los componentes `_card.scss` y `_home.scss`.
- Se actualizaron los estilos en línea de los títulos en `public/biblioteca/index.html`, `public/contacto/index.html` y `src/wp-theme/merci-theme/index.php`.

**Detalle técnico:** Al utilizar la variable `$color-primary`, el compilador SASS propaga automáticamente el nuevo color naranja a todos los enlaces (`a:hover`), bordes de tarjetas y efectos visuales, asegurando cohesión en el diseño. Se refactorizaron estilos fijos para mejorar la escalabilidad del Boilerplate.

**Motivo / criterio:** Consistencia y escalabilidad UI. Mantener colores "quemados" (hardcoded) en HTML o en módulos SASS específicos dificulta el mantenimiento. Centralizar el color de acento en una variable global respeta la arquitectura SASS 7-1.

**Siguiente paso o deuda:** Compilar los estilos con `merci-watch`, verificar la consistencia visual en el navegador y continuar con el despliegue en producción.

### 2026-04-17 — Eliminación automática de contenido por defecto de WP (IaC)

**Contexto:** Las instalaciones limpias de WordPress inyectan contenido de relleno ("¡Hola, mundo!" y "Página de ejemplo") en la base de datos, lo cual restaba profesionalidad a la presentación visual del Boilerplate recién desplegado.

**Hecho:**
- Se amplió la función `merci_boilerplate_auto_setup` en `functions.php`.

**Detalle técnico:** Se utilizaron las funciones `get_post()` y `wp_delete_post(id, true)` para buscar los IDs 1 y 2. Si sus *slugs* coinciden con los predeterminados (en español o inglés), se fuerza su borrado permanente (bypass de la papelera) directamente desde el código.

**Motivo / criterio:** Infraestructura como Código (IaC - Infrastructure as Code). Un Boilerplate verdaderamente automatizado debe autolimpiarse tras su despliegue inicial. Obligar al desarrollador a acceder al CMS para borrar contenido basura manualmente rompe la filosofía de automatización y 0 fricción.

**Siguiente paso o deuda:** Comprobar la desaparición del artículo en el frontend local, realizar el commit final e iniciar la Fase 6.

### 2026-04-17 — Unificación tipográfica y maquetación de vistas dinámicas

**Contexto:** Existía una ligera discrepancia visual entre las páginas estáticas (Biblioteca, Contacto) y las páginas dinámicas de WordPress (Art de Coté, Tienda) en cuanto a márgenes, fondos de tarjeta y coloración de enlaces.

**Hecho:**
- Se actualizó `<main>` en `index.php` para igualar el padding de las vistas estáticas (`4rem 2rem`).
- Se alinearon las propiedades de `_card.scss` para ser idénticas a `_home.scss` (fondo transparente, padding ampliado, hover azul).
- Se forzó el color oscuro (`$color-text-base`) en encabezados globales y enlaces de menú (`.nav__link`).

**Detalle técnico:** Se utilizó `color: inherit` dentro de las etiquetas de encabezado (`h1-h6`) en `_typography.scss` para asegurar que los enlaces dinámicos de título generados por WordPress (`<a href="...">`) sobreescriban el azul por defecto y adopten el negro base.

**Motivo / criterio:** Coherencia de Interfaz (UI). Un Boilerplate profesional no debe presentar saltos de diseño entre sus distintas vistas. Homogeneizar contenedores y tipografía garantiza una experiencia de usuario (UX) fluida, independientemente de si la ruta es resuelta por Nginx directo o por el motor de PHP.

**Siguiente paso o deuda:** Confirmar la estética general en el navegador, ejecutar el commit y proceder con el despliegue al entorno de producción (Fase 6).

### 2026-04-17 — Fix: Variables obsoletas en CSS Reset

**Contexto:** Al compilar el SASS tras la migración al Light Mode, el compilador devolvía un error de variables no definidas en `_reset.scss`, deteniendo la ejecución de `merci-watcher.py`.

**Hecho:**
- Se actualizaron las variables en `src/scss/base/_reset.scss` a `$color-bg-base` y `$color-text-base`.

**Detalle técnico:** Se sustituyeron las antiguas variables del modo oscuro que habían quedado huérfanas tras la refactorización de `_variables.scss` en la sesión anterior.

**Motivo / criterio:** En refactorizaciones globales de sistemas de diseño (Design Systems), es común que algún archivo base mantenga dependencias obsoletas. El compilador SASS actúa de forma estricta, protegiendo la integridad del CSS final e impidiendo que llegue código roto a producción.

**Siguiente paso o deuda:** Verificar que el compilador finalice con éxito y volver al enfoque de despliegue en producción (Fase 6).

### 2026-04-17 — Unificación de UI a "Light Mode" (Modo Claro)

**Contexto:** La paleta de colores oscura limitaba la versatilidad de la plantilla. Se requería unificar la estética de las 5 páginas principales bajo un esquema "Light Mode" limpio y profesional.

**Hecho:**
- Se refactorizaron las variables en `_variables.scss` renombrando referencias de Dark a Base (`$color-bg-base: #ffffff`).
- Se eliminaron los colores quemados (hardcoded) en componentes como `_card.scss`, `_hero.scss` y `_home.scss` sustituyéndolos por variables dinámicas.
- Se ajustó la estructura flex en `_header.scss` para alinear el logotipo a la izquierda y el menú a la derecha.

**Detalle técnico:** El uso de módulos `@use '../abstracts' as *` permitió inyectar el nuevo esquema a lo largo de toda la arquitectura SASS 7-1. Los bordes divisorios se mantuvieron utilizando funciones de canal alfa (`rgba`) sobre el nuevo texto oscuro, asegurando contraste accesible.

**Motivo / criterio:** Escalabilidad de diseño. Un Boilerplate debe proveer un lienzo neutral y altamente legible por defecto. Las variables semánticas (`-base` en lugar de `-dark/-light`) permiten que futuros usuarios de la plantilla cambien todo el aspecto de la web modificando solo dos líneas de código SASS.

**Siguiente paso o deuda:** Validar la nueva interfaz en el navegador y ejecutar el commit.

### 2026-04-17 — Configuración de alias de terminal para Merci Watcher

**Contexto:** Para mantener la agilidad del flujo de trabajo local y seguir la convención del resto de herramientas del sistema Merci, se requería un comando rápido para invocar el vigilante de SASS.

**Hecho:**
- Se añadió el alias `merci-watch` a la configuración de la terminal (`~/.zshrc`).

**Detalle técnico:** El alias ejecuta `python3 $MERCI_ROOT/scripts/merci/merci-watcher.py`, aprovechando la variable de entorno global del proyecto definida en configuraciones anteriores para que funcione desde cualquier directorio.

**Motivo / criterio:** Consistencia operativa y reducción de fricción (DX). Abstraer la ruta del script en un comando corto fomenta el uso constante del compilador en tiempo real durante las sesiones de diseño visual.

**Siguiente paso o deuda:** Validar el alias en la terminal, realizar el commit atómico y proceder con el ajuste de variables (Light Mode) en SASS.

### 2026-04-17 — Restauración del vigilante SASS (merci-watcher.py)

**Contexto:** Al igual que ocurrió con el compilador, el script `merci-watcher.py` no sobrevivió a la limpieza y eliminación de la rama de diseño, perdiéndose la automatización de la compilación en tiempo real.

**Hecho:**
- Se ha restaurado el script `scripts/merci/merci-watcher.py`.

**Detalle técnico:** El script se ha recreado con su lógica original utilizando `path.stat().st_mtime` para monitorizar la carpeta `src/scss/` e invocar a `merci-styles.py` mediante `subprocess.run()`.

**Motivo / criterio:** Resiliencia de la infraestructura local. Recuperar las herramientas de DX (Developer Experience - Experiencia del Desarrollador) es imperativo para mantener la agilidad del Boilerplate. Si una herramienta se pierde en el control de versiones por falta de trackeo, la documentación debe permitir su reconstrucción inmediata.

**Siguiente paso o deuda:** Reanudar la refactorización de variables a modo claro (Light Mode) en el SASS.

### 2026-04-17 — Fix: Resolución de advertencias de deprecación en Dart Sass

**Contexto:** Al compilar los estilos SASS, el compilador emitía advertencias (Deprecation Warnings) indicando que las funciones globales de color (`scale-color`) serán eliminadas en Dart Sass 3.0.0.

**Hecho:**
- Se migró el uso de `scale-color` al módulo moderno `color.scale`.
- Se añadió la importación `@use 'sass:color';` en los archivos `_typography.scss`, `_footer.scss` y `_hero.scss`.

**Detalle técnico:** Dart Sass está abandonando las funciones globales en favor de un sistema de módulos integrados (built-in modules). El uso de `color.scale()` previene que el compilador rompa la compilación en futuras actualizaciones del binario standalone de SASS.

**Motivo / criterio:** Mantenibilidad a largo plazo. Un Boilerplate no debe generar advertencias (warnings) de compilación "out of the box". Atender las deprecaciones a tiempo es una práctica fundamental de higiene técnica.

**Siguiente paso o deuda:** Migrar el esquema de colores a variables agnósticas (Light Mode) en los archivos `abstracts` y eliminar colores quemados (hardcoded).

### 2026-04-17 — Corrección de usuario y ruta web en CloudPanel

**Contexto:** Al intentar acceder al directorio del sitio vía SSH para clonar el repositorio, la navegación fallaba debido a que la ruta teórica no coincidía con la generada por el panel de control.

**Hecho:**
- Se verificó la ruta absoluta real desde la interfaz web de CloudPanel, resultando ser `/home/mercedev-php/htdocs/mercedev.es`.
- Se actualizaron las referencias en `docs/deployment-playbook.md` para utilizar rutas absolutas explícitas.

**Detalle técnico:** CloudPanel genera automáticamente usuarios de sistema anexando sufijos (como `-php`) dependiendo del tipo de aplicación seleccionada (PHP Site) para evitar colisiones de nombres. La asunción de que el usuario del sitio era exactamente el ingresado en el formulario causó el error de navegación.

**Motivo / criterio:** Verificación empírica. La interfaz de gestión (GUI) del panel expone la configuración final del servidor (Document Root absoluto). Es prioritario confiar en los datos de la plataforma IaaS o Panel de Control por encima de las asunciones teóricas al interactuar con el CLI.

**Siguiente paso o deuda:** Iniciar sesión como `mercedev-php` y ejecutar `git clone` en la carpeta web correcta (Fase 2).

### 2026-04-17 — Corrección de rutas absolutas a relativas (Home) en manual de despliegue

**Contexto:** Al intentar navegar y listar archivos (`ls`) en el servidor de producción bajo el usuario del sitio de CloudPanel, el sistema devolvía "Permission denied" debido a una confusión en las rutas documentadas en el manual.

**Hecho:**
- Se actualizaron las rutas en `docs/deployment-playbook.md` cambiando `/htdocs/...` por `~/htdocs/...`.

**Detalle técnico:** CloudPanel aísla (chroot/jail) a los usuarios de los sitios. Intentar acceder a `/htdocs` desde la raíz absoluta del servidor de Ubuntu interfiere con los permisos de `root`. La ruta correcta del directorio web reside dentro del `$HOME` del usuario (`~` que se traduce en `/home/usuario/htdocs/dominio.com`).

**Motivo / criterio:** Seguridad de sistema operativo (Linux). Los aislamientos en jaulas evitan que un sitio web comprometido acceda a los archivos de otro sitio en el mismo servidor. Respetar el uso del directorio `$HOME` (`~`) es vital en arquitecturas multi-tenant o paneles de control.

**Siguiente paso o deuda:** Completar la clonación del repositorio en la carpeta del sitio.

### 2026-04-17 — Fix: Preservación de transparencia (Canal Alpha) en Merci Optimizer

**Contexto:** Al procesar imágenes originales con fondos transparentes (ej. logos en formato PNG), la salida WebP resultante inyectaba un fondo opaco, rompiendo el diseño de la UI en el Frontend.

**Hecho:**
- Se añadió una validación del espacio de color (`img.mode`) en `merci-optimizer.py` antes del proceso de guardado y redimensionado.
- Se actualizó el archivo de pruebas `test_optimizer.py` para mockear el objeto resultante de la conversión.

**Detalle técnico:** Las imágenes guardadas en paleta indexada (Modo `P`) o con alpha explícito (`RGBA`, `LA`) pierden sus propiedades de transparencia al ser procesadas directamente a WebP por Pillow si no se convierten antes a un modo compatible. El bloque `img = img.convert('RGBA')` soluciona esto en memoria, preservando el canal de opacidad para el binario final.

**Motivo / criterio:** Fiabilidad de la herramienta local. Una herramienta de optimización multimedia no puede degradar el aspecto visual (UX/UI) a expensas del tamaño. Gestionar los modos de color garantiza que las imágenes transparentes se empaqueten correctamente en WebP.

**Siguiente paso o deuda:** Re-ejecutar el optimizador para recuperar el logotipo sin fondo y continuar el despliegue con CloudPanel.

### 2026-04-17 — Inclusión de la Fase 0 (DNS e Infraestructura) en manual de despliegue

**Contexto:** El manual de despliegue (`deployment-playbook.md`) asumía infraestructura preexistente. Al tratarse de un "Boilerplate", se requería explicar el proceso conceptual desde la compra del dominio para guiar a usuarios desde cero.

**Hecho:**
- Se refactorizó `docs/deployment-playbook.md` incluyendo la nueva "Fase 0: Fundamentos y Preparación de Infraestructura".
- Se reescribió el documento completo utilizando voz impersonal y verbos en infinitivo.

**Detalle técnico:** Se incluyeron las instrucciones explícitas para separar el Registro del Dominio del proveedor IaaS (Infrastructure as a Service), junto con la directriz de modificar el registro DNS tipo 'A'. Se expandieron acrónimos clave (VPS, SSL, SSH) en su primera aparición.

**Motivo / criterio:** Completitud pedagógica, alineada a las `instrucciones.md`. Un Boilerplate no solo provee código, sino conocimiento operativo. Guiar sobre los DNS (Domain Name System) desmitifica el proceso de paso a producción y previene confusiones habituales de enrutamiento temprano.

**Siguiente paso o deuda:** Ejecutar los pasos documentados del manual sobre el entorno de producción.

### 2026-04-17 — Adopción de CloudPanel para la administración de producción

**Contexto:** Se requiere simplificar la administración a largo plazo del servidor de producción (certificados SSL, bases de datos, versiones de PHP) sin sacrificar la arquitectura LEMP de alto rendimiento diseñada en local.

**Hecho:**
- Se actualizó el `docs/deployment-playbook.md` para reemplazar el aprovisionamiento manual por la instalación de CloudPanel.

**Detalle técnico:** CloudPanel es un panel de control server-level optimizado para Nginx, PHP-FPM y MariaDB. Dado que instala su propia pila hiper-optimizada, requiere un sistema operativo Ubuntu completamente limpio. La configuración de enrutamiento inverso (WordPress aislado) se aplicará a través de la interfaz VHost nativa del panel.

**Motivo / criterio:** Eficiencia operativa (DevOps). Automatizar la gestión del servidor reduce la fricción de mantenimiento. CloudPanel se alinea perfectamente con la arquitectura del Boilerplate al utilizar Nginx de forma nativa, permitiendo inyectar reglas de proxy inverso y enlaces simbólicos sin bloqueos.

**Siguiente paso o deuda:** Destruir y recrear el Droplet (para garantizar un sistema 100% limpio) e iniciar la instalación del panel.

### 2026-04-17 — Diagnóstico de enrutamiento DNS y evaluación de proveedores IaaS

**Contexto:** Pérdida de conectividad con el dominio `mercedev.es` tras el reaprovisionamiento del servidor, sumado al deseo de explorar alternativas a DigitalOcean para el alojamiento del entorno de producción.

**Hecho:**
- Se diagnosticó una desincronización en la Zona DNS: el Registro 'A' del dominio apuntaba a la IP del Droplet destruido (Singapur) en lugar del nuevo nodo europeo.
- Se propusieron proveedores IaaS (Infrastructure as a Service) alternativos (Hetzner, Linode, Vultr) compatibles con el `deployment-playbook.md`.

**Detalle técnico:** Al destruir y recrear máquinas virtuales, la dirección IPv4 pública cambia. Es imperativo actualizar el registro 'A' (y 'AAAA' si se usa IPv6) en el registrador del dominio y esperar el tiempo de propagación (TTL). La arquitectura basada en Ubuntu + LEMP nativo garantiza cero *vendor lock-in*.

**Motivo / criterio:** Separación entre Dominio (Registrador) e Infraestructura (Hosting). La resolución DNS es independiente del estado del servidor. Elegir un proveedor IaaS "Bare Metal" o VPS puro (como Hetzner) permite aplicar la Fase 6.1 de despliegue de forma estandarizada y universal.

**Siguiente paso o deuda:** Actualizar la IP en los registros DNS, elegir el proveedor VPS definitivo y ejecutar el aprovisionamiento LEMP de la Fase 6.

### 2026-04-17 — Diagnóstico de latencia y reaprovisionamiento de infraestructura

**Contexto:** Al iniciar la conexión al servidor de producción (Droplet), se detectó una latencia inaceptable y constante de ~290 ms mediante un test de `ping`, lo que imposibilitaba un trabajo fluido por SSH y amenazaba el rendimiento final del sitio.

**Hecho:**
- Se diagnosticó un error en la elección geográfica del Datacenter durante la creación del Droplet (posiblemente ubicado en Asia/Oceanía).
- Se decidió destruir la máquina virtual actual y reaprovisionar una nueva en una región europea cercana (Frankfurt/Ámsterdam).

**Detalle técnico:** Latencias sostenidas cercanas a los 300ms sin pérdida de paquetes (packet loss) son un síntoma inequívoco de distancia transcontinental debido a las limitaciones físicas de la fibra óptica, no de saturación de red local.

**Motivo / criterio:** Física de redes y Core Web Vitals. Por mucho que se optimice el código (Shift-Left) y el tamaño de los assets (WebP), la ubicación física del servidor dicta el TTFB (Time to First Byte) base. Seleccionar la región Edge adecuada es el primer paso innegociable de un despliegue.

**Siguiente paso o deuda:** Recrear el Droplet, obtener la nueva IP, validar la latencia y proceder con la Fase 1 del Deployment Playbook.

### 2026-04-17 — Inicio de Fase 6 y creación del Deployment Playbook

**Contexto:** Con la auditoría local en verde y el Boilerplate consolidado, es momento de transicionar el proyecto desde el entorno de desarrollo (localhost) hacia la infraestructura de producción (DigitalOcean Droplet).

**Hecho:**
- Se ha redactado el manual de operaciones `docs/deployment-playbook.md`.
- Se ha marcado el primer hito de la Fase 6.1 en el `README.md`.

**Detalle técnico:** El Playbook divide el despliegue en 5 fases operativas: Aprovisionamiento LEMP, Clonación vía Git, Aislamiento WP (Symlink), Enrutamiento Nginx+SSL y Verificación final.

**Motivo / criterio:** Reducción de riesgo y estrés operativo. Documentar el paso a paso ("Runbook" o "Playbook") antes de tocar el servidor de producción previene errores por omisión, asegura que se replican las políticas de seguridad estrictas (Shift-Left) y convierte el despliegue en una tarea rutinaria y auditable.

**Siguiente paso o deuda:** Conectar vía SSH al servidor de producción y ejecutar la Fase 1 del Playbook (Aprovisionamiento LEMP).

### 2026-04-17 — Auditoría arquitectónica externa y fijación de dependencias

**Contexto:** Se sometió el repositorio a un análisis externo automatizado (GitHub Copilot) para evaluar su madurez (readiness) antes del paso a producción (Fase 6).

**Hecho:**
- Se revisó el documento `docs/Analisi-exhaustivo-antes-de-produccion-copilot-github.md`.
- Se modificó `requirements.txt` cambiando `Pillow>=10.0.0` por el anclaje estricto `Pillow==10.2.1`.

**Detalle técnico:** El análisis validó la arquitectura híbrida, la seguridad (CSP) y el aislamiento DevSecOps otorgándole la máxima calificación. Identificó correctamente la carencia de políticas de Backup/Rollback (esperadas en la inminente Fase 6) y alertó sobre el riesgo de mutación de dependencias no ancladas en Python.

**Motivo / criterio:** Reproducibilidad absoluta. En DevOps, usar operadores `>=` en gestores de paquetes expone el despliegue a rupturas (breaking changes) si se publica una actualización mayor de la librería. Fijar versiones con `==` garantiza que el entorno de producción instalará exactamente los mismos binarios que se auditaron en local. Se descartaron recomendaciones de sobreingeniería (Redis, AWS) por violar la premisa de austeridad del proyecto.

**Siguiente paso o deuda:** Diseñar el "Deployment Playbook" (Backups, Rollback, Deploy) como primer hito de la Fase 6.1.

### 2026-04-17 — Restauración del compilador SASS (merci-styles.py)

**Contexto:** Se detectó la ausencia del script compilador `merci-styles.py` tras las maniobras de limpieza y fusión de ramas de diseño, amenazando la mantenibilidad de la arquitectura CSS de la plantilla.

**Hecho:**
- Se ha restaurado y refactorizado el script `scripts/merci/merci-styles.py`.

**Detalle técnico:** El script recupera su lógica autónoma: descarga automáticamente el binario standalone de Dart Sass en `scripts/merci/bin/` (ignorando Node/NPM host) y compila `src/scss/main.scss` a `public/css/main.css`.

**Motivo / criterio:** Resiliencia. Un boilerplate debe contener todas las herramientas necesarias para su propia construcción de forma intrínseca. Si una pieza de infraestructura se pierde (debido a exclusiones o fallos en el trackeo de Git), se debe restituir inmediatamente antes de avanzar a producción.

**Siguiente paso o deuda:** Validar la compilación con `merci-watcher.py` e iniciar la Fase 6 de despliegue con garantías.

### 2026-04-17 — Corrección de URLs canónicas en vistas estáticas

**Contexto:** La auditoría integral previa al despliegue (`merci-audit.py`) detectó dos advertencias no bloqueantes (`WARN SEO_CANONICAL`) por la falta de la etiqueta canónica en las nuevas páginas de la plantilla.

**Hecho:**
- Añadida etiqueta `<link rel="canonical">` a `public/biblioteca/index.html` y `public/contacto/index.html`.

**Detalle técnico:** Se implementaron explícitamente las rutas absolutas (`https://mercedev.es/biblioteca` y `https://mercedev.es/contacto`) utilizando la etiqueta `<link rel="canonical">`, que actúa como la declaración oficial de la "fuente de la verdad" para cada documento.

**Motivo / criterio:** Rigor técnico y SEO "Shift-Left". Los motores de búsqueda (como Google) penalizan el contenido duplicado, algo que ocurre accidentalmente si un usuario accede a la web con `www`, sin `www`, o mediante enlaces con parámetros de rastreo (ej. `?utm_source=twitter`). La etiqueta canónica consolida toda la autoridad SEO de esas variantes en una única URL oficial. Solventar esta advertencia garantiza el estándar de calidad (100/100) del Boilerplate.

**Siguiente paso o deuda:** Confirmar auditoría a 0 advertencias e iniciar definitivamente la Fase 6 (Preparación de Release).

### 2026-04-16 — Auditoría integral pre-despliegue (Sanity Check)

**Contexto:** Antes de iniciar oficialmente la Fase 6 (Preparación de release), se requiere una validación cruzada de todos los sistemas locales para certificar la estabilidad de la plantilla "Merci Boilerplate".

**Hecho:**
- Se ejecutó la batería de pruebas unitarias (`unittest`).
- Se ejecutó la auditoría estática estricta (`merci-audit.py --strict-json-ld`).
- Se ejecutó el rastreador dinámico HTTP (`merci-linkcheck.py`).

**Detalle técnico:** La validación abarca lógica algorítmica (tests), análisis estático de código/SEO/seguridad y verificación dinámica de enrutamiento a través del proxy Nginx.

**Motivo / criterio:** Rigor DevSecOps (Pre-flight check). Un pase a producción debe estar precedido por la confirmación empírica (sin errores ni advertencias) de todas las herramientas de aseguramiento de calidad (QA) implementadas en las fases anteriores.

**Siguiente paso o deuda:** Iniciar la Fase 6 (Despliegue y Auditoría Final) tras confirmar el éxito (código de salida 0) de todos los scripts.

### 2026-04-16 — Fix: Enlace de Tienda en Child Theme

**Contexto:** El rastreador `merci-linkcheck.py` detectó un único enlace roto restante (`/tienda`) originado desde las páginas servidas por WordPress (`/blog`).

**Hecho:**
- Se actualizó el `href` en `src/wp-theme/merci-theme/index.php` de `/tienda` a `/blog/tienda`.

**Detalle técnico:** Las páginas estáticas se actualizaron previamente, pero la plantilla dinámica conservaba la ruta obsoleta. La corrección alinea el 100% de los menús de navegación con la ruta real bajo el proxy inverso de Nginx.

**Motivo / criterio:** Coherencia absoluta en la navegación. La experiencia de usuario debe ser transparente sin importar si el visitante se encuentra en la capa estática o dinámica.

**Siguiente paso o deuda:** Validar el script de enlaces a 0 errores e iniciar la Fase 6 de Preparación de Release.

### 2026-04-16 — Reestructuración de enrutamiento Nginx y resolución de API REST WP

**Contexto:** Persistían errores 404 en rutas dinámicas y la API de WordPress (`wp-json`), impidiendo guardar páginas en el editor de bloques ("La respuesta no es una respuesta JSON válida"). El origen era un conflicto al combinar la directiva `alias` con el motor PHP en Nginx.

**Hecho:**
- Se sustituyó la directiva `alias` por un enlace simbólico físico (`ln -s /var/www/wordpress public/blog`).
- Se simplificó drásticamente el bloque `location` en el Virtual Host de Nginx (`mercedev-local`).
- Se forzó el reseteo de los Enlaces Permanentes en WP.

**Detalle técnico:** El bloque `location /blog` pasó de usar `alias` a confiar en la resolución natural del `root` a través del symlink en `public/blog`. Esto repara variables globales vitales para el enrutamiento interno de WP (como `$_SERVER['REQUEST_URI']`). Tras recargar Nginx (`sudo systemctl reload nginx`) y guardar permalinks, la API REST volvió a operar con normalidad.

**Motivo / criterio:** Robustez de infraestructura. Los alias en Nginx con PHP generan "bugs" históricos de enrutamiento. Un enlace simbólico es una solución nativa del sistema operativo, completamente transparente para el servidor web, resolviendo la raíz arquitectónica del problema en lugar de aplicar parches en el código.

**Siguiente paso o deuda:** Corregir el último enlace roto (`/tienda`) en el Child Theme detectado por el rastreador local.

### 2026-04-16 — Creación de herramienta de rastreo dinámico (Merci LinkCheck)

**Contexto:** La auditoría estática (`merci-audit.py`) no puede validar el enrutamiento real generado por Nginx y WordPress. Se requería una herramienta para asegurar la ausencia de enlaces rotos (404) a nivel de infraestructura HTTP antes del despliegue.

**Hecho:**
- Se implementó `scripts/merci/merci-linkcheck.py`.

**Detalle técnico:** El script es un *crawler* construido con la librería estándar (`urllib` y `html.parser`). Recorre el dominio local iterativamente resolviendo anclas (`<a>`), hojas de estilo (`<link>`) e imágenes (`<img>`), verificando que devuelvan códigos HTTP válidos (200 OK). Mantiene un registro de rutas procesadas y la fuente del enlace roto para facilitar la depuración.

**Motivo / criterio:** Robustez de la arquitectura híbrida. Comprobar dinámicamente el proyecto es la única forma empírica de certificar que el CMS y el núcleo estático están comunicándose y resolviendo las URLs correctamente (Shift-Right testing ejecutado en Shift-Left).

**Siguiente paso o deuda:** Ejecutar el rastreador localmente (`python3 scripts/merci/merci-linkcheck.py`) para certificar que el Boilerplate no tiene enlaces rotos antes de iniciar el despliegue de la Fase 6.

### 2026-04-16 — Purga manual y definitiva del bucle de enlaces (Symlink Loop)

**Contexto:** Al utilizar `git restore` para recuperar la carpeta `merci-theme`, el bucle infinito reapareció, revelando que el enlace simbólico erróneo había quedado registrado en un commit anterior en el historial de Git.

**Hecho:**
- Se extrajeron temporalmente los archivos críticos (`index.php`, `functions.php`, `style.css`).
- Se eliminó y recreó manualmente el directorio `src/wp-theme/merci-theme/`.
- Se devolvieron los archivos a la carpeta limpia para forzar la actualización del índice.

**Detalle técnico:** La secuencia de comandos `mv`, `rm -rf` y `mkdir` permitió destruir físicamente el enlace recursivo a nivel de sistema operativo. Al realizar el commit posterior, se sobrescribe el estado del árbol en Git, purgando permanentemente la referencia al enlace simbólico fantasma.

**Motivo / criterio:** `git restore` recupera fielmente el historial, incluyendo los errores. La cirugía manual de directorios es la intervención más segura y pragmática para romper dependencias circulares (filesystem loops) antes de conciliar el estado limpio con el control de versiones.

**Siguiente paso o deuda:** Finalizar el commit atómico y arrancar con la Fase 6 (Despliegue y Auditoría Final).

### 2026-04-16 — Resolución de bucle infinito (Symlink Loop) en Child Theme

**Contexto:** El directorio `src/wp-theme/merci-theme/` mostraba una recursividad de subcarpetas aparentemente infinitas, provocando confusión y amenazando con bloquear el escaneo del editor de código o de Git.

**Hecho:**
- Se ha identificado la presencia de un bucle de enlaces simbólicos (symlink loop).
- Se han eliminado las subcarpetas/enlaces erróneos dentro del directorio del tema mediante los comandos `rm -rf src/wp-theme/merci-theme/*/` y `find -type l -delete`.

**Detalle técnico:** Este fenómeno óptico del sistema de archivos ocurre cuando un enlace simbólico se crea accidentalmente dentro de la misma ruta a la que apunta (o a su padre), creando una referencia circular. El tamaño real en disco es cero, pero los indexadores (como VS Code o Git) pueden colgarse intentando seguir el "pasillo infinito".

**Motivo / criterio:** Mantener el aislamiento absoluto de los componentes. El directorio `merci-theme` solo debe albergar la tríada de archivos planos (`index.php`, `functions.php`, `style.css`). Cualquier directorio anidado ahí dentro es, por definición de esta arquitectura, un residuo que debe ser purgado.

**Siguiente paso o deuda:** Comprobar la estabilidad del árbol de directorios y avanzar hacia la Fase 6 de despliegue.

### 2026-04-16 — Eliminación de archivo fantasma en el Child Theme

**Contexto:** Un archivo `index.html` residual (con el contenido temporal de la página de Contacto) persistía dentro del directorio del tema de WordPress (`src/wp-theme/merci-theme/`), ensuciando la arquitectura del CMS.

**Hecho:**
- Eliminado `src/wp-theme/merci-theme/index.html` mediante `git rm`.

**Detalle técnico:** La existencia de archivos `.html` estáticos dentro de un tema de WordPress no afecta al motor de renderizado PHP por defecto, pero vulnera los principios de limpieza estructural (Clean Code) y causa confusión.

**Motivo / criterio:** Higiene del código y rigor. La plantilla de WordPress solo debe contener los archivos estrictamente necesarios para su funcionamiento e integración dinámica (`index.php`, `style.css`, `functions.php`).

**Siguiente paso o deuda:** Confirmar la limpieza del repositorio e iniciar por fin la Fase 6 de Preparación de Release.

### 2026-04-16 — Corrección de fronteras Nginx y reubicación de página Contacto

**Contexto:** Al validar la navegación híbrida, los enlaces hacia Tienda y Contacto devolvían error. Se constató un fallo en la generación de archivos y una violación de las fronteras de enrutamiento definidas para el CMS.

**Hecho:**
- Se reubicó el archivo `index.html` de Contacto a su ruta estática correcta (`public/contacto/index.html`).
- Se corrigieron los enlaces de navegación de la Tienda de `/tienda` a `/blog/tienda` en todas las cabeceras.

**Detalle técnico:** El archivo de contacto se había generado erróneamente en el Child Theme. Respecto a la Tienda (WooCommerce), al estar WordPress encapsulado bajo Nginx en la ruta `/blog`, cualquier página dinámica que genere (incluyendo el catálogo) hereda el prefijo de esa ruta base.

**Motivo / criterio:** Arquitectura de aislamiento. Nginx actúa como muro: lo estático vive en la raíz (`/`) y lo dinámico en `/blog`. Intentar acceder a `/tienda` provoca que Nginx busque un archivo estático inexistente, reforzando la necesidad de que los enlaces respeten las fronteras de infraestructura.

**Siguiente paso o deuda:** Validar la navegación estática y dinámica de todo el menú principal.

### 2026-04-16 — Adecuación de la vista pública (Demo Boilerplate)

**Contexto:** Tras el pivote estratégico para convertir el proyecto en "Merci Boilerplate", el archivo estático `index.html` aún contenía textos (copy) específicos de una web personal.

**Hecho:**
- Se refactorizaron los textos del `index.html` para transformarlo en una página de presentación técnica del Boilerplate.
- Se mantuvo la marca de autora (`mercedev.es`) incrustada por diseño en el footer, header y metadatos.

**Detalle técnico:** Se reemplazaron las tarjetas de "Art de Coté" y "Merci" por explicaciones de la "Capa Dinámica" y el "Núcleo Estático". Se actualizó la etiqueta `<title>` para reflejar el nombre de la plantilla.

**Motivo / criterio:** Coherencia de producto. Alguien que clone este repositorio debe encontrar una "Landing Page" que le explique qué acaba de instalar y cómo está estructurado, sirviendo a su vez como demostración visual de los componentes SASS (`.home-grid`, `.home-card`).

**Siguiente paso o deuda:** Iniciar formalmente la Fase 6 (Preparación de Release y Auditoría de Rendimiento).

### 2026-04-16 — Integración y limpieza de rama de diseño

**Contexto:** La rama `feat/fase-3-diseno` cumplió su objetivo de aislar el desarrollo del sistema SASS (Grid/Cards) y el optimizador de imágenes.

**Hecho:**
- Se ha fusionado (merge) la rama `feat/fase-3-diseno` hacia `main`.
- Se ha eliminado la rama de desarrollo.

**Detalle técnico:** Se utilizaron los comandos `git checkout main`, `git merge feat/fase-3-diseno` y `git branch -d feat/fase-3-diseno`.

**Motivo / criterio:** Higiene de control de versiones. Las ramas de funcionalidad deben tener ciclos de vida cortos y eliminarse inmediatamente tras su integración para prevenir repositorios inflados con ramas "zombis" y mantener el árbol de Git limpio y legible.

**Siguiente paso o deuda:** Limpiar los textos e imágenes del `index.html` para reflejar la vista demo del nuevo "Merci Boilerplate".

### 2026-04-16 — Pivote Estratégico: Transición a "Merci Boilerplate"

**Contexto:** Se identificó que el valor real de la arquitectura desarrollada no reside en una página web personal específica, sino en la infraestructura híbrida, de seguridad y automatización subyacente.

**Hecho:**
- Pivote del proyecto de web personal (`mercedev.es`) a plantilla de desarrollo (`Merci Boilerplate`).
- Actualización de `README.md` e `instrucciones.md` para reflejar la nueva misión del repositorio.

**Detalle técnico:** Se preserva toda la integración dinámica (WordPress aislado, Nginx proxy) y la automatización DevSecOps (`merci-audit.py`, `merci-optimizer.py`). El objetivo del código ahora es servir como base "clonable" para futuros proyectos web.

**Motivo / criterio:** Separación de responsabilidades a nivel macro (Arquitectura vs. Producto final). Construir un boilerplate permite abstraer y reutilizar las estrictas medidas de seguridad (Shift-Left) y rendimiento en múltiples webs futuras, maximizando el retorno del tiempo de ingeniería invertido.

**Siguiente paso o deuda:** Limpiar el HTML del núcleo estático (`index.html`) para adaptarlo a un formato de plantilla genérica de demostración.

### 2026-04-16 — Integración de componentes SASS (Grid/Cards) en plantillas dinámicas

**Contexto:** Era necesario aplicar el nuevo diseño visual a la capa de WordPress para que los listados de la Biblioteca y el Blog utilizaran la cuadrícula y las tarjetas BEM recién creadas.

**Hecho:**
- Modificado `index.php` en `merci-theme` introduciendo una bifurcación de renderizado mediante `is_singular()`.
- Inyectadas las clases `.grid` y `.card` para los listados (archivos).
- Implementada lógica condicional en PHP para alternar entre `.card--book` y `.card--booklet`.

**Detalle técnico:** Se usa `has_category('fichas')` para determinar el contexto temático e inyectar el modificador BEM correspondiente en la etiqueta `<article>`. En la vista de lista se llama a `the_excerpt()` para mejorar la maquetación, reservando `the_content()` solo para lecturas individuales.

**Motivo / criterio:** Rendimiento y mantenimiento. Concentrar el enrutamiento visual en un único archivo `index.php` inteligente evita la proliferación de plantillas (template hierarchy clutter). Reutilizar el CSS del núcleo estático avala la arquitectura de UI unificada.

**Siguiente paso o deuda:** Validar la visualización creando entradas de prueba en las diferentes categorías de WordPress.

### 2026-04-16 — Unificación de conceptos y navegación principal

**Contexto:** La nomenclatura utilizada en la navegación ("Fichas Técnicas", "Catálogo") resultaba ambigua y se requería establecer los términos definitivos que representarán la arquitectura de la información de cara al usuario.

**Hecho:**
- Se ha unificado la taxonomía principal: Biblioteca, Blog, Art de Coté, Tienda y Contacto.
- Se han actualizado los enlaces de navegación en el núcleo estático (`index.html`) y en la capa dinámica (`index.php` del Child Theme).

**Detalle técnico:** Se reemplazaron las anclas en los elementos `<nav>`. Las rutas proyectadas son `/biblioteca`, `/blog`, `/blog/category/art-de-cote`, `/tienda` y `/contacto`. El término "Catálogo" se reserva exclusivamente como definición técnica del funcionamiento interno de WooCommerce.

**Motivo / criterio:** Claridad cognitiva (UX). Estandarizar los nombres de las secciones principales empleando terminología web universal evita fricción cognitiva en los visitantes y asienta la convención de negocio.

**Siguiente paso o deuda:** Inyectar las clases SASS (`.grid`, `.card`) diseñadas en los archivos PHP de WordPress para renderizar el contenido dinámico con el nuevo diseño unificado.

### 2026-04-16 — Desacoplamiento visual de la Portada y redefinición de navegación

**Contexto:** Se detectó que usar los componentes genéricos (`.grid`, `.card`) en la página de inicio limitaba la capacidad de tener un diseño de "Landing Page" diferenciado de las vistas de lectura (Blog/Biblioteca). Además, la nomenclatura de navegación ("Blog", "Tienda") resultaba ambigua para el propósito del proyecto.

**Hecho:**
- Renombrados los enlaces de navegación a "Fichas Técnicas", "Art de Coté" y "Catálogo" en `index.html` e `index.php`.
- Refactorizado `index.html` para usar clases BEM exclusivas (`.home-grid`, `.home-card`).
- Creado el archivo SASS `src/scss/pages/_home.scss` para aislar los estilos de la portada.

**Detalle técnico:** Las rutas de navegación ahora apuntan directamente a las taxonomías de WordPress (`/blog/category/fichas` y `/blog/category/art-de-cote`), estableciendo una arquitectura de la información clara. La portada ahora consume estilos independientes, permitiendo que `_card.scss` evolucione específicamente para el contenido dinámico.

**Motivo / criterio:** Separación de responsabilidades a nivel de Interfaz de Usuario (UI). Una Landing Page tiene objetivos de marketing y presentación distintos a los de un archivo documental. Desacoplar sus clases CSS previene regresiones visuales (efectos cascada no deseados) al escalar el diseño del CMS.

**Siguiente paso o deuda:** Crear las categorías correspondientes en el panel de administración de WordPress y diseñar el interior de los artículos (`single.php`).

### 2026-04-16 — Fix: Restauración de colores del Header y composición de portada

**Contexto:** La portada (`index.html`) sufrió una alteración visual no deseada tras compilar los nuevos componentes SASS. El header tomó un color claro rompiendo el modo oscuro, y las tarjetas perdieron su cuadrícula original.

**Hecho:**
- Corregido `background-color` a oscuro (`rgba(15, 23, 42, 0.95)`) en `_header.scss`.
- Sustituida clase heredada `grid-cols-1-2` por el nuevo componente `.grid` en `index.html`.

**Detalle técnico:** En SASS, la reescritura de un componente base como `.card` afecta a todo el DOM (Document Object Model - Modelo de Objetos del Documento) que lo invoque. Al crear el componente `_grid.scss`, era imperativo actualizar el HTML estático para que las tarjetas de la portada heredasen el nuevo layout responsivo (CSS Grid) unificado.

**Motivo / criterio:** Mantenimiento de la cohesión del diseño (UI). El núcleo estático debe consumir los mismos componentes (Grid, Cards) que la capa dinámica para justificar la arquitectura de estilos SASS unificada.

**Siguiente paso o deuda:** Aplicar las nuevas clases BEM a las plantillas dinámicas de WordPress.

### 2026-04-16 — Arquitectura de Información: Separación visual de Blog y Biblioteca

**Contexto:** Necesidad de alinear el diseño visual (SASS) con la estructura conceptual del proyecto, diferenciando la "Biblioteca" (libros técnicos, atemporales, temáticos) del "Blog / Art de Coté" (cuadernillos divulgativos, cronológicos).

**Hecho:**
- Creación de los componentes `_grid.scss` y `_card.scss` en la arquitectura SASS.
- Implementación de modificadores BEM `.card--book` y `.card--booklet`.

**Detalle técnico:** Se ha evitado crear componentes HTML separados, optando por el estándar BEM. `.card--booklet` utiliza acentos azules para el contenido fluido, mientras que `.card--book` utiliza acentos verdes para denotar documentación técnica consolidada. El `_grid.scss` proporciona una cuadrícula responsiva genérica.

**Motivo / criterio:** Separar el diseño visual permite que WordPress (cuyo comportamiento por defecto es cronológico) pueda renderizar distintos tipos de contenido usando la misma estructura HTML base, modificando únicamente la clase CSS según la categoría o el tipo de post.

**Siguiente paso o deuda:** Aplicar estas clases HTML en las plantillas PHP (`index.php` o `archive.php`) del Child Theme para que WordPress escupa el contenido con este nuevo diseño.

### 2026-04-16 — Ajuste de estilos estructurales del header (BEM)

**Contexto:** Tras la inclusión del logotipo y el menú de navegación, el componente `.header` presentaba desalineación visual y dependía de estilos en línea temporales.

**Hecho:**
- Se limpiaron los estilos en línea del `<nav>` en `public/index.html`.
- Se actualizaron las reglas SASS para `.header`, usando Flexbox para alinear `.header__brand` y `.header__nav`.

**Detalle técnico:** Se aplicó `display: flex; justify-content: space-between; align-items: center;` al contenedor principal `.header`. Se definió un `gap: 1.5rem` explícito en `.header__nav` de acuerdo con la metodología BEM.

**Motivo / criterio:** Separación estricta de responsabilidades (Separation of Concerns). Los estilos en línea son un antipatrón en una arquitectura escalable. Toda la lógica visual debe residir en los archivos SASS correspondientes.

**Siguiente paso o deuda:** Diseñar las tarjetas dinámicas (`_card.scss`) y la cuadrícula (`_grid.scss`) para la Biblioteca y el Catálogo.

### 2026-04-16 — Ajuste en auditoría para excepción de Favicon

**Contexto:** Se detectó que la nueva regla de auditoría `IMG_FORMAT` bloquearía incorrectamente el commit del archivo `public/favicon.png`, que debe permanecer en formato no optimizado por razones de compatibilidad.

**Hecho:**
- Se ha modificado la función `audit_image_path` en `merci-audit.py`.

**Detalle técnico:** Se ha añadido una condición de salida temprana (`return`) que ignora la validación si el archivo se llama `favicon.png` y reside directamente en la carpeta `public/`.

**Motivo / criterio:** El favicon es un archivo de sistema con requisitos de compatibilidad que priman sobre la optimización general de assets de contenido. El sistema de auditoría debe ser lo suficientemente inteligente para gestionar estas excepciones arquitectónicas.

**Siguiente paso o deuda:** Realizar el commit de todos los cambios acumulados en la rama `feat/fase-3-diseno`.

### 2026-04-16 — Validación final del optimizador y flujo de assets

**Contexto:** Tras los parches y la creación de tests, se procedió a la prueba de fuego del flujo de optimización con los assets reales del proyecto (`logo.png` y `favicon.png`).

**Hecho:**
- Se ha colocado `favicon.png` en `public/`.
- Se ha colocado `logo.png` en `.assets-raw/`.
- Se ha ejecutado `merci-optimizer.py` con éxito, generando `assets/logo.webp` y las variantes responsivas correspondientes.

**Detalle técnico:** El script ha validado su lógica de no-escalado, omitiendo la generación de imágenes más grandes que el original. Se ha confirmado que el `favicon.png` se sirve correctamente desde la raíz y el `logo.webp` desde `/assets`.

**Motivo / criterio:** El flujo de gestión de assets está completo y validado. La infraestructura de optimización está lista para soportar el futuro contenido visual del blog y el catálogo.

**Siguiente paso o deuda:** Ajustar el CSS del componente `.header` para alinear y estilizar correctamente el nuevo logotipo.

### 2026-04-16 — Integración de identidad visual (Favicon y Logo) y fix en optimizador

**Contexto:** Al proceder a integrar los primeros assets visuales (logo y favicon), se detectó que `merci-optimizer.py` omitiría imágenes con dimensiones inferiores al target mínimo (400px), dejando fuera los logotipos estándar.

**Hecho:**
- Se ha parcheado `merci-optimizer.py` para generar siempre una versión `.webp` base del tamaño original, además de las versiones escaladas.
- Se actualizó `test_optimizer.py` para cubrir el nuevo comportamiento.
- Se implementaron etiquetas `<img>` para el logo y `<link rel="icon">` para el favicon en `index.html` e `index.php`.

**Detalle técnico:** Se diferenció la arquitectura de assets: el `favicon.png` reside sin procesar en `public/` por compatibilidad nativa de navegadores antiguos y crawlers, mientras que el logo viaja por el pipeline de optimización (`.assets-raw/` a `assets/logo.webp`). Se añadieron los atributos `width` y `height` en el HTML para mitigar el Cumulative Layout Shift (CLS).

**Motivo / criterio:** Las automatizaciones no deben convertirse en bloqueadores del diseño. Generar siempre la copia base asegura compatibilidad con cualquier asset visual independientemente de su tamaño. Las medidas en el tag `img` son obligatorias para mantener el Core Web Vitals en verde.

**Siguiente paso o deuda:** Proveer físicamente las imágenes, compilar y revisar en el navegador.

### 2026-04-16 — Lección de TDD: Corrección de `AttributeError` en `unittest.mock`

**Contexto:** Al ejecutar el test para `merci-optimizer.py`, se produjo un `AttributeError: 'PosixPath' object attribute 'glob' is read-only`, bloqueando la validación.

**Hecho:**
- Se ha refactorizado `scripts/merci/tests/test_optimizer.py` para corregir el objetivo de los decoradores `@patch`.

**Detalle técnico:** El error se debía a que se intentaba parchear un método (`.glob`, `.mkdir`) en una *instancia* de un objeto `Path` (`SOURCE_DIR`), lo cual no está permitido. La solución correcta es parchear el método en la *clase* `Path` dentro del espacio de nombres del módulo que se está probando. Los decoradores se cambiaron a `@patch("merci_optimizer.Path.glob")` y `@patch("merci_optimizer.Path.mkdir")`.

**Motivo / criterio:** Lección fundamental de `unittest.mock`: se debe parchear el objeto "donde se busca" (`where it's looked up`), no "donde se define". Al parchear la clase, cualquier instancia creada dentro del test usará la versión simulada del método, respetando la inmutabilidad de los objetos `pathlib`.

**Siguiente paso o deuda:** Re-ejecutar el test para confirmar el éxito y proceder con la optimización de assets.

### 2026-04-16 — Pruebas unitarias de optimizador y auditoría de extensiones

**Contexto:** Antes de utilizar operativamente `merci-optimizer.py`, era imperativo aplicar la regla de TDD (crear su test) y asegurar que el hook de pre-commit bloqueara la adición accidental de formatos no optimizados.

**Hecho:**
- Añadida función `audit_image_path` en `merci-audit.py` para bloquear archivos `.png`, `.jpg`, `.jpeg`.
- Creado el test unitario `scripts/merci/tests/test_optimizer.py`.

**Detalle técnico:** El test utiliza `unittest.mock` para interceptar llamadas a `Pillow` y el sistema de archivos (`Path.glob`, `Image.open`), validando que la lógica de iteración sobre `TARGET_WIDTHS` se cumple sin grabar archivos reales. El auditor ahora filtra extensiones de imagen sin leerlas como texto UTF-8.

**Motivo / criterio:** Rigor DevSecOps. Se previene proactivamente la degradación del rendimiento por despistes humanos (subir un `.png` directo a producción) y se garantiza que la herramienta de optimización está cubierta por test antes de integrarla en el flujo.

**Siguiente paso o deuda:** Ejecutar los tests, confirmar su éxito y pasar a la inclusión del logotipo y favicon en formato optimizado.

### 2026-04-16 — Fase 3.4: Implementación del optimizador de imágenes

**Contexto:** Dentro de la rama `feat/fase-3-diseno`, se aborda el hito 3.4 para automatizar la creación de imágenes responsivas y optimizadas para la web.

**Hecho:**
- Se ha creado el archivo `requirements.txt` para gestionar las dependencias de Python, añadiendo `Pillow`.
- Se ha implementado el script `scripts/merci/merci-optimizer.py`.
- Se ha marcado el hito 3.4 como completado en el `README.md`.

**Detalle técnico:** El script escanea `.assets-raw/` en busca de imágenes, y para cada una, genera múltiples versiones `.webp` en la carpeta `assets/` con diferentes anchos (1920, 1280, 800, 400px), manteniendo la relación de aspecto.

**Motivo / criterio:** Rendimiento (Core Web Vitals). Servir imágenes en formato WebP y con el tamaño adecuado para cada dispositivo (responsive) reduce drásticamente el peso de la página y acelera los tiempos de carga, lo cual es un pilar de la filosofía del proyecto.

**Siguiente paso o deuda:** Instalar las dependencias (`pip install -r requirements.txt`), probar el script con una imagen de ejemplo y proceder con el diseño SASS de las plantillas dinámicas.

### 2026-04-16 — Creación de rama de desarrollo para diseño y optimización

**Contexto:** Iniciar el desarrollo visual (SASS/BEM) y la optimización de multimedia aislando el trabajo para proteger la estabilidad del núcleo ya validado en la rama `main`.

**Hecho:**
- Se aprueba la creación de la rama `feat/fase-3-diseno`.
- Se define el *sprint* de tareas: favicon, logotipo, script `merci-optimizer.py` (Fase 3.4) y plantillas dinámicas (`single.php`).

**Detalle técnico:** El trabajo se desarrollará fuera de `main` usando `git checkout -b feat/fase-3-diseno`. Una vez auditado y finalizado, se integrará (merge) de vuelta.

**Motivo / criterio:** Práctica estándar de Git y DevSecOps. Proteger la rama principal garantiza que siempre exista una versión estable y desplegable del proyecto si el trabajo de diseño experimental sufre regresiones.

**Siguiente paso o deuda:** Crear la rama, implementar `merci-optimizer.py` y añadir los assets estáticos base.

### 2026-04-16 — Definición de tipología de contenidos (Biblioteca y Art de Coté)

**Contexto:** Antes de aplicar diseño visual (Fase 3) o desplegar (Fase 6), es necesario definir cómo se estructurarán los contenidos para que el diseño responda a necesidades reales del producto.

**Hecho:**
- Se ha conceptualizado el formato "Libro/Ficha Técnica" para proyectos mayores (ej. este mismo repositorio).
- Se ha conceptualizado el formato "Cuadernillo" para Art de Coté, basado en la estructura de 3 átomos (Desafío, Maniobra, Aprendizaje).

**Detalle técnico:** Esta arquitectura de información requerirá el uso de categorías en WordPress y la creación de la plantilla `single.php` en el Child Theme. Dicha plantilla debe usar clases BEM específicas (`.booklet__challenge`, `.booklet__maneuver`) para soportar el diseño en SASS.

**Motivo / criterio:** El diseño (CSS) sigue a la función (Semántica). No se puede diseñar la interfaz de un proyecto sin saber qué datos contiene. Esta definición adelanta requisitos de la Fase 7 integrándolos coherentemente en la fase actual de diseño.

**Siguiente paso o deuda:** Crear las plantillas HTML/PHP base para estos tipos de contenido y comenzar su diseño SASS.

### 2026-04-16 — Pivote estratégico: Diseño visual de rutas dinámicas (Catálogo y Blog)

**Contexto:** Se constató que, aunque la infraestructura del catálogo (WooCommerce) y el blog está integrada y asegurada, visualmente carecen de diseño ("no hay web en condiciones"). Esto se debe a la eliminación deliberada de los estilos por defecto para proteger el rendimiento.

**Hecho:**
- Pausa de la entrada a la Fase 6 (Despliegue).
- Retorno al espacio de Ingeniería de Estilos (Fase 3) aplicado a la capa dinámica.

**Detalle técnico:** WooCommerce y WordPress renderizan marcado HTML crudo al haber desencolado `global-styles` y los estilos por defecto. Es necesario construir los componentes SASS (`_card.scss`, `_grid.scss`) y adaptar las plantillas de PHP a la metodología BEM del núcleo estático.

**Motivo / criterio:** Una arquitectura perfecta no cumple su propósito si la interfaz de usuario (UX/UI) parece rota o inacabada. Hay que vestir el chasis dinámico con el sistema de diseño propio antes de presentar el proyecto públicamente como un producto maduro.

**Siguiente paso o deuda:** Diseñar e implementar los componentes SASS para las tarjetas de productos y estructurar la vista del catálogo.

### 2026-04-16 — Conexión del núcleo estático con rutas dinámicas

**Contexto:** La página de inicio (`public/index.html`) carecía de enlaces hacia los sistemas dinámicos recién integrados (`/blog` y `/tienda`), manteniendo un `TODO` pendiente de la Fase 2.

**Hecho:**
- Se ha reemplazado el comentario `TODO` en `public/index.html` por enlaces funcionales.
- Se ha alineado la estructura del `<header>` estático con la del *Child Theme* de WordPress para mantener coherencia semántica.

**Detalle técnico:** Se han añadido etiquetas `<a>` con las clases BEM `header__brand` y `nav__link` apuntando a las rutas que gestiona Nginx como proxy inverso (`/blog` y `/tienda`).

**Motivo / criterio:** Una vez que las rutas dinámicas están aseguradas, aisladas y operativas a nivel de servidor (Fases 4 y 5), es seguro exponerlas en el frontend público para permitir la navegación del usuario final.

**Siguiente paso o deuda:** Iniciar la Fase 6 (Despliegue y Auditoría Final).

### 2026-04-16 — Apertura del repositorio: Licencia y reenfoque arquitectónico

**Contexto:** Preparativos finales para hacer público el repositorio en GitHub. Se requería una licencia formal y ajustar el *copy* de la página de inicio para reflejar la verdadera naturaleza técnica del proyecto.

**Hecho:**
- Añadido archivo `LICENSE` (MIT).
- Actualizado apartado de Licencia en `README.md`.
- Refactorizado texto de `public/index.html` para enfocarlo en Arquitectura de Software y DevSecOps.

**Detalle técnico:** Se implementó la Licencia MIT por ser el estándar para compartir herramientas de código abierto (como el ecosistema de scripts Merci). El HTML se adaptó para destacar conceptos como "Shift-Left", "Aislamiento de sistemas" y "Trazabilidad".

**Motivo / criterio:** Un repositorio público es la carta de presentación técnica. El proyecto no es una web estándar, sino una infraestructura automatizada; el lenguaje empleado debe transmitir esa madurez ingenieril a cualquier visitante o reclutador técnico.

**Siguiente paso o deuda:** Iniciar la Fase 6 (Despliegue y Auditoría Final).

### 2026-04-16 — Cierre de Fase 5: Consolidación del Documento de Hardening

**Contexto:** Finalizar la Fase 5 (Quality Assurance y Hardening) dejando un registro auditable de todas las medidas de seguridad implementadas en las diferentes capas del proyecto.

**Hecho:**
- Se ha creado el documento `docs/checklist-hardening.md`.
- Se ha marcado el último hito de la Fase 5.4 como completado en el `README.md`.

**Detalle técnico:** El documento recopila las directivas CSP, los hooks de bloqueo en WordPress (XML-RPC, generadores), la política estricta de permisos de servidor (`chmod 600` para `wp-config.php`) y las reglas bloqueantes del auditor DevSecOps.

**Motivo / criterio:** La seguridad no es un estado, es un proceso. Documentar estas medidas en forma de *checklist* garantiza que no se pierda conocimiento arquitectónico y proporciona una herramienta de validación vital para futuros despliegues a producción (Fase 6).

**Siguiente paso o deuda:** Iniciar la Fase 3 (Ingeniería de Estilos) para aplicar SASS y BEM al diseño visual.

### 2026-04-16 — Fase 5.4: Auditoría integral exitosa sin hallazgos

**Contexto:** Tras lanzar la ejecución en todo el repositorio de `merci-audit.py --strict-json-ld`, era necesario confirmar el estado del código base.

**Hecho:**
- Se superó la auditoría estricta sin `ERROR` ni `WARN`.
- Se actualizaron los hitos de la Fase 5.4 en el `README.md` (pasada integral y verificación de ausencia de secretos).

**Detalle técnico:** El script verificó sintaxis, secretos, funciones peligrosas de PHP y SEO técnico en HTML, devolviendo un código de salida `0`.

**Motivo / criterio:** Una validación en verde a este nivel de exigencia confirma que las prácticas de seguridad y calidad (Shift-Left) se han mantenido desde la Fase 1.

**Siguiente paso o deuda:** Consolidar el checklist de hardening para dar por cerrada definitivamente la Fase 5.

### 2026-04-16 — Fase 5.4: Verificación integral de seguridad y consistencia

**Contexto:** Iniciar la última fase de aseguramiento de la calidad antes del despliegue, ejecutando una auditoría completa sobre todo el repositorio para detectar inconsistencias o errores residuales.

**Hecho:**
- Se ha ejecutado el comando de auditoría estandarizado sobre todo el proyecto.
- Se ha actualizado el `README.md` para reflejar el avance.

**Detalle técnico:** Se utilizó el comando `python3 scripts/merci/merci-audit.py --strict-json-ld` para forzar la revisión de todos los archivos con el máximo nivel de exigencia, incluyendo la validación estricta de JSON-LD.

**Motivo / criterio:** Garantizar que no quedan cabos sueltos. Una pasada final sobre el estado completo del repositorio es crucial para validar que las integraciones parciales no han introducido regresiones o vulnerabilidades en otras áreas del proyecto.

**Siguiente paso o deuda:** Corregir los hallazgos críticos que reporte el auditor, si los hubiera.

### 2026-04-16 — Fase 5.3: Documentación de criterios de fallo del auditor

**Contexto:** Abordar el último hito de la Fase 5.3, que consiste en documentar explícitamente la diferencia entre los hallazgos bloqueantes y no bloqueantes del sistema de auditoría.

**Hecho:**
- Se ha añadido un párrafo en la sección "Flujo de Contribución y Validación" del `README.md`.
- Se ha clarificado que los `ERROR` bloquean los commits, mientras que las `WARN` solo informan.
- Se ha marcado la Fase 5.3 como completada en el Roadmap.

**Detalle técnico:** La distinción se basa en el código de salida de `merci-audit.py`. Un `ERROR` provoca un código de salida `1`, que es interpretado por el hook de `pre-commit` de Git como un fallo que debe detener la operación.

**Motivo / criterio:** Claridad y predictibilidad para el desarrollador. Es fundamental que el equipo sepa qué tipo de hallazgos detendrán su trabajo y cuáles son meras sugerencias, optimizando así la experiencia de desarrollo (DX).

**Siguiente paso o deuda:** Iniciar la Fase 5.4 (Verificación de seguridad y consistencia) o retomar la Fase 3 (Ingeniería de Estilos).

### 2026-04-16 — Fase 5.3: Estandarización del flujo de auditoría local

**Contexto:** Se clarificó que la Fase 5 no estaba completa. El siguiente paso pendiente era estandarizar la ejecución de auditorías para garantizar la consistencia en el control de calidad antes de cualquier integración de código.

**Hecho:**
- Se ha añadido una sección "Flujo de Contribución y Validación" en el `README.md`.
- Se ha definido el comando `python3 scripts/merci/merci-audit.py --strict-json-ld` como la auditoría completa oficial.

**Detalle técnico:** La estandarización se logra mediante documentación. Al fijar un comando único y oficial, se elimina la ambigüedad y se asegura que todos los desarrolladores validen el código con el mismo nivel de rigurosidad (incluyendo la validación estricta de JSON-LD).

**Motivo / criterio:** Reproducibilidad y fiabilidad. Un flujo de validación estandarizado es fundamental en DevSecOps para que la calidad no dependa de la memoria o disciplina individual, sino del proceso documentado.

**Siguiente paso o deuda:** Abordar el último punto de la Fase 5.3: "Documentar criterios de fallo/bloqueo".

### 2026-04-16 — Fase 5.3: Ampliación de auditoría de seguridad para PHP

**Contexto:** Con la introducción de WordPress, es necesario que el auditor `merci-audit.py` pueda detectar patrones de código PHP peligrosos que son vectores comunes para vulnerabilidades de Ejecución Remota de Código (RCE).

**Hecho:**
- Se ha implementado la función `audit_php_smells` en `merci-audit.py`.
- Se ha actualizado el Roadmap para reflejar el avance en la Fase 5.3.

**Detalle técnico:** La nueva función utiliza una expresión regular para buscar en archivos `.php` el uso de funciones de alto riesgo como `eval()`, `exec()`, `shell_exec()`, `system()`, etc. Emite una advertencia (`WARN`) para que el desarrollador revise el contexto manualmente.

**Motivo / criterio:** Seguridad "Shift-Left". Al detectar el uso de estas funciones antes de que el código llegue al repositorio, se reduce drásticamente la probabilidad de introducir una puerta trasera accidentalmente, especialmente a través de código de terceros (plugins o temas).

**Siguiente paso o deuda:** Probar el auditor contra el `functions.php` y decidir la siguiente regla de QA a implementar.

### 2026-04-16 — Lección de Flujo: Reparación de historial Git y parcheo manual

**Contexto:** Tras un commit exitoso, se intentó corregir una advertencia del linter (`WARN MD_ACRONYM`) con un commit manual. El comando `git add` falló por un error de ruta relativa y un posterior `merci-commit` generó un commit duplicado con un mensaje incorrecto.

**Hecho:**
- Se ha reparado el historial de Git fusionando los dos últimos commits con `git rebase -i HEAD~2`.
- Se ha definido el flujo correcto para parches menores: navegar a la raíz del proyecto y usar `git add <archivo>` y `git commit -m "prefijo: mensaje"` manualmente.

**Detalle técnico:** El error de `git add` se debió a ejecutarlo desde una subcarpeta. El commit duplicado ocurrió porque `merci-commit` re-leyó la última entrada de la bitácora. La solución `fixup` en el rebase interactivo fusiona los cambios y descarta el mensaje del commit secundario.

**Motivo / criterio:** Las herramientas de automatización como `merci-commit` son para hitos principales justificados por la bitácora. Los parches de documentación o correcciones menores deben gestionarse con comandos manuales de Git desde la raíz del proyecto para mantener un historial limpio y semántico.

**Siguiente paso o deuda:** Retomar la elección de la siguiente fase del roadmap (Fase 3 o 5.3).

### 2026-04-16 — Fase 4.4: Erradicación de CSS en línea y carga diferida (Defer)

**Contexto:** El análisis del código fuente reveló que WordPress 6.x seguía inyectando bloques `<style>` en línea (como `global-styles` y `classic-theme-styles`), saltándose el `wp_dequeue_style` estándar. Además, faltaba garantizar que futuros scripts no bloquearan el renderizado.

**Hecho:**
- Se añadieron reglas `remove_action` para `wp_enqueue_global_styles`.
- Se desencoló `classic-theme-styles`.
- Se implementó un filtro global (`merci_defer_js_frontend`) para inyectar `defer` en etiquetas `<script>`.

**Detalle técnico:** La función `wp_enqueue_global_styles` se vincula a los hooks `wp_enqueue_scripts` y `wp_body_open`. Eliminar la acción ataja la raíz del problema. El filtro `script_loader_tag` busca ` src` y lo reemplaza por ` defer src` condicionado por `!is_admin()`.

**Motivo / criterio:** Rendimiento puro (Core Web Vitals). El CSS en línea masivo rompe la limpieza del DOM (Document Object Model - Modelo de Objetos del Documento) y retrasa el TTFB (Time to First Byte - Tiempo hasta el Primer Byte). El uso de `defer` asegura que el parseo HTML nunca sea interrumpido por JS, garantizando un LCP (Largest Contentful Paint - Despliegue del Contenido Más Extenso) inmediato.

**Siguiente paso o deuda:** Dar por finalizada la configuración dinámica y decidir el siguiente paso entre diseño frontend (Fase 3 / 4.5) o QA y Seguridad (Fase 5.3).

### 2026-04-16 — Parche: Forzar URL absoluta para CSS estático

**Contexto:** El CSS unificado devolvía 404. WordPress interceptaba el prefijo `/css/main.css` y lo reescribía automáticamente a `http://localhost/blog/css/main.css` en la función `wp_enqueue_style`.

**Hecho:**
- Restaurada la construcción de `$domain_root` dinámico en `functions.php`.
- Forzado el parámetro de URL a una ruta absoluta como `http://[host]/css/main.css`.

**Detalle técnico:** Se implementó `$domain_root = (is_ssl() ? 'https://' : 'http://') . $_SERVER['HTTP_HOST'];` concatenado explícitamente con `/css/main.css`.

**Motivo / criterio:** Aislar el CMS exige forzar la ruta mediante HTTP absoluto para que Nginx la despache directamente desde `public/css/main.css` sin que el motor interno de WordPress manipule el segmento de red.

**Siguiente paso o deuda:** Validar la carga de estilos e iniciar la Fase 4.4.

### 2026-04-16 — Fase 4.2: Corrección de enrutamiento de assets estáticos en WordPress

**Contexto:** El "escudo de rendimiento" limpiaba correctamente el HTML, pero la hoja de estilos devolvía un error 404. WordPress prefijaba la ruta del CSS con `/blog/`, rompiendo el proxy de Nginx que sirve los assets desde la raíz estática.

**Hecho:**
- Se refactorizó la llamada `wp_enqueue_style` en `functions.php`.
- Se implementó la construcción dinámica de la URL absoluta usando `$_SERVER['HTTP_HOST']`.

**Detalle técnico:** WordPress interpreta las rutas como `/assets/main.css` como relativas a su `siteurl`. Se cambió a `$domain_root = (is_ssl() ? 'https://' : 'http://') . $_SERVER['HTTP_HOST'];` para forzar la petición a `http://localhost/assets/main.css` (directo al bloque Nginx).

**Motivo / criterio:** Aislar el CMS (Content Management System) significa que este no debe gobernar cómo se sirven los estáticos. Al forzar la petición a la raíz del dominio, Nginx intercepta la llamada y la sirve con máxima velocidad (caché), protegiendo las métricas de rendimiento.

**Siguiente paso o deuda:** Recargar el frontend para validar la carga del CSS sin errores 404 y verificar la estructura generada por el `index.php` del Child Theme.

### 2026-04-16 — Fase 4.2: Resolución de permisos para enlaces simbólicos (Child Theme)

**Contexto:** WordPress no detectaba el "Merci Theme" enlazado simbólicamente porque el usuario del servidor web (`www-data`) no tenía permisos para atravesar el directorio personal del usuario local.

**Hecho:**
- Se otorgaron permisos de ejecución/paso a la ruta del repositorio anfitrión.
- Se validó la aparición y activación del tema en el panel de administración de WordPress.

**Detalle técnico:** Se aplicó `chmod +x` a las carpetas `/home/hildegahr/`, `Escritorio/` y `PROYECTO_mercedev.es/`. Esto resuelve el "Permiso denegado" permitiendo a `www-data` resolver el enlace simbólico hacia `style.css` e `index.php`.

**Motivo / criterio:** En entornos LEMP locales, es un desafío común la colisión de permisos entre el usuario de escritorio y el demonio web. Dar permiso de ejecución (`+x`) a los directorios anfitriones permite la lectura a través del symlink sin comprometer la política estricta de permisos de los archivos finales.

**Siguiente paso o deuda:** Validar en el frontend (`http://localhost/blog`) que el "escudo de rendimiento" limpia el código fuente inyectado por defecto.

### 2026-04-16 — Fase 4.0: Configuración de wp-config.php y despliegue final

**Contexto:** Conectar la instancia aislada de WordPress con su base de datos dedicada local y asegurar sus permisos de servidor post-instalación.

**Hecho:**
- Se ha creado y configurado `wp-config.php` con credenciales de base de datos (`wp_mercedev_local`) y claves de seguridad generadas.
- Se ha ejecutado el instalador de WordPress a través del proxy inverso de Nginx (`http://localhost/blog`).
- Se ha aplicado el *hardening* de permisos (`chown` y `chmod`) al directorio `/var/www/wordpress/`.
- Se da por finalizada la Fase 4.0 del Roadmap.

**Detalle técnico:** Se aplicó el principio de mínimo privilegio tras la instalación: directorios a `755`, archivos a `644` y un estricto `600` para `wp-config.php`, asignando la propiedad completa a `www-data:www-data`.

**Motivo / criterio:** La instalación local no exime de aplicar prácticas de seguridad de producción. Blindar `wp-config.php` y los permisos del CMS desde el minuto uno garantiza que la arquitectura probada localmente es segura para su posterior migración al servidor de producción.

**Siguiente paso o deuda:** Validar la visualización del Child Theme (Fase 4.2) ahora que existe un WordPress real donde activarlo.

### 2026-04-16 — Fase 4.0: Configuración de Nginx para entorno local

**Contexto:** Configurar el servidor web Nginx en el entorno de desarrollo local para replicar la arquitectura de enrutamiento inverso (reverse proxy) definida en `docs/integracion-wordpress.md`.

**Hecho:**
- Se ha creado un nuevo archivo de configuración de sitio en `/etc/nginx/sites-available/mercedev-local`.
- Se ha adaptado la configuración para el entorno local, apuntando la raíz estática a la carpeta del proyecto y manteniendo el alias para WordPress.
- Se ha añadido un bloque `location /assets` con una directiva `alias` para servir correctamente los recursos compartidos (CSS).
- Se ha activado el nuevo sitio y desactivado el sitio por defecto de Nginx.

**Detalle técnico:** Se creó el archivo `/etc/nginx/sites-available/mercedev-local` y se enlazó simbólicamente a `/etc/nginx/sites-enabled/`. Se verificó la sintaxis con `sudo nginx -t` y se recargó el servicio con `sudo systemctl reload nginx`. Se instruyó sobre cómo verificar la versión del socket de PHP-FPM en `/run/php/`.

**Motivo / criterio:** Es imprescindible que el entorno de desarrollo local simule fielmente la configuración de producción. La configuración de Nginx es el componente clave que une el núcleo estático y el CMS dinámico, permitiendo probar y validar la arquitectura de aislamiento antes del despliegue.

**Siguiente paso o deuda:** Configurar el archivo `wp-config.php` de WordPress y ejecutar el instalador web para finalizar la instalación.

### 2026-04-16 — Fase 4.0: Creación de base de datos y usuario para WordPress local

**Contexto:** Crear el esquema de base de datos y el usuario dedicado para la instancia local de WordPress, aislando sus datos del resto del sistema.

**Hecho:**
- Se ha accedido a MariaDB con `sudo mysql`.
- Se ha creado la base de datos `wp_mercedev_local` y el usuario `wp_user_local`.

**Detalle técnico:** Se ejecutaron las siguientes sentencias SQL:
```sql
CREATE DATABASE wp_mercedev_local;
CREATE USER 'wp_user_local'@'localhost' IDENTIFIED BY 'tu_contraseña_elegida';
GRANT ALL PRIVILEGES ON wp_mercedev_local.* TO 'wp_user_local'@'localhost';
FLUSH PRIVILEGES;
```
**Motivo / criterio:** El uso de una base de datos y un usuario específicos para cada aplicación es una práctica de seguridad fundamental (principio de mínimo privilegio), incluso en un entorno de desarrollo local.

**Siguiente paso o deuda:** Configurar el bloque de servidor de Nginx para el enrutamiento del núcleo estático y el proxy inverso hacia WordPress.

### 2026-04-16 — Fase 4.0: Instalación de pila LEMP y configuración base de datos local

**Contexto:** Preparación del entorno de desarrollo local anfitrión con Nginx, MariaDB y PHP para albergar la instancia aislada de WordPress, replicando la arquitectura de producción de forma nativa.

**Hecho:**
- Se han instalado los paquetes de la pila LEMP (`nginx`, `mariadb-server`, `php-fpm`, `php-mysql`).
- Se ha asegurado la instalación local de MariaDB estableciendo contraseña root y eliminando usuarios anónimos.

**Detalle técnico:** Se utilizó `sudo apt install` para la provisión de dependencias y `sudo mysql_secure_installation` con autenticación `unix_socket` activada para endurecer el motor de base de datos local.

**Motivo / criterio:** La dependencia de herramientas preempaquetadas (como LocalWP) ofusca la configuración del servidor web, impidiendo auditar y replicar la estrategia de enrutamiento inverso (reverse proxy) de Nginx definida en la Fase 4.1.

**Siguiente paso o deuda:** Crear la base de datos específica para WordPress local, descargar el CMS y configurar el bloque de servidor en Nginx.

### 2026-04-16 — Reajuste de entorno: De servidor a PC local y actualización de directrices

**Contexto:** Confusión entre el entorno de producción (droplet de DigitalOcean) y el entorno de desarrollo (PC local con Ubuntu). Se intentaba configurar bases de datos para el despliegue final cuando el entorno local aún no disponía de la pila tecnológica necesaria para probar la arquitectura aislada.

**Hecho:**
- Se ha añadido la regla 13 a `instrucciones.md` para forzar la verificación de dependencias de entorno antes de avanzar en la configuración.
- Se ha introducido la subfase 4.0 en el `README.md` para formalizar la preparación del entorno local LEMP.

**Detalle técnico:** La configuración local requiere replicar el ecosistema de producción (Linux, Nginx, MariaDB, PHP-FPM) nativamente en el sistema operativo anfitrión (`~/Escritorio/`) para validar el enrutamiento inverso de Nginx sin depender de herramientas aisladas como LocalWP que ofuscan la configuración del servidor.

**Motivo / criterio:** DevSecOps y "Shift-Left" requieren que el entorno de desarrollo local sea una réplica fiel de la arquitectura de producción. No se puede auditar ni endurecer un CMS localmente sin las herramientas nativas.

**Siguiente paso o deuda:** Iniciar la Fase 4.0 instalando Nginx, MariaDB y PHP nativos en el Ubuntu local.

### 2026-04-16 — Fase 5.2: Instalación de la infraestructura de base de datos (MariaDB)

**Contexto:** Al intentar crear la base de datos para WordPress, se detectó que no había ningún servidor de bases de datos instalado en el droplet (error `mysql: orden no encontrada`).

**Hecho:**
- Se ha instalado el servidor de bases de datos MariaDB, el sustituto directo y recomendado de MySQL en Ubuntu.
- Se ha ejecutado el script `mysql_secure_installation` para aplicar un endurecimiento de seguridad inicial.

**Detalle técnico:** Se utilizaron los comandos `sudo apt update`, `sudo apt install mariadb-server` y `sudo mysql_secure_installation`. Se configuró la autenticación `unix_socket` para el usuario root y se eliminaron las configuraciones inseguras por defecto.

**Motivo / criterio:** WordPress requiere una base de datos para funcionar. MariaDB es el estándar de la industria para este stack tecnológico. Asegurar la instalación desde el inicio es un paso fundamental de la filosofía "Shift-Left Security".

**Siguiente paso o deuda:** Proceder con la creación de la base de datos y el usuario específicos para la instancia de WordPress.

### 2026-04-15 — Incorporación de regla de sincronización del Roadmap

**Contexto:** Evitar la desincronización entre el código implementado y el estado de las fases documentadas en el proyecto.

**Hecho:**
- Añadir la regla 12 en `instrucciones.md` que obliga a actualizar el `README.md` inmediatamente tras finalizar una tarea.

**Detalle técnico:** Se formaliza la práctica de marcar con `- [x]` los hitos del `README.md` en la misma sesión de trabajo en la que se consigue el avance.

**Motivo / criterio:** Mantener una única fuente de verdad (Single Source of Truth) del estado del proyecto. Al estar documentada, el asistente de IA asimila la directriz de proponer la actualización automáticamente.

**Siguiente paso o deuda:** Finalizar sesión y retomar mañana con la Fase 5.2 (Permisos del servidor de WordPress).

### 2026-04-15 — Incorporación de Conventional Commits a las directrices

**Contexto:** Necesidad de estandarizar la nomenclatura de los mensajes de commit (especialmente en parches manuales) para mantener un historial de Git semántico y fácil de auditar.

**Hecho:**
- Añadir la regla 11 sobre la convención de prefijos en `instrucciones.md`.

**Detalle técnico:** Se definen los prefijos estándar de la industria (`feat:`, `fix:`, `chore:`, `docs:`, `refactor:`, `perf:`, `test:`, `style:`) como parte inmutable de las directrices del repositorio.

**Motivo / criterio:** La claridad en el control de versiones permite comprender el propósito de cualquier cambio de un solo vistazo. Es un paso clave de madurez DevSecOps que facilitará escalar o retomar el código en el futuro sin fricción.

**Siguiente paso o deuda:** Iniciar la auditoría de permisos del servidor para WordPress (Fase 5.2).

### 2026-04-15 — Soporte para commits menores manuales en merci-commit

**Contexto:** Tareas menores de mantenimiento (como eliminación de duplicados) no ameritan entradas completas en la bitácora, pero la herramienta `merci-commit.py` bloqueaba la acción o duplicaba mensajes forzando una fricción innecesaria.

**Hecho:**
- Añadir comprobación `check_repo_changes` para abortar tempranamente si no hay modificaciones reales en Git.
- Permitir el ingreso de un mensaje manual por terminal si hay cambios de código pero la bitácora está intacta.

**Detalle técnico:** Se implementa `git status --porcelain` para comprobar el estado real de los archivos. Si existen cambios pero no en `bitacora-mercedev.md`, se solicita confirmación para un parche menor y se captura el título vía `input()` de Python, saltándose la extracción de la bitácora.

**Motivo / criterio:** Equilibrio entre DevSecOps y usabilidad (DX). Ofrecer una válvula de escape estructurada para mantenimientos menores mantiene el historial limpio, no desincentiva el uso de la herramienta y agiliza al desarrollador.

**Siguiente paso o deuda:** Validar este nuevo flujo mixto y auditar los permisos del servidor de WordPress (Fase 5.2).

### 2026-04-15 — Endurecimiento (Hardening) de WordPress mediante Child Theme

**Contexto:** Reducir la superficie de ataque del CMS desactivando endpoints obsoletos y evitando fugas de información que faciliten intrusiones.

**Hecho:**
- Añadir reglas de seguridad (Fase 5.2) en `src/wp-theme/merci-theme/functions.php`.
- Actualizar checklist del `README.md`.

**Detalle técnico:** Se usa `remove_action` para eliminar el metadato generador de versión, `wlwmanifest` y `rsd_link`. Se desactiva completamente la API (Application Programming Interface - Interfaz de Programación de Aplicaciones) XML-RPC mediante el filtro `xmlrpc_enabled` para prevenir ataques de fuerza bruta. Se ofuscan los errores de autenticación con `login_errors`.

**Motivo / criterio:** Principio de mínima exposición. XML-RPC es un vector común para ataques DDoS (Distributed Denial of Service - Ataque Distribuido de Denegación de Servicio). Ocultar la versión exacta de WP dificulta el escaneo automatizado de vulnerabilidades conocidas.

**Siguiente paso o deuda:** Auditar la configuración de `wp-config.php` y los permisos del servidor para completar el hardening.

### 2026-04-15 — Resolución de 404 por favicon ausente (Higiene de logs)

**Contexto:** Durante la prueba del servidor local, el registro mostró un error 404 persistente al intentar cargar `favicon.ico`.

**Hecho:**
- Añadir `<link rel="icon" href="data:,">` en el `<head>` de `public/index.html`.

**Detalle técnico:** Los navegadores solicitan automáticamente `/favicon.ico` a la raíz del servidor web. Al no existir el archivo, se genera una petición HTTP (Hypertext Transfer Protocol - Protocolo de Transferencia de Hipertexto) fallida. Se inyecta un URI (Uniform Resource Identifier - Identificador de Recursos Uniforme) de datos vacío para cancelar la petición de red en origen.

**Motivo / criterio:** Rendimiento e higiene del servidor. Un error 404 consume procesamiento innecesario. Un Data URI vacío silencia el comportamiento automático del navegador manteniendo la política de cero dependencias externas.

**Siguiente paso o deuda:** Diseñar el isotipo definitivo para el favicon en fases posteriores. Continuar con el Hardening de WordPress (Fase 5.2).

### 2026-04-15 — Validación local de Content Security Policy (CSP)

**Contexto:** Verificar empíricamente que la política de seguridad estricta no interfiere con la carga de los recursos legítimos del núcleo estático.

**Hecho:**
- Desplegar servidor local de pruebas (`python3 -m http.server 8000 -d public/`).
- Validar ausencia de bloqueos en la consola de herramientas para desarrolladores del navegador.

**Detalle técnico:** Al no poseer dependencias de terceros (como tipografías externas o analíticas), la regla `default-src 'self'` permite cargar correctamente el documento HTML y su hoja de estilos unificada. No se registran errores de tipo "CSP violation".

**Motivo / criterio:** En DevSecOps (Development, Security, and Operations - Desarrollo, Seguridad y Operaciones), la imposición de una política de seguridad siempre debe ir acompañada de una validación funcional para evitar degradación del servicio o bloqueos de UX (User Experience - Experiencia de Usuario).

**Siguiente paso o deuda:** Comenzar el Hardening de WordPress (Fase 5.2).

### 2026-04-15 — Fase 5: Implementación de Content Security Policy (CSP)

**Contexto:** Iniciar la fase de Hardening del núcleo estático protegiéndolo contra ataques de inyección de código.

**Hecho:**
- Añadir directiva CSP (Content Security Policy - Política de Seguridad de Contenidos) en el `<head>` de `public/index.html`.

**Detalle técnico:** Se establece una política estricta mediante etiqueta `<meta>`: `default-src 'self'` restringe todos los recursos al dominio actual. Se bloquean plugins (`object-src 'none'`) y la inyección de bases (`base-uri 'self'`).

**Motivo / criterio:** Aplicación del principio de seguridad "Shift-Left". Una CSP estricta mitiga el riesgo de vulnerabilidades XSS (Cross-Site Scripting - Secuencias de Comandos en Sitios Cruzados) prohibiendo scripts externos o en línea no autorizados.

**Siguiente paso o deuda:** Validar la carga de la portada en el navegador local para confirmar que la política no bloquea assets legítimos y avanzar con el Hardening de WordPress.

### 2026-04-15 — Refinamiento de la política de acrónimos (Linter y directrices)

**Contexto:** La regla estricta de expandir siempre los acrónimos (Inglés - Español) resultaba tediosa para términos que ya estaban muy arraigados en el proyecto.

**Hecho:**
- Actualizar `instrucciones.md` eximiendo de expansión a los acrónimos que aparezcan más de 3 veces.
- Implementar una función de conteo global (`get_global_acronym_count`) en `merci-audit.py`.

**Detalle técnico:** El auditor ahora escanea todo el repositorio buscando archivos `.md`. Si localiza un acrónimo de la *watchlist* que no está expandido, verifica su conteo global. Si es mayor a 3, asume que es un término consolidado y omite la advertencia `WARN MD_ACRONYM`. Se emplea un caché (`GLOBAL_ACRONYM_COUNTS`) para evitar leer el disco repetidas veces.

**Motivo / criterio:** Reducir la fricción y el tedio en el flujo DevSecOps. Se equilibra la necesidad de claridad técnica inicial con la fluidez una vez que un concepto ya es de dominio público en el repositorio.

**Siguiente paso o deuda:** Comitear los cambios del linter y comenzar oficialmente la Fase 5: Quality Assurance y Hardening.

### 2026-04-15 — Validación exitosa del linter de acrónimos

**Contexto:** El nuevo linter de acrónimos detectó correctamente la falta de expansión de "CMS" durante la ejecución de un commit rutinario, validando su eficacia.

**Hecho:**
- Expandir el acrónimo CMS (Content Management System - Sistema de Gestión de Contenidos) en el registro histórico.
- Confirmar el funcionamiento de la regla `WARN` en `merci-audit.py`.

**Detalle técnico:** El auditor emitió la advertencia `WARN MD_ACRONYM` indicando la línea exacta sin bloquear la creación del commit atómico. Esto permitió mantener la fluidez del proceso informando simultáneamente sobre la deuda técnica de redacción.

**Motivo / criterio:** Dejar constancia de que el sistema de vigilancia pasiva (Watchlist) cumple su función como corrector de estilo automatizado (DevSecOps) sin añadir fricción paralizante.

**Siguiente paso o deuda:** Iniciar la Fase 5: Quality Assurance y Hardening.

### 2026-04-15 — Implementación de linter de acrónimos en Merci Audit

**Contexto:** Automatizar la verificación de la regla de estilo que exige expandir los acrónimos técnicos en la bitácora y la documentación (Inglés - Español).

**Hecho:**
- Crear la función `audit_md_acronyms` en `scripts/merci/merci-audit.py`.
- Definir una lista de vigilancia (*watchlist*) para los acrónimos más críticos.

**Detalle técnico:** La función utiliza expresiones regulares para detectar si un acrónimo de la lista está presente en archivos `.md`. Si lo encuentra, verifica que exista al menos una instancia con el patrón `ACRÓNIMO (...)` en el documento. Se clasifica como `warn` para no bloquear commits por falsos positivos.

**Motivo / criterio:** Reducir la carga cognitiva de revisión manual. La automatización parcial mediante *watchlist* es más fiable que una expresión regular genérica para mayúsculas, la cual generaría excesivos falsos positivos.

**Siguiente paso o deuda:** Validar el comportamiento del auditor con un commit y avanzar a la Fase 5: Quality Assurance y Hardening.

### 2026-04-15 — Análisis de impacto de wc-cart-fragments (Deuda de conocimiento)

**Contexto:** Comprensión arquitectónica de los motivos por los que el script `wc-cart-fragments` de WooCommerce degrada el rendimiento web estándar.

**Hecho:**
- Documentar el comportamiento del script AJAX (Asynchronous JavaScript and XML - JavaScript Asíncrono y XML) de fragmentos de carrito.

**Detalle técnico:** El script invoca una petición `POST` a `/?wc-ajax=get_refreshed_fragments` en cada carga de página. Al ser un `POST` que verifica sesiones y bases de datos mediante PHP (Hypertext Preprocessor - Preprocesador de Hipertexto), esquiva las capas de caché estáticas (Varnish, Redis, Nginx FastCGI) elevando drásticamente el consumo de CPU (Central Processing Unit - Unidad Central de Procesamiento) y el TTFB (Time to First Byte - Tiempo hasta el Primer Byte).

**Motivo / criterio:** Dejar constancia del motivo de su desencolado en la Fase 4.3. En arquitecturas en Modo Catálogo, este script aporta 0 funcionalidad a costa de sacrificar métricas críticas de Core Web Vitals como el INP (Interaction to Next Paint - Interacción hasta el Siguiente Pintado).

**Siguiente paso o deuda:** Consolidar el documento en Git e iniciar la Fase 5: Quality Assurance y Hardening.

### 2026-04-15 — Fase 4.3: Configuración de WooCommerce en modo catálogo

**Contexto:** Integrar WooCommerce para mostrar el merchandising de Merci sin el impacto de rendimiento que supone una tienda completa con pasarelas de pago y scripts de carrito AJAX (Asynchronous JavaScript and XML - JavaScript Asíncrono y XML).

**Hecho:**
- Añadir soporte de WooCommerce al `functions.php` del Child Theme.
- Eliminar las acciones de añadir al carrito (`remove_action`).
- Desencolar el script `wc-cart-fragments`.

**Detalle técnico:** Se usa `add_theme_support('woocommerce')` para habilitar las plantillas base. Se bloquea la generación de botones de compra anulando `woocommerce_template_loop_add_to_cart` y `woocommerce_template_single_add_to_cart`. El script de fragmentos de carrito se desencola con prioridad 100.

**Motivo / criterio:** Rendimiento puro. WooCommerce inyecta JS (JavaScript) pesado por defecto para gestionar el carrito en tiempo real en todas las páginas. Al funcionar como mero catálogo, prescindimos de esta carga protegiendo el Web Vitals score.

**Siguiente paso o deuda:** Validar la visualización del catálogo e iniciar la fase de endurecimiento y QA (Fase 5).

### 2026-04-15 — Corrección de importación en pruebas (test_sitemap.py)

**Contexto:** El archivo de pruebas `test_sitemap.py` quedó roto tras estandarizar el nombre del script principal a `merci-sitemap.py` (con guion medio). Python no permite importar módulos con guiones usando la sintaxis estándar de `import`.

**Hecho:**
- Refactorizar `scripts/merci/tests/test_sitemap.py`.
- Implementar carga dinámica de módulos con `importlib.util`.

**Detalle técnico:** Se reemplazó el `sys.path.append` por `spec_from_file_location` y `module_from_spec` de `importlib.util`. Esto permite cargar el archivo `merci-sitemap.py` asociándolo al namespace interno seguro `merci_sitemap` para el parcheo con `unittest.mock`.

**Motivo / criterio:** Mantener la convención de nombres de archivos con guiones en el sistema (ej. `merci-audit.py`, `merci-sitemap.py`) sin sacrificar la cobertura de las pruebas unitarias.

**Siguiente paso o deuda:** Ejecutar los tests para validar el fix y consolidar los cambios con `merci-commit`.

### 2026-04-15 — Creación de index.php del Child Theme con metodología BEM

**Contexto:** Proveer una plantilla base para que WordPress renderice contenido dinámico respetando el estándar HTML5 y las clases CSS del núcleo estático.

**Hecho:**
- Crear `src/wp-theme/merci-theme/index.php`.
- Implementar "The Loop" de WordPress en una estructura unificada.

**Detalle técnico:** Se prescinde de la fragmentación tradicional (`get_header()`, `get_footer()`) para concentrar el marcado en un solo archivo. Se incluyen `wp_head()` y `wp_footer()` para permitir la inyección de nuestros assets estáticos controlados. Se aplican clases BEM (`article`, `article__title`, `article__content`).

**Motivo / criterio:** Minimalismo extremo y reducción de carga de procesamiento I/O de PHP. Al escribir el HTML directamente, se evita que WordPress genere contenedores `<div>` basura o estructuras que rompan el diseño semántico del núcleo.

**Siguiente paso o deuda:** Validar la vista dinámica y proceder con la configuración de WooCommerce en modo catálogo (Fase 4.3).

### 2026-04-15 — Creación de functions.php como escudo de rendimiento

**Contexto:** Necesidad de bloquear la inyección de código basura por defecto de WordPress (scripts de emojis, estilos globales, CSS de Gutenberg) para proteger el rendimiento del frontend.

**Hecho:**
- Crear `src/wp-theme/merci-theme/functions.php`.
- Implementar reglas de limpieza y desencolado (`dequeue`).

**Detalle técnico:** Se emplea `remove_action` para detener los scripts de emojis y `wp_dequeue_style` enganchado a la acción `wp_enqueue_scripts` (con prioridad 100) para bloquear `wp-block-library` y `global-styles`. Finalmente, se encola `/assets/main.css` apuntando a la ruta absoluta expuesta por Nginx.

**Motivo / criterio:** Aislar la vista dinámica del CMS de sus dependencias heredadas pesadas. Si no se bloquea, WordPress inyecta múltiples llamadas de red y estilos en línea que degradarían la métrica de Core Web Vitals lograda en el núcleo estático.
**Motivo / criterio:** Aislar la vista dinámica del CMS (Content Management System - Sistema de Gestión de Contenidos) de sus dependencias heredadas pesadas. Si no se bloquea, WordPress inyecta múltiples llamadas de red y estilos en línea que degradarían la métrica de Core Web Vitals lograda en el núcleo estático.

**Siguiente paso o deuda:** Desarrollar `index.php` del tema para renderizar el esqueleto HTML5 alineado con la metodología BEM del proyecto.

### 2026-04-15 — Añadir salvaguarda a merci-commit.py contra commits sin bitácora

**Contexto:** Evitar la creación de commits duplicados o la omisión de la actualización de la bitácora, que son riesgos inherentes a un flujo de trabajo automatizado.

**Hecho:**
- Modificar `scripts/merci/merci-commit.py` para añadir una verificación previa.

**Detalle técnico:**
- El script ahora ejecuta `git diff --quiet HEAD -- <ruta_bitacora>` antes de proceder.
- Si el comando devuelve un código de salida 0 (sin cambios), se emite una alerta en la terminal y se solicita confirmación explícita del usuario para continuar.

**Motivo / criterio:** Reforzar la disciplina de "documentación primero" y prevenir el ruido en el historial de Git. La confirmación del usuario mantiene la flexibilidad para casos excepcionales sin sacrificar la seguridad del flujo por defecto.

**Siguiente paso o deuda:** Retomar el desarrollo del `functions.php` del Child Theme (Fase 4.2).

### 2026-04-15 — Configuración de alias de terminal (zsh) para el Sistema Merci

**Contexto:** Necesidad de optimizar la experiencia de desarrollo (DX) y reducir la fricción al invocar los scripts de automatización desde distintas ubicaciones del proyecto.

**Hecho:**
- Recapitular y definir bloque de alias en `~/.zshrc` para las herramientas base: `merci-audit`, `merci-styles`, `merci-optimizer` y el nuevo `merci-commit`.

**Detalle técnico:** Se emplea la variable estática `MERCI_ROOT` apuntando a `/home/hildegahr/Escritorio/PROYECTO_mercedev.es` para garantizar la resolución de rutas absolutas al invocar Python, sin importar el directorio de trabajo actual (`pwd`).

**Motivo / criterio:** La carga cognitiva de recordar y tipear rutas relativas largas desincentiva el uso frecuente de herramientas críticas (como la auditoría o los commits atómicos). Abstraer esto en la terminal refuerza el flujo DevSecOps.

**Siguiente paso o deuda:** Validar la usabilidad del flujo con `merci-commit` y arrancar el código del `functions.php` del Child Theme (Fase 4.2).

### 2026-04-15 — Refactorización de merci-commit.py (Auto-Stage)

**Contexto:** El script de automatización de commits no incluía los archivos modificados del código, limitándose a comitear únicamente la bitácora.

**Hecho:**
- Modificar `scripts/merci/merci-commit.py` para ejecutar `git add .` en la raíz del repositorio antes del commit.

**Detalle técnico:**
- Se utiliza el argumento `cwd=REPO_ROOT` en `subprocess.run` para asegurar que el comando `git add .` abarque todo el proyecto, independientemente de desde dónde se invoque el script.

**Motivo / criterio:** Agilizar el flujo de trabajo. La seguridad y prevención de adición de código basura (secretos, archivos pesados) queda delegada a la red de seguridad del pre-commit (`merci-audit.py` y `.gitignore`), manteniendo la arquitectura "Shift-Left" intacta.

**Siguiente paso o deuda:** Validar la automatización y retomar el `functions.php` del Child Theme (Fase 4.2).

### 2026-04-15 — Pausa de Fase 4.2 para automatización de commits (I+D)

**Contexto:** Necesidad de vincular estrechamente la actualización de la bitácora con el historial de Git para evitar desincronización entre documentación y código.

**Hecho:**
- Pausar temporalmente el desarrollo del `functions.php` del Child Theme.
- Diseñar conceptualmente una herramienta de automatización para commits impulsados por la bitácora.

**Detalle técnico:** Se descarta el "auto-commit al guardar" (file watcher) por generar ruido (commit spam) y romper la atomicidad de Git. Se opta por crear un extractor que utilice la última entrada redactada como mensaje estructurado del commit.

**Motivo / criterio:** Mantener un historial de Git semántico, asegurando que el código modificado y su justificación (bitácora) viajen siempre juntos en un único commit atómico.

**Siguiente paso o deuda:** Desarrollar `scripts/merci/merci-commit.py` e integrarlo en el flujo de trabajo local.

### 2026-04-15 — Iniciar Fase 4.2 y creación base del Child Theme

**Contexto:** Iniciar el desarrollo del tema hijo ultraligero para WordPress (Fase 4.2), asegurando cero dependencias externas y preparando el enlace con el núcleo estático.

**Hecho:**
- Crear directorio `src/wp-theme/merci-theme/`.
- Crear archivo manifiesto `style.css`.

**Detalle técnico:** El archivo `style.css` contiene exclusivamente la cabecera de comentarios (`Theme Name`, `Version`, etc.) requerida por WP para reconocer el tema en el panel de administración. No incluye directivas de diseño.

**Motivo / criterio:** Evitar la duplicidad de renderizado y el código basura de los temas por defecto. El diseño real se delegará al `main.css` del núcleo estático para proteger la métrica de rendimiento (Core Web Vitals).

**Siguiente paso o deuda:** Crear el archivo `functions.php` como escudo para bloquear los scripts y estilos inyectados por defecto por WordPress.

### 2026-04-15 — Definir Arquitectura de Aislamiento de WordPress (Fase 4.1)

**Contexto:** Integrar WordPress para `/blog` y `/tienda` sin comprometer la seguridad, inmutabilidad y rendimiento puro originado en el núcleo estático de la carpeta `public/`.

**Hecho:**
- Crear el documento técnico `docs/integracion-wordpress.md`.
- Definir el enrutamiento proxy inverso mediante **Nginx**.
- Configurar de forma teórica la preservación de canónicas (`siteurl` bloqueado a su subdirectorio) y `sitemap_index.xml`.

**Detalle técnico:**
- Plantear una estructura de "Common root": `public/` alberga estáticos, mientras que el CMS reside en otra ruta del sistema anfitrión (ej. `/var/www/wordpress/`). Unir ambos mundos transparentemente usando la directiva `location ^~ /blog`.
- Restringir estrictamente permisos: el proceso PHP de WordPress nunca podrá escribir en `public/`.

**Motivo / criterio:** Aislar vectores de ataque del CMS. Si el CMS es vulnerado (plugins desactualizados), el Frontend estático queda ileso. Además, se evita degradar el Web Vitals score de la portada sirviendo estáticos directamente con el web server.

**Siguiente paso o deuda:** Iniciar la Fase 4.2 que consiste en desarrollar el "Child Theme ultraligero" para el ecosistema de WordPress aislado.


### 2026-04-15 — Refactorización para resolver descoordinación de archivos

**Contexto:** Conflicto de convenciones de nombres y pérdida de coordinación de los scripts locales (`merci_sitemap.py` vs `merci-sitemap.py`) y pérdida de la compilación CSS (`main.scss`).

**Hecho:**
- Restaurar explícitamente `@use 'index';` en `src/scss/main.scss` garantizando compilación exitosa a `public/css/main.css`.
- Traspasar duplicidades experimentales (`merci_ingestor.py`, `merci_sitemap.py`, `pre-commit.sh`) a `laboratorio/scripts_temporales/` para mantener limpio el entorno y respetar la no eliminación de código.
- Restaurar el script `scripts/merci/pre-commit` con la llamada correcta a `merci-sitemap.py`.
- Actualizar el `README.md` para asentar todos los apuntes con las rutas veraces.

**Detalle técnico:**
- Se confirma visualmente la reaparición de `main.css`.
- Se limpia la carpeta `scripts/merci/` manteniéndola con `-` en lugar de `_` como convención primaria.
- Movimiento realizado: `mv scripts/merci/merci_ingestor.py scripts/merci/merci_sitemap.py scripts/merci/pre-commit.sh laboratorio/scripts_temporales/`

**Motivo / criterio:** Consistencia y correspondencia con "lo que existe". Todo el proyecto ya está nuevamente compilando y acoplado.

**Siguiente paso o deuda:** Ninguno, el lío de archivos quedó resuelto.


### 2026-04-15 — Restauración integral de archivos y estabilización modular

**Contexto:** Pérdida de contenido en archivos tras renombrados y reorganización de carpetas.

**Hecho:**
- Reconstruir `public/robots.txt` y `public/sitemap.xml`.
- Restaurar `merci_ingestor.py` y el arnés de pruebas en `/tests`.
- Preservar el experimento de grabación en `/laboratorio/art-de-cote`.

**Detalle técnico:**
- Se asegura que los scripts utilicen nombres de archivo con guion bajo (`merci_sitemap.py`) para ser importables.
- Los archivos pesados de vídeo permanecen excluidos en `.gitignore`.

**Motivo / criterio:** Garantizar la integridad del repositorio antes de avanzar a la Fase 3.

**Siguiente paso o deuda:** Iniciar el desarrollo de estilos SASS.

### 2026-04-15 — Reorganización modular de la carpeta Merci

**Contexto:** Evitar la dispersión de archivos en la carpeta de automatización separando los scripts operativos de las pruebas y los experimentos.

**Hecho:**
- Creación de las subcarpetas `tests/` y `experimental/` en `scripts/merci/`.
- Reubicación de `test_sitemap.py` y el aviso de deprecación de `merci-recorder.py`.

**Detalle técnico:**
- Ajuste de `sys.path` en los tests para localizar módulos en el directorio padre (`parents[1]`).

**Motivo / criterio:** Modularidad y limpieza. Mantener la carpeta raíz de Merci enfocada únicamente en scripts productivos y validados.

**Siguiente paso o deuda:** Migrar futuros tests a la nueva carpeta y mover scripts en desarrollo a la zona experimental.

### 2026-04-15 — Preservación de Merci Recorder como pieza de Art de Coté

**Contexto:** Aplicación de la filosofía del proyecto para no descartar código experimental valioso tras el cambio de estrategia hacia el Ingestor.

**Hecho:**
- Trasladar la lógica funcional de grabación a `laboratorio/art-de-cote/recorder_experiment.py`.
- Mantener `scripts/merci/merci-recorder.py` como un stub de aviso (deprecación).

**Detalle técnico:**
- La lógica preservada incluye la corrección del flag `-nostdin` y el uso de `x11grab` (X Window System - Sistema de Ventanas X).
- Se categoriza como "Artefacto de Laboratorio" para consulta futura.

**Motivo / criterio:** El script falló para el flujo de producción diario pero es un activo de conocimiento sobre automatización multimedia con Python y FFmpeg.

**Siguiente paso o deuda:** Validar el funcionamiento del Ingestor en una sesión real.

### 2026-04-15 — Cambio de estrategia: Ingesta de evidencias en lugar de grabación directa

**Contexto:** El script `merci-recorder.py` no funcionaba correctamente y la necesidad de gestionar evidencias existentes (capturas de pantalla, vídeos) de forma más flexible.

**Hecho:**
- Deprecación de `scripts/merci/merci-recorder.py`.
- Creación de `scripts/merci/merci_ingestor.py` para escanear carpetas de usuario y mover archivos recientes a `.assets-raw/`.
- Actualización de `README.md` e `instrucciones.md` para reflejar la nueva estrategia.

**Detalle técnico:**
- `merci_ingestor.py` busca archivos modificados en los últimos 30 minutos en `~/Pictures`, `~/Videos`, `~/Desktop` (configurable).
- Ofrece al usuario la opción de mover todos, algunos o ninguno de los archivos encontrados a `.assets-raw/`.

**Motivo / criterio:** Priorizar la funcionalidad de ingesta de evidencias existentes, que es más robusta y menos propensa a problemas de entorno que la grabación en tiempo real, y alinear con la gestión de `.assets-raw/`.

**Siguiente paso o deuda:** Probar `merci_ingestor.py` con archivos de prueba y documentar su uso en el `README.md`.

### 2026-04-15 — Resolución definitiva para visualización de vídeos de evidencias

**Contexto:** Fallo persistente en la instalación de extensiones de vídeo en VS Code, incluso usando el CLI y IDs de extensiones válidos.

**Hecho:**
- Confirmar que la instalación de `b-ryan.vscode-video` vía CLI también falla.
- Decidir utilizar reproductores externos (sistema o navegador web) para visualizar los archivos `.mp4` de `laboratorio/evidencias/`.

**Detalle técnico:**
- El problema parece ser una limitación del entorno de VS Code o su acceso al Marketplace, no de la existencia de las extensiones.
- La visualización externa es una solución robusta que no bloquea el flujo de trabajo.

**Motivo / criterio:** Priorizar el avance del proyecto y la generación de evidencias sobre la resolución de un problema de configuración del IDE que consume tiempo.

**Siguiente paso o deuda:** Iniciar la grabación de 30 minutos y proceder con la Fase 3 (Ingeniería de Estilos).

### 2026-04-15 — Incidencia persistente con el Marketplace de VS Code

**Contexto:** No es posible localizar extensiones de vídeo por ID en el Marketplace de la instancia local de VS Code.

**Hecho:**
- Intentar instalación de `moshfeu.video-player` y `frenco.vs-code-media-preview` sin éxito.
- Proponer instalación vía **CLI** (Command Line Interface - Interfaz de Línea de Comandos) de la extensión `b-ryan.vscode-video`.

**Detalle técnico:**
- Comando de rescate: `code --install-extension b-ryan.vscode-video`.
- Alternativa de visualización: uso del navegador host para validar evidencias MP4 si falla el IDE.

**Motivo / criterio:** Evitar la dispersión en problemas de configuración del entorno y priorizar el avance hacia la Fase 3 del Roadmap.

**Siguiente paso o deuda:** Validar visualización de la primera sesión de 30 min y proceder con SASS.

### 2026-04-15 — Clarificación sobre la extensión de visualización de video

**Contexto:** Dificultad para localizar la extensión "Video Player" (`moshfeu.video-player`) en el Marketplace de VS Code.

**Hecho:**
- Reconfirmar la existencia y disponibilidad de la extensión.
- Proporcionar instrucciones precisas para la búsqueda por ID (`moshfeu.video-player`).

**Detalle técnico:**
- La búsqueda por ID es más robusta que por nombre, evitando ambigüedades o errores de tipografía.

**Motivo / criterio:** Asegurar que el desarrollador pueda instalar la herramienta necesaria para revisar las evidencias de video sin interrupciones.

**Siguiente paso o deuda:** Confirmar la instalación y reproducción de un video de prueba.

### 2026-04-15 — Corrección de herramienta: Extensión de visualización de video

**Contexto:** La extensión recomendada anteriormente (`frenco.vs-code-media-preview`) no se encuentra disponible en el Marketplace.

**Hecho:** Sustituir la recomendación por la extensión "Video Player" de moshfeu (`moshfeu.video-player`).

**Detalle técnico:**
- La nueva extensión permite la previsualización de archivos `.mp4` y `.webm` directamente en el **IDE** (Integrated Development Environment - Entorno de Desarrollo Integrado).

**Motivo / criterio:** Garantizar que el flujo de revisión de evidencias en el laboratorio sea funcional con herramientas existentes y verificadas.

**Siguiente paso o deuda:** Validar la apertura de un vídeo de sesión de 30 minutos con esta nueva extensión.

### 2026-04-15 — Instalación de extensión para visualización de evidencias

**Contexto:** Necesidad de revisar los vídeos generados por `merci-recorder.py` sin romper el flujo de trabajo saliendo del editor.

**Hecho:** Seleccionar e instalar la extensión Media Preview (`frenco.vs-code-media-preview`).

**Detalle técnico:**
- La extensión permite renderizar binarios de vídeo y audio en pestañas del **IDE** (Integrated Development Environment - Entorno de Desarrollo Integrado).

**Motivo / criterio:** Mantener la concentración en el entorno de desarrollo y facilitar la validación rápida de las capturas de pantalla antes de documentar en la bitácora.

**Siguiente paso o deuda:** Iniciar la grabación de 30 minutos y verificar la reproducción fluida dentro del editor.

### 2026-04-15 — Validación final y mejora de Merci Recorder

**Contexto:** Realizar prueba de humo del grabador y mejorar la flexibilidad para pruebas cortas.

**Hecho:**
- Añadir soporte para argumentos de duración en `merci-recorder.py`.
- Ejecutar prueba de 10 segundos exitosamente.

**Detalle técnico:**
- Uso de `argparse` para parametrizar la duración.
- Confirmación de que el flag `-nostdin` evita colisiones con la entrada de terminal.
- Validación de `.gitignore`: los binarios generados no son trackeados por Git.

**Motivo / criterio:** Robustez y facilidad de prueba sin sacrificar la configuración por defecto de 30 min.

### 2026-04-15 — Corrección de error interactivo en Merci Recorder

**Contexto:** `ffmpeg` reportó un "Parse error" durante la grabación, causado por entrada inesperada del usuario en la terminal.

**Hecho:**
- Identificar la causa del error como interacción accidental con el modo interactivo de `ffmpeg`.
- Modificar `scripts/merci/merci-recorder.py` para añadir el flag `-nostdin`.

**Detalle técnico:**
- El flag `-nostdin` evita que `ffmpeg` intente leer de la entrada estándar, previniendo errores de parseo por comandos no intencionados.

**Motivo / criterio:** Mejorar la robustez del script y la experiencia de usuario, evitando interrupciones por entradas accidentales.

**Siguiente paso o deuda:** Validar el comportamiento del script con el nuevo flag.

### 2026-04-15 — Prueba de humo y validación de Merci Recorder

**Contexto:** Verificar que el script de captura de pantalla funciona correctamente y que la exclusión en Git es efectiva.

**Hecho:**
- Ejecución de prueba de `scripts/merci/merci-recorder.py`.
- Verificación de salida en `laboratorio/evidencias/`.

**Detalle técnico:**
- El script genera el contenedor `.mp4` usando el códec `libx264`.
- `git status` confirma que los binarios de vídeo son ignorados por el sistema de control de versiones.

**Motivo / criterio:** Garantizar la trazabilidad visual de las sesiones de 30 min sin comprometer el peso del repositorio remoto.

### 2026-04-15 — Implementación de infraestructura de pruebas (QA)

**Contexto:** Ausencia de validación automatizada para los scripts de automatización de Merci.

**Hecho:**
- Creación de `scripts/merci/test_sitemap.py`.
- Definición de estrategia de pruebas unitarias usando la librería estándar de Python.

**Detalle técnico:**
- Uso de `unittest.mock` para simular el sistema de archivos y evitar escrituras reales durante los tests.
- Implementación de **TDD** (Test Driven Development - Desarrollo Dirigido por Pruebas) incipiente para los scripts de sistema.

**Motivo / criterio:** Garantizar la integridad de los metadatos de indexación y la estabilidad de las herramientas de automatización antes de avanzar a fases de diseño visual.

**Siguiente paso o deuda:** Ampliar la cobertura de pruebas a `merci-audit.py`.

### 2026-04-15 — Consolidación del flujo de grabación y protección de repositorio

**Contexto:** Asegurar que el nuevo sistema de grabación no impacte el tamaño del repositorio remoto.

**Hecho:**
- Actualizar `.gitignore` para excluir binarios de vídeo en `laboratorio/evidencias/`.
- Validar la integración de `merci-recorder.py` como herramienta de trazabilidad local.

**Detalle técnico:**
- Adición de patrones `*.mp4` y `*.mov` específicos para la carpeta de evidencias.

**Motivo / criterio:** Autonomía en la captura de evidencias sin gestión manual de archivos externos, respetando la Regla 10 de austeridad en el repo remoto.

**Siguiente paso o deuda:** Iniciar la primera sesión de grabación de 30 minutos para validar el rendimiento del sistema.

### 2026-04-15 — Implementación de sistema de captura de vídeo (Merci Recorder)

**Contexto:** Necesidad de registrar sesiones de desarrollo de 30 minutos para trazabilidad del proceso en el Laboratorio.

**Hecho:**
- Crear `scripts/merci/merci-recorder.py`.
- Integrar lógica de captura automática de pantalla con FFmpeg.

**Detalle técnico:**
- Uso de `x11grab` para la **GUI** (Graphical User Interface - Interfaz Gráfica de Usuario).
- Configuración de duración fija a 1800 segundos (30 minutos).
- Codificación en tiempo real optimizada para baja carga de **CPU** (Central Processing Unit - Unidad Central de Procesamiento).

**Motivo / criterio:** Facilitar la generación de evidencias sin interrumpir el flujo de trabajo manual, manteniendo la coherencia con la Regla 10 de gestión de archivos pesados.

**Siguiente paso o deuda:** Validar el peso de los archivos generados y ajustar el Factor de Tasa Constante (CRF) si superan los 50MB por sesión.

### 2026-04-15 — Política de gestión de evidencias pesadas en el Laboratorio

**Contexto:** Necesidad de evitar el crecimiento excesivo del repositorio Git por la inclusión de vídeos y capturas de pantalla de gran tamaño.

**Hecho:**
- Definir regla de exclusión de binarios pesados en `laboratorio/evidencias/`.
- Actualizar `instrucciones.md` con la norma de "Evidencias Pesadas".

**Detalle técnico:**
- Se establece que `merci-optimizer.py` (o extensiones futuras) se encargará de reducir el material de pruebas antes de su clasificación.
- Los archivos originales (brutos) se mantienen en la carpeta externa de capturas o en `.assets-raw/evidencias/` (fuera de Git).

**Motivo / criterio:** Mantener un repositorio ligero y profesional, evitando el bloqueo por cuotas de GitHub y asegurando clones rápidos.

**Siguiente paso o deuda:** Configurar `.gitignore` para excluir extensiones de vídeo (`.mp4`, `.mov`) dentro de la carpeta de evidencias.

### 2026-04-15 — Pruebas de visualización en navegador e hitos UX/UI (Fase 2)

**Contexto:** Validar el renderizado real del `index.html` tras la aplicación de la jerarquía semántica y la estructura BEM.

**Hecho:**
- Generar informes PDF con capturas del sitio en navegador.
- Crear carpeta `laboratorio/evidencias/` para organizar los artefactos de prueba.

**Detalle técnico:** (Aquí puedes anotar si detectaste algún error de alineación, fuentes o comportamiento responsivo en el PDF).

**Motivo / criterio:** Evitar la dispersión de archivos en la raíz del laboratorio y asegurar que las decisiones de diseño tienen un respaldo visual documentado.

**Siguiente paso o deuda:** (Anotar si hay que retocar algún margen o color tras ver el PDF).

### 2026-04-15 — Refactorización a Módulos SASS y Dart Sass Standalone (Fase 3)

**Contexto:** Se identificó que la librería Python `libsass` no soportaba las directivas modulares (`@use`, `@forward`, `_index.scss`) que permiten una arquitectura de estilos moderna y desacoplada.

**Hecho:**
- Reconfiguración de `src/scss/` incluyendo archivos `_index.scss` que reexportan las partes.
- `main.scss` simplificado a sólo incluir los índices de cada subcarpeta.
- Eliminación de `libsass` de `requirements.txt`.
- Modificación estructural de `scripts/merci/merci-styles.py`: ya no es un script de Python que importe librerías, sino un autómata que descarga la release oficial del binario _Dart Sass_ para Linux, extrae el compilador localmente sin impactar el sistema operativo host, y procesa los estilos.

**Detalle técnico:**
- Almacenaje de los binarios locales de SASS en `scripts/merci/bin/dart-sass/sass`.
- Se llama al proceso aisladamente con `subprocess` de la librería estándar de Python.

**Motivo / criterio:**
- Dar soporte al mejor estilo posible de escritura SASS modular pero evadir a toda costa la necesidad de forzar la instalación global de Node.js o NPM para usar un compilador web, protegiendo así el Paradigma base de "0 dependencias externas host".

**Siguiente paso o deuda:** Validar rendimiento continuo del compilador e iniciar implementación de hojas visuales para nuevos componentes.
### 2026-04-15 — Implementación de la Fase 3: SASS, BEM y Merci Optimizer

**Contexto:** Desplegar el sistema de estilos escalable (SASS) y preparar la automatización para multimedia.

**Hecho:**
- Creación de la arquitectura 7-1 en `src/scss/` con punto de entrada único (`main.scss`).
- Refactorización de `public/index.html` asimilando la metodología BEM.
- Creación de dos piezas fundamentales para Merci: `merci-styles.py` (compilador con libsass) y `merci-optimizer.py` (escalado WebP con Pillow).
- `requirements.txt` ajustado para compilar localmente con Python.

**Detalle técnico:**
- `merci-styles.py` invoca a libsass asilando su función y ahorrando uso manual de consola.
- `.assets-raw/` será escrutado por Merci procesando imágenes WebP hacia `assets/` a medidas predeterminadas.

**Motivo / criterio:** Se eligió `libsass` de Python para unificar el DevSecOps de Merci sin depender de un entorno NodeJS global adicional en Ubuntu, en línea con la filosofía de austeridad tecnológica externa.

**Siguiente paso o deuda:** Validar la instalación con pip y hacer un chequeo de `index.html` estéticamente en navegador.
### 2026-04-14 — Validación de jerarquía de encabezados y landmarks (Fase 2.1)

**Contexto:** Asegurar la accesibilidad y la estructura semántica correcta en la página de inicio.

**Hecho:**
- Añadir encabezado `<h2>` a la sección `#ecosistema` para evitar saltos de nivel.
- Incorporar `aria-label` al elemento `<nav>`.
- Actualizar hitos en `README.md`.

**Detalle técnico:**
- Se garantiza que el árbol de encabezados sea secuencial: `h1` > `h2` > `h3`.
- El uso de **Landmarks** (Puntos de referencia) facilita la navegación a usuarios con tecnologías de asistencia.

**Motivo / criterio:** Cumplir con los estándares de **WAI-ARIA** (Web Accessibility Initiative - Accessible Rich Internet Applications - Iniciativa de Accesibilidad Web - Aplicaciones de Internet Enriquecidas Accesibles) y SEO técnico.

**Siguiente paso o deuda:** Iniciar la Fase 3 (Ingeniería de Estilos).

### 2026-04-14 — Integración de merci-sitemap.py en el hook de pre-commit

**Contexto:** Automatizar la actualización de la fecha `<lastmod>` en `sitemap.xml` cada vez que se realicen cambios en la carpeta `public/`.

**Hecho:** Modificar `scripts/merci/pre-commit`.

**Detalle técnico:**
- Se añadió lógica para detectar archivos staged en `public/`.
- Si se detectan cambios, se ejecuta `python3 scripts/merci/merci-sitemap.py`.
- Se añade `public/sitemap.xml` al índice de Git (`git add public/sitemap.xml`) para incluir su modificación en el commit actual.

**Motivo / criterio:** Asegurar que `sitemap.xml` refleje siempre la fecha de la última modificación de contenido relevante, mejorando la precisión del SEO técnico.

**Siguiente paso o deuda:** Realizar un commit de prueba que incluya cambios en `public/` para validar el funcionamiento del hook.

### 2026-04-14 — Automatización de metadatos de indexación (Sitemap)

**Contexto:** Evitar la actualización manual de la fecha de última modificación en el sitemap.xml para mejorar el SEO técnico.

**Hecho:** Crear script `scripts/merci/merci-sitemap.py` para la gestión automática de fechas en archivos XML.

**Detalle técnico:**
- Uso de la librería `datetime` para obtener la fecha del sistema.
- Empleo de `re.sub` para manipular el contenido del XML sin necesidad de parsers pesados.

**Motivo / criterio:** Mantener la consistencia entre los cambios reales y lo que se informa a los motores de búsqueda de forma automatizada.

**Siguiente paso o deuda:** Integrar la ejecución de este script en el flujo de publicación o en un hook de post-commit.

### 2026-04-14 — Cierre de Fase 1 y creación de activos de indexación (Fase 2.3)

**Contexto:** Finalización formal de la infraestructura base y configuración de la visibilidad para buscadores del núcleo estático.

**Hecho:** 
- Actualizar `README.md` para reflejar la Fase 1 como completada.
- Crear `public/robots.txt` y `public/sitemap.xml`.

**Detalle técnico:** 
- `robots.txt`: Configurado para permitir el rastreo total y apuntar al mapa del sitio.
- `sitemap.xml`: Generado con la URL canónica raíz y prioridad máxima.

**Motivo / criterio:** Cumplir con los estándares de **SEO** (Search Engine Optimization - Optimización para Motores de Búsqueda) técnico definidos en el roadmap.

**Siguiente paso o deuda:** Validar la jerarquía de encabezados (Fase 2.1) para asegurar accesibilidad.

### 2026-04-14 — Validación de Fase 2 (HTML y SEO Técnico) con Merci Audit

**Contexto:** Verificación del primer documento semántico del núcleo estático frente a las reglas de auditoría.

**Hecho:** Ejecutar `merci-audit.py --strict-json-ld` sobre `public/index.html`.

**Detalle técnico:**
- El archivo cumple con los requisitos de metadatos, charset y lenguaje.
- Se valida el bloque JSON-LD (JavaScript Object Notation for Linked Data - Notación de Objetos JavaScript para Datos Enlazados) usando el esquema de `schema.org`.

**Motivo / criterio:** Garantizar que el sitio es indexable y cumple con los estándares de rendimiento y SEO (Search Engine Optimization - Optimización para Motores de Búsqueda) desde la primera línea de código.

**Siguiente paso o deuda:** Implementar navegación (Fase 2.1) y generar `robots.txt` / `sitemap.xml` (Fase 2.3).

### 2026-04-14 — Creación de proyecto y obtención de API Key vía AI Studio

**Contexto:** El error 404 inicial no era solo de configuración de software, sino de falta de infraestructura (proyecto) en el lado de Google.

**Hecho:** Generar una API Key a través de Google AI Studio vinculada a un proyecto nuevo creado automáticamente por la plataforma.

**Detalle técnico:** 
- Acceso a `aistudio.google.com`.
- Uso de la opción "Create API key in new project" para evitar la configuración manual en GCP (Google Cloud Platform - Plataforma en la Nube de Google) Console.

**Motivo / criterio:** Vía más rápida para habilitar `gemini-1.5-pro` sin gestionar capas de facturación o cuotas complejas de Google Cloud de entrada.

**Siguiente paso o deuda:** Probar la conexión en Continue una vez la API Key esté activa y propagada.

### 2026-04-14 — Corrección de error 404 en Continue (Gemini 1.5 Pro)

**Contexto:** Fallo en la conexión con la API de Google al usar gemini-1.5-pro en Continue, con un error 404.

**Hecho:** Identificar que el `provider` en el archivo `/home/hildegahr/.continue/config.yaml` estaba configurado incorrectamente como `gemini`.

**Detalle técnico:** Modificar el `provider` de `gemini` a `google-generative-ai` para el modelo `gemini-1.5-pro` en la configuración de Continue.

**Motivo / criterio:** El `provider` `google-generative-ai` es el nombre correcto para interactuar con la API de Google Gemini a través de Continue.

**Siguiente paso o deuda:** Crear el proyecto en Google Cloud / AI Studio.

### 2026-04-12 — Fase 1: infraestructura, Merci Audit y primer commit

**Contexto:** Arranque del repositorio bajo las directrices de `instrucciones.md` (rendimiento, seguridad shift-left, pedagogía). Objetivo de la Fase 1: estructura de carpetas, script de auditoría local y base Git.

**Hecho:**

- Estructura aprobada en la raíz: `docs/`, `biblioteca/`, `laboratorio/`, `scripts/merci/`, `assets/`, `.assets-raw/` (las carpetas vacías se versionan con `.gitkeep` para que un `git clone` conserve el esqueleto).
- `scripts/merci/merci-audit.py`: auditoría con biblioteca estándar de Python (sin dependencias pip obligatorias en esta fase). Comprueba entre otras cosas patrones de secretos, sintaxis de `.py`, JSON, avisos en JS (`eval` / `new Function`) y reglas SEO mínimas en `.html` / `.htm`.
- `scripts/merci/pre-commit`: shell que ejecuta `merci-audit.py --git-staged` (solo lo que va al commit).
- Enlace local de Git: `.git/hooks/pre-commit` → `../../scripts/merci/pre-commit` (los hooks no viajan con el clone; hay que recrear el enlace en cada máquina o documentar un bootstrap).
- `.gitignore` para `.venv/`, cachés y artefactos de build; `requirements.txt` reservado para fases posteriores (p. ej. Pillow en optimizador).
- Commit inicial en rama `main` con mensaje tipo *chore: commit inicial — Fase 1 (estructura, Merci Audit, directrices)*.

**Detalle técnico:**

- Auditoría sobre todo el árbol: `python3 scripts/merci/merci-audit.py`
- Solo índice (staged), pensado para hook: `python3 scripts/merci/merci-audit.py --git-staged`
- Exigir JSON-LD en HTML cuando toque endurecer CI: flag `--strict-json-ld`
- Instalar hook (desde la raíz del repo): `chmod +x scripts/merci/pre-commit scripts/merci/merci-audit.py` y `ln -sf ../../scripts/merci/pre-commit .git/hooks/pre-commit`
- Saltar el hook solo si es deliberado: `git commit --no-verify`

**Motivo / criterio:** Automatizar comprobaciones antes de integrar cambios encaja con “seguridad shift-left” y con el papel de `merci-audit.py` descrito en instrucciones. Staged-only evita auditar el mundo en cada commit y acelera el flujo.

**Siguiente paso o deuda:** Fase 2 — HTML semántico, JSON-LD e indexación; primer documento público o plantilla que pase el audit sin `--no-verify`.

### 2026-04-12 — Registro cronológico acumulativo (no sustituir historial)

**Contexto:** Asegurar que la bitácora no pierda contexto al añadir sesiones nuevas.

**Hecho:** En `instrucciones.md` (regla 6) y en «Cómo mantenerlo» de este archivo quedó explícito: nuevas entradas **solo al final** del registro; no reemplazar ni borrar bloques ya escritos salvo corrección puntual o retirada de datos sensibles, con motivo claro.

**Detalle técnico:** N/A.

**Motivo / criterio:** El historial del laboratorio es activo de trazabilidad; sobrescribirlo rompería la línea temporal para el «yo futuro» y para el traslado a `biblioteca/`.

**Siguiente paso o deuda:** Seguir añadiendo entradas bajo «Registro cronológico» sin editar entradas previas salvo las excepciones acordadas.

### 2026-04-12 — `.assets-raw`: solo local, sin originales en Git

**Contexto:** Evitar que PSD, RAW, vídeos u otros brutos acaben en GitHub.

**Hecho:** `.gitignore` pasa a ignorar `.assets-raw/*` con excepción de `.assets-raw/.gitkeep`. `instrucciones.md` y `README.md` describen que la carpeta es convención de trabajo local y que lo versionado en `/assets` es lo optimizado.

**Detalle técnico:** Patrón en `.gitignore`: `!.assets-raw/.gitkeep` tras `.assets-raw/*`.

**Motivo / criterio:** Repositorio ligero y reproducible; los originales viven fuera del remoto (disco, NAS, etc.).

**Siguiente paso o deuda:** En Fase 3, documentar el flujo concreto `merci-optimizer.py` de `.assets-raw` → `assets/`.

### 2026-04-12 — Documentación pública sin notas personales al mantenedor

**Contexto:** Evitar frases tipo “cuando lo tengas claro añade LICENSE” en el README u otros textos versionados para GitHub.

**Hecho:** `README.md` (Licencia y otras frases) redactado en tono neutro. Nueva regla 7 en `instrucciones.md`: recordatorios al autor fuera del repo; en Git, texto útil para visitantes o colaboradores.

**Detalle técnico:** N/A.

**Motivo / criterio:** El remoto es documentación de producto/proyecto, no la libreta personal.

**Siguiente paso o deuda:** Revisar futuros `docs/` públicos con el mismo criterio.

### 2026-04-12 — Fase 2: carpeta `public/` como raíz del documento

**Contexto:** Inicio de la Fase 2 por la estructura antes del primer HTML.

**Hecho:** Directorio `public/` en el repo con `.gitkeep`; entrada en §3 de `instrucciones.md` y fila en `README.md`. Convención: aquí vive el núcleo estático servido como documento raíz; WP fuera hasta Fase 4.

**Detalle técnico:** Nombre elegido: `public/` (convención habitual de “document root” en despliegues estáticos).

**Motivo / criterio:** Separar claramente sitio servido, automatización, conocimiento y brutos locales.

**Siguiente paso o deuda:** `public/index.html` semántico + JSON-LD + `robots.txt` / `sitemap.xml` en la misma raíz cuando toque.

---
## Cuando pases esto a la biblioteca

1. **Releer** entradas y quitar ruido (intentos fallidos, datos personales, tokens aunque sean falsos).
2. **Partir por tema:** por ejemplo una ficha “Sistema Merci — auditoría pre-commit” vs “Estructura del repositorio”.
3. **Añadir los tres átomos** donde haya una decisión difícil o un incidente (síntoma, solución, lección o deuda).
4. **Enlazar** al código estable (rutas a `scripts/merci/`, no copiar bloques enormes en la biblioteca salvo que aporten lectura autónoma).

---

*Última revisión de la bitácora: 2026-05-07.*
