# Bitácora del proyecto mercedev.es

## Para qué sirve este archivo

- **Yo futuro:** recuperar en minutos qué se decidió, por qué, y cómo se ejecutó algo técnico sin rebuscar en el chat o en commits sueltos.
- **Biblioteca (al cerrar el proyecto):** aquí vive el borrador narrativo y técnico; luego se depura y se traslada a `biblioteca/` como piezas definitivas (por estantería o tema), siguiendo la idea de “activo de conocimiento” del proyecto.

No sustituye a `instrucciones.md` (directrices y rol del asistente). Complementa el día a día con **hechos, comandos y lecciones**.

---

## Cómo mantenerlo (acuerdo simple)

1. **Añadir entradas al principio** de la sección “Registro cronológico”, con la plantilla de abajo. El registro es **acumulativo**: lo ya escrito forma parte del historial y **no se reemplaza** por nuevas sesiones (así no se pierde contexto ni fechas).
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

### 2026-05-02 — Fix: Exclusión de modelo experimental (Quota limit 0) en Gemini

**Contexto:** Al intentar procesar los últimos artículos, la API de Gemini devolvió un error `HTTP 429` indicando que el límite de cuota era `0` para el modelo `gemini-2.0-flash`, bloqueando la generación estática.

**Hecho:**
- Se actualizó la lista de preferencias en `auto_descubrir_modelo()` dentro de `merci-brain.py`.
- Se eliminó `gemini-2.0-flash` para forzar el uso de la versión estable `gemini-1.5-flash`.

**Detalle técnico:** Google AI Studio impone límites estrictos (o nulos) a modelos en fase experimental o de acceso anticipado según la región o el tier de la cuenta. Retirar la versión 2.0 obliga al script a utilizar la rama 1.5, la cual goza de una cuota gratuita estable de 15 RPM y 1500 peticiones diarias.

**Motivo / criterio:** *Estabilidad sobre Novedad*. En automatizaciones DevSecOps, la fiabilidad de la conexión es más crítica que el uso del último modelo disponible en el mercado.

**Siguiente paso o deuda:** Conectar el frontend (`MerciController.js`) al archivo generado una vez finalizado el escaneo.

### 2026-05-02 — Perf: Construcción incremental y control de cuotas en IA (Rate Limiting)

**Contexto:** El lóbulo frontal (`merci-brain.py`) escaneaba todos los artículos en un bucle rápido, lo que provocó que la API gratuita de Gemini rechazara las conexiones con un error `HTTP 429: Too Many Requests` (límite estricto de 5 peticiones por minuto).

**Hecho:**
- Se refactorizó `merci-brain.py` para leer el archivo `brain_data.json` antes de procesar y saltarse los artículos ya generados (Incremental Build).
- Se implementó un retraso forzado (`time.sleep(15)`) entre llamadas a la API.

**Detalle técnico:** La construcción incremental salva la cuota de la API y reduce el tiempo de compilación a 0 segundos si no hay artículos nuevos. El *Rate Limiting* (15 segundos) garantiza mantenerse dentro del límite de 4-5 RPM de la capa gratuita, evitando baneos del servidor.

**Motivo / criterio:** *Resiliencia y API Governance*. Cuando se integran servicios de terceros (SaaS), es imperativo proteger el orquestador local contra bloqueos de red limitando el consumo (Throttling) y cacheando las respuestas válidas.

**Siguiente paso o deuda:** Conectar el frontend (`MerciController.js`) al archivo generado e integrar el script en el orquestador global.

### 2026-05-02 — Feat: Shift-Left AI (Contexto dinámico inyectado en compilación)

**Contexto:** Se requería dotar al asistente de la interfaz (Merci) de inteligencia artificial para generar saludos contextualizados basados en el artículo que lee el visitante. Realizar peticiones a Gemini desde el frontend Javascript expondría la API Key y arruinaría el rendimiento web (Core Web Vitals).

**Hecho:**
- Se implementó el descubrimiento dinámico de modelos (`gemini-2.5-flash`) en `merci-brain.py`.
- Se programó un escáner de la Biblioteca que extrae el título y la descripción de cada Markdown publicado y solicita a Gemini un saludo ad-hoc.
- Se compiló la salida de la IA en un archivo estático local (`public/js/brain_data.json`).

**Detalle técnico:** Al usar expresiones regulares para leer el YAML Frontmatter, se minimiza la cantidad de tokens enviados a la API (solo se envían metadatos, no el cuerpo completo del artículo). La respuesta se asocia al `slug` del archivo y se empaqueta en JSON.

**Motivo / criterio:** *Shift-Left AI y Edge Performance*. La IA "piensa" en tiempo de compilación dentro del servidor seguro (terminal), no en tiempo de ejecución en el navegador del usuario. Esto permite a la interfaz web ofrecer respuestas generativas complejas con una latencia literal de 0 milisegundos y con coste nulo de API tras el despliegue.

**Siguiente paso o deuda:** Enseñar al frontend (`MerciController.js`) a consumir el nuevo `brain_data.json` y conectar `merci-brain.py` al orquestador maestro (`merci-total`).

### 2026-05-02 — Fix: Resolución de error 404 en conexión sináptica con Gemini (Migración a Flash)

**Contexto:** Al ejecutar la primera prueba de conexión del lóbulo frontal (`merci-brain.py`), la API REST de Google devolvió un error HTTP 404 (Not Found) al solicitar el modelo `gemini-1.5-pro`.

**Hecho:**
- Se refactorizó la URL del endpoint en `scripts/merci/merci-brain.py` para apuntar al modelo ultrarrápido `gemini-1.5-flash`.

**Detalle técnico:** La capa gratuita (v1beta) de Google Cloud / AI Studio rota frecuentemente los alias directos de las versiones Pro o exige sufijos específicos (`-latest`). El modelo Flash ofrece mayor estabilidad en el endpoint y está diseñado específicamente para tareas de baja latencia y alta eficiencia.

**Motivo / criterio:** *Rendimiento y Fricción Cero*. Dado que la IA se utilizará en tiempo de compilación (Shift-Left AI) para procesar artículos, priorizar un modelo optimizado para velocidad (Flash) acelera el flujo de construcción (Build) local y evita romper el pipeline de SSG por cambios de nomenclatura en la API de terceros.

**Siguiente paso o deuda:** Implementar la lógica para que el script lea los artículos de la biblioteca y genere respuestas estáticas (diccionarios JSON).

### 2026-05-02 — Docs: Release v1.4.0 del Boilerplate (CI/CD y Gobernanza)

**Contexto:** Tras integrar GitHub Actions y las plantillas de contribución (Fase 11), el ecosistema base adquirió capacidades de infraestructura en la nube. Era imperativo exportar estas mejoras al repositorio público para que los futuros usuarios hereden el pipeline de integración continua desde el inicio.

**Hecho:**
- Se actualizó `README-merci.md` a la versión `v1.4.0` documentando las novedades de nube y gobernanza.
- Se actualizaron los hitos de la Fase 11 en el `README.md` matriz.
- Se ejecutó el Release Pipeline hacia el repositorio derivado `merci-boilerplate`.

**Motivo / criterio:** *Configuration Drift (Deriva de Configuración)*. Todo componente de infraestructura agnóstico (como `.github/`) pertenece al producto base. Aplicar la Regla 14 de actualización iterativa asegura que el proyecto hijo posea un servidor de CI en la nube preconfigurado ("Out of the Box").

**Siguiente paso o deuda:** Finalizar los últimos hitos de la Fase 11 (Lighthouse CI) o dar el salto definitivo a la Fase 9 (Inteligencia y Autonomía).

### 2026-05-02 — Docs: Gobernanza Open Source (Pull Request Template)

**Contexto:** Tras estandarizar el reporte de *Issues*, era necesario establecer una barrera de calidad para las contribuciones de código (Pull Requests) entrantes, asegurando que los colaboradores respeten la auditoría local y la filosofía del proyecto antes de solicitar una integración.

**Hecho:**
- Se creó el archivo `.github/PULL_REQUEST_TEMPLATE.md`.
- Se incluyó un *checklist* de validación estricto (Shift-Left) en la plantilla.

**Detalle técnico:** GitHub inyecta automáticamente el contenido de este archivo en la caja de descripción cada vez que un usuario abre un nuevo Pull Request. El checklist obliga al contribuyente a confirmar explícitamente que ha ejecutado `merci-audit.py` y que no ha inyectado dependencias externas.

**Motivo / criterio:** *Gatekeeping y Shift-Left Quality*. Un repositorio público atrae contribuciones bienintencionadas pero a menudo desalineadas con la arquitectura (ej. uso de librerías NPM). El checklist actúa como una barrera psicológica y técnica que filtra el código ruidoso, protegiendo el tiempo de revisión de la mantenedora.

**Siguiente paso o deuda:** Finalizar las herramientas de la Fase 11 o transicionar a la Inteligencia y Autonomía (Fase 9).

### 2026-05-02 — Docs: Gobernanza Open Source (Issue Templates)

**Contexto:** Al abrir el Boilerplate a la comunidad o colaborar con otros desarrolladores, se corre el riesgo de recibir reportes de errores desestructurados que no aportan contexto arquitectónico ni pasos de reproducción, generando fricción operativa.

**Hecho:**
- Se crearon las plantillas de contribución `bug_report.md` y `feature_request.md` en el directorio estandarizado `.github/ISSUE_TEMPLATE/`.

**Detalle técnico:** Las plantillas utilizan Markdown con YAML Frontmatter (reconocido nativamente por GitHub) para pre-configurar etiquetas (`bug`, `enhancement`) y prefijos de commits convencionales (`fix:`, `feat:`). Su estructura obliga a quien reporta a utilizar la nomenclatura del proyecto (El Desafío / La Maniobra).

**Motivo / criterio:** *Gobernanza y Fricción Cero*. Estandarizar la entrada de información (Inbound) educa a los colaboradores en la filosofía del proyecto desde el minuto uno. Exigir contexto, entorno y justificación arquitectónica separa las contribuciones valiosas del ruido, manteniendo la higiene del repositorio.

**Siguiente paso o deuda:** Crear la plantilla para Pull Requests (`PULL_REQUEST_TEMPLATE.md`) y dar por consolidada la gobernanza del repositorio.

### 2026-05-02 — Arch: Aceptación de deuda técnica externa en GitHub Actions (Node 20)

**Contexto:** Tras inyectar la variable de entorno para forzar Node.js 24, el runner de GitHub Actions continuó emitiendo la advertencia de deprecación sobre las acciones `checkout@v4` y `setup-python@v5`.

**Hecho:**
- Se constató que el proyecto matriz no utiliza Node.js en su ecosistema.
- Se desestimó la advertencia, asumiéndola como deuda técnica de infraestructura externa.

**Detalle técnico:** El aviso proviene del código interno con el que GitHub programó los *runners* oficiales. Hasta que la plataforma no publique nuevas versiones mayores de estas acciones, la advertencia persistirá a nivel de servidor sin afectar la ejecución.

**Motivo / criterio:** *Separation of Concerns*. En DevSecOps, es vital distinguir entre una vulnerabilidad del código propio y un aviso de mantenimiento de la infraestructura anfitriona. Al tener cero dependencias de Node.js en el proyecto, este aviso no impacta en la seguridad ni el rendimiento.

**Siguiente paso o deuda:** Continuar con la configuración de Gobernanza Open Source (Issue Templates).

### 2026-05-02 — Fix: Resolución de advertencia de deprecación (Node.js 20) en GitHub Actions

**Contexto:** Tras la ejecución exitosa del primer workflow de GitHub Actions, el servidor emitió una advertencia (Warning) indicando que las acciones `checkout@v4` y `setup-python@v5` utilizan Node.js 20, el cual será descontinuado próximamente.

**Hecho:**
- Se inyectó la variable de entorno `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true` a nivel global en `.github/workflows/audit.yml`.

**Detalle técnico:** Forzar el uso de Node.js 24 adelanta la compatibilidad del pipeline y silencia la advertencia de obsolescencia que emite el runner de GitHub, asegurando un reporte de auditoría inmaculado (cero advertencias).

**Motivo / criterio:** *Zero Technical Debt (Cero Deuda Técnica)*. En la arquitectura Merci, las advertencias no se ignoran, se solucionan. Mantener el pipeline en la nube tan limpio como el orquestador local es vital para la disciplina DevSecOps.

**Siguiente paso o deuda:** Continuar con la configuración de Gobernanza Open Source (Issue y PR Templates) de la Fase 11.

### 2026-05-02 — Fix: Reubicación del workflow de GitHub Actions

**Contexto:** El workflow `Merci Audit CI` no se ejecutaba en la nube tras el *push*. Se diagnosticó que el archivo YAML fue guardado en el directorio incorrecto (`laboratorio/`).

**Hecho:** Se movió el archivo `audit.yml` a la ruta estricta obligatoria `.github/workflows/audit.yml`.

**Motivo / criterio:** *Convenciones de CI/CD*. GitHub Actions solo escanea y ejecuta los archivos de declaración de *pipelines* si residen exactamente en la carpeta oculta `.github/workflows/` de la raíz del repositorio.

### 2026-05-02 — Arch: Inicio de Fase 11 (CI/CD) y primer Workflow de GitHub Actions

**Contexto:** Tras finalizar la Fase 8, se requiere trasladar las políticas de seguridad y calidad (Shift-Left) locales hacia la nube, garantizando que ninguna contribución externa ni salto accidental de hooks locales rompa la arquitectura del repositorio público.

**Hecho:**
- Se inició formalmente la Fase 11 (Integración Continua y Calidad en la Nube).
- Se diseñó el primer flujo de GitHub Actions (`.github/workflows/audit.yml`) para automatizar la ejecución de `merci-audit.py`.

**Detalle técnico:** El workflow se configura para reaccionar ante eventos `push` y `pull_request` sobre la rama `main`. Levanta un contenedor virtual Ubuntu, instala Python 3.10 y ejecuta la auditoría estricta (`--strict-json-ld`). Si el script de Python devuelve un código de salida `1` (Error), GitHub marcará el commit con una cruz roja y bloqueará la integración del código.

**Motivo / criterio:** *Continuous Integration (CI)*. La confianza en el código no debe depender exclusivamente de la disciplina del desarrollador en su máquina local. Automatizar la auditoría en el servidor transforma las reglas documentadas en barreras físicas inquebrantables.

**Siguiente paso o deuda:** Validar la ejecución exitosa del workflow en GitHub y continuar con la Gobernanza Open Source (Issue Templates).

### 2026-05-02 — Milestone: Cierre de Fase 8 y Validación del Definition of Done

**Contexto:** Finalizar formalmente la Fase 8 (Expansión de Contenido y Contexto Inteligente) garantizando la higiene absoluta del repositorio antes de iniciar la orquestación en la nube (Fase 11).

**Hecho:** Se ejecutó y superó el Protocolo Estricto de Cierre de Fase:
- [x] **1. Deuda Técnica:** 0 TODOs pendientes. Rendimiento 100/100 retenido en vistas dinámicas.
- [x] **2. Cosecha de Conocimiento:** Cuadernillo sobre Ceguera de Proxy extraído y promovido.
- [x] **3. Auditoría Documental:** `README.md` actualizado reflejando el SSOT por Slug y el escudo Anti-Proxy.
- [x] **4. Evaluación de Release:** Versión `v1.3.1` del Boilerplate exportada con éxito (`merci-init.py` destructivo).
- [x] **5. Snapshot:** Backup local detallado generado (`merci-backup.py -v`) con un peso optimizado de 1.51 MB.
- [x] **6. Sello Definitivo:** Commit atómico en preparación.

**Detalle técnico:** La fase concluye demostrando empíricamente la viabilidad de la arquitectura híbrida (Dev/Prod Parity). El enrutamiento dinámico resuelve las URIs sin colisiones mediante *slugs*, la UI se mantiene purista y la base de datos local ha sido purgada de "posts zombis" (Data Drift). 

**Motivo / criterio:** *Governance y Definition of Done (DoD)*. Sellar el repositorio mediante un checklist auditable previene la transferencia de deuda técnica entre fases. Al saltar directamente a la Fase 11 (CI/CD), el código fuente debe estar inmaculado para que los corredores (runners) en la nube no fallen por problemas de configuración local heredados.

**Siguiente paso o deuda:** Iniciar oficialmente la Fase 11: Integración Continua y Calidad en la Nube (CI/CD con GitHub Actions).

### 2026-05-02 — Docs: Actualización v2.0 del cuadernillo de Alias Inteligentes

**Contexto:** La función Bash `merci` original era rígida y no permitía pasar argumentos adicionales (flags como `-v` o rutas de archivos) a los scripts subyacentes, limitando el uso de herramientas dinámicas como el orquestador de backups o el publicador de WordPress.

**Hecho:**
- Se actualizó el cuadernillo `Alias Inteligentes-bitacora.md` a su versión 2.0.
- Se documentó la inyección de la variable `${@:2}` para admitir parámetros infinitos.
- Se añadió la instrucción de recarga en caliente de la terminal (`source ~/.zshrc`).

**Detalle técnico:** La variable de expansión `${@:2}` captura todos los argumentos a partir del segundo y los traslada al script de Python. Se utilizó el flujo de trabajo estándar (Kill-Switch) para degradar el cuadernillo a borrador en el laboratorio, aplicar el bloque de conocimiento y volver a promoverlo a la biblioteca mediante `merci-promote.py`.

**Motivo / criterio:** *Mejora Continua (Continuous Improvement) y Gestión del Conocimiento*. Los activos de la biblioteca deben ser documentos vivos. Reflejar los parches operativos (como la recarga en caliente y el paso de argumentos) asegura que los futuros usuarios del Boilerplate dispongan de la versión más pulida y eficiente de las herramientas de terminal.

**Siguiente paso o deuda:** Iniciar la Fase 9 (Inteligencia y Autonomía).

### 2026-05-02 — QA: Certificación "Cuádruple 100" en capa dinámica tras refactorización Headless

**Contexto:** Tras erradicar los "posts zombis" de la base de datos local y refactorizar el publicador Headless (`merci-wp.py`) para utilizar resolución dinámica por slug, era imperativo certificar que la arquitectura seguía rindiendo al máximo nivel en producción.

**Hecho:** Se ejecutó una auditoría externa de Google PageSpeed Insights sobre la ruta dinámica de WordPress `/blog/category/art-de-cote/` bajo simulación de red móvil 4G.

**Detalle técnico:** Se logró una puntuación perfecta (100 Rendimiento, 100 Accesibilidad, 100 Mejores Prácticas, 100 SEO). Las métricas Core Web Vitals se mantienen inmaculadas: FCP 0.8s, LCP 1.1s, TBT 0ms y CLS 0. La corrección WAI-ARIA de enlaces de tarjetas y la purga de dependencias JS bloqueantes se validaron con éxito.

**Motivo / criterio:** *QA Assurance y Performance Driven Development*. Lograr 0 ms de Tiempo de Bloqueo Total (TBT) en una vista generada por un CMS pesado demuestra el éxito absoluto del "Escudo de Rendimiento" (desencolado estricto de scripts y bloques en `functions.php`). Certifica que el proyecto cumple sus propios estándares fundacionales y está listo para ser empaquetado como Boilerplate v1.3.1.

**Siguiente paso o deuda:** Ejecutar el Release Pipeline, el Backup Local y el Commit Atómico para cerrar oficialmente la Fase 8 e iniciar la Fase 9 (Inteligencia).

### 2026-05-02 — Docs: Documentación arquitectónica de orquestadores (QUÉ HACE/POR QUÉ)

**Contexto:** La complejidad alcanzada por el publicador Headless (`merci-wp.py`) requería blindar el conocimiento de sus funciones contra futuras refactorizaciones.

**Hecho:** Se estandarizaron los docstrings y comentarios internos de `scripts/merci/merci-wp.py` siguiendo el formato "QUÉ HACE" y "POR QUÉ".

**Detalle técnico:** Explicar explícitamente decisiones como el parseo nativo de YAML, la inyección dual de credenciales y el uso de `slugify`.

**Motivo / criterio:** *Mantenibilidad y Pedagogía*. Un Boilerplate no solo hereda código, sino criterio. Forzar la documentación de la *intención* previene que futuros desarrolladores eliminen piezas clave (como las cabeceras anti-WAF) por considerarlas "redundantes".

### 2026-05-02 — Arch: SSOT Dinámico por Slug (Erradicación de wp_id estático)

**Contexto:** El uso de un `wp_id` inyectado en el YAML local provocaba errores 404 al intentar actualizar artículos tras cambiar el entorno de localhost a producción, ya que los IDs de la base de datos no coincidían y el script intentaba actualizar un ID inexistente.

**Hecho:**
- Se eliminó la lectura e inyección de `wp_id` en el script `merci-wp.py`.
- Se implementó la función `obtener_id_por_slug()` para interrogar a la API REST de destino.

**Detalle técnico:** En lugar de depender del ID local, el script utiliza el nombre del archivo (`target_path.stem`) para preguntar "¿Existe un post con este slug en este entorno?". Si existe, captura su ID remoto temporalmente en memoria y ejecuta un `PUT`; si no, ejecuta un `POST`.

**Motivo / criterio:** *Paridad Dev/Prod Absoluta*. El archivo Markdown se vuelve verdaderamente agnóstico. Al usar el *slug* (el nombre físico del archivo) como clave primaria universal, podemos sincronizar exactamente el mismo documento contra infinitas bases de datos sin colisiones ni corrupción de IDs.

### 2026-05-02 — Fix: Evasión de escudos WAF y proxies (User-Agent corporativo)

**Contexto:** Nginx en CloudPanel devolvía errores 404/403 al intentar interrogar la API REST de WordPress para buscar categorías (ej. `?search=Blog`).

**Hecho:** Se inyectó la cabecera `User-Agent: Merci-Boilerplate-Agent/1.0` en todas las peticiones HTTP dentro de `merci-wp.py`.

**Detalle técnico:** Los firewalls (WAF) y proxies de alto rendimiento bloquean automáticamente agentes de usuario genéricos de librerías como `Python-urllib` asumiendo que son bots maliciosos de *scraping*. 

**Motivo / criterio:** *Identidad de Ecosistema y Bypass Seguro*. Forjar un Agente de Usuario legítimo permite al orquestador atravesar la frontera de Nginx. Además, habilita la trazabilidad forense en los archivos `access.log` del servidor, permitiendo distinguir el tráfico del Boilerplate de los ataques reales.

### 2026-05-02 — Fix: Ceguera de HTTPS en WordPress detrás de Proxy Varnish

**Contexto:** WordPress en producción ocultaba la opción para generar Contraseñas de Aplicación, asumiendo falsamente que el entorno era inseguro (HTTP), a pesar de que CloudPanel servía la web por HTTPS validado.

**Hecho:**
- Se inyectó temporalmente `$_SERVER['HTTPS'] = 'on';` en `wp-config.php` de producción.
- Ante la agresividad de OPcache/FastCGI sobrescribiendo variables globales, se recurrió a la extracción directa de la credencial mediante terminal usando WP-CLI (`wp user application-password create`).

**Detalle técnico:** CloudPanel termina la conexión SSL (offloading) en Nginx y pasa el tráfico interno a PHP por HTTP normal. WP detecta HTTP en entorno de producción y, por seguridad nativa innegociable, bloquea la API de contraseñas. Extraer la clave por terminal salta completamente el servidor web y dialoga directamente con el motor de base de datos.

**Motivo / criterio:** *Infraestructura como Código (IaC)*. Cuando las capas de caché profunda o los proxies ofuscan la Interfaz Gráfica (GUI), descender a la capa del sistema operativo (WP-CLI) es la vía más profesional y segura para aprovisionar herramientas sin alterar permanentemente configuraciones delicadas del servidor web.

### 2026-05-02 — Fix: Bypass de "Ceguera de Proxy" (Autorización REST API)

**Contexto:** Al apuntar el publicador Headless (`merci-wp.py`) a producción, el proxy inverso CloudPanel/Varnish interceptaba y purgaba la cabecera HTTP estándar `Authorization: Basic`, desnudando la petición y provocando que WP la rechazara con un error 401 Unauthorized.

**Hecho:**
- Se implementó un envío dual de credenciales en Python inyectando una cabecera personalizada gemela (`X-Authorization`).
- Se inyectó un parche en `src/wp-theme/merci-theme/functions.php` para restaurar la cabecera oficial en el servidor: `$_SERVER['HTTP_AUTHORIZATION'] = $_SERVER['HTTP_X_AUTHORIZATION']`.

**Detalle técnico:** Los proxies de alto rendimiento están configurados para no cachear peticiones con `Authorization` o purgarla por seguridad. Las cabeceras personalizadas (`X-*`) no son filtradas y atraviesan Varnish intactas. Al llegar a PHP, el filtro de nuestro tema restaura la variable global en memoria justo antes de que WP valide al usuario.

**Motivo / criterio:** *Shift-Left Routing*. En lugar de crear complejas excepciones en la infraestructura de Nginx de CloudPanel (lo que generaría deriva de configuración entre local y nube), solucionarlo a nivel de código de aplicación asegura que el ecosistema funcione en cualquier hosting o proxy del mercado (Agnosticismo de Infraestructura).

### 2026-05-02 — Arch: Conmutador de Entornos (Environment Switcher) en .env

**Contexto:** Se necesitaba un flujo de trabajo que permitiera publicar el mismo archivo Markdown primero en localhost (para pruebas y QA) y luego en producción, sin mezclar credenciales ni alterar el código fuente de los automatismos en Python.

**Hecho:** Se consolidó el uso del archivo `.env` local como un "Conmutador de Vías".

**Detalle técnico:** El archivo `.env` ahora alberga bloques comentados (`#`) independientes para cada entorno (Localhost y Producción). Alternar los comentarios redefine dinámicamente hacia qué servidor apuntan las peticiones de `merci-wp.py`.

**Motivo / criterio:** *Dev/Prod Parity y Simplicidad*. Este enfoque no requiere librerías complejas de gestión de variables de entorno ni comandos extra. Combinado con la resolución dinámica de IDs por *slug*, permite a la desarrolladora incubar en local y desplegar en la nube de forma secuencial usando exactamente los mismos comandos de terminal, garantizando cero colisiones.

### 2026-05-02 — Arch: Resolución dinámica de IDs multi-entorno en Headless CMS

**Contexto:** Al intentar publicar los artículos en el servidor de producción, se evidenció que los archivos Maqrkdown locales contenían atributos `wp_id` asociados a la base de datos de localhost, provocando colisiones de entorno al apuntar el script a la API REST de producción.

**Hecho:** Se refactorizó `scripts/merci/merci-wp.py` para implementar búsqueda dinámica de existencia por `slug`.

**Detalle técnico:** Inyectar la función `obtener_id_por_slug()`. Antes de realizar el POST/PUT, el script interroga al WordPress de destino. Si el artículo ya existe en ese servidor, asume el ID remoto (`entorno_id`), ignorando el `wp_id` escrito en el YAML local.

**Motivo / criterio:** *Dev/Prod Parity (Multi-entorno)*. Depender de un único ID estático en el archivo acopla el código a una sola base de datos. La resolución dinámica permite que el mismo archivo Markdown se sincronice indistintamente contra Localhost, Staging o Producción sin corromper las bases de datos de destino.

### 2026-05-02 — Docs: Release v1.3.0 del Boilerplate y Cierre de Fase 8

**Contexto:** Tras consolidar la paridad absoluta entre el motor SSG y el Headless CMS (generación de PDFs, extracción de resúmenes y SSOT de slugs) y fortificar la documentación contra "posts fantasma" (Data Drift), era imperativo empaquetar estos avances antes de iniciar nuevas lógicas de desarrollo.

**Hecho:**
- Se ejecutó el Release Pipeline exportando el código limpio al repositorio `merci-boilerplate`.
- Se dio por concluida oficialmente la Fase 8 (Expansión de Contenido y Contexto Inteligente).

**Detalle técnico:** Ejecutar el orquestador destructivo `merci-init.py` para ascender los *Shadow Docs* actualizados (README v1.3.0 y el nuevo SOP maestro público) y purgar con éxito todos los borradores residuales, garantizando un ecosistema inmaculado para los usuarios del Boilerplate.

**Motivo / criterio:** *Release Management y Zero Technical Debt*. Aplicar el cierre formal de fase (Definition of Done) exige liberar el ecosistema de "deuda de despliegue". Iniciar el desarrollo de la Fase 9 o Fase 11 sobre un código base no sincronizado con su plantilla matriz es una práctica propensa a crear bifurcaciones problemáticas.

**Siguiente paso o deuda:** Iniciar la Fase 9 (Inteligencia y Autonomía) o Fase 11 (CI/CD Cloud).

### 2026-05-02 — Docs: Reubicación y ampliación del SOP de Publicación Dual

**Contexto:** Tras el incidente de los posts fantasma (Data Drift) por borrado manual de archivos, se evidenció que las reglas de publicación son críticas no solo para el proyecto matriz, sino para cualquier usuario futuro del Boilerplate.

**Hecho:**
- Se movió el archivo `flujo-publicacion-sop.md` desde el directorio privado `docs/matriz/` hacia el directorio público `docs/`.
- Se añadió la "Regla de Oro" sobre la Prevención de Posts Fantasma, prohibiendo el borrado manual de archivos `.md` sincronizados sin antes aplicar el Kill-Switch (`estado: "borrador"`).

**Motivo / criterio:** *Knowledge Export (Exportación de Conocimiento)*. Las mecánicas de sincronización Headless y SSG son el núcleo funcional del producto. Restringir este manual a la matriz ocultaría al usuario final del Boilerplate cómo utilizar el ecosistema de forma segura, provocándoles la misma deuda técnica de desincronización que acabamos de sufrir.

**Siguiente paso o deuda:** Iniciar la Fase 9 (Inteligencia y Autonomía) o Fase 11 (CI/CD).

### 2026-05-02 — Fix: Erradicación de posts fantasma (Data Drift) en Headless CMS

**Contexto:** El orquestador `merci-total` falló en la etapa de rastreo de enlaces (`merci-linkcheck.py`) reportando un 404 en el PDF de `mi-primer-post-automatizado`. El archivo Markdown original había sido eliminado localmente sin pasar por el proceso de despublicación formal.

**Hecho:** Se purgó manualmente la entrada residual desde el panel de administración de WordPress local.

**Detalle técnico:** El script `merci-publish.py` borra la carpeta `descargas/` (Clean Build). Posteriormente, `merci-wp.py` genera PDFs solo para los archivos `.md` existentes en el directorio. Al no existir el archivo local, su PDF no se regenera, pero como WordPress nunca recibió la orden REST de borrarlo, el CMS continuaba sirviendo el post público con un enlace a un archivo inexistente.

