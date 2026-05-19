---
titulo: "Resolución de 404s Headless y Enlaces Ambiguos WAI-ARIA"
descripcion: "Cómo erradicar enlaces rotos en PDFs mediante un patrón de publicación en dos pasos y prevenir colisiones de accesibilidad WCAG inyectando dimensión temporal."
tipo: "cuadernillo"
tema: "DevSecOps y Gobernanza"
fecha: "2026-05-18"
fase: "Épica 3 - Fase 2"
estado: "publicado"
alt_portada: "Lupa escaneando una estructura de nodos de red detectando un enlace roto."
---
## El Desafío (Síntoma)
Durante la validación continua, el rastreador dinámico local (`merci-linkcheck.py`) bloqueó el pipeline al detectar dos anomalías críticas en producción:
1. **Errores 404 en descargas:** El CMS servía enlaces de descarga hacia archivos PDF (`/descargas/articulo.pdf`) que no existían físicamente. Esto sucedía porque el tema de WordPress asumía que siempre habría un PDF para cada artículo, incluso si el generador local había fallado o el artículo de origen había sido eliminado (Posts Zombis).
2. **Infracción WAI-ARIA (WCAG):** Se detectaron múltiples enlaces con el mismo "Nombre Accesible" (`aria-label="Leer artículo completo: [Título]"`) apuntando a destinos diferentes. Esto ocurría en la batería de pruebas automatizadas al publicar varios posts con idéntico título, confundiendo gravemente a los lectores de pantalla.

## La Maniobra (Lógica)
**1. Publicación Headless en Dos Pasos (SSOT):**
Se refactorizó el script publicador (`merci-wp.py`) para arrebatarle el control de la interfaz al tema de WordPress. Ahora, el script ejecuta un POST inicial para obtener el `slug` definitivo. A continuación, intenta compilar el PDF localmente mediante WeasyPrint. **Solo si la generación del PDF tiene éxito**, el script ejecuta una segunda llamada (PUT) a la API de WordPress para inyectar explícitamente la etiqueta `<a download>` dentro del cuerpo del artículo.

**2. Accesibilidad con Dimensión Temporal:**
Para resolver la ambigüedad WAI-ARIA sin alterar la interfaz visual, se inyectó la fecha de publicación en los atributos `aria-label` tanto del motor estático (SSG) como del Child Theme de WordPress (`index.php`). El código resultante se convierte en `<a aria-label="Leer artículo completo: Título (YYYY-MM-DD)">`.

## El Aprendizaje / Deuda Técnica
*   **La suposición genera deuda (Shift-Left):** Delegar la responsabilidad de la UI al CMS bajo la suposición de que "el PDF existirá" es un antipatrón en arquitecturas Headless. El orquestador que inyecta el contenido debe ser la Única Fuente de Verdad (SSOT) garantizando que solo se enlace lo que matemáticamente se ha generado.
*   **El tiempo como factor de unicidad:** En interfaces donde los títulos pueden repetirse (como un blog), añadir la dimensión temporal de publicación al `aria-label` es una solución arquitectónica elegante. Garantiza identificadores únicos para las herramientas de accesibilidad (100/100 en Core Web Vitals) sin forzar a los redactores a inventar títulos artificialmente distintos.

## Resumiendo (Lenguaje no técnico)
En lugar de dar por hecho que un archivo PDF de descarga siempre estará disponible (lo que a menudo provoca que el usuario pinche en un enlace "roto" que no hace nada), el sistema ahora verifica primero su existencia física en el servidor y solo crea el botón de descarga si el archivo es real. Además, se ha añadido la fecha "invisible" a los nombres internos de los artículos para que las personas que usan lectores de pantalla no se confundan cuando haya dos textos distintos que se llamen igual.

<!-- linkedin:
En arquitecturas Headless, asumir que un archivo estático existirá por defecto es el primer paso hacia los enlaces rotos y la pérdida de integridad. 🕸️🔍 

Durante la auditoría del pipeline de publicación automatizado de mercedev.es, el rastreador local 'merci-linkcheck.py' detectó descargas "zombi" y colisiones severas de accesibilidad en los lectores de pantalla debido a enlaces ambiguos.

Para erradicar estos falsos positivos y mantener un 100/100 estricto en WAI-ARIA, se ha implementado un patrón de publicación en dos pasos (Post -> PDF -> Update).

Adicionalmente, se ha inyectado dimensión temporal en los aria-labels, resolviendo la ambigüedad en artículos homónimos y ofreciendo contexto exacto a las tecnologías asistivas.

#DevSecOps #Accesibilidad #WebPerformance #ArquitecturaHeadless#mercedev.es
-->