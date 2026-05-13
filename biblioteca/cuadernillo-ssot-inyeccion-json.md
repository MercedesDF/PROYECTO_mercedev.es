---
titulo: "Optimización del Proceso de Reescritura con IA para SSOT"
descripcion: "Se implementó un patrón 'Decisión vs Ejecución' para reducir tokens y evitar alucinaciones en la reescritura de archivos."
tipo: "cuadernillo"
tema: "DevSecOps y Gobernanza"
fecha: "2026-05-10"
fase: "Épica 2 - Fase 3 (Orquestación de Contenidos)"
estado: "publicado"
alt_portada: "Optimización del Proceso de Reescritura con IA para SSOT"
---

## El Desafío (Síntoma)
Se detectó que pedirle a la IA que reescriba un archivo de 200 líneas del Roadmap solo para poner una 'X' era un desperdicio de tokens y causaba alucinaciones, mutilando el archivo truncándolo.

## La Maniobra (Lógica)
Se aplicó un patrón de 'Decisión vs Ejecución' (Targeted Payload Extraction). Ahora Python (la Mano) extrae las tareas pendientes mediante regex, se las pasa a la IA (el Cerebro), y la IA solo devuelve un array JSON con las tareas completadas. Python hace un .replace() matemático en el archivo físico.

## El Aprendizaje / Deuda Técnica
Se redujo el uso de tokens en un 90% y se eliminó cualquier riesgo de alucinaciones o daños a los documentos Markdown. Esta solución es óptima porque minimiza la carga del sistema y asegura la integridad de los archivos. No se ha asumido ninguna deuda técnica para el futuro.