**Motivo / criterio:** *Higiene Headless y Data Drift*. En una arquitectura desacoplada y unidireccional, borrar un archivo fuente de producción manualmente provoca "posts zombis". La despublicación debe delegarse siempre al "Kill-Switch" automatizado (cambiar a `estado: "borrador"` y ejecutar `merci wp`) antes de borrar el fichero físico localmente.

**Siguiente paso o deuda:** Iniciar la Fase 9 (Inteligencia de Merci) o Fase 11 (CI/CD).

### 2026-05-01 — Fix: Resolución de deriva de slugs (SSOT) entre SSG y Headless CMS

**Contexto:** El rastreador local (`merci-linkcheck.py`) detuvo el pipeline reportando errores 404 en las descargas de PDFs de WordPress. Python generaba los PDFs basándose en el título crudo del Markdown, pero WordPress asignaba "slugs" distintos (ej. añadiendo `-2`) para evitar colisiones en su base de datos.

**Hecho:**
- Se refactorizó `scripts/merci/merci-wp.py` retrasando la generación del PDF mediante WeasyPrint.
- Se redactó el cuadernillo `cuadernillo-ssot-slugs-wp.md` en el laboratorio documentando el incidente.

**Detalle técnico:** Se movió el bloque de generación del PDF al interior de la respuesta exitosa de la API REST (`urllib.request.urlopen`). Ahora, el script extrae el campo `slug` del JSON devuelto por WordPress y utiliza exactamente esa cadena de texto como nombre físico para el archivo `.pdf` (`out_pdf_filename = f"{wp_slug}.pdf"`).

**Motivo / criterio:** *Single Source of Truth (SSOT)*. En un sistema distribuido, la base de datos es la única fuente de verdad para las URIs. Obligar al generador estático (Python) a esperar la respuesta del motor dinámico (WordPress) garantiza la paridad absoluta entre el enlace web renderizado y el archivo físico en el disco duro.

**Siguiente paso o deuda:** Ejecutar `merci total` para validar el pipeline a 0 errores y actualizar el `README-merci.md`.

### 2026-05-01 — QA: Silenciado de falsos positivos en linter de estilos (UI_INLINE_STYLE)

**Contexto:** La primera pasada del nuevo linter de estilos en línea arrojó 3 advertencias (`WARN UI_INLINE_STYLE`) en el HTML compilado de `la-guerra-de-la-especificidad-css.html`. El diagnóstico reveló que correspondían a fragmentos de código educativo documentados en el propio artículo.

**Hecho:**
- Se inyectó la directiva `<!-- merci-audit:silence-style -->` al final de las líneas afectadas en el archivo Markdown original (`biblioteca/cuadernillo-la-guerra-de-la-especificidad-css.md`).

**Detalle técnico:** El auditor no discrimina si la cadena `style="..."` se encuentra renderizada dentro de una etiqueta `<code>` o en un componente estructural. En lugar de aplicar sobreingeniería a las expresiones regulares del linter (lo cual es propenso a fallos), se emplean los marcadores de silenciamiento explícitos nativos de la herramienta.

**Motivo / criterio:** *Fail Gracefully y Falsos Positivos*. Exigir una herramienta estricta implica dotarla de válvulas de escape intencionales. Utilizar el silenciamiento en línea certifica que el desarrollador ha revisado manualmente el hallazgo y asume que es arquitectónicamente seguro, manteniendo la alerta activa para verdaderas violaciones de estilo.

**Siguiente paso o deuda:** Re-ejecutar `merci total` para confirmar el *Zero Warnings* y proceder con la Fase 9 o Fase 11.

### 2026-05-01 — QA: Linter de estilos en línea (UI_INLINE_STYLE)

**Contexto:** Para proteger la arquitectura SASS 7-1 y la metodología BEM, se requería automatizar la detección de estilos en línea (`style="..."`) inyectados en el HTML o en las plantillas PHP, los cuales generan deuda técnica y problemas de especificidad.

**Hecho:**
- Se implementó la regla `audit_inline_styles` en `scripts/merci/merci-audit.py`.

**Detalle técnico:** El linter utiliza una expresión regular para detectar atributos `style=` en archivos `.html`, `.php`, `.js` y `.py`. Evalúa las coincidencias y emite una advertencia (`WARN`). Se implementó una excepción explícita para los estilos del ancla invisible WAI-ARIA (`#top`) para evitar falsos positivos arquitectónicos.

**Motivo / criterio:** *Shift-Left Quality*. En lugar de crear un script independiente que añada fricción operativa, integrar esta validación en el auditor maestro asegura que la comprobación se ejecute automáticamente antes de cada commit. Las advertencias no bloquean el flujo, pero visibilizan la deuda técnica inmediatamente.

**Siguiente paso o deuda:** Ejecutar el auditor para escanear el proyecto en busca de estilos en línea residuales.

### 2026-05-01 — Refactor: Unificación de metadatos y UI responsiva en Biblioteca

**Contexto:** Se detectó una alta entropía en los YAML Frontmatter de la `biblioteca/` (campos `volumen` innecesarios, falta de `tipo`, descripciones y `alt_portada` rotos). Además, en la vista móvil, las secciones de la biblioteca (`.library-section`) carecían de *padding* lateral, pegando el contenido a los bordes del dispositivo.

**Hecho:**
- Se estandarizó el Frontmatter de los cuadernillos para asegurar un parseo SSG uniforme.
- Se creó el archivo fundacional `docs/plantilla-cuadernillo.md` para prevenir futuras derivas de formato.
- Se inyectó `padding: 0 $spacing-lg;` responsivo en el componente `.library-section` (SASS).

**Motivo / criterio:** *Single Source of Truth (SSOT) y Mobile First*. La ausencia de una plantilla estricta para "cuadernillos" provocaba que los archivos heredaran metadatos obsoletos (como `volumen:` o `portada:`). La corrección CSS alinea el comportamiento del contenedor `.library-section` con la navegación superior, restaurando el 100/100 en usabilidad móvil.

**Siguiente paso o deuda:** Recompilar SASS, ejecutar QA (`merci total`) y proceder a empaquetar el commit atómico.

### 2026-05-01 — QA: Resolución de colisión de enlaces ancla (WAI-ARIA) en el SSG

**Contexto:** El pipeline se detuvo en la fase de `merci-linkcheck.py` al detectar enlaces ambiguos en el índice de la Biblioteca. El nombre de la estantería "Art de Coté" generó enlaces ancla (`#art-de-cote`) que colisionaban con el enlace homónimo del menú de navegación global (`/blog/category/art-de-cote/`).

**Hecho:**
- Se parcheó `scripts/merci/merci-publish.py` para inyectar dinámicamente atributos `aria-label` en los enlaces de las estanterías temáticas.

**Detalle técnico:** Se transformaron los anclajes para que posean nombres accesibles únicos como `aria-label="Explorar estantería: {tema}"`. El texto visual se mantiene inalterado, pero los lectores de pantalla y las herramientas de auditoría ahora logran diferenciar semánticamente el enlace de ancla interno del enlace de navegación estructural.

**Motivo / criterio:** *Shift-Left Accessibility*. Las colisiones WAI-ARIA son inevitables cuando el contenido generado dinámicamente (SSG) hereda nombres que coinciden con elementos estructurales. Garantizar identificadores únicos a nivel de compilador evita tener que limitar la nomenclatura que elija el autor.

**Siguiente paso o deuda:** Re-ejecutar el pipeline maestro para certificar 0 errores y proceder al commit.

### 2026-05-01 — QA: Validación End-to-End del publicador social (LinkedIn)

**Contexto:** Se necesitaba certificar que el ecosistema completo funcionara en cadena (Laboratorio -> Promote -> WordPress -> LinkedIn) extrayendo el texto multilínea correctamente tras la migración a comentarios HTML.

**Hecho:**
- Se ejecutó con éxito el pipeline completo sobre un artículo real.
- Se actualizó el `README.md` marcando la automatización de LinkedIn y la Fase 8 como completadas.

**Detalle técnico:** El orquestador `merci-linkedin.py` localizó exitosamente el marcador `wp_id`, extrajo el bloque `<!-- linkedin: ... -->` preservando los saltos de línea, publicó a través de la API OIDC y selló el archivo local inyectando el `linkedin_id` de forma atómica.

**Motivo / criterio:** *QA de Integración (End-to-End Testing)*. Un desarrollo no se da por terminado hasta que se valida empíricamente su funcionamiento en el entorno final de producción. Con este éxito, la Fase 8 queda formalmente clausurada y la arquitectura de distribución consolidada.

**Siguiente paso o deuda:** Iniciar la Fase 9 (Inteligencia y Autonomía) o saltar a la Fase 11 (CI/CD Cloud).

### 2026-05-01 — Fix: Resolución de truncamiento de texto multilínea YAML (merci-promote)

**Contexto:** Al promocionar un artículo y enviarlo a LinkedIn, la red social publicó un post vacío que solo contenía el símbolo `|`. Se diagnosticó que `merci-promote` (y otros scripts) utilizan un parseador YAML rudimentario (`split(":")`) que destruyó el bloque de texto multilínea al no encontrar el delimitador de clave-valor en las líneas inferiores.

**Hecho:**
- Se refactorizó `merci-linkedin.py` para leer el texto a publicar desde un comentario HTML (`<!-- linkedin: ... -->`) ubicado en el cuerpo del documento (`md_body`).
- Se actualizaron las plantillas (`plantilla-blog.md`, `plantilla-art-de-cote.md`) para retirar el campo `linkedin_post` del YAML Frontmatter e inyectar el bloque HTML oculto.

**Detalle técnico:** Implementar un parseador YAML completo en Python nativo para soportar *block scalars* (bloques multilínea) requiere miles de líneas de código o añadir la dependencia externa `PyYAML`. Extraer la responsabilidad del texto largo hacia el cuerpo del Markdown (escondiéndolo en un comentario HTML que los navegadores ignoran) sortea la limitación técnica manteniendo la directriz de "0 dependencias bloqueantes".

**Motivo / criterio:** *Robustez vs. Deuda Técnica*. Si una herramienta casera tiene límites estructurales, adaptar el formato de entrada (Markdown) es infinitamente más seguro y mantenible que intentar reinventar la rueda programando un parseador complejo propenso a errores.

**Siguiente paso o deuda:** Validar la republicación en LinkedIn con texto multilínea intacto.

### 2026-04-30 — DevSecOps: Bloqueo de token OIDC de LinkedIn en control de versiones

**Contexto:** Durante las pruebas del motor de LinkedIn, el instinto DevSecOps alertó sobre la posible inclusión accidental del archivo de credenciales (`.linkedin_token.json`) en el commit automático, ya que no había sido excluido en la configuración pasiva.

**Hecho:**
- Se ejecutó `git reset --soft HEAD~1` y `git rm --cached .linkedin_token.json` para expurgar el token del historial local.
- Se añadió el archivo `.linkedin_token.json` al `.gitignore`.
- Se parcheó `scripts/merci/merci-audit.py` para incluir este archivo en la lista estricta de `BANNED_TRACKED_FILE`.

**Detalle técnico:** El script `merci-commit.py` ejecuta `git add .` automáticamente. Sin la exclusión, el token OAuth habría viajado al repositorio público. Inyectar el archivo en la regla `BANNED_TRACKED_FILE` del auditor garantiza un "fail-fast", bloqueando atómicamente cualquier commit si Git intenta rastrearlo en el futuro.

**Motivo / criterio:** *Shift-Left Security y Zero Trust*. Los tokens OIDC poseen permisos de escritura y representan un riesgo crítico de seguridad si se filtran. La política exige que el escudo activo (el auditor pre-commit) conozca la existencia de nuevos archivos de credenciales para interceptarlos infaliblemente en caso de que fallen las exclusiones pasivas.

**Siguiente paso o deuda:** Finalizar el commit atómico saneado y verificar si la publicación en LinkedIn fue exitosa.

### 2026-04-30 — Feat: Motor de Publicación Automática en LinkedIn (SSOT Estricto)

**Contexto:** Tras asegurar la obtención del *Access Token* (OIDC), era necesario desarrollar el módulo de publicación. Se debatió si el script de LinkedIn debía leer los artículos directamente de la API del servidor web de producción para garantizar que solo se publicaran artículos "reales".

**Hecho:**
- Se amplió `scripts/merci/merci-linkedin.py` implementando la inyección a la API y el parseo YAML local.
- Se estableció la validación estricta de pre-existencia web: el script solo lee archivos locales que posean el marcador `wp_id`.

**Detalle técnico:** Leer del servidor web destruiría el texto personalizado del campo `linkedin_post`. Al exigir que el archivo Markdown local contenga `wp_id`, usamos la inyección previa de `merci-wp.py` como garantía irrefutable de que el contenido está vivo en producción. Si se cumplen las condiciones, realiza un POST a `/v2/ugcPosts` e inyecta el `linkedin_id` para prevenir duplicados.

**Motivo / criterio:** *Decoupling y Single Source of Truth*. Separar los scripts por canal (uno para WP, otro para LinkedIn) aísla los fallos de las APIs externas. Confiar en la firma YAML local unifica el flujo: el Markdown es el único DNI del artículo.

**Siguiente paso o deuda:** Crear un artículo de prueba, promoverlo, publicarlo en WP y ejecutar el script para ver el post real en LinkedIn.

### 2026-04-30 — Feat: Motor de Autenticación OIDC para LinkedIn (Cero Dependencias)

**Contexto:** Para automatizar las publicaciones en LinkedIn (Fase 8.3) con robustez a largo plazo, se descartó el uso de tokens estáticos manuales en favor del flujo completo "Three-legged OAuth 2.0" (OIDC), permitiendo al script gestionar y renovar sus propias credenciales.

**Hecho:**
- Se configuró la aplicación en el portal de desarrolladores de LinkedIn (Scopes: `openid`, `profile`, `w_member_social`).
- Se desarrolló el motor base en `scripts/merci/merci-linkedin.py` utilizando la librería estándar `http.server` y `urllib`.

**Detalle técnico:** El script levanta un `HTTPServer` efímero en el puerto 8000 que bloquea la ejecución (`handle_request()`) hasta atrapar el *callback* del navegador. Extrae el código `?code=XYZ`, realiza el POST de intercambio por el *Access Token* y lo guarda físicamente en el archivo seguro `.linkedin_token.json`.

**Motivo / criterio:** *Zero Bloat & Autonomía*. Programar un servidor web de un solo uso en lugar de importar librerías pesadas como `Flask` o `requests_oauthlib` demuestra la potencia de Vanilla Python. Este flujo garantiza que la integración no colapse por caducidad de tokens en el futuro.

**Siguiente paso o deuda:** Ejecutar el script por primera vez para generar el token inicial, y luego diseñar la función para publicar un post real enviando datos a la API de LinkedIn.

### 2026-04-30 — Arch: Pivote estratégico hacia automatización social (LinkedIn)

**Contexto:** Tras validar el MVP de la tienda WooCommerce (diseño, inyección headless, paridad de entornos), se determinó que su propósito principal como demostración técnica estaba cumplido. El valor de negocio inmediato no reside en la venta de merchandising, sino en la difusión de estos logros técnicos.

**Hecho:**
- Se aparca formalmente el desarrollo de la tienda.
- Se re-prioriza como hito inmediato el desarrollo del script de automatización para LinkedIn (`merci-linkedin.py`), retomando la Fase 8.3.

**Motivo / criterio:** *Business Value vs. Technical Exercise*. La tienda ha servido como un caso de estudio perfecto para demostrar la integración de un e-commerce en una arquitectura Headless de alto rendimiento. Ahora, el Retorno de la Inversión (ROI) es mayor si se capitaliza este logro mediante la difusión en redes profesionales, en lugar de seguir añadiendo funcionalidades a un escaparate no comercial.

**Siguiente paso o deuda:** Diseñar la arquitectura de autenticación (OAuth 2.0) para `merci-linkedin.py` y comenzar su implementación.

### 2026-04-30 — Fix: Resolución de rutas estáticas en inyector Headless de WC

**Contexto:** El inyector de productos (`merci-wc-mock.py`) enviaba una URL de imagen incorrecta a WooCommerce (`/blog/assets/images/...`), provocando que la imagen no se descargara ni se adjuntara al producto en la tienda.

**Hecho:**
- Se implementó la variable `domain_root` utilizando `wp_url.removesuffix('/blog')` en `merci-wc-mock.py`.
- Se actualizó el *payload* JSON para que el campo `src` de la imagen apunte a la raíz del dominio estático.

**Detalle técnico:** En la arquitectura aislada, la variable de entorno `WP_URL` apunta al subdirectorio del CMS, pero Nginx sirve los *assets* multimedia directamente desde la raíz pública. Amputar programáticamente el sufijo del CMS en Python garantiza que la API REST reciba una URI absoluta resoluble, manteniendo la segregación de entornos.

**Motivo / criterio:** *Single Source of Truth y Aislamiento*. No duplicar variables de entorno (como crear un `STATIC_URL` en el `.env`) mantiene la configuración sencilla. Inferir matemáticamente la ruta estática a partir de la ruta dinámica es el enfoque más resiliente frente a cambios de dominio.

**Siguiente paso o deuda:** Validar la inyección correcta de la imagen en la tienda y proceder con LinkedIn (Fase 8.3).

### 2026-04-30 — Fix: Purga de título duplicado e inyección de imágenes optimizadas en WC

**Contexto:** La página principal de la tienda (`archive-product.php`) mostraba el título "Tienda" por duplicado. Además, se requería definir el flujo de trabajo para insertar imágenes optimizadas en los productos vía API Headless.

**Hecho:**
- Se inyectó el filtro `woocommerce_show_page_title` devolviendo `false` en `functions.php` para eliminar el título nativo del plugin.
- Se actualizó el script `merci-wc-mock.py` añadiendo el *payload* de imágenes apuntando a los *assets* locales generados por `merci-optimizer.py`.

**Detalle técnico:** WooCommerce inyecta automáticamente `<h1 class="page-title">` al renderizar el bucle de productos. Como nuestra plantilla `woocommerce.php` ya provee un componente BEM `.hero`, el filtro nativo purga la inyección redundante. Para las imágenes, la API REST requiere una URI absoluta (`src`); proveer la ruta local de la imagen `.webp` generada por nuestro orquestador obliga a WP a consumir el archivo ya optimizado, protegiendo los Core Web Vitals.

**Motivo / criterio:** *Zero Bloat y UI/UX*. Desactivar elementos nativos del CMS mediante hooks de PHP evita tener que ocultarlos con `display: none` en CSS, manteniendo el DOM lo más ligero posible. Interceptar el flujo multimedia asegura que ninguna imagen bruta llegue a la base de datos dinámica.

**Siguiente paso o deuda:** Validar visualmente la tienda sin títulos duplicados y el producto con su imagen, y proceder a LinkedIn (Fase 8.3).

### 2026-04-30 — Feat: Inyector Headless de Productos Mock (WooCommerce)

**Contexto:** Para validar los estilos SASS de la tienda en el entorno local recién configurado, era necesario crear un producto de prueba. Para mantener la filosofía "CLI-first" y no depender del panel de administración (GUI) de WordPress, se requería una vía de inyección desde la terminal.

**Hecho:**
- Se desarrolló el script experimental `laboratorio/scripts_temporales/merci-wc-mock.py`.
- El script consume el archivo `.env` existente y realiza un `POST` a la API REST nativa de WooCommerce (`/wc/v3/products`).

**Detalle técnico:** Se descartó el uso de comandos `curl` crudos para evitar exponer la contraseña de aplicación (`WP_APP_PASSWORD`) en el historial de la terminal (`.bash_history`), cumpliendo con los estándares de seguridad (Shift-Left). El script interactúa mediante Autenticación Básica Base64.

**Motivo / criterio:** *Developer Experience (DX) y Seguridad*. Automatizar la inyección de datos de prueba (Mock Data) acelera el desarrollo del frontend. Utilizar las mismas credenciales seguras que `merci-wp.py` demuestra la versatilidad de la arquitectura Headless.

**Siguiente paso o deuda:** Inyectar el producto, validar el diseño del catálogo individual y, finalmente, comenzar con LinkedIn.

### 2026-04-30 — UX: Enlace de retroceso en vista de producto (WooCommerce)

**Contexto:** Tras restaurar la paridad de entornos y validar los estilos SASS de la tienda, se observó que la vista de producto individual (`single-product`) carecía de un atajo para regresar rápidamente al catálogo, generando fricción en la navegación.

**Hecho:**
- Se inyectó un enlace condicional (`is_product()`) en `src/wp-theme/merci-theme/woocommerce.php` apuntando a la página principal de la tienda.
- Se reutilizó la clase SASS existente `.card__back-link` para mantener la consistencia visual.

**Motivo / criterio:** *Fricción Cero y Reusabilidad*. Proveer una vía de escape clara mejora la experiencia de usuario (UX). Reutilizar una clase CSS semántica creada originalmente para la biblioteca (`.card__back-link`) evita inyectar estilos en línea o crear código duplicado, cumpliendo con el principio DRY (Don't Repeat Yourself).

**Siguiente paso o deuda:** Dar por cerrado el MVP de la tienda e iniciar el diseño del script de automatización para LinkedIn (`merci-linkedin.py`).

### 2026-04-30 — Arch: Restauración de Paridad de Entornos (Dev/Prod Parity)

**Contexto:** Durante la estilización del MVP de la tienda, se detectó una desconexión total entre el código SASS y la visualización local. El diagnóstico reveló que WooCommerce estaba instalado exclusivamente en el servidor de producción, pero ausente en el entorno de desarrollo local.

**Hecho:**
- Se pausó el desarrollo de código.
- Se instruyó la instalación, activación y configuración de WooCommerce en el WordPress local, incluyendo la creación de datos de prueba (Mock Data).

**Motivo / criterio:** *Dev/Prod Parity* (Paridad Desarrollo/Producción). Desarrollar sobre un entorno local que no refleja la topología exacta de producción genera "ceguera de desarrollo" y fomenta el anti-patrón de probar código directamente en la web pública. Replicar el CMS y sus plugins clave en local es un requisito innegociable de la arquitectura DevSecOps.

**Siguiente paso o deuda:** Validar visualmente los estilos SASS de la tienda en el entorno local ahora que el motor dinámico está operativo, y continuar con LinkedIn.

### 2026-04-30 — Fix: Resolución de Jerarquía de Plantillas en WooCommerce

**Contexto (El Desafío):** La página de la tienda (`/blog/tienda`) renderizaba un contenedor vacío (`.article__content`) a pesar de que la plantilla `woocommerce.php` contenía la función `woocommerce_content()` correcta. El CMS estaba ignorando la plantilla específica y recurriendo a `index.php`.

**Hecho (La Maniobra):**
- Se configuró la página "Tienda" como la página oficial en el panel de administración de WordPress, bajo `WooCommerce > Ajustes > Productos`.

**Detalle técnico:** La existencia de un archivo `woocommerce.php` en el tema no es suficiente. WordPress solo lo utiliza si la URL que se está visitando corresponde a la página asignada explícitamente como "Página de la tienda" en los ajustes del plugin. Sin esta asignación, WordPress trata la URL como una página estándar y aplica su jerarquía de plantillas por defecto (`page.php` o, en su defecto, `index.php`).

**Motivo / criterio (El Aprendizaje):** *Template Hierarchy y Configuración sobre Código*. La configuración del panel de administración de un CMS a menudo tiene mayor precedencia que la estructura de archivos del tema. Comprender la jerarquía de plantillas es crucial para depurar por qué un archivo de tema es ignorado por el motor de renderizado.

**Siguiente paso o deuda:** Validar que la tienda ahora renderiza los productos y sus estilos SASS correctamente.

### 2026-04-30 — Fix: Inyección nativa de WooCommerce (Template Hierarchy)

**Contexto:** Al intentar estilizar la tienda MVP, la página no renderizaba ningún producto (HTML vacío dentro de `.article__content`). Una auditoría del DOM (F12) reveló que el CMS estaba ejecutando el bucle estándar (`the_content()`) en lugar de la cuadrícula de la tienda.

**Hecho:**
- Se reemplazó el bucle `The Loop` estándar de WordPress por la función `woocommerce_content()` dentro del archivo `src/wp-theme/merci-theme/woocommerce.php`.

**Detalle técnico:** WooCommerce renderiza su tienda en una "Página" (Page) física de WP. Si el archivo `woocommerce.php` es una copia literal de `index.php` usando `the_content()`, devuelve un bloque vacío. Llamar a `woocommerce_content()` le devuelve el control del renderizado al plugin dentro de nuestros contenedores semánticos SASS.

**Motivo / criterio:** *Separation of Concerns* y Arquitectura de Plantillas. Obligar a WooCommerce a usar su propio motor de renderizado dentro de nuestra caja fuerte (`<section class="section">`) es el único método validado y oficial para evitar colisiones de rutas dinámicas manteniendo el 100% de nuestros estilos base.

**Siguiente paso o deuda:** Validar la cuadrícula SASS compilada en el navegador y continuar con la automatización para LinkedIn.

### 2026-04-30 — Docs: Refinamiento del SOP de Release del Boilerplate

**Contexto (El Desafío):** Se detectó una fisura lógica en el Procedimiento Operativo Estándar (SOP) de actualización del Boilerplate (`docs/matriz/mantenimiento-boilerplate-sop.md`). Las instrucciones indicaban modificar archivos en la matriz local y luego clonar desde el remoto, pero omitían el paso crítico de subir (`git push`) los cambios locales al servidor.

**Hecho (La Maniobra):**
- Se actualizó `docs/matriz/mantenimiento-boilerplate-sop.md` para dividir el "Paso 1" en dos sub-pasos explícitos: el sello local (`merci commit`) y la sincronización remota (`git push`).

**Detalle técnico:** El comando `git clone` del SOP se nutre del estado del repositorio en GitHub, no del estado del disco duro local. Sin un `push` previo, el clon temporal siempre descargaba una versión obsoleta del código, invalidando las correcciones recién aplicadas.

**Motivo / criterio (El Aprendizaje):** *Infrastructure as Code (IaC) y Rigor Operativo*. Un SOP debe ser atómico e inequívoco. Este refinamiento previene la "falsa ejecución" del pipeline, garantizando que el proceso de instanciación siempre parta de la última versión validada y subida del código matriz.

**Siguiente paso o deuda:** Con el pipeline de release blindado, iniciar el desarrollo de la automatización social para LinkedIn (`merci-linkedin.py`).

### 2026-04-30 — DevSecOps: Prevención de fuga de datos en directorios Headless

**Contexto:** Se sugirió modificar el script de instanciación para simplemente "no borrar" las carpetas dinámicas (`blog/` y `art-de-cote/`). El análisis arquitectónico reveló que esto expondría los borradores y artículos publicados de la autora en el repositorio público. Además, se detectó que las carpetas raíz dinámicas no estaban siendo purgadas.

**Hecho:**
- Se añadieron `blog/` y `art-de-cote/` de la raíz a la lista de eliminación de `purge_directory` en `merci-init.py`.
- Se refactorizó la lógica de reconstrucción para generar las 4 carpetas dinámicas (en la raíz y en laboratorio) con sus respectivos `.gitkeep` tras la limpieza.

**Detalle técnico:** En lugar de excluir directorios del borrado (lo que conserva su contenido interno), se arrasa con ellos y se vuelven a crear usando `mkdir(parents=True, exist_ok=True)` y `touch(".gitkeep")`.

**Motivo / criterio:** *Data Leak Prevention (DLP)*. Un boilerplate debe ser un lienzo en blanco. Excluir carpetas del borrado es un antipatrón de seguridad si estas pueden contener propiedad intelectual. Destruir y reconstruir el andamiaje garantiza la higiene absoluta del repositorio derivado.

**Siguiente paso o deuda:** Retomar el desarrollo de la automatización social para LinkedIn (`merci-linkedin.py`).

### 2026-04-30 — UX/UI: Estilización del MVP de la tienda (WooCommerce)

**Contexto:** Tras decidir pivotar hacia la creación de una tienda mínima viable (MVP) antes de la campaña de LinkedIn, era necesario "vestir" el HTML crudo que genera WooCommerce, ya que sus estilos CSS nativos fueron purgados para mantener el 100/100 en Core Web Vitals.

**Hecho:**
- Se creó y estilizó el componente `src/scss/components/_woocommerce.scss`.
- Se implementó un diseño de tarjetas en cuadrícula (Grid) para la vista de catálogo (`archive-product.php`).
- Se maquetó la vista de producto individual (`single-product.php`) con un layout de 2 columnas (galería + resumen) y se normalizaron los estilos del formulario de compra y las pestañas de descripción.

**Detalle técnico:** Se utilizaron las clases BEM y variables SASS existentes para mantener la coherencia visual. Se aplicó `display: grid` y `grid-template-columns` para las vistas de catálogo y producto, y `flexbox` para alinear los elementos del formulario de compra.

**Motivo / criterio:** *Zero Bloat y Coherencia Visual*. En lugar de cargar los pesados CSS de WooCommerce, se aplicaron estilos ultraligeros y a medida, garantizando que la tienda se integre visualmente en el ecosistema Merci sin degradar el rendimiento.

**Siguiente paso o deuda:** Con el MVP de la tienda funcional, el siguiente paso es retomar la automatización de LinkedIn (`merci-linkedin.py`).

### 2026-04-30 — Fix: Preservación de estructura de directorios en instanciación

**Contexto:** Tras instanciar el Boilerplate, el orquestador `merci-wp.py` emitía advertencias indicando que los directorios `blog/` y `art-de-cote/` no existían, ya que Git no rastrea carpetas vacías y `merci-init.py` destruía el contenido del `laboratorio/`.

**Hecho:**
- Se añadieron archivos `.gitkeep` a las carpetas `laboratorio/blog/` y `laboratorio/art-de-cote/` de la matriz.
- Se parcheó `scripts/merci/merci-init.py` para reconstruir estos subdirectorios estructurales y generar sus respectivos `.gitkeep` tras la purga del laboratorio.

**Detalle técnico:** La función `purge_directory` usa `shutil.rmtree`, lo que erradica subdirectorios enteros. Recrearlos explícitamente con `mkdir` y `touch(".gitkeep")` asegura que la topología de incubación Headless esté lista desde el commit cero del nuevo proyecto.

**Motivo / criterio:** *Developer Experience (DX) y Robustez*. Un entorno de desarrollo debe proveer el andamiaje completo necesario para que sus herramientas CLI operen sin emitir advertencias de "archivo no encontrado" por problemas derivados del control de versiones.

**Siguiente paso o deuda:** Retomar el MVP de la tienda (WooCommerce) estandarizando sus estilos visuales.

### 2026-04-30 — Fix: Resolución de enlace roto (PGP) en QA de Boilerplate

**Contexto:** Al instanciar y auditar el Boilerplate v1.2.1, el orquestador `merci-total` detuvo el pipeline en la fase de `merci-linkcheck.py` al detectar un error 404 en el enlace `/llave-publica.asc` de la página estática de Contacto.

**Hecho:**
- Se creó el archivo de texto plano `public/llave-publica.asc` con un bloque de mensaje explicativo (Placeholder) para satisfacer el escaneo de red.

**Motivo / criterio:** *QA Estricto (Fail-Fast)*. El orquestador demostró su valor al no tolerar "promesas" de archivos futuros. Para que la plantilla apruebe su propia auditoría desde el commit cero, todos los enlaces estructurales deben resolver a un archivo real, delegando al usuario final la tarea de reemplazar el archivo de muestra con su clave criptográfica real.

**Siguiente paso o deuda:** Retomar el MVP de la tienda (WooCommerce) estandarizando sus estilos visuales.

### 2026-04-30 — Fix: Generación de plantilla .env en instanciación (Release v1.2.1)

**Contexto:** Un nuevo usuario que clona el Boilerplate v1.2.0 experimentaba un fallo crítico en su primer `merci total` porque el pipeline de QA invocaba a `merci-wp.py`, el cual colapsaba al no encontrar el archivo `.env` (excluido por `.gitignore`).

**Hecho:**
- Se modificó `scripts/merci/merci-init.py` para inyectar dinámicamente un archivo `.env` de ejemplo con las variables `WP_URL`, `WP_USER` y `WP_APP_PASSWORD`.
- Se actualizó la versión en `README-merci.md` a v1.2.1.

**Detalle técnico:** El script ahora utiliza `write_text` para crear el archivo de configuración en la raíz del clon antes de finalizar el proceso, asegurando que la dependencia de variables de entorno esté satisfecha para el orquestador.

**Motivo / criterio:** *Developer Experience (DX) y Fricción Cero*. Un boilerplate debe funcionar *out of the box* (listo para usar). Entregar un pipeline roto degrada la confianza en la herramienta. Proveer un `.env` de muestra transforma un error de código (`FileNotFoundError`) en un fallo de conexión controlado, informando al usuario de lo que debe configurar.

**Siguiente paso o deuda:** Retomar el MVP de la tienda (WooCommerce) estandarizando sus estilos visuales en la arquitectura SASS 7-1.

### 2026-04-30 — Docs: Release v1.2.0 del Boilerplate (Consolidación Headless y QA)

**Contexto:** Tras finalizar las herramientas de publicación Headless (`merci-wp`), el enrutamiento contextual (`merci-promote`) y purificar la interfaz estática (Contacto), el ecosistema base alcanzó un hito de madurez que debía ser exportado a la plantilla pública antes de iniciar ramas de desarrollo paralelas (como WooCommerce).

**Hecho:**
- Se actualizó `README-merci.md` con las novedades de la v1.2.0.
- Se marcó la Fase 8.3 como completada al 100% en `instrucciones-merci.md`.
- Se ejecutó el pipeline de despliegue (`merci-init.py` destructivo y `rsync --delete`) para exportar el código inmaculado al repositorio `merci-boilerplate`.

**Detalle técnico:** El orquestador de instanciación purgó automáticamente los manuales SOP exclusivos de la matriz (`docs/matriz/`) asegurando que los "Shadow Docs" ascendieran atómicamente a su versión final en el destino, erradicando la derivación de configuración.

**Motivo / criterio:** *Release Management y Single Source of Truth (SSOT)*. Iniciar desarrollos nuevos (tienda) teniendo "deuda de despliegue" pendiente es un antipatrón. Empaquetar y sellar el repositorio ahora asegura que el Boilerplate herede un estado estable y 100/100 auditado antes de introducir la complejidad de un e-commerce.

**Siguiente paso o deuda:** Desarrollar el MVP de la tienda (WooCommerce) estandarizando sus estilos visuales en la arquitectura SASS 7-1.

### 2026-04-30 — UX/UI: Refactorización purista de la página de Contacto

**Contexto:** La página de contacto (`public/contacto/index.html`) conservaba el texto "placeholder" (texto de relleno) genérico del Boilerplate. Se requería definir el método de contacto sin violar la arquitectura de 0 dependencias ni engordar el código con servicios de terceros (formularios).

**Hecho:**
- Se eliminó el texto genérico del Hero y se implementó un diseño purista tipográfico.
- Se inyectó un canal de comunicación directo (`mailto:`) y un bloque preparado para alojar una clave pública PGP (Pretty Good Privacy).

**Motivo / criterio:** *Zero Bloat y DevSecOps*. Depender de un `<form>` requiere procesado backend (PHP) o servicios de terceros que inyectan scripts y latencia, vulnerando la política estricta de rendimiento y privacidad (GDPR). Proveer un email directo y soporte para cifrado E2EE (End-to-End Encryption) es el estándar técnico superior.

**Siguiente paso o deuda:** Iniciar el diseño y desarrollo de la automatización Headless para LinkedIn (`merci-linkedin.py`).

### 2026-04-30 — Docs: Publicación de cuadernillo sobre optimización de backups

**Contexto:** La drástica reducción del peso de las copias de seguridad (de 50 MB a 0.35 MB) mediante el uso del modo `--verbose` y rutas absolutas se consideró un caso de éxito digno de ser documentado como activo de conocimiento.

**Hecho:** Se redactó y publicó el archivo `biblioteca/cuadernillo-optimizacion-backups-locales.md`.

**Detalle técnico:** El documento explica el diagnóstico a través de la terminal (Caja de Cristal) y la diferencia crítica entre excluir carpetas por coincidencia de cadenas de texto frente al uso de rutas absolutas estructuradas en Python (`Path`).

**Motivo / criterio:** *Knowledge Management*. Trasladar las victorias de rendimiento e infraestructura a la Biblioteca consolida la madurez del ecosistema y sirve como manual de mejores prácticas para el desarrollo y depuración de herramientas CLI locales.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).

