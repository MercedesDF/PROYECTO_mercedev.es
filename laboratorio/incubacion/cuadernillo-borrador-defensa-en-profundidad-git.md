---
titulo: "Fix: Sincronización de DLP en .gitignore para docs/matriz"
descripcion: "Se añadió explícitamente el directorio 'docs/matriz/' al archivo '.gitignore' para evitar que Git rastreara los archivos automáticamente y bloqueara el pipeline por DLP."
tipo: "cuadernillo"
tema: "DevSecOps y Gobernanza"
fecha: "2026-05-10"
fase: "Épica 2 - Fase 3 (Orquestación de Contenidos)"
estado: "borrador"
alt_portada: "Esquema conceptual de la Defensa en Profundidad mostrando a Git como escudo pasivo y al Linter como escudo activo."
---

<!-- linkedin:
Se implementó una solución crítica para evitar bucles infinitos y fugas de datos en el flujo de trabajo del proyecto mercedev.es. Añadiendo explícitamente 'docs/matriz/' al archivo '.gitignore', se aseguró que Git no rastreara los archivos automáticamente, lo que permitió superar el bloqueo por DLP. #DevSecOps #Gobernanza
-->

## El Desafío (Síntoma)
Se detectó un fallo bloqueante en bucle con la carpeta privada `docs/matriz`. A pesar de purgar la caché de Git con `git rm --cached`, los archivos volvían a aparecer al hacer el siguiente `merci commit`, lo que provocaba que el Agente Auditor volviera a saltar bloqueando el pipeline por DLP.

## La Maniobra (Lógica)
Se añadió explícitamente el directorio `docs/matriz/` al archivo `.gitignore`. Esta acción aseguró que Git no rastreara los archivos automáticamente, lo que evitó que el linter `merci-audit.py` continuara bloqueando el pipeline con un error `BANNED_TRACKED_FILE`.

## El Aprendizaje / Deuda Técnica
Esta solución demuestra la importancia de la Defensa en Profundidad (Defense in Depth). El `.gitignore` es el escudo pasivo que evita que los archivos sean rastreados accidentalmente, mientras que el linter es el escudo activo que detecta y bloquea posibles fugas de datos. Es crucial que ambos trabajen en tándem para evitar ciclos infinitos de falsos positivos y garantizar la seguridad del flujo de trabajo.