[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Cómo el equipo de ciberseguridad de Anthropic construyó una plataforma de detección con Claude Code

## ¿De qué trata este post?

Estudio de caso del 11 de mayo de 2026 escrito por Jackie Bow, Technical Lead del equipo Detection Platform Engineering de Anthropic, sobre cómo construyeron **CLUE (Claude Looks Up Evidence)** — una plataforma de detección y respuesta con dos superficies (CLUE Triage y CLUE Investigate) que usa Claude como interfaz en lenguaje natural sobre los sistemas internos de Anthropic. El post detalla qué desplegaron, cómo midieron impacto (tasa de falsos positivos, volumen de consultas y tool calls, horas ahorradas) y cómo su filosofía pasó de los playbooks tipo SOAR a darle a Claude límites y dejar que elija sus propios caminos de investigación.

## ¿Cuándo es útil?

- Cuando un equipo de seguridad defensiva evalúa montar una superficie Claude para triage e investigación sobre su SIEM y sus sistemas internos.
- Cuando hay que diseñar la frontera entre playbooks deterministas e investigación por agentes, y el alcance de los datos que el agente puede leer.
- Cuando se prepara el caso de negocio interno de una plataforma de detección: volumen de alertas, reducción de falsos positivos, horas ahorradas, cobertura de señales de baja confianza.
- Cuando se modela cómo el contexto organizacional (Slack, docs internos, data warehouse, repos de código) se conecta a un agente de seguridad vía herramientas.

## Puntos clave

- CLUE Triage hace el triage de primera pasada sobre toda alerta entrante y la enriquece con contexto de Slack, documentación interna, código y data warehouse; el analista recibe disposition y confidence score.
- CLUE Investigate ofrece una interfaz de consulta en lenguaje natural; Claude corre un bucle agéntico donde un orquestador despacha sub-agentes que ejecutan consultas en paralelo y sintetizan hallazgos.
- Impacto reportado: la tasa de falsos positivos cayó de **~1 de cada 3 a 7%**; en 30 días CLUE automatizó **~12.000 consultas y 27.000 tool calls**, **~1.870 horas / 234 días-persona** de trabajo manual, **ahorros de tiempo de 5–10x**; promedio de ~25 tool calls y ~11 consultas por investigación.
- Construido con Claude Code como "compañero de diseño y colaborador": PoC en un día, diseño e implementación en una semana.
- Filosofía: codificar los límites (qué herramientas y datos puede tocar Claude) pero dejar la estrategia abierta — Claude encuentra rutas de investigación que un humano no habría prescrito.
- Hacia adelante: pasar de reacción a alertas a caza continua proactiva, tratar el corpus de transcripts de investigación como memoria organizacional y abrazar la no-determinismo corriendo múltiples estrategias en paralelo.

## Recursos incluidos

- `skills/clue-style-detection-platform-playbook/SKILL.md` — cómo planear una plataforma de detección al estilo CLUE: superficies, forma del bucle agéntico, fuentes de contexto, métricas y gobernanza.
- `skills/clue-style-detection-platform-playbook/references/clue-architecture-from-post.md` — catálogo textual de componentes, métricas y citas del post.
- `skills/clue-style-detection-platform-playbook/examples/data-governance-investigation.md` — ejemplo trabajado que sigue el escenario de gobernanza de datos de contratistas mencionado en el post.

## Fuente

- [How Anthropic's cybersecurity team built a threat detection platform with Claude Code](https://claude.com/blog/how-anthropic-uses-claude-cybersecurity) (blog de Anthropic, 11 de mayo de 2026)
