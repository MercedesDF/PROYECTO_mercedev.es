---
titulo: "Resolución de 404s Headless y Enlaces Ambiguos WAI-ARIA"
descripcion: "Cómo erradicar enlaces rotos en PDFs mediante un patrón de publicación en dos pasos y prevenir colisiones de accesibilidad WCAG inyectando dimensión temporal."
tipo: "cuadernillo"
tema: "DevSecOps y Gobernanza"
fecha: "2026-05-18"
fase: "Epic 3 - Fase 2"
estado: "publicado"
alt_portada: "Lupa escaneando una estructura de nodos de red detectando un enlace roto."
---
## El Desafío (Síntoma)
Durante la validación continua, el rastreador dinámico local (`merci-linkcheck.py`) bloqueó el pipeline al detectar dos anomalías críticas en producción:
1. **Errores 404 en descargas:** El CMS servía enlaces de descarga hacia archivos PDF (`/descargas/articulo.pdf`) que no existían físicamente. Esto sucedía porque el tema de WordPress asumía que siempre habría un PDF para cada artículo, incluso si el generador local había fallado o el artículo de origen había sido eliminado (Posts Zombis).
2. **Infracción WAI-ARIA (WCAG):** Se detectaron múltiples enlaces con el mismo "Nombre Accesible" (`aria-label="Leer artículo completo: [Título]"`) apuntando a destinos diferentes. Esto ocurría en la batería de pruebas automatizadas al publicar varios posts con idéntico título, confundiendo gravemente a los lectores de pantalla.

## La Maniobra (Lógica)
**1. Amputación de PDFs Dinámicos (Zero Bloat):**
Para resolver los 404 de los adjuntos rotos, se decidió extirpar completamente la generación de PDFs del orquestador Headless (`merci-wp.py`). El contenido dinámico y efímero del blog no requiere versiones descargables pesadas; estas se reservan exclusivamente para los manuales inmutables de la Biblioteca estática.

**2. Accesibilidad con Dimensión Temporal:**
Para resolver la ambigüedad WAI-ARIA sin alterar la interfaz visual, se inyectó la fecha de publicación en los atributos `aria-label` tanto del motor estático (SSG) como del Child Theme de WordPress (`index.php`). El código resultante se convierte en `<a aria-label="Leer artículo completo: Título (YYYY-MM-DD)">`.

## El Aprendizaje / Deuda Técnica
*   **Erradicar es mejor que parchear:** Intentar crear flujos complejos (publicación en dos pasos) para mantener una funcionalidad innecesaria (PDFs de posts de blog) genera deuda técnica. La mejor solución DevSecOps suele ser borrar la característica superflua.
*   **El tiempo como factor de unicidad:** En interfaces donde los títulos pueden repetirse (como un blog), añadir la dimensión temporal de publicación al `aria-label` es una solución arquitectónica elegante. Garantiza identificadores únicos para las herramientas de accesibilidad (100/100 en Core Web Vitals) sin forzar a los redactores a inventar títulos artificialmente distintos.

## En resumen
En lugar de intentar arreglar los botones de descarga de PDFs rotos en el blog, nos dimos cuenta de que nadie necesita descargar en PDF una noticia rápida. Así que eliminamos completamente esa opción para el blog, dejando la web más ligera y sin errores. Además, se ha añadido la fecha "invisible" a los nombres internos de los artículos para que las personas que usan lectores de pantalla no se confundan cuando haya dos textos distintos que se llamen igual.

<!-- linkedin:
Añadir funcionalidades innecesarias es el primer paso hacia los enlaces rotos y la pérdida de integridad. 🕸️🔍 

Durante la auditoría del pipeline de publicación automatizado de mercedev.es, el rastreador local 'merci-linkcheck.py' detectó descargas "zombi" y colisiones severas de accesibilidad en los lectores de pantalla debido a enlaces ambiguos.

Para erradicar estos falsos positivos, aplicamos la regla de oro: amputar la característica de raíz. Los PDFs dinámicos fueron eliminados del blog en favor de un enfoque 100% ultraligero.

Adicionalmente, se ha inyectado dimensión temporal en los aria-labels, resolviendo la ambigüedad en artículos homónimos y ofreciendo contexto exacto a las tecnologías asistivas.

#DevSecOps #Accesibilidad #WebPerformance #ArquitecturaHeadless#mercedev.es
-->