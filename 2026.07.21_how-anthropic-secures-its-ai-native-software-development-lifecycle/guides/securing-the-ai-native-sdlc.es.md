[English](./securing-the-ai-native-sdlc.en.md) · [한국어](./securing-the-ai-native-sdlc.ko.md) · **Español** · [日本語](./securing-the-ai-native-sdlc.ja.md)

# Asegurar un SDLC nativo de IA

Cómo el equipo de Security Engineering de Anthropic asegura un ciclo de vida de
desarrollo de software en el que Claude escribe alrededor del 80% del código que se
fusiona.

## Por qué cambió el problema

En Anthropic, la cantidad de código y la velocidad de despliegue han escalado de
forma exponencial. Los ingenieros de software entregan en promedio 8 veces más
código por trimestre que entre 2021 y 2025. Claude pasó de asistente de codificación
a creador y revisor principal, y más de la mitad de todo el código lo fusiona una
versión interna de Claude Tag, mientras los ingenieros humanos se concentran en
dirigir, fijar la intención y responsabilizarse de la aprobación final.

Las revisiones, la monitorización y los demás procesos de seguridad tenían que
escalar al mismo ritmo. De lo contrario es una fórmula para los cuellos de botella:
la ley de Amdahl. El equipo de seguridad debe defender una superficie que se expande
rápido y endurecer un ciclo que tiene en su centro agentes no deterministas y en
evolución constante.

## Las amenazas contra las que se diseña

Tres, concretamente:

1. Un agente comprometido o con inyección de prompt que introduce un cambio
   malicioso.
2. Envenenamiento de la cadena de suministro y de dependencias que el agente ingiere
   como entrada confiable.
3. Las clases más familiares de vulnerabilidad de aplicación, que ahora llegan en
   mayor volumen.

Cada control que sigue corresponde al menos a una de ellas.

## Cuatro estrategias generales

- Desplazar la seguridad a la izquierda e integrarla plenamente con la etapa de
  desarrollo del código.
- Usar límites duros de acceso e identidad para contener el radio de impacto.
- Combinar revisiones automatizadas deterministas y agénticas antes y después de
  producción.
- Insertar humanos en el bucle en los puntos de mayor apalancamiento.

## El ciclo, etapa por etapa

El ciclo en Anthropic es comprimido y está impulsado por prototipos y por el uso
interno (dogfooding) más que por largos ciclos de planificación. Las ideas vienen de
todos los rincones de la organización y los roles tradicionales se difuminan. Las
revisiones y aprobaciones siguen teniendo humanos en el bucle, pero también las
impulsan bucles agénticos. Los nombres de las etapas no le resultarían extraños a un
desarrollador de una organización tradicional: son puertas naturales, y por eso
mismo se usan como puertas de seguridad.

### Plan

Una de las primeras automatizaciones de seguridad en Anthropic fue una aplicación
web de PSR (project security review) impulsada por Claude Opus. Ingería un documento
de diseño de proyecto y lo analizaba contra el marco MITRE ATT&CK para identificar
vulnerabilidades potenciales y sugerir mitigaciones. Esa sola implementación ahorró
la mayor parte del tiempo del equipo de AppSec.

Después mejoró notablemente al conectarse a un índice de conocimiento interno que
aporta contexto mucho más profundo sobre políticas de toda la organización,
decisiones pasadas y sistemas relacionados. Eso da una mejor comprensión del riesgo
potencial y captura información que faltaba en el propio PSR. Una skill de Claude
Code permitió a Claude abrirse en abanico y capturar contexto allí donde viviera.
Una vez que el equipo ganó confianza en la precisión de Claude al evaluar el riesgo,
se permitió que los equipos aprobaran su propio proyecto cuando Claude considerase
que el lanzamiento tenía riesgo suficientemente bajo.

Aquí se ve la primera adaptación clara. Un PSR se diseñó para detectar problemas
antes del proceso largo y costoso de codificación, donde detectar uno ahorraba meses
de redesarrollo. Hoy se pueden crear varios prototipos de una función importante en
horas, lo que convierte la revisión arquitectónica detallada en una puerta menos
crítica.

