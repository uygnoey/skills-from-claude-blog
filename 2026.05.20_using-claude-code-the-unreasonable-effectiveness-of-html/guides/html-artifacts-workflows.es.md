[English](./html-artifacts-workflows.en.md) · [한국어](./html-artifacts-workflows.ko.md) · **Español** · [日本語](./html-artifacts-workflows.ja.md)

# Flujos de trabajo con artefactos HTML en Claude Code

## ¿De qué trata esta guía?
Una guía práctica para usar archivos HTML como artefactos de trabajo en Claude Code (en vez de Markdown) para planificación, entendimiento de código, prototipado e informes.

## ¿Cuándo es útil?
Cuando Markdown se queda corto en legibilidad, diseño o cuando necesitas incluir interactividad ligera.

## Puntos clave
- Prefiere HTML cuando necesitas un diseño más rico (rejillas/columnas/recuadros) y mayor densidad de información.
- Para esfuerzos grandes, itera sobre varios artefactos HTML (opciones → maquetas → plan de implementación) y luego inicia una sesión nueva para implementar.
- Para revisión/entendimiento, pide diffs renderizados con anotaciones en línea y hallazgos codificados por severidad.
- Para “editores desechables”, incluye siempre un botón de exportación (copiar como JSON/prompt/diff/Markdown).

## Patrones de flujo sugeridos
1. **Rejilla de exploración**: comparar alternativas lado a lado
2. **Plan de implementación**: maquetas, diagramas de flujo de datos y fragmentos clave
3. **Explicar un PR/sistema**: diff + anotaciones + sección de “gotchas”
4. **Prototipar interacciones**: sliders/perillas para ajustar parámetros
5. **Editor específico**: UI de un solo uso con exportación a un formato duradero

## Recursos incluidos
- Plantillas de prompts: `../skills/html-artifacts/templates/prompt-patterns.md`

## Fuente
- https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html
