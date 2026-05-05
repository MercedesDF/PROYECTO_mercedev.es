# mercedev.es

Base de conocimiento y centro de operaciones DevSecOps de Mercedes. Arquitectura de software híbrida, Desarrollo Guiado por Especificaciones (Spec-Driven Development) y orquestación de Inteligencia Artificial bajo estrictos estándares de gobernanza.

Repositorio del sitio **mercedev.es**: núcleo estático minimalista (100/100 Core Web Vitals), biblioteca de Decisiones de Arquitectura (ADRs) y automatización local en Python puro (**Sistema Merci**).

## Requisitos

- **Python 3.10+** (para `merci-audit.py`; sin dependencias pip obligatorias en la fase actual).
- **Git** y, si se usa el hook de pre-commit, un shell compatible con el script indicado más abajo (p. ej. **sh** o **zsh**).

## Puesta en marcha

```bash
git clone git@github.com:MercedesDF/PROYECTO_mercedev.es.git
cd PROYECTO_mercedev.es
python3 scripts/merci/merci-audit.py
```

Auditoría solo sobre los archivos ya en el índice (staged), misma lógica que el hook:

```bash
python3 scripts/merci/merci-audit.py --git-staged
```

### Hook de pre-commit (opcional, en cada clon)

```bash
chmod +x scripts/merci/pre-commit scripts/merci/merci-audit.py
ln -sf ../../scripts/merci/pre-commit .git/hooks/pre-commit
```

## Estructura principal

| Ruta | Contenido |
|------|-----------|
| `docs/` | Estrategia y directrices |
| `biblioteca/` | Documentación técnica definitiva (por estanterías) |
| `laboratorio/` | I+D y bitácora de proyecto (`bitacora-mercedev.md`) |
| `scripts/merci/` | Ecosistema DevSecOps local en Python puro |
| `assets/` | Multimedia optimizado para producción |
| `public/` | Raíz del documento del sitio estático (HTML, `robots.txt`, `sitemap.xml`; enlaces a `assets/`). |
| `.assets-raw/` | Originales sin procesar en el entorno local; Git ignora el contenido salvo `.gitkeep` (PSD/RAW/vídeo no van al remoto). |

### Ecosistema Merci (Scripts Principales)
- `merci-audit.py`: Auditoría estática y bloqueo de secretos (SAST - Static Application Security Testing - Pruebas Estáticas de Seguridad de Aplicaciones).
- `merci-commit.py`: Empaquetado atómico impulsado por la lectura de la bitácora.
- `merci-total.py`: Orquestador maestro del pipeline local.
- `merci-brain.py`: Lóbulo frontal de Inteligencia Artificial (Shift-Left AI).
- `merci-publish.py` y `merci-promote.py`: Motor SSG (Static Site Generation - Generación de Sitios Estáticos) y promoción de contenidos.
- `merci-sync-pages.py`: Sincronizador de estructuras comunes estáticas (SSOT en páginas independientes).
- `merci-sitemap.py` y `merci-linkcheck.py`: Rastreador dinámico (DAST) y generación de mapa XML.
- `merci-backup.py`: Creador de instantáneas ultraligeras (Snapshots).
- `merci-init.py`: Instanciador destructivo para nuevos repositorios derivados.
- `merci-linkedin.py`: Motor de autenticación OIDC (OpenID Connect) y publicación automatizada en LinkedIn.
- `merci-wp.py`: Publicador Headless para WordPress vía API REST.
- `merci-styles.py` y `merci-watcher.py`: Compilador SASS 7-1 local y vigilante en tiempo real.
- `merci-optimizer.py`: Optimizador de imágenes a formato WebP.

## Entorno de Desarrollo Local
Para mantener la separación de responsabilidades y la alta velocidad, el desarrollo se divide en dos fases con ecosistemas distintos:

### 1. Desarrollo UI/UX Estático (Python)
Para maquetar HTML y SASS sin levantar bases de datos ni Nginx.
Abre dos terminales: una para `python3 scripts/merci/merci-watcher.py` y otra en `public/` para el servidor efímero `python3 -m http.server 8000`.

