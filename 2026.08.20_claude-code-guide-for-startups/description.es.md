[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Anthropic entrevistó a más de una docena de startups de rápido crecimiento —Artemis Security, Cainex, Clay, ClickHouse, Cognition, Commure, Crosby, Emergent, Harvey, Heidi, Higgsfield, Omni, Parahelp, Translucent, Zingage— sobre cómo usan Claude Code para construir productos y escalar sus empresas, y destiló las respuestas en cinco reglas operativas. La pregunta que enmarca todo: ¿cómo sería un ciclo de vida de desarrollo de producto construido con Claude Code desde cero?

Las cinco reglas: todo el mundo entrega, automatiza lo tedioso, confía pero verifica, construye para reconstruir, y prototipa-usa internamente-productiza. Cada capítulo trae citas de fundadores y consejos concretos, y la guía cierra con una lista de verificación de una página. Entre los resultados reportados: 30% más funcionalidades entregadas (ClickHouse), 2–3x de productividad en ingeniería (Omni), 100% del triaje de bugs automatizado (Clay) y más de 6.000 PR por semana (Artemis Security).

## ¿Cuándo es útil?
- Cuando un equipo pequeño necesita una forma de organizarse alrededor de la codificación agéntica, y no una lista de funcionalidades.
- Cuando quienes no son ingenieros tienen la mejor visión de producto pero no hay camino de la idea al prototipo funcional.
- Cuando hay que decidir qué partes del SDLC delegar a agentes y qué debe existir antes de poder confiar en ellos.
- Cuando las reescrituras siempre pierden la pelea por la priorización y el desmontaje de deuda técnica nunca se agenda.
- Cuando los experimentos internos con agentes necesitan una ruta hacia el producto de cara al cliente.

## Puntos clave
- **El paso 0→1 se abre a todos; la división del trabajo permanece.** Marketing sigue haciendo marketing y desarrollo sigue desarrollando, pero quien entiende el problema construye la primera versión. Heidi llama a la cadena de traspasos antigua el "problema del teléfono descompuesto".
- **Las contribuciones necesitan mecanismos, no ánimos.** Conecta Claude a herramientas reales vía MCP o CLI, dale a los prototipos un foro que alimente la hoja de ruta (las revisiones trimestrales de Clay, el canal de Slack de Omni) y comparte los estándares como skills mediante un directorio o un marketplace de plugins.
- **Los agentes se hacen cargo del trabajo recurrente de punta a punta.** Los agentes de tests inestables y de cobertura faltante de ClickHouse son el segundo y tercer contribuyente de su repositorio; Clay automatizó el triaje de bugs desde el primer pase hasta la corrección sugerida; el revisor de Translucent se despliega en abanico y sintetiza múltiples ángulos.
- **Las reglas 2 y 3 forman un par.** Zingage dio a Claude autonomía total al principio y obtuvo código plausible que se desviaba de su arquitectura "de formas que parecían correctas pero no lo eran"; la solución fueron 567 líneas de invariantes en `CLAUDE.md`.
- **Corrige el principio, no el ejemplo.** Cainex canaliza las correcciones de sus auditores hacia instrucciones de agente versionadas y hace back-testing contra un conjunto dorado más muestras aleatorias, tras una primera versión que sobreajustaba y acumulaba parches.
- **Nada es permanente.** Clay lo construye cuatro veces; Harvey rehízo la arquitectura con cada ola de capacidad de los modelos; Commure convirtió el desmontaje de feature flags en una sola invocación de skill. Los worktrees de git y el modo plan son lo que abarata reconstruir.
- **El volante de inercia.** Avanzar en tu propia práctica de codificación agéntica te enseña cómo evoluciona el diseño del arnés en la frontera, y eso lo inviertes en tus propios agentes y productos: agente interno → uso interno → producto de cara al cliente sobre la API de Claude, el SDK o Managed Agents.

## Recursos incluidos
- `skills/agentic-coding-operating-rules/SKILL.md` — las cinco reglas como procedimiento operativo aplicable.
- `skills/agentic-coding-operating-rules/references/five-rules.md` — cada regla completa, con las citas de fundadores y sus límites.
- `skills/agentic-coding-operating-rules/references/checklist.md` — la lista de verificación técnica consolidada de la guía.
- `skills/agentic-coding-operating-rules/templates/root-context-file.md` — un andamiaje de `CLAUDE.md` raíz para invariantes.
- `skills/agentic-coding-operating-rules/examples/self-improvement-loop.md` — el bucle de corrección de Cainex, paso a paso.
- `skills/agentic-coding-operating-rules/examples/company-patterns.md` — lo que hizo cada una de las quince empresas.
- `agents/flaky-test-fixer.md`, `agents/test-coverage-finder.md`, `agents/multi-angle-code-reviewer.md`, `agents/bug-triage.md` — los cuatro roles de agente nombrados en la guía.
- `guides/startup-operating-model.{en,ko,es,ja}.md` — el modelo operativo y una secuencia de adopción.

## Fuente
[The Claude Code guide for startups](https://claude.com/blog/claude-code-guide-for-startups) por Michael Segner — publicado el 2026-08-20.
