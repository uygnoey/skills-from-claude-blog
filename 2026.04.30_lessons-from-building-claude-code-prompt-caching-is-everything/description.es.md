[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Lecciones al construir Claude Code: el prompt caching lo es todo

## ¿De qué trata este post?

El post de Anthropic del 30 de abril de 2026, escrito por Thariq Shihipar (miembro del staff técnico del equipo de Claude Code), comparte las lecciones de prompt caching que el equipo integró en el arnés. Explica cómo funciona el prefix matching, en qué orden Claude Code coloca el contenido estático y dinámico, por qué actualizar el system prompt de forma improvisada rompe el cache, por qué cambiar de modelo o herramientas a mitad de sesión es peligroso, cómo Plan Mode y tool search evitan invalidar el cache, y cómo se implementa la compaction como cache-safe forking. Termina con cinco patrones reutilizables para cualquier persona que construya agentes.

## ¿Cuándo es útil?

- Estás construyendo u operando un agent de larga duración y tu objetivo es mantener alta la tasa de cache hits.
- Estás depurando una regresión donde la tasa de cache hits cayó tras un cambio (timestamps, orden de herramientas, ajustes de parámetros, etc.).
- Estás diseñando una feature como Plan Mode que "parece" requerir cambiar el toolset y necesitas una alternativa cache-safe.
- Estás implementando compaction o sumarización y quieres que comparta el prefix cacheado del padre en vez de pagar la tarifa completa de input no cacheado.
- Buscas un modelo de SLO/alertas alrededor de la tasa de cache hits.

## Puntos clave

- Prompt caching es un prefix match — cualquier cambio dentro del prefix invalida todo lo que viene después.
- Layout del arnés de Claude Code: system prompt estático + herramientas (cacheado globalmente) → CLAUDE.md (cacheado por proyecto) → contexto de sesión (cacheado por sesión) → mensajes de la conversación.
- Maneras comunes de romper el orden del cache: timestamps en el system prompt estático, orden de herramientas no determinista, cambios en los parámetros de las herramientas.
- Para información dinámica (hora actual, cambios de archivos), usa mensajes — Claude Code añade una etiqueta `<system-reminder>` en el siguiente user message o tool result en lugar de editar el system prompt.
- No cambies de modelo a mitad de sesión. Pasar de Opus a Haiku con 100k tokens fuerza reconstruir el cache para Haiku y termina siendo más caro que dejar que Opus responda. Si necesitas cambiar, usa un subagent que prepare un mensaje de hand-off — Claude Code lo hace con los Explore agents en Haiku.
- Nunca añadas o quites herramientas a mitad de sesión. Plan Mode mantiene todas las herramientas y usa EnterPlanMode/ExitPlanMode como herramientas en sí. Tool search usa stubs con `defer_loading: true` en vez de retirar herramientas.
- La compaction se implementa como cache-safe forking: mismo system prompt, mismo contexto de usuario/sistema y mismas tool definitions que el padre, con el prompt de compaction añadido como nuevo user message al final. Se reserva un "compaction buffer" en la ventana de contexto. La compaction ya viene integrada en la API.
- El equipo monitorea la tasa de cache hits como si fuera uptime y declara SEVs cuando baja demasiado.

## Recursos incluidos

- Skill: `skills/agent-prompt-caching-best-practices/SKILL.md` — las reglas accionables y patrones de diseño para mantener estable el prefix, en forma de checklist.
- Referencia: `skills/agent-prompt-caching-best-practices/references/lessons-from-claude-code.md` — las lecciones del post citadas literalmente (layout, mensajes para updates, estabilidad de modelo y herramientas, cache-safe forking, los cinco patrones resumen).
- Ejemplos: `skills/agent-prompt-caching-best-practices/examples/cache-safe-feature-design.md` — ejemplos concretos adaptados del post (Plan Mode como tools, defer_loading para tool search, compaction como cache-safe forking).

## Fuente

Lessons from building Claude Code: Prompt caching is everything — Anthropic (Thariq Shihipar), 30 de abril de 2026: <https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything>
