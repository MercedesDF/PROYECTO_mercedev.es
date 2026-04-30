---
titulo: "La Guerra de la Especificidad CSS"
descripcion: "Análisis forense de por qué la pseudo-clase :visited no se aplicaba a los enlaces, y cómo la jerarquía de selectores determina el resultado final."
tipo: "cuadernillo"
tema: "Arquitectura y Rendimiento"
fecha: "2026-04-29"
estado: "publicado"
alt_portada: "Diagrama que muestra la puntuación de especificidad de diferentes selectores CSS, desde un selector de etiqueta hasta un estilo en línea."
---

## 1. El Desafío (Síntoma)

Tras implementar la pseudo-clase `:visited` en la arquitectura SASS para mejorar la usabilidad, se detectó que los enlaces de los títulos en las tarjetas de la Biblioteca y los enlaces del índice autogenerado no cambiaban de color tras ser pulsados. El navegador parecía ignorar por completo la regla de estilo para los enlaces visitados.

## 2. La Maniobra (Lógica)

El diagnóstico reveló dos colisiones de **Especificidad CSS**, un sistema de puntuación invisible que usa el navegador para decidir qué regla aplicar cuando varias apuntan al mismo elemento.

#### Incidente 1: Estilos en Línea (Puntuación: 1000)

Los enlaces del índice (`.indice__enlace`) tenían un `style="color: #475569;"` inyectado directamente en el HTML por el script de Python. Un estilo en línea tiene la máxima prioridad (1000 puntos), aplastando cualquier regla externa de una hoja de estilos, cuya especificidad es mucho menor (ej. `a:visited` solo vale 10 puntos).

*   **Solución:** Se eliminó el atributo `style="color: ..."` del script Python y se delegó el control cromático a clases SASS (`.indice__enlace`), restaurando el flujo natural de la cascada.

#### Incidente 2: Selectores Anidados (Puntuación: 0-0-2 vs 0-1-1)

Los enlaces de las tarjetas estaban dentro de un `<h2>`. La hoja de estilos contenía una regla `h2 a { color: inherit; }`. Este selector anidado (`h2 a`) tiene una especificidad de `0,0,2` (dos selectores de etiqueta). La regla global `a:visited` tiene una especificidad de `0,1,1` (un selector de pseudo-clase y un selector de etiqueta).

Aunque `0,1,1` parece mayor, el navegador prioriza el primer número distinto de izquierda a derecha. Como `2` es mayor que `1` en la última columna, la regla `h2 a` ganaba siempre la "guerra".

*   **Solución:** Se añadió una regla más específica: `h2 a:visited { color: $color-visited; }`. Este nuevo selector (`0,1,2`) ahora sí tiene la puntuación necesaria para sobrescribir al selector base.

## 3. El Aprendizaje / Deuda Técnica

La Especificidad CSS es la causa raíz de la mayoría de los bugs visuales de "mi CSS no funciona". Como regla arquitectónica:

1.  **Evitar Estilos en Línea para Colores:** Nunca se debe usar `style="color:..."` en elementos que necesiten estados interactivos (`:hover`, `:focus`, `:visited`). La especificidad de 1000 puntos de los estilos en línea es un "arma nuclear" que destruye la interactividad.
2.  **Igualar o Superar la Especificidad:** Para sobrescribir una regla, el nuevo selector debe tener, como mínimo, la misma "puntuación" de especificidad.

Comprender este sistema de puntuación es fundamental para mantener una arquitectura SASS 7-1 limpia, predecible y sin necesidad de usar `!important` (el cual es un anti-patrón que indica una mala planificación estructural).

---
