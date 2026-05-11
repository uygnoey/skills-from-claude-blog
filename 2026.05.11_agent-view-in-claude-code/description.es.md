[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Agent view en Claude Code

## ¿De qué trata este post?
Agent view es una interfaz de terminal a pantalla completa para gestionar varias sesiones en segundo plano de Claude Code desde un solo lugar.

## ¿Cuándo es útil?
Es útil cuando quieres ejecutar varias tareas independientes en paralelo (por ejemplo, corregir un bug, revisar un PR o investigar logs) y solo intervenir cuando una sesión necesita tu input.

## Puntos clave
- Abre agent view con `claude agents`.
- Puedes despachar nuevas sesiones en segundo plano, monitorear su estado, previsualizar y responder, o adjuntarte y volver a la tabla.
- Agent view es una "research preview" y requiere Claude Code v2.1.139+.
- Las sesiones se ejecutan bajo un proceso supervisor y su estado persiste en disco entre reinicios de la terminal.

## Recursos incluidos
- Skill: `manage-agent-view-sessions` (comandos, sintaxis de filtros y listas de verificación repetibles para gestionar sesiones)
- Guía: `agent-view-quickstart` (cómo incorporar agent view en el trabajo diario)

## Fuente
- https://claude.com/blog/agent-view-in-claude-code
- https://code.claude.com/docs/en/agent-view
