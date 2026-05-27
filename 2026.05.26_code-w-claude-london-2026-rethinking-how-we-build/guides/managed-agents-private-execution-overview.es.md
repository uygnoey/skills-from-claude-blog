[English](./managed-agents-private-execution-overview.en.md) · [한국어](./managed-agents-private-execution-overview.ko.md) · **Español** · [日本語](./managed-agents-private-execution-overview.ja.md)

# Opciones de ejecución privada para Claude Managed Agents (visión general)

## ¿Qué es esto?
Una guía breve y orientada a la decisión sobre dos capacidades de la Claude Platform mencionadas en el resumen de Code w/ Claude London 2026: sandboxes autoalojados y túneles MCP.

## Árbol de decisión
1) ¿Necesitas controlar **dónde se ejecuta el código del agente** (los datos/archivos no pueden salir de tu perímetro)?
- Sí → Sandboxes autoalojados.

2) ¿Necesitas que Claude acceda a **servidores MCP privados** sin exponer endpoints entrantes?
- Sí → Túneles MCP.

3) ¿Necesitas ambos?
- Sí → Usa ambos en conjunto.

## Checklist de implementación (alto nivel)
- Define el perímetro de datos (repos, archivos, secretos, logs).
- Lista las herramientas internas a exponer (servidores MCP) y su autenticación.
- Define la política de egreso de red y los requisitos de auditoría.
- Asigna responsables: runtime/infra, seguridad y administradores de la Console.

## Lecturas adicionales
- Referencia: `../skills/managed-agents-private-execution/references/managed-agents-private-execution.md`
- Fuente (resumen del evento): https://claude.com/blog/code-w-claude-london-2026-rethinking-how-we-build
