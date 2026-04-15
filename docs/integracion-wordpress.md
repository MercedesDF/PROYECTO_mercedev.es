# Integración y Aislamiento Dinámico (WordPress)

Este documento define la arquitectura técnica y operativa para la **Fase 4.1**. El objetivo es implementar espacios dinámicos administrables (`/blog`, `/tienda`) sin que el componente dinámico (WordPress) vulnere ni contamine la arquitectura estricta del núcleo servido desde `public/`.

## Estrategia de Enrutamiento Inverso (Nginx)

Se prescribe el uso de **Nginx** como *reverse proxy* e interceptador maestro. En el servidor huésped (Ubuntu), el entorno estático y el entorno dinámico vivirán en directorios padre separados (directorios hermanos), con Nginx encargándose de ensamblarlos en la misma URL transparente para el usuario final.

### Reglas de Configuración (Virtual Host Base)

```nginx
server {
    listen 80;
    server_name mercedev.es www.mercedev.es;

    # 1. El Core Estático (Frontera inmutable)
    root /var/www/mercedev/public;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }

    # 2. El Core Dinámico (Aislamiento de WordPress)
    location ^~ /blog {
        alias /var/www/wordpress/;
        index index.php;
        try_files $uri $uri/ /blog/index.php?$args;

        location ~ \.php$ {
            include fastcgi_params;
            fastcgi_pass unix:/run/php/php8.2-fpm.sock;
            fastcgi_param SCRIPT_FILENAME $request_filename;
        }
    }
}
```

## Definición de Fronteras y Blindajes

Para asegurar la supervivencia del paradigma minimalista y la puntuación perfecta de rendimiento en la raíz, deben cumplirse las siguientes fronteras:

1. **`public/` es _Read Only_ para el CMS:** Ningún script, actualizador o plugin de WordPress tendrá permisos de escritura (CHMOD) sobre el directorio `public/` ni sus predecesores en el proyecto Git.
2. **Dependencias Separadas:** Las actualizaciones de seguridad de WP, temas y plugins se ejecutan dentro del alcance de su alias (`/var/www/wordpress`). No viajan por nuestro repositorio Git, excepto el *Child Theme* diseñado en la Fase 4.2 si decidimos versionarlo en una carpeta separada (ej. `src/wp-theme/`).
3. **Consumo de Assets Unidireccional:** WordPress reutilizará las hojas de estilo y utilidades web compiladas en la carpeta universal `/assets/`. **Nunca** inyectará código a la inversa (hacia la home o estáticas).

## Preservación Canónica y de Indexación

La sobreposición de rutas tiene el riesgo de romper la cadena de rastreo de SEO técnico. Se previene implementando:

1. **Bloqueo del Canibalismo de Portada:** En las opciones globales de WordPress, las rutas `siteurl` y `home` se unifican obligatoriamente como `https://mercedev.es/blog`. No se debe instalar en la raíz ni usar plugins para desviar "la portada de WordPress" a la raíz del dominio principal.
2. **Jerarquía Unificada del Sitemap:** Un sitemap de índice (`sitemap_index.xml`) puede declarar dónde localizar los XML locales estáticos creados por `merci_sitemap.py` y dónde iniciar la traza generada automáticamente por WordPress para el contenido.

---
*Conclusión de Fase 4.1. Este documento sella la decisión de diseño arquitectónico y marca la pauta de despliegue antes de iniciar el Child Theme en la Fase 4.2.*
