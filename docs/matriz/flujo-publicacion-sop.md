# SOP: Flujo de Publicación Dual (SSG y Headless WP)

Este documento define el Procedimiento Operativo Estándar (SOP) para la publicación de contenidos en el ecosistema híbrido `mercedev.es`. 

Por diseño arquitectónico (Environment Segregation), el núcleo estático (Biblioteca) y la capa dinámica (Blog/Tienda en WordPress) viven en universos separados. **Sus flujos de publicación nunca deben cruzarse.**

---

## FLUJO 1: La Biblioteca (Núcleo Estático / SSG)
**Destino:** `public/biblioteca/`
**Características:** Contenido fundacional, manuales y proyectos. Genera HTML ultrarrápido y PDF descargable.

### Paso a Paso:
1. **Incubación:** Crea o edita tu documento Markdown (`.md`) dentro de la carpeta `laboratorio/`. Su YAML Frontmatter debe tener `estado: "borrador"`.
2. **Curación (Promote):** Cuando esté listo para publicarse, ejecuta en la terminal:
   ```bash
   python3 scripts/merci/merci-promote.py
   ```
   *Nota:* El asistente interactivo validará el SEO/Accesibilidad, cambiará el estado a `"publicado"` y moverá físicamente el archivo a la carpeta `biblioteca/`.
3. **Compilación y QA:** Ejecuta el orquestador maestro para transformar el Markdown en HTML/PDF, actualizar el índice y pasar la auditoría estricta:
   ```bash
   merci total
   ```
4. **Sello y Empaquetado:** Sella la publicación subiendo los archivos a Git:
   ```bash
   merci commit
   ```

---

## FLUJO 2: Blog y Art de Coté (WordPress Headless)
**Destino:** Base de datos local de WordPress (visible en `/blog`).
**Características:** Contenido dinámico, artículos colaterales, reflexiones o novedades.

### Paso a Paso:
1. **Redacción Aislada:** Crea tu documento Markdown en una subcarpeta ajena al flujo estático, por ejemplo dentro de tu zona de pruebas (ej. `laboratorio/art-de-cote/`). 
   *Asegúrate de que el YAML tenga `estado: "publicado"` y un `tema:` que coincida con una categoría de tu WordPress.*
2. **Sincronización Directa (Headless):** Ejecuta el script sin argumentos para escanear y sincronizar automáticamente todas las carpetas dinámicas (`blog/` y `art-de-cote/`):
   ```bash
   python3 scripts/merci/merci-wp.py
   ```
   *(Opcional: puedes pasarle la ruta de un archivo o carpeta específica si solo quieres sincronizar ese elemento).*
3. **Actualización y Borradores (Kill-Switch WP):** En la primera ejecución, el script **escribirá el `wp_id`** dentro del YAML de tu archivo local. En futuras ejecuciones, el script detectará el ID y actualizará el post en la base de datos de WordPress. Si cambias el `estado` a `"borrador"`, el artículo se ocultará de la vista pública del blog automáticamente.
4. **Sello de Código Fuente:** Opcionalmente, ejecuta `merci commit` para guardar el archivo `.md` (con su nuevo `wp_id`) en tu control de versiones.

---

## ⚠️ Reglas de Oro (Hardening Operativo)

- **Prohibición de cruce:** Nunca ejecutes `merci-promote.py` sobre un archivo destinado a WordPress. Si lo haces, el script lo enviará a la `biblioteca/` y el SSG intentará compilarlo como una página estática.
- **Despublicación SSG (Kill-Switch):** Si necesitas retirar un artículo de la Biblioteca, edita su `.md` en la carpeta `biblioteca/`, cambia el YAML a `estado: "borrador"` y ejecuta `merci total`. El orquestador destruirá el HTML/PDF público y enviará el archivo de vuelta al `laboratorio/`.
- **Entorno encendido:** El *Flujo 2* requiere obligatoriamente que el servidor Nginx/MariaDB local esté encendido para poder comunicarse con la API REST de WordPress.