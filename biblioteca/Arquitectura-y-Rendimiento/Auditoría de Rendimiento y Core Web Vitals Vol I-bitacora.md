---
titulo: "Auditoría de Rendimiento y Core Web Vitals Vol I"
descripcion: "Análisis de las métricas de Google PageSpeed Insights y cómo la arquitectura del Merci Boilerplate logra una puntuación de 100/100."
tipo: "bitacora"
tema: "Arquitectura y Rendimiento"
volumen: 1
fecha: "2026-04-21"
estado: "publicado"
portada: "portada-auditoria.webp"
alt_portada: "Gráfico de puntuación 100 sobre 100 en todas las métricas de Google PageSpeed Insights."
---

Este documento explica el significado de las métricas de Google PageSpeed Insights y cómo la arquitectura del "Merci Boilerplate" logra una puntuación perfecta de **100/100** en todas las categorías.

## 1. Rendimiento (Performance)
Mide la velocidad real a la que el usuario percibe que la página carga y reacciona. Se basa en los **Core Web Vitals** (Métricas Web Principales).

*   **LCP (Largest Contentful Paint - Despliegue del Contenido Más Extenso):** Mide cuánto tarda en pintarse el elemento más grande visible (como el texto del Hero o el Logotipo). 
    *   *Cómo sacamos 100:* Al no tener JavaScript bloqueante en la cabecera (usamos el atributo `defer`) y compilar un CSS ultraligero sin frameworks (SASS 7-1), el navegador pinta el LCP casi instantáneamente.
*   **INP (Interaction to Next Paint - Interacción hasta el Siguiente Pintado):** Mide la latencia de respuesta cuando el usuario hace clic o toca la pantalla.
    *   *Cómo sacamos 100:* Al programar el menú en Vanilla JS (JavaScript puro) en lugar de React o jQuery, el hilo principal del procesador siempre está libre para responder al instante. Además, en WooCommerce desactivamos el pesado script `wc-cart-fragments` basado en AJAX (Asynchronous JavaScript and XML - JavaScript Asíncrono y XML).
*   **CLS (Cumulative Layout Shift - Cambio Acumulativo de Diseño):** Mide cuánto "salta" la página mientras se cargan los elementos.
    *   *Cómo sacamos 100:* En nuestro HTML, a cada imagen (como el logotipo) le asignamos atributos explícitos `width` y `height`. El navegador reserva el hueco exacto antes de descargar la imagen, evitando saltos visuales.

## 2. Accesibilidad (Accessibility)
Mide si el sitio es navegable por personas con discapacidades (ej. usuarios ciegos que usan lectores de pantalla).

*   *Cómo sacamos 100:* 
    *   Usamos **HTML5 Semántico** estricto (`<header>`, `<main>`, `<section>`, `<nav>`, `<article>`).
    *   Mantuvimos un contraste de color muy alto (texto muy oscuro sobre fondo claro o naranja vibrante).
    *   A los botones sin texto visible (como la "hamburguesa" del menú móvil) les inyectamos etiquetas **WAI-ARIA** (Web Accessibility Initiative - Accessible Rich Internet Applications), específicamente `aria-label="Abrir menú"`, para que los lectores de pantalla sepan qué hace el botón.

## 3. Mejores Prácticas (Best Practices)
Audita la higiene del código, la seguridad moderna y el respeto por los estándares actuales de la W3C.

*   *Cómo sacamos 100:*
    *   **Imágenes Modernas:** Usamos el script `merci-optimizer.py` para convertir todo al formato de nueva generación `.webp`.
    *   **Seguridad:** Implementamos el certificado **SSL/TLS** (Let's Encrypt) forzando HTTPS y añadimos una **CSP (Content Security Policy - Política de Seguridad de Contenidos)** en el `<head>` que bloquea inyecciones de código malicioso.
    *   **Código limpio:** Nuestro auditor (`merci-audit.py`) prohibió el uso de APIs obsoletas de JavaScript (como `eval()`) y atributos CSS en línea (`style="..."`).

## 4. SEO (Search Engine Optimization - Optimización para Motores de Búsqueda)
Verifica que las páginas estén perfectamente configuradas para que los robots de Google las entiendan, las clasifiquen y las posicionen.

*   *Cómo sacamos 100:*
    *   **Metadatos:** Cada página tiene un `<title>` único, una `<meta name="description">` clara y la etiqueta `<link rel="canonical">` para evitar penalizaciones por contenido duplicado.
    *   **Datos Estructurados:** Inyectamos el bloque **JSON-LD** (JavaScript Object Notation for Linked Data - Notación de Objetos JavaScript para Datos Enlazados), dándole a Google un mapa exacto de qué es cada página.
    *   **Rastreabilidad:** Generamos un `robots.txt` amigable y automatizamos la fecha de nuestro `sitemap.xml` gracias a `merci-sitemap.py`.

---

### Conclusión Arquitectónica

El "Merci Boilerplate" demuestra que el ecosistema dinámico (WordPress/WooCommerce) no es lento por naturaleza, sino por cómo se implementa habitualmente. 

Al aplicar el principio de **Aislamiento**, la carga dinámica se produce tras el escudo de rendimiento de un Child Theme desprovisto de estilos basura, mientras que Nginx sirve la frontera estática a velocidad de disco. El resultado es un producto digital indestructible y perfectamente optimizado.