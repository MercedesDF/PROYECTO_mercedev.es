---
titulo: "Tutorial: Cómo enviar correos cifrados con PGP"
descripcion: "Guía paso a paso para proteger tus comunicaciones por correo electrónico utilizando cifrado asimétrico PGP."
tipo: "cuadernillo"
tema: "DevSecOps y Gobernanza"
fecha: "2026-05-21"
estado: "publicado"
alt_portada: "Un candado abierto y otro cerrado, simbolizando criptografía asimétrica."
fase: "Epic 3 - Fase 4"
---
## El concepto (Sin tecnicismos)
El cifrado PGP (Pretty Good Privacy) funciona con un sistema de "dos llaves" (criptografía asimétrica):
1. **La Llave Pública:** Es como un buzón abierto. Cualquiera puede usarla para meter un mensaje y cerrarlo. Se puede compartir libremente.
2. **La Llave Privada:** Es la única que puede abrir ese buzón. Nunca se comparte y está protegida por contraseña.

Cuando descargas mi llave pública desde la página de contacto, tu ordenador la usa para "cerrar" el mensaje. Una vez cifrado, ni siquiera tú puedes volver a leerlo. Solo yo, con mi llave privada, podré descifrarlo al recibirlo.

## Opción 1: Mozilla Thunderbird (La más fácil)
Thunderbird es un gestor de correo gratuito que trae PGP integrado de fábrica.
1. Descarga e instala [Thunderbird](https://www.thunderbird.net/).
2. Configura tu cuenta de correo habitual (Gmail, Outlook, etc.).
3. Ve a **Herramientas > Administrador de claves OpenPGP**.
4. Selecciona **Archivo > Importar clave(s) pública(s) de un archivo** y elige el archivo `llave-publica.asc` que descargaste de mi web.
5. Al redactar un nuevo mensaje para mí, activa el botón **Cifrar** en la barra superior. ¡Listo!

## Opción 2: Correo web (Gmail/Outlook) con Mailvelope
Si prefieres seguir usando tu correo directamente desde el navegador:
1. Instala la extensión gratuita Mailvelope para Chrome, Edge o Firefox.
2. Abre las opciones de la extensión y ve al **Administrador de Claves**.
3. Haz clic en **Importar** y sube el archivo `llave-publica.asc`.
4. Cuando abras Gmail o Outlook, verás el icono de Mailvelope integrado en el editor de mensajes. Úsalo para escribir y cifrar el correo antes de darle a enviar.

## Opción 3: Terminal (Para ingenieros)
Si ya usas GnuPG en tu sistema Linux o macOS:
```bash
# 1. Importa la clave
gpg --import llave-publica.asc

# 2. Cifra tu mensaje (genera un archivo .asc)
gpg --encrypt --armor --recipient mercedev@mercedev.es mensaje.txt
```
Copia el bloque de texto cifrado resultante y pégalo en un correo normal.