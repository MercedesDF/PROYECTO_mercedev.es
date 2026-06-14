---
titulo: "Optimización del Dashboard de Grafana para Mejorar la Experiencia del Autor"
descripción: "Se implementó una solución que reduce el tiempo de respuesta en el dashboard de Grafana al actualizar los estados documentales."
estado: "publicado"
estado_social: "aprobado"
subtema: "Blog"
fase: "Epic 3 - Fase 2"
fecha: "2026-05-18"
descripcion: "Se implementó una solución que reduce el tiempo de respuesta en el dashboard de Grafana al actualizar los estados documentales."
---
<!-- linkedin:
La eficiencia es clave. Al reducir significativamente el tiempo de respuesta en el dashboard de Grafana, se ha mejorado la experiencia del autor. Conoce cómo se implementó esta solución en merci-sre.py y descubre los beneficios reales. #DevSecOps #DesarrolloWeb
-->

La interacción con el dashboard de Grafana presentaba fricciones operativas cuando se detectó que tardaba demasiado en actualizar los estados documentales, como la incubación y promoción, al interactuar con los agentes. Estas métricas fluctuaban frecuentemente al crear contenido, lo que generaba una mala experiencia de usuario (UX). 

Para resolver este problema, se invirtió la lógica del Muestreo Escalonado en el script `merci-sre.py`. La función `actualizar_estado_documental` ahora escanea los YAML Frontmatter cada segundo, mientras que la lectura de los JSON (deriva, duración) se ejecuta cada 10 segundos (`ticks % 10 == 0`). Esta modificación permitió optimizar el tiempo de respuesta y mejorar la interactividad del dashboard.

Al priorizar la Experiencia del Autor sobre la optimización pura de I/O de disco, se descubrió que en hardware moderno (SSD), escanear directorios locales cada segundo tiene un coste marginal que se compensa ampliamente con un dashboard reactivo en tiempo real. 

Para explorar más detalles sobre esta implementación y cómo afectó la eficiencia del ecosistema, el [documento completo está disponible en el siguiente enlace](/biblioteca/optimizacion-del-dashboard-de-grafana-para-mejorar-la-experiencia-del-autor.html).