# Bitácora del proyecto mercedev.es

## Para qué sirve este archivo

- **Yo futuro:** recuperar en minutos qué se decidió, por qué, y cómo se ejecutó algo técnico sin rebuscar en el chat o en commits sueltos.
- **Biblioteca (al cerrar el proyecto):** aquí vive el borrador narrativo y técnico; luego se depura y se traslada a `biblioteca/` como piezas definitivas (por estantería o tema), siguiendo la idea de “activo de conocimiento” del proyecto.

No sustituye a `instrucciones.md` (directrices y rol del asistente). Complementa el día a día con **hechos, comandos y lecciones**.

---

## Cómo mantenerlo (acuerdo simple)

1. **Añadir entradas al final** de la sección “Registro cronológico”, con la plantilla de abajo. El registro es **acumulativo**: lo ya escrito forma parte del historial y **no se reemplaza** por nuevas sesiones (así no se pierde contexto ni fechas).
2. **Una entrada por sesión o por tema cerrado** (lo que resulte más claro al escribir).
3. Si algo fue un error o una vulnerabilidad evitada, opcionalmente usar los **tres átomos** del proyecto (Desafío → Maniobra → Aprendizaje/Deuda) en el cuerpo de la entrada.
4. **Correcciones excepcionales** (typo, dato incorrecto, redacción de un solo párrafo, retirada de información sensible): editar solo el fragmento necesario o añadir una línea aclaratoria bajo la entrada; evitar reescribir todo el archivo o borrar entradas enteras sin motivo documentado.

### Plantilla para nuevas entradas

Copia el bloque y rellénalo.

```markdown
### AAAA-MM-DD — Título corto del cambio o sesión

**Contexto:** (qué querías lograr o qué problema apareció)

**Hecho:** (lista breve: archivos, fases del roadmap, PR/commit si aplica)

**Detalle técnico:** (comandos, rutas, flags; solo lo que necesites recordar)

**Motivo / criterio:** (por qué esta opción y no otra)

**Siguiente paso o deuda:** (qué queda pendiente)
```

---

## Registro cronológico

### 2026-04-14 — Integración de merci-sitemap.py en el hook de pre-commit

**Contexto:** Automatizar la actualización de la fecha `<lastmod>` en `sitemap.xml` cada vez que se realicen cambios en la carpeta `public/`.

**Hecho:** Modificar `scripts/merci/pre-commit`.

**Detalle técnico:**
- Se añadió lógica para detectar archivos staged en `public/`.
- Si se detectan cambios, se ejecuta `python3 scripts/merci/merci-sitemap.py`.
- Se añade `public/sitemap.xml` al índice de Git (`git add public/sitemap.xml`) para incluir su modificación en el commit actual.

**Motivo / criterio:** Asegurar que `sitemap.xml` refleje siempre la fecha de la última modificación de contenido relevante, mejorando la precisión del SEO técnico.

**Siguiente paso o deuda:** Realizar un commit de prueba que incluya cambios en `public/` para validar el funcionamiento del hook.

### 2026-04-14 — Automatización de metadatos de indexación (Sitemap)

**Contexto:** Evitar la actualización manual de la fecha de última modificación en el sitemap.xml para mejorar el SEO técnico.

**Hecho:** Crear script `scripts/merci/merci-sitemap.py` para la gestión automática de fechas en archivos XML.

**Detalle técnico:**
- Uso de la librería `datetime` para obtener la fecha del sistema.
- Empleo de `re.sub` para manipular el contenido del XML sin necesidad de parsers pesados.

**Motivo / criterio:** Mantener la consistencia entre los cambios reales y lo que se informa a los motores de búsqueda de forma automatizada.

**Siguiente paso o deuda:** Integrar la ejecución de este script en el flujo de publicación o en un hook de post-commit.

### 2026-04-14 — Cierre de Fase 1 y creación de activos de indexación (Fase 2.3)

**Contexto:** Finalización formal de la infraestructura base y configuración de la visibilidad para buscadores del núcleo estático.

**Hecho:** 
- Actualizar `README.md` para reflejar la Fase 1 como completada.
- Crear `public/robots.txt` y `public/sitemap.xml`.

**Detalle técnico:** 
- `robots.txt`: Configurado para permitir el rastreo total y apuntar al mapa del sitio.
- `sitemap.xml`: Generado con la URL canónica raíz y prioridad máxima.

**Motivo / criterio:** Cumplir con los estándares de **SEO** (Search Engine Optimization - Optimización para Motores de Búsqueda) técnico definidos en el roadmap.

