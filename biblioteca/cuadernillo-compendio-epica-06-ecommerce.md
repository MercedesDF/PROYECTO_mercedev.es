---
titulo: "Compendio Estratégico: E-commerce Híbrido Extremo (Zero-JS)"
descripcion: "Resumen arquitectónico de la Épica 6: Inyección Headless de catálogo y Carrito Zero-JS con TBT 0ms."
estado: "publicado"
tema: "DevSecOps y Gobernanza"
alt_portada: "Esquema conceptual de la integración Headless de WooCommerce con un frontend estático"
fase: "Epic 6 - Fase 1"
fecha: "2026-05-26"
---
# Compendio Estratégico: E-commerce Híbrido Extremo (Zero-JS)

## El Desafío
Integrar un motor de comercio electrónico pesado (WooCommerce) en una arquitectura orientada al rendimiento extremo (100/100 Core Web Vitals), sin degradar el Tiempo de Bloqueo Total (TBT) y manteniendo la filosofía Headless para el catálogo de productos.

## La Maniobra
La Épica 6 abordó el reto a través de dos ejes arquitectónicos:

1. **Catálogo Headless (`merci-shop.py`):** Los productos se escriben en Markdown con metadatos YAML y se inyectan directamente vía API REST, tratando a WooCommerce como un simple motor de base de datos pasivo.
2. **Carrito Zero-JS:** Se desencolaron absolutamente todos los scripts AJAX (`wc-cart-fragments`), librerías de bloques Gutenberg y frameworks de React inyectados por las versiones modernas del CMS. Al aplicar auto-sanación en la base de datos (convirtiendo bloques a shortcodes clásicos), obligamos a WooCommerce a funcionar con peticiones `POST` HTML nativas.

## El Aprendizaje
El "Mejor código es el que no existe". Al obligar a WooCommerce a comportarse como una aplicación de los años 90 (recargando la página entera tras enviar un formulario POST en lugar de usar pesadas llamadas AJAX), eliminamos toda carga de procesamiento de JavaScript en el navegador del cliente. 

El resultado empírico es un TBT (Total Blocking Time) garantizado de 0ms, demostrando que es posible tener un e-commerce 100% funcional y ultrarrápido si se extirpa implacablemente la dependencia de JavaScript en el lado del cliente (Client-side rendering).