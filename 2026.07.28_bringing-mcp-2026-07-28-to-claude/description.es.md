[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
El anuncio de MCP 2026-07-28, la quinta versión de la especificación del Model Context Protocol, publicada el 28 de julio de 2026. Tres cambios la definen: MCP pasa de un protocolo bidireccional con estado a un **núcleo sin estado de petición/respuesta**, MCP Apps y Tasks se gradúan dentro de un **marco de extensiones versionado**, y **la autorización se alinea con OAuth 2.0 y OIDC de producción**, de modo que los servidores se conectan a sistemas de identidad empresarial como Entra u Okta sin apaños. El soporte se está desplegando en los productos de Claude.

El artículo cubre también el lado de Claude: más de 950 servidores MCP listados en el directorio de conectores, MCP Apps para interfaces interactivas dentro de la conversación, autenticación gestionada por la empresa para conectores aprovisionados por el IdP a toda la organización, un panel de observabilidad para desarrolladores de conectores, y túneles MCP (research preview) para alcanzar servidores dentro de una red privada.

## ¿Cuándo es útil?
- Al planificar o refactorizar un servidor MCP y decidir qué cambia el núcleo sin estado en su estado y su despliegue.
- Al decidir si un servidor puede moverse a infraestructura serverless o edge.
- Al conectar un servidor a un proveedor de identidad empresarial, o al eliminar el pegamento de autenticación escrito a medida para cubrir huecos de la especificación anterior.
- Al añadir interfaces interactivas o trabajo de larga duración a un servidor y buscar la vía soportada en lugar de un apaño sobre el protocolo central.
- Al desplegar conectores a nivel de organización mediante un IdP en lugar de usuario por usuario.
- Al preparar un conector para el directorio de Claude, o al usar después su panel de rendimiento.
- Cuando una herramienta interna está tras un cortafuegos y exponer un endpoint público no es la opción adecuada.

## Puntos clave
- **Núcleo sin estado.** La petición/respuesta sustituye al protocolo bidireccional con estado. Los servidores pueden desplegarse en serverless y edge, lo que simplifica tanto construir para Claude como escalar a medida que crece la adopción.
- **El encuadre de despliegue que llega del ecosistema:** el núcleo sin estado convierte MCP en una carga de trabajo HTTP de primera clase, sin gestión de sesiones que sortear.
- **Extensiones versionadas.** MCP Apps y Tasks se publican bajo un marco formal, así que las interfaces interactivas y el trabajo de larga duración son capacidades añadidas y no cambios al protocolo central.
- **Autorización endurecida.** La autorización ahora coincide con cómo se despliegan realmente OAuth 2.0 y OIDC en producción, que es lo que hace que Entra y Okta funcionen sin apaños.
- **Escala del estándar.** MCP superó recientemente los 400 millones de descargas mensuales del SDK, 4x más este año; Claude lista más de 950 servidores MCP en su directorio de conectores.
- **MCP Apps** permite a un servidor renderizar interfaz interactiva en línea, de modo que el usuario ve lo que hace el conector sin cambiar de pestaña.
- **La autenticación gestionada por la empresa** no exige nada al usuario final: el administrador autoriza el conector una vez, los usuarios heredan el acceso por sus grupos del IdP y queda conectado en el primer inicio de sesión.
- **La observabilidad de conectores** muestra adopción, errores y latencia, y uso por producto: sirve para encontrar herramientas que faltan, no solo las que fallan.
- **Los túneles MCP (research preview)** alcanzan servidores dentro de una red privada sin reglas de firewall entrantes, sin endpoints públicos y sin listas de IP permitidas en el origen.

## Recursos incluidos
- `skills/mcp-2026-07-28-adoption/SKILL.md` — un procedimiento de adopción: qué cambia el núcleo sin estado, cuándo recurrir a cada extensión, cómo alinear la autorización, qué capacidades del lado de Claude aplican y un orden de despliegue que sigue las dependencias.
- `skills/mcp-2026-07-28-adoption/references/whats-new.md` — los tres cambios de la especificación al completo, las cifras del ecosistema y lo que reportaron quienes construyeron durante la beta.
- `skills/mcp-2026-07-28-adoption/references/claude-mcp-capabilities.md` — MCP Apps, autenticación gestionada por la empresa, observabilidad de conectores y túneles MCP, cada uno con cuándo construir para ello.
- `guides/mcp-2026-07-28-release.{en,ko,es,ja}.md` — la versión como recorrido narrativo en cuatro idiomas.

## Fuente
[Bringing MCP 2026-07-28 to Claude](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude) — publicado el 2026-07-28.
