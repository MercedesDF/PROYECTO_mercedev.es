---
titulo: "Optimización del Dashboard de Grafana para Mejorar la Experiencia del Autor"
descripcion: "Se implementó una solución que reduce el tiempo de respuesta en el dashboard de Grafana al actualizar los estados documentales."
tipo: "cuadernillo"
tema: "DevSecOps e Infraestructura"
subtema: "Gobernanza"
fecha: "2026-05-18"
fase: "Epic 3 - Fase 4"
estado: "publicado"
alt_portada: "Optimización del dashboard de Grafana para una mejor experiencia del autor."
---
## El Desafío (Síntoma)
Se detectó que el dashboard de Grafana tardaba mucho en actualizar los estados documentales (incubación, promoción) al interactuar con los agentes. Esto generaba fricción (peor DX) porque estas son las métricas que más fluctúan al crear contenido.

## La Maniobra (Lógica)
Se invirtió la lógica del Muestreo Escalonado (Staggered Sampling) en `merci-sre.py`. Ahora la función `actualizar_estado_documental` escanea los YAML Frontmatter cada segundo, mientras que la lectura de los JSON (deriva, duración) se ejecuta cada 10 segundos (`ticks % 10 == 0`).

## El Aprendizaje / Deuda Técnica
Priorizar la Experiencia del Autor (Author Experience) sobre la optimización pura de I/O de disco. En hardware moderno (SSD), escanear directorios locales cada segundo tiene un coste marginal que se compensa ampliamente con un dashboard reactivo en tiempo real.