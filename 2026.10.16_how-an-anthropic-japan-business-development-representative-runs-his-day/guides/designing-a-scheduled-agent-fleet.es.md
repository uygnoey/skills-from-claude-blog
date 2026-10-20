[English](./designing-a-scheduled-agent-fleet.en.md) · [한국어](./designing-a-scheduled-agent-fleet.ko.md) · **Español** · [日本語](./designing-a-scheduled-agent-fleet.ja.md)

# Diseñar una flota de agentes programados

Una metodología para sustituir un flujo de trabajo diario y repetitivo por un grupo reducido de
agentes programados, a partir de cómo un representante de desarrollo de negocio del equipo de
Anthropic en Japón construyó la flota "Nakama", la prototipó en Claude y la trasladó a Claude
Managed Agents.

## La forma del problema

La versión manual de este trabajo no es difícil: es temprana y constante. Un par de horas cada mañana
enrutando y calificando leads, después escribir correos en japonés o inglés y, con el tiempo que
sobre, actualizar el CRM, normalmente con un día o más de retraso.

Lo que cambia con una flota no es que el trabajo desaparezca, sino quién produce la primera versión.
Los agentes preparan casi todo antes de que empiece el día y la persona revisa.

## Etapa 1 — Reparte el trabajo: un trabajo por agente

Escribe el día como los pasos que realmente haces y da a cada paso su propio agente. Una
responsabilidad única mantiene cada agente fácil de razonar y fácil de seguir cuando algo falla.

La flota original quedó en seis agentes: un enrutador que da dueño a cada lead entrante antes de que
el equipo empiece, un triador que califica y redacta el primer contacto, un redactor de respuestas
que corre cada hora, un actualizador del CRM, un resumidor de fin de día y un coordinador que
modifica a los otros cinco.

Dos reglas hacen que el reparto funcione:

1. **Cada agente reporta en algún sitio.** El enrutador publica un informe de ejecución —todos los
   leads entrados, todos los asignados— en un canal dedicado, para que el relevo se pueda comprobar
   en lugar de suponerse.
2. **Un reglamento escrito define cada carril.** Las preguntas de precio, las cuentas sensibles y las
   peticiones ambiguas van a la persona. Nada improvisa para saltarse ese límite.

## Etapa 2 — Prototipa en Claude, no en infraestructura

No necesitas infraestructura gestionada para empezar. El prototipo son tres piezas por agente: una
skill con las instrucciones de un trabajo, una tarea programada para que corra sin ti y una carpeta
compartida como base de conocimiento donde cada skill escribe lo que aprende.

La primera versión será tosca y funcionará igual. Entrega a Claude una pieza del trabajo a la vez,
corrige lo que haga mal y guarda la corrección. No escribas un prompt detallado para cada ejecución:
describe el trabajo una vez, deja que Claude redacte, arregla el borrador y conserva el arreglo.

## Etapa 3 — Muévete cuando el problema sea el seguimiento

El prototipo se queda corto por dos razones, y ninguna es de capacidad.

- **Compartir es mandar un zip.** Los compañeros que quieren el montaje reciben skills y unos cuantos
  archivos Markdown que deben subir y sobre los que luego tienen que contestar preguntas de
  configuración antes de que algo funcione.
- **Nada tiene una definición única.** Cada agente es una skill, una tarea programada y una carpeta,
  editados desde cualquier conversación abierta: la misma skill se cambia desde muchos sitios.

El objetivo de mudarse es definir cada agente una vez, en un lugar, con cada cambio visible. La
migración es un mapeo, no una reescritura: la skill pasa a ser el prompt de sistema, la tarea
programada una programación del deployment, la carpeta compartida un almacén de memoria y los accesos
a servicios unas bóvedas con permisos limitados.

Tampoco hace falta ser desarrollador. Describe el trabajo de cada agente en lenguaje natural, deja que
Claude escriba los scripts cortos de configuración y ejecútalos desde una terminal. Si empiezas de
cero, el quickstart de la Console trae plantillas de agentes listas para usar.

## Etapa 4 — Opera la flota

