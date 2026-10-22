[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Anthropic abre los plugins como la vía principal para que los desarrolladores creen extensiones de
terceros para Claude. Un plugin empaqueta conectores MCP, Agent Skills o ambos, y los plugins
aprobados aparecen en el directorio de Claude. El portal de envío ya está abierto para
desarrolladores con planes de pago de Claude.

## ¿Cuándo es útil?
- Al decidir entre publicar un único conector MCP o un paquete de plugin completo.
- Al preparar un envío y querer saber qué revisa el proceso.
- Al planificar cómo medir un listado una vez publicado.

## Puntos clave
- Dos vías: un único conector MCP (apuntando a un servidor MCP remoto) o un paquete de plugin alojado
  en GitHub con servidores MCP y skills. En Claude Code el paquete también puede incluir LSP,
  comandos, hooks y agentes.
- Los envíos se validan automáticamente y pasan un análisis de seguridad; el portal muestra el estado
  de revisión, los resultados del análisis y los cambios recomendados. Tras la aprobación, el
  desarrollador elige cuándo publicar.
- Analítica: instalaciones por superficie de producto y por versión; métricas de descubrimiento con
  vistas del listado y las búsquedas que llevan a él.
- Claude admite la especificación MCP más reciente (núcleo sin estado), además de MCP Apps (interfaz
  interactiva en el chat) y Enterprise Managed Auth (OAuth sin intervención para usuarios
  empresariales).
- Llega una experiencia de descubrimiento única para Claude y Claude Code; los skills, conectores y
  plugins existentes no necesitan cambios, y más adelante un listado de conector podrá convertirse
  en plugin.

## Recursos incluidos
- Skill: `plugin-directory-submission` — elegir la vía de envío, ciclo de revisión, publicación,
  analítica, extensiones de MCP 2.0 (`references/submission-portal.md`).

## Fuente
- https://claude.com/resources/articles/build-plugins-for-claude
