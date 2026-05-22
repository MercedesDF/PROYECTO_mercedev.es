---
titulo: "Compendio Estratégico: Épica 4 - Rendimiento Extremo y Estabilización"
fecha: "2026-05-22"
tema: "DevSecOps y Gobernanza"
estado: "incubacion"
---

**Contexto:** El proyecto padecía una fuerte inestabilidad en la métrica TBT (Total Blocking Time) bajo emulación móvil estricta (4G CPU Throttling). La fluctuación aleatoria destruía la fiabilidad de las auditorías.

**Maniobras Arquitectónicas:**
1. **Yielding en JS (Shift-Left Performance):** Fragmentamos la inicialización asíncrona en `main.js` (`requestIdleCallback`) y `MerciController.js` (Promesas `setTimeout`) para ceder el paso al hilo principal, evadiendo los bloqueos del Garbage Collector de V8.
2. **Inversión de Prioridad LCP:** Mediante análisis empírico de red, descubrimos que el verdadero LCP era el titular `<h2>` y no el logotipo. Retiramos `fetchpriority="high"` del logo y aplicamos `decoding="async"`, liberando ancho de banda masivo para el CSS crítico.
3. **Fail-Fast en Orquestación:** Endurecimos el script `merci-commit.py` para devolver códigos de salida fatales (`sys.exit(1)`) en cancelaciones, bloqueando despliegues "fantasma" en el orquestador maestro.

**Aprendizaje / Deuda Técnica:**
El rendimiento extremo a nivel 100/100 exige abandonar las suposiciones teóricas (como creer que la imagen más grande es siempre el LCP) y abrazar el empirismo de los JSON de PageSpeed. Este chasis blindado a 0ms de TBT constante es el cimiento obligatorio y no-negociable antes de inyectar arquitecturas pesadas (como pasarelas de pago de WooCommerce en futuras épicas).

<!-- linkedin: 🚀 ¿Atrapado en el infierno del TBT aleatorio en PageSpeed? Te cuento cómo domamos el Garbage Collector de V8 y descubrimos que el LCP no siempre es tu imagen más grande. Lee el postmortem de nuestra Épica 4 de rendimiento extremo. -->