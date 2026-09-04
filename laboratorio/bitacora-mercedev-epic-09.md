# Bitácora del proyecto mercedev.es — Épica 9: Antigravity SRE, Chaos Engineering & Refinamiento CSS

## Para qué sirve este archivo

- **Yo futuro:** recuperar en minutos qué se decidió, por qué, y cómo se ejecutó algo técnico sin rebuscar en el chat o en commits sueltos.
- **Biblioteca (al cerrar el proyecto):** aquí vive el borrador narrativo y técnico; luego se depura y se traslada a `biblioteca/` como piezas definitivas (por estantería o tema), siguiendo la idea de “activo de conocimiento” del proyecto.

No sustituye a `instrucciones.md` (directrices y rol del asistente). Complementa el día a día con **hechos, comandos y lecciones**.

---

## Cómo mantenerlo (acuerdo simple)

1. **Añadir entradas al principio** de la sección “Registro cronológico”, con la plantilla de abajo. El registro es **acumulativo**: lo ya escrito forma parte del historial y **no se reemplaza** por nuevas sesiones (así no se pierde contexto ni fechas).
2. **Una entrada por sesión o por tema cerrado** (lo que resulte más claro al escribir).
3. Si algo fue un error o una vulnerabilidad evitada, opcionalmente usar los **tres átomos** del proyecto (Desafío → Maniobra → Aprendizaje/Deuda) en el cuerpo de la entrada.
4. **Convención de Rutas:** Al hacer referencia a archivos o directorios, usar rutas relativas a la raíz del proyecto, comenzando con `PROYECTO_mercedev.es/` (ej. `PROYECTO_mercedev.es/laboratorio/archivo.md`). No incluir el prefijo absoluto del sistema operativo (ej. `/home/tu_usuario/ruta_al_proyecto/`).
5. **Correcciones excepcionales** (typo, dato incorrecto, redacción de un solo párrafo, retirada de información sensible): editar solo el fragmento necesario o añadir una línea aclaratoria bajo la entrada; evitar reescribir todo el archivo o borrar entradas enteras sin motivo documentado.

### Plantilla para nuevas entradas

Plantilla base para el registro de sesiones.

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

### 2026-07-03 — Ajuste de Tamaño de Contexto y Unificación de Agentes Locales en LiteLLM

**Contexto:**
Se detectó un fallo crítico de procesamiento en el servidor local de LM Studio (`OpenAIException - Error code: 400 - Context size has been exceeded`). Esto ocurría porque los límites de tokens de salida de los agentes (`max_tokens=3000` y `max_tokens=4000` en `merci-blogger.py` y `merci-librarian.py` respectivamente) sumados a los tokens del prompt de entrada superaban la ventana de contexto de 4096 tokens configurada por defecto en el modelo cargado en local (`qwen/qwen3.5-9b`). Asimismo, `merci-librarian.py` seguía llamando de forma directa a un modelo de Gemini no tipado en lugar del alias unificado `ide-agent` del proxy.

**Hecho:**
- Se redujo el parámetro `max_tokens` a un valor conservador de `1500` en `PROYECTO_mercedev.es/scripts/merci/merci-blogger.py` y `PROYECTO_mercedev.es/scripts/merci/merci-librarian.py` para asegurar compatibilidad total con la ventana de contexto de modelos locales.
- Se refactorizó `merci-librarian.py` para consumir la petición de IA a través del alias `openai/ide-agent` expuesto en el proxy (puerto 4000).
- Se comprobó mediante `merci-total.py` que la compilación y QA finalizan con éxito en verde.

**Detalle técnico:**
- Archivo modificado: `PROYECTO_mercedev.es/scripts/merci/merci-blogger.py` (Línea 145).
- Archivo modificado: `PROYECTO_mercedev.es/scripts/merci/merci-librarian.py` (Línea 49 y 57).
- Comandos ejecutados: `python3 scripts/merci/merci-total.py` y `python3 scripts/merci/merci-audit.py`.

**Motivo / criterio:**
Garantizar la estabilidad y consistencia de la pila local de IA. Acotar el tamaño máximo de respuesta a 1500 tokens previene desbordamientos de memoria en el servidor local de inferencia sin menoscabar la calidad del texto técnico o de marketing autogenerado.

**Siguiente paso o deuda:**
- Siguiente paso: Confirmar los cambios pendientes en el control de versiones local.

---

### 2026-07-03 — Prefijado de Modelos del Proxy para Evasión de Errores del SDK de LiteLLM

**Contexto:**
Se identificó un fallo de comunicación del lado del cliente en `merci-brain.py` y `merci-blogger.py`. Aunque los puertos locales de LiteLLM (4000) y LM Studio (1234) estaban encendidos y escuchando en la terminal, las llamadas SDK fallaban inmediatamente antes de transmitirse debido a la validación estricta del cliente de LiteLLM, que requiere un prefijo de proveedor conocido (ej. `openai/`) para omitir la inferencia estática de modelos desconocidos (`local-agent` e `ide-agent`). Además, se diagnosticó que el servidor local de LM Studio no tiene ningún modelo cargado en memoria RAM en la sesión actual de la terminal.

**Hecho:**
- Se modificaron `PROYECTO_mercedev.es/scripts/merci/merci-brain.py` y `PROYECTO_mercedev.es/scripts/merci/merci-blogger.py` para prefijar los nombres de modelo en las llamadas de finalización como `openai/local-agent` y `openai/ide-agent` respectivamente.
- Se comprobó mediante un script de depuración que la llamada de red ahora atraviesa exitosamente el SDK cliente y se enruta de forma correcta hacia el puerto 4000 del proxy.
- Se verificó que el pipeline general de compilación estática y auditoría finaliza con éxito en verde.

**Detalle técnico:**
- Archivo modificado: `PROYECTO_mercedev.es/scripts/merci/merci-brain.py` (Línea 58).
- Archivo modificado: `PROYECTO_mercedev.es/scripts/merci/merci-blogger.py` (Línea 137).
- Script efímero creado para pruebas: `/home/hildegahr/.gemini/antigravity-ide/brain/d6d9933e-122a-4840-8d6c-20b5fc4426ed/scratch/test_local_agent.py`.
- Comandos ejecutados: `ss -tuln`, `lms ps` y `python3 scripts/merci/merci-total.py`.

