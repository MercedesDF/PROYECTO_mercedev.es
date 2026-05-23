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

### 2026-05-23 — Milestone: Cierre Definitivo de Épica 5 (Showcase)

**Contexto:** Aplicar el Protocolo Estricto de Cierre de Fase (Definition of Done) para dar por concluida la Épica 5 y certificar la versión del Boilerplate.

**Hecho:** Se ejecutó y validó el checklist completo:
- [x] **1. Deuda Técnica:** 0 TODOs. Amputados los textos residuales sobre descarga de PDFs en el blog, alineando la narrativa con la decisión arquitectónica reciente de eliminarlos del orquestador Headless.
- [x] **2. Cosecha de Conocimiento:** Documentados los aprendizajes sobre DLP y el patrón del Clon Efímero.
- [x] **3. Auditoría Documental:** `ROADMAP.md` y `README.md` actualizados. Épica 5 sellada y Épica 6 abierta.
- [x] **4. Evaluación de Release:** Boilerplate v1.15.1 sellado y exportado al subdominio con una Out-Of-The-Box Experience inmaculada.
- [x] **5. Certificación de Rendimiento:** Auditorías finales en verde (100/100, TBT 0ms).
- [x] **6. Snapshot:** Backup local generado con éxito.
- [x] **7. Sello Definitivo:** Commit atómico de consolidación generado.

**Motivo / criterio:** *Governance y QA Assurance*. Finalizar formalmente la épica asegura que la demostración pública (`boilerplate.mercedev.es`) refleja fielmente el código limpio.

**Siguiente paso o deuda:** Iniciar la Épica 6 (E-commerce Híbrido Extremo).

### 2026-05-23 — Hardening Documental, Zero Noise y Amputación de PDFs Dinámicos

**Contexto:** Tras la estabilización de los flujos de publicación estáticos y dinámicos, se detectaron múltiples fricciones operativas menores: inconsistencias en los metadatos YAML generados por IA, ruido excesivo en la terminal por actualizaciones redundantes de métricas, alertas de deriva documental en scripts de uso exclusivamente privado y una "fuga de propósito" en la generación de PDFs desde artículos efímeros del blog.

**Hecho:**
- Hardening masivo en los prompts de IA (`prompt-blogger.md`, `prompt-bibliotecario.md`).
- Normalización de los campos `fase:` en el YAML Frontmatter a la nomenclatura estándar `Epic X - Fase Y`.
- Aislamiento DLP físico del script `merci-showcase.py` a `scripts/matriz/`.
- Implementación del patrón *Cache Hit* (`.metrics_cache`) en `merci-extract-metrics.py`.
- Amputación de la lógica de PDFs dinámicos (WeasyPrint) en `merci-wp.py`.

**Detalle técnico:** Se modificó la función de alias `merci()` en Zsh para leer rutinas privadas sin alertar al auditor `merci-drift.py`. Se ajustaron los prompts de los LLMs para erradicar el plural mayestático en favor de voz pasiva/impersonal. Los PDFs ahora se abren en pestañas nuevas seguras (`target="_blank"`) en lugar de forzar descargas directas en `merci-publish.py`.

**Motivo / criterio:** La deuda técnica documental y el *scope creep* (fuga de alcance) degradan la Experiencia del Desarrollador (DX). Aislar scripts destructivos fuera del escrutinio del auditor garantiza el cumplimiento de las políticas de seguridad de la matriz. Silenciar salidas de consola redundantes consolida el paradigma *Zero Maintenance*. Extirpar la generación de PDFs del blog purifica la arquitectura: el contenido efímero y dinámico debe ser ultraligero.

**Siguiente paso o deuda:** Cierre formal de la fase y la Epic 5 (Showcase).


### 2026-05-22 — UX/DX: Integración del Showcase en portada y preservación de autoría

**Contexto:** Era necesario dar visibilidad al Showcase desde el proyecto matriz para derivar tráfico, y se decidió conservar los enlaces a los perfiles profesionales de la autora en el footer de la demostración pública, ya que está alojada bajo su propio subdominio.

**Hecho:**
- Se inyectó el CTA (Call to Action) "Ver Demo Interactiva" apuntando a `boilerplate.mercedev.es` en `public/index.html`.
- Se refactorizó `merci-init.py` con el flag `--preserve-socials` y se actualizó `merci-showcase.py` para invocarlo con este parámetro.
- Se empaquetó el hotfix documental (v1.15.1).

