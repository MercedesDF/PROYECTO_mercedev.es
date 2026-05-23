---
titulo: "Organización del Laboratorio con Patrones Zero-Code"
descripcion: "Se describe cómo se organizó el laboratorio para mejorar la visibilidad y seguridad mediante el uso de patrones Zero-Code."
tipo: "cuadernillo"
tema: "DevSecOps y Gobernanza"
fecha: "2026-05-09"
fase: "Epic 2 - Fase 3"
estado: "publicado"
alt_portada: "Un laboratorio organizado con bandejas de entrada y estados documentales para mejorar la visibilidad y seguridad."
---
## El Desafío (Síntoma)
El laboratorio era un caos visual, lo que dificultaba la organización y el seguimiento de los proyectos en curso.

## La Maniobra (Lógica)
Se implementaron patrones Zero-Code para organizar el laboratorio. Primero, se renombró el directorio `incubacion/` para que todo lo nuevo caiga ahí. Segundo, se introdujo un estado `incubacion` en el YAML Frontmatter de los archivos, lo que permitía ocultar los archivos con estado `borrador` en la terminal. Finalmente, se aplicó DLP (Data Leak Prevention) excluyendo el directorio `docs/matriz` del `.gitignore`, asegurando que no subiera a la nube.

## El Aprendizaje / Deuda Técnica
La organización del laboratorio mediante patrones Zero-Code mejoró significativamente la visibilidad y seguridad. La implementación del estado `incubacion` en el YAML Frontmatter facilitó la gestión de los proyectos en diferentes fases. Además, la adopción de DLP evitó posibles fugas de datos sensibles a través del control de versiones.