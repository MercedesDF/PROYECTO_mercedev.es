# Bitácora del proyecto mercedev.es — Épica 5: Showcase y Distribución del Boilerplate

## Para qué sirve este archivo

Bitácora activa a partir de la finalización de la Épica 4 (Estabilización y Rendimiento Extremo).
Registra exclusivamente las decisiones, experimentos y aprendizajes de la Épica 5 (Showcase y Distribución) documentada en el `ROADMAP.md` maestro.

No sustituye a `instrucciones.md` (directrices y rol del asistente). Complementa el día a día con **hechos, comandos y lecciones**.

---

## Cómo mantenerlo (acuerdo simple)

1. **Añadir entradas al principio** de la sección "Registro cronológico" (orden cronológico inverso: lo más reciente arriba).
2. **Una entrada por sesión o por tema cerrado**.
3. Si algo fue un error o una vulnerabilidad evitada, usar los **tres átomos** del proyecto (Desafío → Maniobra → Aprendizaje/Deuda).
4. **Correcciones excepcionales**: editar solo el fragmento necesario; no borrar entradas sin motivo documentado.

### Plantilla para nuevas entradas

```markdown
### AAAA-MM-DD — Título corto del cambio o sesión

**Contexto:** (objetivo a lograr o problema surgido)

**Hecho:** (lista breve: archivos, fases del roadmap, PR/commit si aplica)

**Detalle técnico:** (comandos, rutas, flags; datos necesarios para el registro)

**Motivo / criterio:** (justificación de la decisión arquitectónica tomada)

**Siguiente paso o deuda:** (acciones pendientes o próximos hitos)
```

---

## Registro cronológico

### 2026-05-22 — Sec/Arch: Extracción de configuración de infraestructura a .env (Showcase)

**Contexto:** El script de despliegue `merci-showcase.py` mantenía las rutas del servidor (usuario SSH, dominio, path) *hardcodeadas* directamente en el código Python. Esto es un anti-patrón de infraestructura que genera deuda técnica.

**Hecho:** Se refactorizó `scripts/merci/merci-showcase.py` para parsear el archivo `.env` en tiempo de ejecución, extrayendo las nuevas claves `SHOWCASE_USER`, `SHOWCASE_HOST` y `SHOWCASE_PATH`.

**Motivo / criterio:** *Twelve-Factor App y Zero Trust*. La configuración del entorno debe estar estrictamente separada del código. Además, extraer las rutas de despliegue al archivo ignorado `.env` blinda la infraestructura en caso de que, por algún error de exclusión en el futuro, el orquestador acabara filtrado en un commit remoto.

**Siguiente paso o deuda:** Inyectar las variables en el `.env` local y sellar los cambios con un commit atómico.

### 2026-05-22 — Milestone: Despliegue de Demostración Interactiva (Showcase)

**Contexto:** Desplegar una instancia pública de la plantilla base en el subdominio `boilerplate.mercedev.es` para que los usuarios y evaluadores puedan interactuar con la arquitectura 100/100 antes de clonarla.

**Hecho:**
- Se ejecutó exitosamente el orquestador `merci-showcase.py`.
- El Clon Efímero fue purgado de datos personales e instanciado bajo el dominio de demostración.
- Se completó el hito de despliegue en la Fase 1 del Roadmap.

**Motivo / criterio:** *Dogfooding y Showcase*. Demostrar empíricamente que la instanciación de un Boilerplate genera un producto impecable y veloz en la vida real. Sincronizarlo en nuestra propia infraestructura (CloudPanel) confirma que los manuales de despliegue del proyecto son robustos.

**Siguiente paso o deuda:** Realizar el commit atómico de cierre de Fase 1 (Épica 5).

### 2026-05-22 — Fix: Resolución de Permission Denied en Clon Efímero (Symlinks)

**Contexto:** La ejecución de `merci-showcase.py` colapsó con un error `[Errno 13] Permission denied` al intentar copiar el directorio `public/blog`.

**Hecho:**
- Se diagnosticó que el error era causado por la función `shutil.copytree` al intentar seguir el enlace simbólico (`public/blog`) hacia la instalación de WordPress, la cual contiene archivos con permisos restringidos (`wp-config.php`).
- Se parcheó `scripts/merci/merci-showcase.py` añadiendo el parámetro `symlinks=True` a `shutil.copytree` y expandiendo la lista de directorios ignorados (`blog`, `tienda`).

