[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Soporte de Claude para el framework Foundation Models de Apple

## ¿De qué trata este post?
Anthropic presenta un nuevo paquete de Swift que conecta el framework Foundation Models de Apple con Claude. El enfoque es usar modelos en el dispositivo para tareas simples y transferir a Claude las solicitudes más complejas.

## ¿Cuándo es útil?
- Cuando quieres mantener resumen/extracción rápidos y privados en el dispositivo, pero necesitas una escalada fluida a un modelo más potente para razonamiento de varios pasos.
- Cuando quieres que salidas tipadas en Swift (vía guided generation de Apple) se conviertan en entradas limpias y estructuradas para una llamada a la API de Claude.

## Puntos clave
- Usa el framework Foundation Models en el dispositivo (p. ej., resumen y extracción) y pasa a Claude para razonamiento multi‑paso, generación de código, búsqueda web y ejecución de código para análisis de datos.
- Mantén una experiencia unificada transmitiendo (streaming) la respuesta de Claude en la misma vista de UI.
- Las salidas tipadas reducen la dependencia del texto crudo del usuario al invocar a Claude.

## Recursos incluidos
- Un Agent Skill reutilizable que documenta el patrón “primero en el dispositivo y luego a Claude” para apps con Foundation Models (ver `skills/foundation-models-handoff/SKILL.md`).
- Un esqueleto de plugin para empaquetar y distribuir el skill (ver `plugin/.claude-plugin/plugin.json`).

## Fuente
- https://claude.com/blog/claude-for-foundation-models
