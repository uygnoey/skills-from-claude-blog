[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Una guía práctica de Lydia Hallie sobre por qué dos sesiones de Claude Code que hacen la misma tarea pueden costar cantidades muy distintas, y sobre qué está bajo tu control. Las herramientas de codificación agéntica facturan por token y no por puesto, así que la pregunta no es cómo usar menos tokens, sino cómo mantener los que gastas apuntando a la tarea que realmente pediste, en lugar de reenviar archivos y salidas de comandos irrelevantes en cada turno.

Divide el problema en dos variables: cuánto cuesta un token (modelo, entrada frente a salida, caché de prompts) y cuántos tokens envía la sesión (qué entra en el contexto y cuánto tiempo permanece), y cierra con un orden aproximado de prioridad sobre dónde mirar primero.

## ¿Cuándo es útil?
- Cuando las sesiones resultan caras y no está claro adónde se va el gasto.
- Cuando una conversación larga arrastra a cada turno lecturas sin relación hechas esa mañana.
- Cuando hay que decidir entre `/clear`, `/compact` y `/rewind`.
- Cuando las definiciones de herramientas de los servidores MCP conectados, o un `CLAUDE.md` desbordado, llenan el contexto antes de que hayas escrito nada.
- Cuando valoras si un trabajo ruidoso — rastrear logs, analizar trazas — corresponde a un subagente.
- Cuando incorporas a un equipo a la codificación agéntica y quieres fijar los hábitos pronto.

## Puntos clave
- **Los tokens de salida cuestan unas 5× los de entrada**, y los tokens de razonamiento son de salida, así que el nivel de esfuerzo es un dial directo sobre la mitad cara. `MAX_THINKING_TOKENS=0` baja un escalón por debajo de `/effort low` durante una sesión (no aplica a Fable 5).
- **Las lecturas de caché cuestan unas 0,1× la entrada; una escritura hasta 2×, una vez por token.** Preservar la caché pesa más que casi cualquier otra optimización.
- **Qué rompe la caché:** `/model`, `/effort` y el modo rápido forman parte de la clave de caché y fuerzan un prellenado completo; `/compact` sustituye la conversación (el prompt de sistema sobrevive); la caché expira tras 1 hora con suscripción y 5 minutos con clave de API, y `ENABLE_PROMPT_CACHING_1H=1` amplía este último caso.
- **`/rewind` es gratis** — recorta el final y deja la caché intacta. `/compact` siempre cuesta algo, y por eso conviene compactar *antes* de una pausa y no después de que la caché haya expirado.
- **Fija `/model` y `/effort` una vez en una sesión nueva.** Ambos persisten de la sesión anterior, así que lo que está en vigor puede no ser lo que pretendías.
- **Nada se envía una sola vez.** Cada archivo leído y cada salida de comando se reenvían en cada turno posterior — cacheados y baratos, pero ocupando contexto. El turno 40 paga por los treinta y nueve anteriores, y por eso una sesión larga cuesta más que el mismo trabajo repartido.
- **Ejecuta `/context` una vez** para ver la carga permanente: definiciones de herramientas, prompt de sistema, `CLAUDE.md`, elementos de arranque. Mantén `CLAUDE.md` específico, traslada las instrucciones de flujo de trabajo a skills (que se cargan solo al usarse) y desactiva con `/mcp` los servidores MCP que no uses.
- **Señala el archivo.** Una petición vaga dispara un grep y una ristra de lecturas; nombrar el archivo da una sola lectura; mencionarlo con `@` no da ninguna, porque se adjunta antes de enviar el mensaje. Menciónalo una vez por conversación: repetirlo adjunta otra copia.
- **Silencia tus comandos.** La salida se añade igual que la lectura de un archivo y permanece toda la sesión. Pon los dos o tres comandos que usas todo el día en `CLAUDE.md` con sus flags silenciosos. La salida por encima de unos 30.000 caracteres se escribe a un archivo con una vista previa en línea (`BASH_MAX_OUTPUT_LENGTH`).
- **`/loop` se dispara como un turno completo en la sesión que lo inició**, arrastrando toda la conversación cada vez, y falla la caché si pasa más de una hora entre disparos. Ejecuta los bucles desde una sesión nueva en otra terminal.
- **Los subagentes tienen su propio contexto pero no tu conversación**, y solo vuelve su respuesta. Compensan cuando un trabajo genera mucha salida que no necesitas; fija un modelo más pequeño en la configuración del subagente para trabajos ruidosos que delegas a menudo.
- **Por dónde mirar primero**, aproximadamente por impacto: duración de la sesión, tamaño de la salida de comandos, archivos leídos, y modelo y esfuerzo.
- En un modelo de 1M de contexto, `/autocompact 200k` restaura la red de seguridad de compactado automático (Claude Code v2.1.221+).

## Recursos incluidos
- `skills/token-efficient-sessions/SKILL.md` — las prácticas como skill accionable.
- `skills/token-efficient-sessions/references/token-pricing.md` — modelo, entrada/salida y la tabla completa de invalidación de caché.
- `skills/token-efficient-sessions/references/context-lifecycle.md` — qué entra en el contexto, cuánto permanece y la decisión entre `/clear`, `/compact` y `/rewind`.
- `skills/token-efficient-sessions/templates/claude-md-snippets.md` — secciones de comandos habituales e instrucciones de compactado para pegar en `CLAUDE.md`.
- `skills/token-efficient-sessions/examples/session-patterns.md` — ocho pares de antes y después.
- `guides/session-cost-optimization.{en,ko,es,ja}.md` — el mismo material como guía en cuatro idiomas.

## Fuente
- https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions (14 de agosto de 2026)