**Motivo / criterio:**
Asegurar que los agentes de software se comuniquen correctamente con la pasarela de enrutamiento unificado de la suite de desarrollo, respetando el estándar API de LiteLLM y garantizando el flujo híbrido de resiliencia.

**Siguiente paso o deuda:**
- Siguiente paso: Si se desea habilitar la contingencia local, el operador debe cargar un modelo en la RAM de LM Studio ejecutando `lms load qwen/qwen3.5-9b` en la terminal.

---

### 2026-07-03 — Persistencia de Advertencias de Triage en el Orquestador del Glosario

**Contexto:**
Al ejecutar el orquestador global (`merci-total.py`), los avisos sobre términos pendientes de triage (`merci glosario --ai`) generados por `merci-glosario.py` se imprimían en las primeras etapas y terminaban desplazados o cortados del área visible (viewport) debido al desplazamiento de pantalla (*scrolling*) provocado por las salidas de los subsiguientes scripts. Adicionalmente, el almacenamiento en búfer de salida de terminal en subprocesos causaba renderizados incompletos o desordenados de emojis y textos en ciertos emuladores de terminal.

**Hecho:**
- Se configuró `PROYECTO_mercedev.es/scripts/merci/merci-glosario.py` en Modo Compilación para forzar el volcado inmediato (`flush=True`) de sus impresiones a la salida estándar (stdout).
- Se implementó en `merci-glosario.py` la escritura del total de términos pendientes de definir en el archivo de caché local `PROYECTO_mercedev.es/observabilidad/.pending_glossary_terms`.
- Se modificó `PROYECTO_mercedev.es/scripts/merci/merci-total.py` para leer este indicador y reimprimir el aviso consolidado al final de la ejecución del pipeline, justo antes del bloque interactivo de Experiencia del Desarrollador (DX).
- Se validó la visualización final del pipeline obteniendo la advertencia al final de la salida con éxito.

**Detalle técnico:**
- Archivo modificado: `PROYECTO_mercedev.es/scripts/merci/merci-glosario.py` (Líneas 232-255).
- Archivo modificado: `PROYECTO_mercedev.es/scripts/merci/merci-total.py` (Líneas 112-126).
- Archivo temporal: `PROYECTO_mercedev.es/observabilidad/.pending_glossary_terms`.
- Comando ejecutado: `python3 scripts/merci/merci-total.py`.

**Motivo / criterio:**
Asegurar una Experiencia de Desarrollador (DX) impecable y sin fricciones visuales. La pérdida silenciosa de advertencias sobre términos sin definir por scroll o buffer rompe el bucle de retroalimentación de la gobernanza documental (Spec as Source). Este mecanismo de persistencia garantiza que el triage no quede invisible para el operador.

**Siguiente paso o deuda:**
- Siguiente paso: Realizar el triage de los términos pendientes ejecutando `merci glosario --ai` de forma interactiva en la terminal de usuario.

---

### 2026-07-03 — Organización de Auditorías de Tienda y Publicación de Cuadernillo Lighthouse

**Contexto:**
Se identificó acumulación de archivos JSON pesados e informales de auditorías de Lighthouse en la raíz del proyecto (`tienda-audit-*.json`). Estos archivos se generaron durante las pruebas de optimización de la tienda de WooCommerce, pero ensuciaban el árbol de Git y el espacio de trabajo. Se acordó estructurar su almacenamiento local sin versionarlos en la nube y redactar un cuadernillo en la biblioteca para formalizar y documentar el proceso técnico llevado a cabo para lograr el pleno 100/100/100/100 en la tienda comercial.

**Hecho:**
- Se creó el directorio de diagnósticos `PROYECTO_mercedev.es/observabilidad/audits/` y se trasladaron los informes JSON allí.
- Se añadió la regla correspondiente en `PROYECTO_mercedev.es/.gitignore` para ignorar la carpeta `observabilidad/audits/`.
- Se eliminó el archivo duplicado y redundante `PROYECTO_mercedev.es/biblioteca/cuadernillo-cuadernillo-domando-woocommerce.md`.
- Se redactó y publicó el cuadernillo `PROYECTO_mercedev.es/biblioteca/cuadernillo-optimizacion-lighthouse-woocommerce.md` explicando detalladamente los frentes de optimización (desencolado de scripts de bloques, imágenes responsivas, filtro de robots a nivel de PHP).
- Se ejecutó el pipeline completo de compilación y QA, validando la integración del nuevo manual y la coherencia del sitemap y el buscador estático.

**Detalle técnico:**
- Archivo nuevo: `PROYECTO_mercedev.es/biblioteca/cuadernillo-optimizacion-lighthouse-woocommerce.md`.
- Archivo eliminado: `PROYECTO_mercedev.es/biblioteca/cuadernillo-cuadernillo-domando-woocommerce.md`.
- Archivo modificado: `PROYECTO_mercedev.es/.gitignore` (Líneas 43-46).
- Archivos reubicados: `tienda-audit*.json` de la raíz a `observabilidad/audits/`.
- Comando ejecutado: `python3 scripts/merci/merci-total.py`.

**Motivo / criterio:**
Mantener el repositorio limpio, ligero y libre de artefactos estáticos redundantes (Zero-Bloat en el control de versiones) sin perder la capacidad de consulta local. El nuevo cuadernillo consolida el conocimiento técnico acumulado, garantizando que el esfuerzo de optimización de WooCommerce quede estructurado como una Única Fuente de Verdad (SSOT) en la biblioteca pública.

**Siguiente paso o deuda:**
- Siguiente paso: Confirmar los cambios pendientes en el control de versiones local.

---

### 2026-07-03 — Corrección del Enrutamiento Resiliente de Inteligencia Artificial (LiteLLM / LM Studio)

