[English](./agent-first-platform-rollout.en.md) · [한국어](./agent-first-platform-rollout.ko.md) · **Español** · [日本語](./agent-first-platform-rollout.ja.md)

# De funciones de IA a agent-first: cómo secuenciar el despliegue

Derivado del caso de monday.com del 20 de agosto de 2026: la reconstrucción de su plataforma de gestión del trabajo — usada por más de 250.000 empresas — en un producto donde personas y agentes colaboran sobre los mismos elementos. La experiencia reconstruida se lanzó en mayo de 2026 y alcanzó 5 millones de interacciones con agentes en dos meses.

## Empieza por la versión que falló

Lo más útil del caso es el intento que no funcionó. En mayo de 2025, durante un "AI month" interno, monday incrustó funciones de IA en los flujos existentes: resumir texto, categorizar información. Hubo adopción. El patrón no arraigó.

El nombre que le puso el equipo, de la VP de Producto Orly Stern Izhaki, es **"AI dust"**: automatizaciones espolvoreadas sobre flujos que por lo demás seguían iguales. La conclusión fue que adoptar funciones de IA no equivale a convertirse en una empresa de IA.

Merece la pena detenerse aquí porque este modo de fallo no se ve en las métricas de lanzamiento. Las funciones que resumen y categorizan ayudan de verdad. Simplemente no cambian cómo se hace el trabajo, así que el uso se estabiliza en una franja estrecha y deja de acumularse. El director de Producto y Tecnología, Daniel Lereya, describe el giro posterior hacia un producto agent-first como una de las decisiones más significativas de la compañía — una descripción justa de la decisión de reconstruir en lugar de añadir.

**Diagnóstico:** si tu producto funciona igual con la IA apagada, lo que añadiste es polvo. Nada del trabajo se ha movido.

## Fase 1 — Define qué significa "agent-first" para tu producto

Antes de construir nada, responde a la pregunta que señala la quinta lección: ¿qué significa ya tu producto para quien lo usa? La respuesta de monday fue que siempre había sido el sitio donde la gente hace equipo, y los agentes se incorporaron como miembros del equipo. La transformación extendió una identidad existente en vez de sustituirla.

Equivocarse aquí sale caro de una forma concreta: si los agentes obligan a aprender un modelo mental nuevo *y* a confiar en una nueva clase de actor a la vez, has duplicado el coste de adopción. La manera habitual de que ocurra sin querer es una superficie de chat aparte, con sus propios conceptos, junto al producto.

## Fase 2 — Reencuadra al equipo antes de reconstruir

La primera lección de monday es que los modelos mentales costaron más que la tecnología: llevar a los equipos de "mejorar el producto existente" a "reconstruir responsablemente para un futuro distinto" tomó más tiempo que la ingeniería.

Dos implicaciones para el plan:

- **Programa el reencuadre.** Un calendario con estimaciones de ingeniería y sin tiempo asignado a cambiar lo que el equipo cree que está construyendo se retrasará justo en la parte no programada.
- **Espera resistencia de tu mejor gente.** La experiencia en el producto actual es exactamente lo que el reencuadre les pide soltar.

## Fase 3 — Reestructura la propiedad para un periodo de cambio simultáneo

La segunda lección viene con una condición previa que conviene leer con atención: dirección, UX, tecnología, precio, modelos de confianza y definiciones de calidad se movían *a la vez*. En esas condiciones, equipos pequeños con propiedad clara y derechos de decisión rápidos mantuvieron mejor la alineación que las estructuras jerárquicas.

La regla general no es "la jerarquía es mala". Es que la jerarquía sufre cuando todos los insumos de una decisión siguen en movimiento, porque cada decisión tiene que subir y bajar mientras sus premisas cambian por debajo. Estructura según el número de variables inestables simultáneas, no según el tamaño del proyecto.

## Fase 4 — Define trabajos de agente, función por función

El modo de fallo al otro lado del polvo de IA es un único asistente general que nadie sabe describir. monday definió en su lugar trabajos con nombre:

- **IT** — un Intake & Triage Agent (clasificar, autorresolver, escalar), un Knowledge Agent (detectar huecos, redactar artículos), un Incident Agent (detectar incidentes, abrir salas de crisis).
- **RR. HH.** — cribado de currículos, agenda de entrevistas, coordinación de contratación, gestión de feedback.
- **Marketing** — inteligencia competitiva, battlecards.
- **Oficina ejecutiva** — un Operator Agent, un Org Health Agent, un Strategy Consultant Agent.

