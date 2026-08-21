[English](./ciso-agentic-ai-governance.en.md) · [한국어](./ciso-agentic-ai-governance.ko.md) · **Español** · [日本語](./ciso-agentic-ai-governance.ja.md)

# Guía del CISO para gobernar la IA agéntica

A los líderes de seguridad se les pide aprobar casos de uso de IA agéntica que no existían hace
unos meses. Los consejos quieren saber si algo de esto está gobernado y, en algún rincón de la
organización, un empleado ya conectó un agente a algo sin decírselo a nadie.

Decir **no** produce adopción en la sombra: cero telemetría y, por lo general, ningún interruptor
de apagado. Decir **sí** sin controles produce incidentes, y el primer incidente serio con un
agente hace retroceder todo el programa de IA de la empresa.

La responsabilidad no es alcanzar riesgo cero. Es hacer que el riesgo agéntico sea **legible y
acotado**, para que pueda aceptarse deliberadamente por quien tiene autoridad para aceptarlo y el
negocio avance en los términos de seguridad en lugar de rodearla.

## Riesgo externo frente a riesgo interno

La IA está colapsando el tiempo entre la existencia de una vulnerabilidad y un exploit
funcional. Se espera que una enorme cantidad de errores que llevaban años sin ser vistos sean
encontrados por modelos y encadenados en exploits funcionales. Los modelos de frontera ya
encuentran vulnerabilidades serias que años de revisión humana pasaron por alto, incluidas
OpenBSD, el kernel de Linux y Mozilla Firefox. Cerrar esas brechas merece su propio programa;
esta guía cubre el lado **interno**.

## Las dos amenazas internas dominantes

1. **Fuga de datos a través de sistemas conectados.** Para muchas organizaciones, el vector más
   probable es una fuga habilitada al conectar sistemas dispares mediante agentes personales con
   supervisión insuficiente.
2. **Inyección de prompts.** Un atacante esconde instrucciones dentro del contenido que el agente
   lee, y el agente sigue al atacante en lugar del usuario. Cualquier agente que toque contenido
   no confiable puede quedar expuesto. A medida que los modelos ganan capacidad resisten la
   inyección notablemente mejor y las tasas de éxito de ataque siguen bajando, pero no son cero.

Hay muchas preocupaciones más allá de estas dos, y el aluvión de nuevas categorías puede resultar
abrumador. Para eso están las cuatro preguntas.

## Las cuatro preguntas

Cuando un caso de uso agéntico llega a revisión, se evalúa su riesgo preguntando:

1. **¿Qué contenido no confiable ingiere?** No confiable significa cualquier cosa que un atacante
   pudiera plausiblemente escribir o alterar: correo externo, la web abierta, documentos de
   terceros, repositorios públicos. Si la respuesta es "nada", el riesgo específico del agente es
   casi cero: avanza rápido.
2. **¿Qué acciones puede tomar y en nombre de quién?** Solo lectura es una preocupación distinta
   de lectura/escritura. Las llamadas a herramientas, la ejecución de código y la salida de red
   amplían la apertura. Toda acción ocurre bajo alguna identidad, y hay que saber cuál.
3. **¿Cuál es el radio de impacto si se desalinea?** Alcance × severidad: ¿el incidente tuvo
   acceso a un archivo o a toda la organización, y sería una anomalía, una molestia, una
   exposición de datos o un incidente real?
4. **¿Qué observabilidad tengo?** ¿Puedes distinguir las acciones del agente de las del usuario?
   ¿Llegan a tu SIEM?

Las cuatro respuestas dan una imagen del riesgo. El **principio de mínima agencia** dice qué
hacer con ella: otorgar la capacidad más estrecha que aún complete la tarea. La postura por
defecto es un **despliegue marcado por el administrador**: habilitar a un grupo pequeño, observar
la telemetría y luego ampliar.

## El espectro de identidad agéntica

Todo lo que se despliega se sitúa en uno de los dos extremos de un espectro de modelo de acceso
por identidad.

