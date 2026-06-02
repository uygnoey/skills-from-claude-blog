[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Este post presenta los “dynamic workflows” en Claude Code: una función que permite que Claude Code escriba y orqueste, sobre la marcha, un arnés multiagente para resolver tareas complejas de forma más nativa.

## ¿Cuándo es útil?
Los dynamic workflows son más adecuados para tareas complejas y de alto valor en las que la orquestación aporta ventajas (por ejemplo, triage, verificación o trabajo de ingeniería en varios pasos) y cuando conviene dividir el trabajo entre varios subagentes enfocados.

## Puntos clave
- Los dynamic workflows ejecutan un archivo de workflow en JavaScript y pueden crear y coordinar subagentes.
- Patrones comunes: classify-and-act, fan-out-and-synthesize, verificación adversarial, generate-and-filter, selección por torneo y bucles hasta cumplir una condición de parada.
- El workflow puede decidir qué modelo usa cada agente y si los subagentes se ejecutan en su propio worktree.
- Si se interrumpe, se puede reanudar la sesión y continuar.
- Se pueden guardar localmente (p. ej., `~/.claude/workflows`) y distribuir mediante un skill.

## Recursos incluidos
- Skill: `skills/dynamic-workflows-harness/` (biblioteca de patrones + plantillas de prompts reutilizables)
- Guide: `guides/dynamic-workflows.es.md` (explicación extensa + casos de uso)

## Fuente
- https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code
