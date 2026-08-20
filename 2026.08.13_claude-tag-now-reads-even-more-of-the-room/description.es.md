[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un anuncio de actualización de Claude Tag, la integración con Slack, sobre **cuándo decide colaborar proactivamente con un equipo**. Antes evaluaba un mensaje cada vez. Ahora usa el contexto de todo el canal, junto con su memoria y las instrucciones permanentes que se le han dado, para decidir cuándo intervenir — lo que el anuncio cifra en aproximadamente un 30% mejor a la hora de juzgar cuándo responder proactivamente y cuándo no.

La actualización también detalla las cuatro opciones que Claude toma ante cualquier mensaje, los mecanismos que le permiten no intervenir, y que el contexto adicional que ahora mantiene no cuenta para los límites de uso ni de gasto.

## ¿Cuándo es útil?
- Cuando un agente residente en Slack interviene demasiado, o demasiado poco, y hay que decidir qué control usar.
- Cuando se redactan instrucciones permanentes para un canal y se quiere saber qué palancas mueven realmente.
- Cuando alguien pregunta qué efecto tiene la ventana de contexto más amplia sobre la factura.
- Cuando un hilo parece sin responder y no está claro si el agente lo ha recogido.

## Puntos clave
- **El contexto de todo el canal sustituye a la evaluación mensaje a mensaje.** Claude ahora juzga a partir del contexto del canal más su memoria y las instrucciones permanentes.
- **Aproximadamente un 30% mejor** determinando cuándo responder proactivamente y cuándo no.
- **Cuatro opciones ante cualquier mensaje:** responder en línea para respuestas breves y verificables; iniciar trabajo más profundo en un hilo para asuntos complejos; enrutar el mensaje a un flujo de trabajo existente; o permanecer en silencio.
- **El silencio es un modo real**, evaluado igual que los demás — no es un fallo de respuesta.
- **Saber cuándo no intervenir** proviene de cuatro mecanismos: rúbricas específicas por canal que ponderan utilidad y confianza; menor atención a los canales inactivos hasta que se menciona a Claude; controles de usuario para desactivar las respuestas automáticas; e instrucciones en lenguaje natural para personalizar el comportamiento.
- **Sin coste adicional hoy.** Mantener más contexto sí incrementa el uso de Claude Tag, pero el contexto adicional que retiene no cuenta para los límites de uso ni de gasto.
- **Acuse de recibo más rápido.** Claude confirma los mensajes en segundos en lugar de operar en silencio durante el arranque.
- **Disponibilidad:** activo para clientes de Claude Teams y Enterprise.

## Recursos incluidos
- `skills/channel-proactivity-tuning/SKILL.md` — elegir el modo de respuesta adecuado, redactar instrucciones permanentes y usar los controles de contención cuando el agente interviene en exceso.
- `skills/channel-proactivity-tuning/references/response-modes.md` — los cuatro modos y cómo elegir entre ellos por canal.
- `skills/channel-proactivity-tuning/references/suppression-controls.md` — los cuatro mecanismos de contención, del más acotado al más amplio.
- `skills/channel-proactivity-tuning/templates/standing-instructions.md` — plantilla de instrucciones en lenguaje natural por canal.

## Fuente
- https://claude.com/blog/claude-tag-now-reads-even-more-of-the-room