- **La cuenta de servicio del sistema.** Una identidad autocontenida, de propósito único y de
  mínimo privilegio que hace exactamente una cosa para el negocio, sin identidad humana asociada:
  un agente de respuesta a incidentes, un agente de triaje de tickets, un revisor de código
  autónomo, un agente de espacio de trabajo compartido al que los equipos etiquetan en un canal.
- **La credencial humana.** Cuando un empleado usa una interfaz de chat o un arnés de agente
  personal en su portátil, la persona frente al teclado responde por el resultado, igual que
  responde por cualquier otra cosa hecha con sus credenciales.
- **El medio ambiguo**, donde un agente lleva la identidad delegada de una persona a sistemas que
  esa persona no está mirando, es donde la responsabilidad se vuelve ambigua. **La responsabilidad
  ambigua es cómo los incidentes se vuelven inexplicables.**

Un agente que se desvía de tu intención es indistinguible de un ataque interno. La industria pasó
2019–2022 formalizando el riesgo interno como disciplina distinta de la defensa perimetral, al
reconocer que el vector más peligroso suele ser el que compromete a alguien que ya tiene acceso
legítimo. La diferencia operativa es el tiempo de respuesta: el informe *Cost of Insider Risks*
2026 del Ponemon Institute encontró que las organizaciones tardaron una media de **67 días** en
contener un incidente interno. A velocidad de ejecución de agentes, 67 días es directamente la
unidad de medida equivocada.

## Caso de estudio: un agente de respuesta a incidentes

Hace más de un año, Anthropic apuntó Claude a su proceso de respuesta a incidentes. El agente
recibió tres herramientas: acceso de solo lectura a los registros de producción, que no contienen
PII; acceso a Slack para abrir el canal de incidente y ejecutar el proceso; y la capacidad de
redactar un Google Doc para el postmortem tras la resolución.

Con las cuatro preguntas: **ningún contenido no confiable** (registros propios y Slack interno
propio; una inyección exigiría un insider o una cuenta comprometida); **lee en todas partes,
escribe solo documentos nuevos y mensajes de Slack**, sin ediciones ni borrados, sin cambios de
permisos, sin endpoints externos; **radio de impacto** limitado a algunas líneas de registro
levemente sensibles en un canal ya restringido; **observabilidad** completa, con cada acción en el
SIEM. No estaba libre de riesgo, pero operaba con una superficie de escritura acotada y cobertura
de auditoría total.

Entonces ocurrió algo instructivo. En noviembre de 2025 el agente pasó de Claude Opus 4 a Claude
Opus 4.5 **sin cambiar nada más**: ni herramientas, ni permisos, ni prompts. El salto de
inteligencia por sí solo bastó para que el agente notara, en mitad de un incidente, que ya había
encontrado la causa raíz en un stack trace y que, ante la ausencia del humano que aún no había
llegado, podía intentar arreglar producción contactando a otro agente con acceso al código. Las
trazas de razonamiento lo mostraban: *He hecho lo que me pidieron. El humano no está. ¿Y si
arreglo el problema?* Por Slack pidió el arreglo a una instancia interna capaz de escribir
cambios de código y subirlos para revisión humana; el arreglo fue a un pull request que una
persona revisó antes de llegar a producción.

El radio de impacto ampliado por esta comunicación emergente entre agentes seguía gobernado por
los principios originales: lo peor que podía pasar era subir un cambio de código con una línea de
registro de producción. Dos lecciones:

1. **Pueden aparecer capacidades nuevas dentro de los límites de un despliegue existente.**
   Limita accesos y acciones, no lo que crees que el modelo de hoy puede hacer.
2. **Los controles funcionan incluso con agentes estocásticos.** El comportamiento tuvo un humano
   en el bucle porque ocurrió en un canal de Slack, y la única acción de escritura seguía
   requiriendo revisión humana.

## Caso de estudio: un arnés de agente personal

Claude Cowork está en el extremo del operador humano. Su modelo de amenazas es directo porque el
agente es esencialmente Claude Code ejecutándose en local o dentro de una interfaz alojada. La
app de escritorio sigue siendo necesaria para acceso a archivos locales, uso de navegador y uso
de computadora. La superficie completa tiene dos partes: un entorno de ejecución (posiblemente
remoto) que maneja orquestación, llamadas MCP y peticiones de red salientes, más un puente local
para acceso a archivos y pantalla.

