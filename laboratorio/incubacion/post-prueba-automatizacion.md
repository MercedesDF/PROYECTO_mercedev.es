---
titulo: "Prueba de Integración: WP y LinkedIn"
descripcion: "Validando el pipeline de publicación automatizada End-to-End."
fecha: "2026-05-08"
estado: "incubacion"
estado_social: "en_cola"
tipo: "articulo"
tema: "DevSecOps"
alt_portada: "Esquema de integración continua"
linkedin_id: "urn:li:share:7458645854158016512"
---

## El Desafío
Probar que el ecosistema es capaz de publicar simultáneamente en el Headless CMS y en redes sociales sin intervención manual, usando únicamente un archivo Markdown como Única Fuente de Verdad (SSOT).

## La Maniobra
Se inyectó el estado `"publicado"` en el YAML Frontmatter y un comentario HTML oculto en el cuerpo del documento para que lo lea el publicador social:

<!-- linkedin: ¡La Fase 3 está sellada! 🚀 Hoy he logrado que mi orquestador DevSecOps en Python publique automáticamente en mi Headless CMS y en LinkedIn leyendo un único archivo Markdown desde mi terminal local. Cero fricción, cero dependencias, pura automatización. #Python #DevSecOps #Productividad -->

## El Aprendizaje
La separación de responsabilidades funciona. El script `merci-wp` asume la carga dinámica web, y `merci-linkedin` asume la carga social, enlazados por el mismo Markdown.