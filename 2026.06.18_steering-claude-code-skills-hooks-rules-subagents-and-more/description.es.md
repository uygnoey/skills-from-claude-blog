[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Steering Claude Code: skills, hooks, subagents and more

## ¿De qué trata este post?

Este post explica las principales formas de dirigir el comportamiento de Claude Code y ofrece un marco de decisión para elegir dónde deben vivir las instrucciones.

## ¿Cuándo es útil?

Es útil cuando estás personalizando Claude Code y necesitas equilibrar costo de contexto, persistencia en sesiones largas (compaction) y autoridad de las instrucciones.

## Puntos clave

- Se cubren 7 métodos: archivos CLAUDE.md, rules, skills, subagents, hooks, output styles y añadir al system prompt.
- Cada método difiere en cuándo se carga, cómo se comporta con compaction y su costo de contexto.
- Consejo: mantener el CLAUDE.md raíz conciso (<200 líneas), mover procedimientos a skills y restricciones a rules con paths.
- Usa subagents para tareas laterales aisladas cuyos pasos intermedios no deben ensuciar el hilo principal.
- Usa hooks para automatización y enforcement deterministas (p. ej., PreToolUse puede denegar llamadas saliendo con código 2).
- Usa output styles solo para cambios de rol significativos; revisa estilos incorporados antes de crear uno personalizado.
- El post menciona que puedes agrupar varios métodos como un plugin para compartir una configuración coherente.

## Recursos incluidos

- Tabla comparativa de métodos y trade-offs
- Ejemplos: frontmatter de rules con paths; comportamiento de carga de CLAUDE.md en subdirectorios
- Tipos de hooks y eventos (PreCompact, PreToolUse)

## Fuente

- https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more
