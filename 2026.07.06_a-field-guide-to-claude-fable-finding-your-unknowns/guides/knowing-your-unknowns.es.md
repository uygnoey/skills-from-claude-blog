[English](./knowing-your-unknowns.en.md) · [한국어](./knowing-your-unknowns.ko.md) · **Español** · [日本語](./knowing-your-unknowns.ja.md)

# Conocer tus incógnitas: hacer coincidir el mapa y el territorio

## El cambio

Los prompts, las skills y el contexto que le entregas a Claude son **el mapa**. El código, sus
restricciones y todo lo que es cierto sobre él pero nadie escribió son **el territorio**.

El trabajo sale mal donde ambos discrepan. A medida que los modelos mejoran, la restricción
que limita la calidad se desplaza: deja de ser lo bien que planificas y pasa a ser lo bien que
sacas a la luz aquello que no sabías que tenías que decir. Planificar mejora el mapa; no hace
nada por las partes del territorio que nunca has visto.

## Cuatro tipos de hueco

Todo lo que no has dicho cae en uno de cuatro tipos, y no responden al mismo tratamiento.

- **Conocido conocido** — lo que pones deliberadamente en el prompt. Es un problema de
  escritura, no de descubrimiento.
- **Conocido desconocido** — huecos que sabes nombrar. Sabes que hay una capa de caché; sabes
  que no sabes cómo se invalida. Estos basta con preguntarlos.
- **Desconocido conocido** — detalles tan obvios para ti que nunca se te ocurre escribirlos.
  La convención de equipo no documentada. La razón por la que un módulo tiene esa forma rara.
  Este cuadrante arruina en silencio buenos prompts: el resultado es técnicamente correcto y
  equivocado para tu código.
- **Desconocido desconocido** — puntos ciegos. Factores que no has considerado y sobre los que
  ni sabrías preguntar.

Los dos últimos son los caros, y ninguno se cierra esforzándose más en el prompt.

## Antes de implementar

**Pasada de puntos ciegos.** Pregunta sin rodeos qué no has considerado, e indica cuánto sabes
realmente del área. Una persona senior que nunca ha tocado el módulo de auth y alguien nuevo en
el código necesitan listas distintas, y la respuesta solo sirve si está calibrada a ti.

> I'm working on adding a new auth provider but I know nothing about the auth modules in this
> codebase. Can you do a blind spot pass...

**Lluvias de ideas y prototipos.** Explora varios enfoques antes de comprometerte con uno. No
es cubrirse las espaldas: es cómo descubres los criterios con los que estabas juzgando de forma
implícita. Si aún no distingues un buen resultado de uno malo, construye dos y reacciona a ellos.

**Entrevistas.** Pide que te entrevisten con una pregunta a la vez, priorizando aquellas cuya
respuesta cambiaría la arquitectura.

> Interview me one question at a time about anything ambiguous, prioritize questions where my
> answer would change the architecture.

Lo de "una a la vez" es toda la técnica. Un lote de veinte preguntas se lee en diagonal; una
sola pregunta se piensa, y la respuesta reorienta la siguiente. Es la vía principal para sacar
de tu cabeza lo desconocido conocido.

**Referencias.** Señala código que ya implementa el comportamiento que quieres, aunque esté en
otro lenguaje. Lo que se transfiere es la forma de la solución y el conjunto de casos límite
con los que el autor original se topó y resolvió. Ese conjunto es un inventario gratuito de tus
incógnitas desconocidas para este problema.

**Planes de implementación.** Pide un plan que destaque los puntos de decisión probables, no
solo los pasos. Y revisa las decisiones. Los pasos te dicen si el trabajo se hará; las
decisiones te dicen si se hará bien, y eso es lo que un plan todavía puede cambiar barato.

## Durante la implementación

**Notas de implementación.** Mantén un `implementation-notes.md` temporal. Cuando un caso límite
obligue a desviarse del plan, se registra ahí junto con el motivo.

> Keep an implementation-notes.md file. If you hit an edge case that forces you to deviate
> from the plan...

El territorio revela incógnitas mientras el trabajo ocurre, y el campo que importa es el
porqué. Una lógica de reintentos que no coincide con el plan parece descuido sin explicación y
parece diligencia cuando la nota dice que una API upstream devuelve 200 con un cuerpo de error.

## Después de implementar

**Pitches y explicativos.** Empaqueta el prototipo, la especificación y las notas en un único
documento compartible.

> Package the prototype, the spec, and the implementation notes into a single doc I can drop
> in Slack...

Quien no siguió el proceso no puede revisar un diff. Sí puede revisar la historia de por qué el
cambio es así, incluido el enfoque que se probó y se descartó, que suele ser la parte más
persuasiva.

**Cuestionarios.** Pide un informe sobre los cambios con contexto suficiente para leerlos, más
un cuestionario de autoevaluación.

> Give me a HTML report on the changes for me to read and understand with context...

Suspender tu propio cuestionario sobre tu propio cambio es la forma más barata de descubrir que
no entendiste lo que se lanzó. Hazlo antes de la revisión, no después.

## Cómo encaja todo

El autor editó el vídeo de lanzamiento de Claude Fable con Claude Code, moviéndose entre
transcripción, etalonaje de color y manipulación de vídeo: nada de eso lo conocía al empezar. En
un dominio así de ajeno, planificar no es más barato que prototipar; es peor, porque el plan
fija suposiciones sin fundamento. Las incógnitas se encontraron de forma iterativa: intentar
algo concreto, reaccionar al resultado, preguntar qué no sabías preguntar sobre aquello a lo que
acabas de reaccionar, y repetir con el vocabulario recién adquirido.

Es el caso general, comprimido. Todo proyecto tiene un rincón que no conoces. Este simplemente no
tenía ninguno que el autor sí conociera.

## La idea

Cada explicativo, lluvia de ideas, entrevista, prototipo y referencia es una forma barata de
averiguar lo que no sabías antes de que salga caro arreglarlo. Así que empieza tu próximo
proyecto pidiéndole a Claude que te ayude a encontrar tus incógnitas.

## Fuente

- [A Field Guide to Claude Fable 5: Finding Your Unknowns](https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns), Thariq Shihipar, 2026-07-06
