[English](./delegated-agent-security-architecture.en.md) · [한국어](./delegated-agent-security-architecture.ko.md) · **Español** · [日本語](./delegated-agent-security-architecture.ja.md)

# Arquitectura de seguridad de un agente delegado (Claude Duet)

Cómo protegió Anthropic la vista previa de investigación de Claude Duet, un agente que funciona de forma
continua en un ordenador en la nube y usa las apps que conecta el usuario (23 de octubre de 2026).

## Tres principios
1. Tratar la información con discreción.
2. Mantener el control en manos del usuario.
3. Mantener las credenciales lejos del agente.

Las protecciones se suman al entrenamiento de seguridad del modelo, a las salvaguardas de Claude Code y
Claude Managed Agents, y a nuevos controles para actuar en nombre del usuario.

## 1. Aprobación de acciones importantes
- Las acciones sensibles (enviar mensajes, pagar, borrar) muestran la acción, el destino y el contenido, y
  esperan aprobación.
- Una comprobación automática de intención, ampliada a partir del clasificador del modo automático de
  Claude Code, se ejecuta fuera del modelo, así que las instrucciones ocultas en una página no la afectan.
- Algunas acciones están prohibidas incluso con aprobación: operar con valores, mover dinero entre cuentas
  y acceder a la cuenta de otra persona.
- La frecuencia de aprobación se está calibrando para evitar la fatiga de aprobación.
- Las compras usan una tarjeta de un solo uso (Link de Stripe) limitada a un comercio y un importe.

## 2. Información tratada con discreción
- Un clasificador independiente revisa cada mensaje saliente.
- Nunca compartir: credenciales de acceso, números completos de tarjeta y de cuenta bancaria, números de
  documentos de identidad oficiales.
- Requiere consentimiento: otra información privada, como datos de salud o financieros; la propia
  petición del usuario cuenta como consentimiento.
- Los mensajes bloqueados pueden reescribirse sin el contenido sensible y mostrarse para su aprobación.

## 3. Visibilidad
- Una lista de tareas muestra lo hecho y lo que está en curso; el usuario puede reorientar la tarea.
- El historial y la memoria se conservan hasta que se borran o restablecen; eliminar la cuenta borra los
  datos almacenados.
- Desconectar una app detiene el acceso nuevo, pero lo aprendido permanece hasta restablecer la memoria.

## 4. Aislamiento de credenciales y navegador
- Contraseñas: se escriben en un formulario de la app, se cifran con una clave de un solo uso y la
  máquina del navegador las introduce en el sitio; el modelo nunca las ve. Está prevista una integración
  con 1Password.
- Tokens: el agente usa marcadores de posición; un proxy fuera de su máquina inserta los valores reales.
- Navegador: en su propia VM en la nube, manejado solo con comandos fijos; el código del sitio y las
  cookies se quedan allí, mientras que el texto de las páginas y las descargas vuelven al agente.
- El agente se identifica con un User-Agent propio e IP publicadas; algunos sitios optaron por bloquearlo.

## 5. Pruebas
- Tareas cotidianas en tres variantes: inocente, con instrucciones inyectadas y con tentación de
  extralimitarse.
- Equipos rojos para fugas de información, acciones no aprobadas y prompts maliciosos; modelo de amenazas
  de todo el sistema.
- Revisión del código fuente por una empresa externa de pruebas de penetración, con una segunda fase para
  el navegador en la nube y el formulario de acceso.
- Incluido en el programa público de recompensas por errores de Anthropic en HackerOne.

## Aún en evolución
La frecuencia de aprobación, los métodos de acceso y las comprobaciones de información sensible siguen
cambiando durante la vista previa. Los usuarios pueden informar de problemas directamente a Claude Duet.

Fuente: https://claude.com/resources/articles/claude-duet-safety-privacy-and-security
