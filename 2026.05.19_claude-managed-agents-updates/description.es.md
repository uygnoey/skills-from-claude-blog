[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Este post anuncia dos novedades de Claude Managed Agents: ejecutar herramientas dentro de un sandbox que controlas (sandboxes autoalojados) y conectar agentes de forma segura a servidores privados de Model Context Protocol (MCP) mediante túneles MCP.

## ¿Cuándo es útil?
Es útil cuando necesitas que los agentes trabajen con código, archivos o sistemas internos sensibles, manteniendo la ejecución y el acceso de red dentro del perímetro de seguridad de tu empresa.

## Puntos clave
- Los sandboxes autoalojados trasladan la ejecución de herramientas a infraestructura que controlas (o a un proveedor gestionado), mientras que el bucle del agente (orquestación, gestión de contexto y recuperación de errores) permanece en la infraestructura de Anthropic.
- Puedes elegir proveedor de sandbox (Cloudflare, Daytona, Modal, Vercel) según aislamiento, escala, red y necesidades de runtime.
- Los túneles MCP permiten que los agentes accedan a servidores MCP dentro de una red privada sin exponerlos a Internet pública (una sola conexión saliente, sin reglas de firewall entrantes, cifrado de extremo a extremo).
- Disponibilidad: sandboxes autoalojados en beta pública; túneles MCP en vista previa de investigación y requieren solicitud de acceso.

## Recursos incluidos
- Skill: managed-agents-secure-sandboxing (patrones y listas de verificación para elegir y operar sandboxes autoalojados y túneles MCP)
- Guide: managed-agents-network-perimeter (guía orientada al despliegue para mantener ejecución y conectividad dentro del perímetro)

## Fuente
- https://claude.com/blog/claude-managed-agents-updates
