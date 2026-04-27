[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Prompt caching con Claude

## ¿De qué trata este post?

El anuncio de lanzamiento del prompt caching en la Anthropic API. El post explica cuándo caché paga, la lista de modelos en el lanzamiento (Claude 3.5 Sonnet, Claude 3 Opus, Claude 3 Haiku), las reducciones publicadas de latencia y costo en tres workloads de referencia, el modelo de precios (escribir al caché cuesta +25% sobre el input base; leer del caché cuesta 10% del input base) y un customer spotlight de Notion. Una nota de actualización del 17 de diciembre de 2024 indica que prompt caching pasa a **disponibilidad general** en la Anthropic API y a **preview** en Amazon Bedrock y Google Cloud Vertex AI.

## ¿Cuándo es útil?

- Decidir si prompt caching es la palanca correcta para una integración existente con Claude (frente a recortar prompts, streaming, batching o cambiar de modelo).
- Estimar la ganancia en latencia y costo para workloads similares a los tres benchmarks del post antes de comprometer trabajo de ingeniería.
- Diseñar la estructura del prompt para maximizar hits de caché — qué va en el prefijo cacheado y qué se mantiene dinámico.
- Citar las cifras publicadas (hasta 90% de reducción de costo, 85% de reducción de latencia en prompts largos; 79% de mejora en TTFT en un workload "chat con un libro" de 100k tokens).

## Puntos clave

- Prompt caching permite cachear contexto frecuente entre llamadas a la API. Úsalo cuando envías un bloque grande de contexto una vez y luego haces referencias repetidas.
- Cifras destacadas: hasta **90% menos costo** y hasta **85% menos latencia** en prompts largos. Disponible en el lanzamiento para Claude 3.5 Sonnet, Claude 3 Opus, Claude 3 Haiku en public beta (en el post original; pasa a GA con la actualización del 17-12-2024).
- Casos de uso enumerados: agentes conversacionales, asistentes de código, procesamiento de documentos largos, sets de instrucciones detalladas (con decenas de ejemplos de alta calidad), búsqueda y uso de herramientas en agentes, y experiencias de "conversación" sobre libros / papers / docs / podcasts.
- Workloads de referencia del post:
  - Chat con un libro (prompt cacheado de 100.000 tokens): TTFT 11.5s → 2.4s (-79%), costo -90%.
  - Many-shot prompting (10.000 tokens): TTFT 1.6s → 1.1s (-31%), costo -86%.
  - Conversación multi-turno (10 turnos con system prompt largo): TTFT ~10s → ~2.5s (-75%), costo -53%.
- Modelo de precios: escribir al caché cuesta **25% más** que el input base del modelo; leer del caché cuesta **10%** del input base.
- Customer spotlight: Notion adoptó prompt caching en Notion AI para optimizar operaciones internas y mejorar la respuesta. Cita de Simon Last (cofundador de Notion): "We're excited to use prompt caching to make Notion AI faster and cheaper, all while maintaining state-of-the-art quality."
- Actualización del 17 de diciembre de 2024: prompt caching está en **GA** en la Anthropic API y en **preview** en Amazon Bedrock y Google Cloud Vertex AI.

## Recursos incluidos

- [skills/prompt-caching-design-patterns/SKILL.md](./skills/prompt-caching-design-patterns/SKILL.md): cuándo usarlo, cómo estructurar el prompt para maximizar hits y cómo estimar la ganancia.
- [references/use-cases-and-benchmarks.md](./skills/prompt-caching-design-patterns/references/use-cases-and-benchmarks.md): la lista de casos de uso del lanzamiento y la tabla de workloads de referencia tal como aparecen.
- [examples/prompt-structure-patterns.md](./skills/prompt-caching-design-patterns/examples/prompt-structure-patterns.md): patrones de prefijo cacheado vs. sufijo dinámico derivados del post.

## Fuente

Basado en [Prompt caching with Claude](https://claude.com/blog/prompt-caching) (publicado el 2025-08-14; actualización del 17 de diciembre de 2024 con GA en la Anthropic API y preview en Bedrock y Vertex AI).
