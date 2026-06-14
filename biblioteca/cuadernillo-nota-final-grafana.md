---
titulo: "Conectar la Cantidad de Posts en Espera de LinkedIn con Grafana"
descripcion: "Se implementó una métrica para rastrear los documentos con estado_social en_cola en el agente SRE."
tipo: "cuadernillo"
tema: "DevSecOps e Infraestructura"
subtema: "Gobernanza"
fecha: "2026-05-13"
fase: "Epic 3 - Fase 1"
estado: "publicado"
alt_portada: "Diagrama de flujo del pipeline DevSecOps desde la nota hasta el dashboard de métricas."
---
## El Desafío (Síntoma)
Se detectó que no había una forma de monitorear en tiempo real la cantidad de posts en espera de LinkedIn, lo que dificultaba la observabilidad y gestión de estos documentos.

## La Maniobra (Lógica)
Se implementó la métrica `merci_linkedin_queue_total` en el agente SRE para rastrear los documentos con estado_social en_cola. Esto permitió crear una conexión directa entre LinkedIn y Grafana, facilitando la visualización de la cantidad de posts en espera.

## El Aprendizaje / Deuda Técnica
Tras depurar el YAML Frontmatter generado por Ollama, logramos un pipeline DevSecOps perfecto donde todo fluye desde la nota rápida hasta el dashboard de métricas. Esta solución es óptima porque permite una observabilidad real y eficiente de los posts en espera de LinkedIn.