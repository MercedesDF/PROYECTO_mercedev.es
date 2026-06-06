---
titulo: "Automatización Extendida: Compilador Data-Driven para la Biblioteca"
descripción: "Evolución del agente autónomo hacia una arquitectura JSON (SSOT) para la compilación determinista del conocimiento."
estado: "publicado"
estado_social: "aprobado"
orden_social: 1
tema: "Blog"
fase: "Epic 3 - Fase 2"
fecha: "2026-05-21"
descripcion: "Evolución del agente autónomo hacia una arquitectura JSON (SSOT) para la compilación determinista del conocimiento"
---
<!-- linkedin:
Dejar que una Inteligencia Artificial edite directamente los archivos en producción es una receta garantizada para el desastre visual. En la arquitectura de mercedev.es, se detectó que el agente autónomo rompía ocasionalmente la página del glosario técnico debido a "alucinaciones de formato".

Para solucionarlo, se retiró a la IA el acceso al Markdown, obligándola a guardar los términos en un diccionario de datos (JSON) estricto. Ahora, el sistema actúa como una imprenta mecánica: lee ese diccionario seguro y fabrica la página perfecta y ordenada desde cero en cada actualización, haciendo matemáticamente imposible que un error de la IA rompa el diseño de la web.

⚙️ Una aproximación "Data-Driven" que aísla el estado del código final.

#DevSecOps #InteligenciaArtificial #mercedev.es
-->

Al diseñar la arquitectura del CMS Headless en mercedev.es, surgió un problema recurrente: el Agente Autónomo del glosario extraía e inyectaba nuevas definiciones técnicas directamente en el archivo Markdown (`glosario-tecnico.md`). Sin embargo, esto planteaba dos desafíos significativos:

1. **Fragilidad de Formato:** A pesar de los Prompts estrictos utilizados por la IA, ocasionalmente se producían errores visuales como `**Término**` en lugar de `### Término`. Un simple error tipográfico podía romper la visualización del documento.

2. **Desalineación Filosófica:** El glosario Markdown estaba siendo tratado como una base de datos cuando, en realidad, en un ecosistema SSG (Static Site Generator), la *Única Fuente de Verdad* es la bitácora de documentación. El glosario no debe ser un documento de trabajo, sino un *Art de Coté* (artefacto compilado).

Para resolver estos problemas, se decidió refactorizar el script `merci-glosario.py`, abandonando la inyección directa en Markdown y adoptando un enfoque **Data-Driven (Basado en JSON)**. Este cambio permitió:

1. **Estado JSON Maestro:** Se extrajo el histórico completo del glosario hacia un nuevo archivo `glosario-tecnico.json`. Este JSON almacena los términos, definiciones, el registro de archivos origen y una *lista negra* de términos descartados.

2. **IA Determinista:** Se configuró el cliente HTTP para requerir explícitamente `format: "json"` a la API de Ollama. La IA ahora no devuelve texto libre, sino un objeto estructurado predecible e imposible de romper visualmente.

3. **Compilación Dinámica (Build-Time):** El script ahora opera como un compilador, sincronizando los nuevos términos con el JSON y generando y sobrescribiendo el archivo `glosario-tecnico.md` desde cero cada vez que se ejecuta el pipeline (`merci-total.py`). Esto garantiza que el artefacto resultante esté matemáticamente ordenado (alfabéticamente) y formateado de forma impecable.

La refactorización del enfoque mostró varios beneficios significativos:

*   **JSON sobre Markdown para Agentes:** Cuando un Agente Autónomo tiene permisos de escritura continua, el formato de almacenamiento de estado debe ser estricto (JSON o Base de Datos). Dejar que un LLM manipule código Markdown interactivo o en bruto introduce Deuda Técnica impredecible.
*   **Aislamiento del Origen:** Consolidar el paradigma de que "los archivos .md finales son de solo lectura (compilados)" simplifica el mantenimiento. Si el Markdown se corrompe por acción humana, la próxima ejecución del Build lo restaurará instantáneamente desde el JSON.

Antes, la Inteligencia Artificial escribía el diccionario técnico directamente sobre la página final, causando errores visuales si se equivocaba con el formato o la puntuación. Para solucionarlo, ahora la IA guarda las definiciones en un "cajón de datos" estructurado e invisible. Luego, el sistema actúa como una imprenta mecánica: coge esos datos seguros y fabrica la página perfecta y ordenada alfabéticamente desde cero cada vez. Así se asegura de que el resultado nunca se rompa visualmente, por mucho que la IA falle.

Para obtener más detalles sobre esta evolución en el proceso de automatización,leer el [cuadernillo completo](/biblioteca/automatizacion-extendida-compilador-data-driven-para-la-biblioteca.html).