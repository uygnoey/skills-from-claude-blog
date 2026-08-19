[English](./agentic-ci-on-call.en.md) · [한국어](./agentic-ci-on-call.ko.md) · **Español** · [日本語](./agentic-ci-on-call.ja.md)

# Guardia de CI agéntica

Guía metodológica para convertir a un agente en el primer respondedor de una rotación de guardia de CI/CD, a partir del relato de cómo lo hace el equipo de Integración Continua de Anthropic.

## La tesis

La rotación no consiste sobre todo en problemas difíciles. Consiste sobre todo en verificar alertas, reunir evidencia, publicar actualizaciones de estado y escribir notas de traspaso: trabajo tedioso, que interrumpe y que se repite mecánicamente. Un agente que absorbe esas partes da a cada incidente un primer respondedor inmediato y devuelve al ingeniero el trabajo arquitectónico que de verdad mueve la fiabilidad.

La versión medida de esa tesis, en el relato original: durante varios meses el agente redactó el informe de situación inicial en todos los incidentes recientes que tuvieron uno, normalmente en unos 15 minutos, con una mediana de unos 14 minutos hasta el primer análisis fundamentado en evidencia y un mejor caso de unos 4.

## Cuatro ingredientes

Todo el diseño se deriva de cuatro requisitos. Un agente de guardia necesita:

- **Memoria** — para recordar qué se ha hecho, dentro de un incidente y entre incidentes.
- **Conexiones y acceso** — para investigar, entender y actuar.
- **Horarios** — para saber cuándo volver al trabajo.
- **Instrucciones** — para saber qué hacer.

### Memoria

Dos capas. El canal de chat mantiene la memoria de trabajo dentro de un incidente y entre ellos, de modo que el contexto viaja de turno en turno. Un archivo de lecciones versionado guarda la memoria duradera: qué pasó, la causa raíz, el arreglo y el detalle que conviene recordar, añadido tras cada incidente y leído al comienzo de cada investigación nueva.

La segunda capa es la que hace que el sistema mejore en vez de simplemente funcionar. También es donde viven las lecciones de proceso: entradas sobre cómo investiga el equipo, no solo sobre qué se rompió.

### Conexiones y acceso

Una cuenta de servicio con las herramientas que un ingeniero de guardia usa realmente —plataformas de observabilidad, almacén de logs, sistema de avisos, control de código, acceso al clúster, canales de incidentes—, alcanzadas mediante conectores MCP y concedidas una sola vez por un administrador.

Dos notas de diseño que conviene retener:

- **Añade el agente también a los canales adyacentes**, no solo al de guardia: alertas de servicio, cambios de configuración, despliegues, actualizaciones de PR. Correlacionar un síntoma con un cambio hecho horas antes solo funciona si el agente vio ese cambio.
- **Concede primero acceso de lectura.** Cada capacidad de escritura es una decisión aparte con su propio radio de impacto.

### Horarios

Las rutinas se piden en lenguaje natural en el canal; por ejemplo, solicitar que el traspaso de CI se ejecute cada lunes por la mañana. La petición dice *cuándo*; los archivos de instrucciones dicen *qué*.

### Instrucciones

Las instrucciones permanentes son archivos markdown guardados como skills en un repositorio, no mensajes fijados ni documentos personales. Varias personas del equipo pueden iterarlas y los cambios se gestionan como código. El conjunto incluye instrucciones de enrutamiento, políticas y el registro de lecciones que impulsa el ciclo de mejora.

## El ciclo de vida

### Detección: alertas deterministas, escalado agéntico

La frase más transferible del relato original es esta división: **el proceso de alertas es determinista, mientras que el escalado de guardia tiene rutas deterministas y agénticas.**

Las reglas siguen siendo reglas. El agente trabaja en sus dos extremos.

Antes de que las reglas sean buenas, resuelve el arranque en frío: nadie puede fijar umbrales correctos en un servicio nuevo sin historial de tráfico, así que el agente analiza los primeros días de datos y alertas, propone reglas nuevas y ajusta las mal dimensionadas.

Después de que las reglas disparen, resuelve la fatiga de alertas: verificar cada alerta es tedioso y la atención humana se degrada, mientras que la del agente no lo hace del mismo modo. Aplica criterios concretos del archivo raíz de instrucciones —un umbral, una duración, una excepción para ventanas de despliegue conocidas— y o bien avisa a la guardia o bien escribe la alerta en el registro de lecciones.

Otras vías de entrada permanecen: alguien del equipo que reporta un problema en el canal, o un incidente abierto por el proceso interno que provisiona un canal. Todas convergen en el mismo respondedor.

### Triaje: investigación paralela, guiada por experiencia codificada

Filtrar ruido es la victoria pequeña. La investigación es la grande.

