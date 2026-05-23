---
titulo: "Autenticación OIDC (OAuth 2.0) con Cero Dependencias"
descripcion: "Cómo domar la API de LinkedIn levantando un micro-servidor efímero en Vanilla Python."
tema: "Arquitectura y Rendimiento"
estado: "publicado"
tipo: "cuadernillo"
alt_portada: "Diagrama de flujo de autenticación OIDC con servidor local en Python."
fecha: "2026-05-01"
fase: "Epic 1 - Fase 8"
---

## El Desafío (Síntoma)
Para automatizar las publicaciones del blog hacia LinkedIn, se requería una conexión autenticada. Utilizar "Tokens Estáticos" implicaba renovaciones manuales cada 60 días (fricción operativa). Implementar el flujo completo OIDC (OpenID Connect) garantiza autonomía perpetua, pero convencionalmente requiere librerías externas pesadas (como `requests_oauthlib` o `Flask`), violando la política fundacional de 0 dependencias bloqueantes del proyecto.

## La Maniobra (Lógica)
Se desarrolló un motor de autenticación utilizando exclusivamente la librería estándar de Python (`http.server` y `urllib`). 
El script abre el navegador del usuario para solicitar permiso a LinkedIn, e inmediatamente levanta un micro-servidor web efímero (`localhost:8000/callback`). Este servidor intercepta el código de autorización devuelto por la red social, negocia el canje por el Token de Acceso mediante un POST seguro, y se apaga a sí mismo en milisegundos, guardando la llave localmente.

## El Aprendizaje / Deuda Técnica
El paradigma "Zero Bloat" (Cero Basura) no solo aplica al frontend (CSS/JS), sino también a la infraestructura Backend y CLI (Command Line Interface - Interfaz de Línea de Comandos). 
Replicar un flujo OAuth de tres pasos (Three-legged OAuth) no requiere frameworks masivos. Conocer las capacidades nativas del lenguaje de programación permite construir herramientas DevOps robustas, perpetuas y ultraligeras que no requieren mantenimiento de cadena de suministro (Supply Chain).