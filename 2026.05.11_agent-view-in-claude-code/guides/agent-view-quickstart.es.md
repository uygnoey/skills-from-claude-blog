[English](./agent-view-quickstart.en.md) · [한국어](./agent-view-quickstart.ko.md) · **Español** · [日本語](./agent-view-quickstart.ja.md)

# Inicio rápido de agent view (Claude Code)

## Resumen
Agent view te permite ejecutar y gestionar muchas sesiones en segundo plano de Claude Code desde una sola pantalla.

## Requisitos
- Claude Code v2.1.139+
- La función puede cambiar (research preview)

## Empezar
1. Ejecuta `claude agents`.
2. Escribe un prompt y pulsa `Enter` para despachar una sesión en segundo plano.
3. Repite para lanzar varias sesiones en paralelo.

## Flujo de trabajo diario
- Monitorea qué sesiones están trabajando y cuáles están bloqueadas.
- Usa `Space` para abrir el panel de vista previa y responder sin salir de la tabla.
- Adjunta (`Enter`) solo cuando necesites colaborar en profundidad.
- Vuelve a la tabla con `←` en un prompt vacío.

## Ediciones paralelas seguras
Si varias sesiones van a editar archivos, espera aislamiento mediante worktrees. Los worktrees se crean bajo `.claude/worktrees/` y se eliminan al borrar la sesión.

## Fuente
- https://code.claude.com/docs/en/agent-view
