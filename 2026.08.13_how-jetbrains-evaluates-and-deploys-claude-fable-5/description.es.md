[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Una entrevista con Vladislav Tankov, CTO de JetBrains Agent Systems, sobre cómo JetBrains evalúa un modelo de frontera recién lanzado, decide qué cargas de trabajo migrar a él y establece las salvaguardas a su alrededor antes de que llegue a los clientes. JetBrains atiende a 12,5 millones de usuarios activos y a 88 de las Fortune Global 100, así que la decisión de despliegue pesa de verdad.

El hilo conductor es que las puntuaciones de los benchmarks públicos son una hipótesis, no una respuesta. JetBrains ejecuta grandes conjuntos de evaluación sobre repositorios privados — incluido su propio monorepo —, comprueba si el comportamiento real del modelo coincide con sus puntuaciones publicadas y mantiene tres tablas de clasificación separadas (mejor calidad, menor coste por tarea, mayor velocidad) para que cada carga de trabajo pueda elegir un ganador distinto.

## ¿Cuándo es útil?
- Cuando sale un modelo de frontera y necesitas una respuesta defendible a "¿deberíamos adoptarlo?", respaldada por tu propio código y no por una tabla pública.
- Cuando eliges entre modelos por carga de trabajo en lugar de fijar un único valor por defecto para todo.
- Cuando se está usando una comparación de precio por token para tomar una decisión que debería basarse en el coste por tarea completada.
- Cuando defines qué le corresponde a tu organización en materia de seguridad frente a lo que puedes esperar razonablemente del proveedor del modelo.
- Cuando necesitas una posición sobre retención de datos que sobreviva a una revisión de seguridad.

## Puntos clave
- **Evalúa sobre repositorios privados.** Tareas con las que el modelo no pudo entrenar, que arrastran tus convenciones y tu sistema de compilación. La advertencia de Tankov es que algunos modelos están afinados para puntuar bien en benchmarks públicos y se derrumban en tareas reales.
- **Tres tablas de clasificación, no una** — mejor calidad, menor coste por tarea, mayor velocidad. Fusionarlas en un único ranking destruye la información que necesitas para enrutar el trabajo.
- **Coste por tarea, no por token.** Claude Fable 5 tiene un coste por token más alto pero un coste por tarea menor en trabajo complejo y de larga duración, porque necesita menos pasos.
- **Las cifras reportadas.** 44,3 % de aprobación en Python frente al 28,2 % de Opus 4.8 — unos 16 puntos. En comparación directa, Fable 5 resolvió 18 tareas de Python que Opus 4.8 falló y perdió 2. Las soluciones llegaron con alrededor de un 22 % menos de pasos.
- **Pondera la tasa de "ejecuta pero es incorrecto".** Cuando el código de Fable 5 se ejecutaba, pasaba los tests mucho más a menudo; el código que corre pero produce una respuesta errónea es el tipo de fallo más caro de detectar.
- **Los pasos hasta la solución son una señal de hábitos.** En una tarea de Java el modelo anterior intentaba repetidamente traer un recurso externo que no necesitaba. Tankov lee la diferencia como mejores hábitos de ingeniería en general.
- **Enruta, no reemplaces.** Opus sigue siendo el caballo de batalla — puedes estar muy seguro de que hará el trabajo. Fable 5 se reserva para cuando realmente necesitas buen razonamiento, cuando casi necesitas un socio: un componente de editor de texto enriquecido que resistió varios intentos previos, y ejecuciones agénticas largas que implementan aplicaciones tipo IDE a partir de una especificación en texto e imágenes o reescriben una app existente en otro runtime, framework o lenguaje.
- **La seguridad es un problema del arnés.** JetBrains no intenta construir el modelo más seguro; espera que el red teaming del proveedor sea suficiente y dedica su esfuerzo a la red de seguridad alrededor del modelo — despliegue sistemático, infraestructura, diseño del arnés.
- **Apunta el modelo a tus propios productos.** Pruebas de seguridad de caja blanca contra el software de JetBrains, asumiendo que actores externos usarán modelos comparables en su contra.
- **Retención de datos, dicha explícitamente.** La preferencia es retención cero; una retención limitada a investigar los casos señalados más graves se acepta como un intercambio justo, porque de otro modo nadie puede saber dónde un clasificador funcionó mal. La tensión se nombra: los clasificadores agresivos dificultan el trabajo defensivo de seguridad.
- **Lo que viene** se describe menos como capacidad del modelo y más como una cabina de mando para el desarrollo de software — un espacio donde agentes y personas colaboran, con gobernanza y claridad sobre el retorno de la inversión.

## Recursos incluidos
- `skills/frontier-model-evaluation/SKILL.md` — el método de evaluación y enrutamiento, de principio a fin.
- `skills/frontier-model-evaluation/references/evaluation-dimensions.md` — las seis dimensiones que conviene puntuar por separado y cómo calcular cada una.
- `skills/frontier-model-evaluation/templates/leaderboard-record.md` — registro por ronda de las tres tablas, la decisión de enrutamiento y la postura de despliegue.
- `skills/frontier-model-evaluation/examples/private-eval-comparison.md` — la ronda de JetBrains desarrollada como ejemplo trabajado.
- `guides/frontier-model-evaluation-and-deployment.{en,ko,es,ja}.md` — el mismo material como guía en cuatro idiomas.

## Fuente
- https://claude.com/blog/how-jetbrains-evaluates-and-deploys-claude-fable-5 (13 de agosto de 2026)