### 2. Integración Dinámica WP (Nginx / LEMP)
El servidor nativo de Python **no procesa PHP (Hypertext Preprocessor - Preprocesador de Hipertexto)**. Cuando llegues a la fase de integrar el CMS (Content Management System - Sistema de Gestión de Contenidos), abandona el servidor de Python y usa Nginx local con la configuración de proxy inverso que se detalla en `docs/integracion-wordpress.md`.

## Directrices del proyecto

Las reglas de arquitectura, pedagogía, roadmap y convenciones están en **`instrucciones.md`**. Quien colabore o retome el repo debería leerlo antes de cambiar el stack o las fases.

## Flujo de Contribución y Validación

Antes de cada commit atómico (`merci-commit`), el hook de `pre-commit` ejecuta una auditoría básica sobre los archivos en el *stage*.

Sin embargo, antes de proponer la integración de una rama de funcionalidad (ej. un *Pull Request*), se debe ejecutar la **auditoría completa y estandarizada** sobre todo el proyecto para asegurar la máxima calidad.

**Comando de Auditoría Completa Estandarizada:**
```bash
# Desde la raíz del repositorio
python3 scripts/merci/merci-audit.py --strict-json-ld
```

## Roadmap

Checklist de avance por fases y subfases. Cada hito está pensado para poder marcarse cuando la evidencia técnica exista en el repositorio o en la verificación local.

### Fase 1 - Infraestructura y Automatización Base

#### 1.1 Estructura base de repositorio y entorno
- [x] Verificar la estructura aprobada (`docs/`, `biblioteca/`, `laboratorio/`, `scripts/merci/`, `assets/`, `public/`, `.assets-raw/`).
- [x] Confirmar que `.assets-raw/` mantiene solo `.gitkeep` como contenido versionado.
- [x] Definir y documentar una convención estable de nombres de archivos y rutas.

#### 1.2 Sistema Merci y auditoría inicial
- [x] Ejecutar `python3 scripts/merci/merci-audit.py` en local y registrar resultado base.
- [x] Ejecutar `python3 scripts/merci/merci-audit.py --git-staged` para validar el flujo staged.
- [x] Corregir advertencias críticas detectadas por `merci-audit.py` antes de nuevas fases.

#### 1.3 Integración de hook de pre-commit
- [x] Aplicar permisos de ejecución a `scripts/merci/pre-commit` y `scripts/merci/merci-audit.py`.
- [x] Enlazar hook local a `.git/hooks/pre-commit` y validar su ejecución en un commit de prueba.
- [x] Asegurar que los commits con fallos de auditoría se bloquean correctamente.

#### 1.4 Gobernanza técnica mínima
- [x] Crear entrada de bitácora en `laboratorio/bitacora-mercedev.md` con contexto de arranque.
- [x] Registrar comandos estándar de trabajo para facilitar continuidad entre sesiones.
- [x] Confirmar que la documentación del repo no incluye notas personales ni recordatorios en segunda persona.

### Fase 2 - Arquitectura Semántica y SEO Técnico

#### 2.1 Base semántica del núcleo estático
- [x] Estructurar `public/index.html` con semántica HTML5 estricta (`header`, `main`, `section`, `footer`).
- [x] Validar jerarquía de encabezados (`h1`-`h6`) sin saltos estructurales.
- [x] Incorporar landmarks accesibles para navegación asistida.

#### 2.2 Metadatos y datos estructurados
- [x] Definir metadatos esenciales (`title`, `description`, `canonical`, `viewport`).
- [x] Insertar bloque JSON-LD mínimo alineado con el tipo de sitio.
- [x] Verificar sintaxis del JSON-LD y su coherencia con el contenido real de la página.

#### 2.3 Indexación técnica
- [x] Crear `public/robots.txt` con reglas explícitas de rastreo.
- [x] Crear `public/sitemap.xml` con URLs canónicas previstas para producción.
- [x] Revisar consistencia entre `robots.txt`, `sitemap.xml` y canónicas.
- [x] Automatizar actualización de `lastmod` mediante `merci-sitemap.py`.
- [x] Integrar `merci-sitemap.py` en el hook de pre-commit para actualización automática.

