[English](./inline-dlp-for-claude-enterprise.en.md) · [한국어](./inline-dlp-for-claude-enterprise.ko.md) · **Español** · [日本語](./inline-dlp-for-claude-enterprise.ja.md)

# DLP en línea para Claude Enterprise

Guía de despliegue de **inference hooks**: prevención de pérdida de datos en tiempo real que inspecciona los prompts y las respuestas de las llamadas a herramientas antes de que el modelo actúe sobre ellos.

## El hueco que cierra

Los equipos de seguridad suelen sostener una regla sobre el movimiento de datos: todo canal por el que un empleado pueda mover información sensible debe pasar por un punto de inspección que el equipo controla. El correo tiene uno. Los endpoints tienen uno. El tráfico web tiene uno.

Las superficies de IA no lo tenían, al menos no de forma nativa ni en todas partes. Dentro de un agente de código era posible aplicar controles mediante los hooks del lado del cliente de ese agente, pero eso cubre un solo producto, se configura en el cliente y deja el chat y los espacios de trabajo agénticos fuera del perímetro.

Inference hooks convierte el punto de inspección en una propiedad de la organización y no de un producto.

## Arquitectura

```
Usuario / agente
     │
     │  solicitud de inferencia
     ▼
Claude Enterprise ──── WebSocket firmado ────▶ Tu servidor de seguridad
     │                                              │
     │ ◀──────────── veredicto allow / deny ────────┘
     ▼
El modelo genera
     │
     │  llamada a herramienta (conector MCP / skill / plugin)
     ▼
Respuesta ──── misma comprobación ────▶ veredicto ────▶ el modelo la ve (o no)
```

Dos propiedades determinan todo lo demás en el despliegue:

1. **Es síncrono.** La generación espera un veredicto. La latencia de tu servidor pasa a ser la latencia de cada usuario.
2. **Ocurre antes de la generación.** La inspección sucede antes de que el modelo lea el contenido, no después de que produzca una salida. Eso es lo que la convierte en prevención y no en detección.

## Qué se inspecciona

| Punto | Contenido | Por qué importa |
|---|---|---|
| Antes de generar | El prompt y su contexto | La vía directa por la que una persona mueve datos hacia el modelo |
| Antes de que el modelo lea un resultado de herramienta | La respuesta de la llamada | Los conectores pueden traer contenido restringido sin que nadie lo escriba |

La vía de respuesta de herramientas merece atención específica en el diseño. Cualquier conector con acceso de lectura a un repositorio documental, un sistema de tickets o una base de datos es una ruta por la que contenido clasificado entra automáticamente en la ventana de contexto.

## Forma del despliegue

### Apunta al servidor que ya tienes

El protocolo está basado en webhooks con un esquema publicado. En la práctica esto significa que el punto de decisión suele ser una plataforma existente —Netskope, Palo Alto Networks, Proofpoint, Zscaler o un servidor de seguridad de IA construido internamente— y no algo creado para esta función. La reutilización es el camino recomendado: un solo corpus de políticas, un solo rastro de auditoría, un solo lugar donde se mantienen las reglas.

Para los proveedores de seguridad, la misma propiedad funciona en sentido contrario: se construye una integración contra el esquema documentado y los clientes pueden apuntar su organización a esa plataforma mediante configuración.

### Configura una vez a nivel de organización

Un solo interruptor cubre las superficies de Claude Enterprise, incluidos el chat, Claude Code, Claude Cowork y las llamadas a herramientas hechas a través de conectores MCP, skills y plugins. No hay integración por producto ni un agente aparte que desplegar junto a cada uno.

### Escala con intención

Los controles disponibles existen porque activar la aplicación en línea para todo el mundo a la vez es la forma habitual de arruinar un despliegue:

- **Modo sombra** — siempre permitir, mientras el servidor sigue evaluando. Es la fase de medición y donde se afinan las reglas.
- **Exclusiones por rol** — mantiene fuera del control a los roles de emergencia y administración, que de otro modo podrían quedar bloqueados por el propio mecanismo que administran.
- **Despliegue por porcentaje** — expone a una fracción de la población, de modo que una regla mala sea un incidente contenido y no una caída general.
- **Política de fallo y tiempos de espera** — decide de forma explícita qué ocurre cuando el servidor no responde a tiempo.

## La decisión sobre la política de fallo

Es la decisión que más conviene tomar conscientemente en lugar de heredarla de un valor por defecto.

**Fallo cerrado.** Sin veredicto no hay inferencia. La cobertura es completa; una caída del servidor de políticas es una caída de la IA en toda la organización. Adecuado cuando la sensibilidad de los datos domina.

**Fallo abierto.** Si no llega veredicto dentro del tiempo de espera, la solicitud continúa. Se preserva la disponibilidad, pero cada evento de fallo abierto es una solicitud sin inspeccionar. Adecuado cuando la disponibilidad domina, y solo si esos eventos se registran, se alertan y se revisan; de lo contrario el hueco es invisible.

Se elija lo que se elija, el valor del tiempo de espera forma parte de la decisión. Un tiempo generoso con fallo cerrado convierte un servidor lento en un producto lento; un tiempo ajustado con fallo abierto convierte un servidor lento en huecos silenciosos.

## Consecuencias operativas

- **El servidor de políticas pasa a ser una dependencia de producción.** Su planificación de capacidad, su guardia y sus ventanas de mantenimiento afectan ahora a todas las superficies de IA.
- **Cada regla cuesta latencia en cada solicitud.** Las reglas que no tratan sobre pérdida de datos pertenecen a otro sitio.
- **Las denegaciones necesitan una salida humana.** Un bloqueo sin camino hacia adelante empuja el trabajo a canales no supervisados: justo el modo de fallo que el control pretendía evitar.
- **Las afirmaciones de cobertura necesitan evidencia.** Conserva el historial de configuración: estado del modo sombra, porcentaje, exclusiones, política de fallo y tiempo de espera, cada uno con fecha y motivo.

## Precaución con el nombre

"Inference hooks" y los hooks de ciclo de vida de Claude Code comparten una palabra y poco más:

| | Inference hooks | Hooks de Claude Code |
|---|---|---|
| Dónde se ejecuta | Lado servidor, en la ruta de inferencia | Lado cliente, en el agente de código |
| Quién lo configura | Administrador de la organización | Persona desarrolladora o equipo, en la configuración |
| Qué controla | Prompts y respuestas de herramientas en varias superficies | Eventos de ciclo de vida como PreToolUse y PostToolUse |
| Alcance | Toda la organización | Una instalación del agente |

Son complementarios, no alternativos. Una organización puede usar ambos.

## Cómo empezar

Inference hooks está disponible en beta para clientes de Claude Enterprise. Los detalles de configuración, el esquema del webhook y la disponibilidad actual están en la documentación de la plataforma; confírmalos ahí antes de comprometer una fecha de despliegue.

## Fuente

- https://claude.com/blog/claude-enterprise-inference-hooks
