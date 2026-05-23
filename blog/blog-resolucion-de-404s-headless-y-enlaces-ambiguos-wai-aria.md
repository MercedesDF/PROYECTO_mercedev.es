---
titulo: "Resolución de 404s Headless y Enlaces Ambiguos WAI-ARIA"
descripción: "Cómo erradicar enlaces rotos en PDFs mediante un patrón de publicación en dos pasos y prevenir colisiones de accesibilidad WCAG inyectando dimensión temporal."
estado: "publicado"
estado_social: "aprobado"
tema: "Blog"
fase: "Epic 3 - Fase 2"
fecha: "2026-05-19"
descripcion: "Cómo erradicar enlaces rotos en PDFs mediante un patrón de publicación en dos pasos y prevenir colisiones de accesibilidad WCAG inyectando dimensión temporal."
---
<!-- linkedin:
Durante la auditoría del pipeline de publicación automatizada de mercedev.es, el rastreador local 'merci-linkcheck.py' detectó descargas "zombi" y colisiones severas de accesibilidad en los lectores de pantalla debido a enlaces ambiguos.

Para erradicar estos falsos positivos y mantener un 100/100 estricto en WAI-ARIA, se ha implementado un patrón de publicación en dos pasos (Post -> PDF -> Update).

Adicionalmente, se ha inyectado dimensión temporal en los aria-labels, resolviendo la ambigüedad en artículos homónimos y ofreciendo contexto exacto a las tecnologías asistivas.

En resumen: el sistema ahora verifica que el PDF exista físicamente antes de crear el botón de descarga, evitando los enlaces rotos. Además, se ha incorporado la fecha de publicación de forma "invisible" en los botones para que las personas que usan lectores de pantalla puedan diferenciar fácilmente dos artículos que compartan el mismo título.

#DevSecOps #Accesibilidad #WebPerformance #ArquitecturaHeadless#mercedev.es
-->

Durante las auditorías de rendimiento continuo en producción, el rastreador local (`merci-linkcheck.py`) bloqueó el pipeline al detectar una doble vulnerabilidad funcional: enlaces de descarga que apuntaban a PDFs fantasma (404) y una infracción severa de accesibilidad (WAI-ARIA) provocada por la existencia de atributos idénticos en enlaces que apuntaban a artículos distintos con el mismo título.

En una arquitectura Headless, confiar ciegamente en que el CMS "generará por defecto" el archivo estático es un antipatrón de diseño. 

Para resolver esta fricción, se arremetió contra el flujo de publicación implementando un patrón de dos pasos en el orquestador (`merci-wp.py`).

Ahora, el sistema publica primero la entrada, compila el PDF de forma local, y únicamente si la generación física tiene éxito, realiza una segunda actualización inyectando la descarga.

Paralelamente, inyectar una dimensión temporal (la fecha) en los atributos WAI-ARIA erradicó por completo las colisiones para los lectores de pantalla sin alterar la interfaz visual en lo más mínimo.

### 💡 En resumen:

En lugar de dar por hecho que un archivo PDF de descarga siempre estará disponible (lo que a menudo provoca que el usuario pinche en un enlace "roto" que no hace nada), el sistema ahora verifica primero su existencia física en el servidor y solo crea el botón de descarga si el archivo es real.

Además, se ha añadido la fecha "invisible" a los nombres internos de los artículos para que las personas que usan lectores de pantalla no se confundan cuando haya dos textos distintos que se llamen igual.

Tienes disponible el cuadernillo técnico detallando el código y la arquitectura de esta maniobra en la estantería de DevSecOps: [Resolución de 404s Headless y Enlaces Ambiguos WAI-ARIA](/biblioteca/resolucion-de-404s-headless-y-enlaces-ambiguos-wai-aria.html).