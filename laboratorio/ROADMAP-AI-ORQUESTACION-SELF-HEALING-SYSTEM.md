# 🗺️ ROADMAP: AI ORCHESTRATION & SELF-HEALING SYSTEM

## Fase 1: Cimientos y Conectividad 

- [x] 🔴 Setup de Modelos (Hybrid Stack): Configurar Ollama para ejecución local y LiteLLM para fallback con Gemini Flash API.
- [x] Directorio del Cerebro: Crear /merci-brain para centralizar los agentes de Python.
- [x] Estandarización de Prompts: Crear /laboratorio/prompts con las reglas de estilo y arquitectura para que las IAs mantengan la coherencia del repo.

## Fase 2: El Agente Auditor (Self-Healing Base) 

- [x] Evolución de merci-audit.py: Integrar IA para que el script no solo detecte errores, sino que sugiera el comando de reparación.
- [x] IA-Fix Workflow: Crear GitHub Action que dispare una corrección automática de IA ante fallos del linter utilizando el *Hybrid Stack*.
- [x] WebP Automation: Implementar agente que vigile /.assets-raw y convierta automáticamente cualquier subida a .webp optimizado.

## Fase 3: Orquestación de Contenidos y Docs

- [x] 🔴 Agente Bibliotecario (deprecado): Automatizar la creación de cuadernillos en /biblioteca a partir de notas rápidas en Markdown.
- [x] Sync SSOT (relegado a Cloud puro): Agente que verifique que el README.md y los /docs están siempre sincronizados tras cada cambio de código.
- [x] AI-Changelog (descartado por límites cognitivos locales): Generación automática de historial de cambios realizados por agentes en /docs/CHANGELOG_AI.md.
- [x] Pipeline WP → LinkedIn (Automatización Social): Conectar `merci-wp.py` con `merci-linkedin.py` para que al publicar o actualizar un post en WordPress con `estado: "publicado"`, se dispare automáticamente la publicación del anuncio en LinkedIn. El bloque `<!-- linkedin: -->` del Frontmatter ya contiene el texto del anuncio; el agente debe leerlo y enviarlo sin intervención manual. Prerequisito: revisar el estado del token OIDC (OpenID Connect) almacenado en `.linkedin_token.json` y su caducidad.

## Fase 4: Observabilidad y SRE IA

- [ ] Dashboard de Confianza: Implementar Grafana para visualizar cuántos cambios de IA han sido aprobados vs. rechazados.
- [ ] Chaos Engineering con IA: Script que use la IA para simular fallos en el merci-boilerplate y verificar que el sistema de rollback funciona.
- [ ] Hardening Automation: Agente que audite el cumplimiento de la docs/checklist-hardening.md de forma continua.
- [ ] **Evaluación de Tienda WooCommerce (Deuda Fase 4.3):** Estudiar la viabilidad de activar WooCommerce más allá del modo catálogo actual. Evaluar: pasarela de pago compatible con la arquitectura (sin degradar Core Web Vitals), impacto en CSP (Content Security Policy), y si el volumen de productos justifica la complejidad operativa. Decisión de arquitectura previa obligatoria antes de cualquier implementación.

---

Este es el Roadmap actualizado basado en los últimos avances descritos en la Bitácora.
