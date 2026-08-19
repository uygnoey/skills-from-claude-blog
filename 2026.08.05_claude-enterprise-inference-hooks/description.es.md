[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Es el anuncio de **inference hooks**, una función de seguridad de Claude Enterprise que añade prevención de pérdida de datos (DLP) en línea. Cada solicitud de inferencia se enruta por una conexión WebSocket firmada hacia un servidor de seguridad que la organización controla. Antes de que el modelo empiece a generar, Claude envía el prompt y su contexto a ese servidor, espera un veredicto de permitir o denegar y solo entonces continúa. La misma comprobación se aplica a las respuestas de las llamadas a herramientas antes de devolverlas al modelo.

Hasta ahora, la aplicación nativa en línea se limitaba a los hooks del lado del cliente de Claude Code. Inference hooks extiende una única capa de aplicación a las superficies de Claude Enterprise —chat, Claude Code, Claude Cowork y las llamadas a herramientas mediante conectores MCP, skills y plugins— sin trabajo de integración por producto.

## ¿Cuándo es útil?
- Cuando el equipo de seguridad o cumplimiento exige que todo canal capaz de mover datos sensibles pase por un punto de inspección que ellos controlan.
- Cuando un programa DLP existente (Netskope, Palo Alto Networks, Proofpoint, Zscaler o un servidor propio) debe cubrir también el uso de IA.
- Cuando se quiere una sola configuración a nivel de organización en lugar de integraciones separadas por producto.
- Cuando se planifica un despliegue por etapas y hacen falta modo sombra, exclusiones y rampas por porcentaje antes de aplicar bloqueos.

## Puntos clave
- **Inspección previa a la generación.** El prompt y el contexto llegan a tu servidor antes de que el modelo genere; Claude continúa solo tras recibir el veredicto.
- **Las respuestas de herramientas también se inspeccionan**, incluidas las alcanzadas mediante conectores MCP, skills y plugins.
- **Protocolo abierto basado en webhooks con esquema publicado**, de modo que se puede reutilizar un servidor DLP existente y los proveedores de seguridad pueden construir integraciones.
- **Un único interruptor a nivel de organización** cubre las superficies de Claude Enterprise en lugar de una integración por producto.
- **Controles de despliegue**: modo sombra (siempre permitir), exclusiones por rol, despliegues por porcentaje, además de política de fallo y tiempos de espera configurables.
- Disponible **en beta para clientes de Claude Enterprise** en el momento de la publicación.
- Atención a la coincidencia de nombres: se trata de *inference hooks del lado del servidor*, no de los hooks de ciclo de vida del lado del cliente de Claude Code (PreToolUse, PostToolUse, etc.).

## Recursos incluidos
- `skills/inference-dlp-rollout/SKILL.md` — procedimiento de despliegue por etapas para activar el DLP en línea sin romper el trabajo de los usuarios.
- `skills/inference-dlp-rollout/references/enforcement-model.md` — dónde ocurre la inspección y qué hace cada control.
- `skills/inference-dlp-rollout/templates/rollout-plan.md` — plantilla rellenable de plan de despliegue y registro de decisiones.
- `guides/inline-dlp-for-claude-enterprise.{en,ko,es,ja}.md` — guía de arquitectura y despliegue en cuatro idiomas.

## Fuente
- https://claude.com/blog/claude-enterprise-inference-hooks
