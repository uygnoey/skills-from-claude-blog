[English](./agentic-model-evaluation-and-governance.en.md) · [한국어](./agentic-model-evaluation-and-governance.ko.md) · **Español** · [日本語](./agentic-model-evaluation-and-governance.ja.md)

# Evaluar y gobernar modelos de frontera para trabajo agéntico

Metodología tomada del relato de Balyasny Asset Management sobre la adopción de Claude Fable 5 (septiembre de 2026).

## 1. Evaluar antes de activarlo
- Usar miles de tareas reales con resultados verificables de su propio dominio (BAM: renta variable, macro, materias primas).
- Probar el modelo solo **y** dentro de su arnés de agentes, con las mismas herramientas, archivos y requisitos que los usuarios.
- Evaluar planificación, selección y uso de herramientas, búsqueda y análisis de evidencias, recuperación de
  errores, verificación de resultados intermedios y entregables fundamentados. Vigilar errores numéricos,
  cobertura incompleta, conclusiones sin respaldo y problemas de recuperación de información.
- Resultado de BAM: 89,4 % para Fable frente a 86,1 % del modelo de producción anterior en el subconjunto relevante.

## 2. Desconfiar de las mejoras sorprendentes hasta verificarlas
Repetir la evaluación, revisar de forma independiente la tarea y la lógica de puntuación, y revisar con el
proveedor antes de aceptar un resultado que parece demasiado bueno.

## 3. Enrutar modelos según la evidencia
Desglosar los resultados por área y usarlos para elegir y enrutar modelos. Publicar pautas sobre qué modelo
usar según eficiencia y coste. Poner el modelo más fuerte en planificación y análisis, donde los errores se propagan.

## 4. Poner los controles alrededor del modelo
| Control | Propósito |
|---|---|
| Límites de datos aprobados | El agente solo ve datos autorizados |
| Mínimo privilegio | Limitado al usuario y la tarea |
| Permisos por herramienta | Limita las acciones posibles |
| Registro y trazabilidad | Detectar y rastrear problemas |
| Revisión humana de resultados relevantes | Nadie depende de trabajo sin revisar |
| Vías de escalado | Los casos límite llegan a una persona |
| Pruebas adversarias y de fallos | Antes de ampliar el acceso |

La capacidad no otorga autoridad: un modelo mejor no recibe más acceso ni puede concedérselo a sí mismo.
El juicio de inversión (o de negocio) sigue en manos de personas.

## 5. Desplegar mediante una plataforma gobernada
Los agentes de BAMAgent planifican, usan sistemas internos aprobados, ejecutan el análisis, verifican los
resultados intermedios y devuelven un entregable revisable. El arnés (diseño del flujo, acceso a datos y
herramientas, contexto de recuperación, permisos, monitorización, revisión humana) y el razonamiento del
modelo son ambos necesarios para la calidad de producción.

## 6. Consejos para otras firmas
- Invertir pronto en evaluaciones basadas en tareas reales y verificables, y usarlas para elegir y enrutar modelos.
- Probar en el mismo entorno y con las mismas herramientas que tendrán los usuarios.
- Tratar la seguridad como una cuestión del modelo operativo; los controles van alrededor del modelo.
- Definir una estrategia de agentes alojados que permita a la empresa aplicar sus políticas y maximizar el valor de los agentes.
- Preguntarse si hay una forma mejor de lograr el resultado, no solo cómo automatizar el proceso actual.

Fuente: https://claude.com/resources/articles/working-at-the-frontier-how-balyasny-asset-management-evaluates-and-governs-claude-fable-5
