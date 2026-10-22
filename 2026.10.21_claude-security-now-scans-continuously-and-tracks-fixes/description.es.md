[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Una actualización de Claude Security, ahora en beta pública para Claude Enterprise. En lugar de
esperar a que alguien inicie un escaneo, sigue los repositorios a medida que cambia el código, registra
qué hallazgos se corrigen y usa lo que el equipo le cuenta sobre su entorno para decidir qué importa.

## ¿Cuándo es útil?
- Cuando un equipo de seguridad Enterprise quiere escaneos siempre actualizados sin programarlos.
- Cuando los hallazgos necesitan contexto del equipo (despliegue, políticas, política de riesgo).
- Cuando los ingenieros quieren clasificar y corregir hallazgos en Claude Code o enviarlos a sus
  herramientas.

## Puntos clave
- Monitoreo continuo: escaneo base profundo y luego escaneos regulares de los cambios según su riesgo
  y complejidad. Conexión mediante la app de GitHub de Claude (incl. GitHub Enterprise Server) o un
  token de GitLab u otro proveedor Git; un proyecto puede abarcar varios repositorios para detectar
  problemas entre servicios.
- Seguimiento de correcciones: los hallazgos se marcan como corregidos cuando llega la corrección (en
  Claude Code o en otro lugar) y se reabren solos si el problema reaparece.
- Base de conocimiento por proyecto y un modelo de amenazas generado y editable que los escaneos
  posteriores usan para decidir qué señalar y qué omitir.
- Cada hallazgo incluye una severidad evaluada frente al modelo de amenazas y una explicación de la
  ruta de ataque, a veces con diagrama.
- API (proyectos, hallazgos, resolver/reabrir, gestión de repositorios), tokens de acceso personal
  limitados a los permisos del usuario, webhooks para nuevos hallazgos y un conector MCP en Claude.ai y
  Claude Code.
- Control de acceso por roles: ver proyectos, clasificar hallazgos y crear proyectos.
- Funciona con toda la familia de modelos, incluido Claude Mythos, sin acceso al Cyber Verification
  Program. 25.000 USD en créditos gratuitos al mes durante dos meses (uso hasta el 31 de diciembre de
  2026; términos en el Help Center).

## Recursos incluidos
- Skill: `continuous-security-scanning` — activación, roles, proyectos, base de conocimiento, modelo
  de amenazas, clasificación, seguimiento de correcciones e integraciones
  (`references/feature-reference.md`, `templates/project-knowledge-base.md`).

## Fuente
- https://claude.com/resources/articles/claude-security-now-scans-continuously-and-tracks-fixes
