---
titulo: "Resolviendo el Problema del Desbordamiento en Bloques de Código"
descripcion: "Descubre cómo una simple modificación en la hoja de estilos base solucionó los problemas de desbordamiento horizontal y exportación PDF en nuestras etiquetas pre y code."
tema: "Blog"
subtema: "Estilos"
fecha: "2026-06-13"
fase: "Epic 8 - Fase 6"
estado: "publicado"
estado_social: "en_cola"
tipo: "blog"
alt_portada: "Representación visual de un bloque de código técnico contenido y perfectamente alineado dentro de los márgenes de una pantalla de teléfono móvil."
---
Cuando la telemetría colapsa, el mundo digital se vuelve a poner de pie. En nuestro caso específico, durante las pruebas de calidad (QA) de la Biblioteca de cuadernillos, se detectó un problema que parecía sencillo pero tenía consecuencias serias.

El texto preformateado en etiquetas `<pre>` y `<code>` estiraba artificialmente el ancho total de la página, provocando desbordamiento horizontal y penalizando métricas clave como Core Web Vitals. Además, al intentar exportar las versiones PDF del ecosistema con motores de renderizado como WeasyPrint, las líneas de código largas se truncaban, ocultando información vital.

La solución a este problema parecía obvia: simplemente necesitábamos asegurarnos de que el texto dentro de estos bloques no superara los límites del contenedor. Pero la implementación de esta solución no fue tan sencilla como uno pudiera pensar.

Se aplicó un parche a nivel arquitectónico en la hoja de estilos base (`src/scss/base/_typography.scss`), estableciendo reglas de contención rígidas e implacables sobre ambas etiquetas semánticas. Se inyectaron las directivas `white-space: pre-wrap;` y `word-break: break-word;`, instruyendo al navegador para que preservara los espacios y sangrías del código original, pero fuerzando un salto de línea si la cadena de texto amenazaba con romper el margen físico.

Además, como medida de seguridad adicional, se añadió `overflow-x: auto;` y `max-width: 100%;` a la etiqueta `<pre>`, lo que protege la estructura principal del documento en dispositivos móviles.

Este pequeño ajuste en la hoja de estilos base nos permitió resolver dos problemas críticos: el desbordamiento horizontal en dispositivos móviles y la exportación documental con líneas de código largas truncadas. La metodología de "Especificación como Fuente" (*Spec as Source*) se refuerza aquí, ya que los estilos CSS no solo embellecen el HTML, sino que también lo protegen en cualquier contexto de lectura.

Proveer reglas CSS agnósticas que cubran tanto las ventanas de navegadores móviles como el renderizado de impresión física (PDFs estáticos) consolida la dualidad de nuestra documentación. Hemos erradicado un *bug* silencioso y recurrente sin añadir lógica pesada en JavaScript, manteniendo un rendimiento puro de 100/100.

### 💡 En resumen:
La solución a los problemas de desbordamiento horizontal y exportación PDF en bloques de código fue una simple modificación en la hoja de estilos base. Utilizando `white-space: pre-wrap;`, `word-break: break-word;`, `overflow-x: auto;` y `max-width: 100%;`, logramos mantener la usabilidad en dispositivos móviles y garantizar una exportación perfecta a PDF.

[Leer cuadernillo](/biblioteca/contencion-visual-y-desbordamiento-en-bloques-de-codigo.html)

---

<!-- linkedin:
Cuando la telemetría colapsa, el mundo digital se vuelve a poner de pie. Descubre cómo una simple modificación en la hoja de estilos base solucionó los problemas de desbordamiento horizontal y exportación PDF en nuestras etiquetas pre y code. #mercedev.es
-->