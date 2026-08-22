[English](./dark-factory-for-agentic-development.en.md) · [한국어](./dark-factory-for-agentic-development.ko.md) · **Español** · [日本語](./dark-factory-for-agentic-development.ja.md)

# Construir una fábrica oscura para el desarrollo con agentes

Cómo Datadog pasó de "los agentes escriben código" a "los agentes escriben especificaciones verificables", y qué exige eso estructuralmente.

## 1. El problema del flujo

El flujo de la ingeniería solía ser una relación directa entre la intención y el código. Entendías el problema, escribías el código, lo probabas, lo revisabas, lo enviabas, lo operabas y repetías. Los agentes cambiaron esa abstracción, y deprisa.

Sesh Nalla, VP de ingeniería en Datadog, sobre en qué se convirtió el trabajo:

> "Ya no escribes el código; das forma al trabajo. Decides qué debe ver el agente. Qué herramientas debe tener, qué significa el éxito, cómo debe detectarse el fallo… Es como si a todos los hubieran ascendido tres niveles en la cadena de mando, algo que no pidieron porque son ingenieros."

Los ingenieros de Datadog usan Claude Code en cuatro categorías de trabajo en producción: cambios puntuales, refactorizaciones grandes, sustitución de sistemas importantes y construcción de sistemas completamente nuevos. A esa escala el ascenso no es una metáfora: es un cambio real en lo que contiene el día de un ingeniero, y el utillaje que hay debajo se construyó para el trabajo anterior.

> "Este es el punto en el que sentí que necesitábamos algo más estructural. Si los agentes van a construir y operar buena parte de nuestros sistemas, de nuestras bases de datos, que son críticas, necesitan el equivalente de este concepto de máquina herramienta. Temper es esa máquina herramienta para Datadog."

## 2. Tres proyectos que hicieron posible Temper

**Courier (2024)**, un sistema distribuido de colas construido con un fuerte modelado formal. La lección: "La dificultad no era construir las partes; era hacer que las interacciones entre ellas fueran observables, comprobables y verificables."

**BitsEvolve (septiembre de 2025)**, optimización evolutiva de bucle cerrado mediante generación de variantes con retroalimentación. La lección: "Este fue para mí el primer atisbo de que partes del software podían cultivarse como organismos vivos: crecidas mediante variación con retroalimentación y adaptación."

**Helix**, un sistema de streaming comparable a Kafka que Claude Code construyó en su mayor parte en días. "Para nuestra incredulidad, en unos días teníamos un sistema comparable a Kafka plenamente funcional." Y entonces la restricción se reubicó:

> "El cuello de botella volvió a moverse: los agentes podían construir grandes partes del sistema… pero luego los humanos todavía tienen que coordinarse para llevar el trabajo a producción a través de herramientas y mecanismos hechos para humanos."

Esa frase es la especificación de lo que vino después. El utillaje del SDLC asume que quien conduce es una persona. Cuando la construcción tarda días, la superficie de coordinación con forma humana pasa a ser la parte lenta.

## 3. Temper: los agentes emiten especificaciones y un kernel las demuestra

La inversión central: los agentes no producen código de aplicación para la lógica de control. Producen **especificaciones**. Un kernel determinista —fuera del LLM— verifica cada una antes de que se ejecute.

Situar la compilación y la prueba fuera del modelo importa por una razón concreta: el artefacto que se verifica es el artefacto que se ejecuta. No hay ningún paso en el que una descripción demostrada se reimplemente a mano en algo que podría diferir.

### Las cuatro capas de verificación

Independientes por diseño, de modo que cada una cubre los puntos ciegos de las demás:

1. **El razonamiento simbólico** demuestra que cada guarda es satisfacible y cada invariante es inductivo.
2. **La exploración exhaustiva de estados** visita todos los estados alcanzables.
3. **La simulación determinista** ejecuta código de producción con inyección de fallos con semilla.
4. **Las pruebas de propiedades aleatorizadas** ejecutan aproximadamente 1.000 secuencias de acciones pseudoaleatorias.

