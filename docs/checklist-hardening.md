# Checklist de Hardening (Endurecimiento) de mercedev.es

Este documento consolida las medidas de seguridad aplicadas en la arquitectura híbrida del proyecto (Núcleo Estático + WordPress aislado). Actúa como lista de verificación de obligado cumplimiento antes de cualquier paso a producción.

## 1. Capa Frontend (Núcleo Estático)

- [x] **Content Security Policy (CSP):** Implementada en el `<head>` de `public/index.html`.
  - `default-src 'self'`: Restringe la carga de recursos (scripts, estilos, imágenes) exclusivamente al dominio propio.
  - `object-src 'none'`: Bloquea la carga de plugins (Flash, Java, etc.).
  - `base-uri 'self'`: Impide la reescritura del origen de las rutas relativas.
  - *Motivo:* Mitigación drástica de ataques XSS (Cross-Site Scripting) y exfiltración de datos.

## 2. Capa Backend (Aislamiento de WordPress)

- [x] **Ofuscación de Versión:** Eliminado el tag generador de WordPress (`remove_action('wp_head', 'wp_generator')`).
  - *Motivo:* Dificulta el escaneo automatizado en busca de vulnerabilidades conocidas para una versión específica.
- [x] **Desactivación de XML-RPC:** Bloqueado mediante filtro (`add_filter('xmlrpc_enabled', '__return_false')`).
  - *Motivo:* Cierra uno de los vectores más comunes para ataques DDoS y de fuerza bruta en WordPress.
- [x] **Ofuscación de Errores de Login:** Mensajes de error genéricos implementados (`login_errors`).
  - *Motivo:* Evita la enumeración de usuarios válidos (el atacante no sabe si falla el usuario o la contraseña).
- [x] **Limpieza de Cabeceras:** Eliminación de enlaces RSD y WLW Manifest.
  - *Motivo:* Reducción de superficie de ataque y limpieza de código basura no utilizado.

## 3. Capa de Infraestructura (Servidor LEMP)

- [x] **Principio de Mínimo Privilegio (Usuarios):**
  - Base de datos (`wp_mercedev_local`): Accedida mediante un usuario de MySQL dedicado (`wp_user_local`), sin privilegios globales.
  - WordPress no usa el usuario por defecto "admin".
- [x] **Permisos de Sistema de Archivos (CHMOD/CHOWN):**
  - Directorio base: Propiedad exclusiva de `www-data:www-data`.
  - Directorios (`755`): Lectura/Ejecución para todos, escritura solo para `www-data`.
  - Archivos (`644`): Lectura para todos, escritura solo para `www-data`.
  - Archivo crítico (`wp-config.php` a `600`): Lectura y escritura **solo** para `www-data`.
- [x] **Fronteras Inmutables (Nginx):**
  - El entorno dinámico (`/blog`) se sirve mediante un `alias` en Nginx desde un directorio físico separado (`/var/www/wordpress`).
  - WordPress no tiene permisos de escritura sobre la raíz estática (`/var/www/mercedev/public`).

## 4. Capa DevSecOps (Control de Calidad Local)

- [x] **Auditoría Pre-Commit (`merci-audit.py`):**
  - Bloqueo automático (Código de salida `1`) si se detectan:
    - Patrones de secretos expuestos (Tokens, claves privadas, API Keys).
    - Errores de sintaxis en Python o JSON.
    - Ausencia de etiquetas SEO críticas (lang, title, description).
  - Detección de "PHP Smells" (Advertencias por uso de funciones peligrosas como `eval()`, `exec()`, `shell_exec()`).
- [x] **Auditoría Estandarizada Pre-Merge:**
  - Obligatoriedad de ejecutar `python3 scripts/merci/merci-audit.py --strict-json-ld` para garantizar la presencia de datos estructurados antes de pasar a producción.

---
*Última revisión: Fase 5 Completada.*