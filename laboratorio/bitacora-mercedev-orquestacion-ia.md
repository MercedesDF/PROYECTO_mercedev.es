# Bitácora del proyecto mercedev.es - fase orquestación con ia

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

### 2026-05-07 — UI: Leyenda descriptiva para el Dashboard de Métricas

**Contexto:** El "Engineering Dashboard" de la portada con las 10 métricas carecía de contexto sobre el origen y la valoración de los números presentados, dificultando la comprensión para usuarios menos técnicos.

**Hecho:** 
- Se inyectó el bloque `<p class="hero__dashboard-legend">` en `public/index.html`.
- Se añadieron las reglas CSS `.hero__dashboard-legend` en `src/scss/components/_hero.scss`.

**Motivo / criterio:** *Accesibilidad Cognitiva y Autoridad*. Explicar de dónde vienen los datos (auditoría real de Google PageSpeed) y qué significan (rango de excelencia / 100 sobre 100) contextualiza las métricas puras, transformando números fríos en un argumento de venta de autoridad técnica verificable.

**Siguiente paso o deuda:** Recompilar el CSS, ejecutar `merci total` y comenzar la Fase 1 de IA.

### 2026-05-07 — Feat: Ampliación de métricas extraídas de PageSpeed (FCP y SI)

**Contexto:** El script de extracción leía 4 métricas (LCP, INP, CLS, TBT), pero el reporte de PageSpeed incluye otras relevantes como First Contentful Paint (FCP) y Speed Index (SI). Se solicitó incluirlas todas en el Dashboard de la portada.

**Hecho:**
- Se inyectaron los patrones Regex bidireccionales para FCP y SI en `laboratorio/scripts_temporales/merci-extract-metrics.py`.
- Se añadieron los bloques HTML para las nuevas métricas en `public/index.html`.
- Se refactorizó la rejilla CSS en `src/scss/components/_hero.scss` de 4 a 5 columnas para alojar perfectamente las 10 métricas totales en dos filas.

**Motivo / criterio:** *Data Completeness y UI Responsiva*. Ignorar datos disponibles en un reporte validado limita la observabilidad. Adaptar la cuadrícula SASS demuestra la flexibilidad de la arquitectura modular: ampliar el dashboard de 8 a 10 métricas cuesta solo un dígito de CSS.

**Siguiente paso o deuda:** Recompilar el CSS, ejecutar `merci total` y arrancar la Fase 1 de IA.

### 2026-05-06 — QA: Intercepción de enlace roto en capa dinámica (Menú Art de Coté)

**Contexto:** El orquestador `merci total` detuvo el pipeline en la fase de rastreo dinámico (`merci-linkcheck.py`) tras detectar un error 404 hacia `/blog/category/art-de-cote/` originado en `/blog/`.

**Hecho:** Se diagnosticó que las plantillas monolíticas de WordPress (`index.php` y `woocommerce.php`) conservaban la ruta antigua en su bloque `<nav>` *hardcodeado*. Se actualizó manualmente el enlace hacia la nueva ruta estática `/art-de-cote/`.

**Motivo / criterio:** *Fail-Fast y DAST*. El escáner de enlaces demuestra su inmenso valor bloqueando el despliegue al detectar asimetrías de enrutamiento entre el núcleo SSG y el CMS. Las plantillas PHP no son procesadas por `merci-sync-pages.py`, exigiendo intervención explícita del autor para mantener la paridad visual.

**Siguiente paso o deuda:** Validar la corrección ejecutando `merci total` y comenzar la Fase 1 del Roadmap de IA.

### 2026-05-06 — Arch: Independencia absoluta de Art de Coté (Opción B)

**Contexto:** Tras decidir migrar Art de Coté al motor estático (SSG), existían dos rutas: subsumirlo en la Biblioteca como una estantería más o darle entidad propia como índice independiente.

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
