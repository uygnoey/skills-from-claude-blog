[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Ian Chan y Annabel Custer, del equipo de marketing operations de Anthropic, describen dos flujos de trabajo que llevaron a Claude Cowork. Ian dedicaba uno o dos días por semana a montar la revisión semanal de métricas de marketing; ahora le lleva como mucho dos horas. Annabel configuraba cada nuevo evento haciendo clic en secuencia por Salesforce, HubSpot, Swoogo y herramientas de email; esa secuencia ahora la ejecuta casi por completo Claude, y ella revisa cada resultado antes de que salga.

Ambos flujos están construidos igual: conectores a las plataformas que el equipo ya usa, más un conjunto de skills pequeñas y de propósito único que se actualizan continuamente a medida que aparecen casos límite. Ian usa tres skills para el informe; Annabel usa un dispatcher y cinco skills especialistas para los builds de campaña, con una instancia de Claude nueva y separada que audita el resultado, y un agente "manager" siempre abierto al que recurre cuando una ejecución falla. Ambos flujos arrancan con tareas programadas: una cada domingo por la noche, otra cada hora.

Las horas recuperadas cambiaron la forma del trabajo, no solo su volumen. Ian dedica ahora más tiempo a ayudar a los marketers a formular sus propias preguntas y a profundizar en la capa de datos; Annabel dedica más tiempo a enablement y a la arquitectura de campañas. Su motivación principal para construir la automatización fue la consistencia y la calidad, no la velocidad: a medida que el equipo de marketing crece, los marketers que clonan páginas de evento desde cualquier plantilla que tengan cerca producen bugs, como emails de confirmación con el nombre de ciudad equivocado.

## ¿Cuándo es útil?
- Cuando un informe recurrente lleva días porque los números viven en un dashboard, en un warehouse, en un mensaje de Slack y en la transcripción de una llamada, y ningún pipeline cubre los cuatro.
- Cuando un proceso de configuración multiplataforma (CRM, automatización de marketing, plataforma de eventos, email) se hace a mano y en secuencia porque las integraciones entre proveedores están incompletas.
- Cuando una cola de solicitudes de entrada necesita enrutado y marcado para que el trabajo no se duplique.
- Cuando la salida automatizada necesita ser verificada por algo que no la produjo.
- Cuando hay que decidir qué va en una skill y qué va en un prompt: la respuesta del post es que una corrección que haces dos veces pertenece a una skill.
- Cuando el objetivo es la consistencia entre builds a escala, y no solo las horas ahorradas.

## Puntos clave
- **Una tarea programada hace la caza de datos antes de que nadie se despierte.** Cada domingo por la noche Claude lee la revisión de la semana anterior y la última transcripción de reunión, mira en Slack en qué está enfocado el equipo de ventas, consulta el warehouse y deja una carpeta con los números y algunas áreas de foco sugeridas. El lunes por la mañana el informe ya está esperando.
- **La persona elige la narrativa; Claude la expande.** Ian confirma o redirige los titulares sugeridos y luego pide expandirlos con detalles de apoyo y ejemplos. Algunas semanas el foco es una prioridad de ventas, otras un lanzamiento de producto; en el cambio de trimestre alimenta el documento de revisión trimestral y encabeza con los planes del trimestre. La diapositiva para el liderazgo sale de los mismos datos y de la misma narrativa, y los seguimientos se convierten en tareas de Asana.
- **Cuando los números no cuadran, Claude señala el desajuste en lugar de adivinar.** Tras una reorganización del equipo de ventas, el reporting de marketing dejó de coincidir con el suyo. Claude sacó a la luz la diferencia y preguntó cómo tratarla.
- **Tres skills sostienen el informe:** una skill de preparación que dirige el ensamblado, el foco, los titulares y la expansión; una skill de corrección que comprueba cada número del borrador contra una fuente verificada; y una skill de action items que convierte los seguimientos en tareas de Asana.
- **Las skills se actualizan al final de cada sesión.** Ian le pide a Claude que resuma lo que surgió y debería volver a las skills: la nueva estructura tras la reorganización de ventas, las correcciones que hizo, una nueva forma de plantear los titulares.
- **Un dispatcher separa el enrutado de la ejecución.** Una vez por hora lee el canal de entrada, escoge la solicitud más urgente, marca el ticket para que el trabajo no se duplique y lo pasa a una de las cinco skills especialistas. Él mismo no configura ningún evento, lo que permite refinar cada especialista sin tocar el enrutado.
- **La skill de event build ejecuta toda la secuencia:** creación de la campaña en el CRM, campaña en la plataforma de automatización con sus workflows y listas, configuración de la plataforma de eventos, redacción de emails, generación de la landing page y todas las integraciones entre ellas. También deja escritas dos actualizaciones en Slack: cuando Claude toma la solicitud y cuando la landing page está lista para revisión.
- **La auditoría empieza sin contexto previo.** Un agente separado envía un registro de prueba en la landing page en vivo, abre el email de confirmación en Gmail y marca la tarea de Asana como completa si todo se ve bien. Annabel revisa cada resultado antes de que salga.
- **Un agente manager se ocupa de los fallos.** Cuando una ejecución se tuerce, lo abre y le pide que mire qué pasó y proponga qué ajustar. Lo que merece la pena conservar vuelve a la skill correspondiente.
- **Cuatro consejos para empezar:** convierte las correcciones repetidas en skills (y deja que Claude escriba la skill); construye primero la skill de corrección; pide a Claude que reflexione sobre qué resultó difícil de las instrucciones tras las primeras ejecuciones; y apóyate en las tareas programadas, porque el trabajo que se ejecuta solo es trabajo que nadie tiene que recordar.

## Recursos incluidos
- `skills/weekly-metrics-report/` — la skill de preparación: caza de datos programada, tablas de métricas, titulares sugeridos, expansión de la narrativa y diapositiva para el liderazgo.
- `skills/report-proofreader/` — la comprobación número a número contra fuentes verificadas; el post recomienda construir esta primero.
- `skills/marketing-ops-dispatcher/` — triaje horario de la entrada, marcado de tickets y enrutado a las cinco especialistas, con una referencia que describe cada una.
- `skills/event-build/` — la configuración de eventos multiplataforma de extremo a extremo y sus dos actualizaciones de Slack.
- `agents/build-auditor.md` — el agente de auditoría sin contexto previo que hace un registro de prueba en la página en vivo antes de dar nada por completado.
- `agents/workflow-manager.md` — el agente permanente que diagnostica una ejecución fallida y propone el cambio en la skill.
- `guides/marketing-ops-automation.{en,ko,es,ja}.md` — el desarrollo completo en cuatro idiomas.

## Fuente
[How Anthropic's marketing operations team uses Claude Cowork to automate reporting and campaign builds](https://claude.com/blog/how-anthropics-marketing-operations-team-uses-claude-cowork-to-automate-reporting-and-campaign-builds) — Ian Chan y Annabel Custer, 8 de julio de 2026
