[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Cómo nuestros partners están poniendo a Opus a trabajar en ciberseguridad

## ¿De qué trata este post?

Actualización de Anthropic del 21 de mayo de 2026 sobre los partners de tecnología y servicios que han lanzado ofertas defensivas de ciberseguridad sobre Claude Opus tras el beta público de Claude Security. El post organiza el trabajo de los partners en tres áreas — testing ofensivo continuo a escala de producción, cerrar la brecha entre encontrar y arreglar, y poner IA en producción con gobernanza — y comparte resultados concretos de Wiz, Palo Alto Networks (Unit 42), CrowdStrike, Accenture (Cyber.AI), TrendAI Vision One, Deloitte (CTEM sobre Deloitte Ascend) y PwC (Claude Native Cybersecurity). También nombra a BCG, Infosys y SentinelOne como otros partners construyendo sobre Opus.

## ¿Cuándo es útil?

- Cuando un comprador de seguridad necesita comparar las ofertas defensivas Opus ya en vivo con un catálogo estructurado en lugar de un recorrido de marketing.
- Cuando un CISO debe mapear qué oferta de partner encaja con cada necesidad interna: pentesting continuo, consolidación exposure→fix, o despliegue de IA gobernado.
- Cuando un partner de plataforma o servicios de seguridad quiere comparar su propia oferta contra lo que ahora es público.
- Cuando se preparan métricas para un memo de directorio (150 mil+ activos pentesteados por semana, un año de pentest en menos de 3 semanas, cobertura del 10% al 80%, escaneos de 3–5 días a menos de una hora, parcheo virtual hasta 96 días antes de un parche del vendor).

## Puntos clave

- **Tres categorías de trabajo de partners** que nombra el post: (1) testing ofensivo continuo a escala de producción, (2) cerrar la brecha entre encontrar y arreglar, (3) poner IA en producción de forma gobernada.
- **Wiz Red Agent** — atacante guiado por Opus que razona sobre webs y APIs; corre continuo sobre más de 150.000 activos productivos por semana y saca miles de hallazgos validados high/critical semanales con cero falsos positivos en producción de clientes.
- **Unit 42 Frontier AI Defense (Palo Alto Networks)** — análisis de exposición liderado por expertos más roadmap de fortalecimiento; en pruebas internas, un año de esfuerzo de pentest en menos de tres semanas.
- **CrowdStrike Frontier AI Readiness and Resilience Service** — combina Opus con AI Red Team Services y frameworks de agentes propios de CrowdStrike; orientado a la plataforma en que confía más del 60% del Fortune 500.
- **Cyber.AI (Accenture)** — bucle agéntico con Opus que cubre detección, priorización y remediación; en la propia infraestructura de Accenture llevó la cobertura del ~10% al 80%+ sobre 1.600 aplicaciones y 500.000+ APIs y redujo los escaneos de 3–5 días a menos de una hora.
- **TrendAI Vision One** — investigación asistida por Opus que alimenta parcheo virtual en 185 países; los hallazgos pasan también al TrendAI Zero Day Initiative para protección hasta 96 días antes del parche del vendor.
- **CTEM sobre Deloitte Ascend** — descubrimiento → validación → priorización → remediación en un mismo workflow, incluido diseño de contramedidas cuando no hay parche; el razonamiento de código y los tests de estabilidad automatizados de Opus reducen la remediación de días/semanas a horas.
- **PwC Claude Native Cybersecurity** — Secure AI Adoption (de sandbox a producción en semanas) y Scaled Frontier Defense (razonamiento agéntico de Opus dentro de gestión de vulnerabilidades, detección, ingeniería de seguridad y GRC existentes, con guardrails y auditabilidad).
- **Ecosistema creciente** — BCG, Infosys y SentinelOne también construyen sobre Opus; habrá más detalles cuando estén disponibles.
- **Sustrato común** — todas las ofertas dependen de las mismas capacidades de Opus: razonar sobre código, mapear exposiciones a riesgo real, y sostener workflows agénticos largos.

## Recursos incluidos

- `skills/frontier-defense-partner-evaluation/SKILL.md` — playbook para evaluar y armar shortlist de las ofertas defensivas Opus descritas en el post.
- `skills/frontier-defense-partner-evaluation/references/partner-catalog-from-post.md` — catálogo textual de partners, ofertas, afirmaciones y métricas citadas en el post.
- `skills/frontier-defense-partner-evaluation/examples/cisos-shortlist-walkthrough.md` — ejemplo trabajado de cómo un CISO arma su shortlist contra tres necesidades internas.

## Fuente

- [How our partners are putting Opus to work for cybersecurity](https://claude.com/blog/how-our-partners-are-putting-opus-to-work-for-cybersecurity) (blog de Anthropic, 21 de mayo de 2026)
