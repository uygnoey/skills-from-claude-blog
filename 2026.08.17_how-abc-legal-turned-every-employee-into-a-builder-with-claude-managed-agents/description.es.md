[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Una historia de cliente sobre ABC Legal, una empresa estadounidense de entrega de documentos legales con 1.100 empleados, contada en gran parte a través de su CTO, Brandon Fuller. Tras el despliegue de Claude Enterprise, los equipos empezaron a construir automatizaciones por su cuenta, pero esos primeros agentes vivían como tareas programadas en escritorios individuales. Migrar a Claude Managed Agents dio a la compañía una única estructura de despliegue, espacios de trabajo compartidos, una sola superficie de auditoría y facturación, y agentes siempre activos en la nube.

A julio de 2026 el equipo registraba más de 50 agentes en producción, hasta un ~50% de reducción en el coste de las tareas humanas que cubren algunos agentes antes de una optimización profunda, y unos 310 empleados de todos los departamentos usando Claude en su trabajo diario.

El post trata sobre todo del modelo operativo: definir cada agente como código, enseñar a los no desarrolladores a desplegar mediante pull requests, y cerrar un bucle de retroalimentación que convierte reacciones de Slack en cambios de prompt fusionados.

## ¿Cuándo es útil?
- Cuando la adopción de IA es entusiasta pero dispersa: automatizaciones que viven en portátiles individuales sin una vista compartida de qué existe, cuánto cuesta o si se ejecutó anoche.
- Cuando quieres que los no desarrolladores construyan automatizaciones de producción sin que el equipo de desarrollo se convierta en el cuello de botella.
- Cuando los agentes necesitan historial de versiones, revisión de código, rollback y traza de auditoría en lugar de una pantalla de administración.
- Cuando hay retroalimentación humana sobre la salida de los agentes y ningún mecanismo que la convierta en mejora.
- Cuando necesitas una forma defendible de decidir qué tareas merecen un agente.

## Puntos clave
- **Cada agente se define como código.** "Un agente es en realidad solo texto estructurado, un prompt más configuración, y todo lo que es texto puede vivir en un repositorio donde toda la empresa lo vea, lo revise y lo mejore." Prompt, lista de herramientas, calendario, credenciales y memoria van a archivos de configuración en un repositorio git junto al software de la compañía. Nada cambia salvo mediante un pull request aprobado.
- **Un kit inicial, construido en una semana, fue lo que hizo que se extendiera.** Dos plantillas en repositorios git dedicados: una para agentes dirigidos por eventos y otra para agentes programados. Cada agente vive en su propia carpeta con una estructura estándar: un archivo de configuración JSON, un prompt de sistema en Markdown, scripts de despliegue y documentación operativa. Fusionar a la rama principal despliega automáticamente. El constructor clona el repositorio, copia una plantilla, le dice a Claude Code qué debe hacer el agente y recibe configuración, prompt, almacén de credenciales y memoria.
- **Los no desarrolladores fueron la prueba.** Un comité de dirección de 15 personas de finanzas, marketing, operaciones y desarrollo —ninguno desarrollador de software— clonó el repositorio y construyó agentes con Claude Code. Los 15 tenían agentes funcionando en una semana; esos constructores formaron a sus equipos y en un mes había más de 50 agentes en marcha. Cada agente tiene un nombre, un responsable y un único trabajo.
- **La parte difícil fue git, no la IA.** "Tuve que explicarles qué era un PR." Conseguir que los usuarios de negocio se sintieran cómodos clonando un repositorio y trabajando con pull requests fue el obstáculo real.
- **Los agentes se supervisan por Slack, y las reacciones son señal de entrenamiento.** Para los agentes cuya salida la gente califica, una arquitectura de tres roles comparte un espacio de trabajo, entorno y bóveda de credenciales, pero corre en calendarios distintos: el Agente Inicial hace el trabajo en tiempo real y registra una traza de auditoría; el Cosechador se ejecuta cada hora o cada día y convierte respuestas en hilo y reacciones emoji en puntos de datos etiquetados; el Afinador se ejecuta semanalmente y propone un cambio al prompt o a la configuración —nunca a los pesos del modelo— como un pull request que un humano revisa y fusiona. No todos los agentes lo necesitan: la mayoría de la flota son ejecutores de una sola tarea cuya salida nadie califica.
- **"X como código" se generaliza.** En la empresa hermana Docketly, unos 145 conjuntos de reglas de entrega son archivos YAML individuales en git en lugar de registros en una pantalla de administración, así que afinar una entrega significa editar un archivo y abrir un PR. Cuatro agentes forman el bucle, incluido un cuarto que empuja la configuración fusionada a la base de datos de producción, ejecutando solo lo que un humano ya aprobó. Una reacción emoji que señala una entrega mal enrutada puede convertirse en un cambio de reglas fusionado en la misma semana.
- **Los criterios de selección de plataforma fueron específicos**: versionado, sesiones observables, facturación por espacio de trabajo, selección de modelo, primitivas de memoria, cableado MCP y ninguna infraestructura que cuidar. La infraestructura gestionada de Anthropic posee el bucle de ejecución, las sesiones, la memoria, la consola y los modelos; ABC Legal posee el prompt, la lista de herramientas, la lógica de disparo, la traza de auditoría y el bucle de retroalimentación.
- **El coste se mide, no se supone.** La métrica es una ratio de eficiencia —el valor entregado frente al coste de ejecución— y cada agente reporta su propio valor a un almacén de datos en horas y dólares en cada ejecución. Los agentes siguen una curva en J: bajo el agua mientras son nuevos y usan modelos más grandes, y luego positivos cuando el equipo escribe evaluaciones, migra a modelos más baratos y rápidos y recorta tokens. El gasto subió durante la primavera y luego cayó en julio mientras el uso seguía creciendo.
- **La confianza se gana, no se concede.** La mayoría de los agentes empiezan con un humano en el bucle, publicando una recomendación en el trabajo o en un canal de Slack. Esas respuestas construyen un conjunto de datos etiquetado que sirve para evaluaciones y comparativas entre modelos frontera. Solo cuando un agente demuestra ser tan bueno o mejor que los humanos en esa tarea pasa a modo automático, y después permanece dentro del mismo marco de medición.

## Recursos incluidos
- `skills/agent-fleet-as-code/SKILL.md` — cómo operar una flota de agentes como código, con los PR como superficie de control.
- `skills/agent-fleet-as-code/templates/agent-config.json` — la configuración JSON estándar por agente.
- `skills/agent-fleet-as-code/templates/system-prompt.md` — la plantilla de prompt de sistema en Markdown.
- `skills/agent-fleet-as-code/templates/operations.md` — la documentación operativa que lleva cada carpeta de agente.
- `skills/agent-fleet-as-code/templates/deploy.sh` — el script de despliegue que referencia la estructura estándar.
- `skills/agent-fleet-as-code/references/starter-kit.md` — las dos plantillas iniciales y la disposición estándar de la carpeta de agente.
- `skills/agent-fleet-as-code/references/self-improving-loop.md` — la arquitectura de cosechador y afinador en detalle.
- `skills/agent-fleet-as-code/references/cost-and-trust.md` — la ratio de eficiencia, la curva en J y la escalera de confianza con humano en el bucle.
- `skills/agent-fleet-as-code/examples/agent-fleet.md` — los agentes que ABC Legal realmente ejecuta.
- `agents/initial-agent.md`, `agents/feedback-harvester.md`, `agents/config-tuner.md`, `agents/config-deployer.md` — los cuatro roles nombrados en el post.
- `guides/fleet-of-agents.{en,ko,es,ja}.md` — la guía de despliegue completa en cuatro idiomas.

## Fuente
- https://claude.com/blog/how-abc-legal-turned-every-employee-into-a-builder-with-claude-managed-agents
