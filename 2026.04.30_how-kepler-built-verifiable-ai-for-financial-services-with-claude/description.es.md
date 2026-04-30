[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un caso de estudio sobre Kepler Finance, una plataforma de investigación para servicios financieros que combina a Claude para la interpretación y el razonamiento con infraestructura determinista que verifica cada cifra contra el documento fuente exacto, la página y la partida.

## ¿Cuándo es útil?
Cuando necesitas patrones para construir sistemas de IA auditables y regulados (especialmente en finanzas) que deben ser verificables y responsables, y para diseñar arquitecturas que separen el razonamiento probabilístico del cómputo y la procedencia demostrablemente correctos.

## Puntos clave
- Kepler combina el razonamiento de Claude con una capa determinista de confianza/verificación (búsqueda, cómputo y ensamblaje) para que cada respuesta sea rastreable y auditable.
- El sistema descompone el trabajo en pipelines por etapas y asigna modelos a cada etapa (razonamiento complejo vs. tareas acotadas de alto rendimiento).
- La ingeniería de contenido (conocimiento estructurado, definiciones y límites) más pipelines de evaluación automatizada ayudan a mantener la fiabilidad ante cambios de prompts, modelos o contexto.
- Se enfatiza diseñar procedencia, registro de auditoría y seguridad desde el primer día.

## Recursos incluidos
- Ninguno (el post describe arquitectura y prácticas; no incluye prompts completos, scripts ni JSON de hooks).

## Fuente
- https://claude.com/blog/how-kepler-built-verifiable-ai-for-financial-services-with-claude
