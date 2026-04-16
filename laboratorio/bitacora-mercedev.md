# Bitácora del proyecto mercedev.es

## Para qué sirve este archivo

- **Yo futuro:** recuperar en minutos qué se decidió, por qué, y cómo se ejecutó algo técnico sin rebuscar en el chat o en commits sueltos.
- **Biblioteca (al cerrar el proyecto):** aquí vive el borrador narrativo y técnico; luego se depura y se traslada a `biblioteca/` como piezas definitivas (por estantería o tema), siguiendo la idea de “activo de conocimiento” del proyecto.

No sustituye a `instrucciones.md` (directrices y rol del asistente). Complementa el día a día con **hechos, comandos y lecciones**.

---

## Cómo mantenerlo (acuerdo simple)

1. **Añadir entradas al final** de la sección “Registro cronológico”, con la plantilla de abajo. El registro es **acumulativo**: lo ya escrito forma parte del historial y **no se reemplaza** por nuevas sesiones (así no se pierde contexto ni fechas).
2. **Una entrada por sesión o por tema cerrado** (lo que resulte más claro al escribir).
3. Si algo fue un error o una vulnerabilidad evitada, opcionalmente usar los **tres átomos** del proyecto (Desafío → Maniobra → Aprendizaje/Deuda) en el cuerpo de la entrada.
4. **Correcciones excepcionales** (typo, dato incorrecto, redacción de un solo párrafo, retirada de información sensible): editar solo el fragmento necesario o añadir una línea aclaratoria bajo la entrada; evitar reescribir todo el archivo o borrar entradas enteras sin motivo documentado.

### Plantilla para nuevas entradas

Copia el bloque y rellénalo.

```markdown
### AAAA-MM-DD — Título corto del cambio o sesión

**Contexto:** (qué querías lograr o qué problema apareció)

**Hecho:** (lista breve: archivos, fases del roadmap, PR/commit si aplica)

**Detalle técnico:** (comandos, rutas, flags; solo lo que necesites recordar)

**Motivo / criterio:** (por qué esta opción y no otra)

**Siguiente paso o deuda:** (qué queda pendiente)
```

---
## Registro cronológico

### 2026-04-16 — Cierre de Fase 5: Consolidación del Documento de Hardening

**Contexto:** Finalizar la Fase 5 (Quality Assurance y Hardening) dejando un registro auditable de todas las medidas de seguridad implementadas en las diferentes capas del proyecto.

**Hecho:**
- Se ha creado el documento `docs/checklist-hardening.md`.
- Se ha marcado el último hito de la Fase 5.4 como completado en el `README.md`.

**Detalle técnico:** El documento recopila las directivas CSP, los hooks de bloqueo en WordPress (XML-RPC, generadores), la política estricta de permisos de servidor (`chmod 600` para `wp-config.php`) y las reglas bloqueantes del auditor DevSecOps.

**Motivo / criterio:** La seguridad no es un estado, es un proceso. Documentar estas medidas en forma de *checklist* garantiza que no se pierda conocimiento arquitectónico y proporciona una herramienta de validación vital para futuros despliegues a producción (Fase 6).

**Siguiente paso o deuda:** Iniciar la Fase 3 (Ingeniería de Estilos) para aplicar SASS y BEM al diseño visual.

### 2026-04-16 — Fase 5.4: Auditoría integral exitosa sin hallazgos

**Contexto:** Tras lanzar la ejecución en todo el repositorio de `merci-audit.py --strict-json-ld`, era necesario confirmar el estado del código base.

**Hecho:**
- Se superó la auditoría estricta sin `ERROR` ni `WARN`.
- Se actualizaron los hitos de la Fase 5.4 en el `README.md` (pasada integral y verificación de ausencia de secretos).

**Detalle técnico:** El script verificó sintaxis, secretos, funciones peligrosas de PHP y SEO técnico en HTML, devolviendo un código de salida `0`.

**Motivo / criterio:** Una validación en verde a este nivel de exigencia confirma que las prácticas de seguridad y calidad (Shift-Left) se han mantenido desde la Fase 1.

**Siguiente paso o deuda:** Consolidar el checklist de hardening para dar por cerrada definitivamente la Fase 5.

### 2026-04-16 — Fase 5.4: Verificación integral de seguridad y consistencia

**Contexto:** Iniciar la última fase de aseguramiento de la calidad antes del despliegue, ejecutando una auditoría completa sobre todo el repositorio para detectar inconsistencias o errores residuales.

**Hecho:**
- Se ha ejecutado el comando de auditoría estandarizado sobre todo el proyecto.
- Se ha actualizado el `README.md` para reflejar el avance.

**Detalle técnico:** Se utilizó el comando `python3 scripts/merci/merci-audit.py --strict-json-ld` para forzar la revisión de todos los archivos con el máximo nivel de exigencia, incluyendo la validación estricta de JSON-LD.

**Motivo / criterio:** Garantizar que no quedan cabos sueltos. Una pasada final sobre el estado completo del repositorio es crucial para validar que las integraciones parciales no han introducido regresiones o vulnerabilidades en otras áreas del proyecto.

**Siguiente paso o deuda:** Corregir los hallazgos críticos que reporte el auditor, si los hubiera.

### 2026-04-16 — Fase 5.3: Documentación de criterios de fallo del auditor

**Contexto:** Abordar el último hito de la Fase 5.3, que consiste en documentar explícitamente la diferencia entre los hallazgos bloqueantes y no bloqueantes del sistema de auditoría.

**Hecho:**
- Se ha añadido un párrafo en la sección "Flujo de Contribución y Validación" del `README.md`.
- Se ha clarificado que los `ERROR` bloquean los commits, mientras que las `WARN` solo informan.
- Se ha marcado la Fase 5.3 como completada en el Roadmap.

**Detalle técnico:** La distinción se basa en el código de salida de `merci-audit.py`. Un `ERROR` provoca un código de salida `1`, que es interpretado por el hook de `pre-commit` de Git como un fallo que debe detener la operación.

**Motivo / criterio:** Claridad y predictibilidad para el desarrollador. Es fundamental que el equipo sepa qué tipo de hallazgos detendrán su trabajo y cuáles son meras sugerencias, optimizando así la experiencia de desarrollo (DX).

**Siguiente paso o deuda:** Iniciar la Fase 5.4 (Verificación de seguridad y consistencia) o retomar la Fase 3 (Ingeniería de Estilos).

### 2026-04-16 — Fase 5.3: Estandarización del flujo de auditoría local

**Contexto:** Se clarificó que la Fase 5 no estaba completa. El siguiente paso pendiente era estandarizar la ejecución de auditorías para garantizar la consistencia en el control de calidad antes de cualquier integración de código.

**Hecho:**
- Se ha añadido una sección "Flujo de Contribución y Validación" en el `README.md`.
- Se ha definido el comando `python3 scripts/merci/merci-audit.py --strict-json-ld` como la auditoría completa oficial.

**Detalle técnico:** La estandarización se logra mediante documentación. Al fijar un comando único y oficial, se elimina la ambigüedad y se asegura que todos los desarrolladores validen el código con el mismo nivel de rigurosidad (incluyendo la validación estricta de JSON-LD).

**Motivo / criterio:** Reproducibilidad y fiabilidad. Un flujo de validación estandarizado es fundamental en DevSecOps para que la calidad no dependa de la memoria o disciplina individual, sino del proceso documentado.

**Siguiente paso o deuda:** Abordar el último punto de la Fase 5.3: "Documentar criterios de fallo/bloqueo".

### 2026-04-16 — Fase 5.3: Ampliación de auditoría de seguridad para PHP

**Contexto:** Con la introducción de WordPress, es necesario que el auditor `merci-audit.py` pueda detectar patrones de código PHP peligrosos que son vectores comunes para vulnerabilidades de Ejecución Remota de Código (RCE).

**Hecho:**
- Se ha implementado la función `audit_php_smells` en `merci-audit.py`.
- Se ha actualizado el Roadmap para reflejar el avance en la Fase 5.3.

**Detalle técnico:** La nueva función utiliza una expresión regular para buscar en archivos `.php` el uso de funciones de alto riesgo como `eval()`, `exec()`, `shell_exec()`, `system()`, etc. Emite una advertencia (`WARN`) para que el desarrollador revise el contexto manualmente.

**Motivo / criterio:** Seguridad "Shift-Left". Al detectar el uso de estas funciones antes de que el código llegue al repositorio, se reduce drásticamente la probabilidad de introducir una puerta trasera accidentalmente, especialmente a través de código de terceros (plugins o temas).

**Siguiente paso o deuda:** Probar el auditor contra el `functions.php` y decidir la siguiente regla de QA a implementar.

### 2026-04-16 — Lección de Flujo: Reparación de historial Git y parcheo manual

**Contexto (Desafío):** Tras un commit exitoso, se intentó corregir una advertencia del linter (`WARN MD_ACRONYM`) con un commit manual. El comando `git add` falló por un error de ruta relativa y un posterior `merci-commit` generó un commit duplicado con un mensaje incorrecto.

**Hecho (Maniobra):**
- Se ha reparado el historial de Git fusionando los dos últimos commits con `git rebase -i HEAD~2`.
- Se ha definido el flujo correcto para parches menores: navegar a la raíz del proyecto y usar `git add <archivo>` y `git commit -m "prefijo: mensaje"` manualmente.

**Detalle técnico:** El error de `git add` se debió a ejecutarlo desde una subcarpeta. El commit duplicado ocurrió porque `merci-commit` re-leyó la última entrada de la bitácora. La solución `fixup` en el rebase interactivo fusiona los cambios y descarta el mensaje del commit secundario.

