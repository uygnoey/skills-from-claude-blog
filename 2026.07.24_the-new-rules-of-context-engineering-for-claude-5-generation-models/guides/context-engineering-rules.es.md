[English](./context-engineering-rules.en.md) · [한국어](./context-engineering-rules.ko.md) · **Español** · [日本語](./context-engineering-rules.ja.md)

# Las nuevas reglas de la ingeniería de contexto

Anthropic eliminó **más del 80 % del prompt de sistema de Claude Code** para los modelos Claude 5, sin
pérdida medible en las evaluaciones de programación. La lección se generaliza: la ingeniería de
contexto que hacía rendir bien a las generaciones anteriores de modelos no es la que hace rendir bien
a las nuevas, y buena parte de ella ahora estorba.

## Quitarle las trabas a Claude

El enfoque anterior sobrerrestringía a Claude. Las reglas se acumulaban en tres capas —el prompt de
sistema, los archivos CLAUDE.md y las skills— y, pasado cierto punto, empezaron a contradecirse. Una
capa decía que dejara la documentación cuando correspondiera; otra decía que no añadiera comentarios.
No se pueden cumplir ambas.

Los modelos nuevos interpretan lo que el usuario realmente quiere sin ese andamiaje. Así que lo que
queda del andamiaje es justo la parte que perjudica: órdenes contradictorias que estrechan el
comportamiento sin ninguna ganancia. Eliminarlas no es perder orientación, es quitar trabas.

Lo segundo que cambió es dónde puede vivir el contexto. Antes Claude dependía de CLAUDE.md como fuente
de memoria, información y orientación a la vez. Ahora la memoria, los artefactos y las skills le dan a
Claude sus propias formas de cargar y compartir contexto entre sesiones, y por eso CLAUDE.md ya no
tiene que cargar con todo.

## Seis cambios

**1. Dar reglas a Claude → dejar que Claude use su criterio.** La línea antigua decía: por defecto no
escribas comentarios, nunca escribas docstrings de varios párrafos ni bloques de comentarios de varias
líneas, una línea corta como máximo. La nueva dice: escribe código que se lea como el código que lo
rodea, igualando su densidad de comentarios, su nomenclatura y su idiom. La prohibición sustituía a un
estándar; enuncia el estándar.

**2. Dar ejemplos a Claude → diseñar interfaces.** Para un modelo nuevo, los ejemplos de uso no solo
ilustran: **restringen**, y lo atan al espacio de exploración que los ejemplos cubren. Traslada la
enseñanza a la propia herramienta: parámetros expresivos y opciones enumeradas con la claridad
suficiente para que el uso correcto se vea desde la firma.

**3. Ponerlo todo por adelantado → divulgación progresiva.** En lugar de un prompt de sistema que
cargue con todo lo que podría necesitarse, carga el contexto de forma selectiva mediante skills y
herramientas de carga diferida, para que la orientación adecuada llegue cuando es pertinente.

**4. Repetirse → descripciones de herramienta simples.** Antes las instrucciones aparecían en el
prompt de sistema *y* en la descripción de la herramienta. Ponlas solo en la descripción. Los modelos
anteriores se beneficiaban de la repetición; los actuales consultan las descripciones de forma fiable,
y el duplicado es una cosa más que mantener sincronizada.

**5. Memoria en archivos CLAUDE.md → memoria automática.** Fijar contexto a mano con la tecla rápida
`#` ya no es el mecanismo. Claude conserva automáticamente las memorias relevantes para el trabajo y
para ti.

**6. Especificaciones simples → referencias ricas.** Los planes en Markdown son la opción de baja
fidelidad. Los artefactos HTML, las referencias de código, las suites de pruebas y las rúbricas
transmiten la misma intención con mucha menos ambigüedad, y Claude maneja referencias cada vez más
complejas.

## Para qué sirve ahora cada capa

**Prompt de sistema.** Contexto de producto: dentro de qué producto opera el agente y qué papel
desempeña. Los usuarios de Claude Code rara vez lo modifican, pero en un agente propio merece un
esfuerzo considerable.

**CLAUDE.md.** Mantenlo ligero: una descripción del repositorio, concentrada en las trampas que solo
se descubren si alguien te las cuenta. Cuando las instrucciones se compliquen, muévelas a una skill
aparte y deja que la divulgación progresiva se encargue de cargarlas.

**Skills.** Guías ligeras para encontrar información bajo demanda. Evita sobrerrestringir salvo donde
sea crítico, y codifica las opiniones y buenas prácticas propias de tu equipo o producto. Divide las
skills largas en varios archivos.

**Referencias.** El lugar de la profundidad, traída con @menciones: especificaciones, mockups, bases
de código. Prefiere el código al texto descriptivo por claridad y fidelidad.

## Por dónde empezar

Ejecuta `/doctor` en Claude Code (`claude doctor` desde la CLI). Ajusta automáticamente el tamaño de
skills, archivos CLAUDE.md y prompts de sistema para los modelos Claude 5: esa es la parte mecánica
del trabajo. La edición a mano es para lo que queda después — las contradicciones entre capas y las
reglas escritas para sortear una limitación que el modelo ya no tiene.

Después, mide. La cifra del 80 % venía acompañada de evaluaciones, y "sin pérdida medible" es una
afirmación que conviene poder hacer sobre tu propio agente en vez de darla por supuesta.

Como dice el artículo: puede que necesites simplificar igual que hicimos nosotros.

## Fuente

["The new rules of context engineering for Claude 5 generation models"](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)
— Thariq Shihipar, 24 de julio de 2026.
