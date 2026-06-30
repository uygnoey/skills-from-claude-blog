[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Este post explica cómo el equipo de Claude Code entiende los **bucles agénticos (agentic loops)**: ciclos de trabajo repetidos que continúan hasta que se cumple una condición de parada.

Presenta una progresión desde el trabajo **por turnos** hacia bucles **basados en objetivos**, **basados en tiempo** y **proactivos**, y aclara cuándo conviene cada enfoque.

## ¿Cuándo es útil?
- Cuando necesitas decidir si basta una sesión interactiva puntual, un bucle con objetivo verificable, un bucle periódico o una rutina totalmente automatizada.
- Cuando quieres mejorar la fiabilidad (auto-verificación) y gestionar el coste/uso de tokens en automatizaciones largas.

## Puntos clave
- Empieza por lo más simple; no todas las tareas requieren bucles complejos.
- Define condiciones de **parada** claras y (en bucles por objetivo) un **límite de turnos** explícito.
- Prefiere criterios de éxito **deterministas** y verificables (tests, puntuaciones, umbrales) frente a juicios subjetivos.
- Mejora la calidad dando a Claude formas de **verificar** el resultado (herramientas, skills, comprobaciones cuantitativas) y usando un segundo agente para revisar cuando sea necesario.
- Gestiona tokens eligiendo el primitive/model adecuados, haciendo un piloto antes de escalar y usando scripts para trabajo determinista.

## Recursos incluidos
- Plantilla de ejemplo `SKILL.md` para verificar cambios de frontend (ver `skills/verify-frontend-change/SKILL.md`).
- Comandos de ejemplo mostrados en el post (ver `skills/loops-playbook/examples/commands.md`).

## Fuente
- https://claude.com/blog/getting-started-with-loops
