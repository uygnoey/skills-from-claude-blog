[English](./auto-mode-in-production-patterns.en.md) · [한국어](./auto-mode-in-production-patterns.ko.md) · **Español** · [日本語](./auto-mode-in-production-patterns.ja.md)

# El modo auto en producción: patrones de Nuro, Gusto y Garner Health

Fuente: https://claude.com/blog/auto-mode-in-production (7 de agosto de 2026)

## El dilema que resuelve el modo auto

El modo auto es ahora el ajuste predeterminado de Claude Code. En lugar de pedirte que
apruebes cada comando que un agente quiere ejecutar, un clasificador evalúa cada acción y
bloquea las que parecen potencialmente dañinas.

Su diseño resuelve un dilema habitual de la programación agéntica:

- **Revisar cada comando** mantiene a una persona en el bucle, pero cuando las sesiones se
  alargan durante horas o se multiplican en paralelo, esa supervisión se convierte en el cuello
  de botella.
- **Saltarse por completo las comprobaciones de permisos** es más rápido, y también es la vía
  por la que se cuelan la inyección de prompts, la deriva de alcance y algún recurso de
  producción borrado.

En evaluaciones internas, el clasificador detectó más acciones peligrosas que los
desarrolladores al aprobar avisos a mano, y su rendimiento se mantuvo bajo red-teaming
externo. Como las sesiones se detienen menos, Claude trabaja **9 veces más tiempo entre
interrupciones** que con el predeterminado anterior, en el conjunto del uso de Claude Code.

## Nuro — agentes autónomos que corren más tiempo

Nuro, la empresa de IA física que desarrolla tecnología universal de conducción autónoma de
nivel 4, adoptó Claude Code a finales de 2025; en marzo ya era la herramienta de programación
agéntica más popular de la compañía.

**El problema antes del modo auto.** El ingeniero de software Kai Zhou había prototipado un
sustituto interno: un hook que enviaba cada acción pendiente a un modelo pequeño, aprobaba
automáticamente el 90 por ciento de lo rutinario y derivaba lo sensible a Slack para revisión
humana. Respondía a una tensión real: a los ingenieros les molestaba vigilar los avisos de
aprobación, pero desde el punto de vista de seguridad y legal de la empresa, saltarse los
permisos era demasiado peligroso para autorizarlo. Cuando llegó el modo auto, Kai archivó el
proyecto paralelo.

**Cómo funciona hoy.**

- Modo auto para todo lo que escribe: «Uso el modo auto en el 100 por cien de mi trabajo de
  programación. La mayoría de las veces abro tres o cuatro sesiones en paralelo en modo auto y
  solo entro cuando hace falta».
- **La excepción es el trabajo que toca a otros equipos.** Cuando Claude Code revisa un pull
  request en su nombre, Kai vuelve al modo interactivo y revisa cada uno antes de que salga.
- **Tampoco corre sin límites.** Nuro se apoya mucho en skills, y los ingenieros deniegan de
  plano en su configuración los comandos más peligrosos, como los borrados recursivos. El
  clasificador decide dentro de esas barreras.

**La gran ganancia: trabajo que sigue corriendo cuando los ingenieros terminan su jornada.** El
equipo de Kai usa el modo auto para agentes de investigación de larga duración que mejoran de
forma incremental las métricas de evaluación de su pila de conducción autónoma: tareas con una
señal clara y medible contra la que el agente puede iterar por su cuenta. Durante la noche, un
agente puede estudiar los falsos negativos que marca la suite de evaluación, redactar una
propuesta, ejecutar experimentos y seguir iterando sobre los resultados. El enfoque se extiende
a cualquier tarea con un método de evaluación claro, porque la propia métrica le dice al agente
si mejora o empeora; otro equipo de Nuro lo usa para reducir la huella de memoria de un binario
concreto.

> «El otro día lancé un agente a las 10 de la noche y siguió corriendo hasta las 5 de la
> mañana, y me dio tres PR por la mañana. Me parece bastante impresionante. Solo el modo auto
> permite este tipo de carga de trabajo».

## Gusto — entregar PR más rápido y con más seguridad

En Gusto, una empresa líder de tecnología para pymes, el paso al modo auto empezó como una
mejora de seguridad proactiva.

**Martin Emde, equipo de AI Dev Tools.** Había visto cómo la fatiga de permisos ralentizaba al
equipo. El modo auto les dio la misma velocidad sin sacrificar control ni seguridad, y desde
que la adopción se consolidó en ingeniería, la carga general de permisos ha bajado de forma
notable.

- 2.425 sesiones de Claude Code desde diciembre, con el modo auto como herramienta diaria.
- El trabajo entre repositorios, que antes se atascaba en aprobaciones de acceso a carpetas,
  ahora corre sin interrupciones.
- Trabajos desatendidos —compilar notas diarias de GitHub, Slack y Jira— se ejecutan solos.
- Alrededor del **10% de las transcripciones de sesión desde mediados de mayo de 2026 incluía
  una denegación del modo auto**, señal de que el clasificador hace trabajo real sin lastrar
  tareas legítimas.

> «El modo auto nos dio un equilibrio más seguro entre velocidad y control. Pudimos eliminar
> los avisos repetidos y aumentar la productividad sin comprometer la seguridad. Vemos que el
> modo auto bloquea en el momento adecuado, y eso nos da la confianza para movernos rápido».

