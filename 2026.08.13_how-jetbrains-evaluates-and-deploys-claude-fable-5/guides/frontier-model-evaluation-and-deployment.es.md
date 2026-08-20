[English](./frontier-model-evaluation-and-deployment.en.md) · [한국어](./frontier-model-evaluation-and-deployment.ko.md) · **Español** · [日本語](./frontier-model-evaluation-and-deployment.ja.md)

# Evaluar y desplegar un modelo de frontera

Una guía sobre la decisión que enfrenta una empresa de herramientas con cada lanzamiento
de un modelo de frontera: ¿es este modelo mejor *para nosotros*?, ¿qué cargas de trabajo
deberían migrar a él?, ¿y qué tiene que ser cierto a su alrededor antes de que llegue a
los clientes? El material proviene de una entrevista con Vladislav Tankov, CTO de
JetBrains Agent Systems, sobre cómo JetBrains evaluó y desplegó Claude Fable 5 — una
empresa con 12,5 millones de usuarios activos y 88 de las Fortune Global 100 entre sus
clientes.

## El punto de partida

Lo interesante no es que la calidad de los modelos haya mejorado, sino que la discusión
interna se acabó. Una empresa que alguna vez tuvo escépticos llegó al punto de asumir sin
más que la IA llegó para quedarse, y las preguntas abiertas bajaron un nivel: qué modelo,
para qué trabajo, bajo qué salvaguardas.

Ese replanteo es lo que convierte el resto de esta guía en un proceso repetible y no en
una decisión de adopción puntual.

## Evaluar sobre tus propios repositorios

Las puntuaciones de los benchmarks públicos son una hipótesis. Algunos modelos están
afinados para puntuar bien en ellos y se derrumban en tareas reales, así que la primera
tarea de una evaluación es comprobar si ese número público sobrevive al contacto con tu
base de código.

La práctica que se desprende:

- **Conjuntos de evaluación privados sobre repositorios privados**, incluido el monorepo
  de la empresa. Tareas extraídas de trabajo con el que el modelo no pudo haber entrenado,
  que arrastran tus convenciones y tu sistema de compilación.
- **Verificar las afirmaciones de los benchmarks** contra tareas del mundo real de forma
  explícita, y tratar la brecha entre ambos como información sobre cómo fue afinado el
  modelo.
- **Tres tablas de clasificación, no una** — mejor calidad, menor coste por tarea, mayor
  velocidad. Cada carga de trabajo elige un ganador distinto, y un único ranking destruye
  justamente la información que necesitas para enrutar el trabajo.

La tabla de coste por tarea merece énfasis. Un modelo puede tener un coste por token más
alto y aun así ser la opción más barata para trabajo complejo y de larga duración, porque
llega a la respuesta en menos pasos. Una comparación por token apunta en la dirección
equivocada precisamente en las cargas donde más está en juego.

## Qué medir

| Dimensión | Qué te dice |
|---|---|
| Tasa de aprobación por lenguaje | La brecha principal y dónde se concentra |
| Comparación directa ganadas/perdidas | Si la mejora es uniforme o un intercambio desigual |
| Tasa de "ejecuta pero es incorrecto" | Exposición al modo de fallo más caro |
| Pasos hasta la solución | Multiplicador de coste y proxy del criterio de ingeniería |
| Coste por tarea completada | El número que realmente gobierna el enrutamiento |
| Latencia | La dimensión decisiva para el uso interactivo en el editor |

En la ronda de JetBrains, Claude Fable 5 aprobó el 44,3 % de las tareas de Python frente
al 28,2 % de Opus 4.8, resolvió 18 tareas de Python que el modelo anterior falló mientras
perdía 2, y llegó a las soluciones con aproximadamente un 22 % menos de pasos.

