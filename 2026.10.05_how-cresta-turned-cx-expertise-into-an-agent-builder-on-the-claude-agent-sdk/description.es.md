[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un caso de cliente sobre Cresta, empresa de IA para experiencia del cliente (CX), y Conductor: un
constructor de agentes en lenguaje natural para crear agentes de CX listos para producción, basado
en Claude Agent SDK. El usuario describe lo que quiere y Conductor lo guía por plano, implementación,
evaluación y optimización.

## ¿Cuándo es útil?
- Cuando un equipo con experiencia de dominio quiere convertirla en un producto que construya agentes.
- Cuando hay que decidir qué construir internamente y qué delegar en Claude Agent SDK.
- Cuando se monta un ciclo de evaluación que detecte mejoras y regresiones al cambiar de modelo.

## Puntos clave
- Claude Agent SDK es el arnés de ejecución de propósito general (reunir contexto, llamar
  herramientas, escribir y ejecutar código); encima van los flujos, herramientas y contexto de CX de
  Cresta. Lo evaluaron por privacidad de datos, arquitectura multiinquilino, distribución de claves a
  nivel de organización, controles y observabilidad.
- Las conversaciones históricas muestran dónde debe intervenir una persona y dónde puede adaptarse
  el modelo. Los flujos críticos, sobre todo en sectores regulados, se fijan con reglas explícitas que
  se prueban y revisan.
- Las tareas de construcción (crear un agente, escribir un caso de prueba, modificar un agente,
  análisis de causa raíz) se puntúan por resultado, ruta de ejecución, calidad frente a una referencia
  curada y uso de recursos, y se repiten con cada nuevo modelo o cambio del framework.
- En su uso inicial, el tiempo de despliegue inicial se redujo aproximadamente a la mitad. Los
  patrones probados se comparten como skills.
- Lecciones: usarlo internamente hasta igualar a un ingeniero experto; invertir solo en ventajas
  únicas; decidir qué debe ser determinista; la construcción inicial es ~20 % del esfuerzo y la
  iteración ~80 %.

## Recursos incluidos
- Skill: `domain-agent-builder` — plan para construir un constructor de agentes de dominio sobre
  Claude Agent SDK, con una plantilla de evaluación de tareas de construcción.

## Fuente
- https://claude.com/resources/articles/how-cresta-turned-cx-expertise-into-an-agent-builder-on-the-claude-agent-sdk
