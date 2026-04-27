# Directrices Base: Merci Boilerplate

Este documento define las reglas de arquitectura e interacción de esta plantilla. Todo desarrollo construido sobre este código base debe respetar estos principios.

## 1. Filosofía del Proyecto
- **Rendimiento > Todo:** Prioridad absoluta a los Core Web Vitals (100/100).
- **Trazabilidad del Error:** Cada problema técnico se documenta en `laboratorio/bitacora-merci-boilerplate.md` usando 3 átomos: Desafío (Síntoma) -> Maniobra (Lógica) -> Aprendizaje.

## 2. Stack Tecnológico y Arquitectura
- **Núcleo Estático:** HTML5 semántico, SASS 7-1 (BEM) compilado localmente y Vanilla JS (0 dependencias).
- **Sistema "Merci":** Automatización local DevSecOps basada en scripts puros de Python 3.10+ en la carpeta `/scripts/merci/`.
- **Capa Dinámica:** WordPress aislado (`/blog`) sirviendo como CMS headless bajo Nginx proxy inverso, sin invadir `/public`.

## 3. Reglas de Interacción y Código
1. **Seguridad Shift-Left:** Todo el código debe pasar obligatoriamente por `python3 scripts/merci/merci-audit.py` antes del commit.
2. **Manejo de Errores:** Todo código debe incluir gestión de excepciones para evitar colapsos silentes.
3. **Bitácora Obligatoria:** `merci-commit.py` bloqueará los empaquetados si no se ha documentado el cambio cronológicamente en la bitácora del laboratorio.
4. **Convención de Commits:** Utilizar prefijos semánticos (`feat:`, `fix:`, `chore:`, `docs:`, `refactor:`, `perf:`).
5. **Aislamiento de WordPress:** El CMS nunca debe escribir ni modificar archivos en el directorio `/public`. Su comunicación con el frontend es unidireccional y controlada por Nginx.

## 4. Flujo Maestro de Publicación de Contenidos (SOP)
El ecosistema cuenta con su propio SSG (Static Site Generation). Para publicar artículos en la Biblioteca estática:
1. Crear archivo Markdown con YAML Frontmatter en `laboratorio/`.
2. Ejecutar `python3 scripts/merci/merci-promote.py` para curarlo y moverlo a la Biblioteca.
3. Ejecutar `python3 scripts/merci/merci-publish.py` para compilar el HTML y generar los PDFs automáticamente.
4. Ejecutar `python3 scripts/merci/merci-total.py` para validar SEO, Sitemaps y compilar el CSS.
5. Empaquetar con `python3 scripts/merci/merci-commit.py`.

## 5. Decisiones Arquitectónicas Restringidas
- **Cero dependencias visuales:** Prohibido el uso de librerías de animación de terceros o frameworks reactivos (Vue/React/Tailwind) en el frontend.
- **Accesibilidad Nativa:** Toda la UI debe ser navegable mediante Tabulador y usar etiquetas semánticas (WAI-ARIA).
- **Focus Management:** No se debe usar `tabindex="-1"` en el `body`.

---
Cualquier colaborador que herede este repositorio debe leer este documento antes de solicitar integraciones o añadir dependencias externas.