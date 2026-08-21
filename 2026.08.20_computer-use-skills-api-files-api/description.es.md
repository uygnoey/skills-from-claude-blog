[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un anuncio de disponibilidad general: el uso de computadora, la Skills API y la Files API ya están disponibles de forma general en la Claude Platform, y el uso de computadora incorpora una nueva herramienta de uso de navegador para agentes que trabajan en aplicaciones web. El planteamiento es que, juntas, permiten construir agentes que operan software, aplican la experiencia de tu equipo y devuelven archivos terminados; la ejecución de código y la búsqueda web, ya disponibles de forma general, encajan en el mismo bucle.

El post explica para qué sirve cada pieza. El uso de computadora opera el software que el agente puede ver, a partir de una captura de pantalla, y eso es lo que le permite funcionar en aplicaciones que nunca se diseñaron para automatizarse. La herramienta de uso de navegador añade la estructura de la página, de modo que el agente actúa sobre un campo o botón concreto en lugar de sobre una posición en pantalla. Una skill es una carpeta de instrucciones, scripts y plantillas que se carga solo cuando la tarea lo requiere, se sube y versiona con la Skills API y se ejecuta en el entorno aislado de ejecución de código de Claude. La Files API almacena los documentos que un agente lee y escribe, referenciados por ID entre peticiones.

## ¿Cuándo es útil?
- Cuando un agente debe trabajar dentro de una aplicación o un portal que no expone API.
- Cuando hay que decidir entre el uso de computadora a nivel de píxeles y la herramienta de uso de navegador, consciente de la estructura, para una tarea web.
- Cuando el procedimiento del equipo sigue creciendo dentro de una cadena de prompt y debería convertirse en un artefacto versionado.
- Cuando un flujo multi-turno reenvía el mismo documento fuente en cada petición.
- Cuando el entregable es un archivo, no un párrafo de texto de respuesta.
- Cuando migras una integración beta existente y quieres saber qué cambió en la disponibilidad general.

## Puntos clave
- **Turnos multi-acción.** La herramienta actualizada de uso de computadora ejecuta varias acciones por turno en vez de una por llamada al modelo, así que las tareas terminan en menos llamadas y menos tiempo. La herramienta de uso de navegador usa los mismos turnos multi-acción y añade la estructura de la página.
- **El uso de computadora ya es apto para cargas de trabajo reguladas por HIPAA** bajo el BAA de Anthropic.
- **Skills API:** una API más sencilla para subir y versionar tus propias skills; se ejecutan en el entorno aislado de ejecución de código de Claude, así que no hay nada que alojar.
- **Files API:** expiración automática de archivos, límites de tasa 5 veces mayores y 1 TB de almacenamiento por organización.
- **El bucle compuesto.** El ejemplo trabajado es un agente de reclamaciones: lee el documento de ingreso desde la Files API, sigue una skill que codifica el procedimiento de presentación del equipo, completa el envío en el portal web de una aseguradora con la herramienta de uso de navegador y guarda la confirmación de vuelta como archivo.
- **Resultado reportado con la nueva herramienta de uso de computadora.** Para agentes que trabajan dentro de sistemas de salud y seguros sin API: el flujo de reclamaciones más largo pasó de 32 minutos a 13, el coste por tarea cayó cerca de un 30% en todos los flujos probados y la finalización llegó al 100%, sin cambios en los prompts.
- **La skill como superficie de personalización.** Box integró la creación especializada de documentos en Box Agent: una skill captura la metodología crediticia de un banco y su formato de memo aprobado, y Box Agent la aplica a documentos que ya están en Box para producir un memo de crédito con fundamento en las fuentes para revisión del analista, de modo que los bancos obtienen agentes para flujos complejos sin construir cada uno desde cero.
- **Disponibilidad.** La Skills API y la Files API también están en Microsoft Foundry; el uso de computadora actualizado y el uso de navegador llegarán pronto a Vertex AI de Google Cloud. Las integraciones beta existentes siguen funcionando mientras migras.

## Recursos incluidos
- `skills/software-operating-agent-stack/SKILL.md` — cómo componer las cuatro capacidades en un solo agente, con las reglas de selección.
- `skills/software-operating-agent-stack/references/capabilities.md` — cada capacidad tal como se anunció, incluido lo que cambió en la disponibilidad general.
- `skills/software-operating-agent-stack/references/availability.md` — disponibilidad por nube y un orden de migración desde la beta.
- `skills/software-operating-agent-stack/examples/workflow-shapes.md` — el agente de reclamaciones y la composición de Box, etapa por etapa.
- `guides/agent-capability-selection.{en,ko,es,ja}.md` — elegir entre las capacidades para un agente en producción.

## Fuente
[Build production agents with computer use, the Skills API, and the Files API](https://claude.com/blog/computer-use-skills-api-files-api) — publicado el 2026-08-20.