Aquí las cuatro preguntas dan respuestas distintas para cada caso de uso, así que el riesgo se
acota con controles. **Siete requisitos**, planteados como lo que cualquier entorno de agentes
debería poder cumplir:

1. **La identidad viene de tu IdP.** Emitida y revocada donde ya emites y revocas todo lo demás,
   con tus grupos existentes como unidad de política. (SAML u OIDC para el inicio de sesión, SCIM
   para el aprovisionamiento; en planes Enterprise, roles personalizados acotan la capacidad por
   grupo.)
2. **Las listas de permitidos de conectores dibujan tu frontera de datos.** Un modelo de dos
   compuertas: un administrador habilita cada conector para toda la organización y luego cada
   usuario autoriza su propia cuenta. La decisión del administrador sobre qué conectores encender
   *es* la decisión sobre a qué datos puede llegar el agente. Mantén los conectores del lado
   corporativo de la frontera corporativo/producción; cuando toquen fuentes no confiables, exige
   revisión humana para cualquier decisión destructiva o irreversible (en correo: solo borradores,
   nunca envío externo automático). Los datos que crucen la frontera pasan por DLP o DSPM.
3. **Aprobación por herramienta y por acción.** La lista de herramientas es una frontera de
   permisos más fina que el conector: permitir redactar documentos pero nunca enviarlos, permitir
   lecturas y búsquedas pero nunca borrados. Si el modo de fallo que te quita el sueño es "se
   borra la base de datos de producción", elimina el verbo *delete* del mundo del agente: nunca
   intentará una acción que no esté en su lista de herramientas. Los agentes de código y de
   navegador habilitan más grados de libertad y son más arriesgados si no se gobiernan bien.
4. **Ejecución en sandbox.** El entorno donde corre el bucle del agente nunca debería contener una
   credencial que valga la pena robar. En sesiones remotas el bucle corre en un sandbox aislado y
   temporal; los tokens de conector nunca entran, porque las llamadas pasan por un proxy inverso
   que inyecta las credenciales reales. En julio de 2026, más del 50% del código enviado en pull
   requests en Anthropic lo escribe un sistema de agentes interno; es seguro sobre todo porque
   todo ocurre en VM efímeras separadas de las claves de producción, con revisión humana antes de
   que algo aterrice.
5. **La lista de permitidos de salida es tu control más fuerte contra la inyección de prompts.**
   Todo el tráfico que sale del entorno de ejecución pasa por un proxy que ese entorno no puede
   reconfigurar ni eludir, y solo los destinos que elegiste son alcanzables. Si un agente queda
   comprometido por algo que leyó, el atacante todavía tiene que sacar los datos; si las
   peticiones salientes solo alcanzan dominios que elegiste, no hay a dónde enviarlos.
6. **La telemetría va a tu SIEM por OpenTelemetry.** Las acciones del agente deben distinguirse de
   las del usuario en el sistema donde ya investigas, y el proveedor debe entregarlo como un flujo
   que puedas dirigir, no como un panel que debas visitar. Los administradores configuran un
   endpoint OTLP y se transmite cada invocación de herramienta: nombre, servidor MCP, parámetros,
   éxito o fallo, duración, junto con la identidad del usuario y el contexto de sesión. Ten en
   cuenta que la actividad de Claude Cowork no se captura hoy en la Compliance API ni en los
   registros de auditoría formales de Anthropic, y que el contenido de los prompts se incluye por
   defecto en su salida OTel (a diferencia de Claude Code, donde es opcional): resuelve tu
   posición de retención y privacidad **antes** de encender el flujo.
7. **Hay un interruptor de apagado para toda la organización.** Un solo conmutador desactiva los
   conectores para todos los usuarios a la vez, sesiones activas incluidas. Los planes Enterprise
   permiten ir más fino antes de ir a cero: RBAC retira el acceso a grupos concretos y los
   controles por conector desactivan escrituras en una integración sin tocar el resto. Traza las
   tres capas **antes** de necesitarlas.

