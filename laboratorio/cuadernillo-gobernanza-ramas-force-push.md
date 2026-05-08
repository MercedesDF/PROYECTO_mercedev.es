---
titulo: "Gobernanza de Ramas y la Tolerancia al Force Push"
descripcion: "Cómo conciliar la protección estricta de la rama principal con la necesidad arquitectónica de truncar historiales en repositorios derivados."
tema: "DevSecOps y Gobernanza"
fecha: "2026-05-08"
fase: "11 (CI/CD Cloud)"
estado: "borrador"
tipo: "cuadernillo"
alt_portada: "Representación de un escudo digital con una puerta trasera autorizada para el administrador."
---

## El Desafío (Síntoma)
Al implementar la infraestructura CI/CD (Continuous Integration / Continuous Deployment - Integración Continua / Despliegue Continuo) en GitHub, la plataforma alerta de que la rama `main` está desprotegida. Al intentar blindarla activando las reglas de protección estándar, GitHub bloquea por defecto las operaciones destructivas como `git push --force`. 

Esto genera una colisión arquitectónica grave con nuestro SOP (Standard Operating Procedure - Procedimiento Operativo Estándar) de Mantenimiento del Boilerplate. Nuestra estrategia de **Prevención de Fuga de Datos** exige el uso de Ramas Huérfanas y un *force push* explícito para truncar el historial inmutable de Git e impedir que la propiedad intelectual de la matriz se filtre a la plantilla pública.

## La Maniobra (Lógica)
Para proteger el repositorio cumpliendo con la gobernanza, pero manteniendo la capacidad operativa, se diseñó una regla de protección híbrida en los ajustes (Settings > Branches) del repositorio:

1. Se activó *Require a pull request before merging* (Requerir PR - Pull Request - Solicitud de Extracción) y *Require status checks to pass* para forzar que nuestro orquestador `merci-audit.py` valide siempre el código en la nube antes de cualquier fusión.
2. **La excepción calculada:** Se marcó explícitamente la casilla **Allow force pushes** (Permitir envíos forzados), restringiendo este privilegio única y exclusivamente a los administradores del repositorio.

## El Aprendizaje / Deuda Técnica
En DevSecOps, la seguridad estricta no debe bloquear la operatividad legítima de los mantenedores ni generar fricción en el despliegue de la infraestructura.

Las reglas de gobernanza "Out-of-the-Box" (listas para usar) están diseñadas para flujos de software tradicionales, donde reescribir la historia en `main` es un tabú. En una arquitectura de Boilerplates que requieren esterilización de historial, diseñar reglas de protección flexibles permite aplicar la guillotina temporal sin exponer el repositorio a contribuciones destructivas de terceros. 

*Toda excepción a una regla de seguridad estándar debe estar justificada y documentada para evitar el "Security Drift" (Deriva de Seguridad) por parte de futuros auditores.*