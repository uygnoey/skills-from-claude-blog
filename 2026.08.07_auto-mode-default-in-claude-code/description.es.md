[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
El anuncio de que **el modo auto pasa a ser el modo de permisos predeterminado en Claude Code** para los planes Pro, Max y Team, a partir del 14 de agosto de 2026. En lugar de pedir al usuario que apruebe cada llamada a herramienta, el modo auto pasa cada llamada por un clasificador orientado a bloquear acciones irreversibles, destructivas o dirigidas fuera del entorno del usuario. Cuando el clasificador bloquea algo, Claude normalmente encuentra por su cuenta una vía más segura o pregunta directamente al usuario; si no puede avanzar —tres bloqueos seguidos, o veinte a lo largo de una sesión— Claude Code vuelve a las aprobaciones manuales.

El post publica además la evidencia de seguridad detrás del cambio: red-teaming interno, red-teaming externo con Apollo Research, una evaluación de inyección de prompts de Trajectory Labs, un estudio controlado con 1.053 evaluadores remunerados y el análisis de sesiones de producción marcadas por el sistema de seguridad. El coste en tokens del clasificador ya no se factura en los planes Pro, Max y Team. El modo auto sigue siendo opcional por ahora en Claude Enterprise, la Claude API, Claude Platform en AWS, Amazon Bedrock, Agent Platform de Google Cloud y Microsoft Foundry.

## ¿Cuándo es útil?
- Cuando hay que decidir si dejar el modo auto como predeterminado o fijar otro valor.
- Cuando un administrador necesita planificar el despliegue —o la exclusión deliberada— antes de que el cambio llegue a sus usuarios.
- Cuando se necesita la evidencia de seguridad (cifras, metodología y sus límites) para justificar el cambio internamente.
- Cuando hay que saber qué reglas de permisos siguen aplicándose en modo auto y cuáles quedan en suspenso.

## Puntos clave
- **La revisión manual se vuelve un hábito.** Los usuarios aprueban el 97% de los avisos de permiso y rechazan solo el 3%, frente al 39% de rechazo cuando Claude presenta un plan. En junio de 2026, el 49,5% de los usuarios activos de la CLI había escrito a mano una regla allow de Bash, el 62% había usado `bypassPermissions` o «no volver a preguntar» en Bash, y el 25% de las sesiones interactivas arrancaba en modo bypass permissions.
- **Estudio controlado.** Entre 1.053 evaluadores remunerados, las personas detectaron el 13,6% de los comandos peligrosos (143 de 1.053); el modo auto bloqueó el 89% (937 de 1.053). Cara a cara, el modo auto bloqueó 800 comandos que una persona aprobó, mientras que las personas bloquearon 6 que el modo auto permitió. La tasa humana caía con la duración de la sesión (~17% al principio, ~5% tras más de 50 avisos); la del modo auto se mantuvo plana.
- **Sesiones reales.** Entre las sesiones marcadas por seguridad (mayo–junio de 2026), el 6,3% de las aprobadas manualmente contenía una acción dañina de gravedad de producción (7+) que el usuario no había pedido explícitamente, frente al 2,4% de las sesiones en modo auto.
- **El red-teaming de Apollo Research** redujo la tasa de fallos del clasificador del 12% al 7%, y el endurecimiento generalizó a un conjunto de ataques reservado.
- **Inyección de prompts.** En la evaluación de Trajectory Labs (72 escenarios × 10 ejecuciones), ninguno de los 720 intentos tuvo éxito contra Fable 5, Opus 5 o Sonnet 5 en modo auto; el 5,83% tuvo éxito contra GPT-5.6 Sol en el modo Auto-review de Codex, y el 19,03% en Full Access.
- **Las reglas de permisos siguen aplicándose antes que el clasificador**, salvo las reglas allow lo bastante amplias como para conceder ejecución arbitraria de código (por ejemplo `Bash(python:*)`), que quedan en suspenso en modo auto. Los archivos de configuración no se modifican.
- **Endurecimientos recientes**: denegaciones duras para la exfiltración de datos (ampliables desde la configuración), reglas explícitas sobre secretos e información sensible junto con una comprobación de si el destino de un git push o un PR es público, privado o de confianza, inspección del git status antes de comandos git destructivos, y cribado de inyección de prompts en el lado de la API para contenido externo.
- **Resultados en producción**: entre quienes lo adoptaron en Teams y Enterprise, los usuarios de modo auto entregan alrededor de un 25% más de PR; Adobe, Nuro, Gusto y Garner Health lo usan como predeterminado en producción.
- **Controles**: `Shift+Tab` en la CLI o el desplegable de modo en la app de escritorio para cambiar; `defaultMode` en managed settings para fijar un predeterminado de organización; `disableAutoMode` para desactivarlo por completo.
- **Advertencia del propio post**: el modo auto depende de sistemas de clasificación y no elimina el riesgo. Para cambios de alto impacto en infraestructura de producción, conviene revisar las acciones de Claude en persona.

## Recursos incluidos
- `skills/auto-mode-adoption/SKILL.md` — decidir, configurar y desplegar un modo de permisos predeterminado.
- `skills/auto-mode-adoption/references/safety-evidence.md` — todas las cifras publicadas, su metodología y sus límites declarados.
- `skills/auto-mode-adoption/references/permission-model.md` — cómo encajan el clasificador, las reglas de permisos, los repliegues y los endurecimientos.
- `skills/auto-mode-adoption/templates/rollout-decision-record.md` — plantilla para registrar la decisión sobre el modo predeterminado.
- `guides/auto-mode-safety-and-rollout.{en,ko,es,ja}.md` — la guía completa del cambio y su evidencia en cuatro idiomas.

## Fuente
- https://claude.com/blog/auto-mode-default-in-claude-code