**Contexto:**
Se identificó una desalineación arquitectónica entre la configuración de resiliencia del enrutador de LiteLLM (`observabilidad/router.yaml`) y el consumo del servicio de Inteligencia Artificial (IA) en los scripts locales (`merci-brain.py` y `merci-blogger.py`). El enrutador tenía como modelo primario una versión obsoleta de Gemini (`gemini-1.5-flash-latest`), y las aplicaciones consultaban directamente nombres de modelo en bruto (`openai/qwen2.5-coder` y `openai/gemini-2.5-flash`) en vez de los alias del proxy (`local-agent` e `ide-agent`), anulando el comportamiento del cortocircuito y degradación elegante (*Circuit Breaker* / *Fallback*).

**Hecho:**
- Se actualizó el modelo principal en `PROYECTO_mercedev.es/observabilidad/router.yaml` a `gemini/gemini-2.5-flash`.
- Se modificó `PROYECTO_mercedev.es/scripts/merci/merci-brain.py` para enrutar las peticiones al alias `local-agent` del proxy LiteLLM (puerto 4000).
- Se modificó `PROYECTO_mercedev.es/scripts/merci/merci-blogger.py` para canalizar las peticiones al alias `ide-agent` del proxy LiteLLM, habilitando la redirección transparente a la nube con contingencia local en LM Studio ante caídas del servicio de red.
- Se auditó el pipeline completo de compilación estática confirmando 0 avisos del linter y verificación de enlaces exitosa.

**Detalle técnico:**
- Archivo modificado: `PROYECTO_mercedev.es/observabilidad/router.yaml` (Línea 10).
- Archivo modificado: `PROYECTO_mercedev.es/scripts/merci/merci-brain.py` (Línea 58).
- Archivo modificado: `PROYECTO_mercedev.es/scripts/merci/merci-blogger.py` (Línea 137).
- Comandos ejecutados: `python3 scripts/merci/merci-audit.py` y `python3 scripts/merci/merci-total.py`.

**Motivo / criterio:**
Restablecer el funcionamiento correcto del patrón Proxy y Resiliencia Híbrida documentado en la biblioteca. Esto asegura que si la conexión a internet cae o falla la cuota de la API de Google, el blog y el motor del compilador puedan realizar la conmutación por error (*failover*) sin errores HTTP.

**Siguiente paso o deuda:**
- Siguiente paso: Evaluar el estado de los servicios locales y apagar LM Studio si no se requiere redactar nuevos borradores promocionales.

---

### 2026-07-03 — Sincronización de Fuentes de Vídeo y Alineación con el Patrón Gemelo Multimedia

**Contexto:**
Se identificó una divergencia entre el diseño documentado en la biblioteca (Estrategia Fallback Video WebM/MP4) y la implementación real del preprocesador multimedia en el generador estático (SSG) `merci-publish.py`, el cual solo inyectaba una única etiqueta source basada en la sintaxis de imagen del Markdown.

**Hecho:**
- Se refactorizó la expresión regular y la lógica de reemplazo de vídeos en `PROYECTO_mercedev.es/scripts/merci/merci-publish.py` para autogenerar el código de doble fuente en cascada (WebM primario y MP4 de fallback) de acuerdo al patrón de Gemelo Multimedia.
- Se verificó que el archivo `showcase-inyeccion-multimedia.html` compilado genera correctamente las etiquetas en cascada y mantiene el 100/100 en la telemetría SRE.
- Se ejecutó el pipeline de Aseguramiento de Calidad (QA) con éxito, confirmando la ausencia de hallazgos en la auditoría estática.

**Detalle técnico:**
- Archivo modificado: `PROYECTO_mercedev.es/scripts/merci/merci-publish.py` (Líneas 205-226) sustituyendo el reemplazo estático por una función auxiliar de conversión dual.
- Comando ejecutado: `python3 scripts/merci/merci-total.py`.

**Motivo / criterio:**
Unificar el comportamiento real del generador estático (SSG) con las especificaciones y contratos de rendimiento multimedia del ecosistema, evitando la degradación de Core Web Vitals en navegadores legacy y asegurando la fidelidad de la documentación pública de la biblioteca.

**Siguiente paso o deuda:**
- Siguiente paso: Confirmar los cambios y sellar la sesión de auditoría del compendio.

---

### 2026-07-03 — Corrección del Linter y Robustez del Flujo de Publicación en LinkedIn

**Contexto:**
Se detectó una advertencia en el linter de Pruebas de Seguridad de Aplicación Estática (SAST) por el uso del acrónimo `COD` sin expandir. Adicionalmente, se reportó un error de Protocolo de Transferencia de Hipertexto (HTTP) 401 en la ejecución del script de integración social de LinkedIn (`merci-linkedin.py`), quedando el sistema bloqueado al no invalidar el token de acceso expirado de Conexión Abierta de Identidad (OIDC).

**Hecho:**
- Se expandió el acrónimo `COD` en `PROYECTO_mercedev.es/laboratorio/bitacora-mercedev-epic-09.md` para cumplir con las directrices de soberanía lingüística como "Pago Contra Reembolso (COD)".
- Se implementó la captura de excepciones HTTP 401 en la obtención del Nombre de Recurso Uniforme (URN) del usuario en `PROYECTO_mercedev.es/scripts/merci/merci-linkedin.py`, realizando el borrado automático del archivo local de credenciales expiradas.
- Se añadió soporte para imprimir explícitamente el enlace de autenticación interactivo en la terminal en caso de fallo de autenticación o ausencia de token.
- Se ejecutó el pipeline de Aseguramiento de Calidad (QA) con éxito, confirmando la ausencia de hallazgos en la auditoría estática.

**Detalle técnico:**
- Archivo modificado: `PROYECTO_mercedev.es/laboratorio/bitacora-mercedev-epic-09.md` (Línea 49).
- Archivo modificado: `PROYECTO_mercedev.es/scripts/merci/merci-linkedin.py` (Líneas 12-18, 124-127 y 166-173) importando `urllib.error` y controlando errores 401 mediante `TOKEN_PATH.unlink()`.
- Comandos ejecutados: `python3 scripts/merci/merci-audit.py` y `python3 scripts/merci/merci-total.py`.

