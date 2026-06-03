[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# How Anthropic enables self-service data analytics with Claude

## ¿De qué trata este post?
Este post explica cómo Anthropic usa Claude para automatizar la mayoría de las solicitudes internas de analítica de negocio, y por qué la precisión en analítica es principalmente un problema de **contexto, recuperación (retrieval) y verificación**, no solo de generación de SQL.

## ¿Cuándo es útil?
Es útil cuando estás construyendo un flujo de trabajo de analítica con agentes (un “copiloto” de analítica) que debe responder preguntas sobre un data warehouse de forma confiable, con defensas frente a entidades ambiguas, datos desactualizados y falta de contexto recuperado.

## Puntos clave
- La analítica difiere del desarrollo de software: a menudo hay una única respuesta correcta asociada a una entidad específica y actual en el modelo de datos.
- Tres modos de fallo dominantes: (1) ambigüedad concepto–entidad, (2) datos desactualizados (staleness) y (3) fallo de recuperación (retrieval).
- El enfoque de Anthropic combina buenas bases de datos, fuentes de verdad explícitas, conocimiento procedimental codificado como skills y validación (evaluaciones offline + monitorización online).
- El apéndice incluye un esqueleto concreto de “skill de warehouse” y un esqueleto de documento de referencia para tablas por dominio.

## Recursos incluidos
- Un esqueleto reutilizable de “skill de warehouse” (apto para `skills/<skill-name>/SKILL.md`).
- Un esqueleto reutilizable de documento de referencia (apto para `skills/<skill-name>/references/*.md`).

## Fuente
- https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude
