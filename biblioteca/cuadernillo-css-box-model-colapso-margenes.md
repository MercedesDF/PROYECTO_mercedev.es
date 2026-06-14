---
titulo: "CSS Box Model y el Colapso de Márgenes en Diseños Asimétricos"
descripcion: "Resolución del desalineamiento vertical en el patrón Side-Heading neutralizando las reglas nativas del DOM mediante rellenos internos (padding)."
tipo: "cuadernillo"
tema: "Desarrollo y Arquitectura"
subtema: "Frontend"
fecha: "2026-05-16"
fase: "Epic 3 - Fase 1"
estado: "publicado"
alt_portada: "Esquema visual del modelo de caja CSS demostrando cómo el uso de padding previene el colapso de márgenes frente al uso del atributo margin."
---
## El Desafío (Síntoma)

Durante la implementación del diseño editorial *Side-Heading* (Titulares flotados a la izquierda), se evidenció un fallo crítico de alineación. Cuando un titular `h2` (elemento extraído del flujo mediante `float: left`) iba seguido inmediatamente de un `h3` o de un párrafo, la línea horizontal divisoria se desfasaba y los textos arrancaban a diferentes alturas. El diagnóstico reveló el fenómeno del *Colapso de Márgenes*: los márgenes superiores de los elementos en el flujo normal se fusionan, mientras que los de los elementos flotados se mantienen rígidos.

## La Maniobra (Lógica)

Se sustituyó el control de distancias basado en `margin-top` por `padding-top` en los bloques divisores del artículo (`src/scss/components/_prose.scss`).

Se neutralizó el margen superior (`margin-top: 0`) para los encabezados secundarios (`> h2`) y sus hermanos adyacentes directos (`> h2 + *`), aplicando un relleno interno idéntico (`padding-top: 4.5rem`) a ambos. La línea separadora (pseudo-elemento `::before`) se ancló mediante un posicionamiento absoluto ajustado exactamente a la mitad del *padding*.

## El Aprendizaje / Deuda Técnica

En la especificación del Consorcio World Wide Web (W3C), los márgenes (margin) pueden colapsar entre hermanos adyacentes, pero los rellenos internos (padding) nunca lo hacen. El diseño asimétrico exige una precisión matemática milimétrica; estandarizar los modelos de caja de todos los elementos para que usen `padding` erradica el comportamiento nativo impredecible del navegador, garantizando que los elementos arranquen exactamente en el mismo píxel horizontal independientemente de su etiqueta.