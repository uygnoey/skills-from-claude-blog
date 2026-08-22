[English](./choosing-a-claude-model.en.md) · [한국어](./choosing-a-claude-model.ko.md) · **Español** · [日本語](./choosing-a-claude-model.ja.md)

# Elegir el modelo de Claude adecuado para tu caso de uso

«¿Qué modelo debería elegir para esta carga de trabajo?» es una de las preguntas más frecuentes que
recibe Anthropic. A medida que se han lanzado más clases y versiones de modelos, la respuesta se ha
vuelto más matizada. Esta guía recorre la familia de modelos, las preguntas que conviene hacerse y
las prácticas que hacen que la respuesta se sostenga en el tiempo.

## La recomendación por defecto: empezar por arriba

Dejemos el matiz a un lado por un momento. La recomendación por defecto es **empezar con el modelo
más inteligente disponible de forma general y usar el nivel de esfuerzo (effort level) para ajustar
rendimiento y coste.**

Por dos razones:

- **El coste por tarea suele ser menor en los modelos más inteligentes**, especialmente con niveles
  de esfuerzo bajos, aunque el precio por token sea más alto. Los modelos más capaces suelen
  necesitar menos turnos y menos tiempo de razonamiento para acertar en la mayoría de las tareas.
- **Empezar con un modelo pequeño complica el diagnóstico.** Cuando algo falla, cuesta distinguir un
  fallo del modelo de un fallo de la configuración.

Cuando aparezcan casos de uso más sensibles a la latencia o al coste, prueba clases inferiores hasta
encontrar el ajuste ideal.

Algunas organizaciones prefieren la dirección contraria: empezar con el modelo más rentable e ir
subiendo de clase hasta alcanzar el listón de calidad. La documentación de selección de modelos de
Anthropic recoge ambos enfoques direccionales. Cualquiera sirve; lo que hace comparables los
resultados es la consistencia.

## La familia de modelos Claude

La familia —Fable, Opus, Sonnet y Haiku— equilibra inteligencia, velocidad y coste de forma distinta
en cada clase. Las clases de modelo **no** se especializan por dominio: no hay un modelo de finanzas
ni un modelo de ciencia. Todos los modelos Claude se entrenan para destacar en programación, tareas
agénticas y trabajo del conocimiento. La diferencia está en **qué tan difícil es el problema que una
clase puede sostener de forma fiable, y cuánto cuesta esa capacidad en precio y velocidad**.

### Mythos / Fable

La clase más capaz, con capacidades de frontera en todos los dominios. Destaca especialmente en
programación, tareas de agentes de larga duración y problemas que la IA no había resuelto de forma
fiable hasta ahora.

La clase se distribuye en dos paquetes del mismo modelo subyacente. **Claude Mythos** está dirigido
a organizaciones de confianza que trabajan con ciberseguridad y biología de doble uso, mientras que
**Claude Fable** incorpora salvaguardas adicionales que hacen que el modelo sea seguro para el
público general. Ambos requieren retención limitada de datos para poder usarse de forma segura.

### Opus

La clase potente para tareas empresariales intensivas en razonamiento. Los modelos Opus se sitúan de
forma constante entre los líderes en benchmarks clave del sector, como **GDPval-AA** para trabajo del
conocimiento y **Terminal-Bench 2.1** para programación agéntica.

La decisión realmente difícil es Opus frente a Fable, ya que ambos destacan en programación, agentes
de larga duración y trabajo del conocimiento. En situaciones reales, los modelos más grandes como
Fable tienden a mostrar más criterio, creatividad y capacidad de escritura, pese a puntuaciones de
benchmark similares. La regla práctica: **si tus evaluaciones o tus pruebas internas muestran que
Opus tiene dificultades en algunas tareas, la respuesta es Fable. Si Opus ya supera el listón de
calidad, su perfil de velocidad y precio puede convertirlo en la mejor opción.**

### Sonnet

