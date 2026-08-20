[English](./slack-analytics-rollout.en.md) · [한국어](./slack-analytics-rollout.ko.md) · **Español** · [日本語](./slack-analytics-rollout.ja.md)

# Desplegar analítica de datos autoservicio en Slack

## Por qué el despliegue es un problema distinto de la precisión
El trabajo previo cubrió cómo llevar un agente de analítica hasta aproximadamente un 95% de precisión: capas semánticas, archivos de skill y suites de evaluación. Esta guía cubre lo que viene después: llevar ese agente a Slack para que cualquier persona de la empresa pueda hacerle preguntas ad hoc. Aquí las decisiones que importan son otras: frescura, permisos y observabilidad.

## 1. Actualiza las skills con la misma frecuencia con la que actualizas los modelos de datos
La decisión arquitectónica central es tratar los archivos de skill como **contenido servido, actualizado de forma continua**, y no como algo que se publica una vez y se olvida.

Los modelos de datos cambian constantemente. Se renombran columnas, se corrigen métricas, se deprecan tablas. Un archivo de skill escrito contra el modelo del trimestre pasado es una fuente de respuestas equivocadas con aire de seguridad. El runtime vuelve a leer los archivos de skill en cada conversación desde un repositorio montado, de modo que el agente siempre resuelve contra las definiciones vigentes.

Consecuencia práctica: las actualizaciones de los archivos de skill deben pasar por el mismo proceso de revisión que gobierna el propio modelo de datos, para que una corrección de métrica y su actualización de skill lleguen juntas.

## 2. Dale al agente skills más allá del acceso a datos
Saber qué tabla consultar es el mínimo. El agente también necesita las convenciones analíticas que tus analistas ya siguen:

- **Pronóstico** — ajuste de tendencia, supuestos de estacionalidad
- **Análisis de cohortes y retención** — definiciones estándar, curvas de retención
- **Análisis de embudo** — definiciones canónicas de etapas
- **Gráficos** — convenciones de visualización
- **Escritura analítica** — estructura, matización, niveles de confianza

Esto documenta la práctica existente en lugar de inventar metodología. Ponerlo por escrito es lo que mantiene la salida del agente consistente con la de los analistas.

## 3. Conecta el contexto de negocio, no solo el almacén de datos
Además de la conexión al almacén, conecta el agente a los índices de conocimiento internos: catálogos de documentos, discusiones y eventos.

Cuando una métrica se mueve, el agente puede entonces buscar qué más ocurrió al mismo tiempo: un informe de incidente, un cambio de feature flag, un anuncio de la competencia. Esa es la diferencia entre "los registros cayeron un 12%" y una respuesta que explica la semana.

## 4. Otorga permisos a la cuenta de servicio de forma deliberada
Trata el acceso del agente a los canales como **una réplica de lectura compartida de tu almacén gobernado**. Cinco protecciones:

1. **Limita la cuenta a datos gobernados.** Deja fuera de alcance los esquemas de staging y scratch sin gobierno.
2. **Clasifica la PII a nivel de columna y niégale acceso al agente.** A nivel de columna, para que una tabla siga sirviendo para agregados mientras las columnas identificativas quedan fuera.
3. **Documenta las rutas de conexión en los archivos de skill.** Así el alcance real del agente puede revisarlo alguien ajeno al equipo de datos.
4. **Trata la pertenencia a un canal como una concesión de acceso.** Todos los miembros de un canal con el agente obtienen acceso indirecto de lectura a todo lo que el agente pueda leer.
5. **Etiqueta cada consulta.** Para trazabilidad de auditoría y atribución de costes.

## 5. Instrumenta cada respuesta
Registra un evento estructurado por cada pregunta. Como mínimo, captura:

- Qué archivos de skill se cargaron y en qué versión
- Reacciones de los usuarios (👍/👎) y cualquier corrección escrita
- Avisos de calidad de datos sobre las tablas accedidas

**La adopción es la métrica más accionable.** Una caída señala una de dos cosas: deriva de skills — las definiciones se movieron y las respuestas empezaron a sentirse erróneas — o una necesidad de datos no cubierta, en la que la gente pregunta por algo que el agente no puede alcanzar.

## Qué habilita esta superficie más allá de preguntas puntuales

**Los hilos como espacios colaborativos.** Varias personas aportan contexto mientras el agente hace el análisis. El hilo se convierte en un registro histórico revisable del problema y de cómo se resolvió.

**Bucles configurados para trabajo repetitivo.**
- Informes proactivos semanales antes de las reuniones de seguimiento
- Monitorización de tests y experimentos
- Observabilidad de pipelines y dashboards
- Clasificación de las preguntas de datos entrantes

**Asistencia proactiva.** Configurado adecuadamente, el agente puede responder más del 75% de las preguntas del canal sin ser mencionado explícitamente.

## Secuencia de implementación
1. Establece primero los permisos
2. Configura la distribución y verifica la frescura
3. Activa la telemetría desde el primer día
4. Conecta los índices de conocimiento cuando las rutas de datos se estabilicen
5. Crea las skills analíticas a partir de las preguntas reales de los usuarios

## Fuente
- https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions
