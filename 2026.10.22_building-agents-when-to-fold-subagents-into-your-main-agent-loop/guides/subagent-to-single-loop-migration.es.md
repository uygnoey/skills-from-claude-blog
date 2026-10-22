[English](./subagent-to-single-loop-migration.en.md) · [한국어](./subagent-to-single-loop-migration.ko.md) · **Español** · [日本語](./subagent-to-single-loop-migration.ja.md)

# De subagentes a un único bucle de agente

Resumen metodológico de la guía de Anthropic para integrar subagentes en el bucle del agente principal.

## 1. Por qué importa
Las grandes organizaciones suelen dejar que cada equipo construya su propio agente y añaden un
orquestador central. Eso provoca pérdida de contexto entre agentes, proliferación de subagentes, un
"Frankenprompt" de reglas contradictorias, evals locales que nadie posee y latencia adicional. Un único
bucle con skills y herramientas de divulgación progresiva conserva el contexto compartido, evita el
exceso de contexto y aprovecha modelos más capaces.

## 2. Cuándo siguen teniendo sentido los subagentes
- Degradación medible por exceso de contexto en un único bucle.
- Tareas paralelas que necesitan ventanas de contexto nuevas y desechables.
- Problemas para elegir herramientas o instrucciones contradictorias en un mismo system prompt.
Si optas por multiagente, empieza por el patrón más simple y divide por contexto, no por tipo de problema.

## 3. Arquitectura objetivo
Un modelo y una ventana de contexto; un bucle abierto de herramientas con presupuestos de turnos y coste
y compuertas de escritura; lotes de herramientas en paralelo cuyos resultados en bruto vuelven al mismo
modelo; un plan escrito en contexto y revisado según llegan resultados; el procedimiento en skills, los
límites estrictos y las consultas a mitad de conversación en herramientas; código solo para cargas
baratas y casi siempre relevantes y para trabajo mecánico dentro de las herramientas.

## 4. Etapas de migración
1. **Evals de finalización de tareas**: conjunto compartido de extremo a extremo (equipo central) más
   conjuntos por skill; 10 ejemplos de referencia para empezar; rúbrica, precisión de enrutamiento y
   luego selección de skill/herramienta.
2. **Fusionar agentes de dominio** que se encadenan, comparten datos o se llaman juntos, empezando por
   los más usados.
3. **Invocar como herramientas los subagentes que se mantienen**: esquema de respuesta compartido; el
   agente principal verifica y conserva la conversación; traspaso completo solo si el subagente debe
   hablar con el usuario.
4. **Integrar un subagente cada vez**: prompts a skills, llamadas API a herramientas MCP; compara las
   tareas que cambian; ejecuta cada tarea más de una vez; mantén el subagente solo si la versión
   integrada puntúa peor.

## 5. Modelo de propiedad
| Activo | Responsable | Regla práctica |
|---|---|---|
| System prompt, evals de extremo a extremo | Pequeño equipo central | Revisa cada nueva skill, herramienta y eval |
| Skills | DRI del equipo | Distintas, bien hechas, con evals |
| Herramientas MCP | Equipos de dominio | Agrupadas por intención; menos de ~30-50 definiciones; búsqueda de herramientas con carga diferida |
| Bases de conocimiento | Equipos de dominio | Tras una herramienta de búsqueda o como archivos de referencia de una skill |

## 6. Herramientas
`/claude-api build-eval`, `/claude-api prompt-audit`, `/claude-api hillclimb`,
`/claude-api cost-optimize`, `/skill-creator`, `/skill-doctor` y el kit de migración (con una demo
sobre un sistema simulado).

## 7. Principio
Mide, cambia una cosa cada vez y conserva lo que funcione.

Fuente: https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
