[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un anuncio: Anthropic trabaja con Millennium, una de las mayores gestoras de inversión alternativa del mundo, para desarrollar conjuntamente un *analista de riesgo digital*: un compañero de equipo de IA que trabaja junto a los gestores de riesgo de la firma y bajo su supervisión, aflorando nuevas perspectivas de riesgo y formando opiniones sobre la exposición al riesgo en distintas clases de activos.

Millennium ya usa Claude y Claude Code de forma amplia — desde las mesas de trading y la ingeniería hasta funciones centrales del negocio, incluyendo muchos de sus más de 340 equipos de inversión. El analista de riesgo digital extiende ese uso ayudando a los gestores de riesgo a acelerar y enriquecer el análisis de posiciones. Lo construyen los expertos en riesgo de Millennium junto con los equipos de investigación e IA aplicada de Anthropic, que trabajan a su lado en el laboratorio de IA interno de la firma.

## ¿Cuándo es útil?
- Cuando un agente de tipo analista debe operar en un dominio regulado o de alto riesgo donde cada salida debe poder rastrearse hasta su razonamiento.
- Cuando la pregunta no es "¿puede el modelo responder?" sino "¿qué debe aprobar una persona para que la respuesta cuente?".
- Cuando el análisis del dominio depende de datos propietarios que el modelo nunca ha visto y de un criterio que la firma no quiere delegar.
- Cuando explicar el *cambio a lo largo del tiempo* — por qué las cifras de hoy difieren de las de ayer — importa más que una respuesta puntual.
- Cuando hay que decidir cómo estructurar un laboratorio de IA interno que someta a los modelos frontera a casos de uso ambiciosos.

## Puntos clave
- **El agente es un compañero, no un reemplazo.** Trabaja junto a los gestores de riesgo y bajo su supervisión; el criterio humano permanece en el centro de la decisión.
- **Datos propietarios más razonamiento frontera.** El analista se apoya en los datos propietarios de Millennium combinados con la inteligencia frontera de Claude, orientado a flujos de trabajo críticos de riesgo.
- **La memoria sirve a la continuidad.** El analista retiene y recupera información a lo largo del tiempo, y eso es lo que le permite explicar los cambios diarios de riesgo en lugar de responder cada pregunta desde cero.
- **La validación humana es un paso del flujo.** Los hallazgos son validados y enriquecidos por los gestores de riesgo de Millennium antes de contar como resultado.
- **Tres controles hacen auditable el análisis:** registra su razonamiento, prueba sus acciones en entornos aislados (sandbox) y exige que expertos humanos evalúen y aprueben sus decisiones.
- **El desarrollo conjunto ocurre en un laboratorio compartido.** Los equipos de investigación e IA aplicada de Anthropic trabajan junto a los expertos en riesgo en el laboratorio de IA de la firma, que además somete a prueba los modelos más recientes frente a casos de uso ambiciosos.
- **El objetivo declarado es el tiempo.** Según se cita en el post, los gestores de riesgo usarán inteligencia frontera para obtener recomendaciones automatizadas con el objetivo de ahorrar tiempo valioso.

## Recursos incluidos
- `skills/supervised-risk-analyst/SKILL.md` — cómo construir un agente analista que opere bajo supervisión humana en un dominio de alto riesgo.
- `skills/supervised-risk-analyst/references/auditability-controls.md` — los tres controles (registro de razonamiento, acciones en sandbox, aprobación humana) escritos como requisitos.
- `skills/supervised-risk-analyst/templates/analyst-charter.md` — una carta de alcance para definir qué posee el agente y dónde debe firmar una persona.
- `skills/supervised-risk-analyst/examples/daily-risk-change-review.md` — el flujo "explica el cambio de riesgo de hoy", paso a paso.

## Fuente
- https://claude.com/blog/millennium-and-anthropic-are-building-a-digital-risk-analyst-with-claude (6 de agosto de 2026)