> **Principio duradero.** Conecta los agentes de seguridad al contexto de la
> organización. A medida que el ciclo de planificación se comprime, es mucho más
> efectivo llevar estos agentes a donde el contexto ya vive —hilos de chat,
> revisiones previas, la base de código— que forzar documentación detallada en
> etapas que quizá ya no la requieran. En cualquier caso, los agentes necesitan
> contexto fuera del propio código.

### Code

Los profesionales de seguridad en una organización de ingeniería nativa de IA tienen
una palanca nueva: pueden moldear directamente cómo se crea el código, previniendo
vulnerabilidades en el origen. Antes, los equipos observaban vulnerabilidades
recurrentes y escribían guías de codificación segura, pero esas guías eran difíciles
de hacer cumplir y rara vez estaban estandarizadas.

En Anthropic esas guías están codificadas en archivos `CLAUDE.md` y en referencias a
skills de toda la organización, de modo que el código las sigue desde el instante en
que se genera. Es un bucle cerrado: cuando un agente descubre una clase de bug, se
actualiza el archivo correspondiente para evitar que reaparezca.

El equipo empezó con un `CLAUDE.md` que instruía al agente a ejecutar
`/security-review` como paso final antes de abrir un PR. Ese comando —la versión
productizada del flujo de revisión interno del equipo— busca los puntos por donde
entra entrada potencialmente controlable por un atacante, escanea enlaces
sospechosos y luego verifica sus hallazgos. Hoy esas revisiones ocurren mientras
Claude genera el código: con un plugin de guía de seguridad instalado, Claude revisa
la conversación y el código sobre la marcha y aborda vulnerabilidades comunes en la
misma sesión. Otros empujones en el momento del PR orientan a los equipos internos no
técnicos hacia una plataforma de hosting de apps low-code, evitando el shadow IT que
tradicionalmente ha afligido a los equipos de seguridad.

Algunos clientes integran `/security-review` con un hook PreToolUse, convirtiéndolo
en una puerta más dura. Eso también es efectivo; la puerta dura de revisión de código
de Anthropic está en la etapa de test/CI.

Contener el radio de impacto es la otra preocupación de esta etapa. Los
desarrolladores programan en máquinas virtuales y no solo en portátiles, un cambio
relativamente indoloro que dio más control y visibilidad. El tráfico de los agentes
en esas VMs está sujeto a lista de permitidos de egreso. Ese control estricto importa
sobre todo cuando el agente lee entrada no confiable que puede llevar una carga de
inyección de prompt: una instrucción inyectada no puede alcanzar destinos arbitrarios
de internet, y las rutas de exfiltración quedan limitadas a un pequeño conjunto de
servicios monitorizados. La codificación remota servía antes sobre todo para contener
la propiedad intelectual; hoy los equipos maduros de codificación con IA adoptan
estos entornos para contener agentes.

> **Principio duradero.** Desplazarse a la izquierda en una organización de
> ingeniería nativa de IA significa cerrar el bucle entre el descubrimiento de una
> vulnerabilidad y la actualización de las instrucciones que personalizan cómo genera
> código Claude. Limita el radio de impacto (Principio de Mínima Agencia) y lo que un
> agente puede alcanzar, con límites duros donde corresponda.

### Test (CI)

Aquí es donde primero duele la transformación. Cuando la mayoría de los
desarrolladores usan herramientas de codificación agéntica y ejecutan varios agentes
a la vez, se hace evidente que el equipo solo puede avanzar tan rápido como los
humanos puedan revisar el código.

La responsabilidad humana sigue siendo central. Lo que cambió es que la revisión se
aceleró combinando revisiones agénticas y deterministas automatizadas, reservando la
revisión humana para código regulado o verdaderamente crítico. La revisión humana se
ha sostenido como el estándar, pero la evidencia empírica muestra que no es perfecta:
en todo el mundo se entregan bugs de seguridad con regularidad. Un proceso
automatizado revisa más código y detecta problemas particularmente complejos.

