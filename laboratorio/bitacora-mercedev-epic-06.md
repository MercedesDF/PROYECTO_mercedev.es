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

### 2026-05-23 — Sec: Extensión de validación AST en auditor Python (Chaos Monkey)

**Contexto:** Un simulacro de seguridad del Agente Chaos reveló que ciertas invocaciones a funciones de sistema de bajo nivel en Python estaban evadiendo los escudos estáticos, representando un riesgo potencial de ejecución no deseada si eran inyectadas en el ecosistema.

**Hecho:** Se implementó y extendió la regla `audit_python_smells` en `scripts/merci/merci-audit.py`.

**Detalle técnico:** La validación ahora parsea el Árbol de Sintaxis Abstracta (AST) para detectar el uso de funciones de sistema (`system`, `eval`, `exec`) y llamadas a subprocesos de bajo nivel (`Popen`). Su uso detiene automáticamente el pipeline. Simultáneamente, la regla es lo suficientemente granular como para permitir la ejecución de APIs de alto nivel (más seguras) estandarizadas por nuestro ecosistema.

**Motivo / criterio:** *Shift-Left Security y Principio de Menor Privilegio*. Bloquear proactivamente el uso de APIs propensas a configuraciones frágiles o inseguras obliga a mantener el estándar seguro en todo el orquestador. Las pruebas del Chaos Monkey siguen demostrando su enorme valor al forzar la evolución del linter.

**Siguiente paso o deuda:** Ejecutar `merci total` para certificar que ningún script legítimo del repositorio se ve afectado por la nueva regla restrictiva, y realizar el commit atómico.