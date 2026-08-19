[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Es el relato en primera persona de un ingeniero del equipo de Integración Continua de Anthropic sobre el agente de guardia que construyó su equipo. Durante varios meses, Claude Tag ha actuado como primer respondedor ante fallos de CI/CD en Anthropic: redactó el informe de situación inicial en todos los incidentes recientes que tuvieron uno, publicando su primer análisis normalmente en unos 15 minutos.

El post recorre primero el montaje y después cada etapa del ciclo de vida del incidente —detección, triaje, resolución y verificación/traspaso— explicando qué hace el agente en cada punto y qué sigue siendo humano.

## ¿Cuándo es útil?
- Cuando la rotación de guardia se llena de clasificación de alertas e interrupciones fuera de horario en lugar de trabajo duradero de fiabilidad.
- Cuando se quiere un primer respondedor que abra cada incidente con una hipótesis fundamentada en evidencia en vez de un canal vacío.
- Cuando el conocimiento sobre incidentes vive en la cabeza de las personas y debe convertirse en instrucciones revisables y versionadas.
- Cuando la codificación agéntica ha elevado el volumen de merges y el proceso de CI debe escalar con él.

## Puntos clave
- **El agente vive donde ya vive la guardia.** Claude Tag mantiene memoria en el canal de Slack de guardia, observa canales adyacentes para obtener contexto (alertas de servicio, cambios de configuración, actualizaciones de PR) y acepta dirección turno a turno durante un incidente. Las rutinas se programan en lenguaje natural en ese mismo canal.
- **El acceso lo concede una sola vez un administrador**, mediante una cuenta de servicio conectada a las herramientas del equipo (por ejemplo Datadog o Grafana) a través de conectores MCP.
- **Las instrucciones permanentes son archivos markdown guardados como skills en un repositorio de GitHub**, de modo que varias personas del equipo pueden iterarlas y los cambios se gestionan como código.
- **Las alertas siguen siendo deterministas; el escalado tiene rutas deterministas y agénticas.** Un archivo raíz de instrucciones recoge los criterios para avisar o posponer, y se usa a Claude para afinar reglas ruidosas o demasiado estrechas desde los primeros días de un servicio nuevo.
- **El triaje se ejecuta como un flujo de trabajo dinámico**: un agente de orquestación levanta subagentes ejecutores que investigan en paralelo cada dependencia y fuente de verdad, y devuelven un informe de situación sintetizado. La mediana del primer análisis con evidencia fue de unos 14 minutos tras abrirse el incidente; en el caso más rápido se nombró la causa raíz en unos 4.
- **La investigación está guiada, no a ciegas.** Una skill de investigación por clase de fallo codifica los pasos que da una persona; un ejemplo llega a 617 líneas y se construyó depurando turno a turno durante un incidente real.
- **Un registro continuo de lecciones es la memoria.** Tras cada incidente, Claude añade qué pasó, la causa raíz, el arreglo y el detalle que conviene recordar, y lo lee al comenzar cada nueva investigación. Los patrones recurrentes se promueven a la skill de investigación.
- **La resolución está acotada por permisos.** El despliegue progresivo tras feature flags lo maneja un agente aparte que corre con los permisos del ingeniero; por lo demás, el agente de guardia propone PRs, pasos de mitigación o acciones sobre el clúster para que un humano los apruebe.
- **La comunicación es un agente aparte.** `ci-weather` reúne canales de incidentes, métricas de build, estadísticas de la cola de merge y retraso de despliegue en un informe estilo redacción publicado en un canal público. El equipo iteró el formato varias veces: la legibilidad es gusto propio del equipo, no fontanería.
- **Las barreras se mantuvieron mientras crecía el volumen.** Los ingenieros entregan aproximadamente 8 veces más código por trimestre que entre 2021 y 2025, y cada PR sigue teniendo una persona propietaria nombrada, requiere aprobación para fusionarse y pasa las mismas puertas de CI.

## Recursos incluidos
- `skills/oncall-first-responder/SKILL.md` — cómo montar y operar un primer respondedor de guardia agéntico.
- `skills/oncall-first-responder/templates/oncall.md` — archivo raíz de instrucciones permanentes (enrutamiento, criterios de aviso, políticas).
- `skills/oncall-first-responder/templates/lessons.md` — el registro continuo de lecciones que el agente lee y amplía.
- `skills/oncall-first-responder/templates/investigation-skill.md` — esqueleto de una skill de investigación por clase de fallo.
- `skills/oncall-first-responder/templates/sitrep.md` — formato del informe de situación.
- `skills/oncall-first-responder/references/incident-lifecycle.md` — qué hace el agente en cada etapa y qué sigue siendo humano.
- `skills/oncall-first-responder/examples/scheduling-routines.md` — las peticiones de rutina en lenguaje natural y los pasos de configuración descritos en el post.
- `agents/incident-orchestrator.md`, `agents/incident-executor.md`, `agents/ci-weather.md` — los tres roles de agente nombrados en el post.
- `guides/agentic-ci-on-call.{en,ko,es,ja}.md` — la guía completa de metodología en cuatro idiomas.

## Fuente
- https://claude.com/blog/ai-ci-cd-on-call
