[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Claude Tag (beta), que añade Claude a un canal de Slack, ahora puede usar los conectores personales de
un miembro para las solicitudes de ese miembro. Antes solo estaban disponibles los conectores que un
administrador asociaba al canal, así que el acceso seguía al canal y no a la persona.

## ¿Cuándo es útil?
- Cuando un miembro necesita datos detrás de su propio inicio de sesión (calendario, documentos
  privados, cuentas de CRM asignadas, despliegues de staging).
- Cuando un administrador decide cómo gobernar el acceso a conectores en canales de Claude Tag.
- Cuando hay que separar lo que puede ejecutarse sin supervisión de lo que requiere a una persona.

## Puntos clave
- Se conectan herramientas en claude.ai/customize; Claude pide permiso la primera vez que una
  solicitud necesita una. Nadie más en el canal puede usar tus conectores.
- Una misma solicitud puede combinar tus conectores con los compartidos del canal.
- El modo revisión muestra cada respuesta antes de publicarla; el modo automático publica salvo que
  detecte contenido sensible.
- Las acciones con conectores personales quedan auditadas bajo tu cuenta en el registro de esa
  herramienta; el trabajo del canal queda bajo su cuenta de servicio. Puedes desconectar cuando quieras.
- Los conectores personales nunca se ejecutan sin supervisión: las rutinas programadas y las acciones
  que Claude inicia por sí mismo usan conectores compartidos.
- Opciones de administración: herramientas compartidas bajo una identidad de agente, canales solo con
  conectores personales apoyados en el control de acceso por roles existente, o decisión herramienta
  por herramienta. En Enterprise se puede exigir revisión para todos.
- Despliegue en planes Team; Enterprise vendrá después.

## Recursos incluidos
- Skill: `slack-personal-connectors` — conectores personales vs. compartidos, modos de publicación,
  gobernanza (`examples/channel-scenarios.md`).

## Fuente
- https://claude.com/resources/articles/claude-tag-now-supports-personal-connectors-in-channels
