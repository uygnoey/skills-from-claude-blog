[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Novedades en Claude Managed Agents: despliegues programados y variables de entorno en vaults

## ¿De qué trata este post?
Este post anuncia dos capacidades nuevas (beta pública) de Claude Managed Agents: despliegues programados (ejecuciones tipo cron) y el almacenamiento de variables de entorno en vaults para autenticar CLIs de forma segura.

## ¿Cuándo es útil?
Es útil cuando quieres que un agente ejecute tareas rutinarias en un horario sin construir tu propio programador, y cuando necesitas pasar secretos (por ejemplo, claves API) a herramientas CLI sin exponerlos al modelo.

## Puntos clave
- Los despliegues programados inician una sesión nueva en un horario cron; puedes pausar/reanudar/archivar y también lanzar ejecuciones bajo demanda.
- Los vaults ahora admiten variables de entorno para que las CLIs hagan solicitudes autenticadas; el agente nunca ve el secreto y los dominios se controlan con una lista permitida.

## Recursos incluidos
- Skill: managed-agents-scheduled-deployments (lista operativa y patrones de uso)

## Fuente
- https://claude.com/blog/whats-new-in-claude-managed-agents