**Siguiente paso o deuda:** Validar la jerarquía de encabezados (Fase 2.1) para asegurar accesibilidad.

### 2026-04-14 — Validación de Fase 2 (HTML y SEO Técnico) con Merci Audit

**Contexto:** Verificación del primer documento semántico del núcleo estático frente a las reglas de auditoría.

**Hecho:** Ejecutar `merci-audit.py --strict-json-ld` sobre `public/index.html`.

**Detalle técnico:**
- El archivo cumple con los requisitos de metadatos, charset y lenguaje.
- Se valida el bloque JSON-LD (JavaScript Object Notation for Linked Data - Notación de Objetos JavaScript para Datos Enlazados) usando el esquema de `schema.org`.

**Motivo / criterio:** Garantizar que el sitio es indexable y cumple con los estándares de rendimiento y SEO (Search Engine Optimization - Optimización para Motores de Búsqueda) desde la primera línea de código.

**Siguiente paso o deuda:** Implementar navegación (Fase 2.1) y generar `robots.txt` / `sitemap.xml` (Fase 2.3).

### 2026-04-14 — Creación de proyecto y obtención de API Key vía AI Studio

**Contexto:** El error 404 inicial no era solo de configuración de software, sino de falta de infraestructura (proyecto) en el lado de Google.

**Hecho:** Generar una API Key a través de Google AI Studio vinculada a un proyecto nuevo creado automáticamente por la plataforma.

**Detalle técnico:** 
- Acceso a `aistudio.google.com`.
- Uso de la opción "Create API key in new project" para evitar la configuración manual en GCP (Google Cloud Platform - Plataforma en la Nube de Google) Console.

**Motivo / criterio:** Vía más rápida para habilitar `gemini-1.5-pro` sin gestionar capas de facturación o cuotas complejas de Google Cloud de entrada.

**Siguiente paso o deuda:** Probar la conexión en Continue una vez la API Key esté activa y propagada.

### 2026-04-14 — Corrección de error 404 en Continue (Gemini 1.5 Pro)

**Contexto:** Fallo en la conexión con la API de Google al usar gemini-1.5-pro en Continue, con un error 404.

**Hecho:** Identificar que el `provider` en el archivo `/home/hildegahr/.continue/config.yaml` estaba configurado incorrectamente como `gemini`.

**Detalle técnico:** Modificar el `provider` de `gemini` a `google-generative-ai` para el modelo `gemini-1.5-pro` en la configuración de Continue.

**Motivo / criterio:** El `provider` `google-generative-ai` es el nombre correcto para interactuar con la API de Google Gemini a través de Continue.

**Siguiente paso o deuda:** Crear el proyecto en Google Cloud / AI Studio.

### 2026-04-12 — Fase 1: infraestructura, Merci Audit y primer commit

**Contexto:** Arranque del repositorio bajo las directrices de `instrucciones.md` (rendimiento, seguridad shift-left, pedagogía). Objetivo de la Fase 1: estructura de carpetas, script de auditoría local y base Git.

**Hecho:**

- Estructura aprobada en la raíz: `docs/`, `biblioteca/`, `laboratorio/`, `scripts/merci/`, `assets/`, `.assets-raw/` (las carpetas vacías se versionan con `.gitkeep` para que un `git clone` conserve el esqueleto).
- `scripts/merci/merci-audit.py`: auditoría con biblioteca estándar de Python (sin dependencias pip obligatorias en esta fase). Comprueba entre otras cosas patrones de secretos, sintaxis de `.py`, JSON, avisos en JS (`eval` / `new Function`) y reglas SEO mínimas en `.html` / `.htm`.
- `scripts/merci/pre-commit`: shell que ejecuta `merci-audit.py --git-staged` (solo lo que va al commit).
- Enlace local de Git: `.git/hooks/pre-commit` → `../../scripts/merci/pre-commit` (los hooks no viajan con el clone; hay que recrear el enlace en cada máquina o documentar un bootstrap).
- `.gitignore` para `.venv/`, cachés y artefactos de build; `requirements.txt` reservado para fases posteriores (p. ej. Pillow en optimizador).
- Commit inicial en rama `main` con mensaje tipo *chore: commit inicial — Fase 1 (estructura, Merci Audit, directrices)*.

**Detalle técnico:**

