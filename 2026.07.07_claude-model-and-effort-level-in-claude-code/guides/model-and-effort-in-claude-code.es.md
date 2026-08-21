[English](./model-and-effort-in-claude-code.en.md) · [한국어](./model-and-effort-in-claude-code.ko.md) · **Español** · [日本語](./model-and-effort-in-claude-code.ja.md)

# Elegir modelo y nivel de esfuerzo en Claude Code

## Conclusiones clave

- **La selección de modelo elige el conjunto de pesos fijos**, es decir, el rango general de
  capacidad del modelo. Se le puede dar contexto o dirigirlo, pero su base de conocimiento y sus
  capacidades globales ya están fijadas.
- **El esfuerzo significa más que "tiempo de pensar".** Controla cuánto trabajo hace Claude sobre
  tu petición en conjunto: cuántos archivos lee, qué herramientas usa y cuántos pasos da antes de
  volver a consultarte.
- **Elige modelos más pequeños para tareas rutinarias y más grandes para tareas complejas o
  ambiguas.** Empieza con el nivel de esfuerzo por defecto de cada modelo y ajústalo como
  preferencia general según el tipo de trabajo que haces, no tarea por tarea.
- **Si Claude tenía todo el contexto pertinente, claramente lo intentó y aun así se equivocó**, es
  señal de elegir un modelo más capaz. **Si se equivocó por saltarse un archivo, no ejecutar las
  pruebas o abandonar una refactorización a medias**, sube el nivel de esfuerzo.

## Los dos ajustes

Claude Code ofrece dos ajustes que parecen "mejorar la respuesta": el modelo y el nivel de
esfuerzo. Es razonable esperar que modelos más grandes como Claude Fable 5 den una salida más
inteligente que Claude Sonnet, y que un esfuerzo mayor signifique que Claude piensa más antes de
responder.

La primera suposición es correcta: los modelos más grandes son más capaces según los benchmarks
estándar de la industria.

Pero el esfuerzo significa más que tiempo de pensar. El nivel de esfuerzo controla cuánto trabajo
hace Claude sobre tu petición en conjunto. Eso incluye cuánto piensa el modelo, pero también
**cuántos archivos lee**, **cuánto verifica** y **hasta dónde empuja una tarea de varios pasos
antes de consultarte**.

Con más esfuerzo, Claude tomará más de esas acciones —leer archivos, ejecutar pruebas, comprobar
dos veces— antes de volver a ti. Con menos esfuerzo, preferirá pedirte más contexto antes que
gastar tokens averiguándolo por su cuenta.

## Cómo funciona la selección de modelo

Cuando pulsas enter, Claude Code ensambla tu mensaje junto con el prompt de sistema, las
definiciones de herramientas, tu `CLAUDE.md`, el historial de conversación y cualquier archivo en
contexto. Todo eso se envía como una sola petición a la API.

El modelo nunca lo ve como texto plano. Lo primero que ocurre en el servidor es la
**tokenización**: el texto se divide en piezas y cada pieza se mapea a un entero de un vocabulario
fijo con el que se entrenó el modelo. `const` podría mapear a `1978`; `await`, a `4293`. A partir
de ahí, tu prompt es un array de enteros.

El trabajo del modelo es tomar ese array y predecir qué token viene después. Calcula una
probabilidad para cada token de su vocabulario y elige entre los más altos. Después de
`const x = await`, un modelo bien entrenado da alta probabilidad a `fetch` y casi cero a `banana`.

Lo que convierte tus tokens de entrada en esas probabilidades son los **pesos** (también llamados
parámetros): miles de millones de números organizados en grandes matrices. Para predecir un token,
el modelo pasa tu entrada por esas matrices —una larga cadena de multiplicaciones matriciales— y
lee las probabilidades al final. En los pesos vive todo lo que el modelo "sabe".

Los pesos de cada modelo se fijan durante el entrenamiento y, para cuando envías peticiones, son de
solo lectura. Nada en tu prompt, tu `CLAUDE.md` o tu contexto los cambia. (Eso es todo lo que
significa la palabra *inferencia*: usar el modelo una vez terminado el entrenamiento, con los pesos
fijos.)

Todo lo que Claude sabe de TypeScript, de frameworks populares, de Go idiomático o de cualquier
otro conocimiento general de programación quedó codificado en esos pesos en el entrenamiento. Tu
prompt y tu contexto pueden dirigir la predicción —poner tu código real delante de Claude es
dirigirlo, y funciona muy bien— pero no añaden nada a los pesos.

Si una librería no existía cuando se entrenó el modelo, no está en los pesos. Puedes poner la
documentación en contexto y Claude la usará, pero **eso es dirigir, no enseñar**: la respuesta se
ve influida solo para esa petición; el modelo subyacente no ha retenido la información. Por eso,
cuando Claude llama con confianza a una API que no existe —una alucinación—, son los pesos
produciendo una secuencia de tokens que parece plausible según patrones de entrenamiento, no una
búsqueda fallida.