El determinismo es lo que hace esto utilizable dentro de un bucle con agentes. Un fallo vuelve con su semilla, así que el agente recibe la ejecución fallida exacta y no una descripción de ella.

### Los tres contratos

Cada capability exige los tres:

- **Comportamiento**: estados, transiciones, precondiciones, propiedades de seguridad.
- **Contrato de datos**: tipos de entidad, propiedades y acciones en forma analizable por máquina.
- **Autorización**: denegación por defecto, aprobación basada en ámbitos con decisiones pendientes.

La denegación por defecto con decisiones pendientes es lo que convierte "el agente quiere más permisos" de incidente en diff revisable.

## 4. La fábrica oscura de Helix

Temper desempeña tres papeles a la vez para la fábrica oscura de Helix:

1. **Plano de control de agentes**: sesiones, roles, colas de trabajo y ciclo de vida de los agentes gestionados.
2. **Capa constructora de herramientas**: permite a los agentes conectar el utillaje del SDLC —Git, CI, despliegue—. Es la respuesta directa al cuello de botella posterior a Helix.
3. **API de control de Helix**: la superficie de ciclo de vida alrededor del plano de datos.

El tercer papel es lo que lo convierte en una máquina herramienta y no en una tubería de compilación: el plano de control de los agentes y el del producto que construyen son la misma superficie explícita y verificada.

## 5. ¿Por qué no construir simplemente una app CRUD?

Claude Code construye bien apps CRUD. La objeción no está ahí. La objeción es dónde acaba la lógica de control:

> "En las apps CRUD normales, la lógica de control está repartida entre rutas, restricciones de base de datos, código de servicio, trabajos en segundo plano y documentación… el modo operativo, que en general toma la forma de una máquina de estados, es implícito en el código."

La lógica de control implícita no puede verificarse ni puede cambiarla un agente con seguridad, porque no hay un único artefacto que cambiar. La respuesta de Temper:

> "Temper hace explícita esa máquina de estados. El agente produce una descripción precisa, no código arbitrario… Los agentes pueden cambiarla dinámicamente, con seguridad, y recargarla en caliente sin pasar por CI."

De convertir la máquina de estados en datos en lugar de código se siguen tres cosas:

- Un agente puede leer toda la lógica de control sin leer todo el código.
- Un cambio es un diff acotado, no una edición en cinco archivos.
- Puede recargarse en caliente bajo política en vez de consumir un ciclo de CI.

## 6. Hacia dónde apunta esto

> "Si los agentes pueden construir software de forma autónoma dentro de fábricas con esta clase de disciplina, quizá no necesitemos detenernos en las fábricas oscuras. El software construido así empieza a parecer un organismo que podemos hacer crecer, cultivar y evolucionar mediante retroalimentación, selección y adaptación."

## 7. Buenas prácticas del equipo de Datadog

**¿Tu cuello de botella real es la generación o la verificación?**
Supón que es la verificación. Los agentes ya producen código más rápido de lo que cualquier equipo puede revisar; la brecha entre lo generado y lo demostrado es donde se acumulan los modos de fallo. Invierte ahí, no en más rendimiento.

**¿Qué debería emitir realmente el agente?**
Especificaciones para la lógica de control (no código) y pruebas que acompañen al código arbitrario. Sitúa la compilación y la prueba fuera del LLM: entrega la especificación a un kernel determinista para que el artefacto que se verifica sea el artefacto que se ejecuta.

**¿Tu lógica de control es explícita o está repartida por el código?**
Saca la máquina de estados de las rutas, los métodos de servicio y los trabajos en segundo plano y conviértela en datos: una tabla de transiciones que un agente pueda leer, modificar y recargar en caliente bajo política.

**¿Puede una persona sostener cada artefacto en su cabeza y comprenderlo?**
Si no, has vuelto al punto de partida. Mantén cada pieza generada lo bastante pequeña como para razonar sobre ella.

## Fuente

[How Datadog built a "universal machine tool" for Claude Code](https://claude.com/blog/how-datadog-built-a-universal-machine-tool-for-claude-code) — Michael Segner, 21 de julio de 2026
