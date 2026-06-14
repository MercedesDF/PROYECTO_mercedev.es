---
titulo: "Out-of-the-Box Experience: Placeholders Anti-403 y Marca Blanca"
descripcion: "Cómo garantizar una demostración impecable de un Boilerplate purgado inyectando plantillas de contingencia con layout heredado."
tipo: "cuadernillo"
tema: "DevSecOps e Infraestructura"
subtema: "Gobernanza"
fecha: "2026-05-23"
fase: "Epic 5 - Fase 1"
estado: "publicado"
alt_portada: "Esquema conceptual de una carpeta vacía que proyecta un holograma de una página web completa."
---
## El Desafío (Síntoma)
Tras ejecutar la instanciación destructiva (`merci-init.py`) para purgar la propiedad intelectual de la matriz, directorios como `/blog` o `/biblioteca` quedaban vacíos. Esto provocaba que, al navegar por el Showcase público, el servidor Nginx devolviera un hostil `403 Forbidden` al no encontrar un archivo `index.html` inicial, arruinando la "Out-of-the-Box Experience" (OOBE). Además, el avatar del asistente conservaba enlaces a los perfiles sociales de la autora original.

## La Maniobra (Lógica)
Se dotó al instanciador de la capacidad de inyectar "Placeholders anti-403". El script lee el `index.html` principal, recorta los bloques estructurales (`<header>` y `<footer>`) y genera páginas de contingencia estáticas dentro de las carpetas vaciadas. Paralelamente, se aplicó una función de anonimización para sustituir los enlaces de LinkedIn y GitHub por URLs genéricas en el código de la UI.

## El Aprendizaje / Deuda Técnica
Un Boilerplate Open Source debe sentirse como un producto terminado desde el milisegundo cero, incluso estando vacío de contenido. Suplir la falta de información con plantillas dinámicas que heredan la navegación global retiene al usuario dentro de la demostración en lugar de expulsarlo. Anonimizar explícitamente el proyecto protege la privacidad sin destruir los componentes interactivos.

## En resumen
Al vaciar la plantilla de datos personales para hacerla pública, los menús de la web llevaban a páginas de error vacías y "rotas". En lugar de dejarlo así, se le enseñó al sistema a crear automáticamente páginas temporales de "Próximamente" que mantienen el mismo menú y diseño del resto de la web. Así, quien pruebe la plantilla podrá navegar sin tropezarse con errores técnicos.

<!-- linkedin:
El primer contacto de un desarrollador con tu framework define si lo adopta o lo descarta. Entregar un ecosistema con enlaces rotos es un antipatrón en la "Out-of-the-Box Experience" (OOBE). 🚀

Al instanciar y limpiar el Boilerplate de mercedev.es para su demostración pública, los directorios vaciados devolvían errores 403. Para remediarlo de forma elegante, se automatizó la inyección de plantillas Anti-403: páginas de contingencia que heredan dinámicamente el layout (menús y footer) de la web.

Se ha logrado entregar una demostración vacía pero interactiva y 100% navegable.

La usabilidad no empieza cuando se añade contenido; empieza en el manejo de los estados vacíos.

#DevSecOps #DeveloperExperience #ArquitecturaSoftware #mercedev.es
-->