#### 2.4 Ingesta de Evidencias (Laboratorio)
- [x] Implementar `laboratorio/scripts_temporales/merci_ingestor.py` para escanear y mover archivos recientes a `.assets-raw/`.
- [x] Documentar rutas de escaneo configurables para `merci_ingestor.py`.
  > **Nota técnica:** Por defecto, el Ingestor escanea `~/Pictures`, `~/Videos` y `~/Desktop`. Para añadir carpetas personalizadas (como tu NAS local o carpeta de descargas), edita la variable `USER_CAPTURE_DIRS` en las primeras líneas de `laboratorio/scripts_temporales/merci_ingestor.py`.

#### 2.4 Validación SEO y accesibilidad base
- [x] Confirmar atributos `lang`, `charset` y semántica documental mínima.
- [x] Verificar que imágenes críticas incluyen texto alternativo útil (actualmente sin dependencias visuales críticas).
- [x] Registrar en bitácora los criterios de aceptación SEO para cierre de fase.

### Fase 3 - Ingeniería de Estilos

#### 3.1 Arquitectura SASS 7-1
- [x] Crear árbol SASS 7-1 y documentar responsabilidad de cada carpeta.
- [x] Definir un punto de entrada único de compilación hacia un solo CSS final.
- [x] Verificar orden de importación para evitar cascadas inesperadas.

#### 3.2 Metodología BEM
- [x] Establecer convención BEM (Block, Element, Modifier - Modificador de Elemento de Bloque) para bloques, elementos y modificadores.
- [x] Reflejar la convención BEM en los componentes HTML clave.
- [x] Revisar y eliminar clases ambiguas o no alineadas con BEM.

#### 3.3 Estrategia mobile-first y rendimiento
- [x] Implementar estilos base para móvil antes de breakpoints superiores.
- [x] Definir breakpoints justificados por contenido, no por dispositivo.
- [x] Reducir reglas redundantes y validar peso final del CSS compilado.

#### 3.4 Optimización multimedia con Merci
- [x] Implementar o consolidar `merci-optimizer.py` para generar WebP responsivo.
- [x] Definir tamaños objetivo y nomenclatura de salida en `assets/`.
- [x] Validar que los originales en `.assets-raw/` no pasan al remoto.

### Fase 4 - Integración de Sistemas Dinámicos

#### 4.0 Entorno LEMP local y base de datos
- [x] Verificar instalación de pila LEMP (Nginx, MariaDB, PHP) en PC local.
- [x] Crear base de datos local y usuario para el entorno de WordPress.
- [x] Desplegar WordPress en directorio de desarrollo local replicando la estructura de producción.

#### 4.1 Aislamiento de WordPress
- [x] Definir integración de WordPress en rutas aisladas (`/blog`, `/tienda`) sin invadir `public/`.
- [x] Documentar fronteras entre núcleo estático y capa dinámica (`docs/integracion-wordpress.md`).
- [x] Verificar que el routing previsto no rompe URLs canónicas del núcleo.

#### 4.2 Child theme ultraligero
- [x] Crear child theme con sobrecarga mínima y sin lógica innecesaria.
- [x] Enlazar estilos compartidos de forma controlada para mantener coherencia visual.
- [x] Validar que no se introducen dependencias pesadas en frontend.

#### 4.3 WooCommerce optimizado para catálogo
- [x] Configurar WooCommerce en modo catálogo para merchandising de Merci según alcance funcional definido.
- [x] Limitar plugins y extensiones a los estrictamente necesarios.
- [x] Revisar impacto de scripts dinámicos en tiempos de carga.

#### 4.4 Integración sin degradación del núcleo
- [x] Medir impacto de `/blog` y `/tienda` sobre Core Web Vitals del sitio principal.
- [x] Asegurar carga diferida o condicional de recursos dinámicos.
- [x] Registrar decisiones de integración y deuda técnica asociada en bitácora.

#### 4.5 Presencia pública de Merci (frontend controlado)
- [x] Definir rol de Merci en interfaz (acompañamiento, estados y límites de interacción).
- [x] Diseñar contrato técnico entre backend de Merci y capa visual sin acoplar al núcleo estático.
- [x] Validar que animación, voz o movimiento de Merci no degrada accesibilidad ni rendimiento.