**Motivo / criterio (Aprendizaje):** Las herramientas de automatización como `merci-commit` son para hitos principales justificados por la bitácora. Los parches de documentación o correcciones menores deben gestionarse con comandos manuales de Git desde la raíz del proyecto para mantener un historial limpio y semántico.

**Siguiente paso o deuda:** Retomar la elección de la siguiente fase del roadmap (Fase 3 o 5.3).

### 2026-04-16 — Fase 4.4: Erradicación de CSS en línea y carga diferida (Defer)

**Contexto:** El análisis del código fuente reveló que WordPress 6.x seguía inyectando bloques `<style>` en línea (como `global-styles` y `classic-theme-styles`), saltándose el `wp_dequeue_style` estándar. Además, faltaba garantizar que futuros scripts no bloquearan el renderizado.

**Hecho:**
- Se añadieron reglas `remove_action` para `wp_enqueue_global_styles`.
- Se desencoló `classic-theme-styles`.
- Se implementó un filtro global (`merci_defer_js_frontend`) para inyectar `defer` en etiquetas `<script>`.

**Detalle técnico:** La función `wp_enqueue_global_styles` se vincula a los hooks `wp_enqueue_scripts` y `wp_body_open`. Eliminar la acción ataja la raíz del problema. El filtro `script_loader_tag` busca ` src` y lo reemplaza por ` defer src` condicionado por `!is_admin()`.

**Motivo / criterio:** Rendimiento puro (Core Web Vitals). El CSS en línea masivo rompe la limpieza del DOM (Document Object Model - Modelo de Objetos del Documento) y retrasa el TTFB (Time to First Byte - Tiempo hasta el Primer Byte). El uso de `defer` asegura que el parseo HTML nunca sea interrumpido por JS, garantizando un LCP (Largest Contentful Paint - Despliegue del Contenido Más Extenso) inmediato.

**Siguiente paso o deuda:** Dar por finalizada la configuración dinámica y decidir el siguiente paso entre diseño frontend (Fase 3 / 4.5) o QA y Seguridad (Fase 5.3).

### 2026-04-16 — Parche: Forzar URL absoluta para CSS estático

**Contexto:** El CSS unificado devolvía 404. WordPress interceptaba el prefijo `/css/main.css` y lo reescribía automáticamente a `http://localhost/blog/css/main.css` en la función `wp_enqueue_style`.

**Hecho:**
- Restaurada la construcción de `$domain_root` dinámico en `functions.php`.
- Forzado el parámetro de URL a una ruta absoluta como `http://[host]/css/main.css`.

**Detalle técnico:** Se implementó `$domain_root = (is_ssl() ? 'https://' : 'http://') . $_SERVER['HTTP_HOST'];` concatenado explícitamente con `/css/main.css`.

**Motivo / criterio:** Aislar el CMS exige forzar la ruta mediante HTTP absoluto para que Nginx la despache directamente desde `public/css/main.css` sin que el motor interno de WordPress manipule el segmento de red.

**Siguiente paso o deuda:** Validar la carga de estilos e iniciar la Fase 4.4.

### 2026-04-16 — Fase 4.2: Corrección de enrutamiento de assets estáticos en WordPress

**Contexto:** El "escudo de rendimiento" limpiaba correctamente el HTML, pero la hoja de estilos devolvía un error 404. WordPress prefijaba la ruta del CSS con `/blog/`, rompiendo el proxy de Nginx que sirve los assets desde la raíz estática.

**Hecho:**
- Se refactorizó la llamada `wp_enqueue_style` en `functions.php`.
- Se implementó la construcción dinámica de la URL absoluta usando `$_SERVER['HTTP_HOST']`.

**Detalle técnico:** WordPress interpreta las rutas como `/assets/main.css` como relativas a su `siteurl`. Se cambió a `$domain_root = (is_ssl() ? 'https://' : 'http://') . $_SERVER['HTTP_HOST'];` para forzar la petición a `http://localhost/assets/main.css` (directo al bloque Nginx).

**Motivo / criterio:** Aislar el CMS (Content Management System) significa que este no debe gobernar cómo se sirven los estáticos. Al forzar la petición a la raíz del dominio, Nginx intercepta la llamada y la sirve con máxima velocidad (caché), protegiendo las métricas de rendimiento.

**Siguiente paso o deuda:** Recargar el frontend para validar la carga del CSS sin errores 404 y verificar la estructura generada por el `index.php` del Child Theme.

### 2026-04-16 — Fase 4.2: Resolución de permisos para enlaces simbólicos (Child Theme)

**Contexto:** WordPress no detectaba el "Merci Theme" enlazado simbólicamente porque el usuario del servidor web (`www-data`) no tenía permisos para atravesar el directorio personal del usuario local.

**Hecho:**
- Se otorgaron permisos de ejecución/paso a la ruta del repositorio anfitrión.
- Se validó la aparición y activación del tema en el panel de administración de WordPress.

**Detalle técnico:** Se aplicó `chmod +x` a las carpetas `/home/hildegahr/`, `Escritorio/` y `PROYECTO_mercedev.es/`. Esto resuelve el "Permiso denegado" permitiendo a `www-data` resolver el enlace simbólico hacia `style.css` e `index.php`.

**Motivo / criterio:** En entornos LEMP locales, es un desafío común la colisión de permisos entre el usuario de escritorio y el demonio web. Dar permiso de ejecución (`+x`) a los directorios anfitriones permite la lectura a través del symlink sin comprometer la política estricta de permisos de los archivos finales.

**Siguiente paso o deuda:** Validar en el frontend (`http://localhost/blog`) que el "escudo de rendimiento" limpia el código fuente inyectado por defecto.

### 2026-04-16 — Fase 4.0: Configuración de wp-config.php y despliegue final

**Contexto:** Conectar la instancia aislada de WordPress con su base de datos dedicada local y asegurar sus permisos de servidor post-instalación.

**Hecho:**
- Se ha creado y configurado `wp-config.php` con credenciales de base de datos (`wp_mercedev_local`) y claves de seguridad generadas.
- Se ha ejecutado el instalador de WordPress a través del proxy inverso de Nginx (`http://localhost/blog`).
- Se ha aplicado el *hardening* de permisos (`chown` y `chmod`) al directorio `/var/www/wordpress/`.
- Se da por finalizada la Fase 4.0 del Roadmap.

**Detalle técnico:** Se aplicó el principio de mínimo privilegio tras la instalación: directorios a `755`, archivos a `644` y un estricto `600` para `wp-config.php`, asignando la propiedad completa a `www-data:www-data`.

**Motivo / criterio:** La instalación local no exime de aplicar prácticas de seguridad de producción. Blindar `wp-config.php` y los permisos del CMS desde el minuto uno garantiza que la arquitectura probada localmente es segura para su posterior migración al servidor de producción.

**Siguiente paso o deuda:** Validar la visualización del Child Theme (Fase 4.2) ahora que existe un WordPress real donde activarlo.

### 2026-04-16 — Fase 4.0: Configuración de Nginx para entorno local

**Contexto:** Configurar el servidor web Nginx en el entorno de desarrollo local para replicar la arquitectura de enrutamiento inverso (reverse proxy) definida en `docs/integracion-wordpress.md`.

**Hecho:**
- Se ha creado un nuevo archivo de configuración de sitio en `/etc/nginx/sites-available/mercedev-local`.
- Se ha adaptado la configuración para el entorno local, apuntando la raíz estática a la carpeta del proyecto y manteniendo el alias para WordPress.
- Se ha añadido un bloque `location /assets` con una directiva `alias` para servir correctamente los recursos compartidos (CSS).
- Se ha activado el nuevo sitio y desactivado el sitio por defecto de Nginx.

**Detalle técnico:** Se creó el archivo `/etc/nginx/sites-available/mercedev-local` y se enlazó simbólicamente a `/etc/nginx/sites-enabled/`. Se verificó la sintaxis con `sudo nginx -t` y se recargó el servicio con `sudo systemctl reload nginx`. Se instruyó sobre cómo verificar la versión del socket de PHP-FPM en `/run/php/`.

**Motivo / criterio:** Es imprescindible que el entorno de desarrollo local simule fielmente la configuración de producción. La configuración de Nginx es el componente clave que une el núcleo estático y el CMS dinámico, permitiendo probar y validar la arquitectura de aislamiento antes del despliegue.

**Siguiente paso o deuda:** Configurar el archivo `wp-config.php` de WordPress y ejecutar el instalador web para finalizar la instalación.

### 2026-04-16 — Fase 4.0: Creación de base de datos y usuario para WordPress local

**Contexto:** Crear el esquema de base de datos y el usuario dedicado para la instancia local de WordPress, aislando sus datos del resto del sistema.

**Hecho:**
- Se ha accedido a MariaDB con `sudo mysql`.
- Se ha creado la base de datos `wp_mercedev_local` y el usuario `wp_user_local`.

**Detalle técnico:** Se ejecutaron las siguientes sentencias SQL:
```sql
CREATE DATABASE wp_mercedev_local;
CREATE USER 'wp_user_local'@'localhost' IDENTIFIED BY 'tu_contraseña_elegida';
GRANT ALL PRIVILEGES ON wp_mercedev_local.* TO 'wp_user_local'@'localhost';
FLUSH PRIVILEGES;
```
**Motivo / criterio:** El uso de una base de datos y un usuario específicos para cada aplicación es una práctica de seguridad fundamental (principio de mínimo privilegio), incluso en un entorno de desarrollo local.

**Siguiente paso o deuda:** Configurar el bloque de servidor de Nginx para el enrutamiento del núcleo estático y el proxy inverso hacia WordPress.

### 2026-04-16 — Fase 4.0: Instalación de pila LEMP y configuración base de datos local

