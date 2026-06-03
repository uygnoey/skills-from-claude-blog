[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Lessons from building Claude Code: How we use skills

## ¿De qué trata este post?
Este post resume las lecciones internas de Anthropic al crear y escalar cientos de skills en Claude Code, incluyendo categorías comunes de skills y consejos prácticos para escribirlas, estructurarlas y distribuirlas.

## ¿Cuándo es útil?
Es útil cuando estás diseñando skills para Claude Code y necesitas heurísticas concretas sobre qué incluir (gotchas, referencias, scripts, plantillas), cómo organizar la carpeta para “progressive disclosure” y cómo distribuir skills mediante repositorios o plugins.

## Puntos clave
- Las skills son carpetas (no solo un archivo markdown) y pueden incluir scripts, assets, datos y configuración.
- Anthropic identificó nueve categorías; las skills que se mantienen claramente en una sola categoría suelen funcionar mejor.
- La sección de mayor señal suele ser “Gotchas”, construida a partir de fallos reales.
- Puedes compartir skills registrándolas en `./.claude/skills` o distribuyéndolas como plugins instalables desde un marketplace.
- Los hooks pueden activarse bajo demanda (solo cuando se usa la skill) para no ser disruptivos.

## Recursos incluidos
- Una guía reutilizable tipo checklist para diseño y estructura de skills.
- Una referencia de categorías y ejemplos de skills.

## Fuente
- https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills
