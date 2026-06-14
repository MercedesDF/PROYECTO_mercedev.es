---
titulo: "Consolidación del Enrutamiento Zero-JS: Limpieza de Clases Legacy"
descripcion: "Refactorización para delegar el resaltado de enlaces activos exclusivamente a la hoja de estilos mediante Body IDs, eliminando mutaciones del DOM."
estado: "publicado"
estado_social: "aprobado"
tema: "Varios"
subtema: "Blog"
fase: ""
fecha: "2026-05-17"
---
<!-- linkedin:
La limpieza estructural Zero-JS Routing ha transformado la experiencia de navegación en las páginas estáticas, eliminando la necesidad de mutaciones del DOM y asegurando un estado de interfaz de usuario consistente. #DesarrolloWeb #DevSecOps
-->

Para lograr que el menú de navegación resaltara visualmente la página activa, se presentaba una encrucijada técnica: era posible mantener la clase `nav__link--active` quemada directamente en el archivo maestro de la portada, o bien delegar este comportamiento 100% a la hoja de estilos. Se decidió apostar por un enrutamiento "Zero-JS" puro.

El problema del código *legacy* era que obligaba al script de compilación estática a mutar dinámicamente el DOM en cada página para desplazar la clase activa. Para erradicar esto, se eliminó cualquier rastro de la clase activa y del atributo `aria-current="page"` del HTML original, y se purgó la lógica de mutación de cadenas en el sincronizador `merci-sync-pages.py`. Ahora, el bloque `<header>` se clona de manera literal e inmaculada en todas las rutas estáticas.

¿Cómo sabe el enlace cuándo debe resaltarse? Utilizando selectores CSS precisos basados en el atributo `id` inyectado en el `<body>` de cada página. 

Delegar el estado de la interfaz exclusivamente a la hoja de estilos es la máxima expresión de "Single Source of Truth". Al dejar que el CSS resuelva el estado activo según su contexto, se logra un enrutamiento visual de latencia cero, sin scripts mutantes y reduciendo drásticamente la deuda técnica del generador de sitios estáticos.

Para explorar los detalles de esta refactorización, puedes leer la [documentación arquitectónica aquí](/biblioteca/consolidacion-del-enrutamiento-zero-js-limpieza-de-clases-legacy.html).