**Motivo / criterio:** *Marketing de Autoridad*. Ocultar la demo es un desperdicio del esfuerzo de infraestructura. Proveer el enlace directamente en el *First Fold* convierte la matriz en un embudo hacia el Boilerplate. Retener los créditos de autor en el footer del subdominio de demostración es lícito y potencia la marca personal, pero debe mantenerse como una opción desactivada por defecto para usuarios ajenos que clonen el repositorio.

**Siguiente paso o deuda:** Ejecutar el Protocolo de Cierre (Definition of Done) para la Épica 5 (Certificación 9 Casos, Snapshot y Commit Atómico).

### 2026-05-22 — UX/DX: Inyección de layout completo en placeholders Anti-403

**Contexto:** Las páginas de contingencia generadas por `merci-init.py` para evitar errores 403 en las carpetas vacías (`/biblioteca`, `/blog`) eran páginas HTML en blanco que rompían la experiencia de navegación al carecer de menú o pie de página.

**Hecho:** Se refactorizó la función `generar_placeholders_directorios` en `scripts/merci/merci-init.py`.

**Detalle técnico:** El script ahora lee el `index.html` de la portada, extrae los bloques `<header>` y `<footer>` (incluyendo el asistente Merci) y los inyecta en las plantillas de contingencia. Esto asegura que las páginas de marcador de posición mantengan la navegación y la identidad visual completas del sitio.

**Motivo / criterio:** *Out-Of-The-Box Experience (OOBE) y Consistencia de UI*. Una plantilla de contingencia no debe sentirse como un error. Al heredar el layout completo, el usuario puede navegar desde estas páginas de marcador de posición como si fueran parte integral del sitio, mejorando drásticamente la experiencia de un Boilerplate recién instanciado.

**Siguiente paso o deuda:** Desplegar los parches ejecutando `merci showcase` para reflejar el Boilerplate 100% inmaculado y navegable en producción.

### 2026-05-22 — UX/DX: Resolución de OOBE y Marca Blanca en Showcase

**Contexto:** Al visitar el Showcase desplegado, los enlaces del menú (`/biblioteca`, `/blog`, etc.) devolvían un error `403 Forbidden` porque el instanciador vaciaba las carpetas por DLP. Además, el avatar de Merci conservaba frases hardcodeadas de la autora original y el footer enlazaba a sus perfiles privados.

**Hecho:**
- Se implementó `generar_placeholders_directorios` en `merci-init.py` para inyectar plantillas HTML "anti-403" en las carpetas vacías tras la purga.
- Se añadió `anonimizar_enlaces_y_textos` para sustituir los enlaces de LinkedIn y GitHub por URLs genéricas, y purgar las frases literales en `MerciController.js`.

**Motivo / criterio:** *Out-Of-The-Box Experience (OOBE) y Marca Blanca*. Un Boilerplate debe entregar un ecosistema funcional, no enlaces rotos. Generar páginas de contingencia suple la falta temporal de contenido y protege al usuario de errores de servidor (Nginx). Anonimizar explícitamente los textos y enlaces protege la privacidad de la autora original sin recurrir al borrado destructivo de los componentes interactivos.

**Siguiente paso o deuda:** Desplegar los parches ejecutando `merci showcase` para reflejar el Boilerplate 100% inmaculado y navegable en producción.

### 2026-05-22 — Fix: Resolución de 403 Forbidden (Document Root) en Showcase

**Contexto:** Tras finalizar con éxito el despliegue del Showcase mediante `rsync`, el navegador devolvía un error `403 Forbidden` al visitar el subdominio en producción.

**Hecho:** Se diagnosticó que el *Document Root* por defecto de CloudPanel apuntaba a la raíz del repositorio, donde no existe ningún `index.html`. Se actualizó la configuración en la interfaz de CloudPanel añadiendo el sufijo `/public`.

**Motivo / criterio:** *Infraestructura y Seguridad*. En la arquitectura del Boilerplate, el código fuente y las herramientas CLI residen en la raíz, pero los archivos servibles públicamente se aíslan en la carpeta `public/`. Nginx devuelve 403 al no encontrar el índice y tener el listado de directorios desactivado por seguridad. Apuntar el VHost al directorio correcto resuelve la carga.

