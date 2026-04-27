[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Este post anuncia actualizaciones de la API de Anthropic para reducir el uso de tokens y aumentar el rendimiento con Claude 3.7 Sonnet: límites con conocimiento de caché, un comportamiento de caché de prompts más simple y uso de herramientas eficiente en tokens (incluida la nueva herramienta `text_editor`).

## ¿Cuándo es útil?
- Cuando tu aplicación envía repetidamente contexto largo y casi estático (docs, fragmentos de código, políticas) y quieres reducir costo y latencia.
- Cuando estás limitado por la tasa de tokens de entrada (ITPM) y quieres más rendimiento usando caché de prompts.
- Cuando tus flujos de tool calling generan salidas grandes y quieres reducir tokens de salida.

## Puntos clave
- La caché de prompts puede reducir costos (hasta 90%) y latencia (hasta 85%) en prompts largos.
- En la API de Anthropic para Claude 3.7 Sonnet, los tokens leídos desde caché ya no cuentan para el límite de Input Tokens Per Minute (ITPM).
- La caché de prompts es más simple: al establecer un punto de ruptura de caché, Claude lee automáticamente el prefijo más largo almacenado previamente.
- El uso de herramientas eficiente en tokens (beta) puede reducir el consumo de tokens de salida (hasta 70%, ~14% en promedio).
- La herramienta `text_editor` permite ediciones dirigidas a porciones específicas de texto (p. ej., código o documentos), ayudando a reducir tokens y latencia.

## Recursos incluidos
- Ninguno (post de anuncio).

## Fuente
- https://claude.com/blog/token-saving-updates
