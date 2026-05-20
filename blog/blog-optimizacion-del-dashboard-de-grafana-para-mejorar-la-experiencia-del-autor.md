---
titulo: "Optimización del Dashboard de Grafana para Mejorar la Experiencia del Autor"
descripción: "Se implementó una solución que reduce el tiempo de respuesta en el dashboard de Grafana al actualizar los estados documentales."
estado: "publicado"
estado_social: "aprobado"
tema: "Blog"
fase: "Epic 3 - Fase 2"
fecha: "2026-05-18"
descripcion: "Se implementó una solución que reduce el tiempo de respuesta en el dashboard de Grafana al actualizar los estados documentales."
---
<!-- linkedin:
La eficiencia del equipo es clave. Al reducir significativamente el tiempo de respuesta en el dashboard de Grafana, hemos mejorado la experiencia del autor. Aprende cómo implementamos esta solución en merci-sre.py y descubre los beneficios reales. #DevSecOps #DesarrolloWeb
-->

La interacción con el dashboard de Grafana se volvió un dolor de cabeza cuando detectamos que tardaba mucho en actualizar los estados documentales, como la incubación y promoción, al interactuar con los agentes. Estas métricas fluctuaban frecuentemente al crear contenido, lo que generaba una mala experiencia del usuario (UX). 

Para resolver este problema, invertimos la lógica del Muestreo Escalonado en el script `merci-sre.py`. La función `actualizar_estado_documental` ahora escanea los YAML Frontmatter cada segundo, mientras que la lectura de los JSON (deriva, duración) se ejecuta cada 10 segundos (`ticks % 10 == 0`). Esta modificación permitió optimizar el tiempo de respuesta y mejorar la interactividad del dashboard.

Al priorizar la Experiencia del Autor sobre la optimización pura de I/O de disco, descubrimos que en hardware moderno (SSD), escanear directorios locales cada segundo tiene un coste marginal que se compensa ampliamente con un dashboard reactivo en tiempo real. 

Si quieres aprender más sobre esta implementación y cómo ella afectó la eficiencia del equipo, te recomendamos leer el documento completo en [este enlace](/biblioteca/optimizacion-del-dashboard-de-grafana-para-mejorar-la-experiencia-del-autor.html).