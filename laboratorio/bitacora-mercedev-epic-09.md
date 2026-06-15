# Bitácora del proyecto mercedev.es — Épica 9: Antigravity SRE, Chaos Engineering & Refinamiento CSS

## Para qué sirve este archivo
Bitácora activa para registrar las decisiones, arquitectura y evolución técnica correspondientes a la Épica 9 del Roadmap maestro (Antigravity SRE, Chaos Engineering Avanzado y Refinamiento CSS).

---

## Registro cronológico

### 2026-06-15 — Investigación: Preservación de Herramientas Estériles (FFmpeg)

**Contexto (Desafío):**
Se necesitaba automatizar la purga de tiempos muertos ("congelación de terminal") en los vídeos de demostración del proyecto (showcase). Se experimentó con la vía de bajo nivel usando `FFmpeg` y el filtro `mpdecimate`.

**Hecho (Maniobra):**
- Se generó el script `scripts/temporales/merci-mpdecimate-fastforward.sh`.
- El script cumplió técnicamente su función de compresión extrema (de 272MB a 62MB), pero generó un efecto "Hyper-Timelapse" epiléptico inasumible para la visualización humana.
- Se experimentó alternativamente con `auto-editor` (Python) para recortar fotogramas inactivos manteniendo un "padding" humano (`--margin 0.5s`), pero el intento falló debido a la falta de metadatos de fotogramas constantes (`time_base=0/0`, VFR) en la grabación de pantalla cruda.
- En lugar de desechar el código, se confinó en el nuevo directorio `scripts/temporales/` y se documentó explícitamente en su cabecera el motivo de su fracaso y las alternativas humanas recomendadas (CapCut, auto-editor), cumpliendo las normas de gobernanza.

**Motivo / criterio (Aprendizaje):**
Un script fracasado es una lección arquitectónica valiosa. Mantener el ecosistema Zero-Bloat también implica no saturar la carpeta principal de `scripts/` con utilidades estériles, derivándolas a un silo de cuarentena/histórico debidamente comentado.

### 2026-06-15 — Fase 2: Implementación de Telemetría SRE (Anti-Bloat) y Gobernanza

**Contexto (Desafío):**
Se requería vigilar activamente que el crecimiento del ecosistema no rompa la filosofía "Zero-Bloat". Además, se detectó un truncamiento accidental en el archivo que dicta el perfil operativo de la IA (`.privado/gemini.md`).

**Hecho (Maniobra):**
- Se reconstruyó en su totalidad el archivo `gemini.md` y se promocionó a la base de conocimiento oficial (KI) del IDE Antigravity.
- Se inyectó en `scripts/merci/merci-sre.py` el nuevo Gauge `merci_public_folder_size_mb` y una función recursiva para auditar el tamaño de la carpeta estática.
- Se inyectó programáticamente en `observabilidad/dashboards/merci-dashboard.json` el panel visual "Peso Estático (/public)".
- *Hotfix (Grafana Schema):* Se corrigió una infracción de esquema en el JSON del Dashboard. La API de Grafana v13.0 descartaba silenciosamente el panel porque la propiedad `element` esperaba un objeto `{"kind": "ElementReference", "name": "panel-26"}` y no un *String* plano.

**Motivo / criterio (Aprendizaje):**
Monitorear físicamente el peso del ecosistema permite anticipar la deuda técnica y degradaciones en Core Web Vitals antes de que sucedan. Reparar las reglas de la IA asegura el rigor arquitectónico a futuro.

### 2026-06-15 — Fase 2: Expansión de Telemetría SRE (Accesibilidad & URL Granular)

**Contexto (Desafío):**
Se necesitaba ampliar la telemetría SRE para incorporar la deuda técnica de accesibilidad (cuantificando problemas de contraste de color y ARIA) en Grafana, así como inyectar micro-sellos visuales Zero-JS con las puntuaciones reales de Lighthouse en las 7 páginas principales del ecosistema, evitando degradar la velocidad del pipeline local.

**Hecho (Maniobra):**
- Se diseñó el componente visual `sre-badge` con estilos CSS/SASS glassmorphic y se registró en `src/scss/components/_sre-badge.scss`.
- Se configuró el extractor para solicitar todos los ámbitos de Lighthouse a la API de PageSpeed e implementó la cuantificación detallada de errores de contraste y ARIA en `merci-extract-metrics.py`.
- Se implementó la resolución y caché paralela (`ThreadPoolExecutor`) de las 7 páginas principales del sitio en `observabilidad/.lighthouse_pages_cache.json` con un TTL de 24 horas.
- Se inyectaron dinámicamente los micro-sellos en las portadas e índices compilados mediante `merci-publish.py` e inyectó los badges en archivos estáticos mediante `merci-sync-pages.py` con marcadores `<!-- Merci SRE Badge -->`.
- Se añadieron los Gauges `merci_lighthouse_accessibility_contrast_errors` y `merci_lighthouse_accessibility_aria_errors` en el agente `merci-sre.py` y se crearon los paneles 27 y 28 en el dashboard JSON de Grafana.
- Se actualizaron el ROADMAP, el Walkthrough y el listado de tareas del proyecto.

**Motivo / criterio (Aprendizaje):**
La ejecución concurrente multihilo minimiza el tiempo de red a un único ciclo de llamadas API (~12s) que solo se activa al expirar la caché de 24h. Mantener los badges libres de Javascript preserva el rendimiento óptimo del frontend, garantizando el 100/100 Core Web Vitals en producción.

## Notas Arquitectónicas

*(Espacio para documentar bloqueos o decisiones técnicas durante la ejecución de la épica).*
