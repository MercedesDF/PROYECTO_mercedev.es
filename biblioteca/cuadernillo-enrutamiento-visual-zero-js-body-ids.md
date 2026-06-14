---
titulo: "Enrutamiento Visual Zero-JS mediante Body IDs"
descripcion: "Técnica para resaltar dinámicamente enlaces activos en menús de sitios estáticos utilizando atributos SASS combinados y 0ms de latencia JavaScript."
tipo: "cuadernillo"
tema: "Desarrollo y Arquitectura"
subtema: "Frontend"
fecha: "2026-05-16"
fase: "Epic 3 - Fase 1"
estado: "publicado"
alt_portada: "Código HTML mostrando la inyección de un ID dinámico en la etiqueta body para controlar el CSS del menú de navegación."
---
## El Desafío (Síntoma)

En una arquitectura SSG (Static Site Generation - Generación de Sitios Estáticos) donde el menú principal (`<header>`) se extrae de un archivo base y se inyecta en el resto de páginas de forma idéntica, resultaba imposible añadir la clase `.active` directamente en el HTML del enlace activo. La solución tradicional requiere utilizar JavaScript cliente para leer `window.location.pathname`, lo que introduce latencia, aumenta el peso del DOM y viola la política estricta de Cero Dependencias del proyecto.

## La Maniobra (Lógica)

Se aplicó un patrón de enrutamiento puramente basado en CSS (Cascading Style Sheets) nativo. El orquestador Python, al compilar la vista estática, inyecta un identificador único en la etiqueta global del documento (ej. `<body id="page-sobre-mi">`) basándose en el contexto del archivo.

Posteriormente, en la arquitectura SASS, se utilizan selectores descendentes de atributo combinado para interceptar el enlace que coincide con el ID de la página actual: `#page-sobre-mi .nav__link[href="/sobre-mi/"] { color: $color-primary; }`.

## El Aprendizaje / Deuda Técnica

El motor nativo CSS es invariablemente más rápido y eficiente que cualquier ejecución del DOM mediante JavaScript. Delegar el estado global de la aplicación a identificadores en el contenedor raíz (`<body>`) preserva la inmutabilidad y la pureza del componente `<header>`, logrando un resaltado contextual perfecto sin comprometer la métrica de 100/100 en el Total Blocking Time (TBT).