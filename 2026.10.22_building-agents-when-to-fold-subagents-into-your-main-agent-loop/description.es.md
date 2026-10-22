[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un artículo de buenas prácticas (22 de octubre de 2026, Diane Sarkis) sobre cuándo integrar routers,
planificadores y subagentes de dominio en un único bucle de agente principal que usa skills y búsqueda
de herramientas con divulgación progresiva, y cómo migrar paso a paso en Claude Platform.

## ¿Cuándo es útil?
- Cuando la arquitectura del agente se ha convertido en una copia del organigrama (un subagente por equipo).
- Cuando un sistema multiagente es lento, tiene una voz inconsistente o es difícil de evaluar de extremo
  a extremo.
- Al planificar qué subagentes mantener, invocar como herramientas, fusionar o convertir en skills y
  herramientas.

## Puntos clave
- En comparaciones entre despliegues empresariales, un solo agente con skills superó con frecuencia
  tanto al diseño de un único prompt como al de subagentes en calidad, a menudo con menor coste y latencia.
- Mantén subagentes si hay degradación medible por exceso de contexto, trabajo paralelo que necesita
  contextos desechables, o problemas para elegir herramientas / instrucciones contradictorias.
- Modos de fallo: gestión de contexto, proliferación de subagentes, el "Frankenprompt", evals
  demasiado locales, latencia (un cliente vio una ejecución aproximadamente 2 veces más rápida con un
  solo bucle).
- Diseño objetivo: un modelo, una ventana de contexto, lotes de llamadas a herramientas en paralelo,
  presupuestos y compuertas de escritura en el arnés, y un plan escrito y revisado en contexto; el
  procedimiento va en skills y los límites estrictos en herramientas.
- Migra detrás de una eval de finalización de tareas (10 ejemplos de referencia para empezar), un
  subagente cada vez, revisando qué tareas cambiaron de resultado y ejecutando cada tarea más de una vez.
- Los equipos poseen skills, herramientas MCP (agrupadas por intención del usuario; la elección empeora
  pasadas 30-50 definiciones) y bases de conocimiento; un pequeño equipo central posee el system prompt
  y la calidad de extremo a extremo.
- Ayudas: `/claude-api build-eval`, `prompt-audit`, `hillclimb`, `cost-optimize`, `/skill-creator`,
  `/skill-doctor` y un kit de migración con demo.

## Recursos incluidos
- Skill: `fold-subagents-into-agent-loop` (`references/decision-criteria.md`,
  `references/single-loop-design.md`, `templates/migration-plan.md`, `templates/eval-plan.md`).
- Guía: `guides/subagent-to-single-loop-migration.{en,ko,es,ja}.md`.

## Fuente
- https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
