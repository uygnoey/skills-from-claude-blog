[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?

Este post anuncia actualizaciones de “skill-creator” para ayudar a autores a probar, medir y refinar Agent Skills, de modo que sigan funcionando a medida que evolucionan los modelos.

## ¿Cuándo es útil?

Es útil cuando mantienes skills a lo largo del tiempo y necesitas una forma ligera de detectar regresiones, medir mejoras, comparar variantes y ajustar descripciones para que se activen de forma fiable.

## Puntos clave

- El post distingue dos categorías: skills de “capability uplift” y skills de “encoded preference”.
- Skill-creator ahora permite escribir evals (tests) definiendo prompts de prueba (y archivos si hace falta) y describiendo qué significa un buen resultado.
- Los evals ayudan a detectar regresiones cuando cambian los modelos y a saber cuándo el modelo base ya supera una skill de capability uplift.
- El modo benchmark ejecuta evaluaciones estandarizadas y registra tasa de aprobación, tiempo transcurrido y uso de tokens.
- El soporte multi-agente ejecuta evals en paralelo con contextos limpios y métricas independientes de tokens/tiempo.
- Los comparator agents permiten comparaciones A/B a ciegas (skill vs. sin skill, o dos versiones de la skill).
- Skill-creator puede sugerir ediciones de descripción para reducir falsos positivos y falsos negativos en el disparo.

## Recursos incluidos

- Skill: un playbook práctico para mantener Agent Skills con evals, benchmarks y ajuste de descripciones.
- Referencia: definiciones de “capability uplift” vs “encoded preference”.

## Fuente

- https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills
