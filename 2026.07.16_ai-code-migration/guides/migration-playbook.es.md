[English](./migration-playbook.en.md) · [한국어](./migration-playbook.ko.md) · **Español** · [日本語](./migration-playbook.ja.md)

# Manual: ejecutar una migración a gran escala con agentes

Una migración es grande cuando leer cada diff deja de ser posible. Pasado ese punto, el
trabajo cambia de naturaleza: ya no consiste en escribir código, sino en diseñar los bucles
que escriben el código y observar después lo que esos bucles producen en conjunto.

El artículo original enuncia el principio sin rodeos: no arreglas el código, arreglas el
proceso que produjo el código. Todo lo que sigue se deriva de ahí.

## Por qué cambia la forma del trabajo

El modo de fallo clásico de una reescritura grande es que nunca termina: un equipo pequeño
porta a mano, el original sigue moviéndose y el port queda permanentemente por detrás. El
fan-out de agentes elimina ese límite de rendimiento —el port de Bun que describe el artículo
produjo cerca de un millón de líneas de Rust en menos de dos semanas—, pero lo sustituye por
otro problema. Cuando mil archivos los traducen agentes, una suposición equivocada no es un
error: es un error replicado mil veces, y cada instancia parece razonable vista por separado.

Por eso el punto de apalancamiento se desplaza. A esta escala, el trabajo minucioso archivo
por archivo casi no compra nada. Lo que lo compra todo es un manual de reglas correcto, una
cola que sobrevive a las interrupciones y un árbitro que no sea una opinión.

## El requisito previo: un árbitro

Antes de traducir el primer archivo hace falta algo que pueda ejecutarse contra el original y
contra el port, y que responda igual para ambos. Clasifica las pruebas existentes en dos
grupos: las expresables a través de la superficie pública y las atadas a los internos. Lleva
el primer grupo a aserciones que corran contra ambos lados; descarta el segundo, porque
aquello sobre lo que afirmaba no existirá después de la migración.

Después valida el propio árbitro, en las dos direcciones. Ejecútalo contra el original: debe
pasar. Ejecútalo contra código roto a propósito: debe fallar. Un árbitro verificado en una
sola dirección es la vía habitual por la que una migración acaba con el tablero en verde y el
producto roto.

Si el proyecto no tiene una suite de pruebas utilizable, construye en su lugar un arnés de
paridad con escenarios reales de extremo a extremo. El port de Python a TypeScript del
artículo usó siete, y trató cualquier diferencia de comportamiento como un error a corregir y
no como algo que explicar. Siete escenarios que ejerciten de verdad el sistema valen más que
cientos de pruebas superficiales que solo demuestran que el port compila.

## Fase uno: decidir y ponerlo por escrito

Tres documentos, en un orden fijo.

El **manual de reglas** es la política de traducción: todo lo que un implementador necesita
para portar un archivo sin preguntar a una persona. Su forma la determina una decisión que
hay que tomar antes: ¿es la misma arquitectura en un lenguaje nuevo, o es un rediseño? Un
port que preserva la estructura da un manual hecho sobre todo de tablas de correspondencia
—tipos, modismos, manejo de errores, concurrencia, sustitución de dependencias—. Un rediseño
da algo más parecido a un documento de diseño, porque no hay nada que consultar. Los equipos
que se saltan esta decisión escriben un manual ambiguo justo en los puntos que más importan.

El **mapa de dependencias** es el calendario. Un archivo puede traducirse cuando todo aquello
de lo que depende está listo, así que el mapa determina qué puede correr en paralelo. Si el
ecosistema publica un grafo de módulos, léelo. Si no lo hace —código heredado, C/C++,
Python—, haz que Claude descubra las dependencias y registra el resultado como datos legibles
por máquina que la cola pueda consumir, no como prosa. Anota los ciclos de forma explícita: no
se resuelven solos.

El **inventario de brechas** va al final, y ese orden no es una preferencia estilística. Una
brecha es un lugar al que no llegan los valores por defecto del manual, de modo que solo
puede definirse una vez que esos valores existen. Escrito primero, se convierte en una lista
de inquietudes en lugar de una lista de decisiones.

## Fase dos: intentar romperlo

Ejecuta una mini-migración sobre una muestra pequeña y representativa; el artículo la llama
un viaje de pruebas. Tres papeles: un traductor que trabaja solo con el manual, un revisor en
un contexto aparte que evalúa el resultado como lo haría un ingeniero sénior, y un extractor
de reglas que lee los diffs y propone las reglas que faltaban.

Y después, borra los archivos traducidos.

Esa es la instrucción a la que la gente se resiste, y es la que importa. El producto de esta
fase es un manual mejor, no avance. Conservar los archivos genera presión para conservar las
decisiones incrustadas en ellos, que es exactamente la presión que la fase existe para
eliminar. Repite hasta que una tanda de prueba produzca pocas reglas nuevas; esa convergencia
es la señal para escalar.