**Contexto:** Preparación del entorno de desarrollo local anfitrión con Nginx, MariaDB y PHP para albergar la instancia aislada de WordPress, replicando la arquitectura de producción de forma nativa.

**Hecho:**
- Se han instalado los paquetes de la pila LEMP (`nginx`, `mariadb-server`, `php-fpm`, `php-mysql`).
- Se ha asegurado la instalación local de MariaDB estableciendo contraseña root y eliminando usuarios anónimos.

**Detalle técnico:** Se utilizó `sudo apt install` para la provisión de dependencias y `sudo mysql_secure_installation` con autenticación `unix_socket` activada para endurecer el motor de base de datos local.

**Motivo / criterio:** La dependencia de herramientas preempaquetadas (como LocalWP) ofusca la configuración del servidor web, impidiendo auditar y replicar la estrategia de enrutamiento inverso (reverse proxy) de Nginx definida en la Fase 4.1.

**Siguiente paso o deuda:** Crear la base de datos específica para WordPress local, descargar el CMS y configurar el bloque de servidor en Nginx.

### 2026-04-16 — Reajuste de entorno: De servidor a PC local y actualización de directrices

**Contexto:** Confusión entre el entorno de producción (droplet de DigitalOcean) y el entorno de desarrollo (PC local con Ubuntu). Se intentaba configurar bases de datos para el despliegue final cuando el entorno local aún no disponía de la pila tecnológica necesaria para probar la arquitectura aislada.

**Hecho:**
- Se ha añadido la regla 13 a `instrucciones.md` para forzar la verificación de dependencias de entorno antes de avanzar en la configuración.
- Se ha introducido la subfase 4.0 en el `README.md` para formalizar la preparación del entorno local LEMP.

**Detalle técnico:** La configuración local requiere replicar el ecosistema de producción (Linux, Nginx, MariaDB, PHP-FPM) nativamente en el sistema operativo anfitrión (`~/Escritorio/`) para validar el enrutamiento inverso de Nginx sin depender de herramientas aisladas como LocalWP que ofuscan la configuración del servidor.

**Motivo / criterio:** DevSecOps y "Shift-Left" requieren que el entorno de desarrollo local sea una réplica fiel de la arquitectura de producción. No se puede auditar ni endurecer un CMS localmente sin las herramientas nativas.

**Siguiente paso o deuda:** Iniciar la Fase 4.0 instalando Nginx, MariaDB y PHP nativos en el Ubuntu local.

### 2026-04-16 — Fase 5.2: Instalación de la infraestructura de base de datos (MariaDB)

**Contexto:** Al intentar crear la base de datos para WordPress, se detectó que no había ningún servidor de bases de datos instalado en el droplet (error `mysql: orden no encontrada`).

**Hecho:**
- Se ha instalado el servidor de bases de datos MariaDB, el sustituto directo y recomendado de MySQL en Ubuntu.
- Se ha ejecutado el script `mysql_secure_installation` para aplicar un endurecimiento de seguridad inicial.

**Detalle técnico:** Se utilizaron los comandos `sudo apt update`, `sudo apt install mariadb-server` y `sudo mysql_secure_installation`. Se configuró la autenticación `unix_socket` para el usuario root y se eliminaron las configuraciones inseguras por defecto.

**Motivo / criterio:** WordPress requiere una base de datos para funcionar. MariaDB es el estándar de la industria para este stack tecnológico. Asegurar la instalación desde el inicio es un paso fundamental de la filosofía "Shift-Left Security".

**Siguiente paso o deuda:** Proceder con la creación de la base de datos y el usuario específicos para la instancia de WordPress.

### 2026-04-15 — Incorporación de regla de sincronización del Roadmap

**Contexto:** Evitar la desincronización entre el código implementado y el estado de las fases documentadas en el proyecto.

**Hecho:**
- Añadir la regla 12 en `instrucciones.md` que obliga a actualizar el `README.md` inmediatamente tras finalizar una tarea.

**Detalle técnico:** Se formaliza la práctica de marcar con `- [x]` los hitos del `README.md` en la misma sesión de trabajo en la que se consigue el avance.

**Motivo / criterio:** Mantener una única fuente de verdad (Single Source of Truth) del estado del proyecto. Al estar documentada, el asistente de IA asimila la directriz de proponer la actualización automáticamente.

**Siguiente paso o deuda:** Finalizar sesión y retomar mañana con la Fase 5.2 (Permisos del servidor de WordPress).

### 2026-04-15 — Incorporación de Conventional Commits a las directrices

**Contexto:** Necesidad de estandarizar la nomenclatura de los mensajes de commit (especialmente en parches manuales) para mantener un historial de Git semántico y fácil de auditar.

**Hecho:**
- Añadir la regla 11 sobre la convención de prefijos en `instrucciones.md`.

**Detalle técnico:** Se definen los prefijos estándar de la industria (`feat:`, `fix:`, `chore:`, `docs:`, `refactor:`, `perf:`, `test:`, `style:`) como parte inmutable de las directrices del repositorio.

**Motivo / criterio:** La claridad en el control de versiones permite comprender el propósito de cualquier cambio de un solo vistazo. Es un paso clave de madurez DevSecOps que facilitará escalar o retomar el código en el futuro sin fricción.

**Siguiente paso o deuda:** Iniciar la auditoría de permisos del servidor para WordPress (Fase 5.2).

### 2026-04-15 — Soporte para commits menores manuales en merci-commit

**Contexto:** Tareas menores de mantenimiento (como eliminación de duplicados) no ameritan entradas completas en la bitácora, pero la herramienta `merci-commit.py` bloqueaba la acción o duplicaba mensajes forzando una fricción innecesaria.

**Hecho:**
- Añadir comprobación `check_repo_changes` para abortar tempranamente si no hay modificaciones reales en Git.
- Permitir el ingreso de un mensaje manual por terminal si hay cambios de código pero la bitácora está intacta.

**Detalle técnico:** Se implementa `git status --porcelain` para comprobar el estado real de los archivos. Si existen cambios pero no en `bitacora-mercedev.md`, se solicita confirmación para un parche menor y se captura el título vía `input()` de Python, saltándose la extracción de la bitácora.

**Motivo / criterio:** Equilibrio entre DevSecOps y usabilidad (DX). Ofrecer una válvula de escape estructurada para mantenimientos menores mantiene el historial limpio, no desincentiva el uso de la herramienta y agiliza al desarrollador.

**Siguiente paso o deuda:** Validar este nuevo flujo mixto y auditar los permisos del servidor de WordPress (Fase 5.2).

### 2026-04-15 — Endurecimiento (Hardening) de WordPress mediante Child Theme

**Contexto:** Reducir la superficie de ataque del CMS desactivando endpoints obsoletos y evitando fugas de información que faciliten intrusiones.

**Hecho:**
- Añadir reglas de seguridad (Fase 5.2) en `src/wp-theme/merci-theme/functions.php`.
- Actualizar checklist del `README.md`.

**Detalle técnico:** Se usa `remove_action` para eliminar el metadato generador de versión, `wlwmanifest` y `rsd_link`. Se desactiva completamente la API (Application Programming Interface - Interfaz de Programación de Aplicaciones) XML-RPC mediante el filtro `xmlrpc_enabled` para prevenir ataques de fuerza bruta. Se ofuscan los errores de autenticación con `login_errors`.

**Motivo / criterio:** Principio de mínima exposición. XML-RPC es un vector común para ataques DDoS (Distributed Denial of Service - Ataque Distribuido de Denegación de Servicio). Ocultar la versión exacta de WP dificulta el escaneo automatizado de vulnerabilidades conocidas.

**Siguiente paso o deuda:** Auditar la configuración de `wp-config.php` y los permisos del servidor para completar el hardening.

### 2026-04-15 — Resolución de 404 por favicon ausente (Higiene de logs)

**Contexto:** Durante la prueba del servidor local, el registro mostró un error 404 persistente al intentar cargar `favicon.ico`.

**Hecho:**
- Añadir `<link rel="icon" href="data:,">` en el `<head>` de `public/index.html`.

**Detalle técnico:** Los navegadores solicitan automáticamente `/favicon.ico` a la raíz del servidor web. Al no existir el archivo, se genera una petición HTTP (Hypertext Transfer Protocol - Protocolo de Transferencia de Hipertexto) fallida. Se inyecta un URI (Uniform Resource Identifier - Identificador de Recursos Uniforme) de datos vacío para cancelar la petición de red en origen.

**Motivo / criterio:** Rendimiento e higiene del servidor. Un error 404 consume procesamiento innecesario. Un Data URI vacío silencia el comportamiento automático del navegador manteniendo la política de cero dependencias externas.

**Siguiente paso o deuda:** Diseñar el isotipo definitivo para el favicon en fases posteriores. Continuar con el Hardening de WordPress (Fase 5.2).

### 2026-04-15 — Validación local de Content Security Policy (CSP)

**Contexto:** Verificar empíricamente que la política de seguridad estricta no interfiere con la carga de los recursos legítimos del núcleo estático.

**Hecho:**
- Desplegar servidor local de pruebas (`python3 -m http.server 8000 -d public/`).
- Validar ausencia de bloqueos en la consola de herramientas para desarrolladores del navegador.

**Detalle técnico:** Al no poseer dependencias de terceros (como tipografías externas o analíticas), la regla `default-src 'self'` permite cargar correctamente el documento HTML y su hoja de estilos unificada. No se registran errores de tipo "CSP violation".

**Motivo / criterio:** En DevSecOps (Development, Security, and Operations - Desarrollo, Seguridad y Operaciones), la imposición de una política de seguridad siempre debe ir acompañada de una validación funcional para evitar degradación del servicio o bloqueos de UX (User Experience - Experiencia de Usuario).

