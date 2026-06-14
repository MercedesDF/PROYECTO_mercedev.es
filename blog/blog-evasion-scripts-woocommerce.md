---
titulo: "Domando a WooCommerce: Evasión de Hooks y Rastreo Fantasma"
descripcion: "Cómo neutralizar la inyección tardía de scripts de rastreo y evitar el colapso del TTFB en arquitecturas Zero-JS."
estado: "publicado"
estado_social: "aprobado"
subtema: "Blog"
fase: "Epic 6 - Fase 1"
fecha: "2026-05-26"
---
<!-- linkedin:
En el núcleo estático de mercedev.es, se enfrentó un desafío crítico en la optimización de una tienda híbrida, donde WooCommerce y su característica de rastreo condicional causaban un TTFB de 1000ms. Para resolver este problema, se implementaron estrategias que lograron reducir significativamente el tiempo de carga del servidor.
Para proteger la arquitectura del framework, es crucial entender y dominar la lógica subyacente de los CMS como WooCommerce. La verdadera solución a estos desafíos no radica en soluciones superficiales, sino en interceptar directamente las consultas a la base de datos, garantizando así un rendimiento optimizado.
#DevSecOps #DesarrolloWeb #mercedev.es -->
La optimización extrema de una tienda híbrida requiere un enfoque meticuloso, y durante este proceso, se descubrió que WooCommerce estaba causando problemas significativos. El Tiempo hasta el Primer Byte (TTFB) superaba los 1000ms, lo que afectaba la experiencia del usuario y colapsaba el rendimiento. Además, el script de rastreo (`sourcebuster.min.js`) persistía con un Tiempo de Bloqueo Total (TBT) de ~320ms.

El enigma estaba en la evasión del hook estándar para desregistrar el script. WooCommerce 8.5+ inyectaba el rastreo de forma condicional y tardía, lo que dificultaba su eliminación en el frontend. Para superar este obstáculo, se implementaron estrategias innovadoras.

Primero, se extirpó una rutina de auto-sanación de bloques que colgaba del hook `init`. Esta tarea era esencial para reducir la latencia inicial, pero escanear la base de datos en cada petición HTTP causaba un TTFB extremadamente alto. Se decidió eliminar esta funcionalidad para optimizar el rendimiento.

A continuación, se implementaron filtros que desactivaban directamente la característica de rastreo de WooCommerce. Se utilizaron los hooks `woocommerce_order_attribution_tracking_enabled` y `pre_option_woocommerce_order_attribution_tracking_enabled`, retornando valores que evitaban la ejecución del script. Además, se elevó la prioridad de las funciones de desregistro a `999`, asegurando que estas modificaciones prevalecieran sobre cualquier otra configuración.

### 💡 En resumen:
La solución no radica en soluciones superficiales o intentos de cazar el script en el frontend. La verdadera ingeniería de rendimiento requiere conocer la arquitectura subyacente y tomar medidas directas para interceptar consultas a la base de datos. Al eliminar la característica de rastreo de WooCommerce directamente, se logró reducir significativamente el TTFB y garantizar un rendimiento óptimo.

Para aprender más sobre esta solución detallada, puedes leer el cuadernillo completo [aquí](/biblioteca/domando-a-woocommerce-evasion-de-hooks-y-rastreo-fantasma.html).