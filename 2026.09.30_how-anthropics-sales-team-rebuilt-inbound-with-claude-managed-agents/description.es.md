[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un caso de estudio (30 de septiembre de 2026) de Carl Johnson, líder de desarrollo de ventas en Anthropic,
sobre cómo un agente de compra creado con Claude Managed Agents (beta) atiende ya a la mayoría de los
clientes entrantes y los lleva de "quiero Claude para mi empresa" a la compra, y cómo eso cambió el
trabajo del equipo de ventas.

## ¿Cuándo es útil?
- Cuando la demanda entrante supera un proceso de formulario → BDR → AE y los compradores esperan días por respuestas sencillas.
- Al diseñar una experiencia de compra autoservicio, disponible siempre, que aún pase los acuerdos complejos a los representantes.
- Al escribir e iterar el prompt de un agente de ventas de cara al cliente.

## Puntos clave
- Proceso anterior: decenas de miles de solicitudes entrantes al mes; los representantes respondían preguntas que ya cubría la documentación.
- El agente está en las páginas Contact Sales y Pricing, dentro del producto y en los correos; es opcional (opt-in).
- Cada conversación termina en una compra, un traspaso a un representante con todo el contexto o una respuesta rápida.
- Arquitectura: un prompt, unas pocas herramientas y Claude sobre Managed Agents (alojamiento, sesiones y orquestación de herramientas).
- Por qué Managed Agents: un ingeniero lo lanzó en pocas semanas; los líderes de ventas y contenido editaban el
  prompt en la Console con un agente de staging; cada cambio es una versión (v7 tras una semana de pruebas internas).
- Lecciones: dar a Claude un objetivo, no reglas; menos es más; incluir a expertos en la materia (SME) en el ciclo;
  recomendar el plan adecuado (p. ej., Team en vez de Enterprise); tratar cada motivo de escalado como
  retroalimentación (los traspasos bajaron aproximadamente a la mitad).
- Resultados: miles de conversaciones al día; los leads escalados se convierten en oportunidades más del doble
  de veces y cierran unos cinco días antes; un representante pasó de ~10 a ~6 correos por acuerdo y multiplicó por 2,5 sus cierres.

## Recursos incluidos
- Skill: `inbound-buying-agent-design` (`references/conversation-outcomes.md`,
  `references/lessons-and-results.md`, `templates/goal-first-system-prompt.md`,
  `templates/escalation-feedback-log.md`).

## Fuente
- https://claude.com/resources/articles/how-anthropics-sales-team-rebuilt-inbound-with-claude-managed-agents
