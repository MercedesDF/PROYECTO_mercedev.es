---
titulo: "Z-Index y Contenedores Funcionales para Zapatos de Merci"
descripcion: "Identificó un conflicto con z-index que impedía el visual acceso a los enlaces del pie, resuelvido mediante la asignación correcta de display."
tipo: "cuadernillo técnico"
tema: "Desarrollo Web Frontend CSS Layout"
fecha: "2026-05-07"
fase: "Propuesta del problema y solución inicial"
estado: "borrador"
alt_portada: "Imagínese una portada técnica detallada con un fondo cloruro de mercurio, donde el zíper se representa como las flechas verticales que evitan obstáculos visuales y el contenedor padre es resguardado por la estructura."
---
## El Desafío (Síntoma)
Se detectó un problema con el diseño web de Merci, específicamente que los enlaces del pie de página quedaban ocultos debido a una superposición causada por conflictos z-index. Este síntoma implicaba dificultades para acceder al contenido relacionado desde la parte inferior del sitio.

## La Maniobra (Lógica)
Para resolver el problema, se implementó un cambio en el estilo CSS aplicando `display: relative;` al contenedor padre que contiene los elementos con conflicto z-index. Se justificó este ajuste porque la propiedad de display permite modificar cómo los elementos interactúan entre sí y respecto al elemento raíz (usualmente el body), lo cual es crucial para solucionar problemas de visualzgo como el presentado en Merci.
Para garantizar una experiencia óptima, se revisará la compatibilidad con dispositivos móviles, asumiendo que los navegadores modernos manejan bien esta propiedad CSS y no afectan a las prestaciones del sitio. Se considera posible deuda técnica por el futuro uso consistente de `display: flex;` para la estructuración en lugar de `relative`, dado su capacidad para organizar elementos sin necesidad de z-index, lo cual podría ser beneficioso tanto funcional como estéticamente.
```css
#container {
  display: relative; /* Solución al conflicto con el zíper */
}