**Motivo / criterio:**
Garantizar la auto-reparación (*Self-Healing*) del flujo DevSecOps y optimizar la Experiencia del Desarrollador (DX) en terminales sin interfaz gráfica activa. La soberanía lingüística y la resolución de alertas en el linter son fundamentales para asegurar la higiene documental del repositorio.

**Siguiente paso o deuda:**
- Siguiente paso: Confirmar los cambios pendientes en el control de versiones local e iniciar la re-autenticación interactiva en la cuenta de LinkedIn mediante `merci linkedin`.

---

### 2026-06-18 — Fase 4: Tienda WooCommerce a 100/100/100/100 en Lighthouse

**Contexto:**
La tienda (`/blog/tienda/`) partía de 96/100 en Best Practices, 66/100 en SEO, 86/100 en Performance y 100/100 en Accesibilidad. Objetivo: recuperar el pleno 100/100/100/100 que había tenido antes de los cambios de esta épica.

**Hecho:**
- **Best Practices (96→100):** Se desencolan los scripts de WooCommerce Blocks en el frontend (`wc-cart-block`, `wc-checkout-block`, `wc-blocks`, `wc-settings`…) mediante un hook `wp_enqueue_scripts` a prioridad 100, eliminando 4 errores de consola JS sobre la pasarela de Pago Contra Reembolso (COD). Se añaden los filtros `woocommerce_blocks_has_classic_checkout/cart` para señalizar el modo clásico.
- **SEO (66→100):** WordPress tenía activa la opción "Desanimar motores de búsqueda" (`blog_public=0`), inyectando `<meta name="robots" content="noindex, nofollow">` en todas las páginas. Se amplió el filtro `wp_robots` existente para que elimine `noindex`/`nofollow` y fuerce `index, follow` a prioridad 9999, sobrescribiendo tanto WP Core como WooCommerce.
- **Performance (86→100):** Tres frentes atacados:
  1. **Render-blocking CSS (−170ms):** Añadido `<link rel="preload">` del `main.css` antes del `<link rel="stylesheet">` en `woocommerce.php`.
  2. **Imágenes de productos sobredimensionadas (−481KB):** Modificado `merci-shop.py` para que, al subir imágenes a WooCommerce vía API, prefiera automáticamente la versión `-400w.webp` de cada producto (generada por `merci-optimizer.py` desde `.assets-raw/`) en lugar de la imagen original 2048×2048px.
  3. El optimizer (`merci-optimizer.py`) ya tenía las versiones `-400w` listas en `assets/images/`; bastó con enrutar correctamente la URL en la sincronización con la API de WooCommerce.
- **Aviso "Economía Simulada":** Corregida la imagen de la llama en `woocommerce.php` de `tu_logo-80w.webp` → `favicon.ico` (16×16), coherente con el símbolo de moneda en `functions.php`.
- Pipeline completo `merci-total.py` → 💡 Todo en verde.

**Detalle técnico:**
- `PROYECTO_mercedev.es/src/wp-theme/merci-theme/functions.php`: filtros `wp_robots` (prioridad 9999) y `wp_enqueue_scripts` (prioridad 100) para dequeue de Blocks.
- `PROYECTO_mercedev.es/src/wp-theme/merci-theme/woocommerce.php`: preload CSS + corrección imagen llama.
- `PROYECTO_mercedev.es/scripts/merci/merci-shop.py`: lógica de preferencia `-400w` en URLs de imagen de producto.

**Motivo / criterio:**
El 100/100/100/100 es un contrato de calidad del ecosistema, no un objetivo aspiracional. El optimizer ya existía (`merci-optimizer.py`), el pipeline de imágenes responsivas ya era correcto — solo faltaba cerrar el circuito entre el optimizer y el endpoint de la API de WooCommerce.

**Siguiente paso o deuda:**
- Backup de la épica.
- Checklist de cierre de la Épica 9.

### 2026-06-18 — Fase 4: Optimización Best Practices Tienda WooCommerce (96→100)

**Contexto:**
Lighthouse reportaba 96/100 en Best Practices para la página de la tienda (`/blog/tienda/`) debido a 4 errores de consola repetidos: `Payment gateway 'wc-payment-method-cod' deactivated in Cart and Checkout blocks because its dependencies are missing`. El error era generado por los scripts de WooCommerce Blocks en el frontend, aunque la tienda usa el checkout clásico de WooCommerce (no los bloques de Gutenberg).

**Hecho:**
- Se sustituyó el símbolo de moneda del gateway personalizado de `tu_logo-80w.webp` → `favicon.ico` (16×16) en `functions.php`, manteniendo el estilo CSS `.merci-coin-icon` con `height: 1.2em; width: auto`.
- Se añadieron los filtros `woocommerce_blocks_has_classic_checkout` y `woocommerce_blocks_has_classic_cart` con `__return_true` para señalizar a WooCommerce que el tema usa el checkout clásico.
- Se implementó un hook `wp_enqueue_scripts` con prioridad 100 que desencola y desregistra los scripts de WooCommerce Blocks en el frontend (`wc-cart-block`, `wc-checkout-block`, `wc-blocks`, `wc-settings`, etc.).
- Se verificó el resultado con varias iteraciones de Lighthouse hasta alcanzar **Best Practices: 100/100** y **Accessibility: 100/100** sin errores de consola.
- Se sincronizó el pipeline completo con `merci-total.py` (11s, todo en verde).

**Detalle técnico:**
El error JS no podía resolverse a nivel PHP (hooks de WooCommerce Blocks) porque se producía en el navegador tras la carga de los scripts de bloques. La solución correcta fue desencolar esos scripts a prioridad 100 (posterior al registro de WooCommerce a prioridad 10-20) en `PROYECTO_mercedev.es/src/wp-theme/merci-theme/functions.php`.

**Motivo / criterio:**
Los errores de consola son evaluados por Lighthouse como fallos de Best Practices con peso directo en la puntuación. Desencolar scripts no usados es, además, un acierto de rendimiento (reduce JS en el critical path), alineado con la filosofía Zero-Bloat del ecosistema.

