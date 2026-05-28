[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Este post presenta los **flujos de trabajo dinámicos (dynamic workflows)** en Claude Code: un modo de ejecución en el que Claude puede escribir scripts de orquestación que coordinan decenas o cientos de subagentes en paralelo dentro de una sola sesión y revisar su propio trabajo antes de mostrártelo.

## ¿Cuándo es útil?
Es útil cuando una tarea es demasiado grande para una sola pasada (sobre todo en bases de código complejas o heredadas), por ejemplo:
- una búsqueda de bugs en todo un servicio
- una migración que toca cientos de archivos
- un plan que quieres someter a “stress test” antes de comprometerte

## Puntos clave
- Está pensado para trabajo **paralelo** y de **larga duración** (horas o días).
- El progreso se guarda durante la ejecución, de modo que se puede reanudar si se interrumpe.
- La primera vez que se activa un flujo de trabajo, Claude Code muestra lo que va a ejecutar y pide confirmación.
- Puedes iniciar un flujo pidiéndoselo a Claude directamente o activando **ultracode** (esfuerzo xhigh) para que Claude decida cuándo usarlo.
- Puede consumir muchos más tokens que una sesión típica.

## Recursos incluidos
- Skill: guía para decidir cuándo usar flujos de trabajo dinámicos y cómo estructurar las solicitudes de workflow.

## Fuente
- https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
