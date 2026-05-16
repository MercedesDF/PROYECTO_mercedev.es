---
titulo: "Actualización de la Política de Seguridad para Prevenir ataques a la cadena de suministro"
estado: "incubacion"
estado_social: "en_cola"
tema: "Blog"
fase: ""
fecha: "2026-05-16"
---
<!-- linkedin:
Acabo de bloquear un vector de ataque a la cadena de suministro local. Al instruir a `merci-audit.py` para prohibir la inyección de etiquetas <script src="..."> y <link rel="stylesheet"> desde dominios externos, he blindado la regla arquitectónica de "Zero Bloat" frente a las mutaciones de `merci-chaos.py`. 🛡️💻

#DevSecOps #DesarrolloWeb
-->

Durante las últimas pruebas con el agente `merci-chaos.py`, me di cuenta de que la IA lograba evadir las defensas inyectando una hoja de estilos CSS desde un dominio externo. Esto comprometía la postura de seguridad y violaba la regla arquitectónica de "Zero Bloat". Había que aplicar un parche estructural inmediato.

Para mitigar este riesgo, actualicé el Agente Auditor (`merci-audit.py`) instruyéndolo para bloquear de forma atómica cualquier etiqueta `<script src="...">` o `<link rel="stylesheet">` que apunte a dominios ajenos a localhost o mercedev.es. Además, implementé un mecanismo de degradación elegante ante señales SIGINT (Ctrl+C), para que el orquestador aborte en cascada si intervengo la consola.

Esta maniobra asegura que solo se carguen recursos locales, blindando la cadena de suministro de extremo a extremo y erradicando los ruidos de *traceback* en pantalla si decido forzar el cierre del pipeline.

[Leer cuadernillo técnico] /biblioteca/actualizacion-de-la-politica-de-seguridad-para-prevenir-ataques-a-la-cadena-de-suministro.html