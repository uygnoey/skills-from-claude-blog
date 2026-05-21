[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Claude ahora se integra con más herramientas de seguridad y cumplimiento

## ¿De qué trata este post?

Anuncio de Anthropic del 21 de mayo de 2026 sobre **28 nuevas integraciones de seguridad y cumplimiento** construidas sobre la **Claude Compliance API**, para que los equipos de IT y seguridad gobiernen Claude en Claude Enterprise y la Plataforma Claude del mismo modo que gobiernan cualquier otra aplicación de su stack. El post explica qué expone la API, lista a todos los partners de lanzamiento y orienta a clientes y partners en sus próximos pasos.

## ¿Cuándo es útil?

- Cuando un equipo de IT/seguridad evalúa cómo conectar Claude a sus stacks de DLP, SASE, SIEM, identidad, eDiscovery, AI-SPM u observabilidad de IA.
- Cuando hay que decidir si extender un vendor de seguridad/cumplimiento existente para cubrir Claude en lugar de construir una integración propia.
- Cuando una plataforma vendor de seguridad/cumplimiento se plantea entrar a la red de integraciones.
- Cuando se prepara la historia de gobernanza para que CISO y CRO firmen el rollout de Claude Enterprise o la Plataforma Claude.

## Puntos clave

- La Compliance API es el sustrato de las 28 integraciones.
- **Dos tipos de datos** que la API expone de forma programática a equipos enterprise:
  - **Contenido conversacional de Claude Enterprise** — chats, archivos subidos y proyectos — para aplicar las mismas políticas de seguridad, monitoreo y DLP que ya usan en otras apps de trabajo.
  - **Eventos de actividad en Claude Enterprise y la Plataforma Claude** — logins de usuario, acciones de admin y cambios de configuración — para una vista unificada del uso.
- **Categorías cubiertas** por las 28 integraciones: DLP, SASE, seguridad de datos, SIEM y operaciones de seguridad, identidad, eDiscovery, gestión de postura de seguridad de IA, e infraestructura de observabilidad/telemetría de IA.
- **28 partners de lanzamiento**: Cloudflare, Cribl, CrowdStrike, Cyera, Datadog, Forcepoint, Fortinet, Geordie AI, IBM Guardium, Microsoft Purview, Mimecast, Netskope, Okta, Palo Alto Networks, Proofpoint, Relativity, ReliaQuest, Rubrik, SailPoint, Smarsh, Snyk, Sumo Logic, Tenable, Theta Lake, Trellix, Varonis, Wiz (ahora parte de Google Cloud) y Zscaler.
- **Onboarding cliente** — conectar y configurar la instancia de Claude; los datos fluyen a los dashboards y workflows de alerta que el cliente ya usa.
- **Onboarding partner** — plataformas de seguridad/cumplimiento/IT que hayan construido una integración con la Compliance API pueden aplicar para unirse a la red.

## Recursos incluidos

- `skills/governance-via-compliance-api/SKILL.md` — playbook para elegir la integración de Compliance API que encaja con un stack existente y diseñar la gobernanza de Claude.
- `skills/governance-via-compliance-api/references/launch-partners-by-category.md` — catálogo textual de partners agrupado por las categorías nombradas en el post.
- `skills/governance-via-compliance-api/examples/dlp-and-siem-wiring.md` — ejemplo trabajado conectando cobertura de DLP y SIEM sobre Claude Enterprise y la Plataforma Claude vía la Compliance API.

## Fuente

- [Claude now works with more security and compliance tools](https://claude.com/blog/compliance-api-security-partners) (blog de Anthropic, 21 de mayo de 2026)