### Fase 5 - Quality Assurance y Hardening

#### 5.1 Política de seguridad frontend
- [x] Definir una política CSP progresiva con modo de validación inicial.
- [x] Ajustar orígenes permitidos para scripts, estilos, fuentes e imágenes.
- [x] Verificar que la CSP final no rompe funcionalidad crítica.

#### 5.2 Hardening de WordPress
- [x] Aplicar endurecimiento básico de WP (superficie de ataque mínima).
- [x] Revisar permisos, usuarios administrativos y exposición de endpoints.
- [x] Comprobar desactivación de funcionalidades no necesarias.

#### 5.3 Automatización de control de calidad
- [x] Ampliar checks de pre-commit para cubrir validaciones críticas recurrentes.
- [x] Estandarizar ejecución local de auditorías antes de merge.
- [x] Documentar criterios de fallo/bloqueo para que sean reproducibles.

#### 5.4 Verificación de seguridad y consistencia
- [x] Ejecutar una pasada integral de auditoría estática y corregir hallazgos críticos.
- [x] Confirmar que no hay secretos ni credenciales en el árbol versionado.
- [x] Consolidar checklist de hardening completado en documentación interna.

#### 5.5 Hardening avanzado de cabeceras HTTP
- [x] Implementar HSTS, COOP/COEP y políticas de Referrer/X-Content-Type.
- [x] Migrar la CSP desde la etiqueta `<meta>` a una cabecera HTTP robusta.
- [x] Validar la nueva configuración de seguridad con herramientas externas.

### Fase 6 - Despliegue y Auditoría Final

#### 6.1 Preparación de release
- [x] Definir proceso de despliegue paso a paso para entorno de producción.
- [x] Verificar artefactos finales del núcleo estático antes del deploy.
- [x] Confirmar consistencia de rutas absolutas/relativas para entorno real.

#### 6.2 Auditoría de rendimiento y accesibilidad
- [x] Ejecutar mediciones de Core Web Vitals con metodología reproducible.
- [x] Validar accesibilidad técnica base y corregir desviaciones críticas.
- [x] Comparar resultados frente a objetivos de la filosofía del proyecto.

#### 6.3 Verificación SEO final
- [x] Revisar indexabilidad efectiva, canónicas y metadatos finales.
- [x] Validar `robots.txt` y `sitemap.xml` contra el estado real de URLs.
- [x] Confirmar coherencia entre contenido visible y datos estructurados.

#### 6.4 Cierre documental de despliegue
- [x] Registrar evidencias del despliegue y resultados de auditoría.
- [x] Documentar incidencias y mitigaciones aplicadas durante la salida.
- [x] Dejar criterios explícitos de rollback y recuperación operativa.

### Fase 7 - Automatización y Clasificación

#### 7.1 Flujo de publicación automatizada
- [x] Diseñar flujo de publicación que minimice tareas manuales repetitivas.
- [x] Definir puntos de validación automática previos a publicación.
- [x] Documentar dependencias y responsabilidades del pipeline.

#### 7.2 Plantillas de conocimiento para biblioteca
- [x] Definir plantillas estándar para documentos definitivos en `biblioteca/`.
- [x] Integrar la estructura de 3 átomos (desafío, maniobra, aprendizaje/deuda).
- [x] Validar consistencia editorial y técnica entre estanterías temáticas.

#### 7.3 Flujo laboratorio -> biblioteca
- [x] Formalizar criterio para promover contenido desde `laboratorio/` a `biblioteca/`.
- [x] Añadir checklist de curación y revisión previa a promoción.
- [x] Registrar trazabilidad del origen de cada pieza publicada.

#### 7.4 Mantenimiento y mejora continua
- [x] Definir cadencia de revisión del roadmap y actualización de hitos.
- [x] Revisar periódicamente deuda técnica acumulada por fase.
- [x] Mantener sincronía entre `README.md`, `instrucciones.md` y bitácora activa.

