[English](./fleet-of-agents.en.md) · [한국어](./fleet-of-agents.ko.md) · **Español** · [日本語](./fleet-of-agents.ja.md)

# Desplegar una flota gobernada de agentes

Cómo ABC Legal pasó de automatizaciones dispersas en escritorios a más de 50 agentes en producción, construidos en gran parte por personas que no son desarrolladores de software.

## El problema de partida

ABC Legal es una empresa estadounidense de entrega de documentos legales con 1.100 empleados. Cuando el CTO Brandon Fuller desplegó Claude Enterprise, la adopción ocurrió sola: equipos de notificación procesal, presentación electrónica y operaciones de representación letrada, además de marketing, cumplimiento y finanzas, empezaron a construir automatizaciones sin que nadie se lo pidiera.

> "Nuestros usuarios se volcaron de verdad. Vieron lo fácil que era usar conectores y herramientas, y de repente teníamos gente por toda la organización automatizando las tareas que siempre les habían comido el día."

Es la adopción que cualquier CTO espera, y también donde empieza el problema. **Los primeros agentes vivían donde su constructor los hubiera dejado: como tareas programadas en escritorios individuales.** Es decir, no podían ejecutarse desatendidos, no había una vista única de lo construido y nadie sabía cuánto costaba ni si se había ejecutado anoche.

Migrar a Claude Managed Agents dio a la compañía una estructura de despliegue común, espacios de trabajo compartidos, una sola superficie de auditoría y facturación, y agentes siempre activos en la nube en vez de en el portátil de alguien.

A julio de 2026:

- **más de 50 agentes** construidos con Managed Agents en producción
- **hasta un ~50% de reducción** en el coste de las tareas humanas que cubren algunos agentes, antes de una optimización profunda
- **~310 empleados** de todos los departamentos usando Claude en su trabajo diario

## Principio 1 — Tratar cada agente como software

> "Un agente es en realidad solo texto estructurado, un prompt más configuración, y todo lo que es texto puede vivir en un repositorio donde toda la empresa lo vea, lo revise y lo mejore."

El prompt de un agente, su lista de herramientas, su calendario, sus credenciales y su memoria van a archivos de configuración guardados en un repositorio git junto al software de la compañía. **Nada de un agente cambia salvo mediante un pull request que alguien aprueba**, lo que da a cada agente historial de versiones, revisión de código, rollback y traza de auditoría.

## Principio 2 — Construir primero el kit inicial

Fuller dedicó una semana a construir un kit inicial: dos plantillas, guardadas en repositorios git dedicados.

- **Agentes dirigidos por eventos** — arrancan en el momento en que ocurre algo, como la llegada de un nuevo trabajo o el retorno de un documento desde un tribunal.
- **Agentes programados** — se ejecutan por temporizador: cada hora, cada día o cada semana.

Cada agente vive en su propia carpeta con una estructura estándar: **un archivo de configuración JSON, un prompt de sistema en Markdown, scripts de despliegue y documentación operativa.** Fusionar un cambio en la rama principal despliega el agente automáticamente.

El camino del constructor es deliberadamente corto: clonar el repositorio, copiar una plantilla inicial, decirle a Claude Code qué debe hacer el agente y recibir todo lo que el agente necesita: configuración, prompt, almacén de credenciales y memoria. **Un constructor nunca tiene que escribir software.**

## Principio 3 — Demostrar que los no desarrolladores pueden desplegar

Fuller reunió al comité de dirección de 15 personas de la compañía —finanzas, marketing, operaciones y desarrollo, **ninguno desarrollador de software**— y les hizo clonar el repositorio y construir agentes con Claude Code.

El objetivo era demostrar que los no desarrolladores podían construir agentes de producción por sí mismos. Si cada agente tuviera que pasar por el equipo de desarrollo, ese cuello de botella limitaría la velocidad de toda la empresa. Lo que lo hizo seguro es que no estaban escribiendo software: rellenaban configuración y un prompt, y Managed Agents aportaba el entorno de ejecución.

