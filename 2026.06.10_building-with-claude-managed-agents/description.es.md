[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# La evolución de las superficies agenticas: construir con Claude Managed Agents

## ¿De qué trata este post?
Este post presenta Claude Managed Agents: un conjunto de APIs componibles para crear y desplegar agentes de nivel producción sobre infraestructura gestionada.

También contrasta el uso anterior del API (“tokens in, tokens out”) con productos agénticos como Claude Code y el Claude Agent SDK, y describe Managed Agents como una arquitectura que separa el arnés (el “cerebro”) del sandbox de ejecución (las “manos”).

## ¿Cuándo es útil?
- Cuando quieres operar agentes de forma fiable en producción sin construir y mantener tú mismo todo el arnés y la infraestructura.
- Cuando necesitas manejo seguro de credenciales, sesiones persistentes, observabilidad y orquestación escalable para agentes que usan herramientas.
- Cuando quieres separar el razonamiento del modelo de la ejecución en sandbox (incluidas opciones de sandboxes autoalojados/VPC).

## Puntos clave
- Un agente en producción requiere más que un prompt: hosting y escalado, gestión de sesiones, estado del sistema de archivos, aislamiento de ejecución, credenciales y observabilidad.
- Managed Agents separa el arnés del sandbox; una sesión es un registro append-only de llamadas al modelo, llamadas a herramientas y resultados.
- Las credenciales pueden mantenerse fuera del sandbox mediante Vaults y recuperación bajo demanda, reduciendo la exposición a inyecciones de prompt.
- La latencia puede mejorar porque el razonamiento puede empezar antes de que exista un contenedor, y las sesiones que no usan herramientas pueden evitar el arranque del contenedor.
- Las sesiones duraderas habilitan líneas de tiempo de depuración, Memory y Dreaming (un proceso programado que revisa sesiones/memorias para curar memorias futuras).

## Recursos incluidos
- Skill: checklist del arnés de producción y notas de arquitectura derivadas del post.
- Notas de referencia: Vaults, sesiones y la separación entre gestión y sandbox.

## Fuente
- https://claude.com/blog/building-with-claude-managed-agents
