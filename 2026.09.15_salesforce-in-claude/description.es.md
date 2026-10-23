[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un anuncio (15 de septiembre de 2026) de Salesforce in Claude, un plugin en beta creado con Salesforce que
lleva a Claude las cuentas, oportunidades y pipeline de cada vendedor con sus permisos actuales de
Salesforce. Incluye 37 skills para el trabajo diario de un account executive.

## ¿Cuándo es útil?
- Cuando los vendedores pierden tiempo reuniendo contexto de Salesforce, correo, grabaciones de llamadas y
  Slack.
- Cuando las actualizaciones del CRM llegan tarde después de las reuniones.
- Cuando los administradores planean el despliegue del plugin en los equipos de ventas.

## Puntos clave
- El conector de Salesforce lee y actúa sobre los datos del CRM; el de Slack lee y escribe resúmenes de
  canales de deals e hilos del equipo de cuenta. Una skill de configuración crea en el primer uso un
  Claude Artifact adaptado al rol.
- Flujos: briefing matutino programado (con resumen semanal y borrador para el manager los viernes),
  preparación de llamadas, revisión de deals con un plan de cierre mutuo con fechas, seguimientos y
  actualizaciones de oportunidades tras cada reunión, y dashboards de pipeline y forecast compartibles.
- Salesforce sigue siendo el sistema de registro; Claude solo ve lo que permiten los permisos del vendedor
  y por defecto pide aprobación antes de cualquier escritura. Por defecto no se entrena con datos de clientes
  de Team/Enterprise.
- Beta en todos los planes de pago. El MCP de Salesforce se instala desde el marketplace; los admins
  solicitan acceso en AgentExchange, conectan Salesforce una vez para toda la organización y eligen qué
  grupos reciben el plugin.
- Lo usan GitLab, Siemens, Legora y 7.000 vendedores de Salesforce.

## Recursos incluidos
- Skill: `crm-seller-workflows` (`references/workflows.md`, `references/setup-and-permissions.md`,
  `templates/close-plan.md`, `templates/post-meeting-update.md`).

## Fuente
- https://claude.com/resources/articles/salesforce-in-claude
