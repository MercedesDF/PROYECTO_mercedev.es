# Bitácora del proyecto mercedev.es — Épica 4: Estabilización y Rendimiento Extremo

## Para qué sirve este archivo

Bitácora activa a partir de la finalización de la Épica 3 (DevRel & Observabilidad Avanzada).
Registra exclusivamente las decisiones, experimentos y aprendizajes de la Épica 4 (Estabilización y Rendimiento Extremo) documentada en el `ROADMAP.md` maestro.

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

### 2026-05-22 — Perf: Despriorización de red (Fetch Priority) del logo para salvar el LCP

**Contexto:** Tras las últimas optimizaciones, la puntuación de Lighthouse en móvil 4G cayó a 97/100. El análisis forense del JSON de PageSpeed/Catchpoint reveló que el `logo.webp` (marcado con `fetchpriority="high"`) estaba robando ancho de banda al archivo `main.css`, retrasando el pintado general de la pantalla.

**Hecho:**
- Se reemplazó el atributo `fetchpriority="high"` por `fetchpriority="low"` en el `logo.webp` dentro de `public/index.html` y `src/wp-theme/merci-theme/index.php` (igualando la técnica usada en el avatar de Merci).

**Motivo / criterio:** *Data-Driven Performance*. Se asumía erróneamente que el logotipo era el LCP (Largest Contentful Paint). El reporte JSON demostró que el titular `<h2>` ocupa un área de pantalla mayor (27.904px vs 17.095px), siendo el verdadero LCP. Bajar la prioridad de descarga del logo cede el ancho de banda al CSS crítico, acelerando el renderizado del texto y restaurando el 100/100.

**Siguiente paso o deuda:** Desplegar, validar el 100/100 definitivo y transicionar a la Épica 5 (Showcase).

### 2026-05-22 — Milestone: Validación 100/100 y Cierre de Fase 1 (Épica 4)

**Contexto:** Tras aplicar el yielding en JS y la decodificación asíncrona de imágenes, se requería validar empíricamente la estabilización del Total Blocking Time (TBT) bajo estrangulamiento móvil estricto (Catchpoint / PageSpeed).

**Hecho:**
- Se ejecutaron auditorías externas confirmando TBT 0ms y un cuádruple 100/100 estable en todas las vistas (Mobile 4G, Mobile Potente, Escritorio).
- Se marcaron los hitos de la Fase 1 como completados en el `ROADMAP.md`.

**Motivo / criterio:** *Performance Driven Development*. La eliminación del "Efecto Acantilado" del Garbage Collector garantiza una base predecible e inquebrantable antes de integrar la compleja lógica de WooCommerce (E-commerce Extremo).

**Siguiente paso o deuda:** Iniciar la transición hacia la Épica 5 (Showcase y Distribución del Boilerplate).

### 2026-05-22 — Fix: Prevención de Falsos Positivos en Orquestador de Despliegue

**Contexto:** Al abortar la creación de un commit manual, el script salía silenciosamente con código 0. Esto engañaba al orquestador supremo (`merci-completo.py`), que continuaba ciegamente con el despliegue a producción.

**Hecho:** 
- Se modificó `scripts/merci/merci-commit.py` para devolver `sys.exit(1)` al cancelar la operación.

**Motivo / criterio:** *Fail-Fast y Data Integrity*. Una cancelación de usuario es una interrupción intencionada de la cadena de suministro. Emitir un código de error activa los mecanismos de seguridad del orquestador padre, colapsando el pipeline y evitando operaciones de red y caché innecesarias o despliegues fantasmas.

**Siguiente paso o deuda:** Validar la estabilidad del TBT a 0ms en producción (Completado).

### 2026-05-22 — Perf: Fragmentación de tareas JS (Yielding) en hilo principal

**Contexto:** La inicialización del asistente Merci y la descarga/parseo de su "cerebro" JSON ocurrían de forma síncrona durante la carga inicial de la página, compitiendo por CPU con el dibujado inicial y provocando picos de TBT bajo simulación móvil lenta debido al recolector de basura (Garbage Collector).

**Hecho:** 
- Se refactorizó la instanciación de `MerciController` en `public/js/main.js` envolviéndola en `requestIdleCallback` (con `setTimeout` como fallback para Safari).
- Se inyectó una promesa de yielding (`await new Promise(resolve => setTimeout(resolve, 0));`) en `_connectBrain()` de `MerciController.js` tras el parseo del JSON.
- Se marcó la tarea como completada en el Roadmap de la Épica 4.

**Motivo / criterio:** *Performance Driven Development*. El asistente Merci es un *Progressive Enhancement* (mejora progresiva), no es crítico para el primer renderizado (LCP) ni para la navegación principal. Retrasar intencionadamente su carga (Yielding) protege el presupuesto de rendimiento del hilo principal (Main Thread), fraccionando la ejecución para que ninguna tarea individual supere los 50ms.

**Siguiente paso o deuda:** Desplegar los cambios y ejecutar auditorías continuas para validar la estabilidad absoluta del TBT a 0ms en PageSpeed Insights.

### 2026-05-22 — Arch: Creación de Épica 4 (Performance Extremo) y reestructuración del Roadmap

**Contexto:** El TBT de la versión móvil sufría fluctuaciones (efecto "acantilado" entre 0ms y 548ms) debido a la intervención del Garbage Collector en tareas JavaScript que rozaban el límite de 50ms del hilo principal. Se debatió si abordar la optimización antes o después de la integración del e-commerce.

**Hecho:**
- Se inauguró la Épica 4 centrada exclusivamente en estabilizar el TBT a 0ms en todos los entornos (Móvil 4G, Móvil Potente y Escritorio).
- Se desplazaron las épicas de *Showcase* (ahora Épica 5) y *E-commerce* (ahora Épica 6) en el `ROADMAP.md`.
- Se añadió la deuda técnica de integrar el e-commerce en el orquestador `merci-completo.py`.

**Motivo / criterio:** *Performance First*. Introducir la complejidad de un E-commerce (WooCommerce y pasarelas de pago) sobre una base de rendimiento inestable empujaría las tareas del hilo principal irremediablemente por encima de los 50ms. Garantizar un 100/100 robusto y predecible en simulación Mobile-First es un prerrequisito innegociable antes de añadir lógica de terceros o exhibir el Boilerplate.

**Siguiente paso o deuda:** Implementar fragmentación de tareas (Yielding) en `MerciController.js` y `main.js`, y delegar la decodificación de imágenes mediante atributos asíncronos en el HTML.