**Siguiente paso o deuda:**
SEO (66/100) y Performance (86/100) aún pendientes de optimizar para recuperar el 100/100/100/100.

### 2026-06-18 — Fase 4: Corrección de Paginación Invisible en Blog Cronológico

**Contexto:**
Durante la refactorización a un blog cronológico vertical (Épica 8), se eliminó la paginación por defecto, dejando todas las entradas anteriores al 14/06 inaccesibles desde la interfaz debido al límite predeterminado de 10 posts por página en WordPress.

**Hecho:**
- Se inyectó la función `the_posts_pagination()` en `src/wp-theme/merci-theme/index.php`.
- Se maquetaron los estilos BEM para la paginación nativa de WP en `src/scss/components/_blog-feed.scss` manteniendo la directriz *Zero-Bloat*.
- Se recompilaron los estilos y plantillas con el orquestador maestro (`merci-total.py`), restaurando el acceso a todo el archivo histórico con resultados de validación perfectos (11.19s).

**Motivo / criterio:**
La optimización extrema (Anti-Bloat) nunca debe sacrificar la accesibilidad ni la navegabilidad fundamental del contenido.

### 2026-06-18 — Fase 4: Sincronización del Boilerplate, Circuit Breakers y Pila Híbrida

**Contexto:**
Tras validar el funcionamiento de los Fallbacks y Circuit Breakers (Chaos Engineering), era necesario actualizar la documentación agnóstica (`README-merci.md`, `instrucciones.md`), empaquetar la v1.20.0 y reestructurar el compendio de cierre de la épica según el estándar SEO.

**Hecho:**
- Alineación del comportamiento "Pila Híbrida / Fallback" en los agentes documentados en `instrucciones.md`.
- Inclusión del test de resiliencia (Chaos Fallback) como paso innegociable del Protocolo de Cierre de Fase.
- Lanzamiento de la versión v1.20.0 en el repositorio `merci-boilerplate` usando `merci-release.py --non-interactive` (purgando identidad visual y corporativa en un entorno efímero).
- Corrección de la taxonomía del compendio a "DevSecOps e Infraestructura", cambio a estado borrador y promoción limpia a la Biblioteca mediante `merci promote`.

**Motivo / criterio:**
El Boilerplate debe reflejar siempre el estado del arte de la matriz `mercedev.es`. La nueva arquitectura "Shift-Left AI" con fallback en la nube eleva la resiliencia del pipeline a un grado de confiabilidad ininterrumpida.

### 2026-06-15 — Fase 4: Documentación de la Arquitectura de Enrutamiento Inverso (Art de Coté)

**Contexto:**
Durante la discusión sobre el comportamiento de la Pila Híbrida y los Fallbacks ante la falta de tokens (HTTP 429), se analizó la diferencia entre el router del IDE (`router.yaml` + `merci-boot.sh`) y el router del compilador (`merci-brain.py`). Ambos usan `litellm` pero con prioridades diametralmente opuestas.

**Hecho:**
Se documentó esta dicotomía de diseño creando el artículo público `laboratorio/incubacion/art-de-cote-enrutamiento-ia.md`. El artículo expone cómo el IDE utiliza una ruta "Inteligencia Máxima (Cloud) ➔ Supervivencia Local", mientras que el compilador aplica "Ahorro Máximo (Local) ➔ Rescate Cloud ➔ Circuit Breaker Estático".

**Motivo / criterio:**
*Knowledge Sharing & Transparency*. La decisión de invertir la carga cognitiva dependiendo del entorno (desarrollo vs CI/CD) es un concepto arquitectónico clave que merece ser compartido públicamente, demostrando la madurez del ecosistema Zero-Code. No debe quedar oculto en la documentación interna (`.privado`).

### 2026-06-15 — Fase 4: Debug y Parcheo del Chaos Monkey (Táctica C)

**Contexto:**
Durante las rondas de pruebas de Chaos Engineering saltó la Táctica C (Deriva Documental), en la que el Monkey inyecta un script falso o "fantasma" sin documentar para verificar que las defensas SSOT bloquean el pipeline. Sin embargo, el Chaos Monkey informó de una vulnerabilidad: "El código/archivo pasó indetectado".

**Hecho:**
- Se analizó el flujo de inyección y detección en `merci-chaos.py`.
- Se detectó que el Chaos Monkey estaba invocando el linter general de higiene (`merci-audit.py`) para validar la deriva documental.
- Puesto que `merci-audit.py` audita sintaxis, SEO y secretos pero *no* la gobernanza SSOT (responsabilidad delegada a `merci-drift.py`), el archivo fantasma era validado como "código Python perfecto" y pasaba.
- Se refactorizó la estructura `try/except` de la Táctica C en `merci-chaos.py` para que lance específicamente el binario correcto (`merci-drift.py`).

**Motivo / criterio:**
El testing es tan frágil como la asunción del programador sobre el test. En este caso, el ecosistema DevSecOps funcionaba y estaba bien diseñado (Separation of Concerns entre higiene y deriva), pero el orquestador del test usaba el instrumento equivocado. Corregirlo certifica que la matriz de validación cubre realmente los vectores de ataque previstos.

**Siguiente paso o deuda:**
Lanzar otra ronda de Chaos Engineering para verificar que la Táctica C y el detector de deriva documental se conectan y bloquean la intrusión con éxito.

### 2026-06-15 — Fase 4: Éxito del Chaos Monkey y Activación del Circuit Breaker

**Contexto:**
Tras solucionar el problema de la API de Gemini, se reanudó la simulación de *Chaos Engineering* (Táctica B - Corte de Red). El objetivo era comprobar empíricamente que el entorno de producción puede sobrevivir a un fallo del motor de IA local sin interrupción de servicio y soportar la carga masiva en la nube.

