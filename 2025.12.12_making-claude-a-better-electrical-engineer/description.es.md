[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Making Claude a better electrical engineer

## ¿De qué trata este post?
Este post explica cómo Anthropic colaboró con Diode Computers para mejorar la capacidad de Claude de generar diseños de referencia de PCB usando el lenguaje Zener.

## ¿Cuándo es útil?
Es útil si quieres mejorar el rendimiento del modelo en un dominio estrecho colaborando con expertos, creando un benchmark y iterando sobre modos de fallo.

## Puntos clave
- Define una tarea agéntica concreta y un arnés (harness) de evaluación (testbench) que capture éxito/fracaso en términos del dominio.
- Usa retroalimentación de expertos para identificar fallos comunes y refinar criterios de evaluación.
- Prefiere comprobaciones basadas en requisitos (por ejemplo, capacitancia mínima) en lugar de aserciones frágiles de coincidencia exacta.
- Valida las mejoras con comparaciones a ciegas frente a modelos base.

## Recursos incluidos
- Skill: skills/domain-partnership-benchmarking/SKILL.md

## Fuente
- https://claude.com/blog/making-claude-a-better-electrical-engineer