### 2026-04-30 — Perf: Verificación de reducción masiva en backup local (0.35 MB)

**Contexto:** Tras aplicar las exclusiones de los binarios de Dart Sass y el historial de auditorías de PageSpeed, era necesario verificar empíricamente el impacto en el tamaño del empaquetado final del repositorio.

**Hecho:** El script `merci-backup.py` generó una copia de seguridad exitosa con un peso total de tan solo 0.35 MB.

**Detalle técnico:** La cifra de 0.35 MB representa una reducción de más del 99.3% frente a los 50.31 MB anteriores. Esto certifica que el filtro de rutas absolutas funciona con precisión quirúrgica, aislando el código fuente puro de cualquier artefacto pesado, multimedia incrustada o binario regenerable.

**Motivo / criterio:** *Zero Bloat y Disaster Recovery*. Un entorno DevSecOps debe permitir respaldos ultrarrápidos y portables. Esta métrica consolida empíricamente la arquitectura del proyecto: el peso reside en las dependencias y el CMS, mientras que el código matriz se mantiene estrictamente minimalista y ágil.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).

### 2026-04-30 — Feat: Modo verbose en script de copias de seguridad

**Contexto:** Tras refactorizar las exclusiones del backup para reducir su peso, surgió la necesidad operativa de poder auditar visualmente qué archivos exactos se estaban empaquetando en el archivo ZIP para verificar que no se filtrara basura o código de terceros.

**Hecho:** Se implementó el flag `--verbose` (o `-v`) en `scripts/merci/merci-backup.py`.

**Detalle técnico:** Se integró la lectura de `sys.argv` para activar la variable booleana `verbose`. Durante la iteración `os.walk`, si el modo está activo, la terminal imprime en tiempo real cada ruta relativa que se escribe en el archivo ZIP (`zipf.write`).

**Motivo / criterio:** *Transparencia y Trazabilidad*. Un proceso de copia de seguridad no debe ser una caja negra. Proveer un modo detallado opcional permite a la desarrolladora certificar la exactitud del filtro de exclusiones sin saturar la salida estándar por defecto en la ejecución diaria.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).

### 2026-04-30 — Perf: Refactorización de exclusiones en script de backup

**Contexto:** La ejecución de `merci-backup.py` generaba un archivo ZIP de más de 50 MB, un tamaño desproporcionado para un repositorio de código fuente. Se diagnosticó que el script estaba comprimiendo la instalación completa de WordPress ubicada en la ruta `public/blog`.

**Hecho:** Se modificó la lógica de exclusión en `scripts/merci/merci-backup.py` para utilizar rutas absolutas (`EXCLUDE_PATHS`) en lugar de nombres de carpetas genéricos.

**Detalle técnico:** Anteriormente, el script excluía carpetas de forma global. No se podía excluir la palabra "blog" porque habría omitido el código fuente en `blog/` y `laboratorio/blog/`. Al migrar a una comprobación por ruta absoluta (`Path(root) / d not in EXCLUDE_PATHS`), se bloquea quirúrgicamente la instalación del CMS.

**Motivo / criterio:** *Performance y Zero Bloat*. Las copias de seguridad locales deben ser ultraligeras y contener exclusivamente el estado del proyecto DevSecOps. Las dependencias externas o instalaciones de terceros (como el núcleo de WP) se regeneran o gestionan aparte, no se empaquetan en el backup del código fuente.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).

### 2026-04-30 — Chore: Invalición de caché manual (Cache Busting v12)

**Contexto:** Tras modificar los diálogos interactivos de `MerciController.js`, los cambios no se reflejaban en el servidor de producción para las rutas estáticas (Portada y Contacto) debido a la retención en caché de los navegadores.

**Hecho:** Se incrementó el parámetro de versión (`?v=12`) en las etiquetas `<link>` y `<script>` de `public/index.html` y `public/contacto/index.html`.

**Detalle técnico:** Mientras que el motor SSG y WordPress utilizan un sistema de versionado dinámico (basado en `filemtime` o `time()`), las páginas HTML puras requieren una actualización manual de la cadena de consulta (query string) para forzar a los clientes web y proxies a invalidar sus cachés locales y solicitar el nuevo archivo al servidor.

**Motivo / criterio:** *Cache Invalidation*. Es la técnica estándar y más ligera para asegurar que todos los usuarios reciban la última versión del código frontend sin necesidad de purgar cachés a nivel de servidor (Nginx/Varnish).

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).

### 2026-04-29 — UX/UI: Unificación responsiva de altura en componentes Hero

**Contexto:** Se detectó disparidad visual entre las distintas páginas del ecosistema (Portada, Contacto, Biblioteca). La sección `.hero` crecía en función de la longitud de su texto, provocando que los bloques de cabecera tuvieran tamaños dispares.

**Hecho:** Se implementó `min-height: 40vh` y centrado vertical con `flexbox` en `src/scss/components/_hero.scss`.

**Detalle técnico:** En lugar de aplicar restricciones rígidas (`height` o `max-height`), que corren el riesgo de provocar desbordamientos de texto (overflow) en pantallas móviles estrechas, se definió una altura mínima basada en *Viewport Height* (`vh`). Flexbox (`justify-content: center`) se encarga de absorber la diferencia de longitud del texto repartiendo el espacio vacío, logrando paridad visual en pantallas de escritorio.

**Motivo / criterio:** *Consistencia Visual y Responsive Design*. Establecer un tamaño base flexible estandariza la primera impresión del usuario en todas las rutas sin comprometer la legibilidad ni la puntuación de Core Web Vitals en dispositivos móviles.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).

### 2026-04-29 — Refactor: Poda de redundancias y duplicidades en arquitectura SASS

**Contexto:** Tras analizar la especificidad CSS, se realizó una auditoría profunda en el directorio `src/scss/` buscando más casos de código muerto o duplicado que engordaran la hoja de estilos final.

**Hecho:**
- Se fusionaron las clases gemelas `.section-methodology` y `.section-ecosystem` en una única clase `.home-section` dentro de `_hero.scss` (y se actualizó `public/index.html`).
- Se eliminaron reglas redundantes (`text-decoration: none` y herencia de color en anclas) en `_library-index.scss`.

**Detalle técnico:** Las reglas eliminadas en el índice de la biblioteca eran "código muerto", ya que el archivo base `_typography.scss` ya se encarga de eliminar el subrayado globalmente y de gestionar la herencia de color en los encabezados (`h1-h6 a`). Las secciones de la portada se unificaron bajo un solo bloque BEM (`.home-section`), reduciendo el peso del CSS.

**Motivo / criterio:** *Zero Dead Code* (Cero Código Muerto) y DRY (Don't Repeat Yourself). Las reglas CSS que redeclaran comportamientos ya definidos por la base tipográfica son un lastre. Mantener un CSS minimalista garantiza un procesamiento rápido del render tree en el navegador.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).

### 2026-04-29 — Refactor: Purga de deuda técnica en componente SASS (_hero.scss)

**Contexto:** Una auditoría de la arquitectura SASS 7-1 reveló la existencia de una definición duplicada de la clase `.card` dentro del archivo `_hero.scss`, a pesar de que dicho componente ya tenía su propio archivo dedicado (`_card.scss`).

**Hecho:** Se eliminó el bloque de código `.card` redundante de `src/scss/components/_hero.scss`.

**Detalle técnico:** El archivo `_index.scss` importaba `_hero.scss` antes que `_card.scss`, provocando que el navegador leyera estilos que eran inmediatamente sobrescritos por el componente correcto. Aunque el resultado visual era el esperado, generaba código muerto en el `main.css` final.

**Motivo / criterio:** *Code Hygiene y Single Responsibility Principle*. Cada componente SASS debe ser responsable únicamente de su propio bloque BEM. Eliminar código duplicado o desplazado reduce el peso del CSS final y mejora drásticamente la mantenibilidad y la claridad de la arquitectura.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).

### 2026-04-29 — Refactor: Reestructuración visual del índice de la Biblioteca (Grid y BEM)

**Contexto:** El índice autogenerado de la Biblioteca utilizaba un layout basado en `flexbox` y clases CSS no estandarizadas (`.indice__*`), lo que dificultaba la creación de columnas de ancho uniforme y una jerarquía visual clara entre los títulos de las estanterías y los artículos.

**Hecho:**
- Se refactorizó `src/scss/components/_library-index.scss` para usar `display: grid` en la lista de estanterías.
- Se migraron los estilos de `.indice__*` desde `_typography.scss` a `_library-index.scss`, renombrando las clases para cumplir la metodología BEM (ej. `.library-nav__theme-title`).
- Se modificó `scripts/merci/merci-publish.py` para inyectar las nuevas clases BEM.
- Se diferenció tipográficamente el título de la estantería (mayúsculas, más peso) del de los artículos.

**Detalle técnico:** Se utilizó `grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));` para lograr un diseño de rejilla responsivo sin media queries. La refactorización a BEM y la centralización de los estilos en su propio componente SASS mejoran la mantenibilidad y la Separación de Responsabilidades.

**Motivo / criterio:** *UX y Code Hygiene*. Un layout en rejilla (Grid) es superior a Flexbox para crear columnas de ancho idéntico, mejorando la armonía visual. Diferenciar la tipografía establece una jerarquía clara que guía al usuario. Pagar la deuda técnica de las clases no estándar y centralizarlas en su componente SASS es una práctica de ingeniería de software limpia.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).

### 2026-04-29 — Refactor: Pago de deuda técnica (Eliminación de estilos en línea)

**Contexto:** Una auditoría de código reveló la existencia de una cantidad significativa de estilos en línea (`style="..."`) en el footer y en el índice de la biblioteca, lo cual se considera deuda técnica al violar el principio de Separación de Responsabilidades y la metodología BEM.

**Hecho:**
- Se crearon los componentes SASS `_footer.scss` y `_library-index.scss`.
- Se refactorizaron los archivos `public/index.html`, `public/contacto/index.html`, `src/wp-theme/merci-theme/index.php` y `scripts/merci/merci-publish.py` para eliminar los atributos `style` y reemplazarlos por clases BEM.

**Detalle técnico:** Se extrajo toda la lógica de posicionamiento (flexbox, márgenes) y cromática a clases BEM dedicadas (ej. `.footer__links`, `.library-nav`, `.library-section`). Esto restaura la autoridad de la arquitectura SASS 7-1 y permite el uso de pseudo-clases interactivas y media queries responsivas.

**Motivo / criterio:** *Code Hygiene y Mantenibilidad*. Aunque los estilos en línea son útiles para prototipado rápido, su permanencia en producción genera un código frágil y difícil de mantener. La refactorización a SASS BEM centraliza la capa de presentación, saldando la deuda técnica y preparando el código para futuras iteraciones.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).

### 2026-04-29 — Docs: Publicación de cuadernillo sobre Especificidad CSS

**Contexto:** Los incidentes relacionados con la pseudo-clase `:visited` y la Especificidad CSS fueron considerados una lección de arquitectura de software lo suficientemente valiosa como para ser promovida a un activo de conocimiento permanente en la Biblioteca.

**Hecho:** Se redactó y creó el archivo `biblioteca/cuadernillo-la-guerra-de-la-especificidad-css.md`.

**Detalle técnico:** El cuadernillo se estructuró bajo el formato de 3 átomos (Desafío, Maniobra, Aprendizaje), explicando con ejemplos prácticos del propio proyecto por qué los estilos en línea y los selectores anidados pueden romper la interactividad de los enlaces.

**Motivo / criterio:** *Knowledge Management*. Transformar incidentes de depuración en material didáctico es un pilar de la filosofía del proyecto. Este cuadernillo servirá como referencia futura para evitar el uso de `!important` o la inyección de estilos en línea que comprometan la UX.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).
**Siguiente paso o deuda:** (Pendiente de instrucción).

### 2026-04-29 — QA: Selección cromática matemática para estado :visited (WCAG)

**Contexto:** Era necesario definir el color exacto para la variable `$color-visited` asegurando que mantuviera la coherencia visual con la marca y, simultáneamente, garantizara el 100/100 en accesibilidad en Google PageSpeed Insights.

**Hecho:** Se actualizó `$color-visited` a `#7c2d12` en `src/scss/abstracts/_variables.scss`.

**Detalle técnico:** El color asignado temporalmente (`#070f75`, azul marino) superaba la prueba de contraste pero causaba disonancia cromática. El tono elegido (`#7c2d12`, teja oscuro) mantiene la raíz del color principal (`#ea580c`) pero ofrece un ratio de contraste de ~10.2:1 sobre fondos blancos y ~9.8:1 sobre el gris claro (`#f8fafc`) del índice, superando ampliamente el mínimo exigido de 4.5:1 (Nivel AA) y alcanzando el nivel AAA.

**Motivo / criterio:** *Shift-Left Accessibility y Diseño UI*. Las decisiones de color en una arquitectura estricta no se basan únicamente en la estética. Calcular matemáticamente el ratio de contraste antes de inyectar variables en SASS previene fallos tardíos en la auditoría de rendimiento (Fail-Fast).

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).
**Siguiente paso o deuda:** (Pendiente de instrucción).

### 2026-04-29 — Fix: Aplicación de estado :visited en enlaces de cabecera (Tarjetas)

**Contexto:** Se detectó que los enlaces de los títulos en las tarjetas de la Biblioteca no cambiaban de color al ser visitados, a pesar de que la regla `:visited` global estaba correctamente definida en SASS.

**Hecho:** Se añadió la pseudo-clase `&:visited` dentro del anidamiento de `h1-h6 > a` en `src/scss/base/_typography.scss`.

**Detalle técnico:** La regla `h2 a { color: inherit; }` tenía una especificidad CSS (`0,0,2`) superior a la regla global `a:visited` (`0,1,1`), provocando que el navegador ignorara el color de visitado y forzara la herencia del color del encabezado. Al añadir explícitamente `&:visited { color: $color-visited; }` dentro del bloque del encabezado, se crea una regla más específica (`0,1,2`) que el navegador sí puede aplicar.

**Motivo / criterio:** *CSS Specificity y UX*. Para que los estados interactivos (`:hover`, `:focus`, `:visited`) funcionen de manera predecible, sus reglas deben tener una especificidad igual o superior a las reglas base del elemento. Esta corrección restaura el feedback visual del historial de navegación en todos los componentes.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).
**Siguiente paso o deuda:** (Pendiente de instrucción).

### 2026-04-29 — Fix: Resolución de especificidad CSS en enlaces del índice (SSG)

**Contexto:** Tras habilitar el estado `:visited` en la arquitectura SASS, se detectó que los enlaces del índice autogenerado de la Biblioteca no cambiaban de color tras ser pulsados.

**Hecho:** Se eliminó el atributo `style="color: ..."` de las etiquetas `<a>` en `scripts/merci/merci-publish.py` y se delegó el control cromático a las nuevas clases `.indice__tema` y `.indice__enlace` en `src/scss/base/_typography.scss`.

**Detalle técnico:** Los estilos en línea (`style="..."`) poseen una especificidad CSS de `1000`, aplastando cualquier pseudo-clase externa como `:visited` (cuya especificidad es `0010`). Al extraer el color a clases SASS estandarizadas, se restaura el flujo natural de la cascada CSS, permitiendo al navegador aplicar los colores de historial correctamente.

**Motivo / criterio:** *Separation of Concerns* y Accesibilidad/UX. Inyectar estilos estructurales menores en línea desde Python es aceptable en SSG, pero inyectar colores destruye la interactividad visual (hover, visited, focus). Mantener la capa cromática estrictamente en SASS garantiza la respuesta adecuada a las acciones del usuario.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).
**Siguiente paso o deuda:** (Pendiente de instrucción).

### 2026-04-29 — UX/UI: Incorporación de estado :visited en enlaces globales

**Contexto:** Para mejorar la navegación y reducir la carga cognitiva, era necesario que el usuario pudiera identificar de un vistazo qué artículos o estanterías de la Biblioteca ya había visitado previamente.

**Hecho:** Se instruyó la adición de la pseudo-clase `:visited` en la arquitectura SASS para los enlaces globales.

**Detalle técnico:** En accesibilidad y usabilidad (UX), diferenciar el estado visitado previene que el usuario haga clic repetidamente en contenido ya consumido. Se aplicó un tono ligeramente más oscuro o desaturado al color principal del enlace para mantener la coherencia visual sin violar el contraste WCAG.

**Motivo / criterio:** *Usabilidad y Fricción Cero*. Proveer *feedback* visual del historial de navegación es un estándar web fundamental (Heurísticas de Nielsen) que mejora significativamente la experiencia en sitios con alta densidad de contenido.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).
**Siguiente paso o deuda:** (Pendiente de instrucción).

### 2026-04-29 — Docs: Revisión editorial y refinamiento del copy en la portada

**Contexto:** Antes de subir a producción, se propuso una revisión de los textos de la portada (`public/index.html`) para asegurar que estuvieran alineados con la "Guía de Voz Editorial" (Regla 6), transmitiendo claridad técnica y evitando redundancias.

**Hecho:** Se refinó el subtítulo del Hero y la descripción de la tarjeta del Sistema Merci en `public/index.html`.

**Detalle técnico:** Se eliminó la redundancia ("base de conocimiento y operaciones con base en") sustituyéndola por "centro de operaciones. Un entorno web...". En la tarjeta de Merci, se hizo la llamada a la acción más directa y nativa ("Haz clic sobre su avatar").

**Motivo / criterio:** *UX Copywriting*. El texto de la interfaz es tan importante como la arquitectura subyacente. Aplicar la regla 80/20 (claridad técnica / personalidad) garantiza que el usuario perciba el rigor DevSecOps desde la primera línea que lee.

**Siguiente paso o deuda:** (Pendiente de instrucción).

### 2026-04-29 — Docs: Auditoría de paridad y actualización a Boilerplate v1.1.0

**Contexto:** Antes de desplegar el código a producción y exportar la nueva plantilla al repositorio derivado (`merci-boilerplate`), era imperativo verificar que los manuales operativos reflejaran el estado real del ecosistema (SSOT).

**Hecho:**
- Se incrementó la versión a `v1.1.0` en `README-merci.md`.
- Se actualizaron los listados de scripts y flujos operativos (SOP Dual) en `instrucciones.md` e `instrucciones-merci.md`.

**Detalle técnico:** Se incluyeron de forma explícita las herramientas `merci-wp.py`, `merci-sync-pages.py` y `merci-promote.py` (en su versión con enrutamiento inteligente) dentro de la documentación *Shadow* que viajará con la nueva instanciación del boilerplate.

**Motivo / criterio:** *Governance*. El código no está terminado hasta que la documentación no lo explica. Un salto de versión menor (Minor Release) está justificado por la inclusión de características Headless y de compilación completas y retrocompatibles.

**Siguiente paso o deuda:** Empaquetar la matriz, desplegar en producción y ejecutar el ciclo completo de instanciación hacia el Boilerplate.

### 2026-04-29 — Feat: Integración del publicador Headless (merci-wp) en el orquestador maestro

**Contexto:** Para garantizar que el entorno de producción dinámico (WordPress) se sincronice automáticamente antes de ejecutar las auditorías y el rastreo de enlaces, era necesario incluir el script `merci-wp.py` en la cadena de montaje global.

**Hecho:** Se añadió `merci-wp.py` al array `PIPELINE` de `scripts/merci/merci-total.py`.

**Detalle técnico:** El script se inyectó en la Fase de Construcción (Build), justo después de `merci-publish.py` y antes de `merci-sync-pages.py`. Esto asegura que los markdowns locales se conviertan en posts de WordPress y sus URLs estén activas antes de que `merci-linkcheck.py` y `merci-sitemap.py` rastreen el sitio.

**Motivo / criterio:** *Fricción Cero y Single Source of Truth (SSOT)*. Automatizar la sincronización de WordPress junto con el sitio estático mediante un único comando (`merci total`) unifica definitivamente los flujos de trabajo duales, mitigando el riesgo de que la desarrolladora olvide subir un artículo antes de hacer el commit atómico.

**Siguiente paso o deuda:** Iniciar la automatización social para LinkedIn (Fase 8.3).

### 2026-04-29 — Fix: Ambigüedad WAI-ARIA en menú dinámico (Blog)

**Contexto:** El rastreador `merci-linkcheck.py` detectó una infracción WAI-ARIA en las rutas de WordPress. El menú principal enlaza a `/blog/` con el texto "Blog", mientras que las tarjetas de los artículos enlazan a su categoría `/blog/category/blog/` con el mismo texto exacto, generando confusión para los lectores de pantalla.

**Hecho:** Se inyectó `aria-label="Ir a la portada del Blog"` en el enlace del menú principal en `public/index.html` y `src/wp-theme/merci-theme/index.php`.

**Detalle técnico:** Diferenciar el "Nombre Accesible" mediante `aria-label` resuelve la colisión en el DOM dinámico sin alterar el diseño visual, superando el escaneo automatizado del pipeline.

**Motivo / criterio:** *Accesibilidad Estricta e Inclusión*. Los lectores de pantalla listan enlaces fuera de contexto. Diferenciar sus propósitos semánticamente restaura la puntuación de 100/100 en accesibilidad.

**Siguiente paso o deuda:** Integrar la sincronización masiva de WordPress al pipeline maestro (`merci-total.py`).

### 2026-04-29 — Fix: Robustez en RegEx para saltos de línea y BOM (merci-promote)

**Contexto:** El asistente de promoción (`merci-promote.py`) fallaba al reconocer el YAML Frontmatter de la nueva plantilla de Art de Coté, a pesar de que el formato visual era estructuralmente correcto.

**Hecho:** Se refactorizaron las expresiones regulares en `scripts/merci/merci-promote.py` para tolerar `\r\n` y se cambió la codificación de lectura a `utf-8-sig`.

**Detalle técnico:** La expresión regular original `^---\n` era estricta con el salto de línea Unix (`LF`). Si el editor de texto guardaba el archivo con saltos de línea de Windows (`CRLF`) o inyectaba un carácter BOM (*Byte Order Mark* - `\ufeff`) al inicio, el `match` fallaba silenciosamente. Se actualizó a `^\s*---\r?\n` para absorber caracteres invisibles y retornos de carro.

**Motivo / criterio:** *Robustez y Fricción Cero*. Un script de automatización CLI (Command Line Interface - Interfaz de Línea de Comandos) no debe colapsar por diferencias de codificación de texto a nivel de sistema operativo. Aplicar esta robustez evita bloqueos incomprensibles para el usuario.

**Siguiente paso o deuda:** Validar la promoción del archivo y proceder con la automatización de LinkedIn (Fase 8.3).

### 2026-04-29 — Docs: Creación de plantillas Headless WP y definición de fronteras

**Contexto:** Se requería crear plantillas base (YAML Frontmatter + Markdown) para facilitar la redacción de nuevos artículos destinados a las categorías dinámicas (Blog y Art de Coté). Surgió el debate arquitectónico sobre si debían alojarse en el `laboratorio/` y si pertenecían a las reglas de negocio de la matriz o al ecosistema del Boilerplate.

**Hecho:** Se crearon los archivos `docs/plantilla-blog.md` y `docs/plantilla-art-de-cote.md`.

**Detalle técnico:** Las plantillas incluyen pre-configurados los campos `estado: "borrador"` y sus respectivos `tema:` para garantizar el enrutamiento correcto hacia WordPress por parte de `merci-wp.py`.

**Motivo / criterio:** *Separation of Concerns* (Separación de Responsabilidades). El entorno `laboratorio/` es efímero y se purga durante la instanciación (`merci-init.py`); alojar plantillas allí provocaría su destrucción en proyectos derivados. Ubicarlas en `docs/` consolida el Boilerplate como un producto completo que provee tanto el motor de publicación como los moldes de contenido.

**Siguiente paso o deuda:** Implementar automatización social para publicar entradas del blog directamente en LinkedIn.

### 2026-04-29 — Feat: Expulsión activa de borradores al laboratorio en CMS Headless

**Contexto:** Para garantizar la paridad absoluta con el flujo de la biblioteca estática, los artículos de WordPress que eran despublicados (`estado: "borrador"`) actualizaban su estado en la base de datos pero permanecían físicamente en las carpetas de producción (`blog/` o `art-de-cote/`).

**Hecho:** Se implementó la lógica de "Kill-Switch" con reubicación física en `scripts/merci/merci-wp.py`.

**Detalle técnico:** Tras una petición exitosa a la API de WordPress, si el estado no es `"publicado"` y el archivo no reside ya en `laboratorio/`, el script utiliza `shutil.move()` para trasladarlo de vuelta a `laboratorio/<ruta_relativa>`, replicando su árbol de directorios original dinámicamente (`destino_lab.parent.mkdir()`).

**Motivo / criterio:** *Environment Segregation*. Ningún documento en fase de incubación o revisión debe residir en los directorios raíz, ya sean de la capa estática o dinámica. La automatización de este movimiento previene que el autor olvide limpiar las carpetas de producción tras despublicar un post.

**Siguiente paso o deuda:** Implementar automatización social para publicar entradas del blog directamente en LinkedIn.

### 2026-04-29 — Feat: Enrutamiento contextual en orquestador de promoción (merci-promote)

