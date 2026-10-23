[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un artículo de buenas prácticas (8 de septiembre de 2026, actualizado después con benchmarks de Opus 5.5)
que sostiene que en Claude Platform no hay que elegir entre coste y rendimiento. Tres palancas suelen
mejorar ambos: maximizar los aciertos de la caché de prompts, eliminar antipatrones de prompting al pasar a
modelos de frontera y calibrar el esfuerzo (effort) a la tarea. La guía está empaquetada en la skill
`claude-api`.

## ¿Cuándo es útil?
- Cuando el gasto en la API es alto o la tasa de aciertos de caché es baja.
- Tras migrar a un modelo más nuevo conservando prompts, skills o descripciones de herramientas antiguas.
- Al elegir modelo y nivel de effort frente a una eval.

## Puntos clave
- Caché de prompts: ligada a un modelo, exige un prefijo idéntico byte a byte y tiene un TTL de 5 minutos
  por defecto. Saca del prefijo valores volátiles y herramientas que cambian de orden, usa `defer_loading`,
  envía los cambios del system prompt como mensajes, precalienta con `max_tokens: 0` y considera un TTL de
  1 hora para esperas largas.
- Antipatrones: rituales de verificación, refuerzos de exhaustividad, andamios de scratchpad, ejemplos
  obsoletos, reglas contradictorias y configuración desfasada. `/claude-api prompt-audit` los detecta; en un
  caso de estudio redujo el coste otro ~9% y subió la precisión ~2 puntos.
- Effort: demasiado alto sobrepiensa, demasiado bajo omite evidencia. Barre niveles de effort y prueba
  modelos más fuertes con effort bajo. `/claude-api hillclimb` automatiza la búsqueda con un conjunto de
  prueba reservado.
- `/claude-api cost-optimize` ordena las palancas (caché, recorte, límites de salida, Batch API); en
  benchmarks públicos bajó el coste ~24-73% con poco o ningún cambio de calidad.

## Recursos incluidos
- Skill: `api-cost-performance-tuning` (`references/prompt-cache-checklist.md`,
  `references/prompt-anti-patterns.md`, `references/benchmark-results.md`,
  `templates/cost-audit-report.md`).

## Fuente
- https://claude.com/resources/articles/reducing-cost-and-improving-performance-with-claude-platform
