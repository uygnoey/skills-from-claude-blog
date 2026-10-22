[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un ingeniero de Anthropic explica cómo la programación agéntica multiplicó por ~25 los trabajos de CI
en seis meses, cómo el servicio de análisis de impacto de pruebas (selección de pruebas) estuvo a punto
de convertirse en el cuello de botella y por qué sustituyeron tres parches cada vez más efímeros por un
rediseño sin estado. La lección central: planifica siempre para lo exponencial.

## ¿Cuándo es útil?
- Cuando los PR escritos por agentes hacen crecer la CI más rápido que la plantilla.
- Cuando un servicio de selección de pruebas se retrasa, genera alertas o llega a su límite de memoria.
- Cuando dudas entre otro parche rápido y un rediseño, o al dimensionar un nuevo servicio de CI.

## Puntos clave
- Los ingenieros publican ~8 veces más código por trimestre que en 2021-2025 y Claude escribe ~80 %;
  las pruebas crecieron ~10 veces y los trabajos de CI ~25 veces en seis meses.
- El servicio tiene un listener (registra resultados) y un selector (elige pruebas por PR). El retraso
  del listener produce selección obsoleta: fallos compartidos, bloqueos por pruebas inestables y pruebas
  nuevas o corregidas que no se ejecutan.
- La v0 era un proceso con un único escritor. Cada parche duró menos: máquina más grande (~70 días),
  sharding por paquete (29 días), reinicios diarios (< 1 día).
- Una sesión de larga duración en Claude Tag vigilaba el retraso (alerta a 50.000 trabajos) y defendía
  una reforma completa.
- Rediseño: estado en un almacén en memoria, workers listener sin estado que añaden a un journal y un
  consumidor que lo agrega en historial por prueba cada pocos segundos. Un ingeniero, tres semanas;
  Claude lo ajustó de forma mayormente autónoma; la cola se mantuvo plana.
- Consejos: asume 25 veces la carga en dos trimestres, diseña la v0 para 10-20 veces si el presupuesto
  lo permite, saca el estado del proceso, evita servicios críticos de instancia única e instrumenta
  para que los trabajos que entran igualen a los que salen.

## Recursos incluidos
- Skill: `agent-scale-ci-test-selection` — modelo listener/selector, coste del retraso, vida útil de
  los parches, rediseño sin estado y reglas de planificación (`references/scaling-timeline.md`,
  `templates/ci-scaling-review.md`).
- Guía: `stateless-test-impact-analysis` (en/ko/es/ja) — arquitectura y reglas de planificación.

## Fuente
- https://claude.com/resources/articles/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic
