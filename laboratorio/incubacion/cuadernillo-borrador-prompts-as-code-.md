---
titulo: "Refactorización de System Prompts a Archivos Markdown"
descripcion: "Se centralizan las instrucciones de la IA en archivos Markdown para mejorar la Separación de Responsabilidades y facilitar la gestión del ecosistema de IA."
tipo: "cuadernillo"
tema: "DevSecOps y Gobernanza"
fecha: "2026-05-10"
fase: "Épica 2 - Fase 3 (Orquestación de Contenidos)"
estado: "borrador"
alt_portada: "Refactorización de System Prompts a Archivos Markdown para una gestión más limpia y auditable del ecosistema de IA."
---

<!-- linkedin:
Refactorización completa de los System Prompts a archivos Markdown para una gestión más limpia y auditable del ecosistema de IA. #DevSecOps #GobernanzaTecnica
-->

## El Desafío (Síntoma)
Se detectó que los System Prompts de la IA estaban hardcodeados dentro de las entrañas de los scripts de Python como `merci-ssot.py` y `merci-brain.py`. Esto ensucia el código y viola el principio de Separación de Responsabilidades.

## La Maniobra (Lógica)
Se abstraieron las instrucciones de la IA a archivos Markdown puros en la carpeta `laboratorio/prompts/` (por ejemplo, `prompt-ssot.md`, `prompt-brain.md`). Ahora se tratan los prompts como reglas de negocio o configuración, no como lógica de ejecución de Python, centralizando toda la 'psicología' del ecosistema de IA en un solo directorio auditable.

## El Aprendizaje / Deuda Técnica
Se aprendió que la Separación de Responsabilidades es crucial para mantener el código limpio y fácilmente mantenible. Se asumió una pequeña deuda técnica en la necesidad de actualizar los scripts para leer las instrucciones desde los archivos Markdown, pero esto facilita la gestión del ecosistema de IA y mejora su audibilidad.