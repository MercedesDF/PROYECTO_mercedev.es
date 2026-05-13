---
titulo: "Encadenamiento de Agentes para Automatizar la Promoción de Documentos Técnicos"
descripcion: "Se implementó un flujo automatizado que permite al Bibliotecario crear y promocionar documentos técnicos sin intervención manual del Blogger."
tipo: "cuadernillo"
tema: "DevSecOps y Gobernanza"
fecha: "2026-05-13"
fase: ""
estado: "incubacion"
alt_portada: "Diagrama de flujo que muestra el encadenamiento de agentes para la creación y promoción automática de documentos técnicos."
---

## El Desafío (Síntoma)
El flujo de creación de contenido estaba fragmentado. El Bibliotecario creaba el documento técnico, pero había que invocar manualmente al Blogger para la promoción, y este no sabía qué URL tendría el documento final.

## La Maniobra (Lógica)
Implementamos Agent Chaining (Encadenamiento de Agentes). Ahora el Bibliotecario, al terminar, pregunta si quieres invocar al Blogger. Si aceptas, le pasa el archivo por argumento. El Blogger lee el YAML, deduce la URL final (slugify) e inyecta la directiva para que la IA la incluya en el post promocional.

## El Aprendizaje / Deuda Técnica
Encadenar agentes locales reduce la fricción operativa a cero. Cada IA hace solo una tarea bien definida, pasándose el contexto y el control de forma programática mediante Python.