**Motivo / criterio:** *Hardening y Aislamiento de Entornos*. La solución `symlinks=True` instruye a Python para que copie el enlace simbólico como un "acceso directo" en lugar de intentar leer su contenido, evitando así la colisión de permisos. Ignorar explícitamente las carpetas de infraestructura pesada (CMS) acelera además el proceso de clonación efímera.

**Siguiente paso o deuda:** Re-ejecutar `merci showcase` para validar el despliegue exitoso en `boilerplate.mercedev.es`.

### 2026-05-22 — Fix: Saneamiento de Deriva Documental en orquestadores de despliegue

**Contexto:** El centinela `merci-drift.py` reportó una advertencia semántica bloqueando el pipeline. El nuevo agente `merci-showcase.py` no figuraba en la biblia de la matriz (`instrucciones.md`). Adicionalmente, se detectó una fuga documental pasiva: el script aparecía en `instrucciones-merci.md`, exponiéndose al público.

**Hecho:**
- Se inyectaron `merci-showcase.py`, `merci-deploy.py` y `merci-completo.py` en `instrucciones.md`.
- Se extirpó `merci-showcase.py` del Shadow Doc `instrucciones-merci.md`.

**Motivo / criterio:** *Single Source of Truth y Data Leak Prevention*. Los scripts de despliegue son de uso estrictamente privado del proyecto matriz y de sus credenciales. Documentarlos en la biblia interna es obligatorio para `merci-drift`, pero deben ser purgados del manual que viaja con el Boilerplate para no confundir a los usuarios.

**Siguiente paso o deuda:** Ejecutar `merci-showcase.py` tras aprobar la auditoría.

### 2026-05-22 — Gov: Formalización de métricas de Release y Prevención DLP

**Contexto:** Se requería formalizar qué datos exactos muestra el Dashboard de la portada, estandarizar el proceso de certificación de rendimiento al cerrar una Epic/Fase, y blindar el script del Showcase contra fugas de datos en el Boilerplate público.

**Hecho:**
- Se actualizó el título del dashboard en `public/index.html` a "Auditoría de la última Release (Mobile 4G)".
- Se modificó la Regla 7 (Definition of Done) en `instrucciones.md` añadiendo el paso 5 "Certificación de Rendimiento (9 Casos)".
- Se inyectó la exclusión física de `merci-showcase.py` en `merci-init.py`.

**Motivo / criterio:** *QA Governance y DLP*. Las métricas de la portada son ahora un "Sello de Calidad" inmutable de la Release. Evaluar los 9 casos (Portada, Biblioteca, Blog x Escritorio, 4G, 5G) y guardar el JSON de la Portada 4G para el final asegura que el extractor inyecte el *Worst-Case Scenario*, demostrando empíricamente la robustez de la arquitectura bajo las peores condiciones.

**Siguiente paso o deuda:** Ejecutar `merci-showcase.py` para materializar el despliegue del Boilerplate estático en el subdominio de CloudPanel.

### 2026-05-22 — Arch & CD: Diseño del agente de despliegue para Showcase

**Contexto:** Se requería desplegar la demostración interactiva del Boilerplate en el subdominio `boilerplate.mercedev.es` hospedado en CloudPanel, asegurando que los datos privados de la matriz no se filtren a la web pública y manteniendo un proceso 100% automatizado.

**Hecho:**
- Se descartó el uso de repositorios intermedios o servicios externos en favor de un subdominio bajo control total (Nginx en CloudPanel).
- Se desarrolló el agente `scripts/merci/merci-showcase.py`.
- Se marcaron las tareas de evaluación y diseño de flujo como completadas en el `ROADMAP.md`.

**Motivo / criterio:** *Dogfooding y Privacy by Design*. Reutilizar nuestra propia infraestructura IaaS demuestra confianza en el stack. El script orquesta el patrón arquitectónico del "Clon Efímero": copia el proyecto a una ruta temporal, le inyecta la guillotina de `merci-init.py` para purgar telemetría/identidad y sincroniza el resultado inmaculado mediante `rsync`. Esto garantiza que el Showcase exhiba un lienzo en blanco exacto al que recibiría un usuario de GitHub, sin requerir intervención manual ni comprometer el código fuente activo de la autora.

**Siguiente paso o deuda:** Inyectar la regla DLP para `merci-showcase.py` en `merci-init.py`, ejecutar el script y validar el despliegue del Boilerplate estático.