#### 7.5 Producto Merci (cara pública + backend)
- [x] Planificar carpeta/proyecto dedicado para Merci con límites claros frente a `mercedev.es`.
- [x] Definir roadmap propio de Merci: avatar/estado visual, diálogo y comportamiento por contexto.
- [x] Establecer versión mínima de integración en `mercedev.es` antes de ampliar capacidades.
- [x] Documentar criterio de evolución de Merci para evitar desvíos fuera del orden de fases.

### Fase 8 - Expansión de Contenido y Contexto Inteligente

#### 8.1 El Cerebro de Merci (Context Routing)
- [x] Implementar respuestas contextuales basadas en la ruta (`window.location.pathname`).
- [x] Mantener 0 latencia y 0 dependencias (evitar consultas a base de datos en frontend).

#### 8.2 Ciclo de Migración de Contenidos
- [x] Emplear `merci-promote` para trasladar cuadernillos históricos a la Biblioteca.

#### 8.3 Consolidación Operativa (UX y Headless CMS)
- [x] Unificar enlaces globales en pie de página (LinkedIn, GitHub, Boilerplate) manteniendo paridad Dev/Prod.
- [x] Completar página estática de contacto (`public/contacto/index.html`) y afinar la portada (Sincronización SSOT).
- [x] Generar un pequeño índice curado de los artículos publicados en la biblioteca (Auto-generado por merci-publish).
- [x] Desarrollar publicador Headless (`merci-wp.py`) agnóstico al entorno (Local/Nube) con resolución dinámica por Slug y Proxy Bypass.
- [x] Implementar automatización social para publicar entradas del blog directamente en LinkedIn.
- [x] Prevenir *Data Drift* (Posts Fantasma) aislando el borrado y estableciendo el Kill-Switch de despublicación.

#### 8.4 Identidad y Autoridad Técnica
- [x] Actualización de posicionamiento público y copy de portada (`index.html`).
- [x] Propagación de enlaces de navegación en cabeceras de plantillas estáticas y dinámicas para evitar asimetría visual.
- [x] Diseño e implementación del CV Semántico "Anti-ATS" (`/sobre-mi/index.html`) expuesto con marcado de microdatos JSON-LD (`schema.org/Person`).
- [x] Consolidación documental del patrón arquitectónico en la Biblioteca (`cuadernillo-cv-anti-ats-json-ld.md`).

### Fase 9 - Inteligencia y Autonomía (Merci Avanzado)

#### 9.1 Conexión Dinámica (Opcional)
- [x] Evaluar integración segura con APIs de LLM o modelos locales para respuestas dinámicas (Shift-Left AI con Gemini).
- [x] Garantizar que la IA no rompe la política de 0 dependencias bloqueantes (Graceful Degradation y Fallback estático).

### Fase 10 - Empaquetado y Ecosistema (Release 1.0.0)

#### 10.1 Preparación del Boilerplate
- [x] Crear script de instanciación (`merci-init.py`) para limpiar datos base y arrancar proyectos nuevos.
- [x] Revisión final de documentación pública y lanzamiento de la versión 1.0.0.

### Fase 11 - Integración Continua y Calidad en la Nube (CI/CD)

#### 11.1 Automatización Cloud (GitHub Actions)
- [x] Implementar flujos de GitHub Actions para automatizar `merci-audit` en cada Pull Request.
- [x] ~~Automatizar la compilación SSG (`merci-publish`) directamente en el servidor de despliegue~~ (🛑 **Descartado/Rollback:** Preferencia de Arquitectura por control manual mediante `git pull`).

#### 11.2 Monitorización de Rendimiento
- [x] Integrar Lighthouse CI para garantizar que ninguna actualización degrade el 100/100 en Core Web Vitals.

#### 11.3 Gobernanza Open Source
- [x] Configurar *Issue Templates* y *Pull Request Templates* para estandarizar las contribuciones en repositorios públicos.


## Licencia

Este proyecto se distribuye bajo los términos de la **Licencia MIT**. Consulta el archivo `LICENSE` para más detalles. El contenido narrativo de la biblioteca y bitácora es propiedad intelectual de su autora.
