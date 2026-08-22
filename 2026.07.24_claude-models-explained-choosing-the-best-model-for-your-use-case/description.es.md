[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Michael Segner responde a la pregunta que Anthropic más escucha —«¿qué modelo debería elegir para esta carga de trabajo?»— con una recomendación por defecto y un procedimiento. La recomendación: empezar con el modelo más inteligente disponible de forma general y usar el nivel de esfuerzo para ajustar rendimiento y coste, porque el coste por tarea suele ser menor en los modelos más capaces aunque el precio por token sea más alto, y porque empezar pequeño dificulta distinguir un fallo del modelo de un fallo de configuración.

El procedimiento son cuatro preguntas (qué tan difícil, qué tan rápido, a qué puedes acceder, cuánto cuesta el volumen), un recorrido por las cuatro clases de modelo y para qué sirve realmente cada una, la estrategia del asesor para repartir una tarea entre dos clases, y la razón por la que la decisión final debe tomarla la evaluación y no el benchmark. El encuadre que atraviesa todo el texto: las clases de modelo no se especializan por dominio —no hay un modelo de finanzas ni uno de ciencia—, así que elegir consiste en saber qué tan difícil es el problema que una clase puede sostener de forma fiable y cuánto cuesta esa capacidad en precio y velocidad.

## ¿Cuándo es útil?
- Al elegir clase de modelo para una nueva carga de trabajo en producción y querer un punto de partida defendible en lugar de una corazonada.
- Cuando una carga de trabajo está bajo presión de costes y alguien propone bajar de clase.
- Al decidir entre Opus y Fable, cuyas puntuaciones de benchmark parecen cercanas.
- Cuando una funcionalidad de cara al cliente y sensible a la latencia necesita que se le asigne una clase.
- Cuando un benchmark dice que dos modelos empatan y hace falta algo mejor con lo que decidir.
- Cuando una carga de trabajo falla de forma intermitente y nadie sabe si la culpa es del modelo o de la configuración.

## Puntos clave
- **Empieza arriba y baja después.** El valor por defecto es el modelo más inteligente disponible más el ajuste del nivel de esfuerzo. Empezar en una clase menor difumina el diagnóstico entre fallo del modelo y fallo de configuración.
- **El precio por token no es el precio por tarea.** Los modelos más capaces suelen necesitar menos turnos y menos tiempo de razonamiento, así que el coste por tarea puede ser menor pese a un precio por token más alto, especialmente con esfuerzo bajo.
- **No hay especialistas por dominio.** Todos los modelos Claude se entrenan para destacar en programación, tareas agénticas y trabajo del conocimiento. Las clases difieren en qué tan difícil es el problema que sostienen de forma fiable, no en qué campo conocen.
- **Mythos y Fable son un modelo en dos paquetes.** Mythos para organizaciones de confianza que trabajan con ciberseguridad y biología de doble uso; Fable con salvaguardas adicionales para el público general. Ambos requieren retención limitada de datos.
- **La regla práctica Opus/Fable.** Si las evaluaciones muestran a Opus con dificultades en algunas tareas, la respuesta es Fable. Si Opus ya supera el listón, su perfil de velocidad y precio puede hacerlo mejor. Con puntuaciones similares, los modelos más grandes tienden a mostrar más criterio, creatividad y capacidad de escritura.
- **Los dos hogares de Sonnet.** Cargas de alta frecuencia de cara al cliente, y subagentes de alto volumen en orquestación multiagente.
- **El esfuerzo es un segundo eje, no uno redundante.** Clase superior con esfuerzo alto es el techo de rendimiento; clase superior con esfuerzo *bajo* es a veces más eficiente que una clase menor sin más.
- **La estrategia del asesor.** Un modelo trabajador más rápido llama a un modelo más inteligente para que revise su plan y evalúe su trabajo, con orientación solo cuando hace falta. En SWE-bench Pro, Sonnet 5 con un asesor Fable 5 queda a menos de un 10% de la puntuación de Fable 5 al 63% del precio.
- **Los benchmarks se saturan.** Opus y Fable resuelven casi todo en las pruebas estándar, así que el benchmark deja de discriminar justo donde lo necesitas. Sirven solo como guía direccional.
- **Las evaluaciones propias son el instrumento decisivo.** Un conjunto curado de problemas de producción, incluidos los difíciles donde tus herramientas actuales fallan, con criterios de éxito definidos por tu equipo. Construirlas, mantenerlas y desplegarlas es el trabajo real de la selección de modelos.

## Recursos incluidos
- `skills/model-class-selection/SKILL.md` — el procedimiento de selección: empezar arriba, las cuatro preguntas, el dial del esfuerzo, la opción del asesor y decidir con evaluaciones.
- `skills/model-class-selection/references/model-classes.md` — las cuatro clases completas, la división de paquetes Mythos/Fable y la regla práctica Opus frente a Fable.
- `skills/model-class-selection/references/selection-questions.md` — las cuatro preguntas con sus derivadas y por qué el precio por token y el precio por tarea pueden apuntar en direcciones opuestas.
- `skills/model-class-selection/references/advisor-strategy.md` — el reparto trabajador/asesor, el resultado en SWE-bench Pro y qué medir antes de adoptarlo.
- `skills/model-class-selection/references/evals-and-benchmarks.md` — la saturación de benchmarks, los benchmarks mencionados y qué debe contener una evaluación propia.
- `skills/model-class-selection/examples/selection-scenarios.md` — siete escenarios resueltos, desde tareas de investigación hasta extracción de alto volumen.
- `agents/task-executor.md` — el rol trabajador: planificar, someter el plan a revisión, ejecutar y hacer evaluar el trabajo.
- `agents/plan-advisor.md` — el rol asesor: revisar planes buscando orden erróneo y supuestos sin verificar, evaluar salidas contra los criterios declarados y mantenerse fuera de la ejecución.
- `guides/choosing-a-claude-model.{en,ko,es,ja}.md` — la guía completa en cuatro idiomas.

## Fuente
["Claude models explained: choosing the best model for your use case"](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case) de Michael Segner — publicado el 24 de julio de 2026.