> "Tuve que explicarles qué era un PR. Muchos de ellos pensaban que significaba correr, como un récord personal, lo más rápido que puedas. Ahora se mandan pull requests entre ellos."

En una semana, los 15 tenían agentes funcionando. Esos constructores volvieron a sus equipos y formaron a otros. **En un mes había unos 50 agentes o más en marcha.** Cada uno tiene un nombre, un responsable y un único trabajo.

## Qué hace la flota

ABC Legal tiene ahora un agente en casi cada etapa del proceso de presentación legal y de las operaciones que lo rodean:

- **AI Code Reviewer** — revisa cada pull request en cuatro bases de código con análisis multimodelo, detectando fallos de seguridad, regresiones de rendimiento y credenciales comiteadas. Los ingenieros esperan su revisión antes de fusionar.
- **EvidenceChain™ Delivery Agent** — asumió una tarea semanal manual: extrae un informe de base de datos con los trabajos coincidentes, recupera cada PDF con un navegador integrado en el agente y lo entrega al servidor FTP del cliente a diario. La gestora de cuenta que lo montó nunca había automatizado nada y lo construyó en aproximadamente una hora describiéndoselo a Claude Code.
- **eFiling Rejection Diagnoser** — se dispara cuando un tribunal rechaza una presentación, lee los detalles del trabajo, consulta las reglas del tribunal y publica un diagnóstico en Slack en aproximadamente un minuto. Antes consumía horas del día de un empleado.
- **Agente de verificación de trabajos** — navega el sitio web de un tribunal en un navegador, confirma que la vista o el caso está presentado adecuadamente y ocurre en la fecha indicada, y luego ajusta el trabajo, señalando jurisdicciones, tribunales y plazos de prescripción.
- **Attorney Coverage Agent** — trabaja la red de abogados para cubrir vistas: comprueba disponibilidad, escribe correos y lee las respuestas sobre disponibilidad y precio.
- **Agente de remesas de cuentas por cobrar** — analiza un correo de remesa, construye el archivo de aplicación de pagos de NetSuite y lo publica en Slack para aprobación con un clic, y luego lo importa. Un agente diario emite un veredicto de capitalizar o gastar sobre cada ticket de ingeniería.
- **Analista de Google Ads** — publica una recomendación semanal para el responsable del canal.
- **Charvis** — revisa trabajos de notificación completados y coincide con el equipo de cumplimiento aproximadamente el **98%** de las veces.
- **Service-Overdue-Nudger** — trabaja la capa de nivel 1 de los atrasos operativos y redacta mensajes de seguimiento diarios escalonados para aprobación humana.

## Principio 4 — Cosechar, afinar, repetir

Los agentes trabajan bajo supervisión humana, publicando lo que hicieron o recomiendan en Slack, donde la gente responde en hilos y reacciona con emojis. **Hank**, un agente interno de revisión de código, publica cada revisión en un canal compartido, nombrando el pull request y los recuentos resultantes, de modo que el rastro de lo que el agente decidió es público y buscable.

Todos esos datos de reacción son una señal de entrenamiento que se desperdicia si nada los recoge. **No todos los agentes lo necesitan**: la mayoría de la flota son ejecutores de una sola tarea cuya salida nadie califica, y trabajan solos.

Para los agentes que sí recogen retroalimentación calificada, ABC Legal usa una **arquitectura de tres roles**: agentes separados que comparten un espacio de trabajo, entorno y bóveda de credenciales, pero corren en calendarios distintos.

| Rol | Cadencia | Qué hace |
|---|---|---|
| **Agente Inicial** | Tiempo real | Hace el trabajo cuando llega un encargo o vuelve un documento, y registra una traza de auditoría de cada acción |
| **Cosechador** | Cada hora o cada día | Recoge la retroalimentación humana de Slack —respuestas en hilo y reacciones emoji— convirtiendo cada una en un punto de datos etiquetado |
| **Afinador** | Semanal | Mira todo a la vez y propone un cambio al prompt o la configuración **en lugar de a los pesos del modelo**. Solo redacta; un humano revisa y fusiona el pull request |

