---
titulo: "Automatización Extendida: Delegación del Glosario a IA Local"
descripcion: "Creación de un script y System Prompt para enriquecer iterativamente la Biblioteca con Ollama."
tipo: "cuadernillo"
tema: "Art de Coté"
fecha: "2026-05-20"
fase: "Épica 3 - Fase 2"
estado: "incubacion"
estado_social: "en_cola"
alt_portada: "Diagrama mostrando un script Python interactuando con un modelo local para añadir definiciones estructuradas a un documento."
---

<!-- linkedin:
¡La base de conocimiento de nuestro proyecto ahora tiene vida propia! 🧠 

Acabamos de implementar un flujo `merci-glosario-ai.py` que permite a nuestra IA local (Ollama) actuar como Arquitecto DevSecOps e inyectar nuevas definiciones directamente en el glosario técnico, manteniendo un estricto formato estandarizado. 

Cero fricción, cero alucinaciones y 100% código propio. Lee los detalles de la maniobra arquitectónica aquí:
https://mercedev.es/art-de-cote/automatizacion-extendida-delegacion-glosario-ia-local
-->

## El Desafío (Síntoma)

Tras extraer más de 1400 términos técnicos del análisis de las bitácoras del proyecto y consolidar los 80 conceptos DevSecOps más críticos en `glosario-tecnico.md`, se planteó el reto del mantenimiento. 

El glosario corría el riesgo de quedarse estático y obsoleto a medida que el proyecto avanzara y se introdujeran nuevas herramientas o filosofías. Extraer manualmente cada nuevo término y redactar su definición respetando los campos requeridos (inglés, español, definición técnica, referencias) presentaba un alto grado de fricción operativa, contraviniendo el principio *Zero-Friction*.

## La Maniobra (Lógica)

Se delegó la tarea de ampliación de la base de conocimiento a la inteligencia artificial local (Ollama) integrada en nuestro ecosistema "brain". La solución se compuso de dos artefactos:

1. **System Prompt Estricto (`prompt-glosario.md`):** Se definió un prompt con rol de "Arquitecto de Software Senior y Especialista DevSecOps". Este prompt restringe las respuestas a un formato Markdown rígido, prohibiendo al modelo añadir saludos, introducciones o "humo comercial".
2. **Script de Orquestación (`merci-glosario-ai.py`):** Un script temporal en Python que toma una lista de términos por argumento (`sys.argv`), lee el prompt del sistema y llama mediante subprocesos a la CLI de Ollama (ej. `qwen2.5-coder`). El script captura el *stdout* y realiza un anexo (*append-only*) directamente al final del archivo del glosario técnico.

## El Aprendizaje / Deuda Técnica

*   **Delegación Controlada:** Automatizar la creación de contenido es útil solo cuando la salida de la IA está matemáticamente constreñida. El uso de reglas *System Prompt* inflexibles ("NO añadas texto introductorio") garantiza que el texto generado sea 100% compatible con el parser estático (SSG) de la web.
*   **Deuda Técnica (Ordenación Automática):** Actualmente, el script añade los nuevos términos al final del archivo mediante *append*. Queda como mejora pendiente implementar una función en Python que, además de añadir el término, abra el `.md`, extraiga todos los bloques, los reordene alfabéticamente y sobrescriba el archivo para mantener la cohesión visual del glosario.

*Nota: Al ejecutar `merci publish`, este documento se compilará estáticamente en la ruta `/art-de-cote/` sin depender de WordPress.*