**Chad Kunsman, equipo de AIT Cloud Engineering.** Llegó a la misma conclusión desde el otro
lado. Su trabajo —investigación de endpoints, auditorías de logs, gestión de conectores,
ingesta de documentación a través de una pila de servidores MCP— transcurre en ráfagas cortas
de veinte minutos, no en maratones nocturnos. No buscaba sesiones más largas; quería el ritmo
sin manos de bypass permissions sin la exposición de que se colara un prompt malo o una
inyección de prompts.

> «Dada la protección contra la inyección de prompts, y la forma en que comprueba que lo que
> estás haciendo encaja realmente con lo que pediste, es mejor opción que bypass permissions y
> mucho más rápido que los avisos de permiso».

En las raras ocasiones en que el clasificador interviene, dice que acierta: «Cuando me detuvo,
tenía sentido y explicó por qué. Se estaba desviando de lo que yo había pedido, y consultó. No
estuvo nada desencaminado».

**Dónde sale del modo auto.** Cuando una sesión se mete de lleno en infraestructura de
producción —Terraform, AWS, llamadas POST directas contra APIs en vivo— cambia a accept edits y
verifica cada llamada a herramienta a mano. «Tienes que sopesar el tiempo que ahorras frente a
aquello en lo que razonablemente podría equivocarse, y lo catastrófico que sería. Al final,
sigues siendo responsable de lo que pase».

Ese criterio opera dentro de un esquema más amplio de defensa en profundidad: Gusto enruta su
tráfico MCP por una capa de proxy gobernada con guardas de herramientas e inspección de
prompts, de modo que los agentes trabajan con permisos muy acotados antes de que el modo auto
intervenga.

## Garner Health — acelerar el ciclo de vida del desarrollo (SDLC)

Garner Health, la empresa de tecnología sanitaria, desplegó Claude Code en febrero a sus 550
empleados de todas las funciones. La herramienta está conectada a los sistemas centrales,
incluidos Salesforce, Zendesk y Snowflake, y se anima a los empleados a dedicar unas dos horas
por semana a automatizar las partes más repetibles de su trabajo.

**Antes del modo auto,** esa escala traía sobrecarga. Evan Magnussen, responsable de ingeniería
de plataforma, describe la gestión de permisos como un ciclo tedioso de curar a mano listas de
comandos aprobados y ver cómo se rechazaban comandos encadenados.

**Hoy,** Evan y la mayoría de sus colegas usan el modo auto en cada sesión, desde investigar el
código hasta gestionar integraciones externas a través de MCP.

> «Hemos construido un ciclo de vida de desarrollo estandarizado para toda la organización de
> ingeniería que en realidad solo es posible gracias al modo auto. Los empleados lo viven como
> un peso menos. Ya no tienen que vigilar sus agentes durante horas».

**Ese ciclo funciona como un plugin de skills estandarizadas.** Un agente toma una tarea,
explora el contexto al que tiene acceso, commitea archivos de contexto al repositorio, ejecuta
lo que Evan llama «investigación antagonista» para poner a prueba sus propias suposiciones y
después pasa a la implementación, deteniéndose ante una persona solo cuando necesita contexto
que no puede encontrar por su cuenta. Las fases más intensivas en investigación, señala Evan, no
eran posibles antes del modo auto.

**Ajustes.** De fábrica, el clasificador ha necesitado poco ajuste. La única modificación de
Evan coincide con la de Kai en Nuro: configuró el modo auto para que no apruebe acciones que
comuniquen con otras personas, como enviar mensajes de Slack o correos. «Personalmente no me
gusta que Claude actúe en mi nombre cuando me comunico con otra persona». Los equipos que
trabajan sobre propiedad intelectual central —los más escépticos ante saltarse permisos antes
del modo auto— aprendieron a ajustar los prompts inyectados al clasificador para que fuera más
o menos permisivo con su trabajo.

**Su consejo para otras empresas.** Apostar por ello y construir los controles adecuados para
empoderar a los ingenieros garantizando un despliegue seguro. «Si dijéramos: todos a construir
vuestros propios flujos, y no tuviéramos telemetría, sería muy peligroso. Como tenemos la
telemetría, como hemos construido flujos relativamente estándar, tenemos mucha más confianza».

## Los patrones que conviene copiar

1. **Fija primero barreras duras en la configuración.** El clasificador decide dentro de los
   límites que tú defines; no los sustituye.
2. **Acota las herramientas antes de que el clasificador las vea.** Un proxy MCP gobernado con
   guardas de herramientas e inspección de prompts hace que los agentes ya operen con permisos
   estrechos.
3. **Aplica por defecto un único ajuste acotado:** no aprobar automáticamente acciones que
   comuniquen con otras personas. Dos de los tres equipos llegaron a ello por separado.
4. **Decide de antemano qué sesiones salen del modo auto:** el trabajo que cruza tu frontera y
   la infraestructura de producción.
5. **Ajusta la forma de la tarea al trabajo desatendido.** Una señal de evaluación clara y
   medible es lo que permite a un agente iterar de noche. El entregable son PR terminados para
   revisión, no cambios fusionados.
6. **Estandariza el flujo y luego instruméntalo.** La telemetría es la condición previa que
   hace defendible un despliegue de empresa, no una tarea posterior.
7. **Vigila la tasa de denegaciones.** Que en torno al 10% de las sesiones incluya una
   denegación se lee como un clasificador que hace trabajo real sin obstruir tareas legítimas.
