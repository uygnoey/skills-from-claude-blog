[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Llegar a producción más rápido con la Anthropic Console renovada

## ¿De qué trata este post?

El anuncio de Anthropic del 6 de marzo de 2025 presenta una Anthropic Console rediseñada como un único lugar para construir, probar e iterar despliegues de IA con Claude junto al resto del equipo. El post destaca cuatro herramientas de prompt engineering (Workbench, generación automática de prompts, evaluación con comparación lado a lado y mejora de prompts), prompts compartibles para la colaboración entre funciones, soporte para el último modelo Claude 3.7 Sonnet y la capacidad de controlar el extended thinking budget.

## ¿Cuándo es útil?

- Estás llevando un nuevo prompt a producción y quieres un ciclo estructurado de construir → probar → iterar en lugar de experimentación ad hoc.
- Varios roles (desarrolladores, expertos de dominio, product managers, QA) necesitan colaborar sobre el mismo prompt sin copiar y pegar entre documentos.
- Estás migrando prompts escritos para otros modelos de IA y quieres reescribirlos con las técnicas de prompt engineering de Anthropic.
- Estás adoptando el extended thinking de Claude 3.7 Sonnet y necesitas presupuestar los thinking tokens de forma deliberada.

## Puntos clave

- El Workbench permite estructurar prompts, añadir ejemplos e integrar herramientas externas en un entorno interactivo de prueba de llamadas a la API.
- Un prompt generator convierte una descripción de tarea en un prompt que usa técnicas como chain-of-thought.
- Una herramienta de evaluación genera casos de prueba automáticamente, compara salidas lado a lado y califica la calidad de respuesta.
- Una herramienta de mejora de prompts refina prompts existentes, incluidos los originalmente escritos para otros modelos de IA.
- "Get Code" exporta una llamada a la API lista para producción que se puede desplegar directamente.
- Los prompts compartibles le dan a los equipos una biblioteca centralizada para desarrollar, refinar y estandarizar prompts en toda la organización.
- Soporta Claude 3.7 Sonnet, incluido el presupuesto máximo de thinking tokens para el extended thinking.

## Recursos incluidos

- Skill: `skills/console-build-test-iterate-workflow/SKILL.md` — el ciclo construir → evaluar → mejorar → desplegar que describe el post, con guía sobre prompts compartibles y presupuesto de extended thinking.
- Referencia: `skills/console-build-test-iterate-workflow/references/console-tools-from-post.md` — resumen textual de las herramientas y capacidades de Console que el post enumera.
- Ejemplos: `skills/console-build-test-iterate-workflow/examples/team-collaboration-scenarios.md` — escenarios ilustrativos de prompts compartibles basados en los roles colaboradores que menciona el post.

## Fuente

Get to production faster with the upgraded Anthropic Console — Anthropic, 6 de marzo de 2025: <https://claude.com/blog/upgraded-anthropic-console>