Entonces, ¿qué hace cambiar de modelo? **Cambia qué conjunto de pesos congelados atiende tu
petición.**

El modelo no genera la respuesta entera de una vez. Predice un token, lo añade a la secuencia y
vuelve a ejecutar todo el cómputo para obtener el siguiente. Una respuesta de 200 tokens son 200
pasadas separadas por los pesos. Ese bucle es de donde sale la mayor parte de tu tiempo de espera y
de tu coste de salida.

Así que el ajuste de modelo decide qué pesos atienden tu petición y cuánto cuesta cada token de
salida. Lo que no decide es **cuántos tokens se generan**. Ese número puede variar mucho con el
mismo prompt, según cuánto trabajo decida hacer Claude — y eso es lo que controla el esfuerzo.

## Cómo funciona el nivel de esfuerzo

Cuando Claude Code trabaja en una tarea, los tokens que genera caen en unas pocas categorías:

- **Pensamiento**: el razonamiento que ves fluir antes y entre acciones.
- **Llamadas a herramientas**: bloques estructurados que nombran una herramienta como `Read` o
  `Edit` y sus argumentos, que Claude Code luego parsea y ejecuta.
- **Texto para ti**: el plan, las actualizaciones de progreso, el resumen final.

Todos son tokens de salida ordinarios del mismo bucle, facturados a la misma tarifa. Los tokens de
pensamiento se generan exactamente igual que el resto y permanecen en contexto durante ese turno:
cuando Claude pasa a escribir código, su razonamiento previo forma parte de la entrada, igual que
un archivo que haya leído.

El nivel de esfuerzo se **envía al modelo como parte de la petición**, junto a tu prompt. El modelo
fue entrenado para entender cómo comportarse en cada nivel de esfuerzo, y ese comportamiento
aprendido está grabado en los pesos congelados. Cuando llega tu petición, el nivel de esfuerzo es
una entrada más a la que el modelo responde, igual que responde al texto de tu prompt. Fija el
comportamiento de Claude respecto a cuán exhaustivo y seguro necesita estar antes de considerar
terminada la tarea; se considera en cada turno y se traduce en más tokens para producir respuestas
de mayor confianza. Con el mismo prompt, una ruta de esfuerzo alto puede generar unas 7× más tokens
que una de esfuerzo bajo.

Con esfuerzo alto Claude suele empezar creando un plan, y el nivel de esfuerzo influye en su
profundidad y amplitud. **El plan no queda congelado.** A medida que Claude recibe resultados de
sus acciones, actualiza el progreso y su certeza sobre el resultado acumulado. Así, cuando el paso
1 de un plan de depuración con tres hipótesis encuentra el bug, "investigar las hipótesis 2 y 3"
puede dejar de ser necesario. Claude normalmente lo dirá explícitamente —*la primera comprobación
lo encontró, así que las restantes no hacen falta*— y saltará adelante. Lo ves en Claude Code
cuando las listas de tareas se revisan a mitad de ejecución.

Claude está más predispuesto a comprobar hipótesis adicionales o verificar la corrección con más
esfuerzo, pero en general no inflará artificialmente el uso en tareas simples. El equipo presta
mucha atención al "sobrepensar" durante el entrenamiento, porque degrada la eficacia.

## Elegir un nivel de esfuerzo

Para la mayoría de las tareas, usa el **nivel de esfuerzo por defecto** del modelo. El valor por
defecto es el nivel en el que Claude escala su uso de tokens según lo que la mayoría de la gente
querría gastar en una tarea.

Piensa en el esfuerzo como una **anulación manual** para escalar cuán duro y cuánto tiempo trabaja
Claude. Elígelo deliberadamente cuando tengas una preferencia fuerte por exhaustividad o velocidad
según tu dominio o el tipo de trabajo que haces. Trátalo más como preferencia general que como
decisión tarea por tarea.

Una nota práctica tras el lanzamiento de Claude Opus 4.8: en las pruebas de Anthropic, usar el
ajuste de esfuerzo por defecto de Opus 4.8 produjo mejores resultados con aproximadamente el mismo
número de tokens que usar el ajuste por defecto de Opus 4.7 en la misma tarea.

## Qué cambiar cuando Claude se equivoca

Cuando Claude se equivoca, tu primer instinto no debería ser mover una perilla, sino examinar el
contexto que le diste. ¿Tu prompt es demasiado vago? ¿Está conectado a las herramientas
adecuadas? ¿Equipado con las skills adecuadas? Si estás subiendo el esfuerzo en una tarea que no
debería necesitarlo, el arreglo suele estar aguas arriba: en tu contexto, tu `CLAUDE.md` o cómo se
acotó la tarea.

Suponiendo que diste contexto claro y aun así se equivocó, pregunta: **¿no se esforzó lo
suficiente, o no sabía lo suficiente?**

### Modelo: el problema era demasiado difícil

Elige un modelo más grande cuando el problema es genuinamente difícil: bugs sutiles, dominios poco
familiares, decisiones de arquitectura. Un modelo más grande ayuda donde el más pequeño se equivoca
con confianza por más contexto que le des. Los modelos grandes también manejan mejor la ambigüedad,
mientras que las instrucciones específicas que dirigen la ejecución son mejor receta de éxito en
los pequeños.

Elige un modelo más pequeño cuando el trabajo es rutinario: ediciones que puedes describir con
precisión, cambios mecánicos, preguntas sobre código ya en contexto. No hay razón para pagar por
una capacidad que la tarea no necesita. Si Claude tenía todo el contexto pertinente, claramente lo
intentó y aun así falló, es señal de subir de modelo. Si estás en el modelo grande y el trabajo
lleva un rato siendo rutinario, bajar aumentará la velocidad y normalmente reducirá el coste sin
afectar a la calidad.

### Esfuerzo: Claude no se esforzó lo suficiente

Sube el nivel de esfuerzo si Claude se equivocó por saltarse un archivo, no ejecutar las pruebas o
no comprobar dos veces su trabajo. Esto es especialmente relevante si habías seleccionado un nivel
por debajo del predeterminado del modelo.

## Fable, Opus y Sonnet: el especialista, el experto y el generalista

Una forma de pensar la relación entre ambos ajustes: **Fable** es un especialista que ha visto
problemas que casi nadie más ha visto, **Opus** es el experto y **Sonnet** es un generalista muy
bueno. El nivel de esfuerzo decide cuánto tiempo dedica cualquiera de ellos a tu tarea.

**Opus con esfuerzo bajo** es como tener cinco minutos con un experto con experiencia profunda en
problemas como el tuyo. Trae conocimiento que no está en ninguna parte de tu código: patrones que
ha visto antes, trampas que sabe comprobar, ese tipo de cosas que solo se obtienen tras resolver
muchos problemas similares. Pero cinco minutos son una lectura rápida de tu código, no cuidadosa.

**Sonnet con esfuerzo alto** es como darle toda la tarde a un generalista muy bueno. Leerá todo,
ejecutará cosas, comprobará dos veces su trabajo y acabará entendiendo tu código a fondo. Lo que
aporta menos es ese reconocimiento de "he visto exactamente esto antes".

**Fable, incluso con esfuerzo bajo**, es ese especialista que mira de pasada el problema en el que
todos están atascados y aun así detecta lo que nadie más vería. Ese reconocimiento es lo que más
estás pagando, así que conviene reservarlo para las tareas que de verdad lo necesitan.

Ninguno es universalmente mejor. El ajuste de modelo es aproximadamente **cuán capaz**; el de
esfuerzo, aproximadamente **cuán exhaustivo**. La mayoría de las tareas reales necesitan algo de
ambos.

## Esfuerzo, modelo y consumo de tokens

Cómo interactúan los tres depende de la tarea.

**En trabajo rutinario con el mismo nivel de esfuerzo**, ambos modelos suelen acertar. El modelo
grande consume más tokens con pasos extra de verificación, a un precio por token más alto. Por eso
bajar al modelo pequeño en tramos rutinarios ahorra dinero real sin coste de calidad.

**En trabajo más duro y de varios pasos**, la ecuación cambia. El modelo pequeño tiene que
esforzarse hasta el límite de su capacidad, quemando iteraciones, mientras que el grande alcanza el
mismo listón de calidad en menos pasos. Pagas más por token, pero en tareas que realmente estiran
al pequeño, el coste total por tarea puede salir más bajo. Y más importante: el modelo grande puede
lograr tareas que el pequeño no puede, ni siquiera con el esfuerzo más alto.

Esto es más pronunciado con Fable. En trabajo largo y de varios pasos es donde más se despega: en
las pruebas terminó trabajos que Opus y Sonnet no alcanzan con ningún nivel de esfuerzo. También es
el que más cuesta por token, la otra razón para reservarlo.

El nivel de esfuerzo elige hasta dónde está dispuesto a viajar Claude por esa curva, pero eso no
significa que necesite viajar tan lejos para completar la tarea.

Un matiz más: **el esfuerzo moldea el consumo de tokens, pero no lo limita.** El único tope duro
del sistema es `max_tokens`, que trunca una respuesta a mitad de flujo — un instrumento burdo,
relevante sobre todo para desarrolladores de la API. Controles más suaves, como presupuestos de
tarea o pedirle brevedad en el prompt, son más útiles: sirven como guía que el modelo está entrenado
para seguir —buscará concluir su tarea si se acerca al límite— en vez de un muro contra el que
choca.

## Empieza por los valores por defecto y luego busca las perillas

La mayor parte del tiempo no deberías estar pensando en ninguno de los dos ajustes. Cuando un
resultado no da en el blanco, pregunta: **¿Claude no sabía lo suficiente o no se esforzó lo
suficiente?** — y ajusta en consecuencia.

## Fuente

["Choosing a Claude model and effort level in Claude Code"](https://claude.com/blog/claude-model-and-effort-level-in-claude-code),
por Lydia Hallie, miembro del equipo técnico de Claude Code — publicado el 7 de julio de 2026.
