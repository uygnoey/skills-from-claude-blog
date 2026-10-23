[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un anuncio (17 de septiembre de 2026) de los proyectos rediseñados, en beta en Claude Code: describes un
objetivo y un coordinador gestiona el trabajo en varios hilos, en lugar de que tú dividas tareas, gestiones
traspasos y fusiones resultados.

## ¿Cuándo es útil?
- Para trabajo largo y de varias partes que abarca varios repositorios o muchas subtareas paralelas.
- Cuando quieres delegar resultados (p. ej., "reducir la latencia p75 del checkout") y no prompts sueltos.
- Al decidir cómo configurar y dirigir un proyecto y controlar el uso.

## Puntos clave
- Se empieza con un objetivo y un repositorio o contexto; se configuran entorno, conectores, plugins,
  instrucciones y modelo.
- Al coordinador se le informa como a un jefe de gabinete, y reparte tareas a hilos nuevos o existentes.
- Cada hilo es una sesión en la nube de Claude Code con su propia rama y copia del repositorio; abre PR y
  ejecuta pruebas, y los cambios solapados se resuelven como conflictos de fusión normales. Los hilos pueden
  usar subagentes, bucles y workflows.
- Memoria compartida entre hilos y una biblioteca de archivos y artefactos; se puede ajustar la frecuencia
  de seguimiento, la creación de hilos y el detalle de las actualizaciones.
- Se puede dirigir desde el móvil y el trabajo sigue cuando te ausentas.
- Los hilos paralelos pueden agotar antes los límites de uso; hay uso por proyecto y modelo/esfuerzo por rol.
- Beta primero para algunos usuarios Pro/Max con sesiones en la nube; hilos locales "muy pronto".

## Recursos incluidos
- Skill: `goal-driven-multi-thread-projects` (`templates/coordinator-brief.md`,
  `references/availability-and-limits.md`).

## Fuente
- https://claude.com/resources/articles/projects-redesigned
