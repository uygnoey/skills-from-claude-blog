[English](./frontier-models-at-scale.en.md) · [한국어](./frontier-models-at-scale.ko.md) · **Español** · [日本語](./frontier-models-at-scale.ja.md)

# Operar modelos de frontera de forma eficiente y segura a escala

Lecciones del equipo de AI Capabilities de Block sobre cómo dar modelos de frontera a toda una
organización de ingeniería sin perder el control del coste ni del riesgo.

## 1. Acceso y eficiencia
- Da a cualquier persona con un rol técnico acceso total a los modelos más capaces, para que los
  equipos trabajen siempre en el límite de lo posible.
- Haz que la eficiencia sea lo predeterminado: crea herramientas (el selector automático de Block) que
  sugieran el modelo adecuado para cada tarea y usa sistemas multiagente que combinen modelos grandes y
  pequeños.
- Reserva el modelo de frontera para problemas grandes (diseño de migraciones, orquestación a gran
  escala); deja que modelos más pequeños completen los detalles de los cambios de código.

## 2. Evalúa una cuadrícula, no un control deslizante
- Un modelo con esfuerzo xhigh puede comportarse como un modelo distinto del mismo modelo en medium.
- Para cada caso de uso, evalúa todos los modelos en todos los niveles de esfuerzo.
- Publica recomendaciones claras ("usa este modelo en high por defecto para este tipo de tarea"),
  automatízalas en las herramientas y deja que los expertos exploren más allá.

## 3. Herramientas para muchos agentes
- Las interfaces centradas en una sola conversación no dan abasto con decenas de agentes a la vez.
  Block usa Buzz, un espacio de trabajo de código abierto donde varias personas y muchos agentes
  trabajan en canales e hilos compartidos.

## 4. Salvaguardas por capas
| Capa | Lo que hace Block |
|---|---|
| Garantías humanas | Los merges a main, los despliegues a producción y los cambios de feature flags quedan en manos de personas; los cambios de agentes pasan controles de seguridad y luego dos personas aprueban el despliegue |
| Seguro por defecto | Estaciones de trabajo remotas; lista de permitidos de red en lugar de lista de bloqueados |
| Fuera del bucle del modelo | Controles baratos integrados en las interfaces de trabajo: regex y, cada vez más, clasificadores pequeños |
| Permitido a propósito | Abrir PR, revisar código, consultar logs y bases de datos analíticas |
| Salvaguardas del modelo | La negativa del propio modelo y los clasificadores de seguridad de Anthropic; Block evalúa que Claude se niega a "esquivar" la doble aprobación |

## 5. Mantener el ritmo del mantenimiento
Más PR implican más deuda técnica y más rápido. Ejecuta agentes que recorran el código a diario o cada
semana para encontrar qué limpiar y consolidar.

## 6. Convertir el conocimiento en algo organizativo
Las personas acumulan skills y contexto locales (p. ej., skills que permiten a alguien que no es
desarrollador front-end trabajar en un front-end web). Documenta lo que se aprende y llévalo a un
sistema compartido para que cada ejecución de un agente tenga el mejor contexto disponible.

## Fuente
- https://claude.com/resources/articles/how-block-orchestrates-claude-fable-across-thousands-of-pull-requests
