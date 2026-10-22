[English](./stateless-test-impact-analysis.en.md) · [한국어](./stateless-test-impact-analysis.ko.md) · **Español** · [日本語](./stateless-test-impact-analysis.ja.md)

# Análisis de impacto de pruebas sin estado para CI a escala de agentes

Guía de arquitectura basada en cómo Anthropic rediseñó su servicio de selección de pruebas después de
que los trabajos de CI crecieran unas 25 veces en seis meses.

## Por qué los agentes tensionan la CI
- Los ingenieros publican ~8 veces más código por trimestre que en 2021-2025; Claude escribe ~80 % y
  ayuda a revisar y aprobar PR. Cuando la revisión se acelera, la presión pasa a la CI.
- Las pruebas crecieron ~10 veces; los trabajos de CI, ~25 veces en seis meses.
- Los agentes prefieren PR más pequeños y granulares y hacen push de noche y en fines de semana, lo que
  eleva el nivel mínimo de actividad, mientras las aprobaciones humanas mantienen picos.

## El modelo listener/selector
| Componente | Función |
|---|---|
| Listener | Registra los resultados de cada ejecución de CI |
| Selector | Lee el historial y elige las pruebas de cada PR (rendimiento pasado, relevancia del paquete) |

Si el listener se retrasa, la selección usa datos obsoletos: un cambio malo rompe pruebas para todos,
dependencias inestables bloquean merges y las pruebas nuevas o corregidas no se ejecutan. 20 minutos de
retraso pueden ser decenas de miles de actualizaciones sin aplicar.

## Por qué la v0 dejó de escalar
Un único proceso guardaba el historial por prueba y necesitaba un solo escritor, así que no podía
particionarse horizontalmente. Cada parche duró menos: máquina más grande (~70 días), sharding por
paquete (29 días), reinicios diarios (< 1 día).

## El rediseño
```
Ejecuciones CI ──▶ workers listener sin estado ──append──▶ journal (almacén en memoria)
                                                             │ cada pocos segundos
                                                             ▼
                                          consumidor agrega historial por prueba
                                                             │
PR abierto ──▶ selector ──────── lee historial ◀─────────────┘
```
- Cualquier worker procesa cualquier resultado y no retiene nada en memoria: escala horizontalmente.
- Cuesta más operarlo que el singleton, pero es mucho más fácil de escalar y perfilar en memoria.
- Un ingeniero, tres semanas; Claude ajustó el tamaño del journal y el número de workers de forma
  mayormente autónoma.
- Tras el cambio y el ajuste, el máximo horario de eventos en cola se mantuvo plano.

## Reglas de planificación
1. Supón una carga 25 veces mayor en dos trimestres, tanto si construyes como si compras.
2. Si el presupuesto lo permite, diseña la v0 para 10-20 veces la escala percibida.
3. Mantén el estado fuera del proceso desde el principio.
4. Evita servicios críticos de instancia única salvo que puedas medirlos y hacer canary de los cambios.
5. Instrumenta los servicios como ojos y oídos de Claude; asegúrate de que los trabajos de CI que
   entran sean iguales a los que salen.
6. Usa una sesión de agente de larga duración para vigilar el retraso (Anthropic alertaba a 50.000
   trabajos) y conservar el contexto entre incidentes.

## Fuente
- https://claude.com/resources/articles/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic
