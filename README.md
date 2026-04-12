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

## Licencia

En la raíz del repositorio no figura aún un archivo `LICENSE`; los términos de distribución y reutilización del código no están declarados en este árbol hasta que se publique dicho archivo.
