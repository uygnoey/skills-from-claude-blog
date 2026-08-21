[English](./mcp-2026-07-28-release.en.md) · [한국어](./mcp-2026-07-28-release.ko.md) · **Español** · [日本語](./mcp-2026-07-28-release.ja.md)

# MCP 2026-07-28 llega a Claude

La quinta versión de la especificación del Model Context Protocol, MCP 2026-07-28, se publicó el 28
de julio de 2026. La nueva especificación lleva MCP a un núcleo sin estado, además de endurecer la
autorización y graduar las extensiones oficiales. El soporte se está desplegando en los productos de
Claude.

## Por qué importa esta versión

MCP ha superado recientemente los **400 millones de descargas mensuales del SDK**, un aumento de 4x
este año, y se ha convertido en el estándar de la industria para conectar agentes de IA con
aplicaciones. El anuncio califica 2026-07-28 como una de las versiones más significativas de la
especificación hasta la fecha.

### Núcleo sin estado

MCP pasa de un protocolo bidireccional con estado a un **modelo de petición/respuesta**. Los
servidores ya pueden desplegarse en infraestructura serverless y edge. Esto simplifica la experiencia
de construir servidores MCP para Claude y de escalar su uso a medida que crece su adopción.

Para quien escribe un servidor, la pregunta práctica es dónde vive hoy el estado por sesión. Todo lo
que asumía una conexión de larga duración tiene que moverse: a la petición, a un almacén que el
servidor consulta, o a una Task.

### Extensiones estandarizadas

**MCP Apps** y **Tasks** pasan a formar parte de un **marco de extensiones versionado**, que da a los
desarrolladores una vía formal para añadir capacidades como interfaces interactivas y trabajos de
larga duración sin cambiar el protocolo central. Como el marco está versionado, un servidor puede
declarar qué versiones de extensión implementa en lugar de asumir que el cliente lo soporta todo.

### Autorización endurecida

La autorización se alinea ahora con **despliegues de OAuth 2.0 y OIDC de producción**, de modo que
los servidores MCP se conectan a sistemas de identidad empresarial como **Entra** u **Okta** sin
apaños. El pegamento de autenticación escrito a medida para cubrir huecos de la especificación
anterior es lo primero que conviene eliminar.

## Lo que dijeron quienes construyeron durante la beta

Empresas de todo el ecosistema llevan construyendo sobre la nueva especificación junto a la comunidad
MCP desde la beta.

**Figma** (Josh Clemm, VP de Ingeniería) describe cómo cada vez más creadores usan su servidor MCP
para llevar resultados generados al lienzo de Figma, donde los equipos los exploran, los reinterpretan
y los refinan hasta convertirlos en productos que destacan. A medida que ese uso crece, la
arquitectura sin estado escala con él, y MCP Apps, Tasks y Enterprise-Managed Auth les permiten hacer
más para mantener diseño y código en un mismo flujo conectado.

**Intuit** (Chris Kasten, arquitecto jefe y SVP de Ingeniería, Platform and Development Xceleration
Group) apoya la nueva especificación: el núcleo sin estado y el marco de extensiones, incluidos MCP
Apps y Tasks, permiten a sus tecnólogos y clientes construir y conectar experiencias agénticas a
escala empresarial, y sostener la entrega de experiencias de inteligencia financiera de confianza a
sus 100 millones de consumidores y negocios, allá donde elijan trabajar.

**Netlify** (Sean Roberts, VP de Applied AI) plantea el caso del despliegue con claridad: el núcleo
sin estado convierte MCP en una carga de trabajo HTTP de primera clase, sin gestión de sesiones que
sortear. Sus clientes querían que los MCP en Netlify fueran tan simples como el resto de la
plataforma, y la nueva especificación lo desbloquea desde la raíz; integrar MCP Apps en el marco de
extensiones es un gran paso adelante en escalabilidad, accesibilidad y capacidad para todo el
ecosistema.

