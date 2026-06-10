[English](./managed-agents-architecture.en.md) · [한국어](./managed-agents-architecture.ko.md) · **Español** · [日本語](./managed-agents-architecture.ja.md)

# Visión general de la arquitectura de Managed Agents

## ¿Qué es esta guía?
Un resumen arquitectónico conciso basado en el post “The evolution of agentic surfaces: building with Claude Managed Agents”.

## Idea central
Managed Agents separa:
- El arnés (el “cerebro”): orquestación y llamadas al modelo.
- El sandbox (las “manos”): el entorno de ejecución para herramientas/código.

Una sesión aporta un registro de eventos append-only que conecta ambos.

## Por qué importa la separación
- Seguridad: las credenciales pueden permanecer fuera del sandbox.
- Rendimiento: el razonamiento puede empezar antes de que exista un contenedor; las sesiones que no usan herramientas pueden evitar el arranque del contenedor.
- Operabilidad: sesiones duraderas habilitan líneas de tiempo de depuración, pausa/reanudación y funciones de más alto nivel (Memory, Dreaming).

## Conceptos mencionados en el post
- Agents, environments y sessions como recursos componibles.
- Vaults para credenciales.
- Sandboxes autoalojados opcionales (p. ej., dentro de una VPC).
- MCP tunnels para conectar con servidores MCP en redes privadas.

## Fuente
- https://claude.com/blog/building-with-claude-managed-agents
