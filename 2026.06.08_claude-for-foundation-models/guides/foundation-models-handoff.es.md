[English](./foundation-models-handoff.en.md) · [한국어](./foundation-models-handoff.ko.md) · **Español** · [日本語](./foundation-models-handoff.ja.md)

# Diseñar un traspaso de Apple Foundation Models → Claude

Esta guía resume el enfoque de integración descrito en el post oficial y lo convierte en una lista de verificación reutilizable.

## Lo que describe el post
- Usa el framework Foundation Models de Apple desde Swift para tareas en el dispositivo como resumen y extracción.
- Cuando la solicitud del usuario requiere trabajo más complejo, llama a Claude para razonamiento de varios pasos, generación de código, búsqueda web o ejecución de código para análisis de datos.
- Transmite (streaming) la respuesta de Claude en la misma vista de UI.

## Estructura recomendada del flujo
1. **Paso en el dispositivo (rápido, local)**
   - Define qué extraer o resumir.
   - Prefiere guided generation para producir valores tipados en Swift.
2. **Escalada a Claude (complejo)**
   - Usa los valores tipados como entradas limpias para Claude.
   - Pide a Claude que razone en varios pasos y produzca la respuesta final.
3. **Una sola experiencia de usuario**
   - Presenta el resultado como una interacción continua transmitiendo la salida de Claude en la misma vista.

## Casos de uso del post
- Apps de diario: prompts diarios en el dispositivo → Claude encuentra patrones a lo largo de meses.
- Apps de estudio: definiciones en el dispositivo → Claude responde a preguntas conceptuales más profundas.

## Fuente
- https://claude.com/blog/claude-for-foundation-models
