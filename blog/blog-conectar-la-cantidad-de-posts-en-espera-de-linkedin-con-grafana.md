---
titulo: "Conectar la Cantidad de Posts en Espera de LinkedIn con Grafana"
estado: "publicado"
estado_social: "en_cola"
tema: "Blog"
fase: "Epic 3 - Fase 1"
fecha: "2026-05-13"
descripcion: "Conectar la Cantidad de Posts en Espera de LinkedIn con Grafana"
alt_portada: "Conectar la Cantidad de Posts en Espera de LinkedIn con Grafana"
---
<!-- linkedin:
¿Cómo rastrear en tiempo real los posts de LinkedIn? ¡Con esta solución! 📈 #DevSecOps #DesarrolloWeb
-->

## El Desafío (Síntoma)
No había forma de monitorear en tiempo real la cantidad de posts en espera de LinkedIn.

## La Maniobra (Lógica)
Implementamos la métrica `merci_linkedin_queue_total` en el agente SRE para rastrear documentos con estado_social en_cola. Ahora, los datos se muestran directamente en Grafana.

[Leer el artículo completo](/biblioteca/conectar-la-cantidad-de-posts-en-espera-de-linkedin-con-grafana.html)