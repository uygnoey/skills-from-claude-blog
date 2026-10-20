[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un anuncio (publicado junto con la Open Agent Safety Platform de NVIDIA) sobre cómo Anthropic y NVIDIA
añaden capas de seguridad y control a la pila de agentes. Claude Managed Agents ya ejecuta el trabajo
de los agentes en sandboxes; los sandboxes autoalojados mantienen la ejecución dentro de tu perímetro,
y NVIDIA OpenShell añade un runtime de políticas dentro de ese sandbox que controla a qué puede acceder
el agente y qué puede hacer.

## ¿Cuándo es útil?
- Cuando los agentes clonan repositorios, leen sitios web, analizan salidas de herramientas o instalan
  paquetes.
- Cuando el código y los datos deben permanecer dentro de un perímetro empresarial o regulado.
- Cuando necesitas definir y demostrar el acceso mínimo que necesita un agente.

## Puntos clave
- El contenido no confiable en el sandbox puede traer inyección de prompts o código que se ejecuta.
- Separar el "cerebro" de las "manos": el arnés, el estado de sesión y las credenciales viven fuera del
  sandbox en infraestructura duradera; el sandbox es solo una herramienta de ejecución.
- Sandboxes autoalojados: el bucle del agente (orquestación, gestión de contexto, recuperación de
  errores) permanece en la infraestructura de Anthropic, y las llamadas a herramientas de cada sesión
  se ejecutan en tu infraestructura o en un proveedor de sandboxes gestionado.
- NVIDIA OpenShell bloquea todo salvo que una regla lo permita, revisa cada uso de herramienta, aplica
  reglas a archivos, red y datos, las impone fuera del agente y registra cada decisión.
- Empieza con permisos estrechos, revisa el registro y ajusta las reglas con Claude; el policy prover
  de OpenShell usa prueba matemática para confirmar a qué puede llegar el agente.
- Ejemplos: Sculptor de Clay (monta almacenes de archivos externos, instala paquetes); Rogo (microVMs
  aisladas para clientes regulados).
- Managed Agents está en beta pública; OpenShell es de código abierto bajo Apache 2.0.

## Recursos incluidos
- Skill: `isolate-agent-execution` — pasos para separar cerebro y manos, autoalojar el sandbox y usar
  un runtime de políticas de denegación por defecto, con una lista de verificación de arquitectura.

## Fuente
- https://claude.com/resources/articles/giving-companies-more-control-over-their-ai-agents-with-nvidia
