[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un informe de campo sobre cómo Anthropic despliega Claude Tag dentro de Slack para que los empleados puedan hacer preguntas de datos ad hoc y recibir respuestas basadas en definiciones de datos gobernadas. Retoma donde lo dejó el trabajo anterior sobre precisión — que cubría alcanzar aproximadamente un 95% de precisión mediante capas semánticas, archivos de skill y suites de evaluación — y sostiene que **obtener respuestas precisas y desplegar ampliamente son problemas distintos**. El texto se organiza en torno a cinco aprendizajes de despliegue: actualizar los archivos de skill de forma continua, dar al agente skills analíticas más allá del acceso a tablas, conectarlo al contexto de negocio y no solo al almacén de datos, otorgar permisos a la cuenta de servicio de forma deliberada, e instrumentar cada respuesta.

El hilo conductor es que las propiedades del lado del despliegue — frescura, permisos, observabilidad — son las que determinan si un agente preciso sigue siendo preciso y sigue usándose una vez que está delante de toda la empresa.

## ¿Cuándo es útil?
- Cuando un agente de analítica ya puntúa bien en evaluación y hay que decidir cómo ponerlo delante de personas que no son analistas.
- Cuando las respuestas eran correctas en el lanzamiento y han empezado a desviarse, y hace falta distinguir entre deriva de skills y una necesidad de datos no cubierta.
- Cuando se está definiendo el alcance del acceso al almacén de una cuenta de servicio y se necesita un modelo defendible de lo que realmente concede la pertenencia a un canal.
- Cuando se quiere saber qué registrar para que la adopción y la corrección sean medibles desde el primer día.

## Puntos clave
- **Los archivos de skill son contenido servido, no artefactos publicados.** El runtime los vuelve a leer en cada conversación desde un repositorio montado, de modo que el agente siempre usa definiciones vigentes. Los modelos de datos cambian constantemente: columnas renombradas, métricas corregidas, tablas deprecadas.
- **Las skills analíticas importan tanto como el acceso a datos.** Pronóstico (ajuste de tendencia, supuestos de estacionalidad), análisis de cohortes y retención (definiciones estándar, curvas de retención), análisis de embudo (definiciones canónicas de etapas), gráficos (convenciones de visualización) y escritura analítica (estructura, matización, niveles de confianza). Documentan la práctica existente de los analistas; ponerlas por escrito es lo que produce consistencia.
- **El contexto de negocio convierte los números en explicaciones.** Conectar el agente a los índices de conocimiento internos — documentos, discusiones, eventos — le permite buscar qué ocurrió al mismo tiempo que un movimiento de métrica: informes de incidentes, cambios de feature flags, anuncios de la competencia. La diferencia entre "los registros cayeron un 12%" y una respuesta que explica por qué.
- **Otorga permisos a la cuenta de servicio de forma deliberada.** Limítala a datos gobernados; clasifica la PII a nivel de columna y niégale acceso al agente; documenta las rutas de conexión en los archivos de skill; trata la pertenencia a un canal como una concesión de acceso; etiqueta cada consulta para trazabilidad de auditoría y atribución de costes.
- **La idea que conviene retener:** tratar el acceso de Claude a los canales como *una réplica de lectura compartida de tu almacén gobernado*.
- **Instrumenta cada respuesta.** Registra qué archivos de skill se cargaron y en qué versión, las reacciones de los usuarios (👍/👎) y sus correcciones, y los avisos de calidad de datos sobre las tablas accedidas.
- **La adopción es la métrica más accionable.** Una caída señala deriva de skills o una necesidad de datos no cubierta.
- **Los hilos se convierten en espacios colaborativos.** Varios miembros del equipo aportan contexto mientras Claude realiza el análisis, produciendo un registro histórico revisable del problema y su solución.
- **Los bucles configurados cubren el trabajo repetitivo:** informes proactivos semanales antes de las reuniones de seguimiento, monitorización de tests y experimentos, observabilidad de pipelines y dashboards, y clasificación de las preguntas de datos entrantes.
- **Respuesta proactiva.** Configurado adecuadamente, Claude puede responder más del 75% de las preguntas del canal sin ser mencionado explícitamente.
- **Secuencia de implementación.** Primero los permisos; luego la distribución y una verificación de frescura; telemetría desde el primer día; índices de conocimiento cuando las rutas de datos se estabilicen; y las skills analíticas al final, guiadas por las preguntas que los usuarios hicieron realmente.

## Recursos incluidos
- `skills/slack-analytics-agent-deployment/SKILL.md` — las cinco decisiones de despliegue como procedimiento de trabajo.
- `skills/slack-analytics-agent-deployment/references/permissioning-model.md` — las cinco protecciones y el encuadre de réplica de lectura compartida, con preguntas de revisión.
- `skills/slack-analytics-agent-deployment/references/analytical-skills.md` — las cinco áreas de skills analíticas y cómo redactarlas.
- `skills/slack-analytics-agent-deployment/references/rollout-sequence.md` — el orden de implementación y su porqué.
- `skills/slack-analytics-agent-deployment/templates/telemetry-event.md` — conjunto de campos por pregunta, métricas derivadas y cómo leer una caída de adopción.
- `skills/slack-analytics-agent-deployment/templates/deployment-checklist.md` — checklist previo al lanzamiento sobre permisos, frescura, telemetría, contexto y skills.
- `guides/slack-analytics-rollout.{en,ko,es,ja}.md` — la guía completa de despliegue en cuatro idiomas.

## Fuente
- https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions
