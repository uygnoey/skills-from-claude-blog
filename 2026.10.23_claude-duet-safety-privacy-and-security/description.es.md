[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
La explicación de Anthropic, del 23 de octubre de 2026, sobre cómo se protege Claude Duet, un agente en
vista previa de investigación que funciona de forma continua en un ordenador en la nube y usa las apps que
conecta el usuario. Se organiza en tres principios: tratar la información con discreción, mantener el
control en manos del usuario y mantener las credenciales lejos del agente.

## ¿Cuándo es útil?
- Al diseñar o auditar un agente que envía mensajes, paga, borra o inicia sesión en nombre del usuario.
- Al preparar un plan de evaluación y red team que cubra la inyección de prompts y la extralimitación.
- Al explicar cómo un agente delegado mantiene contraseñas y tokens fuera del modelo.

## Puntos clave
- Las acciones sensibles muestran acción, destino y contenido y esperan aprobación. Una comprobación de
  intención fuera del modelo (ampliada del clasificador del modo automático de Claude Code) resiste las
  instrucciones ocultas. Algunas acciones están prohibidas incluso con aprobación (operar con valores,
  mover dinero entre cuentas, acceder a la cuenta de otra persona). Las compras usan una tarjeta de un
  solo uso de Link (Stripe).
- Un clasificador revisa los mensajes salientes: nunca se comparten credenciales, números completos de
  tarjeta o cuenta ni documentos de identidad; otros datos privados requieren consentimiento (la petición
  del usuario cuenta). Los mensajes bloqueados pueden reescribirse para su aprobación.
- Una lista de tareas da visibilidad y permite reorientar; historial y memoria se conservan hasta
  borrarlos o restablecerlos.
- Las contraseñas pasan por un formulario de la app, cifradas con clave de un solo uso y escritas por la
  máquina del navegador; los tokens son marcadores que rellena un proxy externo; el navegador corre en su
  propia VM con comandos fijos. El agente usa un User-Agent propio e IP publicadas.
- Pruebas: variantes inocente / inyectada / de extralimitación, equipos rojos, modelo de amenazas de todo
  el sistema, prueba de penetración externa y recompensas por errores en HackerOne.

## Recursos incluidos
- Skill: `delegated-agent-safeguards` (`references/information-sharing-tiers.md`,
  `references/credential-and-browser-isolation.md`, `templates/approval-request.md`,
  `examples/evaluation-plan.md`).
- Guía: `guides/delegated-agent-security-architecture` (4 idiomas).

## Fuente
- https://claude.com/resources/articles/claude-duet-safety-privacy-and-security