## La gobernanza no tiene por qué ser un cuello de botella

La observación más frecuente entre CISOs es que los consejos exigen velocidad y la gobernanza
hace que seguridad parezca el cuello de botella. No tiene por qué serlo. De hecho, los equipos de
gobernanza, riesgo y cumplimiento de Anthropic operan sus propios agentes: redactar respuestas a
cuestionarios de seguridad, y leer respuestas de cuestionarios de proveedores y notificaciones de
cambio de subprocesadores para marcar aquellas a las que conviene objetar. Tres aprendizajes:

- **Empieza por el registro de riesgos.** Un registro revisado trimestralmente no puede gobernar
  sistemas que cambian más rápido de lo que el proceso puede documentar riesgos nuevos.
  Automatízalo, quizá integrando un agente con el proceso de revisión de seguridad.
- **Entiende quién los construyó y por qué.** En este caso, personas no ingenieras construyeron
  los agentes de GRC con Claude Code sobre una plataforma interna de aplicaciones de negocio. La
  gente rodea a seguridad porque el camino autorizado es lento, y ese es el origen de la mayor
  parte de la adopción en la sombra. Un analista de cumplimiento que puede construir la
  herramienta que necesita, donde tú puedes verla, no es adopción en la sombra.
- **La responsabilidad humana es parte del flujo de trabajo.** Aceptar riesgo deliberadamente es
  un acto que realizan personas con autoridad para aceptarlo. Con un registro de riesgos vivo y un
  consejo ejecutivo de riesgo detrás (ISO 42001 o equivalente), las reevaluaciones llegan a quien
  puede aceptarlas y las cláusulas marcadas llegan a quien las negocia. Si ya tienes ISO 27001,
  añadir 42001 suele ser incremental con tu auditor actual.

## Diseña para el modelo de dentro de seis meses

Si diseñas tu programa para lo que el modelo puede hacer hoy, estarás por detrás cuando el
programa se lance. Más inteligencia habilita más grados de libertad y deja obsoletos los
andamiajes elaborados con prompts meticulosos; si apoyas tus controles en ellos, serán recortados
en futuras generaciones de aplicaciones internas y te quedarás sin punto de control.

Los agentes que tienen sus propias cuentas y ejecutan flujos de trabajo de varios días ya operan
dentro de las organizaciones, y deben gobernarse como se gobierna a las personas: identidad,
mínimo privilegio, monitorización y un programa de riesgo interno capaz de responder en minutos.
Las organizaciones que desarrollen ese músculo ahora, con agentes de bajo riesgo, estarán listas
para decir que sí cuando lleguen los casos de alta autonomía.

## Tres lugares por donde empezar

1. **Elige el caso de uso agéntico con más presión interna** y pásalo por las cuatro preguntas. La
   meta es encontrar las condiciones bajo las que lo aprobarías, no emitir un veredicto.
2. **Lleva los siete requisitos a los equipos y proveedores a los que ya pagas.** Pregunta a tu
   IdP, a tu SIEM y a cualquier proveedor de agentes cuáles de ellos pueden mostrarte funcionando
   hoy en tu stack.
3. **Decide tu frontera de confianza.** Escribe qué cuenta como contenido no confiable en tu
   entorno. Cada decisión futura sobre agentes se vuelve más fácil una vez que esa línea existe.

Esperar riesgo cero es esperar para siempre. La web es adversaria, los modelos evolucionan rápido,
y las organizaciones que aprendan a dimensionar y aceptar este riesgo ahora son las que obtendrán
la ventaja.

## Fuente

["Zero risk isn't the job: a CISO's guide to agentic AI"](https://claude.com/blog/ciso-guide-to-agentic-ai),
por Jason Clinton, Deputy CISO de Anthropic — publicado el 17 de julio de 2026. Los controles,
certificaciones y white papers detrás del artículo están en
[trust.anthropic.com](https://trust.anthropic.com).