Tres propiedades hacen el trabajo operativo.

**Ejecuciones en segundo plano.** Los agentes corren según su programación con el portátil abierto o
cerrado, sin cron jobs que mantener aparte. Una ejecución fallida se puede abrir y revisar paso a
paso. Mientras se prueba un cambio, las ejecuciones programadas siguen usando la versión desplegada,
así que una edición a medias nunca aterriza en la ejecución de mañana.

**Una memoria compartida.** Todos los agentes leen y escriben en el mismo almacén: la diferencia
entre lo que redactaron y lo que la persona envió, más lo que averiguaron investigando. Una frase
corregida una vez en el redactor de respuestas evita que el triador y el agente de fin de día repitan
el error. Por eso la base de conocimiento importa más que el prompt: el contexto viene del almacén y
los prompts se quedan cortos.

**Credenciales con alcance limitado.** Las credenciales viven en bóvedas gestionadas. Cada deployment
usa solo las que su trabajo necesita, nunca las ve y el acceso se revoca en un paso.

Los cambios en la flota pasan por el coordinador: publica la petición en lenguaje natural en un canal
restringido a quien puede cambiar instrucciones, y el coordinador la recoge en un ciclo corto y guarda
la edición como una versión nueva.

## Etapa 5 — Entrega lo que sale de la rutina

Algunos asuntos requieren un paso que la rutina no cubre: una vía de actualización, un proceso de
compra, un escalado a otro equipo. Los agentes no se detienen a esperar: publican el asunto en el canal
compartido y etiquetan a Claude Tag, que lee el hilo, comprueba las reglas y los términos aplicables,
expone las opciones, redacta lo necesario y etiqueta a una persona cuando hace falta revisión o
aprobación. Cuando otro tiene que responder primero, se pone su propio recordatorio para volver a
mirar e informa del estado en el mismo hilo.

## Etapa 6 — Mantenla eficiente

Los agentes programados corren todos los días aunque nadie mire, así que el desperdicio se acumula.
La mayor parte de la eficiencia está en el diseño: un trabajo por agente, una programación en vez de
un bucle y memoria compartida para corregir una sola vez.

El resto es la elección del modelo. Los agentes guiados por reglas usan el modelo pequeño. Los que
requieren criterio usan el grande —el coordinador más que ninguno, porque una mala edición llega a
todos los agentes—. El caso interesante es el agente que necesita criterio *y* corre
constantemente: ejecútalo en el modelo pequeño y deja que pida consejo al grande cuando se atasque,
recibiendo un plan, una corrección o una señal de alto. El nivel de esfuerzo se configura aparte del
modelo; súbelo solo donde el razonamiento sea difícil.

Vale la pena nombrar los tres errores comunes, porque es fácil caer en ellos: añadir a las
instrucciones en vez de actualizarlas, dar a los agentes más contexto del que su tarea necesita y
ejecutar todo en el modelo más grande con el esfuerzo más alto.

## Qué esperar

En la flota original, contando cada tarea por el tiempo que habría llevado hacerla a mano, los
agentes se encargan de unas 60 horas de trabajo a la semana. El tiempo que se libera va a lo que los
agentes aún no hacen bien: conversaciones con clientes, estrategia de outbound, proyectos
transversales y ayudar a los compañeros a montar sus propias flotas.

Tres lecciones del autor que conviene llevarse a tu propio montaje:

- No necesitas un prompt detallado cada vez. Describe el trabajo una vez, arregla el borrador y deja
  que Claude conserve el arreglo.
- La base de conocimiento importa más que el prompt. Hicieron falta unos cientos de rondas baratas de
  redactar, corregir y guardar para que los borradores sonaran como él.
- Da más espacio a los agentes, y antes. Las tareas que daba por suyas —actualizar la base de
  conocimiento, editar las instrucciones a mano— funcionaron bien en cuanto las soltó.

## Fuente

[How an Anthropic BDR in Japan runs his day with Claude Managed Agents](https://claude.com/resources/articles/how-an-anthropic-japan-business-development-representative-runs-his-day)
(publicado el 2026-10-16).
