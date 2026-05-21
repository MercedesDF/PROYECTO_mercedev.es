# mercedev.es

Repositorio oficial de mercedev.es

Plataforma experimental DevSecOps construida con Python puro, generación estática, automatización operativa e Inteligencia Artificial local.

El proyecto combina:
- Núcleo web ultraligero (100/100 Core Web Vitals).
- Arquitectura Zero-JS crítica.
- Gobernanza documental SSOT (Single Source of Truth).
- Agentes IA locales.
- Automatización DevRel.
- Observabilidad SRE.
- Auditoría continua.
- Generación estática reproducible.

Todo bajo una filosofía de Shift-Left AI, privacidad local, mínima dependencia externa, máxima trazabilidad, automatización incremental y documentación viva.

## ¿Qué es mercedev.es?

mercedev.es no es únicamente una web. Es un ecosistema operativo de ingeniería que integra:

`desarrollo → auditoría → validación → documentación → publicación → observabilidad → auto-reparación`

Todo el flujo se gobierna mediante tooling propio en Python y agentes IA locales. El objetivo del proyecto es experimentar con IA aplicada a ingeniería real, automatización gobernada, pipelines reproducibles, arquitectura estática extrema, *self-healing documentation*, DevSecOps ligero y conocimiento técnico persistente.

### Arquitectura General

```text
Developer
   ↓
merci-total
   ↓
Audit / Hardening
   ↓
SSOT / Self-Healing Docs
   ↓
Static Build
   ↓
Publish / Promotion
   ↓
Telemetry / Monitoring
```

## Características principales

**Núcleo estático ultrarrápido**
HTML estático optimizado, compilación SASS 7-1 local, WebP automatizado, enrutamiento Zero-JS crítico, CLS = 0 y TBT = 0. Arquitectura orientada a la estabilidad visual.

**Inteligencia Artificial local**
Los agentes IA funcionan localmente mediante Ollama y tooling Python propio. Capacidades actuales: auto-reparación de código, sincronización documental SSOT, validación estructural, automatización DevRel, generación de contenido técnico, auditoría contextual y *Agent Chaining* (workflows encadenados). Todo el procesamiento crítico se mantiene local para garantizar privacidad y trazabilidad.

**Gobernanza documental**
La documentación forma parte activa del sistema. El ecosistema mantiene Decisiones de Arquitectura (ADRs), un roadmap vivo, bitácoras técnicas, sincronización SSOT, validación estructural y control activo contra la deriva documental.

**DevSecOps ligero**
El proyecto prioriza la automatización reproducible, auditoría continua, reducción de la superficie de ataque, observabilidad progresiva y mínima complejidad operativa, sin depender de infraestructura pesada de terceros.

## Estructura principal

| Ruta | Contenido |
|------|-----------|
| `docs/` | Estrategia y directrices |
| `biblioteca/` | Documentación técnica definitiva (por estanterías) |
| `laboratorio/` | I+D, bandeja de entrada (`incubacion/`) y bitácoras activas del proyecto |
| `scripts/merci/` | Ecosistema DevSecOps local en Python puro |
| `assets/` | Multimedia optimizado para producción |
| `public/` | Raíz del documento del sitio estático (HTML, `robots.txt`, `sitemap.xml`; enlaces a `assets/`) |
| `.assets-raw/` | Originales sin procesar en el entorno local; Git ignora el contenido salvo `.gitkeep` (PSD/RAW/vídeo no van al remoto) |

## Ecosistema Merci

### Core Pipeline
| Script | Función |
|--------|---------|
| `merci-total.py` | Orquestador maestro |
| `merci-audit.py` | Auditoría estática y bloqueo de secretos |
| `merci-commit.py` | Commits atómicos guiados |
| `merci-init.py` | Instanciador de nuevos repositorios |

### IA & Gobernanza
| Script | Función |
|--------|---------|
| `merci-brain.py` | Orquestador IA Shift-Left |
| `merci-ssot.py` | Self-Healing Docs |
| `merci-librarian.py` | Curación documental Zero-Hallucination |
| `merci-auto-fix.py` | Auto-reparación CI |
| `merci-glosario.py` | Compilador de Glosario Autónomo |

### Publishing & DevRel
| Script | Función |
|--------|---------|
| `merci-publish.py` | Generación estática |
| `merci-telemetry.py` | Inyección de métricas del repo |
| `merci-promote.py` | Promoción automatizada |
| `merci-linkedin.py` | Publicación LinkedIn vía OIDC |
| `merci-wp.py` | Publicación Headless WordPress |

### Observabilidad & Seguridad
| Script | Función |
|--------|---------|
| `merci-sre.py` | Telemetría Prometheus/Grafana |
| `merci-hardening.py` | Auditoría continua |
| `merci-chaos.py` | Chaos Engineering local |
| `merci-linkcheck.py` | Validación de enlaces |
| `merci-drift.py` | Detección de deriva documental |

## Requisitos

- Python 3.10+
- Git
- Shell compatible (bash, zsh o sh)

## Puesta en marcha

```bash
git clone git@github.com:MercedesDF/PROYECTO_mercedev.es.git
cd PROYECTO_mercedev.es

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

### Primer arranque y auditoría

Ejecución del pipeline completo:
```bash
python3 scripts/merci/merci-total.py
```

Auditoría estática aislada:
```bash
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
-| `laboratorio/` | I+D y bitácora de proyecto (`bitacora-mercedev.md`) |
+| `laboratorio/` | I+D, bandeja de entrada (`incubacion/`) y bitácoras activas del proyecto |
| `scripts/merci/` | Ecosistema DevSecOps local en Python puro |
| `assets/` | Multimedia optimizado para producción |
| `public/` | Raíz del documento del sitio estático (HTML, `robots.txt`, `sitemap.xml`; enlaces a `assets/`). |
| `.assets-raw/` | Originales sin procesar en el entorno local; Git ignora el contenido salvo `.gitkeep` (PSD/RAW/vídeo no van al remoto). |

