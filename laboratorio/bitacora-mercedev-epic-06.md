# Bitácora del proyecto mercedev.es — Épica 6: E-commerce Híbrido Extremo

## Para qué sirve este archivo

Bitácora activa a partir de la finalización de la Épica 5 (Showcase y Distribución del Boilerplate).
Registra exclusivamente las decisiones, experimentos y aprendizajes de la Épica 6 (E-commerce Híbrido Extremo) documentada en el `ROADMAP.md` maestro.

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

### 2026-05-23 — Arch: Pivote a "Tienda No Tienda" (Mock E-commerce Headless)

**Contexto:** La Épica 6 preveía la integración de pasarelas de pago reales (Stripe/PayPal) para demostrar un e-commerce híbrido de alto rendimiento. Se replanteó el objetivo buscando demostrar la capacidad arquitectónica (dominar WooCommerce) sin asumir la burocracia legal/financiera ni la carga de scripts de terceros en el frontend.

**Hecho:** Se reestructuró la Épica 6 en el `ROADMAP.md`, cancelando la integración de pasarelas de terceros. Se definió el desarrollo de una "Tienda No Tienda" gobernada 100% mediante terminal y archivos locales.

**Detalle técnico:** En lugar de operar productos desde el panel de WordPress, se utilizarán archivos Markdown con metadatos YAML (precio, inventario, imágenes). Se construirá un orquestador en Python que utilizará la API REST nativa de WooCommerce (`/wc/v3/products`) para sincronizar el catálogo de forma unidireccional (Headless), permitiendo a los visitantes simular una compra sin procesar pagos reales.

**Motivo / criterio:** *Spec-Driven Development y Zero-Risk*. Manejar el catálogo de productos localmente con Python respeta el principio de "Única Fuente de Verdad" (SSOT). Eliminar las pasarelas reales mantiene puro el código, extirpa el riesgo legal y certifica el hito técnico: demostrar que se puede construir un e-commerce extremadamente rápido (100/100) completamente disociado del panel de control tradicional del CMS.

**Siguiente paso o deuda:** Crear la estructura de carpetas (ej. `laboratorio/tienda/`), diseñar la plantilla YAML para productos y desarrollar el script de sincronización.

### 2026-05-23 — Shift-Left SEO: Validación estricta de longitud en metadatos (Chaos Monkey)

**Contexto:** El Agente Chaos saboteó la portada inyectando una meta descripción excesivamente larga y fraudulenta ("FALSAMENTE LABORATORIO..."), evadiendo el auditor estático que solo verificaba la existencia de la etiqueta, pero no su longitud ni calidad SEO.

**Hecho:** Se implementaron reglas de validación de longitud máxima para `<title>` y `<meta name="description">` en `scripts/merci/merci-audit.py`.

**Detalle técnico:** Se añadieron aserciones que lanzan errores bloqueantes `SEO_TITLE_LENGTH` (límite de 65 caracteres) y `SEO_DESC_LENGTH` (límite de 150 caracteres) dentro de la función `audit_html_seo`.

**Motivo / criterio:** *Shift-Left SEO y Calidad Estricta*. Los motores de búsqueda truncan los metadatos excesivamente largos, perdiendo el control del mensaje y afectando al CTR (Click-Through Rate). Validar matemáticamente la longitud en el linter garantiza que los textos promocionales encajen perfectamente en las SERPs (Search Engine Results Pages) y bloquea inyecciones de *spam* o desbordamientos inducidos por el Chaos Monkey.

**Siguiente paso o deuda:** Re-ejecutar `merci chaos` para validar que el linter intercepta y bloquea la mutación por exceso de caracteres.

### 2026-05-23 — DevSecOps: Resiliencia del parser JSON frente a alucinaciones de formato (Agente Chaos)