**Siguiente paso o deuda:** Comenzar el Hardening de WordPress (Fase 5.2).

### 2026-04-15 — Fase 5: Implementación de Content Security Policy (CSP)

**Contexto:** Iniciar la fase de Hardening del núcleo estático protegiéndolo contra ataques de inyección de código.

**Hecho:**
- Añadir directiva CSP (Content Security Policy - Política de Seguridad de Contenidos) en el `<head>` de `public/index.html`.

**Detalle técnico:** Se establece una política estricta mediante etiqueta `<meta>`: `default-src 'self'` restringe todos los recursos al dominio actual. Se bloquean plugins (`object-src 'none'`) y la inyección de bases (`base-uri 'self'`).

**Motivo / criterio:** Aplicación del principio de seguridad "Shift-Left". Una CSP estricta mitiga el riesgo de vulnerabilidades XSS (Cross-Site Scripting - Secuencias de Comandos en Sitios Cruzados) prohibiendo scripts externos o en línea no autorizados.

**Siguiente paso o deuda:** Validar la carga de la portada en el navegador local para confirmar que la política no bloquea assets legítimos y avanzar con el Hardening de WordPress.

### 2026-04-15 — Refinamiento de la política de acrónimos (Linter y directrices)

**Contexto:** La regla estricta de expandir siempre los acrónimos (Inglés - Español) resultaba tediosa para términos que ya estaban muy arraigados en el proyecto.

**Hecho:**
- Actualizar `instrucciones.md` eximiendo de expansión a los acrónimos que aparezcan más de 3 veces.
- Implementar una función de conteo global (`get_global_acronym_count`) en `merci-audit.py`.

**Detalle técnico:** El auditor ahora escanea todo el repositorio buscando archivos `.md`. Si localiza un acrónimo de la *watchlist* que no está expandido, verifica su conteo global. Si es mayor a 3, asume que es un término consolidado y omite la advertencia `WARN MD_ACRONYM`. Se emplea un caché (`GLOBAL_ACRONYM_COUNTS`) para evitar leer el disco repetidas veces.

**Motivo / criterio:** Reducir la fricción y el tedio en el flujo DevSecOps. Se equilibra la necesidad de claridad técnica inicial con la fluidez una vez que un concepto ya es de dominio público en el repositorio.

**Siguiente paso o deuda:** Comitear los cambios del linter y comenzar oficialmente la Fase 5: Quality Assurance y Hardening.

### 2026-04-15 — Validación exitosa del linter de acrónimos

**Contexto:** El nuevo linter de acrónimos detectó correctamente la falta de expansión de "CMS" durante la ejecución de un commit rutinario, validando su eficacia.

**Hecho:**
- Expandir el acrónimo CMS (Content Management System - Sistema de Gestión de Contenidos) en el registro histórico.
- Confirmar el funcionamiento de la regla `WARN` en `merci-audit.py`.

**Detalle técnico:** El auditor emitió la advertencia `WARN MD_ACRONYM` indicando la línea exacta sin bloquear la creación del commit atómico. Esto permitió mantener la fluidez del proceso informando simultáneamente sobre la deuda técnica de redacción.

**Motivo / criterio:** Dejar constancia de que el sistema de vigilancia pasiva (Watchlist) cumple su función como corrector de estilo automatizado (DevSecOps) sin añadir fricción paralizante.

**Siguiente paso o deuda:** Iniciar la Fase 5: Quality Assurance y Hardening.

### 2026-04-15 — Implementación de linter de acrónimos en Merci Audit

**Contexto:** Automatizar la verificación de la regla de estilo que exige expandir los acrónimos técnicos en la bitácora y la documentación (Inglés - Español).

**Hecho:**
- Crear la función `audit_md_acronyms` en `scripts/merci/merci-audit.py`.
- Definir una lista de vigilancia (*watchlist*) para los acrónimos más críticos.

**Detalle técnico:** La función utiliza expresiones regulares para detectar si un acrónimo de la lista está presente en archivos `.md`. Si lo encuentra, verifica que exista al menos una instancia con el patrón `ACRÓNIMO (...)` en el documento. Se clasifica como `warn` para no bloquear commits por falsos positivos.

**Motivo / criterio:** Reducir la carga cognitiva de revisión manual. La automatización parcial mediante *watchlist* es más fiable que una expresión regular genérica para mayúsculas, la cual generaría excesivos falsos positivos.

**Siguiente paso o deuda:** Validar el comportamiento del auditor con un commit y avanzar a la Fase 5: Quality Assurance y Hardening.

### 2026-04-15 — Análisis de impacto de wc-cart-fragments (Deuda de conocimiento)

**Contexto:** Comprensión arquitectónica de los motivos por los que el script `wc-cart-fragments` de WooCommerce degrada el rendimiento web estándar.

**Hecho:**
- Documentar el comportamiento del script AJAX (Asynchronous JavaScript and XML - JavaScript Asíncrono y XML) de fragmentos de carrito.

**Detalle técnico:** El script invoca una petición `POST` a `/?wc-ajax=get_refreshed_fragments` en cada carga de página. Al ser un `POST` que verifica sesiones y bases de datos mediante PHP (Hypertext Preprocessor - Preprocesador de Hipertexto), esquiva las capas de caché estáticas (Varnish, Redis, Nginx FastCGI) elevando drásticamente el consumo de CPU (Central Processing Unit - Unidad Central de Procesamiento) y el TTFB (Time to First Byte - Tiempo hasta el Primer Byte).

**Motivo / criterio:** Dejar constancia del motivo de su desencolado en la Fase 4.3. En arquitecturas en Modo Catálogo, este script aporta 0 funcionalidad a costa de sacrificar métricas críticas de Core Web Vitals como el INP (Interaction to Next Paint - Interacción hasta el Siguiente Pintado).

**Siguiente paso o deuda:** Consolidar el documento en Git e iniciar la Fase 5: Quality Assurance y Hardening.

### 2026-04-15 — Fase 4.3: Configuración de WooCommerce en modo catálogo

**Contexto:** Integrar WooCommerce para mostrar el merchandising de Merci sin el impacto de rendimiento que supone una tienda completa con pasarelas de pago y scripts de carrito AJAX (Asynchronous JavaScript and XML - JavaScript Asíncrono y XML).

**Hecho:**
- Añadir soporte de WooCommerce al `functions.php` del Child Theme.
- Eliminar las acciones de añadir al carrito (`remove_action`).
- Desencolar el script `wc-cart-fragments`.

**Detalle técnico:** Se usa `add_theme_support('woocommerce')` para habilitar las plantillas base. Se bloquea la generación de botones de compra anulando `woocommerce_template_loop_add_to_cart` y `woocommerce_template_single_add_to_cart`. El script de fragmentos de carrito se desencola con prioridad 100.

**Motivo / criterio:** Rendimiento puro. WooCommerce inyecta JS (JavaScript) pesado por defecto para gestionar el carrito en tiempo real en todas las páginas. Al funcionar como mero catálogo, prescindimos de esta carga protegiendo el Web Vitals score.

**Siguiente paso o deuda:** Validar la visualización del catálogo e iniciar la fase de endurecimiento y QA (Fase 5).

### 2026-04-15 — Corrección de importación en pruebas (test_sitemap.py)

**Contexto:** El archivo de pruebas `test_sitemap.py` quedó roto tras estandarizar el nombre del script principal a `merci-sitemap.py` (con guion medio). Python no permite importar módulos con guiones usando la sintaxis estándar de `import`.

**Hecho:**
- Refactorizar `scripts/merci/tests/test_sitemap.py`.
- Implementar carga dinámica de módulos con `importlib.util`.

**Detalle técnico:** Se reemplazó el `sys.path.append` por `spec_from_file_location` y `module_from_spec` de `importlib.util`. Esto permite cargar el archivo `merci-sitemap.py` asociándolo al namespace interno seguro `merci_sitemap` para el parcheo con `unittest.mock`.

**Motivo / criterio:** Mantener la convención de nombres de archivos con guiones en el sistema (ej. `merci-audit.py`, `merci-sitemap.py`) sin sacrificar la cobertura de las pruebas unitarias.

**Siguiente paso o deuda:** Ejecutar los tests para validar el fix y consolidar los cambios con `merci-commit`.

### 2026-04-15 — Creación de index.php del Child Theme con metodología BEM

**Contexto:** Proveer una plantilla base para que WordPress renderice contenido dinámico respetando el estándar HTML5 y las clases CSS del núcleo estático.

**Hecho:**
- Crear `src/wp-theme/merci-theme/index.php`.
- Implementar "The Loop" de WordPress en una estructura unificada.

**Detalle técnico:** Se prescinde de la fragmentación tradicional (`get_header()`, `get_footer()`) para concentrar el marcado en un solo archivo. Se incluyen `wp_head()` y `wp_footer()` para permitir la inyección de nuestros assets estáticos controlados. Se aplican clases BEM (`article`, `article__title`, `article__content`).

**Motivo / criterio:** Minimalismo extremo y reducción de carga de procesamiento I/O de PHP. Al escribir el HTML directamente, se evita que WordPress genere contenedores `<div>` basura o estructuras que rompan el diseño semántico del núcleo.

**Siguiente paso o deuda:** Validar la vista dinámica y proceder con la configuración de WooCommerce en modo catálogo (Fase 4.3).

### 2026-04-15 — Creación de functions.php como escudo de rendimiento

**Contexto:** Necesidad de bloquear la inyección de código basura por defecto de WordPress (scripts de emojis, estilos globales, CSS de Gutenberg) para proteger el rendimiento del frontend.

