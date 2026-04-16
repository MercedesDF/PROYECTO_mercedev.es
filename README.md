# mercedev.es

Repositorio del sitio **mercedev.es**: núcleo estático minimalista, biblioteca de conocimiento y automatización local (**Merci**).

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
| `scripts/merci/` | Automatización Python (p. ej. `merci-audit.py`) |
| `assets/` | Multimedia optimizado para producción |
| `public/` | Raíz del documento del sitio estático (HTML, `robots.txt`, `sitemap.xml`; enlaces a `assets/`). |
| `.assets-raw/` | Originales sin procesar en el entorno local; Git ignora el contenido salvo `.gitkeep` (PSD/RAW/vídeo no van al remoto). |

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
- [x] Establecer convención BEM para bloques, elementos y modificadores.
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
- [ ] Definir rol de Merci en interfaz (acompañamiento, estados y límites de interacción).
- [ ] Diseñar contrato técnico entre backend de Merci y capa visual sin acoplar al núcleo estático.
- [ ] Validar que animación, voz o movimiento de Merci no degrada accesibilidad ni rendimiento.

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
- [ ] Documentar criterios de fallo/bloqueo para que sean reproducibles.

#### 5.4 Verificación de seguridad y consistencia
- [ ] Ejecutar una pasada integral de auditoría estática y corregir hallazgos críticos.
- [ ] Confirmar que no hay secretos ni credenciales en el árbol versionado.
- [ ] Consolidar checklist de hardening completado en documentación interna.

### Fase 6 - Despliegue y Auditoría Final

#### 6.1 Preparación de release
- [ ] Definir proceso de despliegue paso a paso para entorno de producción.
- [ ] Verificar artefactos finales del núcleo estático antes del deploy.
- [ ] Confirmar consistencia de rutas absolutas/relativas para entorno real.

#### 6.2 Auditoría de rendimiento y accesibilidad
- [ ] Ejecutar mediciones de Core Web Vitals con metodología reproducible.
- [ ] Validar accesibilidad técnica base y corregir desviaciones críticas.
- [ ] Comparar resultados frente a objetivos de la filosofía del proyecto.

#### 6.3 Verificación SEO final
- [ ] Revisar indexabilidad efectiva, canónicas y metadatos finales.
- [ ] Validar `robots.txt` y `sitemap.xml` contra el estado real de URLs.
- [ ] Confirmar coherencia entre contenido visible y datos estructurados.

#### 6.4 Cierre documental de despliegue
- [ ] Registrar evidencias del despliegue y resultados de auditoría.
- [ ] Documentar incidencias y mitigaciones aplicadas durante la salida.
- [ ] Dejar criterios explícitos de rollback y recuperación operativa.

### Fase 7 - Automatización y Clasificación

#### 7.1 Flujo de publicación automatizada
- [ ] Diseñar flujo de publicación que minimice tareas manuales repetitivas.
- [ ] Definir puntos de validación automática previos a publicación.
- [ ] Documentar dependencias y responsabilidades del pipeline.

#### 7.2 Plantillas de conocimiento para biblioteca
- [ ] Definir plantillas estándar para documentos definitivos en `biblioteca/`.
- [ ] Integrar la estructura de 3 átomos (desafío, maniobra, aprendizaje/deuda).
- [ ] Validar consistencia editorial y técnica entre estanterías temáticas.

#### 7.3 Flujo laboratorio -> biblioteca
- [ ] Formalizar criterio para promover contenido desde `laboratorio/` a `biblioteca/`.
- [ ] Añadir checklist de curación y revisión previa a promoción.
- [ ] Registrar trazabilidad del origen de cada pieza publicada.

#### 7.4 Mantenimiento y mejora continua
- [ ] Definir cadencia de revisión del roadmap y actualización de hitos.
- [ ] Revisar periódicamente deuda técnica acumulada por fase.
- [ ] Mantener sincronía entre `README.md`, `instrucciones.md` y bitácora activa.

#### 7.5 Producto Merci (cara pública + backend)
- [ ] Planificar carpeta/proyecto dedicado para Merci con límites claros frente a `mercedev.es`.
- [ ] Definir roadmap propio de Merci: avatar/estado visual, diálogo y comportamiento por contexto.
- [ ] Establecer versión mínima de integración en `mercedev.es` antes de ampliar capacidades.
- [ ] Documentar criterio de evolución de Merci para evitar desvíos fuera del orden de fases.

## Licencia

En la raíz del repositorio no figura aún un archivo `LICENSE`; los términos de distribución y reutilización del código no están declarados en este árbol hasta que se publique dicho archivo.
