[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Es el segundo artículo de una serie sobre cómo construir equipos formados por personas y agentes: una entrevista con Jaime DeLanghe, Chief Product Officer de Slack. DeLanghe entró en Slack en 2017 para trabajar en búsqueda y aprendizaje automático, con el objetivo de convertir la conversación de trabajo en conocimiento institucional, y desde el principio ha sostenido que eso solo funciona si la gente trabaja en abierto. El post extiende ese argumento a los agentes: la conversación alrededor del trabajo es el contexto que los agentes necesitan para resultar útiles.

Se recorren seis áreas de práctica, cada una con recomendaciones concretas para llevarlas a cabo: tratar el historial de conversación como una base de conocimiento, los relevos entre personas y agentes, dar a los agentes papeles claros, mantener los canales públicos por defecto, difundir la adopción con el ejemplo, y medir resultados en lugar de actividad.

## ¿Cuándo es útil?
- Cuando los agentes tienen acceso al espacio de trabajo pero producen resultados superficiales porque las decisiones y su razonamiento viven en mensajes directos y hilos privados.
- Cuando hay que decidir qué asume un agente y dónde debe revisar una persona, en lugar de intentar automatizar un flujo de principio a fin.
- Cuando una flota de agentes especializados desorienta a quien tiene como modelo mental un único chatbot.
- Cuando la adopción se ha estancado y el despliegue avanza por mandato en vez de por ejemplos visibles de compañeros.
- Cuando la dirección pide pruebas del valor de la IA y las únicas cifras disponibles son métricas de uso.

## Puntos clave
- **La conversación solo se convierte en conocimiento si algo la lee.** DeLanghe recuerda que la investigación temprana en Slack mostró lo contrario de la promesa: la conversación en gran medida no se convertía en conocimiento y la gente seguía repitiéndose. Digerir ese volumen nunca fue humanamente posible; ahora es trabajo de un agente.
- **Pide el razonamiento, no solo el registro.** En vez de recuperar qué se decidió, pide a un agente que reconstruya por qué se decidió y cómo ha cambiado el contexto desde entonces.
- **Amplía la superficie.** Cuanto más conectes reuniones, correo, calendario y repositorios documentales, menos se repite el equipo.
- **El ritmo central es un ciclo de relevos.** Los agentes hacen el trabajo de producción —redactar, resumir, monitorizar, preparar— y pasan el resultado a una persona, que revisa, decide y reorienta antes de devolverlo. El lunes de DeLanghe empieza con un informe diario construido por un agente, más un resumen de los talleres de la semana anterior con escalaciones señaladas, un informe sobre novedades de IA, preparación de las reuniones del día y una biografía reescrita a la espera de revisión.
- **Ancla el bucle en un canal compartido**, donde personas y agentes clasifican juntos y las personas lideran la priorización. Las señales ligeras deben ser accionables: en su canal, una reacción con emoji añade un elemento y un agente lo recoge.
- **Trata a los agentes como compañeros con un papel.** Objetivos y áreas de foco claros funcionan mejor que un asistente genérico que nadie sabe describir. Su prueba: si el valor de un agente se siente impuesto en lugar de percibirse con claridad, es señal de retirarlo.
- **Público por defecto; privado a propósito.** Un canal privado es un punto ciego para todo agente que deba informar sobre él. Una vez apartado el material genuinamente sensible, lo que empuja el trabajo a los mensajes directos suele ser la incomodidad de ser visto a medio proceso, no el secreto: la palanca real es la seguridad psicológica, no la política.
- **La adopción se propaga por demostración.** Un canal de toda la empresa para compartir trucos hace que una técnica de una función acabe rediseñando otra. Dentro de Slack, el impulso para que los product managers usaran Claude fue en gran medida autoorganizado: un PM escribió qué hizo y cómo lo hizo, y otros copiaron el formato.
- **Mide resultados, no actividad.** El consumo de tokens indica que las luces están encendidas. No indica que el trabajo haya mejorado, y ningún panel cerrará esa brecha por ti.
- **El consejo es cambiar el trabajo, no acelerarlo.** Empieza pronto pero pequeño: pon a un grupo de personas en un canal compartido con un agente, dales los mismos recursos y deja que lo que construyan se difunda solo.

## Recursos incluidos
- `skills/human-agent-team-practices/SKILL.md` — cómo montar y operar un equipo de personas y agentes.
- `skills/human-agent-team-practices/references/practice-areas.md` — las seis áreas de práctica con sus recomendaciones.
- `skills/human-agent-team-practices/examples/weekly-handoff-loop.md` — el ciclo de relevos desarrollado como ejemplo.
- `skills/human-agent-team-practices/templates/show-and-tell-writeup.md` — plantilla de «qué hice y cómo» para difundir la adopción.
- `guides/human-agent-team-operating-model.{en,ko,es,ja}.md` — el mismo material como guía en cuatro idiomas.

## Fuente
- https://claude.com/blog/turning-conversation-into-knowledge-how-slack-builds-human-agent-teams (19 de agosto de 2026)
