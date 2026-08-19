[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Es el anuncio de la guía de producto de Claude Science, una guía práctica de despliegue para organizaciones de ciencias de la vida. El post resume la guía y enlaza al PDF completo.

Claude Science (en beta) se describe como una aplicación para cada paso digital de las ciencias de la vida, construida para ejecutarse junto a los datos del científico y producir resultados que se puedan rastrear, reproducir y defender. La guía cubre qué superficie de Claude usar en cada caso, cómo funciona Claude Science por dentro, las decisiones de diseño que hacen que su análisis resista una revisión, una hoja de ruta de adopción en tres fases, casos de uso por función y flujo de trabajo, y un FAQ para CIO y responsables de TI.

## ¿Cuándo es útil?
- Cuando una organización de investigación debe decidir qué superficie de Claude encaja con cada tipo de trabajo científico: análisis, trabajo documental o pipelines de producción.
- Cuando TI de investigación necesita revisar la huella de instalación, el sandbox, la lista de dominios permitidos y los destinos de despacho de cómputo antes de que los científicos apunten la herramienta a datos controlados.
- Cuando se planifica un despliegue por fases en grupos computacionales en lugar de una activación para toda la organización.
- Cuando los resultados deben ser reproducibles y defendibles ante una publicación, una presentación regulatoria o una revisión interna.

## Puntos clave
- **La elección de superficie va primero.** Claude Science para análisis, figuras y resultados; Claude Chat para consultas rápidas y redacción; Claude Cowork y Claude for Microsoft 365 para trabajo documental a nivel de estudio y presentación; Claude Code cuando el resultado es software que se entrega; Claude Platform y Claude Managed Agents para agentes embebidos y alojados. La mayoría de las organizaciones despliega más de una.
- **Se ejecuta donde están los datos.** Un daemon local en macOS o Linux —un portátil, una máquina Linux del laboratorio, un nodo de login HPC o una VM en la nube— con la interfaz en el navegador. Los trabajos pesados se despachan desde la misma sesión a un host SSH, un clúster SLURM (las directivas de lote se escriben automáticamente) o una cuenta de GPU serverless.
- **Las capacidades de dominio vienen desde el primer día**: capacidades configurables para flujos científicos habituales, conexiones opcionales a más de sesenta bases de datos científicas y unas 150 skills curadas. Como las skills ejecutan código en lugar de recuperar documentos, se pueden encadenar dentro de un mismo análisis, y cada una es de código abierto para inspeccionarla, fijar su versión o extenderla.
- **Cinco decisiones de diseño hacen que el análisis sea revisable**: kernels persistentes (los agentes también ven sus propias gráficas), procedencia en cuatro capas para cada artefacto (descripción, código, conversación e instantánea del entorno), un agente revisor en segundo plano que marca las afirmaciones que no puede rastrear hasta la evidencia, plan antes de la acción con un modelo de permisos visible, y salvaguardas de bioseguridad integradas.
- **Una hoja de ruta en tres fases**: Fundación (revisión de TI y gobierno de datos, patrón de host del daemon, 2–3 grupos campeones, SSO/SCIM, habilitación por parte del administrador), Piloto (análisis reales con datos reales del laboratorio, revisiones semanales, métricas de tiempo de ciclo, tasa de aceptación y reproducción en frío) y Escala (patrón gestionado de host del daemon, catálogo de skills curado, lista de dominios verificada, política de retención de procedencia).
- **La señal de que el piloto funciona es que los campeones empiezan a guardar sus propias skills**: el pipeline de normalización interno del laboratorio o la API del LIMS envueltos una vez para que toda sesión futura los herede.
- **Skills frente a conectores**: un conector cuando la respuesta vive en los sistemas propios de la organización y los permisos importan; una skill de datos científicos cuando la respuesta vive en el registro público. La mayoría de las preguntas reales usa ambos.
- **Los límites conocidos se declaran con claridad**: uso exclusivamente de investigación y no para decisiones clínicas o diagnósticas, no es un sistema validado para GxP, no está listo para HIPAA en el lanzamiento, sin soporte de Windows, no disponible a través de Bedrock, Vertex AI ni Foundry, sin Zero Data Retention, y el cumplimiento para datos de acceso controlado del NIH está en la hoja de ruta.

## Recursos incluidos
- `skills/life-sciences-ai-rollout/SKILL.md` — cómo planificar y ejecutar el despliegue por fases de un banco de trabajo de investigación con IA.
- `skills/life-sciences-ai-rollout/references/surface-selection.md` — la matriz de producto: qué superficie para qué trabajo.
- `skills/life-sciences-ai-rollout/references/product-architecture.md` — daemon local, despacho de cómputo y las cinco decisiones de diseño.
- `skills/life-sciences-ai-rollout/references/scientific-data-skills.md` — el catálogo de skills agrupado por el tipo de pregunta que responde.
- `skills/life-sciences-ai-rollout/references/it-security-faq.md` — el FAQ para CIO y responsables de TI.
- `skills/life-sciences-ai-rollout/templates/adoption-roadmap.md` — plantilla del plan de despliegue por fases.
- `skills/life-sciences-ai-rollout/templates/pilot-scorecard.md` — hoja de medición del piloto.
- `skills/life-sciences-ai-rollout/examples/workflow-use-cases.md` — casos de uso en descubrir, analizar y publicar.
- `guides/life-sciences-deployment.{en,ko,es,ja}.md` — la guía de despliegue completa en cuatro idiomas.

## Fuente
- https://claude.com/blog/the-claude-science-product-guide
