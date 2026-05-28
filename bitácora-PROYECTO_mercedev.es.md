# Bitácora del Proyecto: PROYECTO_mercedev.es

## [2026-05-28] - Resolución de Errores de Aspect Ratio en Auditoría Lighthouse
- **Descripción:** Se ha corregido el error de relación de aspecto reportado por Lighthouse en la auditoría de PageSpeed Insights ("Muestra imágenes con una relación de aspecto incorrecta").
- **Acciones Realizadas:**
  - Se identificó que la imagen del marcador de posición `tu_avatar.webp` tenía dimensiones naturales de `406x389` pero se mostraba en un contenedor estricto de `80x80` (relación de aspecto 1:1) en el DOM.
  - Se redimensionó y recortó mediante script de Python (librería Pillow) la imagen `tu_avatar.webp` a un tamaño de `160x160` (formato WebP). Esto asegura una proporción natural 1:1 exacta, coincidiendo con la declarada en las propiedades HTML y soportando pantallas de alta densidad (Retina, 2x).
  - Se verificó y ajustó preventivamente la imagen `tu_logo.webp` a una resolución de `526x130` (proporción 263:65). De este modo se mantiene la paridad estricta con sus atributos de visualización y se evitan futuras penalizaciones métricas de *Cumulative Layout Shift* (CLS).
- **Resultado:** Las imágenes ahora cumplen las reglas estrictas de rendimiento de Lighthouse. El proyecto mantiene un estado de validación perfecto de cara al cierre de la actual Épica/Fase.
