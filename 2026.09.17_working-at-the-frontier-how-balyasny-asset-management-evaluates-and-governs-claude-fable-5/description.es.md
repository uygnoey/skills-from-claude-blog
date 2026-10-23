[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Entrevista con Charlie Flanagan, Chief AI Officer de Balyasny Asset Management (BAM), publicada el 17 de
septiembre de 2026. Explica cómo BAM evaluó Claude Fable 5 antes de activarlo, cómo gobierna a sus agentes
con controles alrededor del modelo y qué ha hecho posible su plataforma interna de agentes, BAMAgent.

## ¿Cuándo es útil?
- Al decidir si pasar el trabajo de agentes en producción a un nuevo modelo de frontera.
- Al crear un conjunto interno de evaluaciones con tareas reales y verificables en lugar de benchmarks públicos.
- Al definir permisos, registros y revisión humana antes de ampliar el acceso de los agentes en un dominio de alto riesgo.

## Puntos clave
- En 2026 BAM pasó de una IA que busca a una IA que completa trabajo, impulsada por arneses de agentes como
  Claude Code.
- Evaluaciones: miles de tareas financieras con resultados verificables (renta variable, macro, materias
  primas), ejecutadas con el modelo solo y dentro del arnés de agentes de BAM. En el subconjunto relevante,
  Fable obtuvo 89,4 % frente a 86,1 % del modelo de producción anterior, con las mayores mejoras en
  planificación, análisis y ejecución agéntica.
- Un resultado sorprendente (problemas de economía que ningún modelo anterior había resuelto) se trató primero
  como posible fallo de la evaluación: se repitió, se verificó de forma independiente y se revisó con
  Anthropic antes de aceptarlo.
- La seguridad está en los controles alrededor del modelo: límites de datos aprobados, mínimo privilegio,
  permisos por herramienta, registros, revisión humana de resultados relevantes y vías de escalado. Un modelo
  más capaz no recibe más autoridad; el juicio de inversión sigue en manos de personas.
- BAMAgent ejecuta miles de agentes autónomos. El análisis de arbitraje de fusiones pasó de tres a cinco días
  a menos de un día (unos 30 minutos de agente); un análisis de bancos centrales pasó de unos dos días a unos
  30 minutos, manteniendo la revisión. Algunos equipos operan más de 300 agentes.

## Recursos incluidos
- Skill: `frontier-model-eval-governance` (`references/eval-dimensions.md`, `templates/controls-checklist.md`, `examples/workflows.md`).
- Guía: `guides/agentic-model-evaluation-and-governance` (4 idiomas).

## Fuente
- https://claude.com/resources/articles/working-at-the-frontier-how-balyasny-asset-management-evaluates-and-governs-claude-fable-5
