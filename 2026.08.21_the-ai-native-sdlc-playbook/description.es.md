[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
El equipo de Applied AI de Anthropic expone cómo rediseñar el ciclo de vida del desarrollo de software en torno a la codificación agéntica. La premisa: el código ya no es el cuello de botella. Cuando la fase de construcción se comprime a horas, la restricción se desplaza a los pasos que la rodean y siguen a velocidad humana —planificar, revisar y probar, desplegar—, los controles dejan de corresponder con la realidad, y el coste de la gobernanza sube porque las excepciones siguen pasando por comités que se reúnen semanal o mensualmente.

La respuesta no es eliminar los controles, sino cambiar cómo se aplican. El flujo lineal se convierte en un bucle con IA integrada en cada punto, y cada etapa termina commiteando un artefacto versionado que la siguiente lee: `intent.md`, `spec.md`, `plan.md`, el diff y sus pruebas, la PR con sus hallazgos de revisión, el registro del incidente. La cadena de commits es la traza de auditoría. El artículo recorre las seis etapas —planificar, diseñar, construir, probar, desplegar, mantener— como jugadas modulares, cada una con prerrequisitos, pasos de ejecución, consideraciones de gobernanza y un indicador adelantado y otro rezagado.

## ¿Cuándo es útil?
- Cuando la codificación agéntica ha acelerado la construcción pero planificación, revisión, pruebas y despliegue siguen a velocidad humana.
- Cuando la cola de revisión o la firma de seguridad se ha vuelto el cuello de botella, y una organización regulada no puede aceptar ni un backlog creciente ni código insuficientemente revisado en producción.
- Al decidir qué etapa del SDLC transformar primero: el artículo separa el orden de las etapas del orden de adopción y nombra los prerrequisitos de cada jugada.
- Al codificar la política como skills, hooks y managed settings en lugar de aplicarla en reuniones de revisión.
- Cuando un sistema de registro existente (Jira, ServiceNow, una herramienta de requisitos) debe convivir con artefactos en markdown.
- Al cerrar el bucle para que una señal de producción escriba el siguiente `intent.md` sin una persona en el camino de invocación.

## Puntos clave
- **El artefacto commiteado es el hilo.** Cada etapa termina escribiendo uno en el control de versiones y la siguiente empieza leyéndolo. Un `intent.md` aceptado dispara el pase de diseño, un `spec.md` aprobado dispara el modo plan, una PR fusionada dispara el pipeline, y una banda de control superada escribe el siguiente `intent.md`.
- **La intención se captura una vez, con las palabras de quien la propone.** La persona con el problema hace lluvia de ideas con Claude y commitea `intent.md`: sin lenguaje formal y sin necesidad de que un product manager lo redacte. Quienes no manejan git commitean mediante un conector al control de versiones.
- **Requisitos y diseño colapsan en una sola sesión,** restringida por las skills de la organización y con las áreas de preocupación marcadas. La política se aplica mientras se escribe la especificación, no se descubre en una revisión semanas después.
- **Nada se implementa sin un plan aceptado.** El modo plan lo impone por sí mismo: Claude no puede editar archivos hasta que el ingeniero acepta el plan, así que cambiar de rumbo sigue siendo cuestión de editar un documento.
- **Las skills son consultivas; los hooks son deterministas.** «La skill hace raras las infracciones y el hook las hace casi imposibles.» Una política que siempre debe cumplirse necesita algo determinista detrás de la skill.
- **Dale a Claude un bucle de retroalimentación y protege el bucle.** Para corregir un error, escribe y commitea primero la prueba que falla, y luego pide el arreglo sin editar la prueba: un hook bloquea las ediciones de archivos de prueba durante una corrección, porque un agente que arregla código no debe poder debilitar la comprobación sobre ese código.
- **Las evals son la puerta de etapa nativa de IA.** De 20 a 50 tareas reales con sus comprobaciones, ejecutadas de forma no interactiva en CI según calendario y ante cualquier cambio en `CLAUDE.md`, skills o hooks: esa configuración dirige al agente y merece las pruebas de regresión que recibe el código. Cada incidente de producción se convierte en una eval permanente.
- **La revisión corre en ambos sentidos.** Claude revisa todas las PR contra `REVIEW.md` y atiende los comentarios con `@claude` en las suyas. Los hallazgos nunca aprueban ni bloquean por sí solos; la protección de rama sigue exigiendo un code owner, así que el agente que escribió el código no puede aprobarlo.
- **El agente actúa hasta la puerta de producción y no más allá.** La autonomía se escalona por entorno, el despliegue se expone por MCP como una lista de permitidos por entorno, y el rollback debería ser la ruta más ensayada del pipeline.
- **La detección sigue siendo determinista.** Un script versionado vigila una métrica con línea base móvil: 1σ registra, 2σ invoca a Claude en solo lectura, 3σ le permite abrir una PR o disparar un runbook preaprobado. Ningún modelo interviene en la detección.
- **Cada jugada lleva dos números:** un indicador adelantado que dice si el cambio está arraigando y uno rezagado que dice si el resultado mejoró, ambos leídos de git, los metadatos de PR, CI, el registro de incidentes o la exportación de OpenTelemetry.

## Recursos incluidos
- `skills/ai-native-sdlc/SKILL.md` — las seis etapas como procedimiento ejecutable, con la cadena de artefactos y el orden de adopción.
- `skills/ai-native-sdlc/references/stage-plays.md` — cada jugada completa: qué cambia, prerrequisitos, infraestructura, ejecución, gobernanza.
- `skills/ai-native-sdlc/references/governance-and-controls.md` — las cuatro capas de control y el ejemplo de managed settings explicado línea por línea.
- `skills/ai-native-sdlc/references/measurement.md` — la tabla de indicadores adelantados y rezagados, y de dónde se lee cada número.
- `skills/ai-native-sdlc/references/legacy-integration.md` — nombrar una fuente de verdad por artefacto cuando Jira o una herramienta de requisitos ya guarda el registro.
- `skills/ai-native-sdlc/templates/` — `intent.md`, `plan.md`, `claude-md.md`, `review-md.md`, `design-pass-prompt.md` y `verification-block.md` como plantillas rellenables.
- `skills/ai-native-sdlc/examples/` — la skill de política `secure-api-review`, el workflow de evals en CI y la puerta de producción.
- `skills/ai-native-sdlc/data/bands.yaml` — los niveles de respuesta 1σ/2σ/3σ.
- `agents/verifier.md`, `code-simplifier.md`, `codebase-researcher.md` — los tres roles de subagente que nombra el artículo.
- `hooks/production-gate.json` + `.sh` + `.md` — la puerta de release, reproducida del artículo.
- `hooks/test-file-guard.json` + `.sh` + `.md` — una implementación de referencia del bloqueo de archivos de prueba que el artículo especifica.
- `guides/ai-native-sdlc-playbook.{en,ko,es,ja}.md` — el manual completo como recorrido narrativo.

## Fuente
[The AI-Native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook), de Louis Claxton — publicado el 2026-08-21.
