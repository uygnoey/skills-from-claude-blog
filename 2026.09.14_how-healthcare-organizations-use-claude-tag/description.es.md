[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un artículo de buenas prácticas (14 de septiembre de 2026) de Camy Pearson, Maria Howe y Araba Koomson
sobre cómo las organizaciones sanitarias usan Claude Tag (beta, Claude en Slack) en flujos de trabajo que
nunca tocan información de salud protegida (PHI), con ejemplos de Insight Health, Tennr y Medallion.

## ¿Cuándo es útil?
- Cuando un equipo sanitario o regulado quiere un compañero de IA en Slack pero debe mantener fuera la PHI.
- Al elegir canales, conectores y niveles de autonomía para un piloto de Claude Tag.
- Al buscar casos de uso sin PHI ya probados: respuesta a incidentes, herramientas internas, reglas de aseguradoras.

## Puntos clave
- Claude Tag aún no está cubierto por el BAA de Anthropic, así que solo se usa en canales y conectores sin PHI.
- Controles de administración: desactivado por defecto, lista de canales aprobados, mensajes directos
  desactivados, conectores por canal y paquetes de acceso que excluyen el EHR, los sistemas clínicos y las
  comunicaciones con pacientes. Solo ve lo que puede ver el miembro que lo invoca.
- Insight Health combina Claude Tag con Zeus, un agente del Agent SDK cubierto por el BAA que enmascara la
  PHI; el 97 % de las alertas del canal crítico se cerraron sin intervención de un ingeniero.
- Tennr usa Claude Tag como mantenedor principal de un portal interno de ofertas (más de 15 tickets en un mes).
- Medallion acumula en un canal el conocimiento sobre reglas de aseguradoras y etiqueta a expertos cuando
  Claude no está seguro.
- Empieza con un canal y uno o dos conectores, conecta GitHub y haz un piloto de dos semanas.
- Los créditos (25.000 USD Enterprise / 2.500 USD Team con 10+ puestos) vencieron el 1 de octubre de 2026.

## Recursos incluidos
- Skill: `phi-safe-slack-agent-rollout` (`references/customer-patterns.md`,
  `templates/rollout-checklist.md`).

## Fuente
- https://claude.com/resources/articles/how-healthcare-organizations-use-claude-tag
