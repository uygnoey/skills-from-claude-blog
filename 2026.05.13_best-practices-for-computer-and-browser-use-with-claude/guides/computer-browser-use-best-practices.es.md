[English](./computer-browser-use-best-practices.en.md) · [한국어](./computer-browser-use-best-practices.ko.md) · **Español** · [日本語](./computer-browser-use-best-practices.ja.md)

# Guía: buenas prácticas para computer use y browser use con Claude

Esta guía resume valores recomendados y tácticas de depuración para construir agentes fiables de computer/browser use con Claude.

## 1) Tamaño de imagen y escalado
- Reduce el tamaño de las capturas antes de enviarlas.
- Un valor por defecto simple es 1280×720; para Opus 4.7 se sugiere empezar en 1080p.
- Evita resoluciones demasiado bajas (< ~960×540).
- Si necesitas máxima fidelidad dentro de límites, calcula un tamaño “max API fit” manteniendo la relación de aspecto.

## 2) Corrección de coordenadas
Si redimensionaste la captura, reescala las coordenadas devueltas por la API al espacio de pantalla nativo antes de ejecutar clics.

## 3) Formato del mensaje
Coloca la instrucción de texto antes del bloque de imagen en el contenido del mensaje.

## 4) Objetivos pequeños
- Activa zoom para IU densas.
- Prefiere navegación por teclado cuando los objetivos son muy pequeños.
- En pantallas 4K+, usa Opus 4.7 (mayor presupuesto de imagen) o reduce DPI/escala y captura sólo la región relevante.

## 5) Thinking effort (computer use)
- Opus 4.7: por defecto `high`; para rendimiento/coste, `low`; considera `max` sólo para tareas muy difíciles de un solo intento.
- Claude 4.6: por defecto `medium`; para rendimiento/coste, `low`; desactiva thinking sólo en flujos simples donde la latencia sea prioridad.

## 6) Seguridad ante prompt injection
- Trata todo el contenido web como no confiable.
- Prioriza clasificadores integrados vía `computer_20251124`.
- Requiere confirmación humana para acciones irreversibles.
- Limita permisos y registra acciones con detalle.

## 7) Gestión de contexto en sesiones largas
Un valor por defecto práctico del post:
- Un breakpoint de caché en el prefijo estable y tres en los resultados recientes de herramientas.
- Depuración por buffer rodante de capturas (p. ej., keep_n=3, depurar cada ~25 capturas).
- Compaction del lado del servidor alrededor de ~150k tokens de entrada con un prompt de compaction personalizado.

## Fuente
https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude
