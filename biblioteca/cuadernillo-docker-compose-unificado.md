---
titulo: "Eliminación de la versión obsoleta en docker-compose.yml"
descripcion: "Se eliminó el atributo 'version' del archivo docker-compose.yml para alinear con las mejores prácticas de Docker Compose V2."
tipo: "cuadernillo"
tema: "DevSecOps y Gobernanza"
fecha: "2026-05-12"
fase: "Epic 2 - Fase 4"
estado: "publicado"
alt_portada: "Eliminación del atributo 'version' en docker-compose.yml para alinear con las mejores prácticas de Docker Compose V2."
---

## El Desafío (Síntoma)
Se detectó que el archivo `docker-compose.yml` lanzaba un warning advirtiendo que el atributo `version` está obsoleto. Antiguamente los archivos docker-compose.yml llevaban una cabecera como `version: '3.8'`, pero ahora las versiones modernas del motor usan la Especificación Unificada de Compose por defecto y ya no es necesario declararlo.

## La Maniobra (Lógica)
Se eliminó el atributo `version` del archivo `docker-compose.yml`. Se realizó una revisión del archivo para asegurar que no quedaran referencias a versiones obsoletas. El cambio se implementó en la rama principal del repositorio y se ejecutó un `git commit` con el mensaje "Eliminación del atributo 'version' en docker-compose.yml".

## El Aprendizaje / Deuda Técnica
Se aprendió que es importante mantener los archivos de configuración limpios y alineados con las mejores prácticas. La eliminación del atributo `version` no afectó la funcionalidad del archivo, pero sí mejoró la legibilidad y la mantenibilidad del mismo. No se asumió ninguna deuda técnica para el futuro.