Dos resultados merecen más atención que el titular. Primero, cuando el código de Fable 5
se ejecutaba, pasaba los tests mucho más a menudo — y el código que se ejecuta pero
produce una respuesta incorrecta es el tipo de fallo más caro de detectar, porque consume
la atención del revisor y puede llegar a producción. Segundo, en una tarea de Java el
modelo anterior intentaba repetidamente traer un recurso externo que no necesitaba,
mientras que el nuevo simplemente lo omitía. Tankov lo lee como mejores hábitos de
ingeniería en general — el tipo de hallazgo que una tasa de aprobación nunca revela, y por
eso vale la pena registrar los pasos por separado.

## Enrutar el trabajo en vez de cambiar por completo

La adopción no fue un reemplazo. Ambos modelos siguieron en servicio con trabajos
distintos.

- **Opus como caballo de batalla.** En palabras de Tankov, puedes estar muy seguro de que
  hará el trabajo. Ese es el valor por defecto correcto para tareas rutinarias y de alto
  volumen, donde la fiabilidad importa más que la profundidad del razonamiento.
- **Fable 5 cuando el camino es desconocido.** Reservado para cuando, según él, realmente
  necesitas buen razonamiento — cuando casi necesitas un socio. En concreto: un líder
  técnico resolvió casi de una sola vez un componente de editor de texto enriquecido que
  había resistido varios intentos previos.
- **Experimentos agénticos de larga duración.** Los agentes reciben una especificación en
  texto e imágenes e implementan aplicaciones sofisticadas tipo IDE; también generan una
  especificación a partir de una aplicación existente y la reescriben en otro runtime,
  framework o lenguaje en una configuración casi de caja negra.

Vuelve a abrir la decisión de enrutamiento en cada lanzamiento en lugar de congelarla.

## Postura de despliegue: construye la red, no el modelo

JetBrains no intenta hacer el modelo más seguro. La expectativa declarada es que el
red teaming y el trabajo de alineación hechos del lado del proveedor bastan para creer que
el modelo es seguro; el trabajo de la empresa que despliega es la **red de seguridad
alrededor del modelo** — un enfoque sistemático de despliegue donde la seguridad se
garantiza por la infraestructura y el diseño del arnés, no por retocar el modelo.

Dos consecuencias que vale la pena adoptar:

**Apunta el modelo a tus propios productos.** Pruebas de seguridad de caja blanca contra tu
propio software, bajo el supuesto explícito de que actores externos usarán modelos de la
misma clase contra ti. Para un proveedor con clientes empresariales y de sectores
regulados, encontrar esas vulnerabilidades primero lo es todo.

**Adopta una posición explícita sobre la retención de datos.** La preferencia declarada es
retención cero. El compromiso aceptado es una retención limitada a investigar los casos
señalados más graves, con el razonamiento de que sin ella no hay forma de entender qué se
pidió ni dónde un clasificador pudo funcionar incorrectamente — un intercambio justo por
el acceso a inteligencia de frontera. La tensión se nombra en lugar de ocultarse: los
clasificadores de contenido agresivos dificultan el propio trabajo defensivo de seguridad
de la empresa.

## Hacia dónde va esto

La hoja de ruta descrita trata menos sobre la capacidad del modelo — se asume que seguirá
mejorando — y más sobre la superficie que lo rodea: una especie de cabina de mando para el
desarrollo de software, un espacio en el que agentes y personas colaboran, con gestión real
del proceso de desarrollo. Los resultados esperados son desarrolladores entregando más y
mejor código a través de agentes, roles no técnicos con un papel mayor en la creación de
software, y organizaciones que ganan gobernanza y claridad sobre el retorno de la
inversión.

## Artefactos incluidos

- La skill `frontier-model-evaluation` de esta carpeta — el método como skill ejecutable.
- Las dimensiones de evaluación, una plantilla de registro de tablas por ronda y una
  comparación trabajada acompañan a esa skill en su carpeta.

## Fuente

- https://claude.com/blog/how-jetbrains-evaluates-and-deploys-claude-fable-5 (13 de agosto de 2026)