**Paul D'Ambra** (Product Engineer) señala que un protocolo sin estado facilita escalar el servicio y
añadir analítica para los servidores MCP de los clientes: mostrar cómo se usan sus herramientas MCP y
qué herramientas faltan que sus usuarios querrían usar.

**Andrew Goodman** (VP de IA) lo formula como complejidad eliminada: el núcleo sin estado reduce lo
que el equipo tiene que gestionar, así que pueden enviar más funcionalidades a sus clientes, más
rápido y a escala.

**Zoom** (Ross Mayfield, responsable de producto para la plataforma de IA) parte de que el contexto
organizativo es lo que permite a la IA hacer trabajo con sentido, y por eso Zoom construyó servidores
MCP que llevan de forma segura la inteligencia de sus reuniones a plataformas de IA como Claude. La
nueva especificación hace mucho más fácil desplegar y escalar servidores MCP sobre infraestructura
HTTP estándar, de modo que los usuarios reciben esa inteligencia antes y de forma más fiable dentro
de los flujos de trabajo de los que dependen cada día.

## Avances de MCP en Claude

Claude lista ya **más de 950 servidores MCP** en su directorio de conectores, usados por millones de
personas cada día. Junto al soporte para las nuevas extensiones del protocolo, este año se han
lanzado estas funcionalidades:

- **MCP Apps** permite a los servidores renderizar interfaces interactivas directamente en la
  conversación. Los usuarios ven lo que hace un conector y trabajan con él en línea, sin cambiar de
  pestaña.
- **La autenticación gestionada por la empresa** permite a los administradores aprovisionar
  conectores MCP para toda la organización a través de su proveedor de identidad. El administrador
  autoriza el conector una vez, los usuarios heredan el acceso mediante sus grupos del IdP y queda
  conectado en el primer inicio de sesión: configuración cero para el usuario final.
- **La observabilidad para quienes desarrollan conectores** da a los conectores publicados en el
  directorio un panel que muestra su rendimiento en las distintas superficies de producto de Claude.
  Permite seguir la adopción, diagnosticar errores y latencia, y desglosar el uso por producto.
- **Los túneles MCP (research preview)** conectan Claude con servidores MCP dentro de una red privada
  sin exponerlos a internet. Los equipos pueden llevar herramientas internas a Claude sin reglas de
  firewall entrantes, sin endpoints públicos y sin listas de IP permitidas en el origen.

El núcleo sin estado, las extensiones estandarizadas y la autorización endurecida ayudarán a llevar
más aplicaciones a Claude con menos fricción y una experiencia de usuario final más consistente.
Anthropic afirma que seguirá invirtiendo en MCP como estándar abierto junto a la comunidad, y en las
funcionalidades de Claude que hacen MCP más accesible y eficaz en producción.

## Un orden de adopción que sigue las dependencias

1. **Primero, el núcleo sin estado**: las decisiones de despliegue y escalado dependen de él.
2. **Reapunta la autorización al IdP de la organización** mediante la alineación endurecida con
   OAuth 2.0 / OIDC, y combínala con la autenticación gestionada por la empresa para un despliegue
   a nivel de organización.
3. **Añade extensiones donde se ganen su sitio**: Apps para interacción en línea, Tasks para trabajo
   que sobrevive a una petición.
4. **Publica en el directorio de conectores** y usa el panel de observabilidad para seguir adopción,
   errores, latencia y uso por producto.
5. **Para herramientas solo internas**, evalúa los túneles MCP en vez de exponer un endpoint público.

## Para empezar

Explora la especificación y los SDK. El soporte se desplegará pronto en los productos de Claude. Si
planeas enviar tu servidor MCP al directorio de conectores de Claude, lee antes su guía de envío.
Para todos los detalles de la nueva especificación, consulta el anuncio de la versión MCP 2026-07-28.

## Fuente

[Bringing MCP 2026-07-28 to Claude](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude) —
publicado el 2026-07-28.
