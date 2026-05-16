---
titulo: "Actualización de la Política de Seguridad para Prevenir ataques a la cadena de suministro"
estado: "incubacion"
estado_social: "en_cola"
tema: "Blog"
fase: ""
fecha: "2026-05-16"

<!-- linkedin:
Estamos felices de anunciar nuestra última actualización en la seguridad de nuestro proyecto. Al bloquear etiquetas <script src="..."> y <link rel="stylesheet"> externas, hemos salvado nuestra regla arquitectónica "Zero Bloat" y evitado posibles ataques a la cadena de suministro. 🛡️💻

#DevSecOps #DesarrolloWeb
-->

Durante las pruebas finales de Chaos Engineering, me di cuenta de que la IA logró evadir nuestras defensas inyectando una hoja de estilos CSS desde un dominio malicioso externo. Esto comprometía la seguridad del proyecto y violaba la regla arquitectónica de "Zero Bloat". Entonces, decidimos actuar.

Para proteger contra ataques a la cadena de suministro, actualizamos el Agente Auditor para bloquear cualquier etiqueta `<script src="...">` o `<link rel="stylesheet">` que apunte a dominios externos (distintos a localhost o mercedev.es). Además, implementamos un mecanismo de degradación elegante ante señales SIGINT (Ctrl+C), cerrando el pipeline con una experiencia del desarrollador (DX) impecable.

Esta solución es la óptima porque asegura que solo se carguen recursos locales, minimizando el riesgo de ataques a la cadena de suministro. La implementación del mecanismo de degradación elegante mejora la experiencia del desarrollador al proporcionar una salida limpia y ordenada en caso de interrupción inesperada.

Para aprender más sobre esta actualización y cómo podemos proteger aún más nuestra infraestructura, te invitamos a leer la documentación completa aquí: /biblioteca/actualizacion-de-la-politica-de-seguridad-para-prevenir-ataques-a-la-cadena-de-suministro.html