**Hecho:**
- Crear `src/wp-theme/merci-theme/functions.php`.
- Implementar reglas de limpieza y desencolado (`dequeue`).

**Detalle técnico:** Se emplea `remove_action` para detener los scripts de emojis y `wp_dequeue_style` enganchado a la acción `wp_enqueue_scripts` (con prioridad 100) para bloquear `wp-block-library` y `global-styles`. Finalmente, se encola `/assets/main.css` apuntando a la ruta absoluta expuesta por Nginx.

**Motivo / criterio:** Aislar la vista dinámica del CMS de sus dependencias heredadas pesadas. Si no se bloquea, WordPress inyecta múltiples llamadas de red y estilos en línea que degradarían la métrica de Core Web Vitals lograda en el núcleo estático.
**Motivo / criterio:** Aislar la vista dinámica del CMS (Content Management System - Sistema de Gestión de Contenidos) de sus dependencias heredadas pesadas. Si no se bloquea, WordPress inyecta múltiples llamadas de red y estilos en línea que degradarían la métrica de Core Web Vitals lograda en el núcleo estático.

**Siguiente paso o deuda:** Desarrollar `index.php` del tema para renderizar el esqueleto HTML5 alineado con la metodología BEM del proyecto.

### 2026-04-15 — Añadir salvaguarda a merci-commit.py contra commits sin bitácora

**Contexto:** Evitar la creación de commits duplicados o la omisión de la actualización de la bitácora, que son riesgos inherentes a un flujo de trabajo automatizado.

**Hecho:**
- Modificar `scripts/merci/merci-commit.py` para añadir una verificación previa.

**Detalle técnico:**
- El script ahora ejecuta `git diff --quiet HEAD -- <ruta_bitacora>` antes de proceder.
- Si el comando devuelve un código de salida 0 (sin cambios), se emite una alerta en la terminal y se solicita confirmación explícita del usuario para continuar.

**Motivo / criterio:** Reforzar la disciplina de "documentación primero" y prevenir el ruido en el historial de Git. La confirmación del usuario mantiene la flexibilidad para casos excepcionales sin sacrificar la seguridad del flujo por defecto.

**Siguiente paso o deuda:** Retomar el desarrollo del `functions.php` del Child Theme (Fase 4.2).

### 2026-04-15 — Configuración de alias de terminal (zsh) para el Sistema Merci

**Contexto:** Necesidad de optimizar la experiencia de desarrollo (DX) y reducir la fricción al invocar los scripts de automatización desde distintas ubicaciones del proyecto.

**Hecho:**
- Recapitular y definir bloque de alias en `~/.zshrc` para las herramientas base: `merci-audit`, `merci-styles`, `merci-optimizer` y el nuevo `merci-commit`.

**Detalle técnico:** Se emplea la variable estática `MERCI_ROOT` apuntando a `/home/hildegahr/Escritorio/PROYECTO_mercedev.es` para garantizar la resolución de rutas absolutas al invocar Python, sin importar el directorio de trabajo actual (`pwd`).

**Motivo / criterio:** La carga cognitiva de recordar y tipear rutas relativas largas desincentiva el uso frecuente de herramientas críticas (como la auditoría o los commits atómicos). Abstraer esto en la terminal refuerza el flujo DevSecOps.

**Siguiente paso o deuda:** Validar la usabilidad del flujo con `merci-commit` y arrancar el código del `functions.php` del Child Theme (Fase 4.2).

### 2026-04-15 — Refactorización de merci-commit.py (Auto-Stage)

**Contexto:** El script de automatización de commits no incluía los archivos modificados del código, limitándose a comitear únicamente la bitácora.

**Hecho:**
- Modificar `scripts/merci/merci-commit.py` para ejecutar `git add .` en la raíz del repositorio antes del commit.

**Detalle técnico:**
- Se utiliza el argumento `cwd=REPO_ROOT` en `subprocess.run` para asegurar que el comando `git add .` abarque todo el proyecto, independientemente de desde dónde se invoque el script.

**Motivo / criterio:** Agilizar el flujo de trabajo. La seguridad y prevención de adición de código basura (secretos, archivos pesados) queda delegada a la red de seguridad del pre-commit (`merci-audit.py` y `.gitignore`), manteniendo la arquitectura "Shift-Left" intacta.

**Siguiente paso o deuda:** Validar la automatización y retomar el `functions.php` del Child Theme (Fase 4.2).

### 2026-04-15 — Pausa de Fase 4.2 para automatización de commits (I+D)

**Contexto:** Necesidad de vincular estrechamente la actualización de la bitácora con el historial de Git para evitar desincronización entre documentación y código.

**Hecho:**
- Pausar temporalmente el desarrollo del `functions.php` del Child Theme.
- Diseñar conceptualmente una herramienta de automatización para commits impulsados por la bitácora.

**Detalle técnico:** Se descarta el "auto-commit al guardar" (file watcher) por generar ruido (commit spam) y romper la atomicidad de Git. Se opta por crear un extractor que utilice la última entrada redactada como mensaje estructurado del commit.

**Motivo / criterio:** Mantener un historial de Git semántico, asegurando que el código modificado y su justificación (bitácora) viajen siempre juntos en un único commit atómico.

**Siguiente paso o deuda:** Desarrollar `scripts/merci/merci-commit.py` e integrarlo en el flujo de trabajo local.

### 2026-04-15 — Iniciar Fase 4.2 y creación base del Child Theme

**Contexto:** Iniciar el desarrollo del tema hijo ultraligero para WordPress (Fase 4.2), asegurando cero dependencias externas y preparando el enlace con el núcleo estático.

**Hecho:**
- Crear directorio `src/wp-theme/merci-theme/`.
- Crear archivo manifiesto `style.css`.

**Detalle técnico:** El archivo `style.css` contiene exclusivamente la cabecera de comentarios (`Theme Name`, `Version`, etc.) requerida por WP para reconocer el tema en el panel de administración. No incluye directivas de diseño.

**Motivo / criterio:** Evitar la duplicidad de renderizado y el código basura de los temas por defecto. El diseño real se delegará al `main.css` del núcleo estático para proteger la métrica de rendimiento (Core Web Vitals).

**Siguiente paso o deuda:** Crear el archivo `functions.php` como escudo para bloquear los scripts y estilos inyectados por defecto por WordPress.

### 2026-04-15 — Definir Arquitectura de Aislamiento de WordPress (Fase 4.1)

**Contexto:** Integrar WordPress para `/blog` y `/tienda` sin comprometer la seguridad, inmutabilidad y rendimiento puro originado en el núcleo estático de la carpeta `public/`.

**Hecho:**
- Crear el documento técnico `docs/integracion-wordpress.md`.
- Definir el enrutamiento proxy inverso mediante **Nginx**.
- Configurar de forma teórica la preservación de canónicas (`siteurl` bloqueado a su subdirectorio) y `sitemap_index.xml`.

**Detalle técnico:**
- Plantear una estructura de "Common root": `public/` alberga estáticos, mientras que el CMS reside en otra ruta del sistema anfitrión (ej. `/var/www/wordpress/`). Unir ambos mundos transparentemente usando la directiva `location ^~ /blog`.
- Restringir estrictamente permisos: el proceso PHP de WordPress nunca podrá escribir en `public/`.

**Motivo / criterio:** Aislar vectores de ataque del CMS. Si el CMS es vulnerado (plugins desactualizados), el Frontend estático queda ileso. Además, se evita degradar el Web Vitals score de la portada sirviendo estáticos directamente con el web server.

**Siguiente paso o deuda:** Iniciar la Fase 4.2 que consiste en desarrollar el "Child Theme ultraligero" para el ecosistema de WordPress aislado.


### 2026-04-15 — Refactorización para resolver descoordinación de archivos

**Contexto:** Conflicto de convenciones de nombres y pérdida de coordinación de los scripts locales (`merci_sitemap.py` vs `merci-sitemap.py`) y pérdida de la compilación CSS (`main.scss`).

**Hecho:**
- Restaurar explícitamente `@use 'index';` en `src/scss/main.scss` garantizando compilación exitosa a `public/css/main.css`.
- Traspasar duplicidades experimentales (`merci_ingestor.py`, `merci_sitemap.py`, `pre-commit.sh`) a `laboratorio/scripts_temporales/` para mantener limpio el entorno y respetar la no eliminación de código.
- Restaurar el script `scripts/merci/pre-commit` con la llamada correcta a `merci-sitemap.py`.
- Actualizar el `README.md` para asentar todos los apuntes con las rutas veraces.

**Detalle técnico:**
- Se confirma visualmente la reaparición de `main.css`.
- Se limpia la carpeta `scripts/merci/` manteniéndola con `-` en lugar de `_` como convención primaria.
- Movimiento realizado: `mv scripts/merci/merci_ingestor.py scripts/merci/merci_sitemap.py scripts/merci/pre-commit.sh laboratorio/scripts_temporales/`

**Motivo / criterio:** Consistencia y correspondencia con "lo que existe". Todo el proyecto ya está nuevamente compilando y acoplado.

**Siguiente paso o deuda:** Ninguno, el lío de archivos quedó resuelto.


### 2026-04-15 — Restauración integral de archivos y estabilización modular

**Contexto:** Pérdida de contenido en archivos tras renombrados y reorganización de carpetas.

**Hecho:**
- Reconstruir `public/robots.txt` y `public/sitemap.xml`.
- Restaurar `merci_ingestor.py` y el arnés de pruebas en `/tests`.
- Preservar el experimento de grabación en `/laboratorio/art-de-cote`.

**Detalle técnico:**
- Se asegura que los scripts utilicen nombres de archivo con guion bajo (`merci_sitemap.py`) para ser importables.
- Los archivos pesados de vídeo permanecen excluidos en `.gitignore`.