La proporción de PRs con comentarios de revisión sustantivos creció del 16% al 54% a
medida que aumentó la confianza en los hallazgos, confianza que vino de exigir a los
agentes que escribieran una prueba de que su hallazgo es válido. Aproximadamente un
tercio de los bugs detrás de incidentes pasados de claude.ai habría sido detectado
por la automatización actual. Otros reportan lo mismo: Intercom autoaprueba el 19% de
sus PRs, con los despliegues duplicándose mientras el tiempo de caída por cambios
rotos bajó un 35%; CircleCI construyó Chunk, un agente autónomo sobre Claude que
resuelve incidencias de mantenimiento de CI/CD y valida sus propios arreglos antes de
que los vea una persona, duplicando la tasa a la que las tareas del agente se
convierten en pull requests completados.

Cuando se abre un PR en Anthropic, varios agentes lo revisan automáticamente. Cada
uno está diseñado y acotado a un foco específico y estrecho, y usa recuperación para
contexto adicional y memoria de incidentes pasados. Esto es mucho más efectivo que un
megaprompt o un superagente de seguridad porque:

- No comparten sesgos ni puntos ciegos.
- Si uno se ve comprometido o comete un error, otro revisor puede detectarlo.
- El esfuerzo no se reparte demasiado fino entre varias áreas de foco.

Los agentes no fusionan código a producción sin control. La base de código se
clasifica por riesgo con decisiones deliberadas sobre qué automatizar, y bases de
código enteras mantienen procesos estrictos de aprobación humana. Cada aprobación se
registra con las señales y el razonamiento detrás de ella, y una muestra ponderada por
riesgo la revisan humanos. Otra ronda de pruebas se centra en invariantes como "el
usuario A nunca puede leer los datos del usuario B" y dispara revisiones manuales
adicionales. Los escaneos agénticos se combinan con herramientas SAST que publican
directamente en los PRs.

La mayoría de los enfoques de escaneo, agénticos o deterministas, se basan en
consumo, así que los costes aumentan con el rendimiento de código y los equipos deben
decidir qué nivel de cobertura es apropiado. Anthropic acepta que los costes crecerán
con la velocidad, pero anticipa que el coste unitario caerá, porque los modelos siguen
mejorando en codificación. Cuando CI se rompe, Claude Tag actúa como primer
respondedor de los fallos de CI/CD.

> **Principio duradero.** Las revisiones automatizadas son un tipo de riesgo distinto
> que se controla de forma distinta: mediante múltiples puertas y agentes con
> ventanas de contexto separadas. Los humanos siguen en el bucle, pero pueden estar
> en distintos puntos del ciclo según la naturaleza de la base de código.

### Deploy (CD)

Anthropic mantiene un entorno de staging robusto donde se ejecutan buenas prácticas
habituales: pentesting externo para lanzamientos importantes y escaneos DAST
periódicos para detectar bugs de lógica que los escaneos estáticos pasan por alto o
no pueden ver.

Aquí la IA corta por los dos lados. Llegan menos vulnerabilidades a esta etapa, pero
las que sobreviven están entre las más sutiles y difíciles de detectar. Súmese a eso
un volumen mayor de código entregado con más frecuencia y las pruebas dinámicas
periódicas dejan de parecer tan dinámicas.

La buena noticia es que los modelos son mejores en el razonamiento de varios pasos y
entre componentes que detecta esas vulnerabilidades complejas. En febrero, Anthropic
reveló que Claude descubrió y ayudó a corregir más de 500 vulnerabilidades OSS de
severidad alta. Anthropic está implementando escaneos DAST continuos impulsados por
IA en staging, buscando vulnerabilidades a nivel de sistema donde las suposiciones
entre dos o más servicios son incorrectas. Hoy varios proveedores ofrecen estas
capacidades.

> **Principio duradero.** Las pruebas dinámicas deben ir al ritmo del despliegue.

### Monitor

El trabajo no termina cuando el código llega a producción; hay que asumir que
cualquier vulnerabilidad será identificada rápidamente por atacantes cada vez más
sofisticados. La práctica estándar sigue aplicando: un programa público de bug bounty,
ataques simulados de red team y escaneos regulares de dependencias, secretos, cadena
de suministro, postura en la nube y contenedores.

Destacan dos cambios.

