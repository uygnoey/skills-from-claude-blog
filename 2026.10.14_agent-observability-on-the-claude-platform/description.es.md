[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
El anuncio de las trazas de OpenTelemetry (OTel) desde Claude Managed Agents, la Messages API y los SDK
de Claude en Claude Platform, para seguir cada paso de tus agentes en cualquier herramienta OTel.

## ¿Cuándo es útil?
- Cuando quieres visibilidad paso a paso de los agentes creados en Claude Platform.
- Al depurar pasos lentos o fallidos de un agente junto al resto de tu stack.
- Al convertir trazas de producción en evals o al medir el uso de tokens por equipo.

## Puntos clave
- Cada turno del agente, llamada al modelo y uso de herramientas (incluidas las llamadas a servidores
  MCP) llega como una traza OTel estándar con latencia, tokens e IDs.
- Las trazas siguen las convenciones semánticas GenAI de OpenTelemetry, de modo que los datos de Claude y
  de otros proveedores comparten herramientas y paneles. Las trazas de Claude Code y Cowork pueden ir al
  mismo sitio.
- La confianza crece con evidencia: revisa las trazas del agente y amplía su acceso a medida que demuestre
  ser fiable.
- Herramientas citadas: Grafana Cloud, Honeycomb, Sentry, Splunk (depuración); Arize AI, Braintrust,
  Datadog, Langfuse, LangSmith, New Relic, PostHog (evals y calidad); Databricks Unity Gateway (uso en la
  organización). Funciona con cualquier herramienta compatible con OTLP.
- Beta pública. Managed Agents y la Messages API necesitan un destino en Claude Console; los SDK exportan
  automáticamente.
- Testimonios de Foxglove, Ramp (Reflect redujo el uso de tokens un 10–20 % y aceleró las sesiones un 30 %
  en algunos agentes), Sterling Labs y un equipo de agentes contables.

## Recursos incluidos
- Skill: `agent-otel-tracing` — activar la exportación, elegir destino, acceso gradual, ciclo de mejora
  (`references/observability-tools.md`, `examples/customer-patterns.md`).

## Fuente
- https://claude.com/resources/articles/agent-observability-on-the-claude-platform