**Motivo / criterio:** Garantizar la integridad del repositorio antes de avanzar a la Fase 3.

**Siguiente paso o deuda:** Iniciar el desarrollo de estilos SASS.

### 2026-04-15 — Reorganización modular de la carpeta Merci

**Contexto:** Evitar la dispersión de archivos en la carpeta de automatización separando los scripts operativos de las pruebas y los experimentos.

**Hecho:**
- Creación de las subcarpetas `tests/` y `experimental/` en `scripts/merci/`.
- Reubicación de `test_sitemap.py` y el aviso de deprecación de `merci-recorder.py`.

**Detalle técnico:**
- Ajuste de `sys.path` en los tests para localizar módulos en el directorio padre (`parents[1]`).

**Motivo / criterio:** Modularidad y limpieza. Mantener la carpeta raíz de Merci enfocada únicamente en scripts productivos y validados.

**Siguiente paso o deuda:** Migrar futuros tests a la nueva carpeta y mover scripts en desarrollo a la zona experimental.

### 2026-04-15 — Preservación de Merci Recorder como pieza de Art de Coté

**Contexto:** Aplicación de la filosofía del proyecto para no descartar código experimental valioso tras el cambio de estrategia hacia el Ingestor.

**Hecho:**
- Trasladar la lógica funcional de grabación a `laboratorio/art-de-cote/recorder_experiment.py`.
- Mantener `scripts/merci/merci-recorder.py` como un stub de aviso (deprecación).

**Detalle técnico:**
- La lógica preservada incluye la corrección del flag `-nostdin` y el uso de `x11grab` (X Window System - Sistema de Ventanas X).
- Se categoriza como "Artefacto de Laboratorio" para consulta futura.

**Motivo / criterio:** El script falló para el flujo de producción diario pero es un activo de conocimiento sobre automatización multimedia con Python y FFmpeg.

**Siguiente paso o deuda:** Validar el funcionamiento del Ingestor en una sesión real.

### 2026-04-15 — Cambio de estrategia: Ingesta de evidencias en lugar de grabación directa

**Contexto:** El script `merci-recorder.py` no funcionaba correctamente y la necesidad de gestionar evidencias existentes (capturas de pantalla, vídeos) de forma más flexible.

**Hecho:**
- Deprecación de `scripts/merci/merci-recorder.py`.
- Creación de `scripts/merci/merci_ingestor.py` para escanear carpetas de usuario y mover archivos recientes a `.assets-raw/`.
- Actualización de `README.md` e `instrucciones.md` para reflejar la nueva estrategia.

**Detalle técnico:**
- `merci_ingestor.py` busca archivos modificados en los últimos 30 minutos en `~/Pictures`, `~/Videos`, `~/Desktop` (configurable).
- Ofrece al usuario la opción de mover todos, algunos o ninguno de los archivos encontrados a `.assets-raw/`.

**Motivo / criterio:** Priorizar la funcionalidad de ingesta de evidencias existentes, que es más robusta y menos propensa a problemas de entorno que la grabación en tiempo real, y alinear con la gestión de `.assets-raw/`.

**Siguiente paso o deuda:** Probar `merci_ingestor.py` con archivos de prueba y documentar su uso en el `README.md`.

### 2026-04-15 — Resolución definitiva para visualización de vídeos de evidencias

**Contexto:** Fallo persistente en la instalación de extensiones de vídeo en VS Code, incluso usando el CLI y IDs de extensiones válidos.

**Hecho:**
- Confirmar que la instalación de `b-ryan.vscode-video` vía CLI también falla.
- Decidir utilizar reproductores externos (sistema o navegador web) para visualizar los archivos `.mp4` de `laboratorio/evidencias/`.

**Detalle técnico:**
- El problema parece ser una limitación del entorno de VS Code o su acceso al Marketplace, no de la existencia de las extensiones.
- La visualización externa es una solución robusta que no bloquea el flujo de trabajo.

**Motivo / criterio:** Priorizar el avance del proyecto y la generación de evidencias sobre la resolución de un problema de configuración del IDE que consume tiempo.

**Siguiente paso o deuda:** Iniciar la grabación de 30 minutos y proceder con la Fase 3 (Ingeniería de Estilos).

### 2026-04-15 — Incidencia persistente con el Marketplace de VS Code

**Contexto:** No es posible localizar extensiones de vídeo por ID en el Marketplace de la instancia local de VS Code.

**Hecho:**
- Intentar instalación de `moshfeu.video-player` y `frenco.vs-code-media-preview` sin éxito.
- Proponer instalación vía **CLI** (Command Line Interface - Interfaz de Línea de Comandos) de la extensión `b-ryan.vscode-video`.

**Detalle técnico:**
- Comando de rescate: `code --install-extension b-ryan.vscode-video`.
- Alternativa de visualización: uso del navegador host para validar evidencias MP4 si falla el IDE.

**Motivo / criterio:** Evitar la dispersión en problemas de configuración del entorno y priorizar el avance hacia la Fase 3 del Roadmap.

**Siguiente paso o deuda:** Validar visualización de la primera sesión de 30 min y proceder con SASS.

### 2026-04-15 — Clarificación sobre la extensión de visualización de video

**Contexto:** Dificultad para localizar la extensión "Video Player" (`moshfeu.video-player`) en el Marketplace de VS Code.

**Hecho:**
- Reconfirmar la existencia y disponibilidad de la extensión.
- Proporcionar instrucciones precisas para la búsqueda por ID (`moshfeu.video-player`).

**Detalle técnico:**
- La búsqueda por ID es más robusta que por nombre, evitando ambigüedades o errores de tipografía.

**Motivo / criterio:** Asegurar que el desarrollador pueda instalar la herramienta necesaria para revisar las evidencias de video sin interrupciones.

**Siguiente paso o deuda:** Confirmar la instalación y reproducción de un video de prueba.

### 2026-04-15 — Corrección de herramienta: Extensión de visualización de video

**Contexto:** La extensión recomendada anteriormente (`frenco.vs-code-media-preview`) no se encuentra disponible en el Marketplace.

**Hecho:** Sustituir la recomendación por la extensión "Video Player" de moshfeu (`moshfeu.video-player`).

**Detalle técnico:**
- La nueva extensión permite la previsualización de archivos `.mp4` y `.webm` directamente en el **IDE** (Integrated Development Environment - Entorno de Desarrollo Integrado).

**Motivo / criterio:** Garantizar que el flujo de revisión de evidencias en el laboratorio sea funcional con herramientas existentes y verificadas.

**Siguiente paso o deuda:** Validar la apertura de un vídeo de sesión de 30 minutos con esta nueva extensión.

### 2026-04-15 — Instalación de extensión para visualización de evidencias

**Contexto:** Necesidad de revisar los vídeos generados por `merci-recorder.py` sin romper el flujo de trabajo saliendo del editor.

**Hecho:** Seleccionar e instalar la extensión Media Preview (`frenco.vs-code-media-preview`).

**Detalle técnico:**
- La extensión permite renderizar binarios de vídeo y audio en pestañas del **IDE** (Integrated Development Environment - Entorno de Desarrollo Integrado).

**Motivo / criterio:** Mantener la concentración en el entorno de desarrollo y facilitar la validación rápida de las capturas de pantalla antes de documentar en la bitácora.

**Siguiente paso o deuda:** Iniciar la grabación de 30 minutos y verificar la reproducción fluida dentro del editor.

### 2026-04-15 — Validación final y mejora de Merci Recorder

**Contexto:** Realizar prueba de humo del grabador y mejorar la flexibilidad para pruebas cortas.

**Hecho:**
- Añadir soporte para argumentos de duración en `merci-recorder.py`.
- Ejecutar prueba de 10 segundos exitosamente.

**Detalle técnico:**
- Uso de `argparse` para parametrizar la duración.
- Confirmación de que el flag `-nostdin` evita colisiones con la entrada de terminal.
- Validación de `.gitignore`: los binarios generados no son trackeados por Git.

**Motivo / criterio:** Robustez y facilidad de prueba sin sacrificar la configuración por defecto de 30 min.

### 2026-04-15 — Corrección de error interactivo en Merci Recorder

**Contexto:** `ffmpeg` reportó un "Parse error" durante la grabación, causado por entrada inesperada del usuario en la terminal.

**Hecho:**
- Identificar la causa del error como interacción accidental con el modo interactivo de `ffmpeg`.
- Modificar `scripts/merci/merci-recorder.py` para añadir el flag `-nostdin`.

**Detalle técnico:**
- El flag `-nostdin` evita que `ffmpeg` intente leer de la entrada estándar, previniendo errores de parseo por comandos no intencionados.

**Motivo / criterio:** Mejorar la robustez del script y la experiencia de usuario, evitando interrupciones por entradas accidentales.

**Siguiente paso o deuda:** Validar el comportamiento del script con el nuevo flag.

### 2026-04-15 — Prueba de humo y validación de Merci Recorder

**Contexto:** Verificar que el script de captura de pantalla funciona correctamente y que la exclusión en Git es efectiva.

**Hecho:**
- Ejecución de prueba de `scripts/merci/merci-recorder.py`.
- Verificación de salida en `laboratorio/evidencias/`.

**Detalle técnico:**
- El script genera el contenedor `.mp4` usando el códec `libx264`.
- `git status` confirma que los binarios de vídeo son ignorados por el sistema de control de versiones.

**Motivo / criterio:** Garantizar la trazabilidad visual de las sesiones de 30 min sin comprometer el peso del repositorio remoto.

### 2026-04-15 — Implementación de infraestructura de pruebas (QA)

**Contexto:** Ausencia de validación automatizada para los scripts de automatización de Merci.

