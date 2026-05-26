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

### 2026-05-26 — Fix/DX: Restauración de nomenclatura semántica en orquestador de Release

**Contexto:** Se detectó que `merci-release.py` utilizaba el prefijo `chore: release vX.X.X` al realizar el commit automático en el Boilerplate, rompiendo la convención histórica del proyecto (`feat: release "vX.X.X"`).

**Hecho:** Se parcheó `scripts/merci/merci-release.py` para restituir el formato exacto del mensaje de commit con prefijo `feat:` y la versión entrecomillada.

**Motivo / criterio:** *Consistency*. Las convenciones de nomenclatura en Git son vitales para la legibilidad del historial. Aunque `chore` es un estándar aceptado para empaquetados, respetar la convención histórica del proyecto evita disonancia cognitiva al auditar los repositorios derivados.

### 2026-05-26 — Docs: Resolución de Deriva Documental y Release v1.16.1

**Contexto:** Tras finalizar la Épica 6 (E-commerce Híbrido), se detectó que los documentos fundacionales (`flujo-publicacion-sop.md`, `checklist-hardening.md`, `integracion-wordpress.md`) no habían sido actualizados con los nuevos protocolos de publicación de la tienda y las barreras de seguridad (Hardening) implementadas contra WooCommerce.

**Hecho:** Se actualizaron los manuales maestros inyectando el "Flujo 3: Tienda", los escudos contra telemetría/inyecciones en línea y la arquitectura Zero-JS. Se empaquetó la versión `v1.16.1` en `README-merci.md`.

**Motivo / criterio:** *Zero Document Drift y Release Management*. Dado que la carpeta `docs/` se exporta íntegramente al `merci-boilerplate`, actualizar la matriz exige lanzar una nueva versión de parche (Patch Release) para que los proyectos derivados nazcan con las instrucciones de seguridad y operativas precisas, respetando la Regla 14.

**Siguiente paso o deuda:** Exportar el Boilerplate (`merci release`) y continuar con el diseño de la Paleta Premium en la Épica 7.

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