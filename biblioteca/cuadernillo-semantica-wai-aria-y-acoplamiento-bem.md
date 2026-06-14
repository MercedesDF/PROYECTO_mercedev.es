---
titulo: "Semántica HTML y WAI-ARIA: Roles implícitos y acoplamiento BEM"
descripcion: "Por qué los lectores de pantalla ignoran etiquetas aria-label genéricas y el peligro de acoplar bloques BEM."
tipo: "cuadernillo"
tema: "DevSecOps e Infraestructura"
subtema: "Gobernanza"
fecha: "2026-05-06"
fase: "Epic 1 - Fase 11"
estado: "publicado"
alt_portada: "Esquema mostrando un div genérico siendo ignorado por un lector de pantalla frente a uno con role='group'."
---

## El Desafío (Síntoma)
Durante la auditoría de las últimas vistas (Engineering Dashboard y CV Semántico), surgieron dos incidentes arquitectónicos aparentemente inconexos pero nacidos de la misma causa: la falta de semántica estricta.

1. **Ceguera de Lector de Pantalla:** Se inyectó un atributo `aria-label="Métricas de rendimiento del sistema"` a un `<div>` genérico que actuaba como contenedor del dashboard. Sin embargo, las tecnologías asistivas a menudo lo ignoraban por completo al leer la página.
2. **Acoplamiento BEM:** Los botones de llamada a la acción (CTA) del Hero en el currículum estaban utilizando la clase `.nav__link`. Aunque visualmente resolvía el problema temporalmente, ataba el diseño de un componente local a la barra de navegación global de la web.

## La Maniobra (Lógica)
1. **Restauración WAI-ARIA:** Se inyectó explícitamente el atributo `role="group"` al `<div>` genérico del dashboard (`<div class="hero__dashboard" role="group" aria-label="...">`).
2. **Desacoplamiento BEM:** Se eliminó la clase `.nav__link` de los botones del Hero en el HTML. En su lugar, se crearon reglas SASS nativas anidadas dentro de su propio bloque (`.hero__cta a`) para gobernar su aspecto. Adicionalmente, se restituyó la etiqueta estructural `<h2>` para la declaración de intenciones en el currículum que había quedado huérfana.

## El Aprendizaje / Deuda Técnica
Este incidente refuerza dos reglas fundamentales en el ecosistema:

- **WAI-ARIA y Elementos Genéricos:** Un `aria-label` por sí solo no convierte un elemento genérico (`div`, `span`) en algo semánticamente relevante. El estándar dictamina que, si un elemento carece de semántica nativa (como sí la tienen `<nav>`, `<main>`, o `<button>`), el navegador y el Árbol de Accesibilidad no le darán un "nombre accesible" a menos que se le asigne un rol válido (como `group` o `region`).

- **Principio de Responsabilidad Única en CSS:** Reutilizar clases globales (como `.nav__link`) para "ahorrar" código en botones aislados es un antipatrón en la metodología BEM. Genera un código frágil: cualquier cambio futuro de espaciado o color en el menú global habría destrozado visualmente los botones de la portada.

*Si no tiene rol, no existe. Si no es su bloque, no usa su clase.*