# 🗺️ ROADMAP: AI ORCHESTRATION & SELF-HEALING SYSTEM

Este roadmap marca la evolución de mercedev.es de un sitio estático a una plataforma orquestada por IA.  

## Fase 1: Cimientos y Conectividad (Semanas 1-2)

- [x] Setup de Modelos (Hybrid Stack): Configurar Ollama para ejecución local y LiteLLM para fallback con Gemini Flash API.

- [x] Directorio del Cerebro: Crear /merci-brain para centralizar los agentes de Python.

- [x] Estandarización de Prompts: Crear /laboratorio/prompts con las reglas de estilo y arquitectura para que las IAs mantengan la coherencia del repo.  

## Fase 2: El Agente Auditor (Self-Healing Base) (Semanas 3-4)

- [x] Evolución de merci-audit.py: Integrar IA para que el script no solo detecte errores, sino que sugiera el comando de reparación.  

- [x] IA-Fix Workflow: Crear GitHub Action que dispare una corrección automática de IA ante fallos del linter utilizando el *Hybrid Stack*.  

- [x] WebP Automation: Implementar agente que vigile /.assets-raw y convierta automáticamente cualquier subida a .webp optimizado.  

## Fase 3: Orquestación de Contenidos y Docs (Semanas 5-6)

- [ ] Agente Bibliotecario: Automatizar la creación de cuadernillos en /biblioteca a partir de notas rápidas en Markdown.  

- [ ] Sync SSOT (Single Source of Truth): Agente que verifique que el README.md y los /docs están siempre sincronizados tras cada cambio de código.  

- [ ] AI-Changelog: Generación automática de historial de cambios realizados por agentes en /docs/CHANGELOG_AI.md.

- [ ] **Pipeline WP → LinkedIn (Automatización Social):** Conectar `merci-wp.py` con `merci-linkedin.py` para que al publicar o actualizar un post en WordPress con `estado: "publicado"`, se dispare automáticamente la publicación del anuncio en LinkedIn. El bloque `<!-- linkedin: -->` del Frontmatter ya contiene el texto del anuncio; el agente debe leerlo y enviarlo sin intervención manual. Prerequisito: revisar el estado del token OIDC (OpenID Connect) almacenado en `.linkedin_token.json` y su caducidad.

## Fase 4: Observabilidad y SRE IA (Semanas 7-8)

- [ ] Dashboard de Confianza: Implementar Grafana para visualizar cuántos cambios de IA han sido aprobados vs. rechazados.

- [ ] Chaos Engineering con IA: Script que use la IA para simular fallos en el merci-boilerplate y verificar que el sistema de rollback funciona.  

- [ ] Hardening Automation: Agente que audite el cumplimiento de la docs/checklist-hardening.md de forma continua.

- [ ] **Evaluación de Tienda WooCommerce (Deuda Fase 4.3):** Estudiar la viabilidad de activar WooCommerce más allá del modo catálogo actual. Evaluar: pasarela de pago compatible con la arquitectura (sin degradar Core Web Vitals), impacto en CSP (Content Security Policy), y si el volumen de productos justifica la complejidad operativa. Decisión de arquitectura previa obligatoria antes de cualquier implementación.

# 🛠️ STACK TECNOLÓGICO DEL ROADMAP

- Orquestador: Python 3.10+ (Framework: LangChain / LiteLLM).  

- Modelos: Llama 3 (Local) & Gemini Flash (Cloud).

- CI/CD: GitHub Actions (custom workflows).

- Infra: Docker Compose + Digital Ocean Droplet.