El patrón convierte mensajes de Slack en cambios versionados y aprobados por humanos al agente. Los agentes mejoran mediante los mismos flujos de trabajo que los desarrolladores ya usan.

### "Entregas como código": la variante de cuatro agentes

El mismo bucle afina configuración de negocio, no solo prompts. En Docketly, la empresa hermana de 50 personas, el trabajo se organiza en torno a entregas, cada una con su propio conjunto de reglas de enrutado y gestión. **Los ~145 conjuntos de reglas son archivos YAML individuales en git en lugar de registros en una pantalla de administración**, así que afinar una entrega significa editar un archivo y abrir un pull request.

Cuatro agentes forman el bucle: uno publica un veredicto semanal en Slack, el Cosechador convierte las reacciones en etiquetas, el Afinador abre un pull request sobre el YAML y un cuarto agente empuja la configuración fusionada a la base de datos de producción, ejecutando solo lo que un humano ya revisó y aprobó.

En la práctica, una reacción emoji que señala una entrega mal enrutada puede convertirse en un cambio fusionado de las reglas de enrutado de esa entrega dentro de la misma semana. **La revisión es el único paso manual del bucle.**

## Elegir el entorno de ejecución

Fuller evaluó varios frameworks antes de decidirse por Claude Managed Agents como el arnés agéntico de su organización. Sus criterios eran específicos: versionado, sesiones observables, facturación por espacio de trabajo, selección de modelo, primitivas de memoria, cableado MCP y, lo más crítico, **ninguna infraestructura que cuidar.**

La división de responsabilidades encaja limpiamente:

| Propiedad de la plataforma gestionada | Propiedad de ABC Legal |
|---|---|
| El bucle de ejecución | El prompt |
| Las sesiones | La lista de herramientas |
| La memoria | La lógica de disparo |
| La consola | La traza de auditoría |
| Los modelos | El bucle de retroalimentación sobre resultados |

Capacidades especialmente importantes a escala:

- **Versionado** — cada push crea una nueva versión del agente con bloqueo optimista. El rollback es trivial.
- **Flexibilidad de modelo** — Claude Sonnet por defecto para la mayoría de agentes, Claude Haiku para tareas de alto volumen y rápidas, y Claude Opus cuando un razonamiento más profundo justifica el coste. Cambiar de modelo es un cambio de una línea.
- **Cableado MCP y bóvedas de credenciales** — los agentes se conectan a la propia plataforma de ABC Legal (con más de 100 herramientas disponibles), a Metabase para informes, a Slack para la interacción con humanos y a Atlassian para gestión de proyectos.
- **Despliegues programados** — los agentes recurrentes corren con calendarios cron a través de Bitbucket Pipelines, que ya gestiona acceso al repositorio, secretos y facturación.

## El coste, medido

ABC Legal rastrea cada dólar de gasto en IA, desglosado por proveedor, herramienta, equipo y caso de uso. El gasto subió mientras la flota entraba en producción durante la primavera, y luego **empezó a caer en julio mientras el uso seguía creciendo**, resultado del trabajo de eficiencia descrito abajo.

El enfoque sobre el coste es deliberado: empujar el gasto hacia herramientas y agentes verticales y operativos donde el retorno es medible, manteniendo amplio el uso horizontal de chat e ideación y sus costes bajo control.

**La métrica es una ratio de eficiencia: el valor que entrega un agente medido contra lo que cuesta ejecutarlo.** Cada Managed Agent reporta su propio valor a un almacén de datos en cada ejecución, en horas y dólares. Los agentes siguen una **curva en J**: a menudo empiezan bajo el agua mientras son nuevos y usan modelos más grandes, y luego pasan a positivo cuando el equipo escribe evaluaciones, migra a modelos más baratos y rápidos y recorta tokens.

