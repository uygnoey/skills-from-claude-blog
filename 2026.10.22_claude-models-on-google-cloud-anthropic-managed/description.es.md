[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un anuncio (22 de octubre de 2026) de que Claude Models on Google Cloud (Anthropic managed) ya está
disponible de forma general: los clientes de Google Cloud obtienen todas las funciones de Claude Platform
con IAM, facturación y consumo de compromisos de Google Cloud. Claude sigue disponible también mediante
la oferta Google managed.

## ¿Cuándo es útil?
- Cuando un cliente de Google Cloud debe elegir entre las ofertas Anthropic managed y Google managed.
- Cuando un equipo quiere las nuevas funciones y betas de Claude desde el primer día sin salir de Google Cloud.
- Al planificar facturación, IAM y descuentos antes de la incorporación.

## Puntos clave
- Anthropic managed: todas las funciones de la API de Claude, con nuevas funciones y betas el mismo día
  que en Claude Platform nativa. Anthropic opera el servicio y actúa como encargado del tratamiento de datos.
- Funciona con las credenciales IAM existentes de Google Cloud; se factura en una sola factura de Google
  Cloud y consume el compromiso de Google Cloud. Por ahora, endpoints US y Global.
- Incluye: Managed Agents (beta), ejecución de código, uso de computadora, agent skills, estrategia de
  asesor (beta), Files API, citas, búsqueda y obtención web, conector MCP (beta), caché de prompts y
  procesamiento por lotes.
- Fast Mode en Claude Opus 5.5 está disponible de forma general aquí: salida hasta 2,5 veces más rápida,
  8 / 40 USD por millón de tokens de entrada / salida.
- Acceso a Claude Console para escribir prompts, configurar agentes y ejecutarlos en entornos alojados,
  monitorizar uso y costes y gestionar el acceso por espacio de trabajo. Modelos: Fable 5.1, Opus 5.5,
  Sonnet 5.5, Haiku 5.5.
- Google managed sigue siendo la opción cuando Google debe ser el encargado del tratamiento, hay
  requisitos estrictos de residencia regional o se necesitan integraciones nativas como Model Armor o
  Agent Engine.
- Si ya tienes un descuento, contacta primero con tu ejecutivo de cuenta; los descuentos no se aplican
  de forma retroactiva.

## Recursos incluidos
- Skill: `google-cloud-offering-selector` (`references/feature-matrix.md`,
  `templates/offering-decision.md`).

## Fuente
- https://claude.com/resources/articles/claude-models-on-google-cloud-anthropic-managed