**Contexto:** La IA generaba tácticas de sabotaje válidas, pero el script `merci-chaos.py` abortaba creyendo que había fallado la búsqueda. Gracias a la reciente observabilidad de respuestas crudas, se descubrió que el modelo estaba escapando comillas simples (`\'`) dentro del JSON, lo cual es un error de sintaxis en el estándar JSON y provocaba un `JSONDecodeError` silencioso.

**Hecho:** Se refactorizó la función `extract_json_array` en `scripts/merci/merci-chaos.py`.

**Detalle técnico:** Se inyectó un saneamiento previo (`json_str.replace("\\'", "'")`) antes de invocar a `json.loads()`. Esto purifica la cadena de texto de escapes ilegales comunes en los LLMs antes del parseo estricto.

**Motivo / criterio:** *Robustez y Ley de Postel*. Ser liberales en lo que aceptamos. Los Small Language Models (SLMs) cometen micro-errores de sintaxis al generar código estructurado. En lugar de frustrarnos endureciendo el prompt, añadir tolerancia al parser nativo de Python garantiza que el agente sea resiliente y no interrumpa el bucle de pruebas.

**Siguiente paso o deuda:** Re-ejecutar `merci chaos` para confirmar que el payload ahora sí es parseado e inyectado correctamente en el código objetivo.

### 2026-05-23 — DevSecOps: Observabilidad de respuestas crudas en Agente Chaos

**Contexto:** Cuando el Agente Chaos fallaba en su intento de sabotaje por no generar el JSON esperado o errar en la clave de búsqueda, abortaba la ejecución sin mostrar qué había respondido exactamente la IA, dificultando la depuración de alucinaciones del SLM local.

**Hecho:** Se inyectó un registro de respuesta cruda (*raw response*) en la lógica de aborto de `scripts/merci/merci-chaos.py`.

**Detalle técnico:** Si el array `sabotajes` o la clave `buscar` no existen, el script ahora imprime por consola `respuesta.choices[0].message.content`, revelando el texto exacto generado por el modelo local.

**Motivo / criterio:** *Observability y SLM Debugging*. Los Modelos de Lenguaje Pequeños (SLMs) pueden volverse conversacionales o romper el formato exigido. Tener visibilidad total (caja de cristal) de su salida errónea es indispensable para poder endurecer el *System Prompt* y evitar futuras evasiones de formato.

**Siguiente paso o deuda:** Re-ejecutar `merci chaos` hasta atrapar una respuesta cruda fallida y ajustar el `prompt-chaos.md` en consecuencia.

### 2026-05-23 — Sec: Extensión de validación AST en auditor Python (Chaos Monkey)

**Contexto:** Un simulacro de seguridad del Agente Chaos reveló que ciertas invocaciones a funciones de sistema de bajo nivel en Python estaban evadiendo los escudos estáticos, representando un riesgo potencial de ejecución no deseada si eran inyectadas en el ecosistema.

**Hecho:** Se implementó y extendió la regla `audit_python_smells` en `scripts/merci/merci-audit.py`.

**Detalle técnico:** La validación ahora parsea el Árbol de Sintaxis Abstracta (AST) para detectar el uso de funciones de sistema (`system`, `eval`, `exec`) y llamadas a subprocesos de bajo nivel (`Popen`). Su uso detiene automáticamente el pipeline. Simultáneamente, la regla es lo suficientemente granular como para permitir la ejecución de APIs de alto nivel (más seguras) estandarizadas por nuestro ecosistema.

**Motivo / criterio:** *Shift-Left Security y Principio de Menor Privilegio*. Bloquear proactivamente el uso de APIs propensas a configuraciones frágiles o inseguras obliga a mantener el estándar seguro en todo el orquestador. Las pruebas del Chaos Monkey siguen demostrando su enorme valor al forzar la evolución del linter.

**Siguiente paso o deuda:** Ejecutar `merci total` para certificar que ningún script legítimo del repositorio se ve afectado por la nueva regla restrictiva, y realizar el commit atómico.