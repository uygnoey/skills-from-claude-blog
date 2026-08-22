[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Los ingenieros de Datadog usan Claude Code en producción en cuatro categorías: cambios puntuales, refactorizaciones grandes, sustitución de sistemas importantes y construcción de sistemas completamente nuevos. Al escalar ese uso, la restricción se desplazó. Sesh Nalla, VP de ingeniería en Datadog, describe cómo cambia la sensación del trabajo de ingeniería: "Ya no escribes el código; das forma al trabajo. Decides qué debe ver el agente. Qué herramientas debe tener, qué significa el éxito, cómo debe detectarse el fallo… Es como si a todos los hubieran ascendido tres niveles en la cadena de mando, algo que no pidieron porque son ingenieros."

La respuesta estructural que construyó Datadog es **Temper**, descrita como una "máquina herramienta universal" para agentes. En lugar de que los agentes emitan código de aplicación para la lógica de control, emiten **especificaciones**. Un kernel determinista situado fuera del LLM verifica después cada especificación mediante cuatro capas independientes —razonamiento simbólico, exploración exhaustiva de estados, simulación determinista con inyección de fallos con semilla y pruebas de propiedades aleatorizadas— antes de que nada se ejecute. Cada capability se expresa con tres contratos: comportamiento, datos y autorización.

El post recorre cómo tres proyectos anteriores (Courier, BitsEvolve y Helix) hicieron posible Temper, y luego muestra a Temper operando una "fábrica oscura" (dark factory) para Helix, un sistema de streaming comparable a Kafka que Claude Code construyó en su mayor parte en días. Cierra con las buenas prácticas del equipo de Datadog.

## ¿Cuándo es útil?
- Cuando los agentes generan código más rápido de lo que el equipo puede revisar, y la revisión —no la generación— pasa a limitar los envíos.
- Cuando hay que decidir qué debe emitir realmente un agente: código arbitrario o una especificación que un kernel determinista pueda verificar.
- Cuando la lógica de control está repartida entre rutas, restricciones de base de datos, código de servicio, trabajos en segundo plano y documentación, y nadie sabe cuál es la máquina de estados del sistema.
- Cuando los agentes necesitan cambiar el comportamiento operativo de forma segura sin pasar por un ciclo completo de CI cada vez.
- Cuando se construye un bucle autónomo de construcción y operación y hay que decidir qué siguen teniendo que coordinar las personas.
- Cuando hay que juzgar si los artefactos generados han superado el tamaño que una persona puede sostener mentalmente.

## Puntos clave
- **Supón que el cuello de botella es la verificación, no la generación.** Los agentes ya producen código más rápido de lo que cualquier equipo puede revisar. La brecha entre lo generado y lo demostrado es donde se acumulan los modos de fallo, así que la inversión va ahí y no en más rendimiento.
- **Los agentes emiten especificaciones para la lógica de control, no código.** Para el código arbitrario, el planteamiento del artículo es que lleve su propia prueba (proof-carrying). La compilación y la prueba se sitúan fuera del LLM: la especificación va a un kernel determinista, de modo que el artefacto verificado es el artefacto que se ejecuta.
- **Cuatro capas de verificación independientes.** El razonamiento simbólico demuestra que cada guarda es satisfacible y cada invariante es inductivo; la exploración exhaustiva de estados visita todos los estados alcanzables; la simulación determinista ejecuta código de producción con inyección de fallos con semilla; las pruebas de propiedades aleatorizadas ejecutan unas 1.000 secuencias de acciones pseudoaleatorias.
- **Cada capability lleva tres contratos.** Comportamiento (estados, transiciones, precondiciones, propiedades de seguridad), contrato de datos (tipos de entidad, propiedades y acciones en forma analizable por máquina) y autorización (denegación por defecto, aprobación basada en ámbitos con decisiones pendientes y carga en caliente).
- **Tres proyectos hicieron posible Temper.** Courier (2024), un sistema distribuido de colas donde "la dificultad no era construir las partes; era hacer que las interacciones entre ellas fueran observables, comprobables y verificables"; BitsEvolve (septiembre de 2025), un optimizador evolutivo de bucle cerrado que fue "el primer atisbo… de que partes del software podían cultivarse como organismos vivos"; y Helix, donde un sistema comparable a Kafka apareció en días y el cuello de botella volvió a moverse: a las personas coordinando una entrega con herramientas hechas para personas.
- **Temper cumple tres papeles en la fábrica oscura de Helix.** Plano de control de agentes para agentes gestionados (sesiones, roles, colas de trabajo, ciclo de vida); capa constructora de herramientas que permite a los agentes conectar el utillaje del SDLC (Git, CI, despliegue); y la API de control de Helix como superficie de ciclo de vida alrededor del plano de datos.
- **Por qué no una simple app CRUD.** Claude Code construye bien apps CRUD, pero allí el modo operativo —generalmente una máquina de estados— queda implícito y repartido entre rutas, restricciones, código de servicio, trabajos y documentación. Temper hace esa máquina de estados explícita y dirigida por datos: "El agente produce una descripción precisa, no código arbitrario… Los agentes pueden cambiarla dinámicamente, con seguridad, y recargarla en caliente sin pasar por CI."
- **Mantén cada artefacto comprensible para una persona.** Si alguien no puede sostener mentalmente un artefacto generado, has vuelto al punto de partida.
- **Hacia dónde apunta esto.** "El software construido así empieza a parecer un organismo que podemos hacer crecer, cultivar y evolucionar mediante retroalimentación, selección y adaptación."

## Recursos incluidos
- `skills/spec-driven-agent-verification/` — el método de trabajo: desplazar la inversión hacia la verificación, hacer que los agentes emitan contratos en lugar de código de control y situar el kernel fuera del modelo. Incluye referencias sobre las cuatro capas de verificación y sobre la arquitectura de Temper, plantillas para un contrato de capability y una tabla de transiciones, un ejemplo que recorre el camino de Courier a la fábrica oscura y un script verificador de la forma del contrato.
- `guides/dark-factory-for-agentic-development.{en,ko,es,ja}.md` — el recorrido completo en cuatro idiomas.

## Fuente
[How Datadog built a "universal machine tool" for Claude Code](https://claude.com/blog/how-datadog-built-a-universal-machine-tool-for-claude-code) — Michael Segner, 21 de julio de 2026
