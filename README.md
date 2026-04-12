# mercedev.es

Repositorio del sitio **mercedev.es**: núcleo estático minimalista, biblioteca de conocimiento y automatización local (**Merci**).

## Requisitos

- **Python 3.10+** (para `merci-audit.py`; sin dependencias pip obligatorias en la fase actual).
- **Git** y, si usas el hook, **zsh** o cualquier shell compatible con el script de pre-commit.

## Puesta en marcha

```bash
git clone git@github.com:MercedesDF/PROYECTO_mercedev.es.git
cd PROYECTO_mercedev.es
python3 scripts/merci/merci-audit.py
```

Auditoría solo sobre lo que vas a commitear (misma lógica que el hook):

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
| `.assets-raw/` | Originales sin procesar **solo en tu disco**; Git ignora todo salvo `.gitkeep` (nada de PSD/RAW/vídeos en el remoto). |

## Directrices del proyecto

Las reglas de arquitectura, pedagogía, roadmap y convenciones están en **`instrucciones.md`**. Quien colabore o retome el repo debería leerlo antes de cambiar el stack o las fases.

## Licencia

Por definir (añade aquí `LICENSE` o la cláusula que elijas cuando lo tengas claro).
