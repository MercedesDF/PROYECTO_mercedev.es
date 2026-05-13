# Bitácora del proyecto mercedev.es — Épica 3: DevRel & Observabilidad Avanzada

## Para qué sirve este archivo

Bitácora activa a partir del cierre de la Épica 2 (Orquestación con IA, sellada el 2026-05-13).
Registra exclusivamente las decisiones, experimentos y aprendizajes de la Épica 3 (DevRel & Observabilidad Avanzada) documentada en el `ROADMAP.md` maestro.

Los historiales anteriores viven en sus respectivas bitácoras (`bitacora-mercedev-epic-01.md` y `bitacora-mercedev-epic-02.md`).

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

### 2026-05-14 — Refactor: Reestructuración de bitácoras por Épicas

**Contexto:** Validar el autodescubrimiento del nuevo orquestador de commits tras dividir el historial en múltiples archivos de Épica y organizar la documentación de I+D.

**Hecho:** Se renombraron las bitácoras antiguas (`epic-01` y `epic-02`) y se creó esta nueva bitácora estructurada para la Épica 3. Se refactorizó `merci-commit.py` para usar `glob` en el autodescubrimiento.

**Motivo / criterio:** *Zero Maintenance y Clean DX*. Separar los logs por Épica evita archivos infinitos y saturación visual. Refactorizar el orquestador maestro para que detecte las bitácoras automáticamente previene la rotura de la automatización CI/CD local en el futuro.

### 2026-05-14 — Docs: Creación de la estantería SOS Terminal (Píldoras de Conocimiento)

**Contexto:** Registrar micro-lecciones y comandos de terminal críticos que no requieren el formato extenso de un cuadernillo, pero que son vitales para la resolución rápida de incidentes operativos.

**Hecho:** Se definió la nueva taxonomía `tema: "SOS Terminal"` en el Frontmatter de los artículos y se publicó el primer documento resolviendo la deriva del archivo `requirements.txt` en el repositorio público.

**Motivo / criterio:** *Knowledge Harvesting y Fricción Cero*. No toda la documentación debe ser un manual exhaustivo. Aislar los "comandos salvavidas" en su propia estantería dentro de *Art de Coté* acelera la respuesta ante crisis y mantiene la biblioteca libre de "ruido" táctico.
