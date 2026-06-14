---
titulo: "Consolidación del Enrutamiento Zero-JS: Limpieza de Clases Legacy"
descripcion: "Refactorización para delegar el resaltado de enlaces activos exclusivamente a la hoja de estilos mediante Body IDs, eliminando mutaciones del DOM."
estado: "publicado"
tema: "Desarrollo y Arquitectura"
subtema: "Frontend"
tipo: "cuadernillo"
fase: "Epic 3 - Fase 1"
alt_portada: "Diagrama CSS mostrando cómo la combinación de un Body ID y un selector de atributo resalta un elemento del menú."
fecha: "2026-05-17"
---
## El Desafío (Síntoma)
A pesar de haber implementado una arquitectura SASS basada en selectores de Body IDs (ej. `#page-home`) para manejar el resaltado visual del menú, el enlace activo fallaba en las páginas estáticas (Home, Sobre Mí, Contacto). El problema radicaba en la pervivencia de código *legacy*: la clase `nav__link--active` seguía incrustada en el archivo `index.html` original y el script de sincronización de páginas intentaba reescribirla dinámicamente en tiempo de compilación, interfiriendo con la lógica de la hoja de estilos.

## La Maniobra (Lógica)
Se ejecutó una limpieza estructural (Zero-JS Routing). Primero, se eliminó la clase `nav__link--active` y el atributo de accesibilidad `aria-current="page"` quemados en el archivo maestro de la portada. Segundo, se purgó la lógica de mutación de cadenas (uso de `replace()`) en `merci-sync-pages.py`, permitiendo que el bloque `<header>` se clone de manera 100% literal e inmaculada hacia todas las páginas secundarias estáticas.

## El Aprendizaje / Deuda Técnica
Delegar la responsabilidad del estado de la interfaz de usuario (UI) puramente a la hoja de estilos es la máxima expresión de "Single Source of Truth". Modificar el DOM mediante scripts de compilación para alterar clases activas añade complejidad innecesaria. Al mantener el `<header>` idéntico en todo el ecosistema estático y dejar que el CSS resuelva el estado activo en base al contexto (`body id`), se logra un enrutamiento visual de latencia cero y se reduce radicalmente la deuda técnica.