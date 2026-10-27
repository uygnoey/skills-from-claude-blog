[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un artículo de buenas prácticas del 27 de octubre de 2026, basado en un webinar con Google Cloud. Explica
a los equipos de plataforma cómo gestionar el gasto de Claude Code en Google Cloud y demostrar su valor
con tres palancas independientes: controlar, rastrear y demostrar.

## ¿Cuándo es útil?
- Vas a desplegar Claude Code en Google Cloud y necesitas barreras, presupuestos y política de modelos.
- El gasto crece y debes distinguir el uso intensivo de alto valor del desperdicio.
- Estás creando paneles de uso o tienes que mostrar a la dirección el ROI de Claude Code.

## Puntos clave
- La factura es tokens por tarea por precio del modelo. El trabajo agéntico consume más tokens por tarea
  que el chat, así que elegir el modelo adecuado para cada tarea es una palanca importante. Importa más
  el costo por tarea que el precio por token.
- Caja de herramientas: facturación por proyecto, presupuestos y alertas, topes de gasto (Preview),
  exportaciones a BigQuery, cuotas y throughput aprovisionado de Google Cloud, además del Claude apps
  gateway autoalojado con inicio de sesión mediante el IdP.
- Controlar - guiar, no restringir: topes de gasto del gateway por usuario, grupo del IdP u organización,
  por día, semana o mes (valores por desarrollador que cada miembro hereda, no un fondo compartido),
  avisos en la CLI al pasar el 75 % y el 95 %, respuesta 429 al llegar al tope, modelos por defecto y
  listas de modelos permitidos por grupo, y una API de administración para los topes. El desperdicio se
  esconde en la franja media de los grandes consumidores (modelos caros para tareas rutinarias, tareas
  programadas olvidadas).
- Rastrear: OpenTelemetry de Claude Code por usuario, equipo, modelo, skill, plugin, agente y servidor
  MCP; telemetría gestionada por el gateway con identidad verificada; `OTEL_RESOURCE_ATTRIBUTES` para
  centros de costo; una plantilla de panel de Cloud Monitoring; un quickstart de OTel que lleva los
  eventos a BigQuery con consultas SQL; exportaciones de Cloud Billing a BigQuery.
- Demostrar: adopción y uso, satisfacción de los desarrolladores (encuesta antes y después) e impacto
  (tiempo, esfuerzo, volumen) frente a una línea base. Define una unidad de trabajo, como un PR fusionado
  y etiquetado; los "PR creados" de la telemetría no son "PR fusionados", así que crúzalos con el control
  de versiones y los tickets. El registro de prompts es opcional (opt-in).
- Casos de clientes: Delivery Hero, Shopify y Fifth Dimension. Empieza con valores por defecto (tope
  para toda la organización, modelo por defecto, lista permitida) y ajústalos por rol y equipo en un
  ciclo continuo.

## Recursos incluidos
- Skill: `coding-agent-spend-roi` (`references/governance-toolbox.md`, `references/telemetry-and-tracking.md`,
  `references/roi-metrics.md`, `references/resources.md`, `examples/customer-outcomes.md`,
  `templates/rollout-defaults.md`, `templates/roi-report.md`, `templates/otel-resource-attributes.env`).
- Guía: `guides/cost-and-roi-on-google-cloud.{en,ko,es,ja}.md`.

## Fuente
- https://claude.com/resources/articles/how-to-manage-costs-and-demonstrate-roi-for-claude-code-on-google-cloud
