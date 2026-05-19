[English](./managed-agents-network-perimeter.en.md) · [한국어](./managed-agents-network-perimeter.ko.md) · **Español** · [日本語](./managed-agents-network-perimeter.ja.md)

# Mantener la ejecución y la conectividad dentro del perímetro

## Qué cubre esta guía
- Cómo los sandboxes autoalojados cambian el límite de ejecución en Claude Managed Agents.
- Cómo los túneles MCP habilitan conectividad privada a servidores MCP sin exposición pública.

## Guía práctica

### Límite de ejecución
- Coloca repositorios, archivos, dependencias y ejecuciones de herramientas intensivas en cómputo dentro del sandbox.
- Mantén el bucle gestionado del agente en el plano de control.

### Conectividad
- Para servidores MCP privados, prioriza los túneles MCP para evitar reglas de firewall entrantes y endpoints públicos.
- Asegura cifrado de extremo a extremo.

## Fuente
- https://claude.com/blog/claude-managed-agents-updates
