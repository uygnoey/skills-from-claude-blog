[English](./dynamic-workflows.en.md) · [한국어](./dynamic-workflows.ko.md) · **Español** · [日本語](./dynamic-workflows.ja.md)

# Flujos de trabajo dinámicos en Claude Code: cómo usarlos bien

## ¿Qué son los flujos de trabajo dinámicos?
Los flujos de trabajo dinámicos son una capacidad de Claude Code en la que Claude puede generar scripts de orquestación para coordinar decenas o cientos de subagentes en paralelo dentro de una sola sesión y verificar el trabajo antes de mostrártelo.

## Cuándo usar (y cuándo no)
Úsalos cuando:
- la tarea abarca una superficie grande (muchos archivos/módulos/incertidumbre)
- necesitas descubrimiento y revisión amplios en una base de código grande
- quieres someter un plan a “stress test” antes de comprometerte

Evítalos (o empieza más pequeño) cuando:
- la tarea ya está bien acotada y se resuelve en una sola pasada enfocada
- te preocupa el presupuesto de tokens (pueden consumir sustancialmente más)

## Configuración recomendada
- Activa **auto mode** para la mejor experiencia.
- Empieza con una tarea **acotada** para entender el coste/beneficio.

## Dos formas de iniciar
1. Pídele a Claude que cree un workflow directamente.
2. Activa **ultracode** desde el menú de esfuerzo (esfuerzo xhigh) para que Claude decida cuándo usarlo.

## Qué esperar durante la ejecución
- La primera vez que se active un workflow, Claude Code mostrará lo que va a ejecutar y pedirá confirmación.
- Están pensados para ejecuciones largas (horas o días).
- El progreso se guarda mientras se ejecuta, así que se puede reanudar si se interrumpe.

## Fuente
- https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
