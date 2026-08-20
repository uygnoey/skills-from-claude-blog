[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un caso de cliente sobre monday.com — una plataforma de gestión del trabajo que usan más de 250.000 empresas — que se reconstruyó a sí misma: dejó de ser una herramienta que la gente tiene que actualizar para convertirse en un producto agent-first donde personas y agentes trabajan sobre los mismos elementos. La experiencia reconstruida se lanzó en mayo de 2026 y alcanzó 5 millones de interacciones con agentes en dos meses.

El post empieza por lo que no funcionó. Durante un "AI month" en mayo de 2025, monday incrustó funciones de IA en los flujos existentes: resumir texto, categorizar información. La adopción fue real, pero el patrón no arraigó. La VP de Producto Orly Stern Izhaki llama a esa etapa construir "AI dust" — espolvorear automatizaciones sobre flujos que por lo demás seguían igual — y la conclusión fue que adoptar funciones de IA no equivale a convertirse en una empresa de IA. El director de Producto y Tecnología, Daniel Lereya, describe el giro hacia un producto agent-first como una de las decisiones más significativas de la compañía.

Lo que vino después fue una reconstrucción, no una suma: cuatro maneras de traer Claude a la plataforma, agentes con nombre y funciones definidas en IT, RR. HH., marketing y la oficina ejecutiva, y agentes tratados como compañeros de equipo a los que se les asigna trabajo mediante disparadores y menciones dentro del tablero, en vez de a través de una ventana de chat paralela.

## ¿Cuándo es útil?
- Cuando ya lanzaste funciones de IA, el primer mes pintaba bien y el uso se ha aplanado en resúmenes ocasionales.
- Cuando hay que decidir entre incrustar agentes en los flujos existentes o rediseñar el flujo alrededor de ellos.
- Cuando los agentes viven en una superficie de chat paralela al lugar donde está el trabajo y el contexto hay que pegarlo a mano.
- Cuando los pilotos de agentes se atascan antes de producción porque gobernanza, permisos y fiabilidad nunca se diseñaron desde el principio.
- Cuando necesitas describir trabajos concretos de agente por función en lugar de desplegar un único asistente general.

## Puntos clave
- **El "AI dust" es el modo de fallo.** Espolvorear automatizaciones sobre flujos existentes produce funciones que ayudan — resumir, categorizar — sin cambiar cómo se trabaja, y el uso no se acumula.
- **Cuatro vías de despliegue.** monday Agents creados con prompts usando Claude como modelo; bring-your-own-agent, incorporando Claude Managed Agents a la plataforma; agentes especializados prefabricados de la monday Agents Store, con plugins legales y financieros; e integración de Claude para código, donde los equipos conectan Claude en los paneles, asignan tareas y ejecutan en los entornos de cliente.
- **A los agentes se les da un trabajo con nombre, no un mandato general.** IT tiene un Intake & Triage Agent, un Knowledge Agent y un Incident Agent; RR. HH. cubre cribado de currículos, agenda de entrevistas, coordinación de contratación y gestión de feedback; marketing tiene inteligencia competitiva y battlecards; la oficina ejecutiva tiene un Operator Agent, un Org Health Agent y un Strategy Consultant Agent.
- **Diseño de compañero de equipo.** Cada agente tiene nombre, avatar y un sitio en el flujo. El trabajo se asigna con disparadores y menciones allí donde ya están los empleados, no en una interfaz de chat aparte.
- **La línea de producción corre sobre un solo elemento.** En el ejemplo de campaña, un marketer y un responsable de contenido dan forma al brief, un Strategist Agent lo estructura en objetivos, pilares de mensaje, canales y métricas, un Claude Managed Agent genera variantes de landing, un Brand Reviewer las contrasta con las guías de marca y señala problemas, y una persona aprueba antes de publicar.
- **Cooke Seafood, el cliente del cliente.** La mayor empresa pesquera familiar del mundo gestiona la entrega de proyectos y los recursos de unos 200 proyectos activos y propuestos, 130 contratos, y reportes automatizados que elevan riesgos a los registros RAID. La directora de Estrategia, Patti Stevens, resume el cambio como pasar de una plataforma que había que actualizar a una desde la que operan.
- **Cinco lecciones.** Mover los modelos mentales costó más que la tecnología; equipos pequeños con propiedad clara mantuvieron la alineación mientras dirección, UX, precio, modelos de confianza y definiciones de calidad se movían a la vez; la adopción dependió de la infraestructura de confianza — gobernanza, permisos, transparencia, fiabilidad; la capacidad de los agentes dependió de la inversión en backend, incluida monday DB, para anclarlos a datos vivos de proyecto a escala empresarial; y la transformación extendió una identidad existente en lugar de sustituirla.

## Recursos incluidos
- `skills/agent-first-product-transformation/SKILL.md` — pasar de funciones de IA a un producto agent-first.
- `skills/agent-first-product-transformation/references/deployment-models.md` — las cuatro vías para traer agentes a la plataforma y cuándo encaja cada una.
- `skills/agent-first-product-transformation/references/agent-job-map.md` — los trabajos de agente con nombre, por función.
- `skills/agent-first-product-transformation/references/transformation-lessons.md` — las cinco lecciones y lo que cada una implica para un plan.
- `skills/agent-first-product-transformation/examples/campaign-production-line.md` — el ejemplo de marketing de extremo a extremo y el despliegue en Cooke.
- `agents/*.md` — cinco subagentes destilados de los roles con nombre del post.
- `guides/agent-first-platform-rollout.{en,ko,es,ja}.md` — secuenciar un despliegue desde funciones de IA hasta agent-first.

## Fuente
[How monday.com transformed its platform into an agent-first product where humans and agents collaborate](https://claude.com/blog/how-monday-com-transformed-its-platform-into-an-agent-first-product-where-humans-and-agents-collaborate) — publicado el 2026-08-20.
