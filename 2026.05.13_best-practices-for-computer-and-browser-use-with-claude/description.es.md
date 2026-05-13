[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Buenas prácticas para el uso de computadora y navegador con Claude

## ¿De qué trata este post?
Un conjunto práctico de recomendaciones para construir automatizaciones fiables de “computer use” y “browser use” con Claude, centrado en el tamaño de capturas de pantalla, el manejo de coordenadas, el formato de prompts, el ajuste de fiabilidad/coste, la seguridad y la gestión de contexto en sesiones largas.

## ¿Cuándo es útil?
- Cuando construyes un agente que hace clic/escribe en una IU usando capturas de pantalla.
- Cuando la precisión de clic es inconsistente (clics desplazados, casi aciertos, elemento equivocado).
- Cuando necesitas criterios para downscaling, zoom, “thinking effort”, caché y compaction en sesiones largas.
- Cuando diseñas mitigaciones contra prompt injection para agentes que operan en la web abierta.

## Puntos clave
- Reduce el tamaño de las capturas antes de enviarlas (por defecto 1280×720; en Opus 4.7 se sugiere empezar en 1080p).
- Si redimensionas la captura, reescala las coordenadas devueltas por el modelo al espacio de pantalla nativo antes de ejecutar el clic.
- Coloca la instrucción de texto antes del bloque de imagen en el array de contenido.
- Para objetivos pequeños, usa zoom o alternativas de teclado; evita resoluciones demasiado bajas.
- Ajusta el “thinking effort” según el modelo y el escenario; considera un patrón orquestador+subagente para separar planificación y ejecución mecánica.
- Trata todo el contenido web como no confiable; usa clasificadores integrados, limita permisos, registra acciones y pide confirmación humana antes de acciones irreversibles.
- En agentes de larga duración, usa puntos de caché, depura capturas antiguas y considera compaction del lado del servidor.

## Recursos incluidos
Esta carpeta incluye:
- Un Agent Skill reutilizable con checklists y guía de implementación.
- Scripts auxiliares para preparar capturas, reescalar coordenadas, colocar cache_control y depurar capturas antiguas.
- Una referencia con valores recomendados y optimizaciones que no aportaron mejoras.

## Fuente
Blog de Claude: https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude
