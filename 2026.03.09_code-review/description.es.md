[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Este post presenta Code Review en Claude Code: una función de revisión automática de pull requests que envía varios agentes para buscar bugs y problemas, y publica una revisión consolidada en el PR.

## ¿Cuándo es útil?
- Cuando necesitas una cobertura de revisión más profunda que linters ligeros o una lectura rápida con un LLM.
- Cuando quieres comentarios de revisión consistentes en cada PR, manteniendo la decisión final de aprobación en manos humanas.

## Puntos clave
- Se envía un equipo de agentes en cada PR; la profundidad escala según el tamaño y la complejidad del cambio.
- Los resultados llegan como un comentario general y comentarios en línea.
- Está diseñado para profundidad (y por eso suele ser más costoso que opciones más ligeras).
- La función no aprueba PRs; las personas deciden si se hace merge.

## Recursos incluidos
- Skill: "Revisión automática de PR con equipos de agentes" (derivada del flujo descrito en el post y de la configuración para admins y desarrolladores).

## Fuente
- https://claude.com/blog/code-review