**Contexto:** Para cumplir con la nueva unificación del flujo de publicación (SSOT), se requería que el asistente interactivo `merci-promote.py` reconociera los subdirectorios de incubación dinámica (`laboratorio/blog` y `laboratorio/art-de-cote`) y trasladara los documentos curados a sus respectivas carpetas raíz.

**Hecho:** Se refactorizó `scripts/merci/merci-promote.py` implementando escaneo recursivo (`rglob`) y una lógica de enrutamiento basada en las rutas relativas.

**Detalle técnico:** El script extrae las partes del directorio del archivo analizado (`rel_path.parts[:-1]`). Si detecta la palabra clave "blog" o "art-de-cote", asigna dinámicamente el directorio de destino y actualiza el mensaje de salida para sugerir el comando de publicación adecuado (`merci wp` en lugar de `merci total`).

**Motivo / criterio:** *Context-Awareness y Experiencia del Desarrollador*. En un ecosistema con múltiples motores de renderizado, centralizar la curación documental en una sola herramienta CLI evita el error humano. El script actúa como un "router" inteligente: el autor solo tiene que organizar sus borradores en carpetas dentro del laboratorio, y Python infiere matemáticamente el destino de producción.

**Siguiente paso o deuda:** Implementar automatización social para publicar entradas del blog directamente en LinkedIn (Fase 8.3).

### 2026-04-29 — Arch: Unificación del flujo de promoción para Headless CMS

**Contexto:** Los artículos destinados a WordPress se publicaban directamente desde el entorno de incubación (`laboratorio/`), saltándose el proceso de curación y creando disparidad arquitectónica respecto a la biblioteca estática. Además, WordPress no actualizaba las categorías de posts existentes si la API no lograba resolver el ID de la nueva categoría temporalmente.

**Hecho:**
- Se modificó la lista `WP_DIRS` en `scripts/merci/merci-wp.py` para apuntar a los directorios raíz `blog/` y `art-de-cote/`.
- Se redefinió el SOP de publicación dual (`docs/matriz/flujo-publicacion-sop.md`) para exigir el uso de `merci-promote.py` antes de sincronizar con WP.

**Motivo / criterio:** *Paridad de flujos y Separation of Concerns*. El entorno `laboratorio/` debe ser estrictamente para incubación. Aplicar la herramienta de promoción a los contenidos dinámicos unifica la experiencia del desarrollador (Developer Experience): todo nace en el laboratorio y todo se promueve a un directorio de pre-producción en la raíz, independientemente del motor de renderizado final (SSG o WP).

**Siguiente paso o deuda:** Refactorizar `merci-promote.py` para soportar el traslado de documentos hacia los directorios dinámicos (`blog/` y `art-de-cote/`).

### 2026-04-29 — Fix: Resolución de error WAI-ARIA por 'Trailing Slashes' y refuerzo de Whitelist en WP

**Contexto:** El orquestador `merci-total.py` detuvo el pipeline reportando un error de accesibilidad WAI-ARIA (Enlaces ambiguos) en el menú principal. Paralelamente, los posts de "Art de Coté" seguían apareciendo en la portada dinámica (`/blog`), indicando un fallo en el modelo Whitelist implementado anteriormente.

**Hecho:**
- Se añadieron barras finales (*trailing slashes*) a las rutas de directorio en la navegación (`<nav>`) de todos los componentes estáticos y dinámicos (ej. `/blog/category/art-de-cote/`).
- Se modificó la función `merci_filtrar_feed_principal` en `functions.php` delegando la consulta del slug directamente a `$query->set('category_name', 'blog')`.

**Detalle técnico:** El linter de accesibilidad detectaba el enlace del menú (sin barra final) y el enlace autogenerado por WordPress en la tarjeta del post (con barra final) como dos destinos distintos compartiendo el mismo texto ancla. Añadir las barras estandariza las URIs y elimina la colisión. Respecto a WordPress, usar `get_category_by_slug` generaba un "fallo abierto": si la categoría no se recuperaba instantáneamente, el condicional se omitía y WP mostraba todos los posts por defecto. Usar `category_name` impone un "fallo seguro" delegado al motor SQL de WP.

**Motivo / criterio:** *QA Estricto y Arquitectura Segura*. Las URIs de directorios deben terminar en `/` por estándar SEO (evita redirecciones 301 de servidor). En el backend, las funciones de filtro (Hooks) deben programarse siempre bajo el principio de fallo seguro (Fail-Safe) para garantizar la segregación de entornos.

**Siguiente paso o deuda:** Validar el pipeline en verde y confirmar la segregación de posts en WordPress.

### 2026-04-29 — Feat: Sincronización masiva en publicador Headless (merci-wp.py)

**Contexto:** El publicador Headless de WordPress operaba sobre un solo archivo a la vez. Para garantizar la paridad absoluta entre los Markdowns locales y la base de datos de WordPress (ej. cambios masivos de formato o despublicaciones en bloque), se requería que el script actuara como un sincronizador global similar al de la biblioteca (`merci-publish.py`).

**Hecho:** 
- Se refactorizó `scripts/merci/merci-wp.py` para procesar directorios completos de forma recursiva.
- Se definieron los directorios `laboratorio/blog` y `laboratorio/art-de-cote` como orígenes por defecto si el script se ejecuta sin argumentos.
- Se actualizó el manual operativo (`docs/matriz/flujo-publicacion-sop.md`).

**Detalle técnico:** Se extrajo la carga de credenciales `.env` fuera del bucle de publicación para optimizar recursos de I/O. Las interrupciones `sys.exit(1)` en el procesamiento individual de archivos se reemplazaron por retornos tempranos (`return False`) para aplicar el patrón "Fail-Gracefully" (Fallar con elegancia), permitiendo que el lote completo finalice aunque un archivo esté malformado.

**Motivo / criterio:** *Single Source of Truth (SSOT)*. Obligar al desarrollador a recordar qué archivo modificó para sincronizarlo individualmente genera Deriva de Configuración. Ejecutar una sincronización masiva asegura que las despublicaciones (`estado: "borrador"`) se reflejen instantáneamente en el entorno de producción dinámico sin fricción operativa.

**Siguiente paso o deuda:** Validar la automatización masiva y avanzar, bajo autorización, a la integración de automatización social para LinkedIn (Fase 8.3).

### 2026-04-29 — Arch: Pivot a modelo Whitelist en el feed principal de WordPress

**Contexto:** Tras aplicar una regla de exclusión para separar "Art de Coté" del feed principal, se debatió que un enfoque de "lista negra" no es escalable. El feed principal (`/blog`) debía actuar como un contenedor estanco exclusivo, no como un recolector general que requiere exclusiones manuales.

**Hecho:** Se refactorizó la función en `functions.php` a `merci_filtrar_feed_principal` (hook `pre_get_posts`) y se añadió la autocreación de la categoría "Blog".

**Detalle técnico:** En lugar de excluir categorías con ID negativo (`'-' . $id`), la consulta `is_home()` ahora fuerza explícitamente la inclusión exclusiva del ID de la categoría "Blog" (`$query->set('cat', $blog_cat->term_id)`).

**Motivo / criterio:** *Arquitectura de la Información y Escalabilidad (Whitelist vs Blacklist)*. Un modelo de lista blanca asegura que cualquier futura taxonomía o categoría independiente creada en el CMS quedará automáticamente aislada del blog sin necesidad de modificar el código del tema.

**Siguiente paso o deuda:** Implementar automatización social para publicar entradas del blog directamente en LinkedIn (Fase 8.3).

### 2026-04-29 — Arch: Segregación de categorías en el feed principal de WordPress

**Contexto:** Tras publicar un artículo en la categoría "Art de Coté" mediante el publicador Headless, se observó que dicho artículo aparecía tanto en su página de categoría como en el listado principal del blog (`/blog`), rompiendo la separación conceptual de los contenidos.

**Hecho:** Se implementó la función `merci_excluir_categorias_del_blog` en el archivo `functions.php` del tema, enganchada al hook `pre_get_posts`.

**Detalle técnico:** La función intercepta la consulta principal de WordPress (`is_main_query()`) cuando se renderiza la página de inicio del blog (`is_home()`). Obtiene dinámicamente el ID de la categoría "Art de Coté" mediante `get_category_by_slug()` y modifica la consulta (`$query->set()`) para excluir explícitamente los posts de dicho ID.

**Motivo / criterio:** *Arquitectura de la Información*. El comportamiento por defecto de WordPress es mostrar todos los posts en su feed principal. Para lograr una separación estricta entre un "blog" cronológico y colecciones temáticas, es necesario filtrar la consulta principal. Usar el hook `pre_get_posts` es el método canónico y más eficiente para lograrlo sin afectar el rendimiento.

**Siguiente paso o deuda:** Implementar automatización social para publicar entradas del blog directamente en LinkedIn (Fase 8.3).

### 2026-04-29 — Docs: Creación del SOP maestro de Publicación Dual

**Contexto:** Tras la implementación exitosa del publicador Headless para WordPress (`merci-wp.py`), el ecosistema pasó a gobernar dos flujos de publicación completamente distintos (SSG estático vs API REST dinámica). Era imperativo documentar las fronteras operativas para evitar que el desarrollador cruce herramientas por error (ej. promover un post de WP a la biblioteca estática).

**Hecho:** Se redactó y consolidó el documento `docs/matriz/flujo-publicacion-sop.md` (SOP: Flujo de Publicación Dual).

**Detalle técnico:** El documento actúa como una guía de referencia rápida (*Cheat Sheet*) que separa explícitamente el Flujo 1 (Laboratorio -> Promote -> Publish) del Flujo 2 (Art de Coté -> WP Headless).

**Motivo / criterio:** *Governance y Developer Experience (DX)*. Un ecosistema DevSecOps complejo requiere reglas de operación claras. Documentar las "Reglas de Oro" y los comandos exactos externaliza la carga cognitiva de la memoria del desarrollador hacia el repositorio de código, garantizando la mantenibilidad a largo plazo.

**Siguiente paso o deuda:** Implementar automatización social para publicar entradas del blog directamente en LinkedIn (Fase 8.3).

### 2026-04-29 — Feat: Sincronización bidireccional (Update) en Headless CMS

**Contexto:** El publicador Headless (`merci-wp.py`) generaba un artículo duplicado cada vez que se ejecutaba sobre el mismo archivo. Además, se detectó que pasar documentos destinados a WordPress por el flujo de `merci-promote` los ubicaba en la `biblioteca/`, provocando que el orquestador SSG los compilara erróneamente como páginas estáticas.

**Hecho:** 
- Se modificó `scripts/merci/merci-wp.py` para que lea y escriba dinámicamente el atributo `wp_id` en el YAML Frontmatter del archivo Markdown local.
- Se estableció la regla de segregar los archivos Markdown destinados a WordPress en carpetas externas a `biblioteca/` (ej. `art-de-cote/`) y omitir su paso por `merci-promote`.

**Detalle técnico:** En la primera publicación, el script captura el `id` numérico devuelto por la API de WordPress y reescribe físicamente el YAML del archivo `.md` inyectando `wp_id: "ID"`. En ejecuciones posteriores, el script detecta este ID y muta su endpoint a `/wp-json/wp/v2/posts/{id}` para realizar una actualización (Update) en lugar de una creación (Create).

**Motivo / criterio:** *Single Source of Truth (SSOT) Bidireccional*. Para que un Headless CMS en terminal funcione sin fricción, el archivo de texto local debe ser consciente de su entidad gemela en la base de datos. La inyección automática elimina el riesgo de duplicidad sin requerir interacción manual del autor.

**Siguiente paso o deuda:** Implementar automatización social para publicar entradas del blog directamente en LinkedIn.

### 2026-04-29 — Feat: Publicador Headless para WordPress (merci-wp.py)

**Contexto:** Para eliminar la fricción de usar el panel de administración de WordPress, se requería una herramienta de terminal para publicar artículos directamente desde archivos Markdown locales.

**Hecho:**
- Se desarrolló el script `scripts/merci/merci-wp.py`.
- Se documentó el proceso de creación de Contraseñas de Aplicación en WordPress y la configuración del archivo `.env`.
- Se actualizó el `README.md` para registrar la nueva herramienta y marcar la tarea como completada.

**Detalle técnico:** El script utiliza únicamente la biblioteca estándar de Python. Lee las credenciales de un archivo `.env` local, convierte el Markdown a HTML, y realiza dos peticiones a la API REST de WordPress: una (GET) para resolver el ID numérico de la categoría a partir de su nombre (leído del campo `tema:` del YAML), y otra (POST) para publicar el contenido. La autenticación se realiza mediante Basic Auth, enviando el usuario y la contraseña de aplicación codificados en Base64 en la cabecera `Authorization`.

**Motivo / criterio:** *Fricción Cero y Developer Experience (DX)*. Automatizar la publicación desde la terminal se alinea con la filosofía "CLI-first" del proyecto. Evitar dependencias externas (`requests`, `python-dotenv`) mantiene el núcleo de automatización ultraligero y portable.

**Siguiente paso o deuda:** Implementar la automatización social para publicar en LinkedIn.

### 2026-04-29 — QA: Certificación "Cuádruple 100" en auditoría móvil extrema

**Contexto:** Tras solventar las penalizaciones de contraste de color (WCAG) y la ambigüedad de enlaces (WAI-ARIA) en la nueva página índice de la Biblioteca, era obligatorio certificar el estado del arte mediante una auditoría de caja negra externa (Google PageSpeed Insights).

**Hecho:** Se logró la máxima puntuación posible (100/100 en Rendimiento, Accesibilidad, Mejores Prácticas y SEO) bajo condiciones simuladas de estrés (Moto G Power sobre red 4G lenta).

**Detalle técnico:** Las correcciones de accesibilidad (atributos `aria-label` y CSS de herencia de color) se integraron sin añadir un solo milisegundo al tiempo de carga. Las métricas Core Web Vitals continuaron marcando TBT 0ms y un Speed Index de apenas 0.8s.

**Motivo / criterio:** *Quality Assurance*. Obtener un 4x100 en móvil demuestra que la accesibilidad universal y el rendimiento extremo no son conceptos excluyentes si se aborda el desarrollo desde una arquitectura de Cero Dependencias (Vanilla JS + SASS 7-1 + SSG en Python puro).

**Siguiente paso o deuda:** Iniciar el desarrollo e integración del publicador Headless CMS (`merci-wp.py`) para WordPress.

### 2026-04-29 — QA: Certificación 100/100 en Rendimiento (Core Web Vitals) de la Biblioteca

**Contexto:** Tras la inyección masiva de nodos en el DOM para construir el "Mega-Menú" y la reestructuración de la página de la Biblioteca, era imperativo asegurar que la complejidad estructural no hubiera degradado el rendimiento.

**Hecho:** Se ejecutó una auditoría final de Lighthouse (PageSpeed Insights). El resultado certificó un Rendimiento perfecto: FCP 0.8s, LCP 1.1s, TBT 0ms y CLS 0.

**Detalle técnico:** Lograr **0 ms** de Tiempo de Bloqueo Total (TBT) demuestra que el hilo principal (Main Thread) del navegador está completamente libre. El CLS en 0 confirma que la carga asíncrona de estilos e imágenes no provoca repintados destructivos (Layout Thrashing).

**Motivo / criterio:** *Performance Driven Development*. Esta métrica valida empíricamente la filosofía fundacional del proyecto: usar Vanilla JS, SASS 7-1 nativo y un orquestador SSG en Python aplasta en rendimiento a cualquier framework reactivo moderno (React/Vue/Tailwind) dependiente de ecosistemas Node.js pesados.

**Siguiente paso o deuda:** Probar el publicador Headless (`merci-wp.py`) recién diseñado para escribir en WordPress local desde la terminal.

### 2026-04-29 — DevSecOps: Shift-Left Accessibility en rastreador de enlaces (DAST)

**Contexto:** Tras solucionar manualmente una advertencia de Lighthouse ("Identical links have the same purpose"), se propuso automatizar la detección de esta regla WAI-ARIA localmente para no depender de herramientas externas, atrapando el error directamente en la integración continua.

**Hecho:** Se refactorizó `scripts/merci/merci-linkcheck.py` transformándolo en un auditor dinámico dual (detecta enlaces rotos 404 + ambigüedad de accesibilidad).

**Detalle técnico:** Se amplió la clase `LinkParser` (heredada de `HTMLParser`) para registrar cuándo el parseo ocurre dentro de una etiqueta `<a>` y extraer su texto visible (`handle_data`) o su `aria-label`. Al finalizar una página, se mapean los "Nombres Accesibles" resultantes contra sus URLs de destino. Si un mismo nombre apunta a más de un destino único (`len(set(hrefs)) > 1`), el orquestador aborta la ejecución con un error `♿❌ Error WCAG`.

**Motivo / criterio:** *Shift-Left Accessibility*. Mover las validaciones de accesibilidad hacia la etapa de pre-commit elimina la latencia de descubrimiento de deuda técnica. Ampliar una herramienta nativa existente en Python logra este hito manteniendo la política innegociable de 0 dependencias (sin requerir Lighthouse CLI o módulos pesados de NPM).

**Siguiente paso o deuda:** Desarrollar el publicador Headless (`merci-wp.py`) para escribir en WordPress local desde la terminal.

### 2026-04-29 — QA: Resolución de ambigüedad en enlaces idénticos (WAI-ARIA)

**Contexto:** Lighthouse detectó una infracción de "Mejores Prácticas/Accesibilidad" porque los enlaces del Mega-Menú y los títulos de las tarjetas tenían el mismo texto visible (el título del artículo) pero apuntaban a destinos diferentes (`#ancla` vs `/url-final.html`).

**Hecho:** Se inyectaron atributos `aria-label` descriptivos en `scripts/merci/merci-publish.py` para diferenciar el propósito de cada enlace.

**Detalle técnico:** El enlace del Mega-Menú ahora se anuncia a los lectores de pantalla como `Ir al resumen de: [Título]`, mientras que el enlace de la tarjeta se anuncia como `Leer artículo completo: [Título]`.

**Motivo / criterio:** *Accesibilidad Estricta (100/100)*. Los lectores de pantalla listan los enlaces fuera de contexto. Si dos enlaces se llaman igual pero hacen cosas distintas, el usuario con discapacidad visual no puede predecir el resultado. Diferenciar sus propósitos mediante WAI-ARIA restaura la puntuación y mejora la UX inclusiva.

**Siguiente paso o deuda:** Desarrollar el publicador Headless (`merci-wp.py`) para escribir en WordPress local desde la terminal.

### 2026-04-29 — QA: Resolución de contraste WCAG en índice de la Biblioteca

**Contexto:** Tras la creación del Mega-Menú (índice curado) en la Biblioteca, una auditoría de Lighthouse detectó que el color naranja de los enlaces de las estanterías (`#ea580c`) sobre el fondo gris claro (`#f8fafc`) no alcanzaba el ratio de contraste mínimo exigido, provocando una penalización en Accesibilidad.

**Hecho:** Se oscureció el color de los enlaces a `#9a3412` (y su borde inferior a `rgba(154, 52, 18, 0.3)`) en el orquestador `scripts/merci/merci-publish.py`.

**Detalle técnico:** El color original `#ea580c` tiene un ratio de contraste de ~3.0:1 sobre fondos claros, lo cual está en el límite para textos en negrita grandes, pero falla el umbral estricto de 4.5:1 para textos generales. El nuevo tono `#9a3412` eleva el contraste por encima de 6:1, garantizando el 100/100 en Core Web Vitals (Accesibilidad).

**Motivo / criterio:** *Accesibilidad Estricta (100/100)*. La estética (un color vibrante) nunca debe comprometer la legibilidad. Si una herramienta automatizada detecta un problema de contraste, se corrige inmediatamente endureciendo el tono hacia umbrales seguros (Shift-Left Accessibility).

**Siguiente paso o deuda:** Desarrollar el publicador Headless (`merci-wp.py`) para escribir en WordPress local desde la terminal.

### 2026-04-29 — QA: Resolución de contraste WCAG en enlaces del footer

**Contexto:** Tras la inyección de los nuevos enlaces sociales en el footer, la auditoría de Lighthouse (PageSpeed Insights) reportó una caída a 95/100 en Accesibilidad debido a un ratio de contraste deficiente.

**Hecho:** Se aplicaron estilos en línea (`color: inherit; text-decoration: underline; text-underline-offset: 4px;`) a la clase `.footer__link` en la portada (`public/index.html`) y la plantilla CMS (`src/wp-theme/merci-theme/index.php`).
*Nota:* La página estática de contacto heredó la corrección automáticamente sin intervención manual gracias a la ejecución de `merci-sync-pages.py` en el orquestador.

**Detalle técnico:** Los navegadores aplican un color azul por defecto (`#0000EE`) a los enlaces no estilizados, el cual falla sistemáticamente el ratio de contraste 4.5:1 de las normativas WCAG (Web Content Accessibility Guidelines - Pautas de Accesibilidad al Contenido en la Web) sobre fondos oscuros o claros con poca luminancia.

**Motivo / criterio:** *Accesibilidad Estricta (100/100)*. Además del color, forzar el subrayado cumple con la norma de que "el color no debe ser el único indicador visual de interactividad". Mantener el 100/100 es innegociable en el ecosistema.

**Siguiente paso o deuda:** Desarrollar el publicador Headless (`merci-wp.py`) para escribir en WordPress local desde la terminal.

### 2026-04-29 — UX: Enlaces de "Volver arriba" en estanterías de la Biblioteca

**Contexto:** Con la implementación del "Mega-Menú" y el scroll suave hacia las tarjetas de los artículos, los usuarios necesitaban una forma rápida de regresar al índice superior tras revisar una estantería completa, sin depender del enlace del footer o de hacer scroll manual.

**Hecho:** Se inyectó un enlace `↑ Volver arriba` (apuntando a `#top`) a la derecha de cada título de sección (Estantería) en el orquestador `scripts/merci/merci-publish.py`.

**Detalle técnico:** Se envolvió el título de la sección (`<h2>`) y el nuevo enlace (`<a>`) en un contenedor `<div>` con `display: flex; justify-content: space-between; align-items: baseline;`. Esto garantiza que, sin importar la longitud del título del tema, el botón de retorno siempre quede fijado a la derecha de la pantalla y alineado con la base del texto.

**Motivo / criterio:** *Fricción Cero y Microinteracciones*. Facilitar atajos de navegación contextuales mejora radicalmente la Experiencia de Usuario (UX) en páginas que actúan como índices o directorios largos. Al usar CSS nativo (Flexbox), se logra el diseño perfecto sin afectar el rendimiento ni requerir JavaScript.

**Siguiente paso o deuda:** Desarrollar el publicador Headless (`merci-wp.py`) para escribir en WordPress local desde la terminal.

### 2026-04-29 — UX: Corrección de flujo de navegación en índice de Biblioteca

**Contexto:** Los sub-enlaces del índice curado recién generado dirigían al usuario directamente a la página del artículo individual, provocando que la sección de tarjetas resumen de la propia página índice quedara huérfana e ignorada.

**Hecho:** Se modificaron los enlaces del bloque `<nav>` en `scripts/merci/merci-publish.py` para que actúen como anclas internas (`#`). Simultáneamente, se inyectaron IDs dinámicos (basados en el título) y la propiedad `scroll-margin-top` en los elementos `<article>` de las tarjetas.

**Detalle técnico:** Al utilizar `slugify(pub["titulo"])` generamos un anclaje único por tarjeta (ej. `id="mi-articulo"`). Los enlaces del menú ahora apuntan a `#mi-articulo` en lugar de a `/biblioteca/mi-articulo.html`.

**Motivo / criterio:** *Retención de Contexto y UX*. El objetivo de una página índice es actuar como un escaparate. Redirigir al usuario al resumen de la tarjeta permite que lea la descripción (excerpt) antes de decidir si desea hacer clic en el título y abandonar la navegación panorámica.

**Siguiente paso o deuda:** Desarrollar el publicador Headless (`merci-wp.py`) para escribir en WordPress local desde la terminal.

### 2026-04-29 — UX/UI: Expansión del índice curado con sub-enlaces de artículos (SSG)

**Contexto:** El índice curado superior recién creado solo mostraba las "Estanterías" (temas), obligando al usuario a hacer clic o scroll a ciegas para descubrir qué artículos contenía cada categoría.

**Hecho:** Se refactorizó el bucle de generación del índice en `scripts/merci/merci-publish.py` para inyectar una lista anidada (`<ul>`) con los enlaces directos a cada artículo bajo su respectiva estantería.

**Detalle técnico:** Se alteró el layout del contenedor padre (`<li>`) aplicando CSS `flex: 1 1 300px`, creando automáticamente un diseño de columnas responsivo (tipo mampostería) que se adapta al ancho de la pantalla móvil o de escritorio sin usar CSS Grid explícito.

**Motivo / criterio:** *Fricción Cero y Descubrimiento*. Evolucionar el índice hacia un patrón de "Mega Menú" o "Mapa del Sitio" visual expone todo el conocimiento disponible en el primer impacto (Above the Fold). Al autogenerarse en Python durante el proceso SSG, esta rica interfaz cuesta 0 milisegundos de renderizado extra al navegador.

**Siguiente paso o deuda:** Desarrollar el publicador Headless (`merci-wp.py`) para escribir en WordPress local desde la terminal.

### 2026-04-29 — UX: Reestructuración visual e índice curado en la Biblioteca (SSG)

**Contexto:** La página principal autogenerada de la Biblioteca carecía de una sección `Hero`, lo que rompía la consistencia visual con el resto del ecosistema (Portada, Contacto). Además, carecía de un índice rápido, dificultando la navegación a medida que aumentaban las estanterías temáticas.

**Hecho:** Se refactorizó la función `generar_indice_biblioteca()` en `scripts/merci/merci-publish.py` para inyectar una sección `Hero` y un bloque `<nav>` dinámico con enlaces ancla.

**Detalle técnico:** Se reutilizó la función existente `slugify()` para convertir los nombres de los temas en atributos `id` HTML5 válidos. Se inyectó la propiedad CSS nativa `scroll-margin-top: 100px;` en cada sección temática para garantizar que la cabecera fija de la web no solape los títulos al realizar saltos internos mediante los enlaces ancla.

**Motivo / criterio:** *UX (Experiencia de Usuario) y Fricción Cero*. Un motor de Generación de Sitios Estáticos (SSG) no solo debe agrupar enlaces, debe maquetar interfaces coherentes. Autogenerar el índice curado (*Table of Contents*) elimina la necesidad de mantenimiento manual por parte del autor al inaugurar nuevos temas.

**Siguiente paso o deuda:** Desarrollar el publicador Headless (`merci-wp.py`) para escribir en WordPress local desde la terminal.

### 2026-04-29 — Feat: Reestructuración y unificación del pipeline maestro (merci-total)

**Contexto:** Para evitar desincronizaciones por olvido de compilación manual, se vió que integrar el motor SSG (`merci-publish.py`) dentro del orquestador global de QA (`merci-total.py`) actualizaría la página de biblioteca a los nuevos formatos. Además, se detectó que el sincronizador de páginas (`merci-sync-pages.py`) se estaba ejecutando al final del proceso, después de las herramientas de auditoría.

**Hecho:** 
- Se inyectó `merci-publish.py` en la constante `PIPELINE` de `merci-total.py`.
- Se reordenó el flujo de ejecución para separar estrictamente la Fase de Compilación (Build) de la Fase de Aseguramiento de Calidad (QA).

**Detalle técnico:** El nuevo orden arquitectónico es: Optimización multimedia -> Compilación SASS -> Generación SSG (Publish) -> Propagación SSOT (Sync Pages) -> Generación de XML (Sitemap) -> Auditoría Shift-Left (Audit) -> Rastreo de enlaces (Linkcheck). 

**Motivo / criterio:** *Pipeline as Code y Shift-Left*. Si las herramientas de QA (Audit, Linkcheck, Sitemap) se ejecutan antes de que los HTML definitivos hayan sido generados o sincronizados, el orquestador estaría validando "código fantasma" u obsoleto, dando falsos positivos de éxito. El orden de ejecución es tan crítico como el código mismo.

**Siguiente paso o deuda:** Desarrollar el índice curado de la biblioteca o el publicador Headless (`merci-wp.py`).

### 2026-04-29 — Feat: Sincronización automatizada de páginas estáticas (SSOT)

**Contexto:** La página estática de contacto (`public/contacto/index.html`) requería actualización manual de la cabecera, pie de página y asistente Merci cada vez que la portada cambiaba, violando el principio de única fuente de verdad (SSOT).

**Hecho:**
- Se desarrolló el script `scripts/merci/merci-sync-pages.py`.
- Se actualizó el `README.md` marcando la tarea de contacto como completada y registrando el nuevo script.

**Detalle técnico:** El script en Python utiliza Expresiones Regulares (`re.sub` y `re.search`) con la bandera `re.DOTALL` para capturar físicamente el `<header>`, `<footer>` y `<aside class="merci-ui">` de `public/index.html` y sobrescribirlos en `public/contacto/index.html`.

**Motivo / criterio:** *Fricción Cero y Single Source of Truth*. Al igual que `merci-publish` genera los artículos a partir del marco de la portada, `merci-sync-pages` extiende esa misma lógica de componentes inmutables a las páginas estáticas independientes. Elimina el riesgo de "desincronización visual" por error humano.

**Siguiente paso o deuda:** Integrar la llamada a `merci-sync-pages.py` dentro del orquestador `merci-total.py` para automatizarlo en el QA global, y crear el índice curado de la biblioteca.

### 2026-04-29 — Docs: Expansión del Roadmap (Fase 8.3 Consolidación Operativa)

**Contexto:** Antes de proceder con las tareas de consolidación de UX (contacto, home, índice de biblioteca) y automatización Headless (publicador WP y automatización de LinkedIn), se detectó que estas intenciones no estaban formalmente registradas en el Roadmap, contraviniendo el rigor de las directrices operativas.

**Hecho:** Se expandió la Fase 8 en el `README.md` inyectando la subfase `8.3 Consolidación Operativa (UX y Headless CMS)`. Se marcó como completada la primera tarea (inyección de enlaces en el footer).

**Detalle técnico:** La Regla 12 de `instrucciones.md` exige mantener la hoja de ruta sincronizada. Añadir las tareas de consolidación formaliza la deuda técnica autoimpuesta y prepara el terreno para el desarrollo de `merci-wp.py`.

**Motivo / criterio:** *Governance y Compliance (Gobernanza y Cumplimiento)*. En un ciclo de vida estructurado, ninguna maniobra técnica "improvisada" es válida. Todo desarrollo debe responder a un requisito explícito en el Roadmap para mantener la Única Fuente de Verdad (SSOT).

**Siguiente paso o deuda:** Completar la página estática de Contacto (`public/contacto/index.html`) y refinar la portada.

### 2026-04-29 — UX/UI: Consolidación de la interfaz y enlaces globales

**Contexto:** Antes de abordar la Fase 9 (Integración de IA), se detectó la necesidad de consolidar la UX (User Experience - Experiencia de Usuario) inyectando los enlaces a redes profesionales (LinkedIn, GitHub) y al ecosistema hijo (`merci-boilerplate`), además de buscar un modelo de publicación para WordPress que no dependiera del panel de administración (GUI).

**Hecho:** 
- Se inyectó el bloque `.footer__links` en `public/index.html` con atributos de seguridad para enlaces externos (`target="_blank" rel="noopener noreferrer"`).

**Detalle técnico:** Al inyectar los enlaces en el `<footer>` de la portada estática, el orquestador `merci-publish.py` los absorberá y propagará automáticamente a todos los artículos compilados de la Biblioteca en su próxima ejecución, manteniendo el principio de SSOT (Single Source of Truth).

**Motivo / criterio:** *Consolidación antes de Innovación*. Evitar el "Shiny Object Syndrome" estabilizando la identidad pública y los flujos de trabajo locales (Headless CMS) garantiza que el ecosistema base sea robusto y operable antes de introducir lógicas asíncronas complejas como la Inteligencia Artificial.

**Siguiente paso o deuda:** Crear la página estática de Contacto (`public/contacto/index.html`) y propagar el nuevo footer a la plantilla de WordPress.

### 2026-04-29 — DevSecOps: Truncamiento de historial Git (Orphan Branch) en Boilerplate

**Contexto:** Tras el despliegue exitoso de la Release 1.0.0 del Boilerplate, una inspección del `git log` reveló que el repositorio destino conservaba el historial de commits de la matriz original, exponiendo metadatos, correos electrónicos y trazabilidad privada.

**Hecho:** Se ejecutó un truncamiento absoluto del historial en el repositorio `merci-boilerplate` local utilizando `git checkout --orphan`, seguido de una reescritura remota con `git push --force`.

**Detalle técnico:** La creación de una rama huérfana (`--orphan`) desconecta el árbol de trabajo actual de cualquier commit anterior. Al reemplazar la rama `main` con esta nueva rama y forzar la subida, el servidor remoto (GitHub) descarta el historial antiguo, dejando un único commit fundacional inmaculado.

**Motivo / criterio:** *Data Leak Prevention* (Prevención de Pérdida de Datos). Un boilerplate público debe ser un lienzo en blanco (Zero Trust). El código fuente no solo incluye los archivos físicos actuales, sino toda la memoria inmutable de Git. Purgar el historial asegura la sanitización total de la propiedad intelectual exportada.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-29 — Fix: Sincronización destructiva (rsync --delete) y purga de assets

**Contexto:** Tras la instanciación del Boilerplate, se detectó que los archivos originales (`README-merci.md`, `bitacora-mercedev.md`, scripts temporales y multimedia personal) seguían apareciendo en el repositorio destino, a pesar de que `merci-init.py` los borraba o renombraba correctamente en el clon temporal.

**Hecho:** 
- Se añadió la bandera `--delete` al comando `rsync` en `mantenimiento-boilerplate-sop.md`.
- Se amplió `merci-init.py` para purgar explícitamente `.assets-raw`, `assets/images` (conservando logos/favicon) y `public/art-de-cote`.

**Motivo / criterio:** *Configuration Drift* (Archivos Fantasma). El comando `rsync` estándar solo añade o actualiza archivos; si el repositorio de destino contiene archivos de subidas anteriores que ya no existen en la matriz, estos nunca se borrarán a menos que se exija una sincronización de espejo estricta con `--delete`. Esto resuelve el falso positivo de fallo en el orquestador Python y garantiza un empaquetado inmaculado.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-29 — Fix: Purga de Shadow Docs residuales en instanciación

**Contexto:** Al ejecutar la instanciación (`merci-init.py`) siguiendo el SOP de mantenimiento, se detectó que los archivos originales `README-merci.md` e `instrucciones-merci.md` permanecían en el directorio junto a sus versiones definitivas (`README.md` e `instrucciones.md`), generando duplicidad documental en el Boilerplate.

**Hecho:** Se instruyó la corrección en `scripts/merci/merci-init.py` para aplicar una maniobra destructiva (renombrado atómico) al ascender los *Shadow Docs*.

**Detalle técnico:** En lugar de una simple copia, el orquestador Python debe utilizar el método `.replace()` de `pathlib.Path` para sobrescribir atómicamente el documento destino y erradicar el archivo `-merci` de origen en un solo movimiento.

**Motivo / criterio:** *Zero Bloat* y *Single Source of Truth*. El código fuente exportado debe ser inmaculado. Conservar la infraestructura "en la sombra" dentro del repositorio público del Boilerplate confunde al usuario final y expone artefactos de la matriz innecesariamente.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-29 — Docs: Aclaración del pipeline de rsync y Shadow Docs

**Contexto:** Existía la duda de si el comando de sincronización `rsync` hacia el repositorio del Boilerplate debía excluir explícitamente los manuales de la matriz (`README.md` e `instrucciones.md`) para evitar contaminar el repositorio destino, o si debían viajar los archivos gemelos (`-merci.md`).

**Hecho:** Se validó y documentó la simplificación del comando de transferencia (`rsync -av --exclude='.git'`) en el SOP de mantenimiento, sin añadir exclusiones manuales para la documentación.

**Detalle técnico:** La topología del *Release Pipeline* delega la manipulación de archivos al script de instanciación (`merci-init.py`), el cual se ejecuta en un directorio efímero *antes* de la sincronización. Este script elimina físicamente los manuales de la matriz y renombra los *Shadow Docs* a sus nombres definitivos. Al ejecutarse el comando `rsync` en el paso posterior, la carpeta ya contiene la documentación purificada y correcta.

**Motivo / criterio:** *Separation of Concerns* (Separación de Responsabilidades) y *Infrastructure as Code*. El orquestador de Python es el único responsable de la mutación estructural del proyecto. Delegar exclusiones complejas a un comando de shell (rsync) lo vuelve frágil e interfiere con el ascenso de los documentos correctos preparados por el script.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-28 — Docs: Auditoría externa de IA y expansión del Roadmap (Fase 11)

**Contexto:** Tras cerrar la Fase 10 (Release 1.0.0 del Boilerplate), se sometió el repositorio a un análisis externo (Copilot). El dictamen situó la arquitectura en el top 1-3% global por rigor DevSecOps y optimización, y sugirió mejoras de integración en la nube.

**Hecho:**
- Se filtraron las propuestas, rechazando las que requerían dependencias pesadas (Cypress, telemetría) y aceptando las de CI/CD puro.
- Se inyectó la nueva "Fase 11: Integración Continua y Calidad en la Nube" en el Roadmap del `README.md` e `instrucciones.md` (GitHub Actions, Lighthouse CI e Issue Templates).

**Motivo / criterio:** *Continuous Improvement* (Mejora Continua). La validación externa confirma la solidez fundacional. Adoptar flujos de CI en la nube alinea el proyecto con estándares corporativos Enterprise, delegando la auditoría al servidor sin engordar el código fuente local ni violar la política de cero dependencias bloqueantes.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-28 — Docs: Principio de inmutabilidad en el registro histórico

**Contexto:** Tras reubicar documentos operativos a la carpeta `docs/matriz/`, se debatió si actualizar las rutas absolutas mencionadas en entradas de la bitácora redactadas en días anteriores (Fase 7) para que coincidieran con la nueva topología.

**Hecho:** Se decidió no modificar los registros pasados y asentar la regla estricta de inmutabilidad documental en el laboratorio.

**Motivo / criterio:** *Append-Only Log* (Registro de solo adición). La bitácora es un documento forense que refleja la realidad técnica exacta del momento en que se escribió. Reescribir el pasado para ajustar rutas o nombres de archivos que cambiaron posteriormente destruye la trazabilidad y es un antipatrón de auditoría. Los cambios arquitectónicos se documentan siempre como nuevos eventos en el presente.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-28 — Refactor: Agrupación de SOPs exclusivos en subdirectorio matriz/

**Contexto:** La purga selectiva de manuales en `merci-init.py` requería añadir manualmente cada nuevo archivo a eliminar, lo cual no es escalable si el proyecto matriz aumenta su documentación interna.

**Hecho:**
- Se creó el subdirectorio `docs/matriz/` y se movieron los archivos `flujo-publicacion-sop.md` y `mantenimiento-boilerplate-sop.md` mediante `git mv`.
- Se actualizó `merci-init.py` para erradicar el directorio completo `docs/matriz/` de forma dinámica mediante `shutil.rmtree()`.

**Motivo / criterio:** *Escalabilidad y Mantenibilidad*. Agrupar los documentos exclusivos del proyecto matriz en una única carpeta dedicada simplifica la lógica del script destructivo. Cualquier futuro manual interno depositado en esa carpeta quedará automáticamente excluido del Boilerplate sin necesidad de modificar código Python.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-28 — Fix: Resolución de colisión de contexto (Enrutamiento en MerciController)

**Contexto:** El asistente Merci repetía las frases del Blog al navegar por la Tienda. Esto ocurría porque la URL de la tienda (`/blog/tienda`) contiene el segmento `/blog`, provocando un falso positivo en la validación secuencial del controlador.

**Hecho:** Se inyectó una cláusula condicional específica para `/tienda` en el método `_loadKnowledgeBase()` de `public/js/MerciController.js`.

**Detalle técnico:** En enrutamientos de frontend basados en coincidencias de subcadenas (`String.prototype.includes()`), el orden de evaluación es estricto. Se ubicó la validación de `/tienda` estructuralmente *antes* que la de `/blog` para que el bloque `if` intercepte la ruta anidada más específica en primer lugar.

**Motivo / criterio:** *Context-Awareness* (Conciencia de contexto). Para que un agente conversacional mantenga la coherencia, la inferencia de su entorno debe manejar correctamente las colisiones de directorios. 

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-28 — Fix: Expansión de acrónimos rezagados (TTFB y CPU)

**Contexto:** La auditoría pre-commit (`merci-audit.py`) detectó acrónimos no expandidos (TTFB y CPU) en la bitácora y en cuadernillos promovidos a la biblioteca, bloqueando el empaquetado para asegurar la accesibilidad cognitiva.

**Hecho:** Se expandieron los acrónimos `TTFB` y `CPU` siguiendo el estándar `Acrónimo (Inglés - Español)` en los archivos correspondientes.

**Motivo / criterio:** *Inclusión Cognitiva*. La auditoría es implacable por diseño: cualquier nuevo acrónimo introducido en la documentación debe ser explicado en su primera aparición para no generar deuda técnica documental.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-28 — Fix: Resolución de TypeError por método inexistente en MerciController

**Contexto:** Al interactuar con el asistente Merci en el entorno local, la consola del navegador arrojaba el error fatal `Uncaught TypeError: this.setState is not a function`.

**Hecho:** Se corrigió la asignación de estado en el método `sleep()` de `public/js/MerciController.js`.

**Detalle técnico:** Se reemplazó la llamada al método inexistente `this.setState('idle')` por la asignación directa de la propiedad `this.state = 'idle'`.

**Motivo / criterio:** *Vanilla JS vs Frameworks*. El uso de `setState` es un remanente o confusión común procedente de frameworks reactivos (como React). En una arquitectura de 0 dependencias con POO estricta, si no se declara un *setter* explícito, el estado se muta directamente sobre la propiedad de la instancia para evitar colapsos de ejecución.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-28 — Docs: Redacción de cuadernillos técnicos (QA, Git y WP)

**Contexto:** Antes de sellar la nueva versión base del ecosistema, era imperativo transformar las resoluciones técnicas críticas de la última sesión (conflictos de Git, caché móvil y jerarquía de WooCommerce) en activos de conocimiento reutilizables.

**Hecho:** Se redactaron tres nuevos cuadernillos en formato borrador dentro de `laboratorio/`:
- `cuadernillo-cache-movil-webkit.md` (Cache Busting)
- `cuadernillo-domando-woocommerce.md` (Template Hierarchy)
- `cuadernillo-conflictos-git-ours.md` (Git Merge Conflicts)

**Motivo / criterio:** *Knowledge Management* (Gestión del Conocimiento). La documentación operativa no solo abarca el "cómo instalar", sino el "cómo sobrevivir". Documentar los incidentes reales bajo los 3 átomos del proyecto convierte la deuda técnica sufrida en una inversión formativa para el futuro del *Boilerplate*.

**Siguiente paso o deuda:** Promover los cuadernillos a la Biblioteca o Art de Coté (según corresponda) mediante `merci-promote.py` e iniciar la Fase 9.

### 2026-04-28 — QA: Certificación 100/100 en Core Web Vitals (Capa Dinámica)

**Contexto:** Antes de empaquetar y exportar la versión final del Boilerplate (Release 1.0.0), se requería validación empírica de que la capa dinámica (WordPress/WooCommerce) no degradaba el rendimiento extremo del núcleo estático.

**Hecho:** Se ejecutó la auditoría de Google PageSpeed Insights (Lighthouse) sobre la ruta de producción `/blog` en la vista móvil.

**Detalle técnico:** La auditoría certificó una puntuación perfecta cuádruple: 100 Rendimiento, 100 Accesibilidad, 100 Mejores Prácticas y 100 SEO. Métricas clave: FCP 0.8s, LCP 1.1s, TBT 0ms. Esto valida empíricamente el éxito de las purgas de assets (`wp_dequeue_style` de `wc-blocks`) y la arquitectura de proxy inverso.

**Motivo / criterio:** *QA Assurance* (Aseguramiento de Calidad). Una infraestructura DevSecOps no admite suposiciones. Validar la excelencia técnica en el entorno más hostil (móvil 4G simulado sobre CMS) es el requisito final innegociable antes de liberar una plantilla fundacional al público.

**Siguiente paso o deuda:** Ejecutar el Release Pipeline (exportar a `merci-boilerplate`) e iniciar la Fase 9.

### 2026-04-28 — Fix: Resolución de colisión y carga doble de scripts JS en WP

**Contexto:** La consola del navegador en el entorno dinámico (`/blog`) arrojaba un error crítico: `SyntaxError: Identifier 'NavigationController' has already been declared`. Este error colapsaba la ejecución del frontend.

**Hecho:** Se desactivó la carga de `main.js` mediante `wp_enqueue_script` en `functions.php`.

**Detalle técnico:** Al implementar el patrón de *Cache Busting* dinámico (`time()`) en las plantillas `index.php` y `woocommerce.php`, se insertó la etiqueta `<script>` directamente en el `<head>`. Sin embargo, `functions.php` seguía encolando el mismo archivo en el `wp_footer()`. Declarar una clase de ES6 (`class NavigationController`) dos veces en el mismo ámbito global (Global Scope) produce un `SyntaxError` fatal.

**Motivo / criterio:** *Single Source of Truth*. Los *assets* estáticos deben cargarse desde un único punto de control. Al haber delegado la responsabilidad del versionado dinámico directamente a las plantillas, la inyección desde el functions queda obsoleta y genera una condición de carrera y duplicidad de código.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-28 — Perf: Purga de bloques WooCommerce y oEmbed en WP

**Contexto:** La auditoría de Lighthouse (PageSpeed Insights) reveló que la capa dinámica (Blog/Tienda) no alcanzaba el 100/100 en móviles, sufriendo penalizaciones por CSS y JS no utilizado, a diferencia del núcleo estático.

**Hecho:** Se inyectaron reglas de desencolado (`wp_dequeue_style`) para `wc-blocks-style` y `wc-blocks-vendors-style` en `functions.php`. Se eliminaron los enlaces de oEmbed y REST API de la cabecera.

**Detalle técnico:** Aunque se había desactivado el CSS base de WooCommerce en fases anteriores, el plugin inyecta silenciosamente un archivo masivo de estilos para sus bloques de Gutenberg (`wc-blocks-style`). Adicionalmente, WP inyecta scripts de descubrimiento oEmbed innecesarios. Su purga restaura el DOM ultraligero.

**Motivo / criterio:** *Zero Bloat* (Cero Basura). La disparidad de rendimiento entre el SSG y WP suele radicar en el código "invisible" que los plugins asumen que el tema necesita. Desactivar todo lo que no esté estrictamente controlado por nuestra arquitectura SASS 7-1 protege las Core Web Vitals en dispositivos móviles de gama baja.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-28 — Fix: Soporte oficial WooCommerce y purga absoluta de caché PHP

**Contexto:** La tienda ignoraba el archivo `woocommerce.php` y los dispositivos móviles seguían mostrando HTML/CSS cacheado en vistas dinámicas, impidiendo el uso del menú y ocultando al asistente.

**Hecho:**
- Se inyectó `add_theme_support('woocommerce')` en `functions.php` para obligar al plugin a respetar la jerarquía de plantillas del tema.
- Se reemplazó la lógica `filemtime` por `time()` en los *Cache Busters* de las plantillas PHP para forzar peticiones únicas en cada recarga.
- Se incrementó a `v=11` la versión de los *assets* en páginas HTML estáticas.

**Motivo / criterio:** *Template Hierarchy y Cache Invalidation*. WooCommerce se protege a sí mismo sirviendo sus plantillas base si el tema activo no declara soporte explícito, ignorando `woocommerce.php`. Para entornos de desarrollo o infraestructuras con cachés agresivas, usar el *timestamp* actual (`time()`) es la única garantía de purga instantánea sin acceso directo al servidor.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-28 — Fix: Rutas de caché dinámico en WP y alineación de footer

**Contexto:** El menú móvil seguía sin funcionar en las vistas dinámicas (WordPress) debido a que la función de purga de caché PHP apuntaba a una ruta de servidor incorrecta, sirviendo versiones obsoletas del JS. Adicionalmente, el enlace "Volver arriba" interfería visualmente con el asistente Merci en pantallas pequeñas al estar centrado.

**Hecho:**
- Se corrigió la ruta de `$root_dir` en `index.php` y `woocommerce.php` para apuntar correctamente al directorio estático en el servidor anfitrión (`/mercedev.es/public`).
- Se refactorizó la estructura HTML del `<footer>` en todas las plantillas, alineando el texto a la izquierda y añadiendo un padding inferior de seguridad (`6rem`).

**Motivo / criterio:** *Rutas Absolutas y Usabilidad (UX)*. Al usar enlaces simbólicos en Nginx, la constante `ABSPATH` de WordPress requiere una travesía de directorios explícita para localizar los archivos estáticos. A nivel de UI, aislar los elementos interactivos flotantes (Merci) de los enlaces base del footer previene clics accidentales (Fat Finger Syndrome) en dispositivos móviles.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-28 — Fix: Unificación de carga de assets y Cache Busting dinámico en WP

**Contexto:** Una auditoría multidispositivo final reveló que, a pesar de los parches anteriores, las vistas dinámicas (Blog, Tienda) y la página estática de Contacto seguían mostrando versiones cacheadas de CSS y JS en tablets y móviles, rompiendo la UI de Merci y el menú.

**Hecho:**
- Se implementó la carga directa del `main.css` con `filemtime` en `index.php` y `woocommerce.php`, eliminando la dependencia del `functions.php`.
- Se actualizaron manualmente la versión de los assets en `contacto/index.html` y `index.html` para forzar la purga de caché.

**Motivo / criterio:** *Single Source of Truth* y *Cache Invalidation*. La gestión de assets debe ser consistente. Cargar todos los recursos del núcleo estático (CSS y JS) con la misma estrategia de versionado dinámico en todas las plantillas (estáticas y PHP) erradica definitivamente los problemas de caché y asegura la paridad visual y funcional entre todos los dispositivos.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-28 — Fix: Unificación de carga de assets y Cache Busting dinámico en WP

**Contexto:** Una auditoría multidispositivo final reveló que, a pesar de los parches anteriores, las vistas dinámicas (Blog, Tienda) y la página estática de Contacto seguían mostrando versiones cacheadas de CSS y JS en tablets y móviles, rompiendo la UI de Merci y el menú.

**Hecho:**
- Se implementó la carga directa del `main.css` con `filemtime` en `index.php` y `woocommerce.php`, eliminando la dependencia del `functions.php`.
- Se actualizaron manualmente la versión de los assets en `contacto/index.html` y `index.html` para forzar la purga de caché.

**Motivo / criterio:** *Single Source of Truth* y *Cache Invalidation*. La gestión de assets debe ser consistente. Cargar todos los recursos del núcleo estático (CSS y JS) con la misma estrategia de versionado dinámico en todas las plantillas (estáticas y PHP) erradica definitivamente los problemas de caché y asegura la paridad visual y funcional entre todos los dispositivos.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-27 — Fix: Restauración de WooCommerce y dependencias dinámicas JS

**Contexto:** Una auditoría móvil exhaustiva reveló que las páginas de WordPress (Blog/Tienda) no desplegaban el menú hamburguesa y que WooCommerce perdía todo el formato visual y estructural del tema.

**Hecho:**
- Se inyectó dinámicamente `main.js` en `index.php` utilizando `filemtime` para forzar la purga de caché.
- Se creó el archivo `woocommerce.php` en el Child Theme copiando la estructura base monolítica.
- Se aplicaron los Cache Busters (`?v=...`) y el ancla `#top` a la página estática `contacto/index.html`.

**Motivo / criterio:** *Template Hierarchy* y Paridad. El fallo del menú en WP se debía a la omisión de `main.js` (donde reside el controlador de navegación). La rotura de la tienda se debía a que WooCommerce ignora `index.php` e inyecta su propio HTML desnudo a menos que exista un `woocommerce.php` explícito que envuelva su función `woocommerce_content()` dentro de nuestra arquitectura BEM.

**Siguiente paso o deuda:** Desplegar en producción y confirmar resolución en dispositivos móviles.

### 2026-04-27 — Fix: Resolución de Caché Móvil y Bug de pointer-events (iOS Safari)

**Contexto:** El asistente Merci funcionaba correctamente en la simulación móvil del PC, pero en un dispositivo físico real aparecía roto (posición estática al final de la página) y sus clics eran ignorados.

**Hecho:** 
- Se inyectaron *Cache Busters* (`?v=...`) en las etiquetas `<script>` y `<link>` en todas las plantillas HTML/PHP del proyecto.
- Se eliminaron las reglas CSS `pointer-events: none` y `pointer-events: auto` del contenedor de Merci en SASS.

**Detalle técnico:** El síntoma de disparidad entre el PC y el móvil físico es el indicador estándar de caché agresiva. El navegador móvil conservaba una versión antigua de `main.css` y `MerciController.js` en memoria. Adicionalmente, se retiró el uso de `pointer-events` cruzados debido a un bug conocido en WebKit (iOS Safari) donde el navegador se niega a registrar eventos de *touch/click* en elementos hijos si el contenedor padre tiene `pointer-events: none`.

**Motivo / criterio:** *Cross-Browser Compatibility* (Compatibilidad entre navegadores). Inyectar versiones en los *assets* estáticos obliga a los móviles a purgar su caché y descargar el último código. Evitar "hacks" de CSS (`pointer-events`) en contenedores interactivos previene colapsos en motores de renderizado estrictos como los de Apple.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-27 — Feat: Reubicación automática de borradores al laboratorio en SSG

**Contexto:** Se estableció como regla de arquitectura que la carpeta `biblioteca/` no debe contener archivos en estado de incubación o borrador (Environment Segregation). Sin embargo, si un archivo era despublicado cambiando su YAML a `estado: "borrador"`, permanecía físicamente en la biblioteca, requiriendo su traslado manual.

**Hecho:** Se implementó una rutina de reubicación física en la máquina de estados de `scripts/merci/merci-publish.py`.

**Detalle técnico:** En el bloque de control del "Kill-Switch", si un documento no tiene el estado `publicado`, además de purgar sus artefactos HTML/PDF generados, el orquestador utiliza `shutil.move()` para trasladar el archivo `.md` original de vuelta al directorio `laboratorio/`.

**Motivo / criterio:** *Automation & Environment Segregation*. Un entorno DevSecOps maduro no confía en la disciplina manual para mantener la higiene de los directorios. El orquestador actúa como un agente activo que expulsa el contenido no válido del entorno de producción hacia la zona de pruebas.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-28 — Fix: Purga selectiva de SOPs en instanciación de Boilerplate

**Contexto:** Se detectó que el script de inicialización (`merci-init.py`) exportaba la totalidad de la carpeta `docs/` al nuevo proyecto. Esto incluía manuales de procedimiento (SOP) exclusivos de la matriz (`flujo-publicacion-sop.md` y `mantenimiento-boilerplate-sop.md`), generando ruido documental y confusión para el usuario final del Boilerplate.

**Hecho:** Se inyectó una rutina de borrado selectivo (`unlink`) para los archivos SOP específicos dentro de la fase de purga de `scripts/merci/merci-init.py`.

**Motivo / criterio:** *Separation of Concerns* (Separación de Responsabilidades Documentales). La documentación de infraestructura (`deployment`, `hardening`) es agnóstica y debe viajar con la plantilla. La documentación de gobierno de repositorios y flujos de publicación personalizados pertenece exclusivamente a la "Instancia Cliente" (el proyecto matriz) y debe ser erradicada del código base redistribuible.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-28 — Docs: Creación del SOP de actualización del Boilerplate

**Contexto:** Las instrucciones para actualizar el repositorio `merci-boilerplate` desde el proyecto matriz estaban definidas únicamente en la Regla 14 de `instrucciones.md` y en un cuadernillo divulgativo, dificultando su localización como manual operativo estricto.

**Hecho:** Se redactó el documento `docs/mantenimiento-boilerplate-sop.md`.

**Motivo / criterio:** *Operabilidad y SSOT*. Un proceso complejo de múltiples pasos que involucra clonaciones destructivas (`merci-init.py`), comandos nativos (`rm -rf`, `rsync`) y saltos entre repositorios debe estar centralizado en un documento SOP (Standard Operating Procedure) oficial para evitar errores humanos o pérdida de datos durante las futuras *releases*.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-27 — Fix: Resolución de TypeError por firmas de funciones en SSG

**Contexto:** El orquestador `merci-publish.py` colapsó con un `TypeError` (`takes 3 positional arguments but 6 were given`) al intentar compilar la biblioteca tras la actualización de caché móvil.

**Hecho:** Se actualizaron las firmas de las funciones `procesar_archivo` y `generar_indice_biblioteca` para aceptar los parámetros de versión dinámica.

**Detalle técnico:** Durante la implementación del *Cache Busting*, se añadieron tres nuevos argumentos en las invocaciones de las funciones dentro de `main()`, pero se omitió actualizar la definición de las mismas. Se inyectaron los argumentos `css_v`, `js_c_v` y `js_m_v` requeridos por las plantillas f-string internas.

**Motivo / criterio:** *Code Consistency* (Consistencia del código). Las definiciones de las funciones deben alinearse estrictamente con los argumentos inyectados y las interpolaciones generadas en las vistas HTML.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-27 — Fix: Restauración de WooCommerce y dependencias dinámicas JS

**Contexto:** Una auditoría móvil exhaustiva reveló que las páginas de WordPress (Blog/Tienda) no desplegaban el menú hamburguesa y que WooCommerce perdía todo el formato visual y estructural del tema.

**Hecho:**
- Se inyectó dinámicamente `main.js` en `index.php` utilizando `filemtime` para forzar la purga de caché.
- Se creó el archivo `woocommerce.php` en el Child Theme copiando la estructura base monolítica.
- Se aplicaron los Cache Busters (`?v=...`) y el ancla `#top` a la página estática `contacto/index.html`.

**Motivo / criterio:** *Template Hierarchy* y Paridad. El fallo del menú en WP se debía a la omisión de `main.js` (donde reside el controlador de navegación). La rotura de la tienda se debía a que WooCommerce ignora `index.php` e inyecta su propio HTML desnudo a menos que exista un `woocommerce.php` explícito que envuelva su función `woocommerce_content()` dentro de nuestra arquitectura BEM.

**Siguiente paso o deuda:** Desplegar en producción y confirmar resolución en dispositivos móviles.



### 2026-04-27 — Fix: Resolución de Caché Móvil y Bug de pointer-events (iOS Safari)

**Contexto:** El asistente Merci funcionaba correctamente en la simulación móvil del PC, pero en un dispositivo físico real aparecía roto (posición estática al final de la página) y sus clics eran ignorados.

**Hecho:** 
- Se inyectaron *Cache Busters* (`?v=...`) en las etiquetas `<script>` y `<link>` en todas las plantillas HTML/PHP del proyecto.
- Se eliminaron las reglas CSS `pointer-events: none` y `pointer-events: auto` del contenedor de Merci en SASS.

**Detalle técnico:** El síntoma de disparidad entre el PC y el móvil físico es el indicador estándar de caché agresiva. El navegador móvil conservaba una versión antigua de `main.css` y `MerciController.js` en memoria. Adicionalmente, se retiró el uso de `pointer-events` cruzados debido a un bug conocido en WebKit (iOS Safari) donde el navegador se niega a registrar eventos de *touch/click* en elementos hijos si el contenedor padre tiene `pointer-events: none`.

**Motivo / criterio:** *Cross-Browser Compatibility* (Compatibilidad entre navegadores). Inyectar versiones en los *assets* estáticos obliga a los móviles a purgar su caché y descargar el último código. Evitar "hacks" de CSS (`pointer-events`) en contenedores interactivos previene colapsos en motores de renderizado estrictos como los de Apple.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-27 — Fix: Resolución de caché móvil y consistencia de plantillas

**Contexto:** Una auditoría multidispositivo reveló que el asistente Merci y el menú móvil fallaban en tablets y teléfonos (CSS/JS rotos), y que las plantillas dinámicas (PHP) y estáticas (`contacto/`) tenían inconsistencias en el footer.

**Hecho:**
- Se implementó una estrategia de "Cache Busting" dinámico en `merci-publish.py` usando la fecha de modificación del archivo (`.stat().st_mtime`) como versión.
- Se actualizaron manualmente las versiones en los archivos estáticos (`index.html`, `contacto/index.html`).
- Se corrigió el placeholder `{{DOMINIO}}` en `src/wp-theme/merci-theme/index.php`.

**Motivo / criterio:** *Dev/Prod Parity & Cache Invalidation*. La disparidad entre el PC y el móvil es un síntoma inequívoco de caché agresiva. Usar `filemtime` como versión es la técnica más robusta para forzar la purga. Corregir los placeholders y los footers desactualizados restaura la consistencia visual y funcional en todo el ecosistema híbrido.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía. Se asume la deuda de refactorizar las plantillas de WooCommerce para corregir su footer.

### 2026-04-27 — Feat: Automatización de la fecha de última revisión en bitácora

**Contexto:** La línea final del archivo de bitácora (`*Última revisión de la bitácora: 2026-05-02.*`) contenía una fecha obsoleta (2026-04-14) porque dependía de la actualización manual por parte de la autora en cada sesión.

**Hecho:** Se implementó una rutina de actualización automática en `scripts/merci/merci-commit.py` mediante expresiones regulares.

