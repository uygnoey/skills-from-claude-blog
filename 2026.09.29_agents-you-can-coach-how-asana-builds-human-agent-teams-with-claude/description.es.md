[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
El tercer post de la serie de Claude sobre equipos humano-agente. Arnab Bose, Chief Product Officer de
Asana, explica cómo Asana opera agentes de IA ("AI teammates") dentro de su modelo Work Graph®: agentes
con roles acotados, memoria compartida que solo personas designadas pueden confirmar y trabajo publicado
donde todos pueden verlo y entrenarlo, además de tres trabajos que Asana ha confiado a agentes
impulsados por Claude.

## ¿Cuándo es útil?
- Al incorporar agentes a los proyectos, tareas o canales de un equipo.
- Al definir el rol, las instrucciones, los permisos y la gobernanza de un agente.
- Al decidir quién puede entrenar a un agente y quién solo trabaja con él.
- Al convertir trabajo recurrente de síntesis (triaje de preguntas, resúmenes de estado, planificación
  de ciclos) en trabajo de agentes.

## Puntos clave
- Primero estructura el trabajo: lleva entradas no estructuradas a Claude, discútelas y registra lo
  accionable como proyectos y tareas que agentes y colegas puedan tomar.
- Cada agente tiene un rol, skills predefinidas, integraciones y una página de perfil (propósito,
  usuarios, administradores, instrucciones, skills, integraciones, permisos). El acceso se limita a
  proyectos, documentos y apps concretos, y a los permisos de quien invoca al agente.
- Cualquiera puede dar feedback de tarea; solo admins y editores pueden confirmar, deshacer o borrar la
  memoria compartida permanente. El equipo dueño del estándar (p. ej., la voz de marca) es dueño del
  agente.
- Los agentes publican su plan y sus pasos en tareas compartidas, así los revisores ven la petición y el
  ida y vuelta y pueden corregir tanto las instrucciones como el resultado.
- Trabajos: preguntas de producto desde Slack (responder, registrar vacíos de producto, avisar a
  enablement de preguntas repetidas); un resumen diario At-Risk Renewal en tres grupos, global y luego
  por región; planificación de ciclos de ingeniería en Command, con datos expuestos por el servidor MCP
  de Asana.

## Recursos incluidos
- Skill: `design-coachable-agent-teammates` — procedimiento de configuración con plantilla de perfil
  de agente, plantilla de resumen de renovaciones en riesgo y ejemplos de los tres trabajos de Asana.
- Guía: `coachable-human-agent-teams` (en/ko/es/ja) — las cuatro prácticas y los tres trabajos de un
  vistazo.

## Fuente
- https://claude.com/resources/articles/agents-you-can-coach-how-asana-builds-human-agent-teams-with-claude
