---
titulo: "Resolución de 404s Headless y Enlaces Ambiguos WAI-ARIA"
descripción: "Cómo erradicar enlaces rotos en PDFs mediante un patrón de publicación en dos pasos y prevenir colisiones de accesibilidad WCAG inyectando dimensión temporal."
estado: "publicado"
estado_social: "aprobado"
tema: "Varios"
subtema: "Blog"
fase: "Epic 3 - Fase 2"
fecha: "2026-05-19"
descripcion: "Cómo erradicar enlaces rotos en PDFs mediante un patrón de publicación en dos pasos y prevenir colisiones de accesibilidad WCAG inyectando dimensión temporal."
---
<!-- linkedin:
Durante la auditoría del pipeline de publicación automatizada de mercedev.es, el rastreador local 'merci-linkcheck.py' detectó descargas "zombi" y colisiones severas de accesibilidad en los lectores de pantalla debido a enlaces ambiguos.

Para erradicar estos falsos positivos, se aplicó la regla de oro del minimalismo: amputar la característica. Los PDFs dinámicos fueron eliminados del blog en favor de un enfoque 100% ultraligero.

Adicionalmente, se ha inyectado dimensión temporal en los aria-labels, resolviendo la ambigüedad en artículos homónimos y ofreciendo contexto exacto a las tecnologías asistivas.

En resumen: en lugar de intentar arreglar los botones de descarga de PDFs en el blog, se eliminaron por completo por ser innecesarios. Además, se ha incorporado la fecha de publicación de forma "invisible" en los botones para que las personas que usan lectores de pantalla puedan diferenciar fácilmente dos artículos que compartan el mismo título.

#DevSecOps #Accesibilidad #WebPerformance #ArquitecturaHeadless#mercedev.es
-->

Durante las auditorías de rendimiento continuo en producción, el rastreador local (`merci-linkcheck.py`) bloqueó el pipeline al detectar una doble vulnerabilidad funcional: enlaces de descarga que apuntaban a PDFs fantasma (404) y una infracción severa de accesibilidad (WAI-ARIA) provocada por la existencia de atributos idénticos en enlaces que apuntaban a artículos distintos con el mismo título.

En una arquitectura Headless, confiar ciegamente en que el CMS "generará por defecto" el archivo estático es un antipatrón de diseño. 

Para resolver esta fricción, se tomó la decisión más sana a nivel arquitectónico: extirpar la funcionalidad. Se amputó la generación de PDFs dinámicos en el orquestador (`merci-wp.py`). El blog es un flujo rápido y efímero; no necesita la pesada carga de renderizar documentos offline. Si alguien quiere un PDF inmutable, acudirá a la Biblioteca estática.

Paralelamente, inyectar una dimensión temporal (la fecha) en los atributos WAI-ARIA erradicó por completo las colisiones para los lectores de pantalla sin alterar la interfaz visual en lo más mínimo.

### 💡 En resumen:

En lugar de intentar arreglar los botones de descarga rotos en las noticias del blog, nos dimos cuenta de que era una función innecesaria y los eliminamos completamente, haciendo la web más ligera y libre de errores.

Además, se ha añadido la fecha "invisible" a los nombres internos de los artículos para que las personas que usan lectores de pantalla no se confundan cuando haya dos textos distintos que se llamen igual.

Tienes disponible el cuadernillo técnico detallando el código y la arquitectura de esta maniobra en la estantería de DevSecOps: [Resolución de 404s Headless y Enlaces Ambiguos WAI-ARIA](/biblioteca/resolucion-de-404s-headless-y-enlaces-ambiguos-wai-aria.html).