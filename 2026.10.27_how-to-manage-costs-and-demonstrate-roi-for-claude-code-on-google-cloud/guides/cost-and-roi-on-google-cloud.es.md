[English](./cost-and-roi-on-google-cloud.en.md) · [한국어](./cost-and-roi-on-google-cloud.ko.md) · **Español** · [日本語](./cost-and-roi-on-google-cloud.ja.md)

# Costo y ROI de Claude Code en Google Cloud: controlar -> rastrear -> demostrar

Resumen metodológico de la guía de Anthropic para equipos de plataforma que usan Claude Code en Google Cloud.

## 1. Por qué la factura es como es
Claude en Google Cloud se cobra por consumo: la adopción genera uso, el uso es lo que pagas y también es
donde aparece el valor. Costo = tokens por tarea x precio del modelo. Las herramientas agénticas leen
archivos, ejecutan herramientas y razonan sobre toda la tarea, por lo que consumen más tokens por tarea
que el chat. Elegir el modelo adecuado para cada tarea es el otro gran control. La visibilidad viene del
Claude apps gateway y de los servicios de Google Cloud.

## 2. La caja de herramientas
| Capa | Capacidades |
|---|---|
| Google Cloud | Facturación por proyecto, presupuestos y alertas, topes de gasto (Preview), exportaciones a BigQuery, cuotas (solicitudes y tokens de entrada/salida por minuto, por familia de modelos y ubicación), throughput aprovisionado |
| Claude apps gateway | Autoalojado, en el mismo binario `claude`, se ejecuta en tu proyecto; inicio de sesión con el IdP (p. ej. Google Workspace) para que cada solicitud tenga identidad verificada; listas de modelos permitidos por grupo; topes de gasto por usuario, grupo del IdP u organización, por día, semana o mes |

## 3. Palanca 1 - Controlar
Guiar en lugar de restringir. Las sesiones costosas suelen ser de usuarios avanzados que hacen trabajo de
alto valor; el desperdicio está en la franja media de los grandes consumidores (un modelo caro para una
tarea rutinaria, una tarea programada olvidada).
- **Topes de gasto**: por usuario, grupo u organización; los de grupo y organización son valores por
  desarrollador heredados, no un fondo compartido.
- **Alertas de umbral**: avisos en la CLI al pasar el 75 % y el 95 %; 429 en el tope hasta que se
  reinicie el periodo o se suba. Las alertas de Cloud Billing son para administradores.
- **Modelos por defecto y listas permitidas**: por grupo del IdP, aplicadas en el servidor. Casi todos
  mantienen el modelo por defecto.
- **API de administración del gateway**: cambia topes por programa, p. ej. desde tickets.

## 4. Palanca 2 - Rastrear
- OpenTelemetry de Claude Code: sesiones, tiempo activo, líneas de código, commits, PR, tokens y costo,
  por usuario, equipo y modelo, y ahora también por skill, plugin, agente y servidor MCP. Se envía por
  OTLP mediante un colector o el gateway.
- Telemetría del gateway: un único destino para todos; exportaciones etiquetadas con correo verificado y
  grupos del IdP.
- `OTEL_RESOURCE_ATTRIBUTES` (p. ej. `department=engineering,cost_center=eng-123`) para vistas por centro
  de costo en Cloud Monitoring, Grafana o Splunk.
- Paneles: desarrolladores activos, sesiones de las últimas 24 horas, tokens y solicitudes bloqueadas
  (combínalas con un flujo de tickets para subir el tope). La plantilla "Claude Code Monitoring" se puede
  copiar desde la consola de Cloud Monitoring.
- Quickstart de OTel: Cloud Logging/Monitoring más tablas particionadas de BigQuery por tipo de evento
  (solicitudes a la API, decisiones de herramientas, resultados de herramientas, respuestas del
  asistente, ejecuciones de hooks) con SQL para gasto por desarrollador/modelo, éxito y latencia de
  herramientas, tiempo de espera de hooks y análisis por turno y sesión.
- Cloud Billing a BigQuery: filtra los SKU de Claude por modelo y tipo de token.

## 5. Palanca 3 - Demostrar
| Dimensión | Ejemplos | Fuente |
|---|---|---|
| Adopción y uso | Usuarios activados, uso diario/semanal, retención, usuarios avanzados | OTel |
| Satisfacción | Satisfacción, ahorro de tiempo percibido, confianza, fricción | Encuesta antes/después + seguimientos |
| Impacto | Tiempo (PR abierto -> fusionado, plazo de revisión); esfuerzo (iteraciones, comentarios y retrabajo por PR); volumen (PR por ingeniero, frecuencia de despliegue, trabajos concretos) | Línea base de control de versiones + tickets |

**Unidad de trabajo**: cuenta PR fusionados de una clase definida (Claude lo abre, una persona decide si
se publica), identificados por etiqueta, ID de ticket y participación de Claude. Para trabajo que no es
un PR, cuenta una cosa terminada donde queda registrada.

**Telemetría nativa**: tasa de aceptación, líneas modificadas, commits, PR creados, PR por usuario, costo
por unidad de resultado. Los PR creados no son PR fusionados: crúzalos con GitHub/GitLab y los tickets.
El registro de prompts es opt-in y muestra valor fuera de los PR (un SRE depurando un incidente, un
ingeniero de ventas generando datos para una demo).

## 6. Resultados de referencia
- Delivery Hero: renovación de un sistema de diseño en 100 componentes de UI en minutos en lugar de una semana.
- Shopify: personas no ingenieras crean herramientas internas en minutos en lugar de días.
- Fifth Dimension: más de 300 000 líneas de código al mes con un 98 % de aceptación.

## 7. Primeros pasos
Un ciclo continuo: empieza con un tope de gasto para toda la organización, un modelo por defecto y una
lista de modelos permitidos; ajusta por rol y equipo a medida que llegan los datos; relaciona las
métricas con el valor y repórtalo a las partes interesadas.

## Fuente
- https://claude.com/resources/articles/how-to-manage-costs-and-demonstrate-roi-for-claude-code-on-google-cloud
