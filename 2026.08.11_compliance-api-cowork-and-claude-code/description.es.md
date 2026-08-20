[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un anuncio de que la **Compliance API ya cubre Claude Cowork y Claude Code**, en beta, para clientes de Claude Enterprise. Cowork queda cubierto en escritorio, web y móvil; Claude Code queda cubierto en la CLI y en la aplicación de escritorio. Ambos productos se leen a través de la misma interfaz de la Compliance API, de modo que los equipos de cumplimiento y seguridad extraen el contenido y los metadatos de sesión desde un solo lugar en vez de dos.

El post enumera qué contiene un registro de sesión — prompts y respuestas, contenido de las llamadas a herramientas (web y Model Context Protocol), y skills y artifacts capturados como texto de transcripción — además de los metadatos que lo acompañan: ID de usuario verificado y dirección de correo, ID de organización, ID de sesión e ID por mensaje, y marcas de tiempo. También indica qué queda fuera de la beta y confirma que no hace falta infraestructura nueva: la cobertura viene incluida con la Compliance API y usa tu Compliance Access Key existente, y las organizaciones que ya exportan datos de OpenTelemetry pueden seguir ejecutando ambos sistemas en paralelo.

## ¿Cuándo es útil?
- Cuando un equipo de cumplimiento o seguridad necesita las sesiones de Cowork y Claude Code en el mismo feed de auditoría que ya usa con la Compliance API.
- Cuando defines el alcance de un programa de retención, eDiscovery o investigación y necesitas saber exactamente qué superficies entran hoy en ese alcance.
- Cuando tienes que explicar a auditores o revisores qué campos se capturan por sesión y por mensaje.
- Cuando decides si mantener una exportación de OpenTelemetry en paralelo a la Compliance API.

## Puntos clave
- **Beta, solo Claude Enterprise.** La cobertura está disponible hoy y viene incluida con la Compliance API: sin derecho de uso aparte, y con tu Compliance Access Key existente.
- **Interfaz unificada.** El contenido y los metadatos de sesión de Cowork y Claude Code se extraen mediante la misma interfaz de la Compliance API.
- **Superficies cubiertas.** Cowork en escritorio, web y móvil; Claude Code en la CLI y en la aplicación de escritorio.
- **Contenido de sesión capturado.** Prompts y respuestas; contenido de llamadas a herramientas (web y Model Context Protocol); skills y artifacts, capturados como texto de transcripción.
- **Metadatos de sesión capturados.** ID de usuario verificado y dirección de correo, ID de organización, ID de sesión e ID por mensaje, y marcas de tiempo.
- **Excluido de la beta.** Claude Code en la web; Claude Code a través de Claude Platform; sesiones en Amazon Bedrock, Google Cloud Vertex AI o Microsoft Foundry.
- **Convive con OpenTelemetry.** Las organizaciones que ya exportan datos OTel pueden seguir ejecutando ambos sistemas a la vez, sin requisitos de infraestructura adicionales.

## Recursos incluidos
- `skills/compliance-session-coverage/SKILL.md` — define el alcance de una extracción por Compliance API sobre Cowork y Claude Code, y verifica la cobertura antes de depender de ella.
- `skills/compliance-session-coverage/references/coverage-matrix.md` — superficies cubiertas, superficies excluidas y todos los campos capturados que nombra el post.
- `skills/compliance-session-coverage/templates/coverage-verification-checklist.md` — una lista de verificación rellenable para confirmar el alcance antes de una auditoría o investigación.

## Fuente
- https://claude.com/blog/compliance-api-cowork-and-claude-code
