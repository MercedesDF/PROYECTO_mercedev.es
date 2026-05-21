---
titulo: "La Vida Oculta detrás de las Comunicaciones Seguras con PGP"
descripcion: "Un viaje por el mundo de la seguridad sin formularios PHP ni dependencias externas."
estado: "publicado"
estado_social: "aprobado"
tema: "Blog"
fase: "Epic 3  - Fase 3"
tipo: "blog"
alt_portada: "Representación abstracta de un candado criptográfico protegiendo un sobre de correo."
fecha: "2026-05-21"
---
<!-- linkedin:
La seguridad en las comunicaciones es un tema crucial, y mercedev.es ha desarrollado una solución innovadora utilizando PGP y GnuPG. Se generó un par de claves criptográficas locales para cifrar mensajes de manera segura, sin necesidad de backend o formularios PHP. Este ste enfoque protege la integridad de la arquitectura estática y garantiza que solo tú puedas leer los mensajes enviados.

#DevSecOps #DesarrolloWeb #mercedev.es
-->

En el núcleo estático de mercedev.es, encontramos un desafío: cómo permitir a clientes y auditores enviar información confidencial sin comprometer la integridad de nuestra arquitectura estática. Los formularios tradicionales, basados en PHP o Node.js, son complejos y llenos de posibles vulnerabilidades. Además, los correos electrónicos no cifrados pueden ser interceptados por cualquier nodo intermedio.

La solución que encontrada es implementar un modelo de comunicación asimétrica utilizando el estándar PGP (Pretty Good Privacy) mediante la herramienta nativa GnuPG. Esta elección permite generar un par de claves criptográficas locales, protegiendo la clave privada con una frase de paso fuerte.

En lugar de desplegar una API REST para procesar mensajes, se exporta la clave pública a un archivo ASCII de texto plano y se deposita en el directorio `/public/` para que sea servido directamente desde el servidor web como un activo estático. En la página de contacto, se publica el enlace al archivo `.asc` junto con la Huella Digital criptográfica.

### 💡 Resumiendo:
En lugar de formularios de contacto vulnerables y dependientes de backend, se ha optado por una solución más segura: ofrecer una "caja fuerte" pública. Cualquiera puede descargarse nuestra "llave pública" para cifrar un mensaje desde su propio ordenador. Ese mensaje viaja por internet como un código indescifrable que nadie puede leer, y solo nosotros podemos abrirlo al recibirlo.

Para saber más sobre cómo se implementó esta solución, puedes leer el [cuadernillo completo](/biblioteca/identidad-criptografica-comunicaciones-cifradas-con-pgp.html).