### Ecosistema Merci (Scripts Principales)
- `merci-audit.py`: Auditoría estática y bloqueo de secretos (SAST - Static Application Security Testing - Pruebas Estáticas de Seguridad de Aplicaciones).
- `merci-auto-fix.py`: Agente autónomo de auto-reparación de código en la nube (GitHub Actions).
- `merci-commit.py`: Empaquetado atómico impulsado por la lectura de la bitácora.
- `merci-total.py`: Orquestador maestro del pipeline local.
- `merci-brain.py`: Lóbulo frontal de Inteligencia Artificial (Shift-Left AI).
- `merci-ssot.py`: Agente Sync SSOT (Self-Healing Docs) para la curación autónoma de la deriva documental.
- `merci-librarian.py`: Agente Bibliotecario (Zero-Hallucination) para el formateo estricto de cuadernillos.
- `merci-glosario.py`: Compilador de Glosario Autónomo (Data-Driven).
- `merci-blogger.py`: Agente Redactor DevRel para marketing y automatización social (Agent Chaining).
- `merci-publish.py` y `merci-promote.py`: Motor SSG (Static Site Generation - Generación de Sitios Estáticos) y promoción de contenidos.
- `merci-sync-pages.py`: Sincronizador de estructuras comunes estáticas (SSOT en páginas independientes).
- `merci-sitemap.py` y `merci-linkcheck.py`: Rastreador dinámico (DAST) y generación de mapa XML.
- `merci-backup.py`: Creador de instantáneas ultraligeras (Snapshots).
- `merci-init.py`: Instanciador destructivo para nuevos repositorios derivados.
- `merci-linkedin.py`: Motor de autenticación OIDC (OpenID Connect) y publicación automatizada en LinkedIn.
- `merci-wp.py`: Publicador Headless para WordPress vía API REST.
- `merci-extract-metrics.py`: Extractor de métricas Core Web Vitals desde PDFs de PageSpeed Insights.
- `merci-telemetry.py`: Inyector dinámico de telemetría del proyecto (Commits, Agentes, Docs).
- `merci-styles.py` y `merci-watcher.py`: Compilador SASS 7-1 local y vigilante en tiempo real.
- `merci-optimizer.py` y `merci-assets-watcher.py`: Optimizador WebP y agente vigilante de activos multimedia en segundo plano.
- `merci-sre.py`: Demonio de telemetría pasiva para la ingesta de datos en Prometheus y Grafana.
- `merci-hardening.py`: Agente de auditoría continua de seguridad pasiva e infraestructura.
- `merci-chaos.py`: Agente de Chaos Engineering con IA local para inyección y validación de vulnerabilidades.
- `merci-drift.py`: Detector de Deriva Documental temporal y semántica.
- `merci-queue.py`: Visor de terminal interactivo para monitorizar el estado del buffer social.

## Entorno de Desarrollo Local
Para mantener la separación de responsabilidades y la alta velocidad, el desarrollo se divide en dos fases con ecosistemas distintos:

### 1. Desarrollo UI/UX Estático (Python)
Para maquetar HTML y SASS sin levantar bases de datos ni Nginx.
Se requieren dos terminales: una para ejecutar `python3 scripts/merci/merci-watcher.py` y otra en el directorio `public/` para el servidor efímero `python3 -m http.server 8000`.

### 2. Integración Dinámica WP (Nginx / LEMP)
El servidor nativo de Python **no procesa PHP (Hypertext Preprocessor - Preprocesador de Hipertexto)**. Para la fase de integración del CMS (Content Management System - Sistema de Gestión de Contenidos), es necesario detener el servidor de Python y utilizar Nginx local con la configuración de proxy inverso detallada en `docs/integracion-wordpress.md`.

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

## 🗺️ Roadmap y Estado del Proyecto

El proyecto se organiza en grandes "Épicas" arquitectónicas. El desglose detallado de tareas técnicas y métricas reside en el **`ROADMAP.md`** maestro.

- **Epic-01: Fundación DevSecOps** — Construcción del núcleo estático (100/100), integración Headless CMS y orquestadores locales en Python.
  - Estado: ✅ Completada (2026-05-06)

- **Epic-02: Orquestación IA & Self-Healing** — Agentes locales (Ollama) para auto-reparación, gobernanza documental (SSOT) y observabilidad (SRE/Grafana).
  - Estado: ✅ Completada (2026-05-13)

- **Epic-03: DevRel & Observabilidad Avanzada** — Creación de Buffer Social, DevRel, telemetría, consolidación Zero-JS y automatización de métricas JSON.
  - Estado: ✅ Completada (2026-05-21)

- **Epic-04: Showcase y Distribución del Boilerplate** — Demostración interactiva y despliegue automatizado de la plantilla pública.
  - Estado: ⏳ En cola.

- **Epic-05: E-commerce Híbrido Extremo** — Pasarelas de pago en WooCommerce aisladas con Web Workers (Partytown) para mantener TBT en 0ms.
  - Estado: ⏳ En cola.


## Licencia

Este proyecto se distribuye bajo los términos de la **Licencia MIT**. Consulta el archivo `LICENSE` para más detalles. El contenido narrativo de la biblioteca y bitácora es propiedad intelectual de su autora.
