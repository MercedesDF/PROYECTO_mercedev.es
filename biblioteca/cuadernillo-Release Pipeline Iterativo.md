---
titulo: "Release Pipeline Iterativo: Agile en despliegue de plantillas"
descripcion: "Cómo gobernar la actualización de un Boilerplate desde un proyecto matriz sin sufrir Deriva de Configuración."
tipo: "cuadernillo"
tema: "DevSecOps e Infraestructura"
subtema: "Gobernanza"
fecha: "2026-04-27"
fase: "Epic 1 - Fase 8"
estado: "publicado"
alt_portada: "Diagrama de flujo circular mostrando la clonación, instanciación, auditoría y retroalimentación hacia el proyecto matriz."
---

## El Desafío (Síntoma)
Al extraer un ecosistema base (Merci Boilerplate) a partir de un proyecto vivo (`mercedev.es`), surge el riesgo de la **Deriva de Configuración (Configuration Drift)**. Cuando se detecta un error en la plantilla exportada, el instinto natural del desarrollador es corregirlo directamente en el repositorio hijo. Esto provoca que el proyecto matriz y la plantilla se desincronicen de forma silenciosa, convirtiendo el mantenimiento a largo plazo en una deuda técnica insostenible.

## La Maniobra (Lógica)
Se estableció un **Release Pipeline Iterativo** basado en principios Agile y de Única Fuente de Verdad (SSOT - Single Source of Truth). El protocolo innegociable para cada subida de versión es:

1. **Clonación efímera:** Se clona la matriz en un directorio temporal y se ejecuta la purga de identidad y binarios (`merci-init.py`).
2. **Despliegue Ágil:** Se copian los archivos al repositorio destino mediante `rsync` (excluyendo historiales Git y metadatos documentales propios).
3. **QA Fail-Fast:** Se ejecuta el orquestador maestro (`merci-total`) en el destino.
4. **Iteración estricta:** Si existe el más mínimo fallo, se destruye el clon temporal, se aplica la corrección obligatoriamente en el **proyecto matriz** (`mercedev.es`) y se reinicia el ciclo desde el paso 1.

## El Aprendizaje / Deuda Técnica
Gobernar infraestructuras como código exige disciplina arquitectónica. Arreglar bugs directamente en artefactos derivados (forks o plantillas exportadas) es un antipatrón. Forzar la resolución de problemas exclusivamente en el entorno anfitrión garantiza que toda mejora o parche beneficie simultáneamente a la web en producción y a la plantilla, consolidando el proyecto matriz como la verdadera única fuente de verdad.