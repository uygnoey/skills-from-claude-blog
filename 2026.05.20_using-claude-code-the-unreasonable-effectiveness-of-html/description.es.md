[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Using Claude Code: The unreasonable effectiveness of HTML

## ¿De qué trata este post?
Este post explica por qué una persona del equipo de Claude Code prefiere generar **archivos HTML** (en lugar de Markdown) al usar Claude Code, y describe formas prácticas de usar HTML como un medio más rico, legible y fácil de compartir para el trabajo asistido por IA.

## ¿Cuándo es útil?
- Cuando necesitas resultados más fáciles de leer y revisar que en Markdown.
- Cuando necesitas diseños más ricos (rejillas, columnas, recuadros), diagramas (SVG) o interactividad integrada.
- Cuando quieres artefactos fáciles de compartir y reutilizar (p. ej., exploraciones de planificación, explicaciones para revisar un PR, informes de incidentes).
- Cuando una interfaz de edición “desechable” y específica facilita editar datos estructurados y exportarlos de vuelta a Claude Code (p. ej., copiar como JSON/prompt/diff).

## Puntos clave
- Se presenta HTML como un “lienzo más rico” que mejora la densidad de información, la legibilidad y la capacidad de compartir frente a Markdown.
- Un flujo de trabajo productivo es iterar sobre varios artefactos HTML (lluvia de ideas → exploración de opciones → maquetas → plan de implementación) y luego iniciar una sesión nueva para implementar usando esos artefactos como contexto.
- Los artefactos HTML son especialmente útiles para revisión/entendimiento de código (renderizar diffs, anotar, codificar hallazgos por severidad), prototipado de diseño e investigación/reporting.
- Para interfaces de edición personalizadas, conviene terminar con un botón de exportación (p. ej., “copy as JSON”, “copy as prompt”, “copy diff”) para que el resultado se pueda pegar en Claude Code o guardar en un archivo.

## Recursos incluidos
- Skill: `skills/html-artifacts/SKILL.md`
- Guide: `guides/html-artifacts-workflows.*.md`

## Fuente
- https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html