La clase versátil para tareas cotidianas: un equilibrio de rendimiento, coste y velocidad para el
conjunto más amplio de casos de uso generales, incluidos los **subagentes de alto volumen en montajes
de orquestación multiagente**.

### Haiku

La clase más económica y rápida, diseñada para **cargas de trabajo de alta frecuencia donde la
latencia y el coste importan**.

## Cuatro preguntas para elegir clase

1. **¿Qué tan difícil es esta tarea?** Si suele llevar mucho tiempo, implica varios pasos o no se
   había resuelto antes, corresponde una clase más capaz.
2. **¿Cuáles son las necesidades de latencia?** Si el modelo participa en cargas de alta frecuencia
   de cara al cliente, Sonnet suele ser la mejor opción.
3. **¿Cuáles son las restricciones de acceso?** Mythos solo está disponible para organizaciones bajo
   Project Glasswing, y no todas las organizaciones habilitan todas las clases para todos los roles.
4. **¿Cuál es la economía unitaria?** Los volúmenes de producción altos pueden encajar mejor con
   clases inferiores, sobre todo si las evaluaciones muestran que esas tareas se completan de forma
   satisfactoria. Los modelos tienen precios distintos por token y costes por tarea distintos según
   su capacidad y su nivel de esfuerzo.

### El esfuerzo es el segundo dial

El nivel de esfuerzo también desplaza el equilibrio calidad/velocidad/coste. Los modelos de clase
superior con esfuerzo alto ofrecen el mejor rendimiento posible, y **los modelos de clase superior
con esfuerzo bajo pueden ser a veces más eficientes que los modelos más pequeños**. Por eso «empezar
arriba y bajar el esfuerzo» suele ganar a «empezar pequeño». Explora la rejilla clase × esfuerzo, no
un solo eje.

## Combinar fortalezas: la estrategia del asesor

No hace falta ejecutar toda la tarea en una sola clase. La **estrategia del asesor** permite que
modelos trabajadores más rápidos y económicos llamen a modelos más inteligentes para que revisen su
plan y evalúen su trabajo.

Como el modelo ejecutor **solo recibe orientación cuando hace falta**, la mejora es sustancial en
relación con el coste. En **SWE-bench Pro, Sonnet 5 con un asesor Fable 5 queda a menos de un 10% de
la puntuación de Fable 5 al 63% del precio** de usar Fable 5 para toda la tarea.

## Cómo ayudan las evaluaciones y los benchmarks

Hay dos formas habituales de comprobar si las capacidades son suficientes:

**Los benchmarks estándar** son conjuntos de tareas predeterminadas con soluciones conocidas, a
menudo específicas de un dominio. Son guías direccionales útiles entre clases y entre proveedores. El
problema es la **saturación**: modelos potentes como Opus y Fable resuelven casi todas las preguntas
del test, de modo que el benchmark deja de discriminar precisamente entre los modelos que estás
comparando.

**Las evaluaciones propias** son la respuesta cuando eso ocurre. Usa los modelos en cargas de trabajo
reales o pruébalos con tus propias evaluaciones: normalmente un conjunto curado de problemas
extraídos de producción, **incluidas las tareas difíciles donde tus herramientas actuales se quedan
cortas**, con criterios de éxito definidos por tu equipo. Ahí es donde la capacidad y la creatividad
de los modelos de frontera empiezan a separarse del resto y entre sí.

## Tomar la decisión acertada

No hay un enfoque único para la selección de modelos, y por eso existen varias clases. En última
instancia, la mejor forma de elegir un modelo es entender los fundamentos de cada clase y entender tu
caso de uso en profundidad, lo que significa **construir, mantener y desplegar evaluaciones sólidas**
y revisar la decisión cuando cambien la carga de trabajo, el volumen o la propia gama de modelos.

## Fuente

["Claude models explained: choosing the best model for your use case"](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case)
de Michael Segner — publicado el 24 de julio de 2026.
