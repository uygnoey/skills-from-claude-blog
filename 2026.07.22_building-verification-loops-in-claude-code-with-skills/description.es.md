[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Delba de Oliveira, del equipo de Claude Code, explica cómo convertir en skills las comprobaciones manuales que repites después de cada cambio, para que Claude cierre su propio bucle de retroalimentación. La mayoría de las sesiones de codificación agéntica siguen un bucle — reunir contexto, actuar, verificar los resultados, volver atrás si hace falta — y Claude ya verifica algunas cosas por su cuenta a partir de las señales deterministas de la base de código: comprobadores de tipos, linters, pruebas, errores en tiempo de ejecución. Todo lo que Claude no puede inferir se convierte en los pasos que das a mano, y esos son los pasos que merece la pena codificar.

El post recorre los bucles integrados que conviene probar primero, la forma mínima de un `SKILL.md` de verificación y las cuatro maneras de desplegar una comprobación — independiente, incrustada en la skill que produce el artefacto, encadenada tras otra skill, o ejecutada en cada PR — cada una con la situación que le corresponde, su coste y la señal de que se te ha quedado pequeña.

## ¿Cuándo es útil?
- Cuando haces la misma pequeña corrección cada vez que Claude implementa una funcionalidad.
- Cuando existe una regla específica del proyecto que ningún linter genérico detecta.
- Cuando empiezas un proyecto nuevo y necesitas dejar por escrito cómo debe comportarse.
- Cuando decides si una comprobación debe invocarse a mano, incrustarse, encadenarse o convertirse en una puerta de PR para todo el equipo.
- Cuando quieres añadir verificación a una skill que no puedes editar: integrada o gestionada por un plugin.
- Cuando un hábito personal está listo para convertirse en infraestructura de equipo.

## Puntos clave
- **Un bucle de verificación es un ciclo repetido en el que el agente comprueba su propio trabajo** — ejecutando pruebas, linters o comprobaciones personalizadas — y arregla lo que falla antes de seguir. Empaquetado como skill, cada sesión aplica las mismas comprobaciones sin depender de que alguien las recuerde.
- **Prueba primero lo integrado**: `/verify`, los códigos de error de la cadena de herramientas (enumera los comandos exactos de build y test en `CLAUDE.md`), Code Review en vista previa de investigación, GitHub Actions, la validación de especificaciones y las rúbricas de Claude Managed Agents, donde un agente evaluador independiente devuelve los fallos al bucle de retrabajo.
- **Escribe la comprobación en lenguaje llano, como se la entregarías a alguien en su primer día.** Si cuesta articularla, pide antes las buenas prácticas a Claude y edita: tus diferencias son justo lo que hay que capturar.
- **La comprobación no tiene por qué ser cualitativa.** "Rechaza cualquier migración que elimine una columna sin un paso de backfill" es determinista, específica del proyecto y ningún linter genérico la detectará.
- **La skill de verificación más simple son unas líneas de frontmatter más un cuerpo**: qué leer, qué confirmar, cómo informar y corregir. `skill-creator` te entrevistará si prefieres no escribirla a mano.
- **La independiente** se gana su sitio en comprobaciones transversales que no aplican siempre; el coste es acordarse de invocarla, y ejecutarla tras cada cambio es la señal para incrustarla o encadenarla.
- **La incrustada** es una línea añadida al cuerpo de la skill productora, pero solo funciona en skills que puedes editar: las integradas y las gestionadas por plugins se sobrescriben al actualizar.
- **La encadenada** convierte un hábito en un contrato: "siempre ejecuto `/verify` después de `/simplify`" pasa a ser "`/simplify` siempre ejecuta `/verify` al terminar". El equipo de Claude Code de Anthropic encadena `/code-review` → `/simplify` → `/verify` → `/design`. Cambia flexibilidad por automatización y puede aumentar el gasto de tokens.
- **En cada PR** es donde la verificación deja de ser infraestructura personal y pasa a ser infraestructura de equipo, pero conviene esperar mientras la cadena siga cambiando: cada ajuste se vuelve un evento visible para todos.

## Recursos incluidos
- `skills/verification-loop-builder/SKILL.md` — los bucles integrados, cómo escribir la comprobación, los cuatro patrones de despliegue y el proceso de creación en seis pasos.
- `skills/verification-loop-builder/templates/verification-skill.md` — la forma mínima de frontmatter más cuerpo, con guía campo a campo.
- `skills/verification-loop-builder/templates/wrapper-chain-skill.md` — el patrón envoltorio para encadenar sobre una skill que no puedes modificar.
- `skills/verification-loop-builder/examples/verify-log-hygiene.md` — la skill de higiene de logs del post, completa.
- `skills/verification-loop-builder/examples/scaffold-component-embedded.md` — la incrustación de una línea dentro de una skill de scaffolding de componentes.
- `skills/verification-loop-builder/references/built-in-loops.md` — los seis enfoques de verificación integrados en detalle.
- `skills/verification-loop-builder/references/deployment-patterns.md` — independiente, incrustada, encadenada y para todos los PR, con costes y señales de haberla superado.
- `guides/verification-loops.{en,ko,es,ja}.md` — el recorrido completo en cuatro idiomas.

## Fuente
[Building verification loops in Claude Code with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills) — Delba de Oliveira, 22 de julio de 2026.