**Detalle técnico:** Justo antes de ejecutar el `git add .`, el script lee el contenido completo de la bitácora, localiza la cadena de texto de la última revisión y sustituye la fecha por el día actual (`datetime.now()`), sobrescribiendo el archivo para que se empaquete con el dato exacto.

**Motivo / criterio:** *Fricción Cero*. Eliminar tareas repetitivas y propensas al error humano. Si el orquestador de commits ya lee la bitácora para extraer el mensaje, es el lugar arquitectónicamente perfecto para actualizar sus metadatos internos de forma transparente.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-27 — Fix: Expansión de acrónimo SEO en plantilla de proyecto

**Contexto:** Tras el simulacro de instanciación del Boilerplate, el auditor `merci-audit.py` levantó una advertencia por el acrónimo "SEO" no expandido. El diagnóstico reveló que el término residía en los comentarios del YAML Frontmatter del archivo `docs/plantilla-proyecto.md`.

**Hecho:** Se expandió el acrónimo SEO (Search Engine Optimization - Optimización para Motores de Búsqueda) directamente en la plantilla base del repositorio.

**Motivo / criterio:** *Standalone Compliance*. Al igual que ocurrió con los Shadow Docs, las plantillas fundacionales que sobreviven al script de inicialización (`merci-init.py`) deben ser semánticamente autosuficientes para no heredar advertencias de linter al nuevo usuario.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-27 — Fix: Expansión de acrónimos en Shadow Docs (Boilerplate)

**Contexto:** Al ejecutar la auditoría (`merci total`) en el repositorio clonado del Boilerplate, el linter de accesibilidad cognitiva emitió advertencias (WARN) por acrónimos no expandidos (como BEM). Esto ocurrió porque al purgar la biblioteca y el laboratorio, el recuento global de dichos términos cayó por debajo del umbral de consolidación (>3).

**Hecho:** Se expandió explícitamente el acrónimo BEM (Block, Element, Modifier - Modificador de Elemento de Bloque) en `README-merci.md`, `instrucciones-merci.md` e `instrucciones.md`.

**Detalle técnico:** Se aplicó la convención de expansión `ACRÓNIMO (Inglés - Español)` directamente en las documentaciones "en la sombra", garantizando que el texto base del Boilerplate cumpla con el análisis estático de `merci-audit.py` por sí mismo.

**Motivo / criterio:** *Standalone Compliance*. Una plantilla agnóstica debe ser 100% autosuficiente y superar su propia auditoría con 0 advertencias desde el commit inicial, sin depender de la densidad documental del proyecto matriz del que fue extraída.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía.

### 2026-04-27 — Docs: Versionado Semántico en Shadow Docs (v1.0.0)

**Contexto:** El documento en la sombra `README-merci.md` (que asciende a README oficial tras la instanciación) carecía de la declaración explícita de la versión del motor, dificultando la trazabilidad para los usuarios del Boilerplate.

**Hecho:** Se inyectó la etiqueta de versión `v1.0.0` en el encabezado principal de `README-merci.md`.

**Motivo / criterio:** *Semantic Versioning* (Versionado Semántico). El archivo maestro de un proyecto agnóstico debe indicar claramente en qué punto de madurez se encuentra. Al estar integrado en el Release Pipeline Agile (Regla 14), este número se incrementará manualmente en el proyecto matriz justo antes de empaquetar futuras *releases* (ej. `v1.1.0`).

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-27 — Perf: Optimización de peso en copias de seguridad (Backup Local)

**Contexto:** El script de copias de seguridad locales (`merci-backup.py`) estaba generando archivos ZIP de casi 47 MB, un peso desproporcionado para un repositorio de código y texto. El diagnóstico reveló que estaba comprimiendo los binarios de la carpeta `evidencias/` y los PDFs generados en `descargas/`.

**Hecho:** Se añadieron los directorios `evidencias` y `descargas` al conjunto (set) de exclusión `EXCLUDE_DIRS` en el script de backup.

**Detalle técnico:** Al ignorar estas carpetas en el recorrido `os.walk()`, se evita procesar y comprimir archivos multimedia pesados o artefactos dinámicos que pueden ser regenerados a voluntad mediante el orquestador SSG.

**Motivo / criterio:** *Performance y Eficiencia*. Una herramienta de *Disaster Recovery* local debe ser ultrarrápida y generar instantáneas ligeras. Excluir binarios que no forman parte del código fuente matriz garantiza que el backup se ejecute en milisegundos y consuma un espacio residual en el disco.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-27 — Feat: Bloqueo activo de evidencias y assets pesados (Shift-Left)

**Contexto:** Para asegurar que el historial de Git no se vuelva a contaminar con archivos binarios (vídeos, capturas) tras los incidentes con la carpeta `evidencias/`, el uso de `.gitignore` resultó ser insuficiente por su naturaleza pasiva frente a archivos previamente rastreados.

**Hecho:** Se implementó la regla `BANNED_TRACKED_FILE` en `scripts/merci/merci-audit.py` (auditor maestro).

**Detalle técnico:** Se creó la función `audit_banned_tracked_files` que consulta directamente a Git (`git ls-files` o `git diff --cached`). Si detecta que cualquier archivo (excepto `.gitkeep`) bajo `laboratorio/evidencias/` o `.assets-raw/` está a punto de ser comiteado o ya está siendo rastreado, inyecta un `ERROR` bloqueante en el estado de la auditoría.

**Motivo / criterio:** *Shift-Left Security*. Delegar la higiene del repositorio a la memoria humana o a un `.gitignore` pasivo genera fugas de datos. Un escudo activo (Linter) que bloquea el commit atómico previene físicamente la subida de archivos pesados al servidor remoto.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-27 — Fix: Erradicación de evidencias rastreadas heredadas

**Contexto:** Tras resolver un conflicto de fusión masivo, la carpeta `laboratorio/evidencias/` volvió a subirse al repositorio remoto a pesar de estar incluida en el `.gitignore`.

**Hecho:** Se ejecutó `git rm -r --cached laboratorio/evidencias/` para forzar a Git a "olvidar" los archivos sin borrarlos del disco duro local, y se generó un nuevo commit para purgar el servidor.

**Detalle técnico:** El archivo `.gitignore` previene que archivos *nuevos* sean añadidos al índice (`staged`), pero **no tiene efecto** sobre archivos que ya estaban siendo rastreados (tracked) en el historial previo. Al fusionar la rama remota, Git recuperó la memoria de esos archivos. Para aplicar un gitignore retroactivamente, es obligatorio eliminar los archivos de la caché de Git explícitamente.

**Motivo / criterio:** Higiene del repositorio. Comprender la diferencia entre archivos *tracked* y *untracked* es vital. La eliminación de la caché es la única maniobra válida para forzar a Git a soltar archivos que ya había asimilado en el pasado.

**Siguiente paso o deuda:** Inyectar una regla de validación en `merci-audit.py` para bloquear atómicamente cualquier commit que contenga archivos en esta carpeta.

### 2026-04-27 — Fix: Restauración de clase estructural para menú móvil

**Contexto:** En el entorno de producción, el menú hamburguesa no se desplegaba en las páginas de la Biblioteca ni en las vistas dinámicas de WordPress, aislando al usuario en móvil.

**Hecho:** Se inyectó la clase `.page` en las etiquetas `<body>` del orquestador `merci-publish.py` y del archivo `index.php` del Child Theme. También se corrigió la inyección del ancla invisible `#top` en el índice de la biblioteca.

**Detalle técnico:** El análisis del código Vanilla JS (`main.js`) reveló que estaba perfectamente estructurado con Cláusulas de Guarda (Guard Clauses), por lo que no había colapsos por `TypeError`. El fallo era exclusivamente CSS: las reglas de visualización del menú dependían del contexto `.page` en el `body`, el cual fue omitido durante la generación dinámica del HTML.

**Motivo / criterio:** Paridad de Entornos (Dev/Prod Parity). El núcleo estático base (`public/index.html`) poseía el atributo `class="page"` que habilitaba ciertas reglas SASS en cascada. Todo motor de renderizado (SSG o PHP) que reutilice el mismo CSS debe emitir exactamente la misma estructura de contenedores padre para evitar roturas visuales.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-27 — Fix: Resolución masiva de conflictos (Estrategia --ours)

**Contexto:** Al ejecutar `git pull`, estalló un conflicto de fusión masivo afectando a la bitácora, scripts, HTMLs y binarios (PDFs). El origen de esta colisión fue la reescritura del historial local (`git reset --soft`) realizada en sesiones anteriores, lo que provocó que el servidor remoto conservara un historial "fantasma" obsoleto que colisionó con la línea temporal actual.

**Hecho:** Se resolvieron los conflictos favoreciendo en bloque la versión local mediante el comando `git checkout --ours .`.

**Detalle técnico:** En lugar de resolver manualmente archivo por archivo (imposible para los binarios `add/add`), se utilizó la estrategia de resolución de Git que impone el árbol de trabajo local (`HEAD`) sobre el remoto. Esto elimina los marcadores de conflicto y restaura la integridad de los archivos generados y del código fuente.

**Motivo / criterio:** *Single Source of Truth (SSOT)*. Cuando se sabe con absoluta certeza que el entorno local contiene la última versión validada y segura del código (gracias al aislamiento DevSecOps), la maniobra más segura es descartar la rama remota divergente en bloque. Intentar fusionar código generado (SSG) manualmente es un antipatrón.

**Siguiente paso o deuda:** Finalizar el commit de fusión y continuar a la Fase 9.

### 2026-04-27 — Fix: Resolución de conflicto de sobreescritura en `git pull`

**Contexto:** Al ejecutar `git pull` tras configurar la estrategia de fusión, Git abortó la operación con el error: "Los cambios locales de los siguientes archivos serán sobrescritos al fusionar". Esto ocurrió porque existían modificaciones locales en `laboratorio/bitacora-mercedev.md` que aún no habían sido empaquetadas en un commit.

**Hecho:** Se empaquetaron los cambios locales pendientes mediante `merci-commit.py` antes de volver a intentar la sincronización.

**Detalle técnico:** Git se niega a ejecutar un `pull` si este va a sobrescribir trabajo local no guardado (uncommitted). El flujo de trabajo correcto es siempre: 1) Guardar el trabajo local (`git add .` y `git commit`) y 2) Sincronizar con el servidor (`git pull`).

**Motivo / criterio:** *Integridad de datos*. Es un mecanismo de seguridad fundamental de Git para prevenir la pérdida de trabajo. Nunca se debe forzar una sincronización sobre cambios locales no guardados. La solución es siempre confirmar el estado local antes de integrar el estado remoto.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).


### 2026-04-27 — Fix: Configuración de reconciliación para ramas divergentes (Git)

**Contexto:** Al ejecutar `git pull` para resolver un error de `non-fast-forward`, Git bloqueó la operación indicando que las ramas habían divergido (existían commits distintos tanto en local como en remoto) y requería especificar una estrategia de reconciliación explícita.

**Hecho:** Se configuró la estrategia de fusión por defecto (`git config pull.rebase false`) y se completó la sincronización (`git pull` seguido de `git push`).

**Detalle técnico:** Las ramas divergen cuando el historial local y el remoto se bifurcan (por ejemplo, al crear commits locales tras haber modificado el repositorio en la nube). Configurar `pull.rebase false` instruye a Git para que resuelva estas colisiones creando un "commit de fusión" (Merge Commit) estándar, preservando la cronología exacta de ambas líneas temporales sin reescribir el historial.

**Motivo / criterio:** Gobernanza del repositorio. Definir explícitamente la estrategia de fusión es una buena práctica de ingeniería que previene comportamientos erráticos o destructivos al sincronizar código en entornos de desarrollo distribuidos.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-27 — Fix: Restauración del scroll en el ancla "Volver arriba"

**Contexto:** El enlace "Volver arriba" (`#top`) en el footer dejó de realizar el desplazamiento (scroll) físico esperado. El script `merci-linkcheck.py` no auditó este error porque, por estándar técnico, los rastreadores ignoran los fragmentos de ancla (`#`).

**Hecho:** Se separó el identificador de ancla del contenedor visual `<header>`.

**Detalle técnico:** Se eliminó el `id="top"` y `tabindex="-1"` del `<header>` en `public/index.html` (y derivados) y se inyectó un `<div>` vacío (`position: absolute; top: 0; left: 0;`) con el `id="top"` justo después de abrir la etiqueta `<body>`. Se replicó la inyección en las plantillas f-string de `scripts/merci/merci-publish.py`.

**Motivo / criterio:** *Separation of Concerns* (Separación de responsabilidades). Al trasladar el `id="top"` al `<header>` (que es fijo o se encuentra siempre visible arriba) en la Fase 2, el navegador asumía que ya estaba en el *viewport* y omitía el scroll. Crear un ancla independiente restaura el scroll a la coordenada absoluta `0,0` manteniendo la puntuación WAI-ARIA 100/100.

**Siguiente paso o deuda:** Aplicar el mismo parche en la plantilla de WordPress (`src/wp-theme/merci-theme/index.php`) para mantener la paridad entre entornos.

### 2026-04-27 — Fix: Resolución de error `non-fast-forward` en `git push`

**Contexto:** Al intentar subir cambios al repositorio remoto (`git push`), la operación fue rechazada con el error `non-fast-forward`. Esto indica que el historial del servidor (GitHub) contenía commits que no existían en el repositorio local, creando una divergencia.

**Hecho:** Se ejecutó `git pull` para descargar los cambios remotos y fusionarlos con la rama local. Tras la fusión, se pudo ejecutar `git push` con éxito.

**Detalle técnico:** El comando `git pull` es un atajo para `git fetch` (descargar el historial del servidor) seguido de `git merge origin/main` (integrar los cambios remotos en la rama local). Si no hay conflictos, Git crea automáticamente un "merge commit" para unir las dos líneas de historial.

**Motivo / criterio:** *Integridad del Historial*. Git bloquea los `push` "non-fast-forward" como un mecanismo de seguridad para prevenir la sobreescritura accidental de trabajo que ya existe en el servidor. La solución canónica es siempre integrar los cambios remotos (`pull`) antes de empujar los locales (`push`), garantizando que no se pierda ningún commit.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-27 — Docs: Cuadernillo sobre recuperación de datos y peligros de GUI en Git

**Contexto:** Tras un incidente donde la interfaz gráfica del editor (VS Code) indujo a la eliminación física accidental de una carpeta no versionada (`evidencias/`), surgió la necesidad de documentar la vulnerabilidad operativa de depender de herramientas visuales para el control de versiones.

**Hecho:** Se redactó el activo de conocimiento `laboratorio/Recuperación de datos y el peligro de los comandos destructivos en Git-cuadernillo` detallando el incidente y la maniobra forense de rescate.

**Detalle técnico:** El cuadernillo expone cómo la regla `.gitignore` oculta elementos en la vista del editor, provocando ilusiones ópticas de borrado, y documenta la recuperación de los archivos desde la papelera del sistema anfitrión, reafirmando el uso de `ls -la` en terminal nativa como diagnóstico definitivo.

**Motivo / criterio:** *Knowledge Management* (Gestión del conocimiento). Transformar un accidente operativo en documentación fundacional mitiga el riesgo de que futuros desarrolladores repitan el error. Asienta la directriz de que la terminal es la única fuente de verdad y justifica la obligatoriedad de la herramienta de backups locales.

**Siguiente paso o deuda:** Iniciar la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-27 — Feat: Herramienta de copias de seguridad locales (Backup)

**Contexto:** El uso de interfaces gráficas o comandos complejos de Git conlleva el riesgo inherente de pérdida accidental de archivos locales no rastreados (ej. eliminación accidental al descartar cambios). Se requería un mecanismo "salvavidas" local antes de operar ramas o historiales.

**Hecho:** Se desarrolló `scripts/merci/merci-backup.py` y se añadió el directorio `backups/` al archivo `.gitignore`.

**Detalle técnico:** El script utiliza la librería estándar `zipfile` para empaquetar el árbol del proyecto de forma iterativa, excluyendo activamente directorios de infraestructura pesados (`.git`, `.venv`, `.assets-raw`) para garantizar una compresión rápida (Zip Deflated) y ligera.

**Motivo / criterio:** *Disaster Recovery* (Recuperación ante desastres). Proveer una herramienta CLI estandarizada que genere instantáneas locales (Snapshots) otorga confianza al desarrollador para realizar maniobras destructivas o refactorizaciones profundas sin depender exclusivamente del control de versiones remoto.

**Siguiente paso o deuda:** Iniciar el desarrollo de la Fase 9: Inteligencia y Autonomía (Integración de IA en Vanilla JS).

### 2026-04-27 — Fix: Exclusión estricta de evidencias del control de versiones

**Contexto:** La carpeta `laboratorio/evidencias/`, destinada a almacenar material multimedia pesado (vídeos, capturas) para futuros montajes, corría el riesgo de ser rastreada por Git y subida al servidor remoto, inflando el peso del repositorio.

**Hecho:** Se implementó una regla de exclusión estricta en `.gitignore` para `laboratorio/evidencias/*`, preservando únicamente el archivo `.gitkeep`.

**Detalle técnico:** Al igual que con el directorio `.assets-raw/`, esta regla permite que la estructura de carpetas persista en el proyecto mientras vuelve a Git completamente "ciego" ante los binarios que se depositen en su interior.

**Motivo / criterio:** Rigor de infraestructura. El sistema de control de versiones está diseñado para código, no para almacenamiento de archivos brutos o pesados. Aislar este contenido garantiza clones rápidos y evita alcanzar las cuotas de almacenamiento de las plataformas Git.

**Siguiente paso o deuda:** Definir y desarrollar la estrategia técnica para la publicación de estos contenidos visuales en el futuro (evaluar la incrustación de vídeos optimizados vs. GIFs animados simulando vídeos dentro de la documentación).

### 2026-04-27 — Feat: Auto-nombrado (Slugificación) de URLs en SSG

**Contexto:** Existía un acoplamiento rígido entre el nombre físico del archivo `.md` y la URL pública final (`.html`). Si el autor utilizaba nombres descriptivos o prefijos numéricos para organizar su entorno local, estos ensuciaban las rutas SEO de producción.

**Hecho:** Se implementó una función de `slugify` nativa en `scripts/merci/merci-publish.py` para generar los nombres de archivo de salida basándose estrictamente en el atributo `titulo` del YAML Frontmatter.

**Detalle técnico:** Se empleó la librería estándar `unicodedata` (`NFKD`) para normalizar y despojar al texto de acentos o diacríticos del español, y expresiones regulares (`re.sub`) para reemplazar espacios por guiones y eliminar caracteres inválidos para URLs.

**Motivo / criterio:** *Separation of Concerns* (Separación de Responsabilidades). Desacoplar la estructura del sistema de archivos local de la topología de URLs públicas mejora drásticamente la Developer Experience (DX). Permite reorganizar, renombrar y prefijar archivos `.md` localmente sin alterar enlaces indexados ni romper la arquitectura de la información web.

**Siguiente paso o deuda:** Desarrollar el script de copias de seguridad (Backup Local) en Python.

### 2026-04-27 — docs: Reestructuración nombres documentos a publicar

**Contexto:** Dificultad para relacionar visualmente los archivos compilados (`.html` / `.pdf`) con sus documentos origen (`.md`) en el editor debido a discrepancias o abreviaturas en los nombres físicos.

**Hecho:** Renombrar los archivos `.md` de la biblioteca para que coincidan exactamente con el título del documento, facilitando su localización a medida que el repositorio crece.

**Detalle técnico:** Modificación manual del nombre físico de los archivos directamente en el directorio local de la biblioteca.

**Motivo / criterio:** Ejecución manual justificada por el bajo volumen actual de archivos. Se asume la deuda técnica de automatizar el renombrado (slugificación) basado en el YAML Frontmatter en el futuro.

**Siguiente paso o deuda:** Estructurar la `biblioteca/` en subcarpetas temáticas (ej. `DevSecOps y Gobernanza/`) y refactorizar `merci-publish.py` para soportar lectura recursiva y auto-nombrado.

### 2026-04-27 — Feat: Clean Build automático en orquestador SSG

**Contexto:** Si un documento Markdown en la `biblioteca/` era renombrado o eliminado, el orquestador generaba la nueva versión pero los archivos `.html` y `.pdf` antiguos permanecían para siempre en `public/` como "archivos zombis". Requerir que el usuario ejecutara `rm -rf` manualmente era peligroso y propenso a errores.

**Hecho:** Se implementó el patrón de "Clean Build" (Compilación limpia) creando la función `limpiar_directorio_salida()` en `scripts/merci/merci-publish.py`.

**Detalle técnico:** Al iniciar el pipeline, el script escanea los directorios de destino (`public/biblioteca` y `public/descargas`) y ejecuta un `unlink()` estrictamente filtrado por las extensiones `.html` y `.pdf`. Esto garantiza que marcadores como `.gitkeep` u otros assets permanezcan intactos.

**Motivo / criterio:** *Zero Dead Code / DX (Developer Experience)*. El directorio de salida (public) debe ser un reflejo exacto y efímero del estado actual del directorio de origen (código fuente). Automatizar la purga antes de la compilación asegura esta paridad sin depender de comandos destructivos manuales por parte del desarrollador.

**Siguiente paso o deuda:** Crear el script Python para copias de seguridad locales (Backups) o avanzar a la Fase 9 (Inteligencia).

### 2026-04-27 — Fix: Restauración de lógica visual dinámica en SSG

**Contexto:** El orquestador de publicación estática (`merci-publish.py`) sobrescribía el diseño visual de las tarjetas forzando la clase CSS `.card--book` para todos los documentos de la Biblioteca, ignorando el atributo explícito `tipo: "cuadernillo"` definido por la autora en el YAML Frontmatter.

**Hecho:** Se refactorizó la asignación de variables de `clase_css` en `scripts/merci/merci-publish.py` tanto para la página individual como para el generador del índice.

**Detalle técnico:** Se implementó una lógica condicional en línea (Ternary Operator) que evalúa si el `tipo` es "cuadernillo" para inyectar el modificador BEM `.card--booklet`. Para cualquier otro caso, aplica degradación elegante devolviendo `.card--book`.

**Motivo / criterio:** *Single Source of Truth (SSOT)*. El motor de compilación debe respetar ciegamente las definiciones del archivo origen. Forzar clases CSS rompe la jerarquía de la información y la autoridad del Frontmatter.

**Siguiente paso o deuda:** Validar la visualización del borde naranja en los cuadernillos y continuar hacia la Fase 9 (Inteligencia) o el script de Backup Local.

### 2026-04-27 — Arquitectura: Implementación de Documentación en la Sombra (Shadow Docs)

**Contexto:** Al gobernar el Boilerplate desde este proyecto matriz, el `README.md` y las `instrucciones.md` entraban en colisión, ya que el repositorio padre y el hijo requieren documentaciones totalmente diferentes. Actualizar el clon manualmente era propenso a errores.

**Hecho:**
- Se crearon los archivos gemelos `-merci.md` (`README-merci.md`, `instrucciones-merci.md`) y `bitacora-merci-boilerplate.md` en este repositorio base.
- Se actualizó `merci-init.py` dotándolo de la capacidad de intercambiar los gemelos (borrar los personales y renombrar los agnósticos) durante el proceso de purga.

**Detalle técnico:** Se añadió el parámetro `exclude` a la función `purge_directory` para que la guillotina no arrasara con `bitacora-merci-boilerplate.md` al limpiar el laboratorio. Luego, mediante `Path.rename()`, se ascienden los archivos gemelos a su ruta oficial.

**Motivo / criterio:** *Shadow Documentation / IaC*. Almacenar la documentación del proyecto hijo "inactiva" en la matriz garantiza el control de versiones (SSOT) de todas las facetas del código. Automatizar su intercambio elimina el factor de error humano en el Release Pipeline iterativo.

**Siguiente paso o deuda:** Iniciar el desarrollo de la Fase 9 (Inteligencia y Autonomía) o el script local de Backups.

### 2026-04-27 — Docs: Definición del Release Pipeline Agile para el Boilerplate

**Contexto:** El proceso de actualizar y trasladar mejoras desde el proyecto matriz (`mercedev.es`) hacia el repositorio derivado (`merci-boilerplate`) corría el riesgo de sufrir "Configuration Drift" (Deriva de Configuración) si los bugs se parcheaban directamente en el destino.

**Hecho:**
- Se inyectó la Regla 14 en `instrucciones.md` dictando el flujo de trabajo circular estricto.
- Se redactó el cuadernillo divulgativo `cuadernillo-agile-release-pipeline.md` detallando la maniobra.

**Detalle técnico:** El flujo documentado exige que ante cualquier fallo detectado en el QA del boilerplate, se aborte el empaquetado, se corrija el código fuente en el proyecto matriz, y se reinicie el ciclo de clonación (`merci-init.py`) desde cero.

**Motivo / criterio:** Gobernanza de Repositorios y SSOT (Single Source of Truth). Aplicar metodologías *Agile* al despliegue de infraestructura garantiza que el proyecto original herede y capitalice siempre las soluciones descubiertas durante la exportación de plantillas.

**Siguiente paso o deuda:** Desarrollar el script de copias de seguridad locales (Backup) en Python.

### 2026-04-27 — Sincronización de Parches (Backport) desde Merci Boilerplate

**Contexto:** Durante el empaquetado del repositorio hijo (`merci-boilerplate`), se detectaron y solventaron deudas documentales como la falta de expansión del acrónimo JSON-LD, la omisión del entorno de desarrollo dual y la lista incompleta de herramientas en el `README.md`. Al ser `mercedev.es` la única fuente de verdad (SSOT), estos parches debían retroceder al proyecto matriz.

**Hecho:**
- Se expandió el acrónimo JSON-LD en `docs/flujo-publicacion-sop.md`.
- Se amplió el `README.md` listando el ecosistema DevSecOps completo (`merci-promote.py`, `merci-publish.py`, `merci-watcher.py`, etc.).
- Se inyectó la sección "Entorno de Desarrollo Local" al `README.md` de la matriz.

**Detalle técnico:** Modificaciones directas en los archivos Markdown para asegurar la paridad documental entre el Boilerplate generado y el motor anfitrión original.

**Motivo / criterio:** *Single Source of Truth (SSOT)*. Los errores solucionados en la plantilla derivada (fork) deben reflejarse retroactivamente en el repositorio padre (backporting) para evitar la deriva de configuración (Configuration Drift) y proteger la higiene del conocimiento de la rama principal.

**Siguiente paso o deuda:** Avanzar hacia la Fase 9 (Inteligencia y Autonomía) del asistente Merci.

### 2026-04-26 — Fix: Prevención de fuga de datos (Data Leak) en empaquetado

**Contexto:** Durante la creación de la Release 1.0.0 del Merci Boilerplate, se detectó que el clon resultante conservaba los archivos PDF generados por WeasyPrint en `public/descargas/`. Esto rompía la promesa de un "lienzo en blanco" y provocaba una fuga de datos (Data Leak) de los artículos de la autora hacia el repositorio público.

**Hecho:** Se parcheó el script destructivo `scripts/merci/merci-init.py` añadiendo la orden explícita de purgar el directorio de descargas.

**Detalle técnico:** Se incluyó la instrucción `purge_directory(REPO_ROOT / "public" / "descargas")` en el bloque de purga de datos históricos, asegurando que los artefactos binarios sean erradicados junto con el historial de Markdown y HTML.

**Motivo / criterio:** *Data Leak Prevention (Prevención de Pérdida de Datos)*. Un script que pretende empaquetar una infraestructura agnóstica debe ser exhaustivo. Dejar binarios compilados del autor original contamina el peso del repositorio de destino y expone propiedad intelectual que no forma parte del motor DevSecOps.

**Siguiente paso o deuda:** Desarrollar el script de copias de seguridad locales (Backup Local) en Python o avanzar hacia la Fase 9 (Inteligencia y Autonomía).

### 2026-04-26 — Feat: Script de instanciación del Boilerplate (Fase 10)

**Contexto:** Para convertir el repositorio en un producto reutilizable (Boilerplate Release 1.0.0), se necesitaba un mecanismo automatizado que permitiera a un usuario clonar el proyecto, limpiar todas las referencias personales (dominio, nombre) y purgar el historial documental sin tener que hacerlo archivo por archivo.

**Hecho:**
- Se creó el script destructivo `scripts/merci/merci-init.py`.
- Se implementó la purga automática de los directorios `biblioteca/`, `laboratorio/` y `public/biblioteca/`.
- Se implementó el reemplazo recursivo de la identidad (`mercedev.es`, `mercedev`, `Mercedes`) en todos los archivos de configuración y código fuente.
- Se marcó la Fase 10 como completada en el Roadmap.

**Motivo / criterio:** *Automation & Reusability*. Un boilerplate debe ser un lienzo en blanco para el nuevo desarrollador. Automatizar la inicialización cierra el ciclo de vida del proyecto, convirtiéndolo formalmente en la versión 1.0.0 lista para ser distribuida.

**Siguiente paso o deuda:** Dar por finalizado el roadmap fundacional, hacer el *push* definitivo y descansar.

### 2026-04-25 — Fix: Refuerzo de segregación de entornos (Zero Drafts in Library)

**Contexto:** Se detectó una violación de las reglas arquitectónicas: archivos con `estado: "borrador"`, tests huérfanos (`test-borrador.md`) o documentos con marcadores `TODO` pendientes estaban residiendo físicamente en el directorio fuente `biblioteca/`.

**Hecho:**
- Se ejecutó una purga manual moviendo el contenido crudo (`bitacora-merci-boilerplate.md`) de vuelta a `laboratorio/` y eliminando los archivos de test (`test-borrador.md`).
- Se eliminaron los HTML y PDF residuales generados por error en el entorno `public/`.
- Se asienta la regla estricta: El directorio `biblioteca/` en el código fuente es sagrado y solo puede alojar activos de conocimiento 100% curados y terminados.

**Motivo / criterio:** *Environment Segregation* (Segregación de Entornos). Mezclar contenido en incubación con contenido curado en el mismo directorio de origen destruye la confianza en el repositorio y genera fugas de información hacia el entorno de producción al compilar el SSG.

**Siguiente paso o deuda:** Modificar `merci-audit.py` en el futuro para que bloquee atómicamente los commits si detecta YAMLs con `estado: "borrador"` dentro de la carpeta `biblioteca/`.

### 2026-04-25 — Feat: Migración histórica y publicación del Volumen I (Fase 8.2)

**Contexto:** Tras perfeccionar el orquestador SSG (Static Site Generation - Generación de Sitios Estáticos) y el asistente de promoción, era el momento de validar el flujo completo vaciando la deuda documental del laboratorio y trasladando el historial fundacional (Volumen I) a la Biblioteca.

