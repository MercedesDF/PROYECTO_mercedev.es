---
tema: "DevSecOps y Gobernanza"
estado: "incubacion"
---

# Ideación de Proyectos Futuros (Spin-offs de Merci)

Este documento sirve como contenedor de ideas para futuros proyectos que hereden la filosofía *Zero-Bloat*, *Shift-Left AI* y *Spec-Driven Development* de `mercedev.es`, pero que vivirán en repositorios independientes.

## 1. El Gemelo Digital de Infraestructura (IoT / HomeLab SRE)
Evolucionar los agentes SRE (`merci-sre.py`) para monitorizar hardware físico (Raspberry Pi, servidores) o domótica. El frontend sería un SVG/CSS ultraligero (Vanilla JS) que refleja el estado de los sensores en tiempo real sin requerir nubes de terceros (Local-First).

## 2. Empaquetado de "Merci CLI" (DevSecOps Framework)
Extraer los 25+ agentes de la carpeta `scripts/merci/` y convertirlos en un paquete oficial de Python (`pip install merci-core`). Permitiría a cualquier usuario de la comunidad aplicar auditorías, Chaos Engineering y orquestación SSOT en sus propios repositorios de forma agnóstica.

## 3. Cerebro Local (Personal Knowledge Management - PKM)
Un gestor de notas en terminal que utiliza Ollama (RAG / Embeddings locales) para vigilar una carpeta de Markdown, conectando conceptos automáticamente e inyectando enlaces cruzados entre notas históricas y nuevas sin usar interfaces gráficas pesadas (como Obsidian o Notion).

---
**Motivo de este registro:**
Evitar la pérdida de ideas arquitectónicas (Knowledge Harvesting) mientras se mantiene el enfoque táctico en el proyecto actual (`mercedev.es`). Cuando se inicie un nuevo repositorio, este documento podrá servir como manifiesto fundacional.