## La confianza, ganada

La mayoría de los agentes empiezan con un humano en el bucle: el agente mira el trabajo o el ticket y hace una recomendación para que una persona la revise antes de actuar. La recomendación se guarda en el trabajo y aparece en un banner para que la persona la acepte o rechace en su propio flujo, o se publica en un canal de Slack donde la gente responde en el hilo.

Esas respuestas construyen un conjunto de datos etiquetado de aciertos y errores, que alimenta el bucle de cosechador y afinador y permite al equipo escribir evaluaciones y comparar agentes entre modelos frontera. **Una vez que un agente demuestra ser tan bueno o mejor que los humanos en esa tarea concreta, pasa a modo automático y actúa por su cuenta**, y después permanece dentro del mismo marco de medición para vigilar cambios en su rendimiento.

## Los principios de trabajo de Fuller

- **Piensa en todo como código.** *"El código es solo texto estructurado. Los LLM son motores de texto. Cuanto más de tu negocio puedas convertir en texto en un repositorio, más palanca te dan los agentes."* Esto aplica al software tradicional e igualmente a prompts, esquemas, reglas de despacho, plantillas de notificación y configuraciones de negocio.
- **Empieza con humanos en el bucle.** Cada agente empieza publicando recomendaciones para revisión humana. Solo tras demostrar coincidencia consistente con las decisiones humanas se gana el derecho a actuar por su cuenta. *"Cada agente se gana la confianza antes de actuar solo. No empieza ahí."*
- **Usa el PR como superficie de control.** *"Si quieres un agente involucrado en una decisión, haz que la decisión parezca un pull request."* Comentarios línea a línea, flujos de aprobación y trazas de auditoría inmutables vienen gratis con el control de versiones, y componen de forma natural tanto con revisión de IA como humana.
- **Invierte en el bucle de retroalimentación.** El patrón cosechador-afinador significa que los agentes mejoran sin reentrenamiento. Respuestas en Slack y reacciones emoji se convierten en señales estructuradas que retroalimentan cambios de prompt y configuración, todo por el mismo flujo de pull request que los humanos ya usan.
- **Sáltate el desvío de las tareas programadas.** ABC Legal invirtió tiempo real construyendo tareas programadas y rutinas locales antes de migrar a Managed Agents, en gran parte porque el producto acababa de lanzarse en beta. El consejo de Fuller hoy es ir directo a Managed Agents.
- **Espera el obstáculo de git, no el de la IA.** La parte difícil fue lograr que los usuarios de negocio se sintieran cómodos clonando un repositorio y trabajando con Git y pull requests, más que cualquier cosa sobre la IA en sí. Funcionó, y rápido, pero fue un obstáculo real que a Fuller le gustaría ver aliviado en las propias herramientas.
- **No toda tarea merece un agente.** El coste es real, así que cada equipo tiene que pensar en términos de valor sobre coste. El trabajo consiste en escoger problemas abordables que de verdad ahorren tiempo o creen automatización, y estar dispuesto a decir que una tarea dada no merece un agente.

## Qué viene después

La flota sigue creciendo. Entre los proyectos en curso hay un revisor de fotos de notificación, un agente de triaje de PagerDuty, un resumen diario de KPI y bucles de Afinador ampliados sobre agentes existentes. El equipo también identifica más candidatos a "X como código": plantillas de notificación, reglas de enrutado de eventos y lógica de despacho que puedan moverse a repositorios donde los agentes puedan leerlos, razonar sobre ellos y proponer mejoras.

> "Queremos que la IA sostenga un negocio capaz de funcionar solo, con los empleados libres para dirigirlo." — Brandon Fuller, CTO, ABC Legal

## Fuente

- https://claude.com/blog/how-abc-legal-turned-every-employee-into-a-builder-with-claude-managed-agents
