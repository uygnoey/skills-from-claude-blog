[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Jason Clinton, Deputy CISO de Anthropic, describe el marco de riesgo que su equipo desarrolló para aprobar despliegues de IA agéntica. El argumento: en la era agéntica, el trabajo de un CISO no es alcanzar riesgo cero, sino hacer que el riesgo agéntico sea **legible y acotado**, de modo que pueda aceptarse deliberadamente por quien tiene autoridad para aceptarlo. Decir "no" produce adopción en la sombra, sin telemetría y sin interruptor de apagado; decir "sí" sin controles produce el primer incidente serio con un agente, que hace retroceder todo el programa de IA.

El post ofrece cuatro preguntas que hacer a cualquier caso de uso agéntico, sitúa cada despliegue en un espectro de identidad que va de la cuenta de servicio del sistema a la credencial humana, y enuncia siete controles que cualquier entorno de agentes debería poder cumplir. Dos casos de estudio lo sostienen: un agente interno de respuesta a incidentes que es una cuenta de servicio acotada, y un arnés de agente personal donde las cuatro preguntas dan una respuesta distinta para cada caso de uso, de modo que son los controles —y no un veredicto único— los que acotan el riesgo.

## ¿Cuándo es útil?
- Cuando un equipo pide conectar un agente a sistemas internos y el proceso de revisión de seguridad todavía no tiene un marco para ello.
- Cuando se redacta o revisa un proceso de aprobación de agentes y hacen falta las preguntas que producen *condiciones* de aprobación en lugar de un sí o un no.
- Cuando hay que decidir qué controles exigir a un proveedor de agentes: los siete requisitos están escritos para llevárselos a tu IdP, a tu SIEM y a cualquier proveedor al que ya pagas.
- Cuando la responsabilidad por las acciones de un agente es difusa porque lleva la identidad delegada de una persona a sistemas que esa persona no está mirando.
- Cuando se señala a la gobernanza como el cuello de botella y hace falta el patrón en el que los equipos de GRC operan sus propios agentes.
- Cuando se diseña un programa que debe seguir en pie frente a un modelo más capaz dentro de seis meses.

## Puntos clave
- **Las cuatro preguntas.** ¿Qué contenido no confiable ingiere? ¿Qué acciones puede tomar y en nombre de quién? ¿Cuál es el radio de impacto si se desalinea? ¿Qué observabilidad tengo? Si no entra nada no confiable, el riesgo específico del agente es casi cero: avanza rápido.
- **El principio de mínima agencia.** Las cuatro respuestas dan la imagen; la mínima agencia dice qué hacer con ella: otorgar la capacidad más estrecha que aún complete la tarea. Postura por defecto: despliegue marcado por el administrador — grupo pequeño, observar telemetría, ampliar.
- **Un agente desalineado es una amenaza interna, no un problema perimetral.** El informe 2026 de Ponemon sitúa la contención media de un incidente interno en 67 días; a velocidad de agentes esa es la unidad de medida equivocada.
- **El medio ambiguo del espectro de identidad es la parte peligrosa.** Un agente que lleva identidad delegada a sistemas no vigilados vuelve ambigua la responsabilidad, y "la responsabilidad ambigua es cómo los incidentes se vuelven inexplicables".
- **Pueden aparecer capacidades sin ningún cambio de configuración.** Pasar el agente de respuesta a incidentes de Opus 4 a Opus 4.5 —sin herramientas, permisos ni prompts nuevos— bastó para que contactara a un agente escritor de código en mitad de un incidente para arreglar producción. Los controles aguantaron: el arreglo fue a un PR revisado por una persona. Limita accesos y acciones, no lo que crees que el modelo de hoy puede hacer.
- **Quita el verbo, no solo el conector.** "Si el modo de fallo que te quita el sueño es 'se borra la base de datos de producción', elimina el verbo delete del mundo del agente. Nunca intentará una acción que no esté en su lista de herramientas."
- **La lista de permitidos de salida es el control más fuerte contra la inyección de prompts.** Un agente comprometido todavía tiene que sacar los datos; si las peticiones salientes solo alcanzan dominios que elegiste, no hay destino bajo control del atacante.
- **El sandbox nunca debería contener una credencial que valga la pena robar.** Los tokens de conector se quedan fuera gracias a un proxy inverso que inyecta las credenciales reales. Más del 50% del código en los PR de Anthropic en julio de 2026 lo escriben agentes, y funciona con seguridad por las VM efímeras más la revisión humana antes de que algo aterrice.
- **La telemetría debe ser un flujo, no un panel** — OpenTelemetry hacia tu SIEM, con las acciones del agente distinguibles de las del usuario. Ojo: el contenido de los prompts va activado por defecto en la salida OTel de Cowork, y Cowork todavía no está en la Compliance API.
- **La gobernanza no tiene por qué ser el cuello de botella.** Automatiza el registro de riesgos, averigua quién construye agentes y por qué (la gente rodea a seguridad cuando el camino autorizado es lento) y mantén la aceptación humana del riesgo dentro del flujo de trabajo.
- **Diseña para el modelo de dentro de seis meses.** Los andamiajes elaborados de prompts se recortan en futuras aplicaciones internas; si tus controles viven ahí, pierdes el punto de control.

## Recursos incluidos
- `skills/agentic-risk-assessment/SKILL.md` — las cuatro preguntas, la mínima agencia, el espectro de identidad y los siete controles como procedimiento de revisión ejecutable.
- `skills/agentic-risk-assessment/references/four-questions.md` — definiciones completas y guía de evaluación para cada pregunta.
- `skills/agentic-risk-assessment/references/identity-spectrum.md` — cuenta de servicio frente a credencial humana, el medio ambiguo y el encuadre de riesgo interno.
- `skills/agentic-risk-assessment/references/deployment-controls.md` — los siete controles, cada uno como requisito y como implementación, con qué preguntar a un proveedor.
- `skills/agentic-risk-assessment/examples/incident-response-agent.md` — el caso de la cuenta de servicio acotada, incluida la comunicación emergente entre agentes tras una actualización de modelo.
- `skills/agentic-risk-assessment/examples/personal-agent-harness.md` — el caso de la credencial humana y la superficie de sistema en dos partes.
- `skills/agentic-risk-assessment/templates/risk-review.md` — ficha de revisión para un caso de uso agéntico.
- `skills/agentic-risk-assessment/templates/trust-boundary.md` — plantilla para escribir qué cuenta como contenido no confiable.
- `agents/incident-response-coordinator.md` — subagente para el rol de respuesta a incidentes, acotado a lecturas más documentos nuevos y mensajes de chat.
- `agents/vendor-change-reviewer.md` — subagente de GRC que marca respuestas de cuestionarios de proveedores y avisos de cambio de subprocesadores para decisión humana.
- `guides/ciso-agentic-ai-governance.{en,ko,es,ja}.md` — la guía completa en cuatro idiomas.

## Fuente
["Zero risk isn't the job: a CISO's guide to agentic AI"](https://claude.com/blog/ciso-guide-to-agentic-ai), por Jason Clinton, Deputy CISO de Anthropic — publicado el 17 de julio de 2026.