- Auditoría sobre todo el árbol: `python3 scripts/merci/merci-audit.py`
- Solo índice (staged), pensado para hook: `python3 scripts/merci/merci-audit.py --git-staged`
- Exigir JSON-LD en HTML cuando toque endurecer CI: flag `--strict-json-ld`
- Instalar hook (desde la raíz del repo): `chmod +x scripts/merci/pre-commit scripts/merci/merci-audit.py` y `ln -sf ../../scripts/merci/pre-commit .git/hooks/pre-commit`
- Saltar el hook solo si es deliberado: `git commit --no-verify`

**Motivo / criterio:** Automatizar comprobaciones antes de integrar cambios encaja con “seguridad shift-left” y con el papel de `merci-audit.py` descrito en instrucciones. Staged-only evita auditar el mundo en cada commit y acelera el flujo.

**Siguiente paso o deuda:** Fase 2 — HTML semántico, JSON-LD e indexación; primer documento público o plantilla que pase el audit sin `--no-verify`.

### 2026-04-12 — Registro cronológico acumulativo (no sustituir historial)

**Contexto:** Asegurar que la bitácora no pierda contexto al añadir sesiones nuevas.

**Hecho:** En `instrucciones.md` (regla 6) y en «Cómo mantenerlo» de este archivo quedó explícito: nuevas entradas **solo al final** del registro; no reemplazar ni borrar bloques ya escritos salvo corrección puntual o retirada de datos sensibles, con motivo claro.

**Detalle técnico:** N/A.

**Motivo / criterio:** El historial del laboratorio es activo de trazabilidad; sobrescribirlo rompería la línea temporal para el «yo futuro» y para el traslado a `biblioteca/`.

**Siguiente paso o deuda:** Seguir añadiendo entradas bajo «Registro cronológico» sin editar entradas previas salvo las excepciones acordadas.

### 2026-04-12 — `.assets-raw`: solo local, sin originales en Git

**Contexto:** Evitar que PSD, RAW, vídeos u otros brutos acaben en GitHub.

**Hecho:** `.gitignore` pasa a ignorar `.assets-raw/*` con excepción de `.assets-raw/.gitkeep`. `instrucciones.md` y `README.md` describen que la carpeta es convención de trabajo local y que lo versionado en `/assets` es lo optimizado.

**Detalle técnico:** Patrón en `.gitignore`: `!.assets-raw/.gitkeep` tras `.assets-raw/*`.

**Motivo / criterio:** Repositorio ligero y reproducible; los originales viven fuera del remoto (disco, NAS, etc.).

**Siguiente paso o deuda:** En Fase 3, documentar el flujo concreto `merci-optimizer.py` de `.assets-raw` → `assets/`.

### 2026-04-12 — Documentación pública sin notas personales al mantenedor

**Contexto:** Evitar frases tipo “cuando lo tengas claro añade LICENSE” en el README u otros textos versionados para GitHub.

**Hecho:** `README.md` (Licencia y otras frases) redactado en tono neutro. Nueva regla 7 en `instrucciones.md`: recordatorios al autor fuera del repo; en Git, texto útil para visitantes o colaboradores.

**Detalle técnico:** N/A.

**Motivo / criterio:** El remoto es documentación de producto/proyecto, no la libreta personal.

**Siguiente paso o deuda:** Revisar futuros `docs/` públicos con el mismo criterio.

### 2026-04-12 — Fase 2: carpeta `public/` como raíz del documento

**Contexto:** Inicio de la Fase 2 por la estructura antes del primer HTML.

**Hecho:** Directorio `public/` en el repo con `.gitkeep`; entrada en §3 de `instrucciones.md` y fila en `README.md`. Convención: aquí vive el núcleo estático servido como documento raíz; WP fuera hasta Fase 4.

**Detalle técnico:** Nombre elegido: `public/` (convención habitual de “document root” en despliegues estáticos).

**Motivo / criterio:** Separar claramente sitio servido, automatización, conocimiento y brutos locales.

**Siguiente paso o deuda:** `public/index.html` semántico + JSON-LD + `robots.txt` / `sitemap.xml` en la misma raíz cuando toque.

---

## Cuando pases esto a la biblioteca

1. **Releer** entradas y quitar ruido (intentos fallidos, datos personales, tokens aunque sean falsos).
2. **Partir por tema:** por ejemplo una ficha “Sistema Merci — auditoría pre-commit” vs “Estructura del repositorio”.
3. **Añadir los tres átomos** donde haya una decisión difícil o un incidente (síntoma, solución, lección o deuda).
4. **Enlazar** al código estable (rutas a `scripts/merci/`, no copiar bloques enormes en la biblioteca salvo que aporten lectura autónoma).

---

*Última revisión de la bitácora: 2026-04-14.*