Leyéndolos en conjunto, se repiten cuatro propiedades que sirven como prueba. Antes de construir un agente deberías poder enunciar: su **disparador** (el momento en que se activa, no el botón que lo invoca), su **verbo acotado** (una descripción de puesto, no un dominio), su **entrega de vuelta** (lo que produce para que una persona u otro agente lo retome) y su **identidad** (nombre y avatar, para poder invocarlo dentro del flujo). Si no puedes nombrar el disparador o la entrega, lo que tienes es una funcionalidad.

## Fase 5 — Pon los agentes donde ya está el trabajo

Cada agente de monday tiene nombre, avatar y un sitio dentro del flujo. El trabajo se asigna con disparadores y menciones en el tablero donde los empleados ya operan, no a través de una interfaz de chat paralela.

Es una decisión de producto con consecuencia técnica. Un agente que vive donde vive el trabajo hereda su contexto — el elemento, su historial, sus responsables, su estado — en lugar de exigir que alguien lo pegue. Tres comprobaciones:

- ¿Puede una persona asignar trabajo sin salir del objeto en el que está?
- ¿El resultado vuelve a ese objeto, donde lo buscará la siguiente persona?
- ¿Se puede saber, mirando el objeto, qué pasos hizo un agente?

## Fase 6 — Haz correr una línea de producción sobre un solo objeto

El ejemplo de campaña concreta la forma. Sobre un único elemento del tablero: un marketer y un responsable de contenido dan forma al brief; un Strategist Agent lo estructura en objetivos, pilares de mensaje, canales y métricas; un Landing Page Builder — un Claude Managed Agent — genera variantes con copy adaptado; un Brand Reviewer contrasta con las guías y señala problemas; un responsable de marketing aprueba o refina antes de publicar.

El patrón generalizable: **intención humana → estructuración por agente → producción por agente → revisión por agente → aprobación humana.** Tres cosas lo sostienen. Un solo objeto lleva el estado, así que nadie pega contexto entre herramientas. La etapa de estructuración es lo que hace posible la de producción. Y productor y revisor son agentes distintos, porque un agente que aprueba su propia salida no es una revisión.

## Fase 7 — Lanza la infraestructura de confianza con la primera versión

La tercera lección de monday es rotunda: gobernanza, permisos, transparencia y fiabilidad determinaron si los agentes pasaban de piloto a producción. No la calidad del modelo.

Trata las cuatro como criterios de aceptación y no como trabajo de endurecimiento, porque un piloto que las omite demuestra bien y luego no convierte — y el fallo se malinterpreta como un problema de capacidad.

- **Gobernanza** — quién autoriza a un agente a actuar sobre qué objetos.
- **Permisos** — el acceso del agente acotado por el de la persona que asigna, no por su propia identidad de servicio.
- **Transparencia** — lo que hizo el agente, visible después sobre el objeto.
- **Fiabilidad** — comportamiento lo bastante predecible como para montar un proceso encima.

## Fase 8 — Financia la capa de datos

Cuarta lección: los agentes rindieron mucho mejor anclados en datos vivos de proyecto, historial de equipo y flujos estructurados, y monday invirtió en **monday DB** para sostener el volumen y la complejidad de los agentes a escala empresarial.

La calidad de los agentes está acotada por lo que la capa de datos puede servir: con qué frescura, con qué estructura, a qué latencia y concurrencia. Los agentes leen mucho más, y mucho más a menudo, que las personas. Una hoja de ruta de capacidades sin partida de infraestructura es un plan para estancarse donde lleguen tus patrones de consulta actuales.

## Cómo es el estado final

Cooke, presentada como la mayor empresa pesquera familiar del mundo, gestiona la entrega de proyectos y los recursos de unos 200 proyectos activos y propuestos, 130 contratos, y reportes automatizados que elevan riesgos a los registros RAID. La directora de Estrategia, Patti Stevens, resume el cambio como pasar de una plataforma que había que actualizar a una desde la que operan.

Esa distinción resume todo. Un sistema que *actualizas* es aquel donde el trabajo real ocurre en otro sitio y la herramienta guarda un registro — que es justo la condición en la que las funciones de IA se vuelven polvo, porque decoran el registro en vez de hacer el trabajo. Los tres despliegues de Cooke comparten una propiedad útil como heurística para elegir por dónde empezar: entrega de proyectos, estado de contratos y registros de riesgo son casos en los que el registro y el trabajo ya son el mismo objeto.

## Fuente
[How monday.com transformed its platform into an agent-first product where humans and agents collaborate](https://claude.com/blog/how-monday-com-transformed-its-platform-into-an-agent-first-product-where-humans-and-agents-collaborate) (publicado el 2026-08-20).
