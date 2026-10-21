[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Una entrevista con Bradley Axen, responsable de AI Capabilities en Block (Square, Cash App), sobre cómo
Block evalúa modelos, cómo Claude Fable 5 orquesta migraciones de código a escala de toda la empresa
con miles de pull requests, cómo Block orienta a sus empleados hacia un uso eficiente de los modelos y
en qué salvaguardas se apoya cuando todo el personal técnico tiene acceso a modelos de frontera.

## ¿Cuándo es útil?
- Al planificar una migración de cientos o miles de PR en muchos repositorios.
- Al decidir qué modelo y qué nivel de esfuerzo usar para un tipo de tarea de agente.
- Al diseñar barreras de protección para agentes que escriben código en una organización grande.

## Puntos clave
- Orquestación por niveles: una persona dirige; Fable hace el diseño inicial (modelos de datos,
  especificaciones de API, algoritmos) y dirige hasta decenas de modelos más pequeños (Opus, Sonnet) que
  editan archivos y ejecutan pruebas. Los primeros resultados muestran más tokens desplazándose a los
  modelos trabajadores sin pérdida de calidad; en una migración se pueden fusionar mil PR orquestados
  por Fable.
- Block lo ejecuta en Buzz, su espacio de trabajo de código abierto donde personas y agentes comparten
  canales e hilos.
- Los agentes recorren a diario o cada semana un código base de alrededor de un millón de líneas para
  encontrar deuda técnica que limpiar y consolidar.
- Eficiencia: acceso total a modelos de frontera para perfiles técnicos y un selector automático de
  modelos. Cada caso de uso se evalúa con todos los modelos y todos los niveles de esfuerzo: una
  cuadrícula, no un control deslizante.
- Salvaguardas: los merges a main, los despliegues a producción y los feature flags quedan en manos de
  personas; los cambios de los agentes pasan controles de seguridad y requieren dos aprobaciones
  humanas. Estaciones de trabajo remotas, listas de permitidos de red y controles baratos fuera del
  bucle del modelo (regex, clasificadores pequeños). Abrir PR, revisar código y consultar logs y bases de
  datos analíticas se permite a propósito. Claude se niega a eludir la doble aprobación, y Block lo
  evalúa.
- La madurez organizativa consiste en recordar el contexto aprendido a nivel de sistema, no individual.

## Recursos incluidos
- Skill: `orchestrated-code-migrations` — migraciones con orquestador y trabajadores por niveles,
  selección de modelo × esfuerzo (`templates/model-effort-grid.md`) y salvaguardas
  (`references/safeguards.md`).
- Agentes: `migration-orchestrator` y `migration-worker`, los dos roles descritos en el post.
- Guía: "Operar modelos de frontera de forma eficiente y segura a escala" en cuatro idiomas.

## Fuente
- https://claude.com/resources/articles/how-block-orchestrates-claude-fable-across-thousands-of-pull-requests
