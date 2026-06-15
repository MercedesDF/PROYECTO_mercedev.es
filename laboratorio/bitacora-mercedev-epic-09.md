# Bitácora del proyecto mercedev.es — Épica 9: Antigravity SRE, Chaos Engineering & Refinamiento CSS

## Para qué sirve este archivo
Bitácora activa para registrar las decisiones, arquitectura y evolución técnica correspondientes a la Épica 9 del Roadmap maestro (Antigravity SRE, Chaos Engineering Avanzado y Refinamiento CSS).

---

## Registro cronológico

### 2026-06-15 — Investigación: Preservación de Herramientas Estériles (FFmpeg)

**Contexto (Desafío):**
Se necesitaba automatizar la purga de tiempos muertos ("congelación de terminal") en los vídeos de demostración del proyecto (showcase). Se experimentó con la vía de bajo nivel usando `FFmpeg` y el filtro `mpdecimate`.

**Hecho (Maniobra):**
- Se generó el script `scripts/temporales/merci-mpdecimate-fastforward.sh`.
- El script cumplió técnicamente su función de compresión extrema (de 272MB a 62MB), pero generó un efecto "Hyper-Timelapse" epiléptico inasumible para la visualización humana.
- Se experimentó alternativamente con `auto-editor` (Python) para recortar fotogramas inactivos manteniendo un "padding" humano (`--margin 0.5s`), pero el intento falló debido a la falta de metadatos de fotogramas constantes (`time_base=0/0`, VFR) en la grabación de pantalla cruda.
- En lugar de desechar el código, se confinó en el nuevo directorio `scripts/temporales/` y se documentó explícitamente en su cabecera el motivo de su fracaso y las alternativas humanas recomendadas (CapCut, auto-editor), cumpliendo las normas de gobernanza.

**Motivo / criterio (Aprendizaje):**
Un script fracasado es una lección arquitectónica valiosa. Mantener el ecosistema Zero-Bloat también implica no saturar la carpeta principal de `scripts/` con utilidades estériles, derivándolas a un silo de cuarentena/histórico debidamente comentado.
## Notas Arquitectónicas

*(Espacio para documentar bloqueos o decisiones técnicas durante la ejecución de la épica).*