Las fases uno y dos son donde se va el tiempo humano. Todo lo posterior es sobre todo colas
que se consumen.

## De la fase tres en adelante: cuatro bucles con la misma forma

Traducir, compilar, ejecutar, igualar comportamiento. Solo se diferencian en qué alimenta la
cola: archivos del mapa de dependencias, luego errores de compilación, luego caídas, luego
diferencias frente al original. Las listas de tareas se escriben solas: un error del
compilador es el siguiente ítem, y una marca `// TODO(port)` dejada por un traductor es el
siguiente ítem.

Tres decisiones de diseño sostienen estos bucles.

**"Hecho" tiene que ser mecánico.** La formulación del artículo es que hecho significa que el
archivo de salida existe en disco. Las migraciones largas se interrumpen —límites de tasa,
reinicios, una tanda que decides tirar— y una cola cuya prueba de finalización requiere
criterio no puede reanudarse. Mantén el estado de la cola en disco, nunca solo en el contexto
de un agente, y haz que regenerar una tanda sea una operación barata y rutinaria, porque la
harás cada vez que cambie una regla.

**La incertidumbre se señala, nunca se adivina.** Un implementador que no está seguro emite
`// TODO(port): <motivo>` y sigue adelante. Esa es la diferencia entre un ítem visible en la
cola y un riesgo de corrección invisible. El texto del motivo importa más de lo que parece:
es lo que permite que una pasada posterior agrupe cincuenta marcas en una sola decisión en
vez de cincuenta improvisaciones.

**La revisión es adversarial.** Dos revisores por unidad de trabajo, en contextos separados
para que no se anclen entre sí, y el desacuerdo escala a un tercer agente. El artículo señala
que a menudo compensa el consumo de tokens, y la razón es estructural: un único revisor
converge hacia el encuadre del implementador, y un error sistémico revisado desde ese
encuadre se aprueba mil veces seguidas.

## La jugada que define el método

Cuando un revisor detecta el mismo fallo en muchos archivos, no arregles los archivos. Añade
una frase al manual de reglas y regenera la tanda afectada.

Un parche archivo por archivo deja el generador produciendo el error, así que volverás a
pagarlo en la tanda siguiente y en la de después. Un cambio en el manual detiene el error en
su origen y repara todo lo que ya había tocado. Por eso la regeneración barata de tandas se
enumeró como requisito de diseño y no como comodidad.

La misma lógica se aplica a tu atención. Los fallos individuales son la razón de ser de los
agentes reparadores. Tu trabajo durante las fases de consumo es notar qué categorías de fallo
se repiten y qué cambio único hace desaparecer una categoría entera.

## Gastar de forma deliberada

El gasto de tokens se concentra en los bucles, así que ahí es donde la elección de modelo
importa de verdad. Los implementadores son de alto volumen y están restringidos por el
manual: van en un modelo más pequeño —el artículo reporta doce subagentes Sonnet en paralelo
en el port de Python a TypeScript—. Los revisores, árbitros y delegadores son de bajo volumen
y cargados de criterio: van en uno más grande. Usar el modelo más grande en todas partes
gasta la mayor parte del presupuesto en el papel que menos lo necesita.

Las cifras publicadas de la migración de Bun dan una idea de la escala: 5.900 millones de
tokens de entrada y 690 millones de salida, unos 165.000 dólares a precio de API, para un
port de un millón de líneas que salió con binarios un 19 % más pequeños y un rendimiento real
entre un 2 % y un 5 % mejor. Ese coste es previsible de antemano si sabes dónde se concentran
tus tokens.

Serializa también lo que no paraleliza. Una compilación de todo el espacio de trabajo va
detrás de un script orquestador que ejecute la construcción una vez y agrupe los errores para
que los reparadores se repartan. Agentes que invocan cada uno la construcción consumen el
paralelismo que habías diseñado.

## Qué aspecto tiene el éxito

Bun se integró con el 100 % de su suite de pruebas existente en verde y con 19 regresiones
posteriores, todas corregidas. Esa es la forma realista de una migración exitosa a esta
escala. La pregunta que una migración debe responder no es si hay regresiones, sino si son
localizables y baratas —lo que equivale a decir que el árbitro que construiste en el paso
previo es lo que determina si todo esto funciona.

## Adaptarlo

El artículo es explícito: cada migración es distinta y esto es un punto de partida, no una
receta. Planifica la tuya con Claude antes de comprometerte, sobre todo la decisión
arquitectónica de la fase uno, que determina si tu manual será un conjunto de tablas o un
documento de diseño y, por tanto, la forma de todo lo que viene después.

## Fuente

[How Anthropic Runs Large-Scale Code Migrations with Claude Code](https://claude.com/blog/ai-code-migration) — publicado el 2026-07-16.