**Hecho:**
- El *Chaos Monkey* inyectó con éxito una caída catastrófica en Ollama (puerto muerto 9999).
- El sistema de agentes interceptó el fallo de conexión (`[Errno 111] Connection refused`) y aplicó el *Fallback* a Gemini 2.5 Flash de forma transparente.
- Tras 8 iteraciones de fallback exitosas, la cuenta gratuita de la API de Google aplicó un *Rate Limit* (Demasiadas peticiones).
- Lejos de crashear el pipeline, el patrón *Circuit Breaker* diseñado en `merci-brain.py` capturó la excepción, suspendió elegantemente las llamadas a la API, e inyectó automáticamente una cadena de contingencia (`[Fallback]`) en los 84 artículos restantes.
- La compilación finalizó con código de éxito (Exit 0) y el *Chaos Monkey* aplicó el *Auto-Healing* devolviendo el repositorio a su estado inmaculado.

**Motivo / criterio:**
El objetivo de SRE (*Site Reliability Engineering*) no es que los componentes nunca fallen, sino que el sistema global nunca colapse cuando lo hacen. La prueba empírica demuestra que el ecosistema cuenta con doble capa de protección: resiliencia ante cortes de red (*Fallback*) y resiliencia ante denegación de servicio o límites de cuota (*Circuit Breaker*).

**Siguiente paso o deuda:**
Promover el aprendizaje de esta sesión a la biblioteca creando un nuevo cuadernillo sobre la arquitectura de Pila Híbrida y *Chaos Engineering*.

### 2026-06-15 — Fase 4: Descubrimiento de Fallo en Producción por Chaos Engineering

**Contexto:**
Al probar el *Chaos Monkey* con la nueva Táctica B (Corte de Red), confirmamos el inmenso valor de las prácticas de *Chaos Engineering*. La simulación inyectó un fallo catastrófico en Ollama, obligando al sistema a realizar un *fallback* automático hacia el proxy de Gemini. Sin embargo, el fallback falló inesperadamente porque el modelo `gemini-1.5-flash` había quedado obsoleto y ya no era soportado por la API de Google (v1beta).

**Hecho:**
- El experimento de caos abortó limpiamente, dejando un archivo residual `brain_data.json` que detuvo futuras simulaciones por seguridad (ensuciando Git).
- Se ejecutó un script de *debug* (`test_gemini.py`) que iteró sobre modelos alternativos soportados.
- Se descubrió que la API aceptaba el modelo `gemini-2.5-flash`.
- Se actualizó el modelo en los agentes `merci-brain.py` y `merci-blogger.py` a `gemini/gemini-2.5-flash`.
- Se limpió el entorno de trabajo y el *Chaos Monkey* recuperó su estado de operatividad seguro.

**Motivo / criterio:**
Las APIs externas son un componente de alto riesgo en la cadena de suministro (*Supply Chain*). El hecho de que el modelo `1.5-flash` fuera descontinuado habría provocado una caída total silenciosa de nuestros agentes si el nodo local de Ollama hubiera fallado en producción. El *Chaos Monkey* ha demostrado su valor al sacar a la luz este fallo oculto antes de que afectara a los flujos reales.

**Siguiente paso o deuda:**
Realizar el commit de estos cambios e iniciar una nueva simulación de *Chaos Engineering* (`merci chaos`) para comprobar que ahora sí, las tres tácticas y el escudo funcionan perfectamente.

### 2026-06-15 — Fase 4: Preparación para Chaos Engineering (Hybrid Stack & Tácticas)

**Contexto:**
Para probar la resiliencia del motor de IA y las defensas contra derivas documentales, necesitábamos asegurar que el entorno utilizaba verdaderamente un "Hybrid Stack" (con Ollama como primario y Gemini como respaldo) y extender el script del Chaos Monkey para inyectar estos fallos específicos de red y gobernanza.

**Hecho:**
- Se refactorizó `scripts/merci/merci-brain.py` y `scripts/merci/merci-blogger.py` para implementar un bloque `try...except` que intenta llamar a `ollama/qwen2.5-coder` (con timeout de 10s) y realiza el *fallback* al Gemini Proxy (`litellm`) en caso de fallo.
- Se amplió `scripts/merci/merci-chaos.py` con dos nuevas tácticas: Táctica B (Corte de Red) falsificando el puerto local de Ollama para forzar el fallback; y Táctica C (Deriva Documental) inyectando un script fantasma no registrado.
- Se refactorizaron las Expresiones Regulares en `scripts/merci/merci-commit.py` haciéndolas robustas y agnósticas para soportar cualquier sintaxis en los títulos de las secciones de la bitácora.

**Detalle técnico:**
Se actualizaron `merci-brain.py`, `merci-blogger.py` y `merci-chaos.py`. La Táctica B muta dinámicamente `os.environ["OLLAMA_API_BASE"] = "http://localhost:9999"` durante la ejecución para forzar caídas controladas.

**Motivo / criterio:**
El concepto de "Pila Híbrida" (Hybrid Stack) exige que exista un motor local gratuito como primera opción, utilizando la nube solo como salvavidas. Extender el Chaos Monkey garantiza de forma empírica que esta red de seguridad y el escudo linter de deriva funcionan bajo presión extrema.

**Siguiente paso o deuda:**
Lanzar la simulación de *Chaos Engineering* (`merci-chaos.py`) tras limpiar el directorio de trabajo, para validar las tres tácticas y hacer la comprobación de auditoría definitiva.

### 2026-06-15 — Fase 3: Autarquía del Motor de IA ( Antigravity Proxy / LiteLLM )

**Contexto:**
La arquitectura requería evolucionar más allá de la dependencia exclusiva en modelos locales (Ollama), configurando un enrutamiento seguro hacia el IDE Antigravity / Gemini Proxy como motor de contingencia y respaldo definitivo.

**Hecho:**
- Se refactorizó `merci-blogger.py` para reemplazar las peticiones directas a `http://localhost:11434` (Ollama) por integraciones usando la librería `litellm`.
- Se refactorizó `merci-brain.py` inyectando compatibilidad con `litellm` para redirigir la carga cognitiva (saludos y procesamiento contextual) al modelo `gemini/gemini-1.5-flash` a través de la clave `GEMINI_API_KEY` extraída del archivo `.env`.
- Se validó el aislamiento de la configuración (silenciando la telemetría de LiteLLM para no ensuciar la salida DevSecOps).
- Se marcó el hito de "Autarquía del Motor de IA" como completado (`[x]`) en el ROADMAP maestro.

