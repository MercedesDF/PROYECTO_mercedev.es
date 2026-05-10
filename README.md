# mercedev.es

Base de conocimiento y centro de operaciones DevSecOps de Mercedes. Un ecosistema autónomo impulsado por Inteligencia Artificial Local (Shift-Left AI) y Desarrollo Guiado por Especificaciones (Spec-Driven Development).

Repositorio del sitio **mercedev.es**: combina un núcleo estático ultrarrápido (100/100 Core Web Vitals), una biblioteca de Decisiones de Arquitectura (ADRs) y un orquestador local en Python puro (**Sistema Merci**) con agentes de IA integrados para auto-reparación y gobernanza documental.

> 🤖 **Inteligencia y Gobernanza:** El ecosistema incluye agentes de IA locales que auto-reparan código, auto-documentan el Roadmap y generan bases de conocimiento estáticas con coste cero y privacidad total. La justificación de las decisiones DevSecOps reside en la carpeta `/docs` y en la bitácora activa.

## Requisitos

- **Python 3.10+** (requiere entorno virtual para dependencias de IA, SSG y optimización).
- **Git** y un intérprete de comandos compatible (**sh**, **bash** o **zsh**) para la integración de hooks.

## Puesta en marcha

```bash
git clone git@github.com:MercedesDF/PROYECTO_mercedev.es.git
cd PROYECTO_mercedev.es
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
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
- `merci-publish.py` y `merci-promote.py`: Motor SSG (Static Site Generation - Generación de Sitios Estáticos) y promoción de contenidos.
- `merci-sync-pages.py`: Sincronizador de estructuras comunes estáticas (SSOT en páginas independientes).
- `merci-sitemap.py` y `merci-linkcheck.py`: Rastreador dinámico (DAST) y generación de mapa XML.
- `merci-backup.py`: Creador de instantáneas ultraligeras (Snapshots).
- `merci-init.py`: Instanciador destructivo para nuevos repositorios derivados.
- `merci-linkedin.py`: Motor de autenticación OIDC (OpenID Connect) y publicación automatizada en LinkedIn.
- `merci-wp.py`: Publicador Headless para WordPress vía API REST.
- `merci-extract-metrics.py`: Extractor de métricas Core Web Vitals desde PDFs de PageSpeed Insights.
- `merci-styles.py` y `merci-watcher.py`: Compilador SASS 7-1 local y vigilante en tiempo real.
- `merci-optimizer.py` y `merci-assets-watcher.py`: Optimizador WebP y agente vigilante de activos multimedia en segundo plano.

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

El proyecto se divide en grandes "Épicas" arquitectónicas. Puedes consultar el progreso detallado y el estado de las tareas individuales en el **Roadmap Maestro (ROADMAP.md)**.

### Épica 1: Fundación DevSecOps (Fases 1-11) ✅

**Fases 1-11 (Concluidas):**
- Construcción del núcleo estático (HTML5, SASS 7-1, Vanilla JS) y los orquestadores locales en Python puro.
- Integración de WordPress como CMS Headless aislado (Proxy Nginx). 
- Aplicación estricta de metodologías *Shift-Left Security*, 
- Integración Continua (CI/CD) y rendimiento extremo, garantizando 100/100 en Core Web Vitals con 0 dependencias externas.

### Épica 2: Orquestación IA & Self-Healing (Fases 1-4) 🚧

**Fases 1-3 (Concluidas):** 
Integración de agentes de IA (Small Language Models) operando de forma 100% offline y gratuita (Ollama/LiteLLM). 
Los agentes auto-reparan el código ante fallos del linter, estructuran cuadernillos, evitan la deriva documental (Document Drift) y automatizan la publicación en redes sociales.

**Fase 4 - Observabilidad y SRE IA (En curso):** 
Transición de la automatización ciega a la gobernanza empírica basada en datos.
Despliegue de infraestructura efímera en contenedores Docker (Prometheus + Grafana) para medir la fiabilidad de los agentes de IA, simular caos (Chaos Engineering) y auditar de forma continua el endurecimiento del ecosistema.


## Licencia

Este proyecto se distribuye bajo los términos de la **Licencia MIT**. Consulta el archivo `LICENSE` para más detalles. El contenido narrativo de la biblioteca y bitácora es propiedad intelectual de su autora.
