[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Tres historias de clientes que usan el **modo auto** de Claude Code como predeterminado diario en producción: **Nuro**, **Gusto** y **Garner Health**. El modo auto sustituye la aprobación comando a comando por un clasificador que evalúa cada acción y bloquea las potencialmente dañinas. El post lo plantea como la resolución del dilema entre velocidad y seguridad en la programación agéntica: revisar cada comando mantiene a una persona en el bucle, pero se convierte en el cuello de botella cuando las sesiones duran horas o se multiplican en paralelo, mientras que saltarse las comprobaciones de permisos por completo es la vía por la que se cuelan la inyección de prompts, la deriva de alcance y algún recurso de producción borrado.

En el conjunto del uso de Claude Code, Claude trabaja **9 veces más tiempo entre interrupciones** que con el predeterminado anterior.

## ¿Cuándo es útil?
- Al decidir si convertir el modo auto en el predeterminado de un equipo o de la empresa, cuando hacen falta patrones operativos concretos y no una descripción de la función.
- Al diseñar las barreras que rodean al modo auto: reglas de denegación, ajuste del clasificador, proxy de MCP, telemetría.
- Cuando se quiere saber dónde los profesionales salen deliberadamente del modo auto.
- Al construir agentes de larga duración o nocturnos, buscando qué formas de tarea funcionan realmente sin supervisión.

## Puntos clave
- **El modo auto opera dentro de las barreras, no en lugar de ellas.** Los ingenieros de Nuro deniegan de plano en su configuración los comandos más peligrosos, como los borrados recursivos, y el clasificador decide dentro de esos límites. Gusto enruta su tráfico MCP por una capa de proxy gobernada con guardas de herramientas e inspección de prompts, de modo que los agentes ya trabajan con permisos muy acotados antes de que el modo auto intervenga.
- **La ganancia es la duración sin supervisión, no la velocidad por paso.** Nuro ejecuta agentes de investigación nocturnos que mejoran de forma incremental las métricas de evaluación de su pila de conducción autónoma; un ingeniero lanzó un agente a las 22:00 y tenía tres PR por la mañana. El patrón se generaliza a cualquier tarea con una señal de evaluación clara contra la que iterar; otro equipo de Nuro lo usó para reducir la huella de memoria de un binario.
- **Las sesiones cortas también ganan.** Un ingeniero cloud de Gusto trabaja en ráfagas de veinte minutos —investigación de endpoints, auditorías de logs, gestión de conectores, ingesta de documentación a través de servidores MCP— y eligió el modo auto frente a bypass permissions por la protección contra inyección de prompts y la comprobación de intención, no por sesiones más largas.
- **El clasificador hace trabajo real.** Según el propio análisis de Gusto, cerca del 10% de las transcripciones de sesión desde mediados de mayo de 2026 incluye una denegación del modo auto. Un ingeniero ha lanzado 2.425 sesiones desde diciembre con el modo auto como herramienta diaria.
- **Aun así, se sale deliberadamente.** Kai, en Nuro, vuelve al modo interactivo cuando Claude Code revisa un pull request en su nombre. Chad, en Gusto, cambia a accept edits para Terraform, AWS y llamadas POST directas contra APIs en vivo: «al final, sigues siendo responsable de lo que pase».
- **El ajuste es mínimo pero concreto.** La única modificación de Garner Health coincide con la de Nuro: configurar el modo auto para que no apruebe acciones que comunican con otras personas, como enviar mensajes de Slack o correos.
- **El modo auto puede ser la condición previa de un SDLC estandarizado.** Garner Health desplegó Claude Code a sus 550 empleados, conectado a Salesforce, Zendesk y Snowflake, y ejecuta su ciclo de vida como un plugin de skills estandarizadas: explorar el contexto, commitear archivos de contexto al repositorio, hacer «investigación antagonista» para poner a prueba sus propias suposiciones y luego implementar, deteniéndose ante una persona solo cuando necesita contexto que no puede encontrar. Las fases más intensivas en investigación no eran posibles antes del modo auto.
- **La telemetría es el control habilitante.** El consejo de Garner para las empresas: construir primero los flujos de trabajo y la telemetría. «Si dijéramos: todos a construir vuestros propios flujos, y no tuviéramos telemetría, sería muy peligroso».

## Recursos incluidos
- `skills/auto-mode-production-practices/SKILL.md` — patrones operativos para usar el modo auto como predeterminado diario.
- `skills/auto-mode-production-practices/references/team-practices.md` — qué configuró cada uno de Nuro, Gusto y Garner Health, y por qué.
- `skills/auto-mode-production-practices/references/unattended-task-patterns.md` — qué formas de tarea funcionan de noche y cuáles no.
- `skills/auto-mode-production-practices/templates/team-auto-mode-policy.md` — plantilla de política de equipo con barreras, excepciones y telemetría.
- `guides/auto-mode-in-production-patterns.{en,ko,es,ja}.md` — los tres casos y sus patrones comunes, en cuatro idiomas.

## Fuente
- https://claude.com/blog/auto-mode-in-production
