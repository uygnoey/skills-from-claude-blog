[English](./dynamic-workflows.en.md) · [한국어](./dynamic-workflows.ko.md) · **Español** · [日本語](./dynamic-workflows.ja.md)

# Guía: dynamic workflows en Claude Code

## Qué es
Los dynamic workflows permiten que Claude Code escriba y ejecute un arnés multiagente a demanda, ejecutando un archivo de workflow en JavaScript que puede crear y coordinar subagentes.

## Cómo funciona (nivel alto)
- El workflow ejecuta un archivo JavaScript con funciones auxiliares especiales para crear y coordinar subagentes.
- Puede usar utilidades estándar de JavaScript (p. ej., JSON, Math, Array) para procesar datos.
- Puede decidir qué modelo usa cada agente y si los subagentes se ejecutan en su propio worktree.
- Si se interrumpe, al reanudar la sesión puede continuar.

## Cuándo usarlo
Es especialmente útil en tareas complejas y de alto valor que se benefician de contextos aislados, roles especializados y síntesis/verificación estructurada.

## Patrones comunes
- Classify-and-act
- Fan-out-and-synthesize (barrera + fusión)
- Verificación adversarial (revisión contra una rúbrica)
- Generate-and-filter (generar muchas → deduplicar → quedarse con lo mejor)
- Torneo (juicio por pares hasta un ganador/top-k)
- Loop until done (condición de parada, no pases fijos)

## Casos de uso
- Ingeniería: dividir por tests/módulos/callsites; arreglar en worktrees en paralelo; revisar adversarialmente y fusionar.
- Triage: clasificar, deduplicar contra lo ya registrado, poner en cuarentena lo incierto y actuar.
- Evals ligeros: ejecutar soluciones candidatas en worktrees, comparar y calificar contra una rúbrica.
- No técnico: crítica multivista, ranking de CV con rúbrica, torneos de naming.

## Guardar y compartir
- Guardar desde el menú del workflow (tecla `s`) y almacenar en `~/.claude/workflows`.
- Para distribuir vía un skill, poner los archivos JavaScript en la carpeta del skill y referenciarlos desde `SKILL.md`.
- Considera tratar los workflows como plantillas para mayor flexibilidad.

## Fuente
- https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code
