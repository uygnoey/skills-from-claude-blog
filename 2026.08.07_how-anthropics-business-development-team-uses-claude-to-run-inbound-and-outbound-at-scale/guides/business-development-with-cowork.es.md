[English](./business-development-with-cowork.en.md) · [한국어](./business-development-with-cowork.ko.md) · **Español** · [日本語](./business-development-with-cowork.ja.md)

# Llevar el inbound y el outbound con un espacio de trabajo con agentes

Derivado del relato en primera persona del 7 de agosto de 2026 de John Albert, representante de desarrollo de negocio (BDR) en Anthropic, sobre cómo su equipo lleva el inbound y el outbound a través de Claude Cowork.

## Adónde se iba el tiempo

Al principio de una carrera como BDR, los ejecutivos de cuenta entregan listas de cientos de cuentas: investigar cada empresa, encontrar a los contactos correctos, dar con los correos, redactar el acercamiento. El lado inbound era igual de manual. Tras entrar en Anthropic y hacerse cargo de la bandeja de ventas, Albert dedicaba unas cinco horas al día a responder a mano el interés entrante — a menudo las mismas preguntas — además de gestionar su propia cartera de cuentas.

Ese trabajo ahora corre como skills y tareas programadas. Los correos personalizados llegan como borradores que él revisa y adapta antes de enviar, y el outbound arranca desde una investigación que no tuvo que compilar durante horas.

## La arquitectura, en una línea

**Contexto curado + skills delgadas + una programación + una persona en cada envío.**

Cada pieza de lo que sigue es una instancia de eso.

## 1. Inbound: la base de conocimiento va primero

El cimiento es un único documento que reúne las preguntas que más llegan a la bandeja de ventas, con las mejores respuestas del equipo. Claude construyó la primera versión a partir de las fuentes existentes y ahora la verifica de forma continua, señalando la información que podría estar desactualizada para que una persona la valide.

Encima se apoya el flujo más pesado. La skill de bandeja corre **cada hora**: revisa la bandeja del representante, encuentra cada hilo que necesita respuesta y deja un borrador para leer, editar y enviar. Está hecha de tres partes delgadas — un system prompt breve, la base de conocimiento como fuente de los hechos de producto y un perfil del estilo de escritura del representante. Cada persona crea ese perfil de voz con una skill que lee documentos, mensajes y correos que ha escrito.

Dos skills más ligeras cubren los bordes administrativos: una vigila Gmail y Google Calendar para avisar de ausencias a reuniones y prospectos que dejan de responder, de modo que el seguimiento sea rápido; otra revisa el CRM en busca de leads nuevos y redacta un primer contacto personalizado, corriendo a lo largo del día para no dejar leads esperando.

## 2. Higiene del pipeline: propuestas con evidencia

Una skill mantiene Salesforce al día leyendo la guía interna del equipo sobre etapas de oportunidad y contrastándola con lo que de verdad ocurre en Gmail y Gong. Si el equipo se reunió con un cliente y la conversación pasó a preguntas de precio, la oportunidad probablemente deba avanzar de etapa.

Claude propone cada actualización **con la evidencia detrás** y espera aprobación. Cuando una propuesta se edita o se rechaza, se registra el motivo para no repetir el error.

## 3. Outbound: un barrido nocturno de toda la cartera

Albert trabaja más de cien cuentas a la vez. Una skill programada durante la noche prospecta toda la cartera y observa el estado actual de cada cuenta: con quién hay contacto, cómo usan el producto hoy, qué señales son relevantes. Para ello se conecta a Salesforce, a herramientas de ventas como Apollo y Common Room, a Gong y al almacén de datos, hace investigación profunda y valida el resultado contra la guía de outbound y los criterios de ICP que el equipo ha curado.

Por la mañana, el representante abre un resumen, una puntuación y una jugada de outbound por cuenta. Un pequeño archivo de memoria y un registro evitan el trabajo repetido o duplicado, y la retroalimentación del representante sobre los resultados vuelve a la skill — que es lo que hace el flujo más útil con el tiempo.

El beneficio aparece en la conversación: el acercamiento va a medida y el representante llega lo bastante informado sobre el negocio del cliente como para tener una discusión estratégica más profunda.

## 4. Coaching de llamadas: una tarjeta de puntuación por llamada de descubrimiento

Otra skill evalúa las transcripciones de Gong contra el playbook de llamadas de descubrimiento del equipo y construye una tarjeta por llamada, con retroalimentación específica de esa conversación: las tres mejores cosas hechas, las tres áreas a mejorar, un aprobado o suspenso explícito frente a los criterios y una única cosa de mayor impacto para practicar a continuación.

## 5. Peticiones puntuales: muchas veces basta un prompt

Las peticiones ad-hoc de los ejecutivos de cuenta permiten al equipo BDR colaborar de forma más estratégica, y la mayoría no necesita una skill:

- **Tendencias de uso de una cuenta grande** — a un prompt de distancia de un panel legible y descriptivo con las tendencias relevantes.
- **Uso no descubierto** — recorrer la cartera completa de un ejecutivo y encontrar señales de uso a nivel de cuenta donde todavía no existe una oportunidad de venta. Suele ser una buena señal para iniciar el contacto y trabajar con el cliente en optimizar su uso.
- **Difusión de eventos** — ante la petición de encontrar cuentas de la cartera de un ejecutivo para invitar a un próximo webinar, Claude revisó datos de uso e historial de CRM en toda la cartera, puntuó cada cuenta contra el ICP y señaló las mejores con los contactos que valía la pena invitar. No existía una skill para eso; bastó un prompt.

## Para empezar

Los consejos del propio post para equipos de desarrollo de negocio:

1. **Construye la base de conocimiento antes que los flujos.** Reúne las preguntas que tu equipo responde una y otra vez, con vuestras mejores respuestas, en un único documento de cara al exterior. No hace falta escribirlo a mano: apunta Claude a la documentación de producto y a los canales del equipo y que construya la primera versión.
2. **Dale a Claude ejemplos de cómo trabaja tu equipo.** Redacta contra el contexto que le des: mensajes que funcionaron, vuestro perfil de cliente ideal y el estilo de escritura de cada representante, para que los borradores suenen a quien los envía.
3. **Mantén a una persona en cada envío.** Claude genera borradores; los representantes los leen, editan y envían.
4. **Comparte las skills en el equipo.** Guarda las más usadas en un plugin compartido, promoviendo una skill allí una vez confirmas que se usa de forma constante en el día a día.
5. **Haz skills lo bastante generales para adaptarse.** Los segmentos, las carteras y los flujos difieren entre representantes, así que las skills compartidas se mantienen generales en vez de ceñirse a la rutina de una persona.
6. **Escribe la retroalimentación de vuelta en las skills.** Cuando descartes un aviso o corrijas un borrador, haz que Claude registre el motivo para no repetir el mismo error.

Y la nota final: simplemente empieza a experimentar. Cuanto más contexto y más herramientas le des, más se puede hacer.

## Fuente

https://claude.com/blog/how-anthropics-business-development-team-uses-claude-to-run-inbound-and-outbound-at-scale (7 de agosto de 2026)
