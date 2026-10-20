[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un artículo de la serie Notes from the Field, escrito por ingenieros de despliegue avanzado de
Anthropic, sobre cómo preparar sistemas críticos y empresas reguladas para una modernización de código
impulsada por agentes. Los agentes ya escriben cambios más rápido de lo que las organizaciones pueden
revisarlos, así que el post propone seis pasos de trabajo organizativo: definir el objetivo, crear el
certificado, fijar la política de promoción, preparar los requisitos previos, construir y refinar el
flujo agéntico y ejecutar la modernización, además de una nota sobre el coste en tokens.

## ¿Cuándo es útil?
- Al definir el alcance de una subida de versión, una reescritura entre stacks o una reconstrucción de
  un sistema sujeto a gestión de cambios, auditoría o reguladores.
- Cuando las partes interesadas no se ponen de acuerdo sobre si el comportamiento puede cambiar.
- Cuando el cuello de botella ya no es escribir código sino revisar y aprobar.
- Cuando la dirección necesita una justificación de negocio o una estimación de coste antes de comprometerse.

## Puntos clave
- Tres tipos de modernización: **uplift** (subida de versión en el mismo stack), **transform**
  (reescritura entre stacks con comportamiento fijo) y **reimagine** (reconstrucción con comportamiento
  modificado y especificación escrita). Decídelo pronto.
- Mapea el código (`assess`, `map`, `extract-rules` del plugin de modernización de código), completa con
  entrevistas y justifica el proyecto sobre todo por **reducción de riesgo**.
- El **certificado** es un conjunto de condiciones verificables automáticamente, sin humanos, que todo
  cambio debe cumplir: tests, cobertura, límites de rendimiento, revisiones adversariales de Claude en
  contextos nuevos, paridad de salida, periodo en staging, escaneos de seguridad. Escríbelo con los
  revisores; que Claude construya la evidencia que falte.
- La **política de promoción** escalona la revisión humana por radio de impacto y confianza del agente,
  corrige en el origen las alertas recurrentes y dedica el tiempo de los expertos a los cambios más
  arriesgados. La dirección debe emitirla de antemano para compartir la responsabilidad.
- Los requisitos previos abarcan entorno, CI/CD, capacidad de revisión y seguridad (mínimo privilegio,
  secretos y datos personales enmascarados, trazabilidad de PR a transcripción).
- Construye el flujo a partir del plugin de modernización de código; ante problemas, corrige el flujo y
  no cada cambio. Pilota una partición de extremo a extremo y luego escala. Un uplift puede hacerse in
  situ, partición por partición.
- Coste: mide tokens en el piloto para estimar un mínimo, pon las comprobaciones caras tras filtros
  baratos y usa modelos como Sonnet para el trabajo mecánico.

## Recursos incluidos
- Skill: `code-modernization-readiness` — el procedimiento de seis pasos con referencias (tipos de
  modernización, condiciones del certificado, política de promoción, lista de requisitos, estimación de
  costes) y una plantilla de carta de modernización.
- Guía: `preparing-ai-code-modernization` (en/ko/es/ja) — la metodología completa.

## Fuente
- https://claude.com/resources/articles/how-to-prepare-for-ai-driven-code-modernization-projects