**Hecho:**
- Creación de `scripts/merci/test_sitemap.py`.
- Definición de estrategia de pruebas unitarias usando la librería estándar de Python.

**Detalle técnico:**
- Uso de `unittest.mock` para simular el sistema de archivos y evitar escrituras reales durante los tests.
- Implementación de **TDD** (Test Driven Development - Desarrollo Dirigido por Pruebas) incipiente para los scripts de sistema.

**Motivo / criterio:** Garantizar la integridad de los metadatos de indexación y la estabilidad de las herramientas de automatización antes de avanzar a fases de diseño visual.

**Siguiente paso o deuda:** Ampliar la cobertura de pruebas a `merci-audit.py`.

### 2026-04-15 — Consolidación del flujo de grabación y protección de repositorio

**Contexto:** Asegurar que el nuevo sistema de grabación no impacte el tamaño del repositorio remoto.

**Hecho:**
- Actualizar `.gitignore` para excluir binarios de vídeo en `laboratorio/evidencias/`.
- Validar la integración de `merci-recorder.py` como herramienta de trazabilidad local.

**Detalle técnico:**
- Adición de patrones `*.mp4` y `*.mov` específicos para la carpeta de evidencias.

**Motivo / criterio:** Autonomía en la captura de evidencias sin gestión manual de archivos externos, respetando la Regla 10 de austeridad en el repo remoto.

**Siguiente paso o deuda:** Iniciar la primera sesión de grabación de 30 minutos para validar el rendimiento del sistema.

### 2026-04-15 — Implementación de sistema de captura de vídeo (Merci Recorder)

**Contexto:** Necesidad de registrar sesiones de desarrollo de 30 minutos para trazabilidad del proceso en el Laboratorio.

**Hecho:**
- Crear `scripts/merci/merci-recorder.py`.
- Integrar lógica de captura automática de pantalla con FFmpeg.

**Detalle técnico:**
- Uso de `x11grab` para la **GUI** (Graphical User Interface - Interfaz Gráfica de Usuario).
- Configuración de duración fija a 1800 segundos (30 minutos).
- Codificación en tiempo real optimizada para baja carga de **CPU** (Central Processing Unit - Unidad Central de Procesamiento).

**Motivo / criterio:** Facilitar la generación de evidencias sin interrumpir el flujo de trabajo manual, manteniendo la coherencia con la Regla 10 de gestión de archivos pesados.

**Siguiente paso o deuda:** Validar el peso de los archivos generados y ajustar el **CRF** (Constant Rate Factor - Factor de Tasa Constante) si superan los 50MB por sesión.

### 2026-04-15 — Política de gestión de evidencias pesadas en el Laboratorio

**Contexto:** Necesidad de evitar el crecimiento excesivo del repositorio Git por la inclusión de vídeos y capturas de pantalla de gran tamaño.

**Hecho:**
- Definir regla de exclusión de binarios pesados en `laboratorio/evidencias/`.
- Actualizar `instrucciones.md` con la norma de "Evidencias Pesadas".

**Detalle técnico:**
- Se establece que `merci-optimizer.py` (o extensiones futuras) se encargará de reducir el material de pruebas antes de su clasificación.
- Los archivos originales (brutos) se mantienen en la carpeta externa de capturas o en `.assets-raw/evidencias/` (fuera de Git).

**Motivo / criterio:** Mantener un repositorio ligero y profesional, evitando el bloqueo por cuotas de GitHub y asegurando clones rápidos.

**Siguiente paso o deuda:** Configurar `.gitignore` para excluir extensiones de vídeo (`.mp4`, `.mov`) dentro de la carpeta de evidencias.

### 2026-04-15 — Pruebas de visualización en navegador e hitos UX/UI (Fase 2)

**Contexto:** Validar el renderizado real del `index.html` tras la aplicación de la jerarquía semántica y la estructura BEM.

**Hecho:**
- Generar informes PDF con capturas del sitio en navegador.
- Crear carpeta `laboratorio/evidencias/` para organizar los artefactos de prueba.

**Detalle técnico:** (Aquí puedes anotar si detectaste algún error de alineación, fuentes o comportamiento responsivo en el PDF).

**Motivo / criterio:** Evitar la dispersión de archivos en la raíz del laboratorio y asegurar que las decisiones de diseño tienen un respaldo visual documentado.

**Siguiente paso o deuda:** (Anotar si hay que retocar algún margen o color tras ver el PDF).

### 2026-04-15 — Refactorización a Módulos SASS y Dart Sass Standalone (Fase 3)

**Contexto:** Se identificó que la librería Python `libsass` no soportaba las directivas modulares (`@use`, `@forward`, `_index.scss`) que permiten una arquitectura de estilos moderna y desacoplada.

**Hecho:**
- Reconfiguración de `src/scss/` incluyendo archivos `_index.scss` que reexportan las partes.
- `main.scss` simplificado a sólo incluir los índices de cada subcarpeta.
- Eliminación de `libsass` de `requirements.txt`.
- Modificación estructural de `scripts/merci/merci-styles.py`: ya no es un script de Python que importe librerías, sino un autómata que descarga la release oficial del binario _Dart Sass_ para Linux, extrae el compilador localmente sin impactar el sistema operativo host, y procesa los estilos.

**Detalle técnico:**
- Almacenaje de los binarios locales de SASS en `scripts/merci/bin/dart-sass/sass`.
- Se llama al proceso aisladamente con `subprocess` de la librería estándar de Python.

**Motivo / criterio:**
- Dar soporte al mejor estilo posible de escritura SASS modular pero evadir a toda costa la necesidad de forzar la instalación global de Node.js o NPM para usar un compilador web, protegiendo así el Paradigma base de "0 dependencias externas host".

**Siguiente paso o deuda:** Validar rendimiento continuo del compilador e iniciar implementación de hojas visuales para nuevos componentes.
### 2026-04-15 — Implementación de la Fase 3: SASS, BEM y Merci Optimizer

**Contexto:** Desplegar el sistema de estilos escalable (SASS) y preparar la automatización para multimedia.

**Hecho:**
- Creación de la arquitectura 7-1 en `src/scss/` con punto de entrada único (`main.scss`).
- Refactorización de `public/index.html` asimilando la metodología BEM.
- Creación de dos piezas fundamentales para Merci: `merci-styles.py` (compilador con libsass) y `merci-optimizer.py` (escalado WebP con Pillow).
- `requirements.txt` ajustado para compilar localmente con Python.

**Detalle técnico:**
- `merci-styles.py` invoca a libsass asilando su función y ahorrando uso manual de consola.
- `.assets-raw/` será escrutado por Merci procesando imágenes WebP hacia `assets/` a medidas predeterminadas.

**Motivo / criterio:** Se eligió `libsass` de Python para unificar el DevSecOps de Merci sin depender de un entorno NodeJS global adicional en Ubuntu, en línea con la filosofía de austeridad tecnológica externa.

**Siguiente paso o deuda:** Validar la instalación con pip y hacer un chequeo de `index.html` estéticamente en navegador.
### 2026-04-14 — Validación de jerarquía de encabezados y landmarks (Fase 2.1)

**Contexto:** Asegurar la accesibilidad y la estructura semántica correcta en la página de inicio.

**Hecho:**
- Añadir encabezado `<h2>` a la sección `#ecosistema` para evitar saltos de nivel.
- Incorporar `aria-label` al elemento `<nav>`.
- Actualizar hitos en `README.md`.

**Detalle técnico:**
- Se garantiza que el árbol de encabezados sea secuencial: `h1` > `h2` > `h3`.
- El uso de **Landmarks** (Puntos de referencia) facilita la navegación a usuarios con tecnologías de asistencia.

**Motivo / criterio:** Cumplir con los estándares de **WAI-ARIA** (Web Accessibility Initiative - Accessible Rich Internet Applications - Iniciativa de Accesibilidad Web - Aplicaciones de Internet Enriquecidas Accesibles) y SEO técnico.

**Siguiente paso o deuda:** Iniciar la Fase 3 (Ingeniería de Estilos).

### 2026-04-14 — Integración de merci-sitemap.py en el hook de pre-commit

**Contexto:** Automatizar la actualización de la fecha `<lastmod>` en `sitemap.xml` cada vez que se realicen cambios en la carpeta `public/`.

**Hecho:** Modificar `scripts/merci/pre-commit`.

**Detalle técnico:**
- Se añadió lógica para detectar archivos staged en `public/`.
- Si se detectan cambios, se ejecuta `python3 scripts/merci/merci-sitemap.py`.
- Se añade `public/sitemap.xml` al índice de Git (`git add public/sitemap.xml`) para incluir su modificación en el commit actual.

**Motivo / criterio:** Asegurar que `sitemap.xml` refleje siempre la fecha de la última modificación de contenido relevante, mejorando la precisión del SEO técnico.

**Siguiente paso o deuda:** Realizar un commit de prueba que incluya cambios en `public/` para validar el funcionamiento del hook.

### 2026-04-14 — Automatización de metadatos de indexación (Sitemap)

**Contexto:** Evitar la actualización manual de la fecha de última modificación en el sitemap.xml para mejorar el SEO técnico.

**Hecho:** Crear script `scripts/merci/merci-sitemap.py` para la gestión automática de fechas en archivos XML.

**Detalle técnico:**
- Uso de la librería `datetime` para obtener la fecha del sistema.
- Empleo de `re.sub` para manipular el contenido del XML sin necesidad de parsers pesados.

**Motivo / criterio:** Mantener la consistencia entre los cambios reales y lo que se informa a los motores de búsqueda de forma automatizada.

**Siguiente paso o deuda:** Integrar la ejecución de este script en el flujo de publicación o en un hook de post-commit.

