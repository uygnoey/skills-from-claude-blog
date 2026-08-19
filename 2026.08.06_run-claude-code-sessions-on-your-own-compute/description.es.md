[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un anuncio de producto: los **entornos autoalojados** (self-hosted environments) para Claude Code entran en beta pública. En lugar de ejecutar las sesiones del agente sobre infraestructura gestionada por Anthropic, una organización puede ejecutarlas en máquinas que aprovisiona ella misma: dentro de su propia red, junto a sus servicios internos, sus cadenas de herramientas y sus controles de seguridad. Las sesiones iniciadas desde la web, el móvil, el escritorio o una rutina se enrutan todas al mismo entorno.

El post es explícito en que esta **no** es la recomendación por defecto. Para la mayoría de las empresas se sigue recomendando la oferta gestionada por su simplicidad operativa; el autoalojamiento es para equipos cuyos requisitos de red, herramientas o cumplimiento hacen que ejecutar el agente en su propia infraestructura sea un requisito duro, y viene acompañado de un compromiso de personal.

## ¿Cuándo es útil?
- Cuando las sesiones del agente deben alcanzar servicios internos, bases de datos o registros de paquetes que no están expuestos a la internet pública.
- Cuando cada sesión debe arrancar con los compiladores, SDK y CLI internos de la empresa ya instalados.
- Cuando el código fuente y los artefactos de compilación deben permanecer en infraestructura que controla la organización.
- Cuando hay que decidir entre la oferta gestionada y el autoalojamiento, y se necesita ver el compromiso con claridad —incluido **qué no** se queda en tu infraestructura— antes de asignar un equipo de plataforma.

## Puntos clave
- **Beta pública, solo planes Team y Enterprise.** Los entornos autoalojados están desactivados por defecto y no están disponibles para organizaciones que usan ZDR.
- **Qué se queda en local y qué no.** Los checkouts del repositorio, los artefactos de compilación, los secretos y cualquier archivo que una sesión cree o modifique permanecen en la infraestructura que aprovisionas. La conversación en sí —prompts, respuestas y resultados de herramientas, que pueden incluir código que Claude lee— sí se envía a Anthropic para la inferencia, y la transcripción de la sesión se almacena para poder retomarla desde cualquier superficie.
- **Los runners son la unidad de ejecución.** Despliegas procesos runner de larga vida; cada uno recoge sesiones e inicia un proceso de Claude Code por sesión.
- **Dos modos de runner.** *Fijo*: mantienes un número determinado de runners activos y las sesiones se distribuyen entre ellos. *Bajo demanda*: un orquestador vigila la cola, arranca runners a medida que llegan sesiones y los detiene al terminar el trabajo, de modo que la capacidad sigue a la demanda.
- **El aislamiento es por sesión, no por runner.** Un runner puede atender varias sesiones, pero cada sesión obtiene su propio checkout, así que el trabajo queda separado entre desarrolladores y cuentas.
- **Un entorno, todas las superficies.** Se configura una vez y las sesiones de todas las superficies compatibles se enrutan hacia él.
- **No es lo mismo que Remote Control.** Remote Control continúa desde el móvil o el navegador una sesión que corre en la máquina del propio desarrollador; termina cuando esa máquina se detiene y está ligada al usuario que ejecutó `claude`. Los entornos autoalojados corren sobre infraestructura compartida que opera un equipo de plataforma y los puede usar cualquier usuario.
- **Alguien tiene que hacerse cargo.** Cuenta con que un equipo de plataforma, de experiencia de desarrollo o de productividad de desarrollo asuma la puesta en marcha y la operación continua: construir y mantener la imagen del runner, actualizar los runners y operar el orquestador si eliges el modo bajo demanda.

## Recursos incluidos
- `skills/self-hosted-coding-environments/SKILL.md` — cómo decidir, dimensionar y operar un entorno autoalojado.
- `skills/self-hosted-coding-environments/references/decision-criteria.md` — gestionado frente a autoalojado, y los requisitos de elegibilidad.
- `skills/self-hosted-coding-environments/references/architecture.md` — runners, los dos modos, aislamiento de sesiones y la frontera de datos.
- `skills/self-hosted-coding-environments/templates/rollout-checklist.md` — lista de verificación de propiedad y despliegue derivada del post.
- `guides/self-hosted-session-environments.{en,ko,es,ja}.md` — el mismo material como guía en cuatro idiomas.

## Fuente
- https://claude.com/blog/run-claude-code-sessions-on-your-own-compute (6 de agosto de 2026)
- Detalles de implementación: https://code.claude.com/docs/en/self-hosted-environments
