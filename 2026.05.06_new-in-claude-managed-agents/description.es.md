[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Este post anuncia nuevas capacidades de Claude Managed Agents: dreaming (avance de investigación), outcomes, orquestación multiagente y webhooks.

## ¿Cuándo es útil?
Es útil cuando quieres agentes que mejoren con el tiempo (memoria + dreaming), que mantengan un estándar de calidad con evaluación automática (outcomes) y que ejecuten trabajo paralelo con especialistas (orquestación multiagente).

## Puntos clave
- Dreaming es un proceso programado que revisa sesiones pasadas y memorias para extraer patrones y refinar lo que el agente recuerda.
- Outcomes te permite definir una rúbrica de éxito; un evaluador separado califica la salida y el agente itera hasta cumplir la rúbrica.
- La orquestación multiagente usa un agente líder que delega a agentes especialistas (con su propio modelo, prompt y herramientas) trabajando en paralelo sobre un sistema de archivos compartido.
- Los webhooks pueden notificarte cuando termina la evaluación de outcomes.

## Recursos incluidos
- Skill: `managed-agent-orchestration` (plantillas de rúbrica para outcomes, lista de verificación para revisión de memoria/dreaming y glosario de roles).

## Fuente
- https://claude.com/blog/new-in-claude-managed-agents
