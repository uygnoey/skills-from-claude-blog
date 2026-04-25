[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?

Este post anuncia versiones nuevas de las herramientas de Claude Platform para web search y web fetch, que pueden ejecutar código automáticamente para filtrar dinámicamente el contenido recuperado antes de insertarlo en la ventana de contexto del modelo.

## ¿Cuándo es útil?

Es útil cuando el flujo de trabajo de búsqueda web de tu agente trae mucho HTML irrelevante o páginas muy largas, y quieres mayor precisión y menor uso de tokens, especialmente para consultar documentación técnica o verificar citas y referencias.

## Puntos clave

- La búsqueda web puede consumir muchos tokens porque a menudo se recupera HTML completo de varios sitios y luego se razona sobre mucho contenido irrelevante.
- Con el filtrado dinámico, las herramientas de web search y web fetch pueden escribir y ejecutar código para posprocesar resultados, conservando solo lo relevante antes de cargarlo en contexto.
- En BrowseComp, la precisión subió de 33.3% → 46.6% (Sonnet 4.6) y de 45.3% → 61.6% (Opus 4.6).
- En DeepsearchQA, la métrica F1 subió de 52.6% → 59.4% (Sonnet 4.6) y de 69.8% → 77.3% (Opus 4.6).
- En ambos benchmarks, el filtrado dinámico mejoró el rendimiento en un promedio de 11% usando 24% menos tokens de entrada.
- El filtrado dinámico está activado por defecto al usar las nuevas versiones de herramientas con Sonnet 4.6 y Opus 4.6 en la API de Claude.

## Recursos incluidos

- Skill: un flujo reutilizable para usar web_search + web_fetch y validar resultados/citas.
- Un ejemplo de solicitud JSON de la API tomado del post.

## Fuente

- https://claude.com/blog/improved-web-search-with-dynamic-filtering