El agente arranca un flujo de trabajo dinámico. Un agente de orquestación levanta subagentes ejecutores que investigan en paralelo cada dependencia y fuente de verdad: paneles, logs, historial de avisos, control de código, clúster, canales de incidentes relacionados. Los ejecutores informan de vuelta; el orquestador sintetiza un único informe de situación coherente en lugar de un montón de salida cruda.

El paralelismo es el mecanismo. Perseguir varias pistas a la vez es lo que trae la primera hipótesis fundamentada al primer cuarto de hora.

Los agentes no buscan a ciegas. Dos artefactos los guían:

**Una skill de investigación por clase de fallo.** Un ejemplo del relato original llega a 617 líneas para una sola clase de fallo y codifica cada paso que da el ingeniero. Y lo decisivo: no se escribió de antemano desde la memoria, sino depurando un incidente real turno a turno con el agente y pidiéndole después que escribiera el archivo a partir de esa sesión. Es la forma fiable de capturar los pasos que un ingeniero con experiencia ejecuta sin darse cuenta.

**El registro de lecciones**, leído primero, para que la hipótesis inicial parta de la realidad reciente.

Lo que sigue siendo humano: la intuición y la experiencia. El agente no siempre acierta a la primera, y el equipo investiga en modo multijugador: cualquiera puede reorientar o añadir una hipótesis en tiempo real.

### Resolución: acotada por el alcance de permisos

Que un agente deba arreglar cosas varía según el equipo. La división del relato original es por permisos, no por capacidad:

- **El despliegue progresivo tras feature flags** corre en un agente *aparte*, creado en un agente de código, con los permisos de un ingeniero nombrado. Su primera etapa gestiona el tráfico canario, vigila incidencias y sube o baja la bandera.
- **Las acciones sobre el clúster** —drenar, acordonar— llegan como recomendaciones.
- **Los pasos de escalado** para picos de demanda llegan completos y los ejecuta una persona.
- **Los arreglos como PR**, lo más frecuente: la guardia revisa, fusiona y despliega.

### Verificación, comunicación y traspaso

La verificación reutiliza las herramientas de la investigación. Un arreglo está hecho cuando la señal vuelve a su línea base, no cuando el cambio se fusiona.

El post-mortem se añade al registro de lecciones automáticamente, como parte de las instrucciones permanentes.

La comunicación pública tiene su propio agente. En el relato original, `ci-weather` reúne canales de incidentes, métricas de build, estadísticas de la cola de merge y retraso de despliegue en un informe estilo redacción publicado en un canal que cualquiera puede leer, de modo que la gente consulta el canal en vez de preguntar a la guardia si debe retener sus merges.

Una advertencia honesta del autor: el formato necesitó varias iteraciones. Un agente puede generar de una sola vez una skill que produce un informe de estado, pero lo que lo hace legible es el gusto propio del equipo. Esa parte es comunicación humana, no fontanería.

Los informes de traspaso para personas se generan a diario y cada semana, para que alguien pueda continuar donde otro lo dejó.

## El ciclo de mejora

1. Incidente resuelto.
2. El agente añade la entrada al registro de lecciones.
3. La siguiente investigación empieza leyéndolo.
4. Los patrones recurrentes se promueven a la skill de investigación.

Las mejores entradas suelen tratar del método y no del mecanismo. La favorita del autor es una que el agente escribió sobre él, después de que teorizara a partir de un archivo de configuración antes de mirar las métricas: consulta primero los datos y teoriza después, porque la configuración dice qué podría fallar y las métricas dicen qué falló.

## Lo que no debe cambiar

El argumento de volumen que sostiene todo esto: los ingenieros del relato entregan aproximadamente 8 veces más código por trimestre que entre 2021 y 2025. La codificación agéntica a ese ritmo necesita una CI agéntica para seguirle el paso.

El listón de calidad se mantuvo porque las barreras no se movieron:

- Cada PR tiene una persona propietaria nombrada.
- Cada cambio requiere aprobación para fusionarse.
- Cada cambio pasa las mismas puertas de CI.

Escalar el sistema de respuesta no es lo mismo que aflojar las condiciones de lo que se fusiona. Lo primero es el objetivo; lo segundo lo destruiría.

## Cómo empezar

El relato describe la puesta en marcha en horas, no días, y enumera los pasos: hace falta un plan Team o Enterprise; el propietario de la organización añade el agente al canal de guardia; conecta los conectores adecuados, el repositorio con las instrucciones permanentes y el acceso remoto del agente de código; y después se añade el agente al canal de incidentes con la instrucción de vigilar y triar de inmediato.

El equipo también publicó un kit de configuración generalizado que convierte el historial de incidentes del propio equipo en manuales de triaje y deja en el canal un agente de solo lectura que diagnostica, escala y aprende. El enlace está en el post original.

## Fuente

- https://claude.com/blog/ai-ci-cd-on-call