### 2026-04-14 — Cierre de Fase 1 y creación de activos de indexación (Fase 2.3)

**Contexto:** Finalización formal de la infraestructura base y configuración de la visibilidad para buscadores del núcleo estático.

**Hecho:** 
- Actualizar `README.md` para reflejar la Fase 1 como completada.
- Crear `public/robots.txt` y `public/sitemap.xml`.

**Detalle técnico:** 
- `robots.txt`: Configurado para permitir el rastreo total y apuntar al mapa del sitio.
- `sitemap.xml`: Generado con la URL canónica raíz y prioridad máxima.

**Motivo / criterio:** Cumplir con los estándares de **SEO** (Search Engine Optimization - Optimización para Motores de Búsqueda) técnico definidos en el roadmap.

**Siguiente paso o deuda:** Validar la jerarquía de encabezados (Fase 2.1) para asegurar accesibilidad.

### 2026-04-14 — Validación de Fase 2 (HTML y SEO Técnico) con Merci Audit

**Contexto:** Verificación del primer documento semántico del núcleo estático frente a las reglas de auditoría.

**Hecho:** Ejecutar `merci-audit.py --strict-json-ld` sobre `public/index.html`.

**Detalle técnico:**
- El archivo cumple con los requisitos de metadatos, charset y lenguaje.
- Se valida el bloque JSON-LD (JavaScript Object Notation for Linked Data - Notación de Objetos JavaScript para Datos Enlazados) usando el esquema de `schema.org`.

**Motivo / criterio:** Garantizar que el sitio es indexable y cumple con los estándares de rendimiento y SEO (Search Engine Optimization - Optimización para Motores de Búsqueda) desde la primera línea de código.

**Siguiente paso o deuda:** Implementar navegación (Fase 2.1) y generar `robots.txt` / `sitemap.xml` (Fase 2.3).

### 2026-04-14 — Creación de proyecto y obtención de API Key vía AI Studio

**Contexto:** El error 404 inicial no era solo de configuración de software, sino de falta de infraestructura (proyecto) en el lado de Google.

**Hecho:** Generar una API Key a través de Google AI Studio vinculada a un proyecto nuevo creado automáticamente por la plataforma.

**Detalle técnico:** 
- Acceso a `aistudio.google.com`.
- Uso de la opción "Create API key in new project" para evitar la configuración manual en GCP (Google Cloud Platform - Plataforma en la Nube de Google) Console.

**Motivo / criterio:** Vía más rápida para habilitar `gemini-1.5-pro` sin gestionar capas de facturación o cuotas complejas de Google Cloud de entrada.

**Siguiente paso o deuda:** Probar la conexión en Continue una vez la API Key esté activa y propagada.

### 2026-04-14 — Corrección de error 404 en Continue (Gemini 1.5 Pro)

**Contexto:** Fallo en la conexión con la API de Google al usar gemini-1.5-pro en Continue, con un error 404.

**Hecho:** Identificar que el `provider` en el archivo `/home/hildegahr/.continue/config.yaml` estaba configurado incorrectamente como `gemini`.

**Detalle técnico:** Modificar el `provider` de `gemini` a `google-generative-ai` para el modelo `gemini-1.5-pro` en la configuración de Continue.

**Motivo / criterio:** El `provider` `google-generative-ai` es el nombre correcto para interactuar con la API de Google Gemini a través de Continue.

**Siguiente paso o deuda:** Crear el proyecto en Google Cloud / AI Studio.

### 2026-04-12 — Fase 1: infraestructura, Merci Audit y primer commit

**Contexto:** Arranque del repositorio bajo las directrices de `instrucciones.md` (rendimiento, seguridad shift-left, pedagogía). Objetivo de la Fase 1: estructura de carpetas, script de auditoría local y base Git.

**Hecho:**

- Estructura aprobada en la raíz: `docs/`, `biblioteca/`, `laboratorio/`, `scripts/merci/`, `assets/`, `.assets-raw/` (las carpetas vacías se versionan con `.gitkeep` para que un `git clone` conserve el esqueleto).
- `scripts/merci/merci-audit.py`: auditoría con biblioteca estándar de Python (sin dependencias pip obligatorias en esta fase). Comprueba entre otras cosas patrones de secretos, sintaxis de `.py`, JSON, avisos en JS (`eval` / `new Function`) y reglas SEO mínimas en `.html` / `.htm`.
- `scripts/merci/pre-commit`: shell que ejecuta `merci-audit.py --git-staged` (solo lo que va al commit).
- Enlace local de Git: `.git/hooks/pre-commit` → `../../scripts/merci/pre-commit` (los hooks no viajan con el clone; hay que recrear el enlace en cada máquina o documentar un bootstrap).
- `.gitignore` para `.venv/`, cachés y artefactos de build; `requirements.txt` reservado para fases posteriores (p. ej. Pillow en optimizador).
- Commit inicial en rama `main` con mensaje tipo *chore: commit inicial — Fase 1 (estructura, Merci Audit, directrices)*.

**Detalle técnico:**

- Auditoría sobre todo el árbol: `python3 scripts/merci/merci-audit.py`
- Solo índice (staged), pensado para hook: `python3 scripts/merci/merci-audit.py --git-staged`
- Exigir JSON-LD en HTML cuando toque endurecer CI: flag `--strict-json-ld`
- Instalar hook (desde la raíz del repo): `chmod +x scripts/merci/pre-commit scripts/merci/merci-audit.py` y `ln -sf ../../scripts/merci/pre-commit .git/hooks/pre-commit`
- Saltar el hook solo si es deliberado: `git commit --no-verify`

**Motivo / criterio:** Automatizar comprobaciones antes de integrar cambios encaja con “seguridad shift-left” y con el papel de `merci-audit.py` descrito en instrucciones. Staged-only evita auditar el mundo en cada commit y acelera el flujo.

**Siguiente paso o deuda:** Fase 2 — HTML semántico, JSON-LD e indexación; primer documento público o plantilla que pase el audit sin `--no-verify`.

### 2026-04-12 — Registro cronológico acumulativo (no sustituir historial)

**Contexto:** Asegurar que la bitácora no pierda contexto al añadir sesiones nuevas.

**Hecho:** En `instrucciones.md` (regla 6) y en «Cómo mantenerlo» de este archivo quedó explícito: nuevas entradas **solo al final** del registro; no reemplazar ni borrar bloques ya escritos salvo corrección puntual o retirada de datos sensibles, con motivo claro.

**Detalle técnico:** N/A.

**Motivo / criterio:** El historial del laboratorio es activo de trazabilidad; sobrescribirlo rompería la línea temporal para el «yo futuro» y para el traslado a `biblioteca/`.

**Siguiente paso o deuda:** Seguir añadiendo entradas bajo «Registro cronológico» sin editar entradas previas salvo las excepciones acordadas.

### 2026-04-12 — `.assets-raw`: solo local, sin originales en Git

**Contexto:** Evitar que PSD, RAW, vídeos u otros brutos acaben en GitHub.

**Hecho:** `.gitignore` pasa a ignorar `.assets-raw/*` con excepción de `.assets-raw/.gitkeep`. `instrucciones.md` y `README.md` describen que la carpeta es convención de trabajo local y que lo versionado en `/assets` es lo optimizado.

**Detalle técnico:** Patrón en `.gitignore`: `!.assets-raw/.gitkeep` tras `.assets-raw/*`.

**Motivo / criterio:** Repositorio ligero y reproducible; los originales viven fuera del remoto (disco, NAS, etc.).

**Siguiente paso o deuda:** En Fase 3, documentar el flujo concreto `merci-optimizer.py` de `.assets-raw` → `assets/`.

### 2026-04-12 — Documentación pública sin notas personales al mantenedor

**Contexto:** Evitar frases tipo “cuando lo tengas claro añade LICENSE” en el README u otros textos versionados para GitHub.

**Hecho:** `README.md` (Licencia y otras frases) redactado en tono neutro. Nueva regla 7 en `instrucciones.md`: recordatorios al autor fuera del repo; en Git, texto útil para visitantes o colaboradores.

**Detalle técnico:** N/A.

**Motivo / criterio:** El remoto es documentación de producto/proyecto, no la libreta personal.

**Siguiente paso o deuda:** Revisar futuros `docs/` públicos con el mismo criterio.

### 2026-04-12 — Fase 2: carpeta `public/` como raíz del documento

**Contexto:** Inicio de la Fase 2 por la estructura antes del primer HTML.

**Hecho:** Directorio `public/` en el repo con `.gitkeep`; entrada en §3 de `instrucciones.md` y fila en `README.md`. Convención: aquí vive el núcleo estático servido como documento raíz; WP fuera hasta Fase 4.

**Detalle técnico:** Nombre elegido: `public/` (convención habitual de “document root” en despliegues estáticos).

**Motivo / criterio:** Separar claramente sitio servido, automatización, conocimiento y brutos locales.

**Siguiente paso o deuda:** `public/index.html` semántico + JSON-LD + `robots.txt` / `sitemap.xml` en la misma raíz cuando toque.

---

## Cuando pases esto a la biblioteca

1. **Releer** entradas y quitar ruido (intentos fallidos, datos personales, tokens aunque sean falsos).
2. **Partir por tema:** por ejemplo una ficha “Sistema Merci — auditoría pre-commit” vs “Estructura del repositorio”.
3. **Añadir los tres átomos** donde haya una decisión difícil o un incidente (síntoma, solución, lección o deuda).
4. **Enlazar** al código estable (rutas a `scripts/merci/`, no copiar bloques enormes en la biblioteca salvo que aporten lectura autónoma).

---

*Última revisión de la bitácora: 2026-04-14.*