**Hecho:**
- Se promovió el archivo histórico a la `biblioteca/` mediante el asistente interactivo `merci-promote.py`.
- Se compiló el sitio estático y el PDF descargable con `merci-publish.py`.
- Se aprovechó para refactorizar y limpiar un evento duplicado (`DOMContentLoaded`) en `public/js/main.js` que había quedado como residuo de pruebas anteriores.

**Motivo / criterio:** *Content Lifecycle Management* (Gestión del Ciclo de Vida del Contenido). El flujo SOP (Standard Operating Procedure) diseñado demuestra su eficacia: redacción libre en laboratorio -> curación estricta con promote -> compilación automatizada con publish.

**Siguiente paso o deuda:** Marcar la Fase 8.2 como completada en el Roadmap y comenzar la investigación para dotar a Merci de capacidades avanzadas (Fase 9).

### 2026-04-25 — Fix: Control de errores (Fail Gracefully) en orquestador SSG

**Contexto:** El orquestador de publicación (`merci-publish.py`) carecía de manejo de excepciones en sus procesos críticos. Cualquier error puntual (un Markdown malformado, un fallo de WeasyPrint al enlazar imágenes o un error de permisos I/O) provocaría un colapso total del script (Fatal Error), deteniendo el pipeline e impidiendo la publicación del resto de documentos válidos.

**Hecho:**
- Se envolvieron los procesos de `markdown.markdown()`, `HTML().write_pdf()` y `.write_text()` en bloques `try-except`.
- Se implementó un retorno temprano (`return False`) con alertas por consola para saltar archivos corruptos.
- Se aplicó degradación elegante (`pass`) en caso de fallo de WeasyPrint.

**Motivo / criterio:** Principio de *Fail Gracefully* (Fallar con elegancia). Un pipeline DevSecOps maduro no se detiene por un solo elemento defectuoso. Capturar el error, reportarlo y continuar con el siguiente archivo garantiza la resiliencia de la cadena de suministro de contenido. Permitir que el HTML se publique aunque el PDF falle prioriza la disponibilidad del conocimiento por encima del formato secundario.

**Siguiente paso o deuda:** Comprometer este parche y proceder con la migración del Volumen I a la Biblioteca mediante `merci-promote` (Fase 8.2).

### 2026-04-25 — Feat: Soporte multimedia avanzado en SSG (Vídeos y PDFs)

**Contexto:** El motor SSG (`merci-publish.py`) parseaba correctamente el texto, pero el formato Markdown no soporta la etiqueta `<video>` nativamente, convirtiendo los archivos `.mp4` en etiquetas `<img>` rotas. Además, el generador de PDFs (WeasyPrint) no lograba renderizar las imágenes porque no lograba resolver las rutas estáticas (`/assets/`).

**Hecho:**
- Se implementó un pre-procesador *Regex* en Python que intercepta la sintaxis `!alt` y la transforma en un `<video>` HTML5 accesible.
- Se añadió el parámetro `base_url` a WeasyPrint apuntando a la raíz `/public`.
- Se implementó un patrón "Fallback" en SASS (`.video-fallback`) que oculta un mensaje de advertencia en la web, pero lo muestra en el PDF para indicar que hay un vídeo no imprimible.

**Motivo / criterio:** Robustez del ciclo de contenidos. Al resolver el `base_url`, los PDFs descargables ahora contendrán todas las capturas y esquemas integrados por el autor. Al usar Expresiones Regulares para el vídeo, ampliamos las capacidades de Markdown manteniendo las "0 dependencias" sin usar plugins externos que ralenticen la compilación.

**Siguiente paso o deuda:** Iniciar el ciclo de migración con la herramienta `merci-promote` (Fase 8.2) probando a publicar el primer Volumen que contendrá estos assets.

### 2026-04-25 — Feat: Enrutamiento por contexto para el cerebro de Merci (Fase 8.1)

**Contexto:** Tras integrar a Merci en todas las vistas (Fase 7.5), el asistente requería "conciencia de contexto" (saber en qué página está el usuario) para ofrecer respuestas útiles, sin sacrificar la velocidad ni requerir conexiones a una base de datos en tiempo real.

**Hecho:**
- Se refactorizó la clase `MerciController` en `public/js/MerciController.js`.
- Se implementó el método `_loadKnowledgeBase()` que lee `window.location.pathname`.
- Se añadieron diccionarios de respuestas específicos para `/biblioteca`, `/blog`, `/art-de-cote` y `/contacto`.
- Se abrió oficialmente la Fase 8 en el `README.md` y las instrucciones.

**Motivo / criterio:** *Context Routing* (Enrutamiento por Contexto) en Vanilla JS. En lugar de realizar peticiones `fetch` lentas a un backend, inyectar el conocimiento directamente en la clase y filtrarlo por la URL actual mantiene la latencia en 0 milisegundos y respeta la política de 0 dependencias externas.

**Siguiente paso o deuda:** Comprometer el código y planificar la migración de los cuadernillos antiguos a la biblioteca definitiva (Fase 8.2).

### 2026-04-25 — Feat: Implementación del asistente interactivo Merci (Fase 7.5)

**Contexto:** Era el momento de dar vida pública al asistente "Merci" en la interfaz web (Fase 7.5). El código original propuesto utilizaba bucles continuos (`setInterval`) para calcular posiciones y mover la imagen por la pantalla, lo que destrozaba el rendimiento (Layout Thrashing) y violaba las directrices de accesibilidad WAI-ARIA. Además, se requería organizar la carpeta de multimedia previendo el crecimiento futuro.

**Hecho:**
- Se reorganizó el directorio multimedia moviendo el avatar a la nueva ruta escalable `/assets/images/`.
- Se desarrolló el componente estructural BEM `_merci.scss` fijando al asistente mediante CSS.
- Se creó la clase `MerciController` en Vanilla JS (Programación Orientada a Objetos) actuando como máquina de estados.
- Se inyectó el componente HTML accesible en `public/index.html`, `public/contacto/index.html`, `src/wp-theme/merci-theme/index.php` y en el orquestador `merci-publish.py`.

**Detalle técnico:** En lugar de manipular el DOM y las coordenadas con JavaScript, el controlador interacciona estrictamente alternando atributos semánticos (`aria-hidden`, `aria-expanded`). Es el CSS el que reacciona a estos cambios de estado ARIA ejecutando transiciones suaves por GPU (`opacity`, `transform`). Esto garantiza un coste de CPU (Central Processing Unit - Unidad Central de Procesamiento) del 0% cuando el asistente está inactivo y asegura que los usuarios de teclado puedan tabular hacia él mediante el uso de un `<button>` nativo.

**Motivo / criterio:** *Rendimiento Extremo y Accesibilidad Universal*. Al anclar visualmente al asistente y delegar las animaciones al motor de hojas de estilo, erradicamos el temido Cumulative Layout Shift (CLS) y evitamos secuestrar el hilo principal (Main Thread) del navegador, manteniendo intacta nuestra puntuación de 100/100 en Core Web Vitals sin usar librerías externas de terceros.

**Siguiente paso o deuda:** Ejecutar el orquestador maestro (`merci-total`), confirmar que ninguna regla SEO ni de rendimiento ha sido penalizada, y ejecutar el commit atómico.

### 2026-04-25 — DevSecOps: Diagnóstico de fallo de suspensión (System Sleep)

**Contexto:** El entorno de desarrollo (Ubuntu) experimentó un "pantallazo gris" que forzó un reinicio abrupto tras la carga de pestañas pesadas en el navegador, sospechando inicialmente de una fuga de memoria (OOM).

**Hecho:**
- Se aisló el navegador abriéndolo mediante terminal (`google-chrome --incognito --restore-last-session=false`).
- Se auditaron los registros críticos del núcleo anterior mediante `journalctl -b -1 -p err`.

**Detalle técnico:** Los logs revelaron `Freezing user space processes failed` y `Failed to put system to sleep. System resumed again: Device or resource busy`. El colapso no fue por RAM, sino porque un proceso de usuario (posiblemente la aceleración de hardware del navegador o un hilo de Bluetooth) se negó a ceder el control al Kernel (ACPI) durante un intento de suspensión, bloqueando la interfaz gráfica.

**Motivo / criterio:** Trazabilidad estricta. Leer los logs del sistema desmiente suposiciones y revela la causa raíz de las inestabilidades. Esto valida empíricamente la necesidad de construir arquitecturas web ligeras (0 dependencias) que no saturen los manejadores de recursos (threads/GPU) del cliente.

### 2026-04-25 — Refactor: Purga de lógica de cuadernillos en SSG

**Contexto:** Tras pivotar la Arquitectura de la Información y delegar los "Cuadernillos" a WordPress (Art de Coté), el orquestador de publicación estática (`merci-publish.py`) y las plantillas conservaban código heredado y condicionales inútiles (deuda técnica).

**Hecho:**
- Se eliminaron las bifurcaciones condicionales para `.card--booklet` en `merci-publish.py`.
- Se actualizaron los textos de la página índice generada para reflejar la taxonomía de "Proyectos" y "Libros".
- Se refactorizó la plantilla base y se renombró de `plantilla-cuadernillo.md` a `plantilla-proyecto.md`.
- Se actualizó la publicación existente de alias absolutos cambiando su tipo a `bitacora`.

**Motivo / criterio:** *Zero Dead Code* (Cero Código Muerto). El código que no se usa es un lastre de mantenimiento. Si la biblioteca solo alberga proyectos y bitácoras fundacionales, el orquestador SSG debe simplificarse eliminando las comprobaciones innecesarias, cumpliendo así con la Navaja de Ockham.

**Siguiente paso o deuda:** Iniciar la Fase 7.5 subiendo el código JavaScript experimental de "Merci" al laboratorio.

### 2026-04-25 — Refactor: Pivote de Arquitectura de la Información (Libros vs Cuadernillos)

**Contexto:** Tras la reescritura de la portada (`public/index.html`) para alinearla con la realidad operativa del proyecto, se detectó que mantener dos tipos de contenido (Cuadernillos y Bitácoras/Libros) dentro de la Biblioteca estática generaba complejidad innecesaria en el mantenimiento.

**Hecho:**
- Se redefinió la taxonomía del contenido: "Proyectos / Libros" residirán exclusivamente en la **Biblioteca** (Núcleo Estático).
- "Cuadernillos / Exploraciones" residirán exclusivamente en la taxonomía **Art de Coté** (Capa Dinámica CMS/WordPress).
- Se actualizó el *copy* de la portada para reflejar esta nueva frontera arquitectónica.

**Motivo / criterio:** *Separation of Concerns* (Separación de Responsabilidades) y Arquitectura de la Información. Delegar el contenido divulgativo, efímero o exploratorio al entorno dinámico (WordPress) reduce la fricción de publicación. Reservar el motor de Generación de Sitios Estáticos (SSG) únicamente para manuales fundacionales pesados optimiza el uso de la herramienta de compilación a PDF y simplifica el pipeline a futuro.

**Siguiente paso o deuda:** (Opcional) Renombrar `docs/plantilla-cuadernillo.md` a `plantilla-proyecto.md` y limpiar la lógica heredada en `merci-publish.py` si se desea erradicar el concepto de "cuadernillo" del núcleo estático.

### 2026-04-25 — QA: Auditoría de Deuda Técnica y cierre de Fase 7.4

**Contexto:** Como parte del ciclo de mantenimiento y mejora continua (Fase 7.4), se procedió a escanear el repositorio en busca de marcadores `TODO` y deuda técnica acumulada en código o infraestructura.

**Hecho:**
- Se constató la ausencia de deuda técnica bloqueante en el código fuente (Python, SASS, JS).
- El único `TODO` restante es de carácter literario (Prólogo del Vol. I) y se encuentra correctamente aislado en el `laboratorio/`.
- Se verificó la sincronía total entre `README.md`, `instrucciones.md` y el `flujo-publicacion-sop.md`.
- Se marcó la Fase 7.4 como oficialmente completada.

**Motivo / criterio:** *Shift-Left Quality*. La ausencia de deuda técnica es el resultado directo de no haber tolerado integraciones a medias durante el desarrollo. Al solucionar la accesibilidad WAI-ARIA, los enlaces rotos y los artefactos huérfanos de forma inmediata, la fase de auditoría se convierte en una simple verificación de higiene.

**Siguiente paso o deuda:** Iniciar la Fase 7.5 (Producto Merci) para abordar la vida pública y la lógica de backend del asistente.

### 2026-04-25 — Docs: Estandarización del Runbook de Publicación (SOP)

**Contexto:** Al iniciar la Fase 7.4 y ante la proliferación de herramientas de consola creadas para el sistema Merci, la bitácora recogía un resumen escueto del orden de ejecución del pipeline, insuficiente para un proyecto de esta envergadura. Existía el riesgo de fricción cognitiva o fallos en cadena (ej. actualizar sitemap antes de compilar HTML).

**Hecho:**
- Se definió y documentó el Standard Operating Procedure (SOP) básico en el `README.md`.
- Se creó el documento de arquitectura detallado `docs/flujo-publicacion-sop.md` explicando el ciclo de vida del conocimiento.
- Se creó el documento de arquitectura detallado `docs/matriz/flujo-publicacion-sop.md` explicando el ciclo de vida del conocimiento.
- Se estableció el pipeline secuencial: `pull` -> `promote` -> `publish` -> `total` -> `commit` -> `push`.
- Se marcó el hito de mantenimiento del Roadmap como completado.

**Detalle técnico:** El nuevo documento especifica el porqué de cada paso. Por ejemplo, `merci publish` (compilación SSG) debe ejecutarse obligatoriamente *antes* que `merci total` (QA y Sitemap), ya que el escáner de enlaces (`linkcheck`) y el generador de `sitemap.xml` dependen de la existencia previa de los archivos HTML finales en la carpeta `public/` para funcionar correctamente.

**Motivo / criterio:** *Developer Experience (DX), Knowledge Management y Pipeline As Code*. Documentar el "Runbook" detallado transforma un conjunto de scripts sueltos en una verdadera cadena de montaje (CI/CD local). Delegar esta explicación profunda a un documento dedicado en `docs/` en lugar de saturar la bitácora respeta el principio de Separación de Responsabilidades Documentales.

**Siguiente paso o deuda:** Auditar la deuda técnica pendiente de las fases anteriores para dar por concluida la Fase 7.4.

### 2026-04-25 — Fix: Reubicación de borradores al entorno de incubación (Laboratorio)

**Contexto:** Tras extraer el Volumen I de la bitácora, el archivo resultante fue ubicado en la carpeta `biblioteca/` con estado `borrador` y tareas pendientes (Prólogo). Esto violaba el flujo del ciclo de vida del contenido de la Fase 7.3.

**Hecho:**
- Se reubicó físicamente el archivo `bitacora-mercedev-vol-I.md` de vuelta al `laboratorio/` mediante `git mv`.
- Se asienta la directriz de que ningún documento "en construcción" debe residir en la biblioteca.

**Motivo / criterio:** *Separación estricta de entornos (Environment Segregation).* La `biblioteca/` es un directorio exclusivo para activos de conocimiento finalizados. El `laboratorio/` es el entorno de incubación. Un borrador solo transiciona a la biblioteca en el momento exacto en que es "curado" y promovido a `publicado` mediante la herramienta `merci promote`.

**Siguiente paso o deuda:** Iniciar la Fase 7.4 (Mantenimiento y mejora continua).

### 2026-04-25 — Refactor: Arquitectura documental en 4 volúmenes (Saga mercedev)

**Contexto:** La bitácora del laboratorio crecía exponencialmente. Se requería trazar una línea divisoria clara entre la creación del motor (Fases 1-6) y las etapas posteriores, planificando el futuro de la identidad del proyecto.

**Hecho:**
- Se definió la arquitectura de conocimiento en 4 volúmenes: Vol I (Nacimiento del Boilerplate), Vol II (Construcción y automatización), Vol III (Vida oculta de Merci) y Vol IV (Vida pública de Merci).
- Se refactorizó el archivo del Volumen I en la biblioteca.
- Se purgó el historial antiguo de Fases 1 a 6 del laboratorio activo mediante un script de truncamiento.

**Motivo / criterio:** *Information Architecture* y escalabilidad cognitiva. Un documento infinito es inmanejable. Tratar el conocimiento técnico como una "Saga Literaria" encaja perfectamente con el pilar pedagógico, permitiendo que el laboratorio actual sea exclusivamente el borrador en vivo del Volumen II.

**Siguiente paso o deuda:** Iniciar la Fase 7.4 y redactar el prólogo del Volumen I cuando se considere oportuno.

### 2026-04-25 — Refactor: Establecimiento de regla pedagógica para bitácoras (Libro Presentación)

**Contexto:** Un extracto crudo del historial (Fases 1 a 6) fue promovido a producción automáticamente por un script, violando el pilar pedagógico del proyecto al presentar un volcado de logs sin narrativa introductoria.

**Hecho:**
- Se despublicó (`estado: "borrador"`) el archivo `biblioteca/bitacora-merci-boilerplate.md`.
- Se inyectó un esqueleto de "Prólogo" obligatorio.
- Se asienta la regla arquitectónica: Los datos crudos (logs) nunca se publican sin un marco de presentación didáctico.

**Motivo / criterio:** *Information Architecture* (Arquitectura de la Información) y UX Pedagógica. Un listado cronológico de commits no constituye un activo de conocimiento por sí solo si carece de contexto. Envolver el "ruido" técnico en un prólogo humano y estructurado transforma el historial en un verdadero "Libro".

**Siguiente paso o deuda:** Escribir el prólogo del Boilerplate y proceder con la planificación de la Fase 7.4.

### 2026-04-25 — Refactor: Escaneo dual y prevención de borradores zombis (merci-promote)

**Contexto:** Los documentos en `biblioteca/` que eran despublicados manualmente (pasando a `estado: "borrador"`) se convertían en "Dark Data" (datos invisibles), ya que el asistente de promoción solo escaneaba el `laboratorio/`. Esto forzaba a la edición manual del YAML para republicarlos, rompiendo el flujo.

**Hecho:**
- Se refactorizó `merci-promote.py` para realizar un escaneo dual (Laboratorio + Biblioteca).
- Se añadió el campo interactivo de `fecha` para permitir mantener la fecha original de publicación.
- Se dividió la lógica final para soportar traslados físicos (`unlink()`) y actualizaciones *in-place*.

**Motivo / criterio:** *Content Lifecycle Management* (Gestión del Ciclo de Vida del Contenido). Centralizar en una única herramienta CLI la transición de cualquier estado inmaduro o despublicado hacia la publicación definitiva elimina la fricción técnica. Pre-rellenar los inputs interactivos con los metadatos preexistentes maximiza la velocidad de republicación sin comprometer las validaciones de calidad estricta.

**Siguiente paso o deuda:** Con el ciclo de contenidos perfeccionado, abordar formalmente la planificación de la Fase 7.4 (Mantenimiento y Mejora Continua).

### 2026-04-25 — Fix: Despublicación activa de artefactos huérfanos en SSG

**Contexto:** Se detectó una fisura en el ciclo de vida del dato. Al cambiar manualmente un documento en `biblioteca/` de estado `publicado` a `borrador`, el orquestador lo saltaba y lo excluía del índice, pero los archivos HTML y PDF generados previamente quedaban huérfanos en `public/`, permaneciendo accesibles mediante su URL directa (fuga de información).

**Hecho:**
- Se refactorizó la máquina de estados en `scripts/merci/merci-publish.py`.
- Se implementó una lógica de "Despublicación Activa" (Kill-Switch).

**Detalle técnico:** Antes de abortar el procesamiento de un archivo que no sea `publicado`, el script resuelve las rutas de salida (`html_target.exists()`) y ejecuta un `unlink()` para purgar físicamente los activos del servidor si existen, emitiendo una alerta `🗑️ Despublicando` por consola.

**Motivo / criterio:** *State Synchronization* (Sincronización de Estado). El estado `borrador` no debe ser solo una omisión de compilación, sino una orden destructiva en el entorno de producción que garantice que el frontend refleje exactamente la intención actual del origen de datos, previniendo artefactos zombis.

**Siguiente paso o deuda:** Iniciar la planificación de la Fase 7.4 (Mantenimiento y mejora continua).

### 2026-04-25 — Feat: Asistente interactivo de promoción (merci-promote.py)

**Contexto:** Existía un hueco operativo (Fase 7.3) entre la redacción de un borrador en el `laboratorio/` y su publicación en la `biblioteca/`. Hacer este traslado manualmente era propenso a errores (olvidos de metadatos, fechas incorrectas o estados inconsistentes).

**Hecho:**
- Se creó el script interactivo CLI `scripts/merci/merci-promote.py`.
- Se marcaron los hitos de la Fase 7.3 como completados en el `README.md`.
- Se validó la promoción del primer borrador de prueba (`test-borrador.md`).

**Detalle técnico:** El script escanea el directorio efímero, parsea el YAML sin dependencias externas (`re` y manipulación de cadenas), solicita la curación interactiva de campos críticos (bloqueando si falta el `alt_portada` para WAI-ARIA), sella la fecha actual, cambia el `estado` a `publicado` y mueve físicamente el archivo al directorio definitivo.

**Motivo / criterio:** *Fricción Cero y Shift-Left Data Quality*. Proveer una herramienta de consola (CLI) para "curar" el documento antes de moverlo previene que archivos incompletos contaminen el entorno de producción. La interactividad actúa como un *checklist* guiado que garantiza el cumplimiento estricto de la accesibilidad y el SEO estructural.

**Siguiente paso o deuda:** Comenzar la planificación de la Fase 7.4 (Mantenimiento y mejora continua) y Fase 7.5, aprovechando que el ejecutor inteligente `merci promote` ya lo reconoce automáticamente.

### 2026-04-25 — Fix: Retrocompatibilidad YAML y validación WAI-ARIA

**Contexto:** Al implementar la máquina de estados y la validación WAI-ARIA estricta en el orquestador (`merci-publish.py`), el documento heredado `cuadernillo-alias-absolutos.md` fue bloqueado y excluido de la compilación por carecer de los campos obligatorios `estado` y `alt_portada`.

**Hecho:**
- Se parcheó manualmente `biblioteca/cuadernillo-alias-absolutos.md` inyectando `estado: "publicado"` y una descripción detallada en `alt_portada`.
- Se ejecutó `merci-publish.py`, confirmando que el orquestador compila el documento y genera el PDF correctamente.

**Motivo / criterio:** Principio "Fail-Fast" y cero tolerancia a la deuda técnica. Que el orquestador bloquee un archivo antiguo demuestra que el escudo de accesibilidad funciona empíricamente. Parchear el origen de datos (el Markdown) es la única vía permitida para integrarlo, garantizando que el HTML resultante mantenga la puntuación 100/100 en Core Web Vitals (Accesibilidad).

**Siguiente paso o deuda:** Diseñar e implementar la herramienta de promoción interactiva (`merci-promote.py`) para la Fase 7.3.

### 2026-04-25 — Feat: Máquina de estados y validación de accesibilidad en orquestador

**Contexto:** Se requería que el orquestador de publicación (`merci-publish.py`) discriminara entre borradores y documentos definitivos listos para compilar, además de blindar la accesibilidad exigiendo la presencia del atributo `alt_portada`. Paralelamente, surgió el dilema de si optimizar el motor introduciendo un sistema de caché basado en hashes de archivos.

**Hecho:**
- Se implementó una máquina de estados (Feature Toggle) basada en la clave YAML `estado` en `merci-publish.py`.
- Se introdujo una aserción estricta WAI-ARIA que bloquea el parseo si el YAML carece de `alt_portada`.
- Se descartó deliberadamente la implementación de caché por hashes.

**Detalle técnico:** El script ahora realiza retornos tempranos (`return False`) de forma silenciosa para archivos que no posean explícitamente `estado: "publicado"`. Asimismo, si el campo `alt_portada` está vacío, aborta la compilación de ese archivo lanzando un error en consola.

**Motivo / criterio:** *Premature Optimization* (Optimización Prematura). Procesar Markdown a HTML en Python es extremadamente rápido. Introducir una caché estática impediría que los artículos antiguos heredaran instantáneamente los cambios en el menú o el pie de página globales (Single Source of Truth) extraídos de la portada, provocando inconsistencia visual. Además, la aserción de la portada blinda mecánicamente la métrica de accesibilidad 100/100 de Lighthouse sin depender de la memoria del autor.

**Siguiente paso o deuda:** Desarrollar el flujo de promoción (Fase 7.3) mediante un script interactivo (`merci-promote.py`) para trasladar y estandarizar borradores desde el laboratorio hacia la biblioteca.

### 2026-04-25 — Refactor: Optimización de metadatos YAML para accesibilidad y pipeline

**Contexto:** Antes de diseñar el script de promoción de contenidos (Fase 7.3), era imperativo auditar la estructura de datos YAML para asegurar que soportara los requisitos de accesibilidad estricta (Core Web Vitals) y el control de flujo del orquestador.

**Hecho:**
- Se añadieron los campos `estado` y `alt_portada` a `docs/plantilla-cuadernillo.md`.
- Se refactorizó retroactivamente `biblioteca/auditoria-rendimiento.md` para cumplir con el nuevo esquema.

**Motivo / criterio:** *Shift-Left Data Design*. Añadir `alt_portada` garantiza desde el origen que el SSG (Static Site Generation) genere etiquetas `<img>` 100% compatibles con WAI-ARIA, evitando penalizaciones de Lighthouse. El campo `estado` (`borrador` vs `publicado`) dota al orquestador de una máquina de estados sencilla para filtrar documentos incompletos durante el proceso de compilación, protegiendo el entorno de producción.

**Siguiente paso o deuda:** Diseñar el flujo operativo y el script de Python para la promoción automatizada de contenidos (Fase 7.3).

### 2026-04-24 — Fix: Resolución de conflicto de enlace simbólico en producción

**Contexto:** Al ejecutar `git pull` en el servidor de producción (CloudPanel), Git abortó la sincronización alertando que los cambios locales en `public/blog` serían sobrescritos. Esto ocurrió porque el enlace simbólico había sido eliminado del índice del repositorio (`git rm --cached`) en una sesión anterior para aislarlo del control de versiones.

**Hecho:**
- Se eliminó temporalmente el enlace simbólico físico en el servidor de producción.
- Se ejecutó la actualización del repositorio (`git pull`) integrando el nuevo `.gitignore`.
- Se reconstruyó manualmente el enlace simbólico (`ln -s`) apuntando al directorio aislado de WordPress.

**Detalle técnico:** Comandos ejecutados secuencialmente en el servidor: `rm public/blog`, seguido de `git pull`, y finalmente `ln -s /home/mercedev-php/htdocs/wordpress /home/mercedev-php/htdocs/mercedev.es/public/blog`.

**Motivo / criterio:** Git implementa mecanismos de seguridad (Fail-Safe) para no destruir archivos locales sin seguimiento que colisionan con el árbol entrante. Destruir y recrear este puente de infraestructura tras aplicar el `.gitignore` actualizado vuelve a Git "ciego" ante el enlace, garantizando que los futuros despliegues fluyan con cero fricción.

**Siguiente paso o deuda:** Iniciar el diseño del flujo de promoción de contenidos (Fase 7.3).

### 2026-04-24 — Feat: Estandarización de plantillas de conocimiento (Fase 7.2)

**Contexto:** Para agilizar el flujo de creación de contenido y asegurar que todas las futuras publicaciones de la Biblioteca cumplan con los requisitos del orquestador (`merci-publish.py`), era necesario establecer una plantilla reutilizable.

**Hecho:**
- Se creó el archivo `docs/plantilla-cuadernillo.md`.
- Se consolidó la estructura obligatoria de metadatos (YAML Frontmatter) y la arquitectura de la información basada en 5 átomos (Contexto, Hecho, Detalle técnico, Motivo, Fuentes).

**Motivo / criterio:** Fricción Cero y Consistencia Editorial. Extraer el formato a una plantilla estática en el directorio de documentación evita que el autor dependa de la memoria o tenga que copiar archivos antiguos, garantizando que el pipeline SSG (Static Site Generation) y la inyección SEO no fallen por atributos omitidos.

**Siguiente paso o deuda:** Empaquetar el commit atómico, definir el flujo de movimiento Laboratorio -> Biblioteca (Fase 7.3) y continuar el roadmap.

### 2026-04-24 — QA: Falsos positivos de accesibilidad por extensiones del navegador

**Contexto:** Durante la auditoría manual de accesibilidad por teclado (tabulación), se detectó que el foco caía en un "agujero negro" de múltiples saltos (tabs fantasma) antes de retornar a la navegación de la web.

**Hecho:**
- Se inyectó un rastreador de eventos JS en la consola del navegador (`document.addEventListener('focusin', ...)`).
- El registro (log) reveló que el foco estaba siendo secuestrado por el elemento `<chatgpt-sidebar>`, el cual es inyectado de forma invisible por una extensión instalada en el navegador del usuario.

**Motivo / criterio:** Aislamiento del entorno de pruebas. Las extensiones del navegador inyectan Shadow DOM y elementos en el código fuente de las páginas visitadas, alterando el árbol de accesibilidad real. Las auditorías manuales (WAI-ARIA) y automáticas (Lighthouse) deben ejecutarse siempre en ventanas de Incógnito/InPrivate puras para evitar depurar "código fantasma" ajeno al proyecto.

**Siguiente paso o deuda:** Realizar el commit atómico de este aprendizaje y avanzar a la Fase 7.2.

### 2026-04-24 — Fix: Purgado de "Tabs Fantasma" y botón de salto a contenido

**Contexto:** Realizando pruebas de accesibilidad, se detectaron dos comportamientos indeseados durante la navegación por teclado: 1) el botón de accesibilidad "Saltar al contenido principal" resultaba redundante según los nuevos criterios, y 2) tras sobrepasar el footer con la tecla tabulador, el foco caía en unos 10 "tabs fantasma" antes de retornar al navegador web.

**Hecho:**
- Se eliminó completamente la etiqueta `<a href="#main" class="skip-link">` de la portada estática (`public/index.html`) y de la plantilla dinámica de WordPress (`src/wp-theme/merci-theme/index.php`).
- Se purgó el bloque CSS `.skip-link` de la arquitectura SASS (`_header.scss`) y se retiró el `tabindex="-1"` del contenedor `<main>`.
- Se añadió el filtro `add_filter('show_admin_bar', '__return_false');` en `functions.php`.
- Se ejecutó el pipeline completo de validación y compilación (`merci-total.py`).

**Motivo / criterio:** Los "tabs fantasma" en la ruta dinámica (`/blog`) eran provocados por los enlaces ocultos de la *Admin Bar* inyectada por WordPress mediante `wp_footer()` para usuarios logueados. Dado que el frontend está desacoplado (estilo Headless/Boilerplate), mantener la barra generaba conflictos de foco. Ocultarla purga estos enlaces invisibles del DOM y restaura la paridad entre las capas estática y dinámica.

