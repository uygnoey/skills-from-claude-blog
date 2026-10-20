[English](./coachable-human-agent-teams.en.md) · [한국어](./coachable-human-agent-teams.ko.md) · **Español** · [日本語](./coachable-human-agent-teams.ja.md)

# Equipos humano-agente que se pueden entrenar: lecciones de Asana

El tercer post de la serie de Claude sobre equipos humano-agente (tras la IA multijugador en Anthropic y
Slack como contexto para agentes). Arnab Bose, Chief Product Officer de Asana, explica cómo Asana opera
agentes de IA como compañeros de equipo dentro de su modelo Work Graph®: la red de tareas, proyectos,
objetivos y conversaciones con responsables, colaboradores y dependencias definidos.

## Decisión de diseño: los agentes viven en el mismo modelo de trabajo
En lugar de añadir nuevas estructuras de contexto para la IA, los agentes de Asana operan dentro del
modelo existente. Tienen roles definidos, reciben tareas, leen y escriben mensajes y aparecen en los
feeds de actividad junto a las personas, con salvaguardas adicionales sobre lo que pueden acceder y
compartir. Claude es la herramienta de IA predeterminada de los empleados de Asana, conectada a Google
Drive, Slack y Asana.

## Cuatro prácticas

| Práctica | Qué significa | Cómo aplicarla |
|---|---|---|
| Estructurar el trabajo antes de que actúen los agentes | Las personas convierten entradas no estructuradas (ideas, Slack, grabaciones, informes, documentos) en proyectos y tareas con Claude; luego los agentes actúan con memoria persistente, credenciales propias y contexto compartido | Empieza con tus ideas → debate con Claude → registra lo accionable en el grafo de trabajo |
| Rol, herramientas y acceso por agente | Agentes construidos en torno a roles (redactor de contenido, analista de insights, project manager, especialista en intake, analista y coordinador de campañas) con skills e integraciones predefinidas; cada uno tiene página de perfil; el acceso efectivo se limita a los permisos de quien lo invoca | Define el rol primero → acota el acceso → nombra usuarios y administradores por separado |
| Separar trabajar con un agente de entrenarlo | La memoria compartida permite reutilizar instrucciones previas entre usuarios; cualquiera da feedback de tarea, pero solo admins/editores confirman, deshacen o borran la memoria permanente | Decide quién entrena y quién usa → asigna editores según experiencia → construye la memoria trabajando |
| Mantener visible el trabajo del agente | El agente publica su plan de investigación y sus pasos en la tarea; cualquiera con acceso puede comentar y dirigirlo | Lleva agentes donde el equipo revisa → marca el trabajo del agente como tal → deja que los revisores lo entrenen |

Por qué importa la visibilidad, según Arnab: con un agente uno a uno, los demás revisores no saben cuál
fue el prompt ni el ida y vuelta. En una tarea compartida, la petición, las objeciones y el resultado
están en un solo lugar, y los revisores pueden corregir las instrucciones que lo produjeron.

## Tres trabajos de agentes en Asana
1. **Preguntas de producto desde Slack**: las preguntas se convierten en tareas; el agente responde con
   guías aprobadas y enlaces a fuentes, registra los vacíos de producto en el proyecto de intake del
   equipo de producto y crea tareas de enablement cuando las preguntas se repiten.
2. **Resumen At-Risk Renewal**: un resumen diario de cada tarea de renovación en riesgo en tres grupos
   (impulso positivo, impulso negativo, seguimientos recomendados), global y luego por región, enviado
   cada mañana a los líderes de clientes e ingresos, que pueden preguntar y entrenar al agente.
3. **Ciclos de ingeniería con Command**: los agentes llenan un tablero no planificado con feedback; las
   personas deciden qué entra en el ciclo; Command da estimaciones optimista/equilibrada/conservadora;
   los tickets van a personas o a agentes de código; los datos son accesibles vía el servidor MCP de
   Asana.

## Conclusión
Un contexto compartido para personas y agentes, una identidad distinta para cada agente para auditar sus
contribuciones y accesos, y un registro duradero de lo que aprenden para que el conocimiento del equipo
se acumule.

Pasos y plantillas reutilizables: la skill `design-coachable-agent-teammates` de esta carpeta.

Fuente: https://claude.com/resources/articles/agents-you-can-coach-how-asana-builds-human-agent-teams-with-claude
