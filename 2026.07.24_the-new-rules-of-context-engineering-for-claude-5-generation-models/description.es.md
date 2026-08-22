[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Thariq Shihipar explica qué cambió en la ingeniería de contexto con la llegada de los modelos de la generación Claude 5, partiendo de un hecho: Anthropic eliminó más del 80 % del prompt de sistema de Claude Code para esos modelos sin pérdida medible en las evaluaciones de programación.

El diagnóstico es que el enfoque anterior le ponía *trabas* a Claude. Las reglas se habían acumulado en tres capas —el prompt de sistema, los archivos CLAUDE.md y las skills— hasta empezar a contradecirse: una capa decía que dejara la documentación cuando correspondiera mientras otra decía que no añadiera comentarios. Los modelos nuevos leen la intención del usuario sin ese andamiaje, así que lo que queda de él es solo el perjuicio. El artículo presenta seis cambios de "antes/ahora" y luego redefine para qué sirve realmente cada capa del contexto ensamblado.

## ¿Cuándo es útil?
- Cuando un prompt de sistema, un CLAUDE.md o una skill han crecido tanto que sospechas que partes de ellos juegan en tu contra.
- Cuando dos capas de tu contexto dan instrucciones que no se pueden cumplir a la vez.
- Cuando migras un agente ajustado para una generación anterior de modelos.
- Cuando decides si enseñar una herramienta con ejemplos o con su firma.
- Cuando la guía de uso de una herramienta está duplicada entre el prompt de sistema y la descripción de la herramienta.
- Cuando eliges el formato de una especificación con la que trabajará Claude.

## Puntos clave
- Se eliminó **más del 80 % del prompt de sistema de Claude Code** para los modelos Claude 5, sin pérdida medible en las evaluaciones de programación.
- **Reglas → criterio.** "Por defecto no escribas comentarios. Nunca escribas docstrings de varios párrafos ni bloques de comentarios de varias líneas: una línea corta como máximo" pasó a ser "Escribe código que se lea como el código que lo rodea: iguala su densidad de comentarios, su nomenclatura y su idiom".
- **Ejemplos → diseño de interfaces.** Los ejemplos de uso atan al modelo nuevo al espacio de exploración que cubren. Pon la guía en parámetros expresivos y opciones bien enumeradas.
- **Todo por adelantado → divulgación progresiva.** Carga el contexto de forma selectiva mediante skills y herramientas de carga diferida en vez de pagarlo todo en cada petición.
- **Repetición → una sola descripción de herramienta.** Los modelos anteriores se beneficiaban de que la misma instrucción apareciera en el prompt de sistema y en la descripción; los actuales consultan las descripciones de forma fiable.
- **Memoria manual → memoria automática.** Fijar contexto con la tecla rápida `#` cede el paso a que Claude conserve lo relevante para el trabajo y para ti.
- **Especificaciones simples → referencias ricas.** Los artefactos HTML, las referencias de código, las suites de pruebas y las rúbricas transmiten la intención con menos ambigüedad que un plan en Markdown.
- **Ahora cada capa tiene un solo cometido.** Prompt de sistema: contexto de producto. CLAUDE.md: ligero, centrado en las trampas. Skills: guías bajo demanda con las opiniones de tu equipo. Referencias: profundidad por @mención, prefiriendo código a prosa.
- **`/doctor`** en Claude Code (`claude doctor` desde la CLI) ajusta automáticamente el tamaño de skills, archivos CLAUDE.md y prompts de sistema para los modelos Claude 5.

## Recursos incluidos
- `skills/context-engineering-for-new-models/SKILL.md` — encontrar las contradicciones, aplicar los seis cambios, reescribir cada capa y medir.
- `skills/context-engineering-for-new-models/references/then-vs-now.md` — los seis cambios con su texto de antes y de ahora y el razonamiento de cada sustitución.
- `skills/context-engineering-for-new-models/references/context-layers.md` — para qué sirven hoy el prompt de sistema, CLAUDE.md, las skills y las referencias.
- `skills/context-engineering-for-new-models/templates/lightweight-claude-md.md` — la forma objetivo para un CLAUDE.md convertido en reglamento, y lo que ya no cabe en él.
- `skills/context-engineering-for-new-models/examples/rule-rewrites.md` — cuatro reescrituras antes/después: una regla de comentarios, una herramienta enseñada con ejemplos, una instrucción duplicada y una especificación en Markdown.
- `guides/context-engineering-rules.{en,ko,es,ja}.md` — el recorrido completo en cuatro idiomas.

## Fuente
[The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) — Thariq Shihipar, 24 de julio de 2026.
