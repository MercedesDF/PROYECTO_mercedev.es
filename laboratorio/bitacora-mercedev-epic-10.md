# Bitácora - Épica 10: Orquestación Zero-Bloat con Antigravity IDE (Agentes y Skills)

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

### 2026-09-04 - Saneamiento de vulnerabilidades (Dependabot)

**Contexto:** Al subir el código a GitHub, Dependabot interceptó la subida alertando de 16 vulnerabilidades (CVEs) críticas y altas en las dependencias locales (`litellm`, `pillow`, `weasyprint`).

**Hecho:** 
- Se desanclaron las versiones estrictas (`==`) en `requirements.txt` reemplazándolas por `>=`.
- Se forzó la actualización del entorno virtual para descargar los parches de seguridad.

**Detalle técnico:** 
- Archivo editado: `requirements.txt`
- Comandos: `pip install --upgrade -r requirements.txt`

**Motivo / criterio:** Sanear la cadena de suministro (Supply Chain) y mantener el entorno local seguro antes de iniciar el diseño de los nuevos agentes.

**Siguiente paso o deuda:** Finalizar este parche de seguridad y comenzar con el diseño de la topología de agentes (Fase 1).

---



### 2026-09-04 - Inicio de Épica 10 y Revisión Documental

**Contexto:** Arranque formal de la Épica 10 centrada en la reconversión del ecosistema hacia el modelo de Inteligencia Artificial basado en agentes de Antigravity IDE.

**Hecho:** 
- Se inicializó la bitácora cronológica y se revisaron las directrices en `instrucciones.md`.
- Se validó y adaptó la estructura de la Épica 10 en `ROADMAP.md` a la filosofía Zero-Bloat.
- Se definió la integración arquitectónica de los agentes con Python.

**Detalle técnico:** 
- Rutas editadas: `ROADMAP.md`, `laboratorio/bitacora-mercedev-epic-10.md`

**Motivo / criterio:** Asegurar el cumplimiento del protocolo de Gobernanza, la soberanía del Castellano y la redacción impersonal.

**Siguiente paso o deuda:** Diseñar la topología de agentes y desplegar la estructura `.agents/` en la raíz del espacio de trabajo (Fase 1).
