[English](./dashboards-motion-rollout.en.md) · [한국어](./dashboards-motion-rollout.ko.md) · **Español** · [日本語](./dashboards-motion-rollout.ja.md)

# Despliegue de Dashboards y Motion y migración de Claude Design

Lista de comprobación para administradores y responsables de equipo, basada en el anuncio del 8 de
octubre de 2026.

## 1. Disponibilidad de un vistazo
| Función | Estado | Planes | Valor por defecto en Enterprise |
|---|---|---|---|
| Claude Dashboards | Beta | Planes de pago | Desactivado (Organization settings > Artifacts) |
| Claude Motion | Beta | Team, Enterprise | Desactivado (Organization settings > Artifacts) |
| Claude Docs, Slides, Design | Disponibilidad general | Todos, incluido Free | Activado por defecto desde el 15 de octubre (se puede activar antes) |

## 2. Antes de activar Dashboards
- Decide qué plataformas de datos conectar (Amazon Redshift, BigQuery, ClickHouse, Databricks,
  Snowflake) y qué otros conectores (p. ej., Salesforce) pueden usar los paneles.
- Presenta Dashboards para preguntas rápidas y exploratorias. Acordad a qué herramienta de BI se envía
  un panel cuando la pregunta requiere más análisis (Amplitude, Grafana, Hex, Mixpanel, Omni,
  Perplexity, PostHog, Sigma; Databricks Genie, Looker, monday.com y Tableau, próximamente).
- Enseña el hábito de verificar: hacer clic en un número para ver su consulta, pedir a Claude que lo
  explique y revisar la última actualización de cada gráfico.

## 3. Antes de activar Motion
- Motion sirve para explicar tu propio trabajo: anima texto, gráficos, formas e imágenes con código. No
  usa un modelo de generación de vídeo, así que no hay metraje generado ni personas generadas por IA.
- Salida: descarga en MP4 o apertura en Adobe, Descript, HeyGen, Higgsfield, invideo, Luma AI o Runway
  (Canva y Captions, próximamente).

## 4. Controles de Enterprise disponibles para artefactos
- Compatibilidad con CMEK para artefactos.
- Los administradores eligen qué plantillas de artefactos usa la organización.
- Compartir fuera de la organización, o con cualquiera que tenga el enlace, solo si el administrador lo
  permite.

## 5. Migración de Claude Design (fecha límite: 14 de diciembre)
Claude Design empezó en claude.ai/design; desde el 16 de septiembre también funciona dentro de cada
conversación de Claude. El sitio independiente sigue activo hasta el 14 de diciembre.
- [ ] **Migrar los sistemas de diseño.** En la página Artifacts, haz clic en "Migrate team design
  systems". Una sola migración trae todos los sistemas de diseño de la organización; los originales
  quedan intactos en la versión independiente hasta su cierre.
- [ ] **Proyectos.** Por ahora no hay que hacer nada; siguen funcionando en la versión independiente
  hasta que cierre.
- [ ] **Guardar chats y comentarios.** Permanecen en la versión independiente y no estarán disponibles
  tras el cierre.
- [ ] **Enlaces públicos.** Los enlaces a proyectos independientes dejan de funcionar al cerrar; planifica
  sustitutos.
- Consulta la guía de migración enlazada en el post original para más detalles.

## Fuente
- https://claude.com/resources/articles/dashboards-and-motion
