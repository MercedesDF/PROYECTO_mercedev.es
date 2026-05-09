---
titulo: "El límite del YAML: Comentarios HTML como almacenamiento de metadatos"
estado: "publicado"
tema: "Arquitectura de software"
tipo: "cuadernillo"
descripcion: "Cómo superar las limitaciones de parseo en YAML inyectando metadatos multilínea dentro de comentarios HTML nativos."
alt_portada: "Fragmento de código mostrando un comentario HTML utilizado como almacenamiento de datos."
fecha: "2026-05-01"
fase: "8 (Expansión de Contenido)"
linkedin_id: "urn:li:share:7458645856410472448"
---

<!-- linkedin:
A veces, la mejor solución a un problema de backend es un "hack" de frontend clásico. Hoy os cuento en Art de Coté cómo usamos comentarios HTML para salvar las limitaciones del formato YAML sin instalar dependencias. 💡
https://mercedev.es/blog/el-limite-del-yaml-comentarios-html
-->

## El Desafío (Síntoma)
En nuestro flujo de automatización, queríamos redactar los posts de LinkedIn directamente en la cabecera YAML de los artículos (usando el formato multilínea `|`). Sin embargo, nuestro parseador de YAML "casero" en Python (basado en divisiones de texto por `:`) destruía los saltos de línea, publicando mensajes vacíos en la red social. Para solucionarlo "correctamente", habríamos tenido que programar un parseador completo o instalar la librería `PyYAML`, rompiendo nuestra estricta regla de 0 dependencias.

## La Maniobra (Lógica)
Optamos por el pensamiento lateral (Navaja de Ockham). En lugar de pelear con el YAML de la cabecera, movimos el texto de LinkedIn al **cuerpo** del artículo Markdown, pero escondido dentro de un comentario HTML estándar (`<!-- linkedin: ... -->`). 

## El Aprendizaje / Deuda Técnica
Como los conversores a HTML y PDF ignoran los comentarios, el texto es invisible para los lectores de la web. Sin embargo, para nuestro script de Python, leer un comentario HTML con una Expresión Regular (`RegEx`) es extremadamente fácil y seguro, conservando todos los saltos de línea intactos. A veces, la sobreingeniería es el enemigo de la eficiencia; adaptar el formato de entrada suele ser mucho más elegante que reinventar la herramienta que lo procesa.