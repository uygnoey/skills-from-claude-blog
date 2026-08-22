[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Anthropic tomó una muestra de 1,2 millones de sesiones de Claude Cowork anonimizadas y agregadas entre el 11 y el 31 de mayo de 2026, procedentes de más de 600.000 organizaciones, y las clasificó con un sistema automático según una taxonomía de 20 categorías de trabajo. El hallazgo principal: aproximadamente la mitad del uso corresponde a "el trabajo alrededor del trabajo" — tareas presentes en una enorme variedad de puestos, pero que rara vez son la responsabilidad central de nadie.

Esa mitad la sostienen las dos categorías mayores. **Procesos de negocio y operaciones** con un 33,4%: reunir actualizaciones dispersas en un único informe, construir listas de verificación de incorporación, conciliar hojas de cálculo. **Creación de contenido y redacción** con un 16,4%: comunicación de negocio intensiva en síntesis, como borradores, presentaciones, publicaciones y propuestas. Ninguna de las dos pertenece a un solo puesto: finanzas, RR. HH. y administración recurren a la primera; marketing, comunicación, desarrollo de negocio y gestión de proyectos recurren a la segunda.

El resto forma una cola larga: desarrollo de software 8,7%, DevOps e infraestructura 7%, investigación e inteligencia 6,4%, análisis de datos e inteligencia de negocio 5,8%, procesamiento y extracción de documentos 4,1%, ventas y operaciones de ingresos 4%, asistencia personal 3,8%, educación 2,4%, inteligencia de reuniones y conversaciones 1,8%, legal y cumplimiento 1,3%, atención al cliente 0,8%.

El post lee esa forma como trabajo conectivo: "la gente usa Claude Cowork para reunir y estructurar la información con la que después aplica su experiencia". Un abogado delega el formato y la presentación de documentos y se queda con el juicio legal; un responsable de contratación delega la agenda y la síntesis de comentarios de entrevistas y se queda con las conversaciones con candidatos; un jefe de equipo delega la presentación que explica una decisión difícil y se queda con la decisión. Esto contrasta con Claude Code, que los desarrolladores usan para el núcleo de su puesto — construir, depurar y desplegar código —, lo que explica en parte por qué el desarrollo de software representa una porción tan pequeña de las sesiones de Cowork.

El post cierra con una sección de metodología y limitaciones inusualmente explícita: el muestreo tiene un tope por hora, de modo que cada cifra es una cuota de sesiones muestreadas y no un volumen absoluto; la taxonomía no tiene categorías propias para marketing, finanzas o RR. HH.; se eligió una ventana de tres semanas porque un cambio en la canalización de etiquetado movió las cuotas alrededor del 11 de mayo; cerca del 5% de las sesiones son de uso personal y no laboral; y todas las etiquetas las aplicó un clasificador automático, no una persona.

## ¿Cuándo es útil?
- Cuando decides qué tareas propias delegar a un agente y quieres una distribución publicada de lo que la gente delega en realidad, en lugar de una suposición.
- Cuando defiendes internamente el uso de herramientas agénticas fuera de ingeniería y necesitas la forma del uso no técnico.
- Cuando clasificas las sesiones de agente de tu propio equipo y quieres una taxonomía y un formato de informe que ya existen.
- Cuando lees o escribes un informe de cuotas de uso y necesitas declarar honestamente las advertencias: muestreo con tope, clasificación automática, granularidad de la taxonomía.
- Cuando intentas explicar por qué una herramienta centrada en código y un agente en interfaz de chat acaban usándose para cosas tan distintas.

## Puntos clave
- **La mitad del uso es "el trabajo alrededor del trabajo".** Procesos de negocio y operaciones (33,4%) más creación de contenido y redacción (16,4%) suman aproximadamente la mitad de las sesiones muestreadas. Ninguna de las dos es el puesto de nadie.
- **La primera categoría más que duplica a la segunda.** 33,4% frente a 16,4%; todas las demás quedan por debajo del 9%.
- **Es trabajo conectivo.** Las hojas de cálculo reúnen datos dispersos en un contexto donde se pueden leer, comparar y seguir; las presentaciones transmiten una idea o decisión a públicos con distinto nivel de contexto; las listas de incorporación ayudan a una nueva persona a acceder al conocimiento institucional.
- **La experiencia se queda con la persona.** Lo que se delega es el ensamblaje y la estructura, no el juicio: el formato y la presentación en vez de la decisión legal, la agenda y la síntesis en vez de la evaluación del candidato, la presentación explicativa en vez de la decisión que explica.
- **El uso de Cowork es el inverso del de Claude Code.** Los desarrolladores usan Claude Code para el núcleo de su puesto y Cowork para el trabajo conectivo y comunicativo que rodea a todos los puestos, incluido el de ingeniería de software: por eso el desarrollo de software es solo el 8,7% de las sesiones de Cowork.
- **Cowork existe porque el terminal era una barrera.** Usuarios no técnicos ya usaban Claude Code para organizar carpetas, eliminar archivos duplicados y escribir fórmulas de hoja de cálculo; para otros el terminal seguía siendo "literalmente una 'caja negra'", así que la capacidad agéntica se trasladó a la interfaz de chat que ya usaban.
- **Cuotas, no volúmenes.** El muestreo está limitado a un máximo fijo de sesiones por hora, así que las cifras no pueden leerse como uso total ni como crecimiento, y las horas de mayor actividad quedan algo infrarrepresentadas.
- **La taxonomía clasifica el trabajo, no el cargo.** No hay categorías propias para marketing, finanzas ni RR. HH., lo que probablemente contribuye a que "procesos de negocio y operaciones" absorba un tercio de todo.
- **La instantánea es explícitamente provisional.** "Esto es solo una instantánea, y Claude Cowork todavía es nuevo; sus usos evolucionan rápido." Anthropic planea seguir publicando datos a medida que el uso cambie.

## Recursos incluidos
- `skills/knowledge-work-usage-taxonomy/` — clasificar sesiones de agente según la taxonomía de 20 categorías del post e informar cuotas con sus advertencias. Incluye una referencia con las cuotas publicadas, otra con el método de muestreo y sus límites, una plantilla de informe y un script que convierte recuentos de sesiones etiquetadas en una tabla de cuotas.
- `guides/work-around-the-work.{en,ko,es,ja}.md` — el recorrido completo de los hallazgos en cuatro idiomas.

## Fuente
[How people are using Claude Cowork](https://claude.com/blog/how-people-are-using-claude-cowork) — 7 de julio de 2026