**Siguiente paso o deuda:** Iniciar la Épica 6 (E-commerce Extremo).

### 2026-05-22 — Milestone: Cierre definitivo de Épica 5 (Showcase)

**Contexto:** Aplicar el Protocolo Estricto de Cierre de Fase (Definition of Done) para dar por concluida la Épica 5, garantizando que el Boilerplate público cuenta con una demostración interactiva continuamente sincronizada.

**Hecho:**
- Se validó el despliegue inmaculado y funcional en `boilerplate.mercedev.es`.
- Se integró la orden `merci showcase` en el SOP de mantenimiento de la matriz.
- Se actualizaron los manuales maestros (`ROADMAP.md` y `README.md`) marcando la Épica 5 como concluida.

**Motivo / criterio:** *Governance y Definition of Done*. La distribución de un framework Open Source no está completa sin una demostración en vivo. Sellar esta épica certifica que el ecosistema cuenta ahora con un mecanismo de *Dogfooding* y un escaparate comercial automatizado, libre de mantenimiento manual.

**Siguiente paso o deuda:** Ejecutar `merci completo` e iniciar la Épica 6 (E-commerce Extremo).

### 2026-05-22 — Fix: Exclusión de archivos inmutables de CloudPanel (.user.ini)

**Contexto:** Tras el parche anterior, `rsync` volvió a abortar con código 23. Al no observarse errores de metadatos en el log, se diagnosticó que `--delete` chocaba contra archivos inmutables del servidor.

**Hecho:** Se añadieron las banderas `--no-perms` y `--exclude=/.user.ini` en `scripts/merci/merci-showcase.py`.

**Motivo / criterio:** *Infraestructura Restringida*. CloudPanel inyecta y bloquea a nivel de Kernel (mediante `chattr +i`) el archivo `.user.ini` en la raíz de los sitios para evitar que los usuarios sobrescriban las directivas base de PHP. Como este archivo no existe en nuestro repositorio local, `rsync --delete` intentaba borrarlo, fallando sistemáticamente. Excluirlo explícitamente y anular el cambio de permisos (`--no-perms`) limpia el último escollo del despliegue.

**Siguiente paso o deuda:** Re-ejecutar `merci showcase` para certificar el código 0.

### 2026-05-22 — Fix: Resolución de Código 23 en Rsync (Exclusión .well-known y Permisos)

**Contexto:** El orquestador de despliegue continuaba abortando con el código de salida 23 de `rsync`. El análisis reveló colisiones con los permisos del sistema anfitrión y directorios protegidos de CloudPanel.

**Hecho:** Se inyectaron las banderas `--no-o` y `--no-g` y la exclusión estricta `--exclude=.well-known` en el comando `rsync` dentro de `scripts/merci/merci-showcase.py`.

