[English](./self-hosted-session-environments.en.md) · [한국어](./self-hosted-session-environments.ko.md) · **Español** · [日本語](./self-hosted-session-environments.ja.md)

# Ejecutar sesiones de codificación con agentes en tu propia infraestructura

Guía de despliegue derivada del anuncio del 6 de agosto de 2026 sobre los entornos autoalojados para Claude Code (beta pública).

## Qué cambia

Por defecto, las sesiones de codificación con agentes se ejecutan sobre infraestructura gestionada por el proveedor. Con un entorno autoalojado se ejecutan en máquinas que aprovisiona tu organización: dentro de tu red, junto a tus servicios internos, tus cadenas de herramientas y tus controles de seguridad. Las sesiones iniciadas desde la web, el móvil, el escritorio o una rutina se enrutan todas a ese mismo entorno.

## Decide primero: ¿es realmente necesario?

El anuncio recomienda la oferta gestionada para la mayoría de las empresas, porque no hay infraestructura que operar ni mantener. El autoalojamiento existe para equipos cuyos requisitos de red, herramientas o cumplimiento convierten la ejecución local en un requisito duro, y trae consigo un compromiso de personal.

Las organizaciones del programa de vista previa lo adoptaron por tres razones:

1. **Acceso a la red**: las sesiones pueden alcanzar servicios internos, bases de datos y registros sin exponerlos a la internet pública.
2. **Personalización**: compiladores, SDK y CLI internos vienen preinstalados, de modo que cada sesión arranca lista para compilar.
3. **Cumplimiento**: el código fuente y los artefactos de compilación permanecen en infraestructura que controlas.

Si ninguno de estos es un requisito duro, quédate con la opción gestionada.

## Conoce la frontera de datos

Este es el punto que más se malinterpreta dentro de una organización.

| Se queda en la infraestructura que aprovisionas | Se envía para la inferencia |
|---|---|
| Checkouts del repositorio | Prompts |
| Artefactos de compilación | Respuestas |
| Secretos | Resultados de herramientas, que pueden incluir código que el modelo lee |
| Cualquier archivo que una sesión cree o modifique | |

Las transcripciones de sesión se almacenan para poder retomar una sesión desde cualquier superficie.

El autoalojamiento reubica **la ejecución y los artefactos**. No mantiene la conversación dentro de tu red. Preséntalo así ante la revisión de seguridad desde el principio.

## Arquitectura

### Runners

Despliegas **runners**: procesos de larga vida que recogen sesiones e inician un proceso de agente por sesión. El runner es la unidad para la que construyes una imagen, y la que despliegas, actualizas y operas.

### Dos modos de capacidad

- **Fijo**: un número determinado de runners permanece activo y las sesiones se reparten entre ellos. Es lo menos costoso de operar; la capacidad ociosa es un coste permanente.
- **Bajo demanda**: un orquestador vigila las sesiones en cola, arranca runners a medida que llegan y los detiene al terminar el trabajo, de modo que la capacidad sigue a la demanda. A cambio, ahora también operas el orquestador.

Elige el modo fijo salvo que la demanda sea lo bastante irregular como para que la capacidad ociosa domine el coste.

### Aislamiento

Un runner puede atender varias sesiones, pero **cada sesión se ejecuta en su propio checkout**. Ese checkout por sesión es la frontera de aislamiento entre desarrolladores y entre cuentas; no lo es el runner.

## No es lo mismo que Remote Control

Remote Control permite a una persona continuar desde el móvil o el navegador una sesión que corre en su propia máquina. Esa sesión termina cuando la máquina deja de ejecutarla y está ligada a quien la inició. Los entornos autoalojados corren sobre infraestructura compartida que opera un equipo de plataforma y cualquier usuario puede utilizarlos.

## Elegibilidad

- Beta pública, para organizaciones con planes Team y Enterprise.
- Desactivado por defecto.
- No disponible para organizaciones que usan ZDR.

## Propiedad

Cuenta con que un equipo de plataforma, de experiencia de desarrollo o de productividad de desarrollo asuma la puesta en marcha y la operación continua:

- construir y mantener la imagen del runner,
- actualizar los runners,
- operar el orquestador, si usas el modo bajo demanda.

Si ningún equipo va a asumir eso, la respuesta correcta es la oferta gestionada.

## Fuente

- https://claude.com/blog/run-claude-code-sessions-on-your-own-compute (6 de agosto de 2026)
- Documentación: https://code.claude.com/docs/en/self-hosted-environments