**Motivo / criterio:**
Centralizar el motor de IA a través de un proxy agnóstico (`litellm`) aumenta la resiliencia del ecosistema, permitiendo un "Shift-Left AI" que no depende del hardware local para mantenerse operativo al 100%.

**Siguiente Paso:**
El paso inmediatamente posterior es activar el *Chaos Engineering* e inyectar cortes de red simulados para verificar si la infraestructura recae exitosamente en el Proxy de Gemini bajo condiciones hostiles, así como inyectar derivas documentales para comprobar el linter `merci-drift`.

### 2026-06-15 — Rectificación: Restauración de botones flotantes (UI/UX)

**Contexto:**
Durante la limpieza de la UI en la Fase 2, se eliminaron los botones de volver arriba (`.floating-back-to-top`) de `index.html`, `sobre-mi` y `contacto` bajo la premisa de que no tenían scroll. Sin embargo, esto violaba el principio de consistencia visual del diseño Premium, ya que los botones debían funcionar en todos lados por igual, manteniéndose ocultos hasta hacer scroll y no actuando simplemente como "barras de desplazamiento" fijas. 

**Hecho:**
- Se han restaurado los botones flotantes (`<a href="#top" class="floating-back-to-top">`) en `public/index.html`.
- Se implementó la clase JavaScript `BackToTopController` en `public/js/main.js` (Zero dependencias externas) que hace uso de `requestAnimationFrame` y eventos pasivos de scroll para mostrar el botón solo cuando `window.scrollY > 300` px.
- Se ejecutó `merci-sync-pages.py` para sincronizar `index.html` con las demás páginas estáticas del ecosistema.

**Motivo / criterio:**
No eliminar elementos globales si la interfaz se siente asimétrica. Si un elemento visual molesta en un contexto (como en páginas sin scroll), es preferible modificar su comportamiento (lógica JS/CSS) que amputarlo por completo de algunas plantillas. Todo error arquitectónico debe añadirse como rectificación nueva (append) y nunca reescribiendo la historia pasada.

### 2026-06-15 — Fase 2: Soporte SRE para Blog, Tienda y Rediseño de Accesibilidad

**Contexto:**
Tras la implementación de la telemetría básica, se detectó que el Blog y la Tienda dinámica (servidas dinámicamente por WordPress/WooCommerce en PHP) carecían de los micro-sellos visuales SRE. Además, se constató que la combinación de colores traslúcidos original sobre fondos claros violaba las directrices de accesibilidad (contraste insuficiente en texto y puntuaciones).

**Hecho:**
- Se amplió `TARGET_URLS` en `merci-extract-metrics.py` para auditar concurrentemente las páginas del Blog (`/blog/`) y la Tienda (`/blog/tienda/`).
- Se diseñó e implementó la función auxiliar PHP `merci_get_sre_badge_html($url)` en `functions.php` del tema de WordPress y se inyectó en los héroes de `index.php` y `woocommerce.php`.
- Se reescribió `src/scss/components/_sre-badge.scss` para utilizar un fondo claro sólido y colores corporativos oscurecidos de alta visibilidad para las puntuaciones, garantizando el cumplimiento de la norma **WCAG AA (> 4.5:1)** sobre blanco: Verde (`#065f46`), Naranja (`#9a3412`) y Rojo (`#b91c1c`).
- Se inyectaron los emoticonos de leyenda (`⚡`, `♿`, `🛡️`, `🔍`) en la frase de puntuaciones de la portada (`index.html`) y se modificó `merci-extract-metrics.py` para mantener su persistencia dinámica.
- Se eliminaron los botones de volver arriba flotantes (`.floating-back-to-top`) de las páginas cortas del ecosistema (`/index.html`, `/sobre-mi/index.html` y `/contacto/index.html`), al carecer de sentido en vistas sin scroll vertical largo, manteniéndose exclusivamente en las estanterías de la biblioteca, proyectos y art-de-cote.
- Se ejecutó el pipeline completo de validación y compilación con éxito, registrando la expansión del acrónimo Tasa de Fotogramas Variable (VFR) en esta entrada activa para satisfacer al linter sin modificar registros históricos.

**Motivo / criterio:**
El principio de inmutabilidad histórica de la bitácora obliga a registrar de forma incremental tanto los aciertos como las rectificaciones de diseño. Integrar capas dinámicas de PHP mediante lectura local de caché en disco preserva las ventajas de velocidad del ecosistema SSG sin deteriorar el TTFB. La gobernanza de accesibilidad (a11y) debe primar sobre los caprichos estéticos, adaptando la UI para ser leída por cualquier usuario.

### 2026-06-15 — Fase 2: Expansión de Telemetría SRE (Accesibilidad & URL Granular)

**Contexto:**
Se necesitaba ampliar la telemetría SRE para incorporar la deuda técnica de accesibilidad (cuantificando problemas de contraste de color y ARIA) en Grafana, así como inyectar micro-sellos visuales Zero-JS con las puntuaciones reales de Lighthouse en las 7 páginas principales del ecosistema, evitando degradar la velocidad del pipeline local.

**Hecho:**
- Se diseñó el componente visual `sre-badge` con estilos CSS/SASS glassmorphic y se registró en `src/scss/components/_sre-badge.scss`.
- Se configuró el extractor para solicitar todos los ámbitos de Lighthouse a la API de PageSpeed e implementó la cuantificación detallada de errores de contraste y ARIA en `merci-extract-metrics.py`.
- Se implementó la resolución y caché paralela (`ThreadPoolExecutor`) de las 7 páginas principales del sitio en `observabilidad/.lighthouse_pages_cache.json` con un TTL de 24 horas.
- Se inyectaron dinámicamente los micro-sellos en las portadas e índices compilados mediante `merci-publish.py` e inyectó los badges en archivos estáticos mediante `merci-sync-pages.py` con marcadores `<!-- Merci SRE Badge -->`.
- Se añadieron los Gauges `merci_lighthouse_accessibility_contrast_errors` y `merci_lighthouse_accessibility_aria_errors` en el agente `merci-sre.py` y se crearon los paneles 27 y 28 en el dashboard JSON de Grafana.
- Se actualizaron el ROADMAP, el Walkthrough y el listado de tareas del proyecto.

