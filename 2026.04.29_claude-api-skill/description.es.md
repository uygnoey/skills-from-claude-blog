[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# El claude-api skill ya está en CodeRabbit, JetBrains, Resolve AI y Warp

## ¿De qué trata este post?

El anuncio de Anthropic del 29 de abril de 2026 informa que CodeRabbit, JetBrains, Resolve AI y Warp ahora incluyen el skill `claude-api`, llevando código listo para producción de la API de Claude a las herramientas que las personas desarrolladoras ya usan. El skill — introducido por primera vez en Claude Code en marzo — captura los detalles que hacen que el código de la API de Claude funcione bien: qué patrón de agente encaja con cada trabajo, qué parámetros cambian entre generaciones de modelos y cuándo aplicar prompt caching. Se mantiene al día a medida que evolucionan los SDK de Anthropic, así que en cuanto sale un nuevo modelo o función de la API, Claude ya lo conoce.

## ¿Cuándo es útil?

- Escribes código con la API de Claude desde CodeRabbit, JetBrains/Junie, Resolve AI, Warp o Claude Code, y quieres aprovechar el skill incluido en lugar de buscar parámetros a mano.
- Estás migrando a un modelo Claude más reciente (el post menciona Claude Opus 4.7) y quieres ayuda guiada para actualizar nombres de modelo, ajustes de thinking, parámetros y beta headers.
- Quieres aplicar prompt caching o context compaction a un agente existente sin releer la documentación desde cero.
- Estás construyendo un producto de coding agent y quieres incluir el skill open source `claude-api` para dar a tus usuarios la misma experiencia.

## Puntos clave

- El skill `claude-api` ahora viene incluido en CodeRabbit, JetBrains, Junie, Resolve AI y Warp — además de Claude Code, donde se lanzó en marzo.
- El skill mantiene a Claude actualizado conforme cambian los SDK, reduciendo sorpresas en code review causadas por conocimiento desactualizado de la API.
- Cuatro prompts representativos que destaca el post:
  - "Improve my cache hit rate." — aplica reglas de prompt caching que muchas personas pasan por alto.
  - "Add context compaction to my agent." — recorre las primitivas de compaction y los patrones de agente.
  - "Upgrade me to the latest Claude model." — migración guiada de modelo; en Claude Code, ejecutable con `/claude-api migrate`.
  - "Build a deep research agent for my industry." — configuración guiada de Claude Managed Agents; en Claude Code, ejecutable con `/claude-api managed-agents-onboard`.
- Para quienes construyen coding agents: el skill es open source en `anthropics/skills`; la guía de bundling describe la configuración en unas 20 líneas de CI, con actualizaciones automáticas.
- Testimonios de clientes en el post: Warp, CodeRabbit, JetBrains y Resolve AI — centrados en mantener el flujo, menos sorpresas en review y adopción más rápida de modelos.

## Recursos incluidos

- Skill: `skills/bundled-api-skill-usage-patterns/SKILL.md` — los cuatro prompts y slash commands del post para trabajar con el skill incluido.
- Referencia: `skills/bundled-api-skill-usage-patterns/references/integrations-and-quotes-from-post.md` — resumen textual de las integraciones anunciadas y de las citas de clientes.
- Ejemplos: `skills/bundled-api-skill-usage-patterns/examples/usage-prompts.md` — los cuatro prompts ilustrativos del post como referencia reutilizable.

## Fuente

Claude API skill now in CodeRabbit, JetBrains, Resolve AI, and Warp — Anthropic, 29 de abril de 2026: <https://claude.com/blog/claude-api-skill>
