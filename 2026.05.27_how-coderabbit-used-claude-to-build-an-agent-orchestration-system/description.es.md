[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
CodeRabbit explica cómo construyó (con Claude) una capa de orquestación de planificación antes de la generación de código, que produce un plan/PRD estructurado para que el equipo lo revise y reduzca resultados de “código que parece correcto pero no cumple la intención”.

## ¿Cuándo es útil?
Es útil cuando el código generado por IA compila y pasa tests pero no resuelve el problema real, o cuando los requisitos y supuestos no se explicitan antes de implementar.

## Puntos clave
- Añadir una fase de planificación estructurada antes de implementar para hacer explícitos los supuestos y alinear al equipo.
- Tratar el plan como un artefacto compartido y una compuerta de calidad antes de generar código.
- Asignar niveles de modelo según la complejidad (Opus para la orquestación, Sonnet para pasos de planificación estructurados, Haiku para tareas acotadas como destilar contexto).
- Evaluar la calidad del plan con un arnés de evaluación (jueces LLM + resultados posteriores en el código, como alcance extra y tokens hasta completar).

## Recursos incluidos
- Plantilla de prompt reutilizable para extraer resultados, supuestos, casos límite y verificaciones de validación.
- Ejemplo de esquema de “PRD colaborativo” para revisión antes de implementar.

## Fuente
- https://claude.com/blog/how-coderabbit-used-claude-to-build-an-agent-orchestration-system