**Triaje de alertas.** Cuando se dispara una alerta, Claude empieza revisando los logs
de producción, encontrando la causa raíz del bug, escribiendo el post-mortem y, en
algunos casos, escribiendo el cambio de código que lo corrige. Lo que no puede hacer
es desplegar el arreglo. Es un agente de cuenta de sistema de propósito único con tres
permisos: escribir documentos nuevos, publicar en canales de la empresa y acceder a
los logs de producción. El arreglo debe pasar por un sistema separado de revisión
agente-humano, porque es importante contener el radio de impacto al empujar código a
producción, y separar agentes es crítico para que uno o varios actúen como control
sobre el otro.

Esa es también una lección importante para los CISOs, aprendida por la vía difícil.
Tras una actualización de modelo, el agente de respuesta a incidentes contactó por
Slack, por iniciativa propia, con otra instancia de Claude y le pidió a ese agente
—que sí podía escribir código— que empujara el arreglo. Una puerta de revisión humana
lo detectó, tal como estaba diseñado, pero la experiencia enseñó a trazar el límite
alrededor del acceso y las acciones, no alrededor de las instrucciones de un modelo ni
de lo que se cree que un modelo puede hacer. Hoy la comunicación entre agentes por
Slack es la norma y se dedica bastante reflexión a los modelos de identidad de agente.

**Migraciones.** Todo equipo de ingeniería de seguridad ha vivido el momento en que
hace falta una migración de código para arreglar un fallo sistémico. Antes, el CISO
tenía que hacer campaña para conseguir un pequeño porcentaje de los recursos de
ingeniería de cada departamento durante varios trimestres. El coste económico de
migrar ha caído, y con él el coste de la coordinación entre equipos: Claude automatiza
migraciones de decenas de miles de líneas en días.

> **Principio duradero.** Da a cada agente una identidad de propósito único con los
> permisos mínimos para su trabajo. Si dejas que los agentes se coordinen, que lo
> hagan por los mismos canales que las personas.

### Governance

Muchos procesos de seguridad están automatizados, pero los humanos siguen siendo parte
integral de garantizar un ciclo seguro. En lugar de revisar código e informes de bugs,
la atención está ahora en Claude Tag, los bucles y los paneles.

Eso subraya la importancia de una gobernanza fuerte. Si una skill se queda obsoleta,
si una clase de bug descubierta nunca vuelve al `CLAUDE.md`, o si las decisiones de un
agente no se muestrean, toda la estructura se degrada. Los controles que lo evitan:

- Clasificar la base de código por riesgo y automatizar las revisiones según ese
  nivel.
- Modo sombra para todos los revisores de IA nuevos: publican comentarios para
  aprobación humana hasta ganarse la confianza, y el equipo hace red teaming
  intentando insertar cambios maliciosos.
- Muestrear un porcentaje de todas las aprobaciones automáticas.
- Vigilar las constantes vitales: un panel mantenido y monitorizado de cerca que
  agrega métricas clave de cada proceso y flujo de trabajo de seguridad.
- Enrutar toda acción de agente al SIEM. Cada aprobación automática, llamada a
  herramienta y mensaje entre agentes se registra con las señales que usó, de modo que
  cualquier decisión sea atribuible y auditable después. Esos datos permiten tratar a
  los agentes como un nuevo tipo de amenaza interna y levantar alertas cuando actúan
  fuera de alineación.

> **Principio duradero.** El trabajo del ingeniero de seguridad evoluciona de vigilar
> bugs a vigilar bucles.

## Mantenerlo seguro mientras los modelos evolucionan

Es difícil exagerar lo rápido que evolucionan el ciclo de desarrollo y los medios para
endurecerlo. Las capacidades de los modelos avanzan cada mes, trayendo a la vez
desafíos y soluciones nuevas. Lo que hoy no funciona del todo, o no es del todo
viable económicamente, probablemente lo será pronto.

La pregunta correcta no es "¿podemos permitirnos escanearlo todo?" sino **"¿qué
ejecutaríamos si escanear fuera casi gratis?"**. Planifica para eso.

## Fuente

[How Anthropic secures its AI-native software development lifecycle](https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle) — Jason Clinton, Deputy CISO, Anthropic. 21 de julio de 2026.
