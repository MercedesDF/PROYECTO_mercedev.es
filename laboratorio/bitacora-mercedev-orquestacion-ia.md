# Bitácora del proyecto mercedev.es - fase orquestación con ia

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

### 2026-05-06 — Docs: Alineación del CV Semántico con la identidad de Performance Engineer

**Contexto:** El currículum semántico (`/sobre-mi/index.html`) conservaba el copy anterior ("Arquitecta de Sistemas de IA") que resultaba ajeno a la nueva identidad profesional y restaba impacto visual a la frase clave "gobernar la incertidumbre".

**Hecho:**
- Se extrajo la frase clave a un `<h2>` independiente con la clase BEM `.hero__statement` (cursiva, `$color-text-base`).
- Se reescribió el primer párrafo del "CV Anti-ATS" para vincular la experiencia industrial de 20 años con el rigor del Performance Engineering.
- Se actualizó el objeto JSON-LD para reflejar los nuevos *skills* ("Spec as Source", "Web Performance").

**Motivo / criterio:** *Coherencia de Marca Personal*. El CV debe respirar el mismo aire empírico y analítico que LinkedIn y la Portada. Darle entidad de `<h2>` a la frase sobre la incertidumbre refuerza la tesis de madurez (Seniority) y crea una jerarquía visual más atractiva antes de entrar en los párrafos densos.

**Siguiente paso o deuda:** Iniciar la automatización e intercepción de errores en Python (Fase 1 de IA).

### 2026-05-06 — Docs: Pivote de identidad hacia Performance Engineering y Spec as Source

**Contexto:** El posicionamiento como "AI Systems Architect" no reflejaba con precisión el trabajo real y el inmenso valor demostrable del ecosistema actual (100/100 cuádruple en PageSpeed Insights, documentación exhaustiva y automatización DevSecOps). Se necesitaba un perfil más "vendible" y ajustado a la realidad técnica.

**Hecho:** Se actualizó `public/index.html` para reflejar el perfil de **Performance Engineer & Technical Writer**.

**Motivo / criterio:** *Authenticity & Market Fit*. "Spec as Source", las métricas de rendimiento perfectas y la trazabilidad documental (ADRs, bitácoras) son habilidades tangibles, raras y altamente demandadas. Presentarse con hechos empíricos (lo que ya se hace y se domina) proyecta mucha más autoridad que prometer orquestación de IA, la cual está apenas comenzando en el Roadmap.

**Siguiente paso o deuda:** Iniciar la automatización e intercepción de errores en Python (Fase 1 de IA).

### 2026-05-06 — Docs: Refinamiento del tono editorial en la portada

**Contexto:** El copy de la portada presentaba un tono demasiado agresivo ("La máquina ejecuta el código. Yo diseño el sistema.", "declaración de intenciones"), alejándose de la Guía de Voz equilibrada del proyecto.

**Hecho:** Se suavizó el `H1`, el subtítulo y la tarjeta "Anti-ATS" en `public/index.html`.

**Motivo / criterio:** *Brand Identity y Tono Editorial*. Mostrar autoridad técnica y *Seniority* no requiere un tono dictatorial ni beligerante. Un enfoque firme pero integrador ("Arquitectura de Sistemas y Orquestación de IA") transmite la misma capacidad técnica resultando mucho más accesible y corporativo para reclutadores o clientes.

**Siguiente paso o deuda:** Iniciar formalmente la Fase 1 del Roadmap de Orquestación de IA.
