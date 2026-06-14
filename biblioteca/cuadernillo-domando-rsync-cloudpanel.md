---
titulo: "Domando Rsync en IaaS Multi-Tenant: Permisos, .user.ini y Código 23"
descripcion: "Resolución de colisiones críticas de despliegue continuo (CD) al utilizar rsync contra un entorno restrictivo de CloudPanel."
tipo: "cuadernillo"
tema: "DevSecOps e Infraestructura"
subtema: "Gobernanza"
fecha: "2026-05-22"
fase: "Epic 5 - Fase 1"
estado: "publicado"
alt_portada: "Consola de terminal mostrando comandos rsync con múltiples banderas de exclusión de permisos."
---
### El Desafío (Síntoma)
Durante el despliegue automatizado del Showcase hacia un subdominio gestionado por CloudPanel, el comando `rsync -avz --delete` falló reiteradamente devolviendo el fatídico "Código de Salida 23". Los errores oscilaban entre `Operation not permitted` al intentar cambiar las fechas de los directorios y bloqueos al intentar borrar archivos del servidor.

### La Maniobra (Lógica)
Se analizó la arquitectura del servidor destino. CloudPanel protege la raíz de los sitios inyectando archivos inmutables a nivel de Kernel (`chattr +i` sobre `.user.ini`) y carpetas SSL (`.well-known`). Como el usuario SSH carece de privilegios `root`, se instruyó a Rsync para operar como un ciudadano educado relajando sus pretensiones de archivo (Archive Mode).
Se inyectaron las banderas `--no-o` (ignorar propietario), `--no-g` (ignorar grupo), `--no-perms` (ignorar chmod), `--omit-dir-times` (no alterar metadatos temporales de carpetas raíz) y exclusiones explícitas (`--exclude=/.well-known` y `--exclude=/.user.ini`). Además, se inyectó la llave SSH explícitamente vía variable `.env`.

### El Aprendizaje / Deuda Técnica
La bandera `-a` (Archive) de Rsync asume un control casi total sobre la máquina destino, algo que un entorno IaaS (Infrastructure as a Service) multi-tenant o administrado siempre bloqueará por diseño de seguridad. Relajar la sincronización de metadatos estructurales (mientras se conserva la fecha de los archivos para caché) es el compromiso necesario para lograr un pipeline CI/CD robusto y sin falsos negativos.

### En resumen
Intentar sincronizar archivos a un servidor moderno a la fuerza bruta es como intentar redecorar un hotel sin pedirle permiso al dueño. El servidor bloqueará la puerta si se intentan alterar funciones críticas como los sistemas de seguridad. Se tuvo que "educar" a la herramienta de subida para que solo moviera el mobiliario (los archivos web) sin intentar cambiar las cerraduras de las puertas o reclamar la propiedad del edificio, logrando por fin un despliegue sin errores.

<!-- linkedin: 
El "Código 23" de Rsync al desplegar una web es un error frustrante pero justificado. 🤬
Ese temido error suele ser culpa del propio servidor Cloud protegiendo su integridad. Descubre en este cuadernillo cómo se han domado los permisos SSH, relajado los metadatos y excluido archivos inmutables del Kernel para lograr despliegues CI/CD de fricción cero. 🚀
-->