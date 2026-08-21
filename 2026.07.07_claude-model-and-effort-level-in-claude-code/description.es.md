[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Lydia Hallie, del equipo de Claude Code, explica los dos ajustes que parecen "mejorar la respuesta" —el modelo y el nivel de esfuerzo— explicando qué cambia realmente cada uno. El ajuste de modelo cambia qué conjunto de pesos congelados atiende tu petición y fija cuánto cuesta cada token de salida. El nivel de esfuerzo, enviado al modelo como parte de la petición junto a tu prompt, fija cuán exhaustivo y seguro necesita estar Claude antes de dar la tarea por terminada: cuánto piensa, cuántos archivos lee, cuánto verifica y hasta dónde empuja una tarea de varios pasos antes de consultarte.

El post recorre la mecánica —tokenización, los pesos, la generación token a token, por qué dirigir con contexto no es enseñar, y por qué una alucinación son los pesos produciendo una secuencia plausible en lugar de una búsqueda fallida— y luego la convierte en una regla práctica. Cuando un resultado no da en el blanco, lo primero es revisar el contexto que diste. Si el contexto era claro y Claude aun así se equivocó, pregunta si *no se esforzó lo suficiente* (sube el esfuerzo) o *no sabía lo suficiente* (elige un modelo más grande).

## ¿Cuándo es útil?
- Cuando una sesión de Claude Code produjo un resultado erróneo o superficial y el instinto es mover una perilla.
- Cuando se elige una preferencia estable de esfuerzo para un equipo o un dominio, en vez de decidir tarea por tarea.
- Cuando hay que decidir si un tramo largo de trabajo rutinario puede bajar a un modelo más pequeño sin perder calidad.
- Cuando hay que explicar a colegas por qué el contexto de un prompt no cambia lo que el modelo sabe.
- Cuando se razona sobre coste: qué gana en una forma de tarea dada, "más capaz por token" o "menos tokens en total".
- Cuando la salida es más larga de lo que quieres y te preguntas si `max_tokens` es la palanca correcta (normalmente no lo es).

## Puntos clave
- **La selección de modelo elige un conjunto de pesos fijos**: el rango general de capacidad del modelo. El contexto dirige la predicción; no añade nada a los pesos.
- **El esfuerzo no es solo tiempo de pensar.** Controla cuánto trabajo hace Claude en conjunto: archivos leídos, herramientas usadas y cuántos pasos da antes de volver a consultarte.
- **Todo tipo de salida es el mismo tipo de token.** Pensamiento, llamadas a herramientas y texto para ti salen del mismo bucle y se facturan igual — y el pensamiento permanece en contexto el resto del turno, así que se convierte en entrada cuando Claude pasa a escribir código.
- **El esfuerzo viaja con la petición.** El modelo fue entrenado para entender cada nivel, y ese comportamiento está grabado en los pesos congelados. Mismo prompt, esfuerzo alto: unas 7× más tokens generados para llegar a una respuesta de mayor confianza.
- **Los planes se revisan, no se ejecutan a ciegas.** Si el paso 1 de un plan de depuración con tres hipótesis encuentra el bug, Claude suele decirlo y saltarse el resto. Más esfuerzo no infla artificialmente el uso en tareas simples: el "sobrepensar" se vigila de cerca en el entrenamiento porque degrada la eficacia.
- **Revisa el contexto antes que la perilla.** Si estás subiendo el esfuerzo en una tarea que no debería necesitarlo, el arreglo suele estar aguas arriba: el prompt, `CLAUDE.md`, las herramientas, las skills o el alcance de la tarea.
- **El diagnóstico.** Se saltó un archivo, no ejecutó las pruebas, abandonó una refactorización → sube el esfuerzo. Tenía el contexto, claramente lo intentó y aun así se equivocó con confianza → modelo más grande.
- **Más grande no es la respuesta por defecto.** El trabajo rutinario y describible con precisión pertenece a un modelo más pequeño; los grandes se ganan su precio en la ambigüedad, los bugs sutiles, los dominios poco familiares y las decisiones de arquitectura.
- **Especialista / experto / generalista.** Fable es el especialista que ha visto problemas que casi nadie más ha visto, Opus es el experto, Sonnet es un generalista muy bueno — y el esfuerzo decide cuánto tiempo dedica cualquiera de ellos. El modelo es aproximadamente *cuán capaz*; el esfuerzo, *cuán exhaustivo*.
- **El coste se invierte según la forma de la tarea.** Trabajo rutinario con el mismo esfuerzo: el modelo pequeño ahorra dinero sin coste de calidad. Trabajo duro de varios pasos: el grande alcanza el listón en menos pasos, así que el coste total por tarea puede salir más bajo — y puede terminar tareas que el pequeño no logra con ningún esfuerzo.
- **El esfuerzo moldea el consumo de tokens, pero no lo limita.** El único tope duro es `max_tokens`, que trunca a mitad de flujo. Los presupuestos de tarea y pedir brevedad son guía entrenada que el modelo sigue, no un muro.

## Recursos incluidos
- `skills/model-and-effort-selection/SKILL.md` — el procedimiento de decisión: primero los valores por defecto, contexto antes que perillas, y luego el diagnóstico "no lo intentó / no sabía".
- `skills/model-and-effort-selection/references/how-inference-works.md` — tokenización, pesos, el bucle de generación y por qué dirigir no es enseñar.
- `skills/model-and-effort-selection/references/effort-mechanics.md` — qué controla el esfuerzo, por qué los tokens de pensamiento son tokens de salida ordinarios y por qué los planes se revisan a mitad de ejecución.
- `skills/model-and-effort-selection/references/model-tiers.md` — el encuadre especialista/experto/generalista y una tabla de qué trabajo encaja con qué modelo.
- `skills/model-and-effort-selection/references/cost-and-tokens.md` — cómo se invierte el coste entre trabajo rutinario y trabajo duro de varios pasos, y por qué `max_tokens` es la palanca equivocada.
- `skills/model-and-effort-selection/examples/choosing-in-practice.md` — siete escenarios trabajados que asocian un síntoma con el ajuste a cambiar.
- `guides/model-and-effort-in-claude-code.{en,ko,es,ja}.md` — la guía completa en cuatro idiomas.

## Fuente
["Choosing a Claude model and effort level in Claude Code"](https://claude.com/blog/claude-model-and-effort-level-in-claude-code), por Lydia Hallie, miembro del equipo técnico de Claude Code — publicado el 7 de julio de 2026.
