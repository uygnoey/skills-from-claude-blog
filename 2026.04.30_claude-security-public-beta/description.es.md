[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Claude Security ya está en beta pública

## ¿De qué trata este post?

El anuncio de Anthropic del 30 de abril de 2026 abre Claude Security — antes conocido como Claude Code Security — en beta pública a todos los clientes de Claude Enterprise. El producto usa Claude Opus 4.7 para escanear bases de código, generar parches dirigidos y enviar los hallazgos a los flujos de trabajo de seguridad ya existentes. El acceso para clientes Claude Team y Max se describe como "próximamente". El post detalla cómo funcionan los escaneos, qué cambió desde el research preview limitado, los partners tecnológicos y de servicios mencionados, y testimonios de clientes.

## ¿Cuándo es útil?

- Eres cliente de Claude Enterprise y estás evaluando desplegar Claude Security en tus bases de código.
- Necesitas planificar la cadencia, el alcance (repositorio, directorio, rama) y cómo los hallazgos llegarán a Slack, Jira, sistemas de auditoría o tu programa de gestión de vulnerabilidades.
- Quieres comparar caminos de adopción: directamente vía `claude.ai/security`, embebido en una plataforma partner (CrowdStrike, Microsoft Security, Palo Alto Networks, SentinelOne, Trend.ai, Wiz) o con un partner de servicios (Accenture, BCG, Deloitte, Infosys, PwC).
- Quieres entender el flujo de dismiss-with-reason y confidence rating antes de compartir hallazgos con los equipos de ingeniería.

## Puntos clave

- Claude Security está en beta pública para clientes Claude Enterprise; el acceso para clientes Claude Team y Max llegará pronto.
- Funciona con Claude Opus 4.7 y se accede desde la barra lateral de Claude.ai o en `claude.ai/security` — sin integración por API ni construcción de un agente a medida.
- Los escaneos pueden limitarse a un repositorio, un directorio específico o una rama.
- Claude razona sobre el código como una persona investigadora de seguridad: traza flujos de datos y la interacción entre archivos y módulos, en lugar de hacer pattern matching de firmas conocidas.
- Cada hallazgo incluye un confidence rating, severidad, impacto probable, pasos de reproducción y un parche dirigido que se puede abrir en Claude Code on the Web.
- Mejoras desde el preview limitado: escaneos programados, escaneos por directorio, descartes con motivo documentado, exportación a CSV/Markdown y webhooks hacia Slack, Jira y otras herramientas.
- Partners tecnológicos que embeben Opus 4.7: CrowdStrike, Microsoft Security, Palo Alto Networks, SentinelOne, Trend.ai, Wiz.
- Partners de servicios: Accenture, BCG, Deloitte, Infosys, PwC.
- Testimonios incluidos en el post: DoorDash, además de citas de un Staff Product Security Engineer, un Information Security Officer y dos Heads of Security.
- Claude Opus 4.7 incluye nuevos cyber safeguards; las organizaciones cuyo trabajo legítimo pueda activarlos pueden unirse al Cyber Verification Program.

## Recursos incluidos

- Skill: `skills/security-public-beta-rollout-guide/SKILL.md` — cuándo usar Claude Security, cómo acotar los escaneos, cómo interpretar los hallazgos y qué camino de adopción (directo / plataforma partner / partner de servicios) encaja con tu organización.
- Referencia: `skills/security-public-beta-rollout-guide/references/features-and-partners-from-post.md` — resumen textual de funcionalidades, flujo de escaneo, partners y citas de clientes.
- Ejemplos: `skills/security-public-beta-rollout-guide/examples/scan-and-triage-workflows.md` — flujos de scoping, programación y triage ilustrativos basados en el post.

## Fuente

Claude Security is now in public beta — Anthropic, 30 de abril de 2026: <https://claude.com/blog/claude-security-public-beta>
