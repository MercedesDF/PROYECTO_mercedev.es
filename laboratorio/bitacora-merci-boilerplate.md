# Bitácora de Proyecto: Merci Boilerplate

Documento central para el registro de decisiones arquitectónicas, resolución de problemas y evolución del código. (Formato: El Desafío -> La Maniobra -> El Aprendizaje).

## Registro cronológico

### 2026-05-16 — Fix: Degradación Elegante en generación de PDFs (WeasyPrint)

**Contexto:** El rastreador dinámico de enlaces (`merci-linkcheck.py`) reportaba errores 404 (`Failed to load resource`) debido a enlaces rotos en los botones de descarga de PDF. Esto sucedía porque el orquestador (`merci-publish.py`) inyectaba incondicionalmente el enlace al PDF en el DOM, incluso cuando la librería `weasyprint` no estaba instalada o fallaba al renderizar el archivo.

**Hecho:** Se implementó una inyección condicional del enlace de descarga HTML en `scripts/merci/merci-publish.py`.

**Detalle técnico:** Se inicializa `pdf_download_link = ""` y solo se le asigna el bloque de código `<a href="/descargas/...">` si la llamada a WeasyPrint se ejecuta con éxito y el comando `out_pdf_path.exists()` confirma que el archivo físico fue creado en disco. Este enlace condicionado se inyecta luego dinámicamente junto al `<h1>`.

**Motivo / criterio:** *Fail Gracefully (Degradación Elegante) y Shift-Left DAST*. Si el entorno local carece de dependencias pesadas, el generador estático debe sobrevivir y publicar el HTML intacto sin generar "enlaces fantasma". Condicionar la UI a la existencia física del recurso erradica los 404 detectados por el linter dinámico y mantiene la promesa de 0 dependencias bloqueantes.

**Siguiente paso o deuda:** Ejecutar `merci total` para compilar el HTML, limpiar los enlaces rotos y empaquetar el commit de la sesión.

### AAAA-MM-DD — Instanciación del repositorio base

**Contexto:** Arranque de un nuevo proyecto utilizando la infraestructura fundacional de Merci Boilerplate. Se requiere limpiar las referencias del proyecto matriz y establecer el estado en blanco.

**Hecho:**
- Clonación del repositorio original.
- Ejecución destructiva de `python3 scripts/merci/merci-init.py`.
- Promoción de archivos documentales agnósticos (`README.md`, `instrucciones.md`).

**Motivo / criterio:** *Single Source of Truth*. Utilizar este script asegura que el nuevo proyecto no herede deuda técnica ni identidad visual del autor original, proveyendo un lienzo estricto DevSecOps desde el commit cero.

**Siguiente paso o deuda:** Configurar la base de datos local y revisar `docs/integracion-wordpress.md`.