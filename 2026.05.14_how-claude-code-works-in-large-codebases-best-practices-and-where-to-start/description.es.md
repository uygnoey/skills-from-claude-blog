[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# How Claude Code works in large codebases: Best practices and where to start

## ¿De qué trata este post?
Este post explica patrones de configuración, herramientas y organización para que Claude Code funcione bien en bases de código grandes, y por dónde empezar a escalarlo.

## ¿Cuándo es útil?
Útil cuando estás implementando o escalando Claude Code en un monorepo o una base de código empresarial y necesitas convenciones de contexto, automatización, propiedad y navegación.

## Puntos clave
- Claude Code navigates codebases agentically (file traversal + targeted search) rather than relying on a pre-built index.
- The harness (e.g., CLAUDE.md, hooks, skills, plugins, MCP, LSP, subagents) often determines real-world performance.
- Keep CLAUDE.md files lean and layered, and review them periodically as model capabilities change.
- Treat adoption as an org problem too: define ownership (DRI / agent manager) and governance early.

## Recursos incluidos
- Skills: 1
- Guides: 1

## Fuente
- https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start