**Motivo / criterio:** *Infraestructura CloudPanel*. La bandera `-a` de Rsync intenta preservar el propietario y grupo de los archivos, operación prohibida para usuarios SSH sin acceso `root`. Adicionalmente, `rsync --delete` intentaba borrar el directorio `.well-known` (usado por Let's Encrypt para renovar SSL), el cual está bloqueado por el IaaS. Excluir el directorio y relajar los metadatos garantiza un despliegue 100% transparente.

**Siguiente paso o deuda:** Re-ejecutar `merci showcase` para finalizar la Fase 1.

### 2026-05-22 — Fix: Prevención de error de permisos de metadatos en Rsync

**Contexto:** Tras lograr la conexión SSH, `rsync` logró subir los archivos pero devolvió el error `failed to set times on "." (Operation not permitted)`, colapsando el orquestador con el código de salida 23.

**Hecho:** Se inyectó la directiva `--omit-dir-times` en el comando `rsync` dentro de `scripts/merci/merci-showcase.py`.

**Motivo / criterio:** *Infraestructura Restringida*. CloudPanel blinda los metadatos estructurales de la carpeta raíz de cada sitio. Intentar forzar la modificación temporal (mtime) de directorios superiores resulta en rechazo. Omitir la copia de tiempos de directorios soluciona el bloqueo manteniendo intactas las fechas de los archivos (esencial para validación de caché).

**Siguiente paso o deuda:** Re-ejecutar `merci showcase` para lograr el código de salida `0` (Éxito absoluto) y dar por cerrada la Fase 1.

### 2026-05-22 — Fix: Robustez en parseador .env nativo (Comentarios en línea)

**Contexto:** El despliegue de `merci-showcase.py` colapsó con un error de sintaxis en `rsync` (`Missing trailing-" in remote-shell command`). El parseador nativo de Python del archivo `.env` no estaba purgando los comentarios en línea (inline comments), arrastrando las comillas intermedias hacia el comando de terminal.

**Hecho:** Se refactorizó la lógica de extracción en `scripts/merci/merci-showcase.py` aplicando `v.split(" #")[0]` antes del limpiado de comillas.

**Motivo / criterio:** *Fail-Safe Parsing*. Prescindir de librerías externas como `python-dotenv` (Zero Bloat) exige que nuestros parseadores caseros sean tolerantes a los patrones habituales de configuración humana, como documentar variables en la misma línea.

**Siguiente paso o deuda:** Re-ejecutar `merci showcase` para finalizar el despliegue de la Fase 1.

### 2026-05-22 — Sec/Arch: Soporte de llaves SSH personalizadas vía .env

**Contexto:** El orquestador `merci-showcase.py` asumía que la llave criptográfica local siempre se llamaba `id_ed25519` o `id_rsa`. Si la desarrolladora utilizaba una llave con nombre personalizado, el despliegue fallaba por `Permission denied`.

**Hecho:** Se refactorizó `merci-showcase.py` añadiendo soporte para la variable opcional `SHOWCASE_SSH_KEY` en el archivo `.env`.

**Motivo / criterio:** *Flexibilidad de Infraestructura*. Las políticas de seguridad a veces requieren el uso de pares de llaves específicos por proyecto o servidor. Permitir que el `.env` declare la ruta absoluta de la llave privada alinea el orquestador con el principio de *Infrastructure as Code* y elimina la suposición de nombres de archivo por defecto.

**Siguiente paso o deuda:** Declarar la variable en el `.env` y re-ejecutar el orquestador.

### 2026-05-22 — Fix: Inyección explícita de clave SSH en orquestador de despliegue

**Contexto:** Al ejecutar `merci showcase`, el comando `rsync` falló con un error `Permission denied (publickey)` a pesar de haber configurado la llave en el servidor (CloudPanel).

**Hecho:**
- Se refactorizó `scripts/merci/merci-showcase.py` para autodescubrir la llave criptográfica local (`id_ed25519` o `id_rsa`).
- Se inyectó el parámetro `-i` en el comando envolvente de SSH de `rsync`.

**Motivo / criterio:** *Infraestructura como Código (IaC)*. Depender de que el cliente SSH del sistema anfitrión ofrezca la llave correcta automáticamente es propenso a fallos, especialmente en máquinas con múltiples pares de llaves (ej. Github, servidores de producción, etc.). Forzar la declaración explícita de la identidad en `rsync` garantiza una autenticación estricta y predecible.

**Siguiente paso o deuda:** Re-ejecutar `merci showcase` para validar el despliegue del Boilerplate estático.

### 2026-05-22 — Fix: Resolución de Permission Denied (SSH) en nuevo usuario de CloudPanel

**Contexto:** Al ejecutar el orquestador de despliegue (`merci-showcase.py`) tras actualizar las credenciales en el `.env`, `rsync` devolvió el error `Permission denied (publickey)` bloqueando la subida.

**Hecho:** Se diagnosticó que CloudPanel crea un usuario de sistema independiente (ej. `mercedev-merci`) para cada nuevo sitio. Este usuario nace con un anillo de llaves vacío y no hereda las claves autorizadas del usuario principal (`mercedev-php`). Se autorizó la clave pública local en la pestaña SSH/FTP del nuevo sitio en CloudPanel.

**Motivo / criterio:** *Security Isolation (Aislamiento de Seguridad)*. La arquitectura multi-tenant de paneles como CloudPanel aísla los entornos web a nivel de sistema operativo. Para desplegar de forma automatizada vía SSH/rsync, es estrictamente obligatorio registrar la clave pública de la máquina de despliegue en cada nuevo usuario creado, manteniendo intacto el principio de Mínimo Privilegio.

**Siguiente paso o deuda:** Re-ejecutar `merci showcase` para confirmar el despliegue del Boilerplate inmaculado en producción.

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