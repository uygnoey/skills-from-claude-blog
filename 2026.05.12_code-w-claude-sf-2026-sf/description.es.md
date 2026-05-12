[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Code w/ Claude SF 2026: Construyendo sobre la exponencial de la IA

## ¿De qué trata este post?

Es el resumen del 12 de mayo de 2026 de Code w/ Claude SF, la conferencia anual de desarrolladores de Anthropic. El post anuncia que se duplican los rate limits de Claude Code, se elevan los límites de la API de Claude Opus y se incorporan cuatro nuevas capacidades a Claude Managed Agents en la Plataforma Claude — Dreaming, Multiagent orchestration, Outcomes y Webhooks — y enlaza las grabaciones en YouTube de keynotes y sesiones.

## ¿Cuándo es útil?

- Cuando un equipo que construye sobre Claude Managed Agents debe decidir si adopta ya Dreaming, Multiagent orchestration, Outcomes o Webhooks.
- Cuando se diseña una arquitectura de agentes que reparte el trabajo entre un agente líder y subagentes especialistas en paralelo sobre un sistema de archivos compartido.
- Cuando hay que definir un estándar de calidad para la salida del agente y conectar un grader separado más un bucle de revisión a una pipeline de producción.
- Cuando se quiere conectar ejecuciones asíncronas de agentes a sistemas existentes mediante webhooks en lugar de polling.

## Puntos clave

- Rate limits de Claude Code duplicados; límites de la API de Claude Opus elevados. Ambos cambios ya están en producción.
- Cuatro nuevas capacidades de Claude Managed Agents disponibles para todos los desarrolladores:
  - **Dreaming** — proceso programado que revisa sesiones pasadas, detecta patrones y cura memoria para que los agentes mejoren entre ejecuciones.
  - **Multiagent orchestration** — un agente líder delega en subagentes especialistas en paralelo sobre un sistema de archivos compartido, cada uno con su propio modelo, prompt y herramientas; todo el flujo es trazable en la Claude Console.
  - **Outcomes** — los desarrolladores definen una rúbrica, un grader separado evalúa cada resultado en su propia ventana de contexto y el agente revisa hasta superar la barra. Anthropic reporta una mejora de hasta 10 puntos en los problemas más difíciles de su benchmark interno.
  - **Webhooks** — una vez definido el outcome, el agente corre hasta el final y notifica por webhook al terminar.
- Charlas de clientes referenciadas: Asana, Cursor, GitHub, Replit, Vercel.
- Code w/ Claude continúa en Londres (19–18 de mayo [sic según el original]) y Tokio (5–6 de junio); las keynotes y sesiones del Día 1 se transmiten en vivo.

## Recursos incluidos

- `skills/managed-agents-new-capabilities/SKILL.md` — playbook para adoptar las cuatro nuevas capacidades de Managed Agents.
- `skills/managed-agents-new-capabilities/references/announcements-from-post.md` — catálogo textual de los anuncios de la conferencia y referencias de clientes en el post.
- `skills/managed-agents-new-capabilities/examples/outcomes-and-multiagent-patterns.md` — patrones trabajados combinando Outcomes, Multiagent orchestration y Webhooks sobre una tarea de ejemplo.

## Fuente

- [Code w/ Claude SF 2026: Building on the AI exponential](https://claude.com/blog/code-w-claude-sf-2026-sf) (blog de Anthropic, 12 de mayo de 2026)