**Motivo / criterio:**
La ejecución concurrente multihilo minimiza el tiempo de red a un único ciclo de llamadas API (~12s) que solo se activa al expirar la caché de 24h. Mantener los badges libres de Javascript preserva el rendimiento óptimo del frontend, garantizando el 100/100 Core Web Vitals en producción.

### 2026-06-15 — Fase 2: Implementación de Telemetría SRE (Anti-Bloat) y Gobernanza

**Contexto:**
Se requería vigilar activamente que el crecimiento del ecosistema no rompa la filosofía "Zero-Bloat". Además, se detectó un truncamiento accidental en el archivo que dicta el perfil operativo de la IA (`.privado/gemini.md`).

**Hecho:**
- Se reconstruyó en su totalidad el archivo `gemini.md` y se promocionó a la base de conocimiento oficial (KI) del IDE Antigravity.
- Se inyectó en `scripts/merci/merci-sre.py` the new Gauge `merci_public_folder_size_bytes` y una función recursiva para auditar el tamaño de la carpeta estática.
- Se inyectó programáticamente en `observabilidad/dashboards/merci-dashboard.json` el panel visual "Peso Estático (/public)".
- *Hotfix (Grafana Schema):* Se corrigió una infracción de esquema en el JSON del Dashboard. La API de Grafana v13.0 descartaba silenciosamente el panel porque la propiedad `element` esperaba un objeto `{"kind": "ElementReference", "name": "panel-26"}` y no un *String* plano.

**Motivo / criterio:**
Monitorear físicamente el peso del ecosistema permite anticipar la deuda técnica y degradaciones en Core Web Vitals antes de que sucedan. Reparar las reglas de la IA asegura el rigor arquitectónico a futuro.

### 2026-06-15 — Investigación: Preservación de Herramientas Estériles (FFmpeg)

**Contexto:**
Se necesitaba automatizar la purga de tiempos muertos ("congelación de terminal") en los vídeos de demostración del proyecto (showcase). Se experimentó con la vía de bajo nivel usando `FFmpeg` y el filtro `mpdecimate`.

**Hecho:**
- Se generó el script `scripts/temporales/merci-mpdecimate-fastforward.sh`.
- El script cumplió técnicamente su función de compresión extrema (de 272MB a 62MB), pero generó un efecto "Hyper-Timelapse" epiléptico inasumible para la visualización humana.
- Se experimentó alternativamente con `auto-editor` (Python) para recortar fotogramas inactivos manteniendo un "padding" humano (`--margin 0.5s`), pero el intento falló debido a la falta de metadatos de fotogramas constantes (`time_base=0/0`, Tasa de Fotogramas Variable (VFR)) en la grabación de pantalla cruda.
- En lugar de desechar el código, se confinó en el nuevo directorio `scripts/temporales/` y se documentó explícitamente en su cabecera el motivo de su fracaso y las alternativas humanas recomendadas (CapCut, auto-editor), cumpliendo las normas de gobernanza.

**Motivo / criterio:**
Un script fracasado es una lección arquitectónica valiosa. Mantener el ecosistema Zero-Bloat también implica no saturar la carpeta principal de `scripts/` con utilidades estériles, derivándolas a un silo de cuarentena/histórico debidamente comentado.

## Notas Arquitectónicas

### 2026-06-18 — Resolución de Bugs en UI, Sincronización y Documentación de Fallbacks IA

**Contexto:**
Se requería unificar la experiencia de usuario con el botón "Volver arriba" que presentaba inconsistencias en diferentes páginas (inexistente en `sobre-mi`, y con scroll irregular en la `portada` y las vistas dinámicas). Además, se solicitó corregir el Glosario Técnico para no aplicar el tooltip a los términos dentro de su propio documento, y subsanar las divergencias de taxonomía en los cuadernillos.

**Hecho:**
- **Scroll Suave y Accesibilidad:** Se implementó un ancla invisible (`<div id="top" tabindex="-1" style="position: absolute; top: 0; left: 0;"></div>`) y se eliminó el `id="top"` del `<header>` en `index.html` y en `merci-theme/index.php`. Esto permite que el botón `.floating-back-to-top` realice un scroll absoluto a la posición 0 sin interferencias con elementos de posición `sticky`.
- **Sincronización:** Se actualizó la expresión regular en `merci-sync-pages.py` para soportar la nueva estructura del ancla sin romper el proceso automatizado de inyección.
- **Burbuja Merci (Glosario):** Se modificó `merci-publish.py` para que la inyección dinámica de etiquetas `<abbr>` omita explícitamente el archivo madre `glosario-tecnico.md`.
- **Gobernanza:** Se corrigieron los metadatos YAML (Frontmatter) en los archivos `compendio-epica-07-multimedia-gamificacion.md` y `cuadernillo-resolucion-desbordamiento-css-codigo.md`, ajustándolos a la taxonomía permitida (`Desarrollo y Arquitectura`).
- **Art de Coté:** Se redactó `art-de-cote-sistemas-fallback-ia.md` documentando las diferencias a nivel arquitectónico entre el modelo de contingencia de LiteLLM y el sistema dinámico de fallback proporcionado por el SDK de Antigravity.

**Motivo / criterio:**
Estas acciones unifican el UX a través del ecosistema SSG, garantizan la pureza del generador estático y aseguran que el conocimiento sobre los mecanismos de resiliencia ante límites de la API quede materializado y accesible según el principio SSOT.

## Notas Arquitectónicas

*(Espacio para documentar bloqueos o decisiones técnicas durante la ejecución de la épica).*