**Siguiente paso o deuda:** Validar la limpieza de la navegación con tabulador sin los enlaces fantasma.

### 2026-04-24 — Fix: Refactorización arquitectónica de foco WAI-ARIA (Eliminación de tabindex en body)

**Contexto:** Se detectó que inyectar `tabindex="-1"` en la etiqueta `<body>` constituía un anti-patrón de accesibilidad. Hacer que el contenedor global del DOM fuera enfocable causaba que los lectores de pantalla reiniciaran la lectura desde el principio al activar el enlace "Volver arriba", abría vectores de "secuestro de foco" por clics inadvertidos y provocaba bugs visuales (Tap Highlight) en navegadores WebKit como iOS Safari.

**Hecho:**
- Se eliminó el atributo `tabindex="-1"` de la etiqueta `<body>` en `public/index.html`, `src/wp-theme/merci-theme/index.php` y `scripts/merci/merci-publish.py`.
- Se trasladó el identificador `id="top"` y su respectivo `tabindex="-1"` al elemento `<header>`, siendo este el primer bloque lógico y semántico de la estructura.
- Se recompilaron los activos estáticos de la biblioteca mediante `.venv/bin/python scripts/merci/merci-publish.py`.

**Motivo / criterio:** WAI-ARIA estricto y Focus Management. El foco de teclado nunca debe viajar al elemento raíz del documento (`<body>`). Al delegar la recepción del foco al `<header>`, el usuario que activa "Volver arriba" queda correctamente posicionado al inicio del contenido semántico, listo para interactuar con la navegación principal sin efectos colaterales indeseados.

**Siguiente paso o deuda:** Validar la restitución del comportamiento esperado del tabulador y proceder a empaquetar el commit atómico.

### 2026-04-24 — Fix: Resolución de foco en enlaces ancla WAI-ARIA (Tabindex)

**Contexto:** Tras implementar los enlaces de accesibilidad ("Saltar al contenido" y "Volver arriba"), se reportó que la navegación por teclado (Tabulador) seguía desfasada. Al hacer clic en los enlaces ancla, el navegador desplazaba la pantalla, pero el foco interno del teclado no viajaba al destino, obligando al usuario a tabular múltiples veces por la interfaz del navegador.

**Hecho:**
- Se inyectó el atributo `tabindex="-1"` en los contenedores destino (`<main id="main">` y `<body id="top">`) en todos los archivos estructurales (`index.html`, `merci-publish.py`, `index.php`).
- Se añadió la regla CSS `[tabindex="-1"]:focus { outline: none; }` en `_header.scss` para prevenir bordes de foco antiestéticos al activarse.
- Se aprovecharon los cambios para inyectar las anclas faltantes en la capa dinámica (`index.php`) que habían sido omitidas.

**Motivo / criterio:** Gestión estricta del foco (Focus Management). Los navegadores modernos no mueven automáticamente el cursor de tabulación a elementos semánticos (como `<main>` o `<body>`) al resolver un enlace ancla a menos que se declaren explícitamente como enfocables mediante `tabindex="-1"`. Este atributo permite recibir foco vía enlace sin alterar el orden natural de tabulación.

**Siguiente paso o deuda:** Validar la experiencia de tabulación, ejecutar un commit atómico y continuar con la Fase 7.2.

### 2026-04-24 — Fix: Resolución de conflicto de dependencias (Pillow 12 vs WeasyPrint)

**Contexto:** Al intentar instalar `weasyprint==63.0`, el gestor de paquetes `pip` arrojó un error de resolución imposible (`ResolutionImpossible`). Se diagnosticó que la versión `63.0` de WeasyPrint limitaba estrictamente su compatibilidad a `Pillow < 11`, colisionando frontalmente con `Pillow==12.2.0` (actualizado recientemente por motivos de seguridad).

**Hecho:**
- Se actualizó el anclaje en `requirements.txt` de `weasyprint==63.0` a la versión moderna `weasyprint==68.1`.

**Motivo / criterio:** Supply Chain Security. En ecosistemas DevSecOps, retroceder una librería base (Pillow) a una versión antigua con vulnerabilidades conocidas (CVE) para satisfacer a una herramienta de exportación secundaria es un antipatrón inaceptable. La solución arquitectónica correcta es avanzar la herramienta secundaria (WeasyPrint) hasta la versión (`68.1`) que dé soporte oficial a la librería parcheada.

**Siguiente paso o deuda:** Ejecutar la instalación de dependencias, validar la generación del PDF y dar por concluida la Fase 7.1.

### 2026-04-24 — Fix: Resolución de incompatibilidad de WeasyPrint (Supply Chain)

**Contexto:** Durante la generación del PDF en el orquestador de publicación (`merci-publish.py`), la ejecución colapsó con el error `AttributeError: 'super' object has no attribute 'transform'`. El diagnóstico reveló una incompatibilidad entre la versión anclada `weasyprint==62.1` y la actualización reciente de una de sus subdependencias internas (`pydyf`) en entornos con Python 3.12.

**Hecho:**
- Se actualizó la dependencia en `requirements.txt` de `weasyprint==62.1` a `weasyprint==63.0`.

**Motivo / criterio:** Mantenimiento de la cadena de suministro de software (Supply Chain). En DevSecOps, cuando una subdependencia transitiva rompe la librería principal, la maniobra correcta es dar el salto a la siguiente *release* estable del paquete anfitrión que haya mitigado la incompatibilidad, en lugar de intentar parchear el código fuente o degradar módulos individuales.

**Siguiente paso o deuda:** Re-instalar dependencias, validar la generación exitosa de los PDFs y dar por cerrada la funcionalidad.

### 2026-04-24 — Feat: Generación automatizada de artefactos PDF (WeasyPrint)

**Contexto:** Se requería dotar a la Biblioteca de la capacidad de generar y ofrecer versiones descargables en PDF de cada artículo para facilitar el consumo offline, la preservación del conocimiento y el formato de "libro/cuadernillo".

**Hecho:**
- Se integró la librería `weasyprint` en el pipeline de publicación.
- Se actualizó `merci-publish.py` para compilar un diseño específico de impresión (con portada generada dinámicamente usando metadatos YAML y saltos de página).
- Se inyectó un botón de descarga (`.card__download`) en las páginas HTML generadas apuntando a la nueva ruta `public/descargas/`.

**Motivo / criterio:** SSG Avanzado y Cero Fricción. Generar el PDF en el mismo instante de la compilación asegura que la versión web y la descargable jamás estén desincronizadas. Se utilizó WeasyPrint por ser el estándar más robusto y moderno en Python para interpretar HTML/CSS hacia PDF nativo sin depender de binarios de navegadores pesados.

**Siguiente paso o deuda:** Validar la visualización del PDF, actualizar la portada con los últimos artículos (si aplica) y dar por cerrada la Fase 7.1.

### 2026-04-24 — Refactor: Paridad WAI-ARIA en WP y corrección arquitectónica SASS 7-1

**Contexto:** Tras implementar el patrón de accesibilidad (skip-link y anclas de retorno) en el núcleo estático, la capa dinámica (WordPress) quedó desincronizada. Además, se detectó que los estilos del bloque principal (`.header`) debían ubicarse estrictamente según el patrón SASS 7-1.

**Hecho:**
- Se ubicó la regla `.skip-link` y los estilos de cabecera en `src/scss/layout/_header.scss` (reafirmando la arquitectura 7-1).
- Se inyectaron los identificadores `#top`, `#main` y el enlace de retroceso (`↑ Volver arriba`) en `src/wp-theme/merci-theme/index.php`.

**Motivo / criterio:** Paridad Dev-Prod y Arquitectura Estricta. En SASS 7-1, los contenedores estructurales (`header`, `footer`) pertenecen al directorio `layout/`, reservando `components/` para widgets reusables (`cards`, `buttons`). Mantener la accesibilidad sincronizada entre Nginx y PHP garantiza una experiencia unificada.

**Siguiente paso o deuda:** Validar la capa dinámica, empaquetar el commit atómico y comenzar la generación de artefactos PDF (Fase 7.1).

### 2026-04-24 — Feat: Patrones de accesibilidad WAI-ARIA (Skip-link y Volver arriba)

**Contexto:** Al auditar la navegación por teclado (Tab), se detectó que tras interactuar con la última publicación (segunda entrada), el foco escapaba a la interfaz del navegador, requiriendo unas 10 pulsaciones para dar la vuelta y reingresar a la web. Además, se forzaba al usuario a tabular por todo el menú principal en cada carga de página.

**Hecho:**
- Se inyectó un enlace oculto `.skip-link` (`Saltar al contenido principal`) al inicio del `<header>`, que se hace visible al recibir el foco.
- Se implementó un enlace de ancla (`↑ Volver arriba`) en el footer.
- Se actualizaron las etiquetas `<body>` y `<main>` en `public/index.html` y `merci-publish.py` añadiendo los anclajes de ID (`#top`, `#main`).

**Motivo / criterio:** WAI-ARIA y Experiencia de Usuario (UX) inclusiva. Un usuario de teclado no debe caer en un "bucle ciego" al llegar al final de la página, ni verse obligado a recorrer menús repetitivos para leer el contenido.

**Siguiente paso o deuda:** Compilar, verificar el funcionamiento con el tabulador, empaquetar el commit atómico y proceder con los PDFs.

### 2026-04-24 — Feat: Enlace de retroceso (UX) en publicaciones individuales

**Contexto:** Las páginas individuales generadas por `merci-publish.py` carecían de un método rápido y contextual para regresar al índice temático de la Biblioteca, obligando al usuario a usar el botón "Atrás" del navegador o buscar en el menú principal.

**Hecho:**
- Se añadió la clase BEM `.card__back-link` en `src/scss/components/_card.scss`.
- Se actualizó el orquestador `scripts/merci/merci-publish.py` para inyectar dinámicamente este enlace (`← Volver a la Biblioteca`) en la cabecera de cada artículo renderizado.

**Motivo / criterio:** Experiencia de Usuario (UX) y navegabilidad. Proveer enlaces de retroceso contextuales reduce la fricción cognitiva, retiene al usuario en el flujo de la aplicación y fomenta la exploración de otras estanterías temáticas.

**Siguiente paso o deuda:** Empaquetar el commit atómico y proceder con la investigación para la generación de los PDFs.

### 2026-04-24 — Fix: Resolución de advertencia SEO (JSON-LD) en el índice de la Biblioteca

**Contexto:** El orquestador local (`merci-total`) reportó una advertencia (`WARN SEO_JSONLD`) indicando que el índice principal de la Biblioteca carecía de datos estructurados, lo cual penaliza el SEO técnico y rompe el estándar de la Fase 2.

**Hecho:**
- Se actualizó la función `generar_indice_biblioteca()` en `scripts/merci/merci-publish.py`.
- Se inyectó dinámicamente un bloque `<script type="application/ld+json">` utilizando el esquema `@type: CollectionPage`.

**Motivo / criterio:** Al migrar la página principal de la Biblioteca a un modelo auto-generado (SSG - Static Site Generation), el archivo HTML perdió sus metadatos estáticos originales. Reintegrar la generación del JSON-LD en el orquestador asegura el cumplimiento de la política estricta de SEO y silencia la advertencia del linter local de manera definitiva.

**Siguiente paso o deuda:** Empaquetar el commit atómico y proceder con la investigación para la generación de los PDFs.

### 2026-04-24 — Feat: Patrón "Stretched Link" en tarjetas de Biblioteca

**Contexto:** En el índice autogenerado de la Biblioteca, solo el texto del título era interactivo. Se requería que toda la superficie de la tarjeta (`.card`) fuera clicable para mejorar la experiencia de usuario (UX) sin ensuciar la semántica HTML5.

**Hecho:**
- Se añadió `position: relative;` al bloque base `.card` en `src/scss/components/_card.scss`.
- Se implementó el pseudoelemento `::after` con `inset: 0;` en el enlace del título (`.card__title a`).
- Se vinculó el cambio de color (`:hover`) del título al estado hover de la tarjeta completa.

**Motivo / criterio:** Semántica y Accesibilidad. Envolver bloques enteros (`<article>`, `<header>`, `<p>`) dentro de una etiqueta `<a>` es válido en HTML5, pero entorpece a los lectores de pantalla. El patrón *Stretched Link* (Enlace Estirado) expande el área clicable del título principal mediante CSS para cubrir su contenedor, manteniendo un DOM limpio, ligero y 100% accesible.

**Siguiente paso o deuda:** Empaquetar el commit atómico y proceder a la investigación para la generación de los PDFs.

### 2026-04-24 — Refactor: Reestructuración temática del índice de Biblioteca (Estanterías)

**Contexto:** La generación del sitio estático para la Biblioteca (`merci-publish.py`) organizaba el contenido cronológicamente (como un blog). Esto violaba la filosofía fundacional de la "Biblioteca", que define el contenido como conocimiento inmutable ordenado por "estanterías" temáticas, delegando la presentación cronológica a la capa dinámica de WordPress (`/blog`).

**Hecho:**
- Se añadió el campo `tema` en el bloque de metadatos YAML de todas las publicaciones de la biblioteca.
- Se refactorizó la función `generar_indice_biblioteca()` en `merci-publish.py` para agrupar los artículos por tema (diccionarios) y renderizarlos en secciones separadas (`<section>`).

**Motivo / criterio:** Arquitectura de la Información y Gestión del Conocimiento. Separar la estructura mental del usuario. El Blog es un flujo temporal (novedades, anuncios); la Biblioteca es un índice de consulta directa agrupado semánticamente (Arquitectura, DevSecOps, SASS).

**Siguiente paso o deuda:** Empaquetar el cambio en un commit atómico y proceder a la investigación para la generación de los PDFs.

### 2026-04-24 — Feat: Auto-generación del índice de la Biblioteca (SSG)

**Contexto:** Se generaban las publicaciones individuales en HTML, pero la página principal de la Biblioteca (`public/biblioteca/index.html`) no existía o no enlazaba dinámicamente el nuevo contenido, obligando a añadir los enlaces manualmente.

**Hecho:**
- Se refactorizó `scripts/merci/merci-publish.py` para recolectar los metadatos de las publicaciones procesadas.
- Se implementó la función `generar_indice_biblioteca()` para compilar automáticamente el `index.html` con una cuadrícula de tarjetas ordenadas por fecha descendente.

**Motivo / criterio:** Fricción Cero y SSG (Static Site Generation - Generación de Sitios Estáticos). Automatizar la creación del índice elimina la necesidad de editar HTML manualmente, protegiendo el diseño y evitando el error humano de publicar un artículo y olvidar enlazarlo.

**Siguiente paso o deuda:** Empaquetar el commit atómico y proceder a la investigación sobre generación de PDFs.

### 2026-04-24 — Fix: Resolución de auditoría SEO en orquestador de publicación

**Contexto:** El orquestador maestro (`merci-total`) abortó el pipeline al detectar que las páginas HTML generadas por `merci-publish.py` carecían de etiquetas SEO obligatorias (meta descripción, URL canónica y JSON-LD), lo cual habría provocado penalizaciones en buscadores.

**Hecho:**
- Se añadió el atributo `descripcion` en el YAML Frontmatter de los archivos Markdown de la biblioteca.
- Se actualizó `scripts/merci/merci-publish.py` para leer dicha descripción y generar dinámicamente las etiquetas `<meta>`, `<link rel="canonical">` y el bloque `<script type="application/ld+json">`.
- Se superó exitosamente la auditoría estricta de `merci-audit.py` logrando 0 errores y 0 advertencias.

**Detalle técnico:** La inyección de metadatos se realiza directamente en el orquestador de Python usando *f-strings*. El esquema de datos estructurados (JSON-LD) se configura con el `@type` `Article`, nutriéndose de los mismos metadatos del YAML para evitar que el desarrollador introduzca información redundante de forma manual.

**Motivo / criterio:** Shift-Left SEO y validación cruzada. El pipeline ha demostrado su valor al actuar como barrera protectora estricta. Solventar este error a nivel de orquestador asegura automáticamente las mejores prácticas de SEO para cualquier futuro artículo publicado.

**Siguiente paso o deuda:** Empaquetar el commit atómico y proceder a la fase de generación automática de artefactos descargables (PDF).

### 2026-04-24 — Fix: Retrocompatibilidad YAML y refinamiento tipográfico SASS

**Contexto:** Durante la ejecución del orquestador de publicación (`merci-publish`), el archivo `auditoria-rendimiento.md` (heredado de la Fase 6) fue bloqueado por carecer de metadatos YAML. Además, el HTML generado a partir de Markdown presentaba una densidad visual alta, requiriendo mayor espaciado entre capítulos para mejorar la legibilidad.

**Hecho:**
- Se inyectó el bloque estandarizado YAML Frontmatter en `auditoria-rendimiento.md`.
- Se añadieron reglas de espaciado (`margin-top`, `margin-bottom`) específicas para encabezados (`h2`, `h3`) y párrafos generados dinámicamente dentro de `.card__content` en la arquitectura SASS.
- Se validó la generación e integración exitosa de ambas publicaciones en el núcleo estático.

**Motivo / criterio:** La política de "Fail-Fast" del orquestador protege el entorno de producción al rechazar archivos malformados, obligando a actualizar la deuda técnica documental. La encapsulación de estilos de Markdown dentro de `.card__content` mantiene el SASS global limpio (Separation of Concerns).

**Siguiente paso o deuda:** Empaquetar el commit atómico e investigar la generación automatizada de artefactos PDF para la biblioteca.

### 2026-04-24 — Feat: Orquestador de publicación estática y abstracción de UI

**Contexto:** Se necesitaba un sistema para transformar los documentos Markdown curados de la biblioteca en páginas HTML estáticas, pero sin duplicar el código del menú (header) y el pie de página (footer) de la web. Además, el script reportó un fallo al intentar procesar archivos heredados (`auditoria-rendimiento.md`) que carecían de metadatos.

**Hecho:**
- Se creó `scripts/merci/merci-publish.py` para parsear Markdown con YAML Frontmatter.
- Se implementó un sistema de extracción dinámica mediante expresiones regulares que lee `public/index.html` para recortar y reutilizar las etiquetas `<header>` y `<footer>`.
- Se validó el "fail-fast" del script frente a archivos sin YAML válido.

**Motivo / criterio:** Single Source of Truth (Única Fuente de Verdad). En lugar de crear motores de plantillas complejos, el script extrae los componentes globales directamente del HTML compilado de la portada. Esto garantiza que cualquier cambio futuro en el menú de la web se propague automáticamente a las publicaciones sin tocar Python. El rechazo de archivos antiguos sin YAML protege el entorno de producción de documentos malformados.

### 2026-04-24 — Docs: Refactorización a MVP de cuadernillo con YAML Frontmatter

**Contexto:** El borrador sobre el problema de los alias y el autodescubrimiento en Python contenía volcados de consola sin procesar. Se requería estructurarlo como un "Producto Mínimo Viable" (MVP) para la biblioteca y añadir el descubrimiento sobre la retención de alias fantasma en la memoria RAM de la terminal.

**Hecho:**
- Se refactorizó `biblioteca/cuadernillo-alias-absolutos.md` eliminando el historial de consola residual.
- Se inyectaron metadatos estructurales (YAML Frontmatter) y se consolidó el contenido bajo el formato de 5 átomos (Contexto, Hecho, Detalle técnico, Motivo, Fuentes).
- Se añadió la nota de depuración sobre purga de RAM mediante `unalias`.

**Motivo / criterio:** Estandarización de la información. Para que el futuro orquestador de publicación (Fase 7.1) automatice la maquetación a HTML/PDF sin fricción, los archivos Markdown deben poseer una estructura de metadatos estricta y predecible.

**Siguiente paso o deuda:** Diseñar e implementar el script maestro de publicación automatizada (`merci-publish.py`).

### 2026-04-24 — Fix: Exclusión de enlace simbólico del CMS en control de versiones

**Contexto:** El enlace simbólico `public/blog` (que conecta el núcleo estático con la instalación aislada de WordPress) corría el riesgo de ser rastreado por Git. Versionar un enlace simbólico que apunta a una ruta absoluta del sistema anfitrión rompe la portabilidad del proyecto al clonarlo en entornos con topologías diferentes.

**Hecho:**
- Se añadió `public/blog` al archivo `.gitignore`.
- Se definió la ejecución de `git rm --cached public/blog` para eliminar el rastro del índice de Git sin destruir el enlace físico en el servidor local.

**Motivo / criterio:** Portabilidad y aislamiento (Shift-Left). El código fuente debe ser universal y agnóstico a la infraestructura. Los enlaces simbólicos son configuraciones exclusivas del servidor (estado) y, al igual que la base de datos o el archivo `wp-config.php`, nunca deben viajar a través del control de versiones.

**Siguiente paso o deuda:** Ejecutar la limpieza del caché de Git, revisar el estado del árbol y realizar el commit de saneamiento mediante `merci-commit.py`.

### 2026-04-24 — Milestone: Bifurcación arquitectónica (Merci Boilerplate vs mercedev.es)

**Contexto:** Tras alcanzar la madurez técnica absoluta (100/100) y purgar la deuda técnica al cierre de la Fase 6, se determinó que las Fases 1-6 conforman un motor de infraestructura agnóstico (DevSecOps, SASS, CSP, Híbrido WP), mientras que la Fase 7 (publicación automatizada, biblioteca) contiene la lógica de negocio específica del proyecto.

**Hecho:**
- Se aprueba la bifurcación (Fork) del proyecto actual en dos entidades separadas.
- Se decide extraer el estado actual del código hacia un nuevo repositorio plantilla (`merci-boilerplate`) abstrayendo los datos personales.
- El repositorio actual (`PROYECTO_mercedev.es`) transiciona oficialmente para convertirse en el primer producto real derivado de dicha plantilla.

**Detalle técnico:** La extracción al nuevo Boilerplate implicará limpiar el `index.html` de textos específicos, establecer un logotipo neutral y sustituir las rutas absolutas por variables (`{{DOMINIO}}`). El repositorio actual mantendrá el historial completo de Git y avanzará hacia la Fase 7 asumiendo su rol de "instancia cliente".

**Motivo / criterio:** Principio de Separación de Responsabilidades (Separation of Concerns). Un *boilerplate* o *framework* no debe contener reglas de negocio ni contenido específico de una marca. Congelar el motor base ahora protege su reusabilidad para futuros proyectos, aislando el desarrollo de la Fase 7 exclusivamente en el producto final.

**Siguiente paso o deuda:** Ejecutar manualmente la copia y abstracción de la carpeta hacia el nuevo repositorio "Merci Boilerplate" e iniciar el diseño de la Fase 7 en el repositorio actual.

### 2026-04-24 — Refactor: Micro-optimización de SEO Técnico (JSON-LD Contextual)

**Contexto:** Una auditoría SEO de "hilado fino" detectó que el esquema JSON-LD inyectado dinámicamente marcaba todas las rutas de WordPress como `@type: WebSite` y usaba `home_url()` (que resuelve a `/blog`), lo cual generaba riesgo de fragmentación de la autoridad de dominio en los motores de búsqueda.

**Hecho:**
- Se refactorizó la matriz `$json_ld` dentro de la función `merci_inyectar_metadatos_seo` en `functions.php`.
- Se implementó condicionalidad semántica (`is_singular()`) para emitir `@type: Article` en páginas de lectura.
- Se forzó el uso de la raíz absoluta del dominio para el esquema `WebSite`.

**Detalle técnico:** Se extrajo la variable `$domain_root` usando la misma expresión regular (`preg_replace`) que en el enlazador de assets. Dependiendo del contexto de la vista, el JSON-LD ahora escupe los datos específicos del post actual (`get_permalink()`, `get_the_title()`) o los datos base del índice, cumpliendo con la especificación estricta de `schema.org`.

**Motivo / criterio:** Consultoría SEO Avanzada. Evitar la canibalización de entidades (que Google interprete `/blog` como un sitio web independiente a la portada). Etiquetar correctamente los posts como "Artículos" habilita la aparición en fragmentos enriquecidos (Rich Snippets).

**Siguiente paso o deuda:** Iniciar el diseño del flujo de la Fase 7.1 (Automatización de publicación).

### 2026-04-24 — Refactor: Auditoría arquitectónica externa y purga de deuda técnica

**Contexto:** Una auditoría externa de código mediante inteligencia artificial detectó cuatro deudas técnicas críticas en el ecosistema: un antipatrón de rendimiento en WordPress, uso de código heredado (legacy), inconsistencia SEO entre frontales y la violación del paradigma de programación orientada a objetos en JavaScript.

**Hecho:**
- Se modificó el hook de aprovisionamiento de base de datos de `init` a `after_switch_theme` en `functions.php`.
- Se eliminó la etiqueta `<title>` deprecada explícita en `index.php` y se activó `add_theme_support('title-tag')`.
- Se inyectó un bloque mínimo de metadatos estructurados (JSON-LD) en el ecosistema dinámico de WordPress.
- Se refactorizó `public/js/main.js` encapsulando la lógica procedimental en la clase `NavigationController`.

**Detalle técnico:** El hook `init` provocaba consultas inútiles a la base de datos en cada petición HTTP (N+1 query problem). La función `wp_title()` está deprecada desde WP 4.4; delegar el título al núcleo limpia el archivo HTML y cumple el estándar moderno. La refactorización a Vanilla JS con paradigma POO (Programación Orientada a Objetos) aísla el comportamiento del menú cumpliendo el Principio de Responsabilidad Única (SOLID).

**Motivo / criterio:** Prácticas estrictas de *Quality Assurance* (QA - Aseguramiento de Calidad) y validación cruzada. El código no solo debe funcionar, sino que debe alinearse perfectamente con la filosofía fundacional del proyecto (rendimiento, arquitectura y cero deuda técnica), sin admitir tolerancias al código "suficientemente bueno".

**Siguiente paso o deuda:** Ejecutar el orquestador de validación y comprometer el código para iniciar la Fase 7.1 (Automatización de publicación).

### 2026-04-23 — Fix: Actualización mayor de Pillow a 12.2.0 (Dependabot)

**Contexto:** Dependabot emitió nuevas alertas y forzó la actualización de su rama (pull request) indicando la necesidad de dar un salto mayor en la versión de `Pillow` hasta la `12.2.0` para mitigar vulnerabilidades encadenadas.

**Hecho:**
- Se actualizó la dependencia en `requirements.txt` de `Pillow==10.4.0` a `Pillow==12.2.0`.

**Detalle técnico:** El salto a una versión mayor (de 10.x a 12.x) incluye importantes parches de seguridad. Dado que `merci-optimizer.py` solo utiliza funciones estándar y consolidadas de apertura, redimensionado y guardado en WebP, la actualización se considera segura y no introduce alteraciones lógicas (*breaking changes*) en la automatización del proyecto.

**Motivo / criterio:** Mantenimiento proactivo y "Zero Trust". Las alertas de seguridad se persiguen hasta su erradicación total. Dar el salto a la última versión estable recomendada por GitHub blinda el entorno local y silencia el ruido operativo en el repositorio.

**Siguiente paso o deuda:** Realizar el push para cerrar definitivamente los hilos de Dependabot e iniciar el diseño del flujo de la Fase 7.

### 2026-04-23 — Fix: Actualización crítica de Pillow a 10.4.0 (Dependabot)

**Contexto:** Tras el último `git push`, GitHub Dependabot reportó dos nuevas vulnerabilidades de severidad alta. Dado que `requirements.txt` solo contiene la dependencia `Pillow`, se deduce que la versión 10.3.0 seguía expuesta a CVEs recientes.

**Hecho:**
- Se actualizó la dependencia en `requirements.txt` de `Pillow==10.3.0` a `Pillow==10.4.0`.
- Se revisó la integridad y sincronización de toda la documentación del directorio `docs/` y el `README.md` confirmando el cierre inmaculado de la Fase 6.

**Detalle técnico:** Las vulnerabilidades descubiertas en procesamiento de imágenes en las versiones anteriores a la 10.4.0 de Pillow pueden permitir ataques o denegación de servicio. Fijar la versión a `10.4.0` parchea estos vectores. La documentación arquitectónica (`docs/`) ha sido validada y refleja el estado exacto de producción (incluyendo el hash CSP y el enrutamiento).

**Motivo / criterio:** La seguridad perimetral no es negociable. En DevSecOps, mantener las dependencias de Python actualizadas es obligatorio, incluso si el script que las usa (`merci-optimizer.py`) se ejecuta únicamente en el entorno local.

**Siguiente paso o deuda:** Desplegar el cambio y comenzar el diseño del script de publicación automatizada (Fase 7.1).

### 2026-04-23 — Fix: Resolución de vulnerabilidad (Dependabot) y sincronización documental

**Contexto:** Al realizar el `git push` de cierre de la Fase 6, GitHub Dependabot reportó una vulnerabilidad de severidad alta (CVE) en las dependencias del proyecto. Además, era necesario alinear los manuales de despliegue (`docs/`) con las últimas configuraciones de seguridad en Nginx (CSP, HSTS) antes de avanzar a la Fase 7.

**Hecho:**
- Se identificó que la librería `Pillow` anclada en `requirements.txt` poseía una vulnerabilidad conocida, por lo que se actualizó a la versión segura `10.3.0`.
- Se actualizaron los manuales `docs/deployment-playbook.md` y `docs/integracion-wordpress.md` para incluir el bloque de Hardening de cabeceras HTTP inyectado en CloudPanel.

**Detalle técnico:** En arquitecturas DevSecOps, las dependencias de Python (utilizadas por `merci-optimizer.py`) deben ser auditadas continuamente. Actualizar la versión estricta en `requirements.txt` soluciona la alerta de GitHub manteniendo la reproducibilidad. Por otro lado, la documentación arquitectónica se sincronizó para reflejar la inyección de la cabecera `Content-Security-Policy` con el *whitelist* criptográfico (Hash SHA-256) y el `preload` de HSTS en el VHost del puerto 8080.

**Motivo / criterio:** Tolerancia cero frente a deuda técnica y brechas de seguridad. Una vulnerabilidad "High", aunque afecte solo al entorno local de automatización, rompe la confianza en el repositorio. Mantener la documentación sincronizada con la realidad del servidor garantiza la reproducibilidad (Infrastructure as Code).

**Siguiente paso o deuda:** Iniciar la Fase 7: Automatización y Clasificación.

---

## Cuando pases esto a la biblioteca

1. **Releer** entradas y quitar ruido (intentos fallidos, datos personales, tokens aunque sean falsos).
2. **Partir por tema:** por ejemplo una ficha “Sistema Merci — auditoría pre-commit” vs “Estructura del repositorio”.
3. **Añadir los tres átomos** donde haya una decisión difícil o un incidente (síntoma, solución, lección o deuda).
4. **Enlazar** al código estable (rutas a `scripts/merci/`, no copiar bloques enormes en la biblioteca salvo que aporten lectura autónoma).

---

*Última revisión de la bitácora: 2026-05-02.*
