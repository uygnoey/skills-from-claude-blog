[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Este post explica cómo Brendan MacLean (MacCoss Lab, University of Washington) incorpora Claude Code de la misma forma en que incorpora a nuevos desarrolladores a un repositorio grande y mantenido durante muchos años: tratando el contexto y la documentación de proceso como artefactos de proyecto versionados.

## ¿Cuándo es útil?
- Cuando necesitas que Claude Code trabaje bien en un repositorio grande y maduro con mucho conocimiento implícito.
- Cuando el equipo rota con frecuencia (estudiantes, contribuyentes de open source) y la incorporación debe ser repetible.
- Cuando quieres reducir el coste de iteración manteniendo contexto duradero y versionado junto al código.

## Puntos clave
- Mantén un repositorio separado de “contexto para IA” (el ejemplo del post es `pwiz-ai`) para que las guías sobrevivan cambios de ramas y mejoren con el tiempo.
- Coloca un `CLAUDE.md` en la raíz para describir la configuración del entorno y enlazar documentación más profunda (“referencia, no incrustes”).
- Construye una biblioteca pequeña y reutilizable de skills para patrones de trabajo recurrentes (p. ej., depuración, convenciones de control de versiones, orientación del proyecto).
- Usa integraciones (el post menciona servidores MCP) para dar a Claude Code acceso a datos del proyecto como resultados de tests, excepciones, hilos de soporte y etiquetas de releases.

## Recursos incluidos
- No hay adjuntos descargables en el post; se mencionan artefactos del proyecto como `CLAUDE.md` y un repositorio auxiliar (`pwiz-ai`).

## Fuente
- https://claude.com/blog/onboarding-claude-code-like-a-new-developer-lessons-from-17-years-of-development
