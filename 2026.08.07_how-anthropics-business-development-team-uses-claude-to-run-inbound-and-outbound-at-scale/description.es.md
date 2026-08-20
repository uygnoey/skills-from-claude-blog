[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un relato en primera persona de John Albert, representante de desarrollo de negocio (BDR) en Anthropic, sobre cómo su equipo lleva el inbound y el outbound a través de Claude Cowork. Antes dedicaba unas cinco horas al día a responder manualmente la bandeja de ventas — muchas veces las mismas preguntas — además de gestionar su propia cartera de cuentas. Ese trabajo ahora corre como skills y tareas programadas, con borradores que él revisa y personaliza antes de enviar.

El post recorre los flujos concretos: una skill de bandeja que corre cada hora, construida sobre una base de conocimiento de ventas y un perfil de voz por representante; monitores ligeros para ausencias a reuniones y leads nuevos; un escáner de pipeline que propone cambios de etapa en el CRM con la evidencia detrás; un barrido de prospección nocturno sobre más de cien cuentas que cada mañana devuelve un resumen, una puntuación y una jugada de outbound; un coach de llamadas que puntúa las llamadas de descubrimiento contra el playbook del equipo; y análisis ad-hoc para peticiones puntuales de los ejecutivos de cuenta. Cierra con seis consejos para empezar.

## ¿Cuándo es útil?
- Cuando una bandeja repetitiva consume horas al día y las respuestas ya existen en algún sitio.
- Cuando la cobertura de outbound está limitada por cuánta investigación manual cabe en una persona con una cartera grande.
- Cuando la higiene del CRM depende de que los representantes recuerden actualizar etapas que la evidencia en el correo y las grabaciones ya implica.
- Cuando se quiere que el trabajo programado del agente produzca borradores revisables en lugar de envíos autónomos.
- Cuando un equipo quiere compartir flujos entre representantes con carteras y rutinas distintas.

## Puntos clave
- **Construye la base de conocimiento antes que los flujos.** Un único documento con las preguntas que el equipo responde una y otra vez, junto a las mejores respuestas, es el cimiento del inbound. Claude creó la primera versión a partir de las fuentes existentes y ahora señala la información que podría estar desactualizada para que una persona la valide.
- **La skill de bandeja es deliberadamente delgada.** Es un system prompt breve, la base de conocimiento como fuente de los hechos de producto y un perfil del estilo de escritura del representante — perfil que a su vez produce una skill de voz que lee documentos, mensajes y correos que esa persona ha escrito. Corre cada hora, encuentra los hilos que necesitan respuesta y deja borradores.
- **Monitores ligeros cubren los huecos.** Una skill vigila Gmail y Google Calendar para avisar de ausencias y prospectos que dejan de responder; otra revisa el CRM en busca de leads nuevos y redacta un primer contacto personalizado a lo largo del día.
- **Las actualizaciones de pipeline llegan como propuestas con evidencia.** Una skill lee la guía interna sobre etapas de oportunidad y la contrasta con lo que de verdad ocurre en el correo y las grabaciones; después propone cada cambio en el CRM con su evidencia y espera aprobación. Las ediciones y los rechazos se registran con su motivo, para no repetir el error.
- **La prospección corre de noche sobre toda la cartera.** Una skill programada observa el estado actual de cada cuenta — con quién hay contacto, cómo usan el producto, qué señales importan — conectándose al CRM, a herramientas de ventas, a las grabaciones de llamadas y al almacén de datos, y valida los hallazgos contra la guía de outbound y los criterios de ICP que el equipo ha curado. Por la mañana el representante abre un resumen, una puntuación y una jugada por cuenta.
- **Un pequeño archivo de memoria y un registro evitan el trabajo duplicado,** y la retroalimentación de los representantes vuelve a la skill.
- **Las llamadas de descubrimiento reciben una tarjeta de puntuación.** Las transcripciones se evalúan contra el playbook: las tres mejores cosas hechas, las tres áreas a mejorar, un aprobado/suspenso explícito frente a los criterios y una única cosa de mayor impacto para practicar a continuación.
- **No todo necesita una skill.** Las peticiones puntuales — un análisis de gasto de una cuenta grande, un barrido de cuentas que usan el producto sin oportunidad asociada, encontrar invitados a un webinar puntuados contra el ICP — muchas veces están a un prompt de distancia.
- **Mantén a una persona en cada envío.** Claude genera borradores; los representantes los leen, editan y envían.
- **Comparte skills, pero mantenlas generales.** El equipo promueve sus skills más usadas a un plugin compartido una vez confirma que se usan a diario, y las mantiene lo bastante generales para adaptarse a distintas carteras y rutinas en vez de ceñirlas a una persona.

## Recursos incluidos
- `skills/inbound-reply-drafting/SKILL.md` — la skill horaria de bandeja, su base de conocimiento y el perfil de voz detrás.
- `skills/account-prospecting-sweep/SKILL.md` — el barrido nocturno de prospección y las peticiones de análisis ad-hoc a su alrededor.
- `skills/pipeline-hygiene-proposals/SKILL.md` — propuestas de etapa en el CRM con evidencia, a la espera de aprobación.
- `skills/discovery-call-scorecard/SKILL.md` — puntuar llamadas de descubrimiento contra un playbook.
- `guides/business-development-with-cowork.{en,ko,es,ja}.md` — el modelo operativo completo y los consejos para empezar, en cuatro idiomas.

## Fuente
- https://claude.com/blog/how-anthropics-business-development-team-uses-claude-to-run-inbound-and-outbound-at-scale (7 de agosto de 2026)
