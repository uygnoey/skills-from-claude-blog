[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un representante de desarrollo de negocio del equipo de Anthropic en Japón describe la flota de
agentes programados —el "Nakama"— que vacía su cola de leads entrantes, redacta correos bilingües a
clientes y mantiene Salesforce al día. Primero prototipó cada agente en Claude como una skill más una
tarea programada más una carpeta compartida; después trasladó la flota a Claude Managed Agents (beta)
y delega en Claude Tag, dentro de Slack, los pasos que salen de la rutina.

## ¿Cuándo es útil?
- Cuando un flujo de trabajo diario y repetitivo (enrutar leads, calificarlos, redactar respuestas,
  actualizar el CRM, hacer seguimiento) es lo bastante grande para repartirlo entre varios agentes de
  propósito único.
- Cuando los agentes prototipados en Claude ya son demasiados para seguirles la pista editando skills
  desde cualquier conversación abierta, y quieres definir cada agente una sola vez con un historial
  versionado.
- Cuando los agentes programados deben ejecutarse con el portátil cerrado, compartir una misma
  memoria y acceder a servicios externos con credenciales que puedas limitar y revocar.
- Cuando quieres controlar el coste de agentes que se ejecutan a diario ajustando el modelo y el
  nivel de esfuerzo al trabajo de cada uno.

## Puntos clave
- Un trabajo por agente. La flota tiene seis: Furiwake (reparte la cola entrante entre los
  representantes), Sabaki (califica los leads del autor y redacta el primer correo), Henji (revisa el
  buzón cada hora y prepara respuestas en japonés o inglés), Shoudan (envía actualizaciones a
  Salesforce), Nokori (al final del día resume reuniones y redacta los seguimientos) y un coordinador
  que actualiza las instrucciones de los demás agentes y la base de conocimiento compartida.
- Prototipa primero en Claude: una skill por agente, una tarea programada por skill y una carpeta
  compartida como base de conocimiento. Pasa a Managed Agents cuando tengas más agentes de los que
  puedas seguir con comodidad.
- En Managed Agents la skill se convierte en el prompt de sistema del agente, la tarea programada en
  una programación del deployment y la carpeta compartida en un almacén de memoria; cada cambio de
  instrucciones se guarda como una versión nueva y las ediciones a medias no llegan a las ejecuciones
  programadas.
- Todos los agentes leen y escriben en el mismo almacén de memoria: guardan la diferencia entre lo
  que redactaron y lo que el autor envió de verdad, así que una corrección se propaga a toda la flota.
- Las credenciales viven en bóvedas gestionadas con permisos limitados y revocables; cada deployment
  usa solo las bóvedas que su trabajo necesita y nunca ve las credenciales.
- Las peticiones de cambio se escriben en lenguaje natural en el canal de Slack de la flota (solo el
  autor puede pedir cambios de instrucciones); el coordinador revisa el canal cada 15 minutos
  aproximadamente y los aplica.
- Lo que sale de la rutina se entrega a Claude Tag en Slack, que expone las opciones, redacta lo
  necesario, se pone sus propios recordatorios de seguimiento y etiqueta a una persona cuando hace
  falta revisión o aprobación.
- El control de coste es diseño más elección de modelo: los agentes guiados por reglas (Furiwake,
  Shoudan) usan Sonnet; los que requieren más criterio (Sabaki, Nokori, el coordinador) usan Opus;
  Henji funciona todo el día con Sonnet y aplica la estrategia del asesor para consultar a Opus
  cuando se atasca. El nivel de esfuerzo se configura aparte del modelo.
- Resultado medido por el autor: la flota se encarga de unas 60 horas de trabajo a la semana,
  contando cada tarea por el tiempo que le habría llevado hacerla a mano.
- Lecciones: describe el trabajo una vez y deja que Claude conserve tus correcciones; la base de
  conocimiento importa más que el prompt; entrega antes más trabajo a los agentes.

## Recursos incluidos
- Skill: `scheduled-agent-fleet` — diseñar, prototipar y operar una flota de agentes programados de
  propósito único, con referencias sobre los roles, la memoria compartida y las credenciales, y la
  asignación de modelo/esfuerzo, más un ejemplo de migración del prototipo a Managed Agents.
- Agents: los seis roles nombrados en el post (`furiwake-lead-router`, `sabaki-lead-triage`,
  `henji-reply-drafter`, `shoudan-crm-updater`, `nokori-day-closer`, `fleet-coordinator`).
- Guide: "Diseñar una flota de agentes programados" en cuatro idiomas.

## Fuente
- https://claude.com/resources/articles/how-an-anthropic-japan-business-development-representative-runs-his-day
