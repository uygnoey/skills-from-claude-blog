[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Anthropic presenta una analítica de administración más rica, entitlements a nivel de modelo y alertas de gasto para Claude Enterprise. La premisa: a medida que Claude asume trabajo agéntico cada vez más difícil y complejo en toda la organización, los patrones de uso y coste dejan de parecerse a los de una herramienta de chat, así que los administradores necesitan tanto la visibilidad para entender cómo se usa Claude como las palancas para gestionar lo que cuesta.

La mitad de visibilidad: un panel de analítica desglosado por grupo y por usuario, filtrable por los grupos SCIM que IT ya gestiona, que muestra el resultado producido (artefactos creados, archivos editados, skills y conectores usados) junto a su coste; dos nuevas pestañas de Claude Code que separan uso de valor, con todas las fórmulas de valor visibles y sus entradas ajustables; un chat de analítica para preguntas en lenguaje natural que devuelve gráficos exportables; y una Analytics API que lleva esos mismos datos a Datadog Cloud Cost Management, CloudZero y otras herramientas que finanzas e IT ya usan.

La mitad de control: valores por defecto y entitlements de modelo para que el trabajo rutinario no arranque en el modelo más caro, alertas de umbral de gasto al 75%/90% para administradores y al 75%/95% para usuarios, y una Admin API que convierte los flujos de control de coste en scripts cuando hay demasiados grupos para gestionarlos a mano. Todo ello se apoya en controles ya existentes: topes de gasto en todos los niveles, control de acceso y enrutamiento de modelos, el panel de uso con exportaciones y los controles de esfuerzo.

## ¿Cuándo es útil?
- Cuando los patrones de uso y coste de una organización empiezan a parecerse a trabajo agéntico y no a chat.
- Cuando finanzas o IT necesitan ver el uso y el coste de Claude junto al resto del gasto en nube e IA.
- Cuando el trabajo rutinario arranca por defecto en el modelo más caro disponible.
- Cuando los usuarios chocan con los límites de gasto a mitad de una tarea sin haberlo visto venir.
- Cuando alguien pregunta qué valor devuelve el despliegue por equipo o por licencia y la respuesta tiene que sostenerse.
- Cuando los límites por grupo superan lo que los administradores pueden revisar haciendo clic.

## Puntos clave
- **Uso y coste por grupo y por usuario**, con el resultado producido —artefactos creados, archivos editados, skills y conectores usados— junto a su coste, filtrable por los grupos SCIM existentes.
- **Claude Code separa uso de valor.** Uso: desarrolladores activos, sesiones, comandos más usados, actualizado a diario. Valor: aumento de productividad, coste por commit, valor anual, con todas las fórmulas visibles y entradas ajustables.
- **El chat de analítica acepta preguntas en lenguaje natural** ("¿Qué equipos duplicaron su uso de Claude este mes?", "¿Dónde obtenemos más valor por licencia?") y devuelve gráficos exportables y compartibles.
- **La Analytics API filtra por rango de fechas, equipo, producto o modelo**, las skills reportan su propio uso y coste, y hay nuevos endpoints para adopción de plugins y creación de artefactos. Integraciones nombradas: Datadog Cloud Cost Management y CloudZero.
- **Los usuarios pueden ver su propio uso** —tendencias en el tiempo, qué productos, modelos y skills usan más, y cómo se acumula en gasto— para que nadie se encuentre con un corte inesperado.
- **Los valores por defecto y los entitlements de modelo** fijan con qué modelo arrancan las conversaciones nuevas en chat, Cowork y Claude Code, y a qué modelos puede acceder cada rol.
- **Las alertas de umbral saltan al 75% y 90% para administradores** y al **75% y 95% in-app para usuarios**, que pueden solicitar un aumento sin salir de Claude.
- **La Admin API automatiza tres flujos nombrados:** revisión de solicitudes de aumento, identificación de miembros próximos a su límite y señalización de cambios rápidos de uso.
- **Tres perspectivas de negocio del post:** la visibilidad de costes como aviso recurrente y no como sorpresa de fin de mes; el coste leído junto al impacto de negocio por equipo para sostener un caso de ROI (un CIO vincula Claude, conectado a servidores MCP empresariales, a un 4% de aumento de ingresos); y las skills que se ejecutan una y otra vez en toda la organización como la señal real de valor, por encima del recuento de tokens.

## Recursos incluidos
- `skills/usage-and-spend-governance/SKILL.md` — instrumentar primero, controlar después: desglosar por grupo, separar uso de valor, extender visibilidad a usuarios, fijar defaults y entitlements, configurar ambos niveles de alerta y automatizar el resto.
- `skills/usage-and-spend-governance/references/analytics-surfaces.md` — las cinco superficies (panel, pestañas de Claude Code, chat de analítica, Analytics API, visibilidad por usuario) y qué muestra cada una.
- `skills/usage-and-spend-governance/references/spend-controls.md` — defaults de modelo, entitlements, ambos niveles de alerta en paralelo y los controles previos sobre los que se apoya.
- `skills/usage-and-spend-governance/references/admin-api-workflows.md` — los tres flujos nombrados de la Admin API y una nota explícita sobre dónde el post no publica formas de endpoint.
- `skills/usage-and-spend-governance/examples/analytics-questions.md` — las dos preguntas del post más tipos de pregunta mapeados a las dimensiones de filtrado que expone la API.
- `skills/usage-and-spend-governance/templates/rollout-checklist.md` — una lista secuenciada desde el prerrequisito SCIM hasta visibilidad, controles, integración y escala.
- `guides/admin-analytics-and-cost-controls.{en,ko,es,ja}.md` — la guía completa en cuatro idiomas.

## Fuente
["Giving admins more visibility and control over Claude spend"](https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend) — Anthropic, publicado el 2 de julio de 2026.
