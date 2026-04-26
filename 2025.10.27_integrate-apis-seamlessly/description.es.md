[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Cómo integrar APIs sin fricciones

## ¿De qué trata este post?

Una guía práctica para pasar de la depuración reactiva al diseño sistemático y anticipado en integraciones de APIs. El artículo original argumenta que la mayoría de los equipos descubren los modos de fallo (límites de tasa, expiración de tokens, cambios de esquema, orden de webhooks) recién en producción y después meten el manejo de errores con calzador. Propone usar Claude.ai para analizar autenticación, límites de tasa y casos límite por adelantado, y Claude Code para generar clientes tipados, flujos OAuth/JWT/rotación de claves y pruebas de contrato/refresco en todo tu repositorio.

## ¿Cuándo es útil?

- Vas a integrar una nueva API de terceros y necesitas una lista de modos de fallo antes de escribir código.
- Tu integración actual sufre incidentes 401/429/timeout y requieres un plan de mejora sistemático.
- Tienes que decidir entre webhooks o polling, o diseñar un cliente versionado que sobreviva a cambios de esquema.
- Quieres estandarizar cómo tu equipo usa Claude.ai (planificación) y Claude Code (implementación/tests/PRs).

## Puntos clave

- Claude.ai para planificar: pega la documentación de la API y pide "riesgos de integración ordenados por probabilidad" → umbrales de rate limit, headers requeridos, nullability de campos, idempotencia, jitter para 429.
- Claude Code para implementar: `npm install -g @anthropic-ai/claude-code` → `claude` → pide OAuth2 con refresco automático, validación de JWT, rotación de claves con monitoreo, y pruebas de contrato/refresco.
- Absorbe cambios de esquema con capas adaptadoras y clientes versionados; usa validación de esquema para detectar rupturas temprano.
- Decide webhooks vs polling según latencia, volumen e infraestructura; las estrategias híbridas son válidas.
- Despliega con Claude Code: `> Commit these API changes and open a PR` genera mensajes de commit y descripciones de PR vinculando cambios y tests.

## Recursos incluidos

- [skills/api-integration-resilience-playbook/SKILL.md](./skills/api-integration-resilience-playbook/SKILL.md): playbook de planificación + implementación con prompts.
- [templates/risk-discovery-prompt.md](./skills/api-integration-resilience-playbook/templates/risk-discovery-prompt.md): prompt reutilizable para listar modos de fallo.
- [templates/auth-implementation-prompt.md](./skills/api-integration-resilience-playbook/templates/auth-implementation-prompt.md): prompt para OAuth2 / JWT / rotación de claves.
- [references/failure-mode-catalog.md](./skills/api-integration-resilience-playbook/references/failure-mode-catalog.md): catálogo de modos de fallo del post.
- [examples/example-prompts.md](./skills/api-integration-resilience-playbook/examples/example-prompts.md): prompts de Claude.ai/Claude Code tal como aparecen en el post.
- [guides/integration-planning-workflow.es.md](./guides/integration-planning-workflow.es.md) (+ en/ko/ja): flujo de trabajo de planificación paso a paso.

## Fuente

Basado en [How to integrate APIs seamlessly](https://claude.com/blog/integrate-apis-seamlessly) (publicado el 2025-10-27).
