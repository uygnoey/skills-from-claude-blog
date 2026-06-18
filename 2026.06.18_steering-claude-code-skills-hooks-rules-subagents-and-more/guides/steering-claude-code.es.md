[English](./steering-claude-code.en.md) · [한국어](./steering-claude-code.ko.md) · **Español** · [日本語](./steering-claude-code.ja.md)

# Marco de decisión para dirigir Claude Code

## Resumen

Claude Code ofrece varios lugares para colocar instrucciones, cada uno con trade-offs (cuándo se cargan, compaction, costo de contexto y autoridad).

## Los 7 métodos

El post cubre: archivos CLAUDE.md, rules, skills, subagents, hooks, output styles y añadir al system prompt.

## Guía práctica

- Mantén el CLAUDE.md raíz conciso (<200 líneas) y trátalo como código (owner + revisión).
- Usa CLAUDE.md en subdirectorios para convenciones limitadas a una carpeta.
- Usa rules para restricciones; prefiere rules con paths para que solo se carguen cuando aplique.
- Usa skills para procedimientos (deploy, checklist de release, procesos de review).
- Usa subagents para tareas laterales aisladas que devuelven solo un resumen.
- Usa hooks para automatización/enforcement deterministas.
- Usa output styles solo para cambios de rol significativos; revisa estilos incorporados antes de crear uno.
- Usa append-system-prompt para instrucciones aditivas de una sola invocación (tono/formato).

## Fuente

- https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more
