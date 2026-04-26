[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Claude ahora puede conectarse a tu mundo

## ¿De qué trata este post?

El anuncio de lanzamiento de **Integrations** —la forma en que Claude se conecta a apps y herramientas mediante servidores MCP remotos— y la ampliación de **Research avanzado**. Juntos permiten a Claude traer contexto desde tus apps de trabajo, buscar en la web y en Google Workspace y entregar reportes completos con citas en cinco a cuarenta y cinco minutos. Publicado originalmente el 2025-05-01; una actualización del 2025-06-03 amplió la disponibilidad a Pro y dejó la búsqueda web global en todos los planes pagos.

## ¿Cuándo es útil?

- Decidir si conectar una app de terceros a Claude vía Integrations en lugar de construir automatización a medida.
- Planificar el uso de Research avanzado para investigaciones multi-fuente que de otro modo tomarían horas.
- Incorporar a un equipo al flujo Integrations + Research y estandarizar qué apps conectar primero.
- Consultar qué servicios estaban disponibles en el lanzamiento y cuáles en la hoja de ruta.

## Puntos clave

- Integrations conecta Claude a **servidores MCP remotos** en web y escritorio, extendiendo el lanzamiento de MCP de noviembre de 2024 más allá de servidores locales en Claude Desktop.
- Línea de lanzamiento de 10 servicios: **Atlassian Jira, Atlassian Confluence, Zapier, Cloudflare, Intercom, Asana, Square, Sentry, PayPal, Linear, Plaid**. La hoja de ruta menciona **Stripe, GitLab, Box**.
- Los desarrolladores pueden construir Integrations propias en tan solo 30 minutos; Cloudflare aporta OAuth, manejo de transporte y despliegue integrados.
- Patrones concretos del post: Zapier conecta miles de apps mediante workflows pre-armados (p. ej. traer datos de ventas de HubSpot, preparar briefs de reunión desde el calendario); Atlassian para planificación de producto y actualizaciones masivas de Confluence/Jira; el agente de IA de Intercom, **Fin**, actúa como cliente MCP y puede registrar bugs en Linear a partir de reportes de usuarios.
- Research avanzado divide la solicitud en sub-investigaciones a través de cientos de fuentes y devuelve un reporte con citas en **5 a 45 minutos**; ahora busca en la web, Google Workspace **y** cualquier Integration conectada.
- **Disponibilidad**: en el lanzamiento, Integrations y Research avanzado en beta para Max, Team, Enterprise; búsqueda web global en planes pagos. Tras la actualización del 2025-06-03, Integrations y Research disponibles en Pro, Max, Team, Enterprise; búsqueda web global en todos los planes de Claude.

## Recursos incluidos

- [skills/connected-tools-research-playbook/SKILL.md](./skills/connected-tools-research-playbook/SKILL.md): patrones para usar Integrations + Research juntos.
- [references/launch-services.md](./skills/connected-tools-research-playbook/references/launch-services.md): herramientas/servicios mencionados en el post.
- [examples/example-workflows.md](./skills/connected-tools-research-playbook/examples/example-workflows.md): ejemplos de workflows del post.
- [guides/getting-started.es.md](./guides/getting-started.es.md) (+ en/ko/ja): cómo habilitar y empezar a usar Integrations y Research.

## Fuente

Basado en [Claude can now connect to your world](https://claude.com/blog/integrations) (publicado el 2025-05-01, actualizado el 2025-06-03).
