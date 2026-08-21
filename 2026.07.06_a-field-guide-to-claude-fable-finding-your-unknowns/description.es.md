[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Guía de campo de Claude Fable 5: encontrar tus incógnitas

## ¿De qué trata este post?

Una guía de campo escrita por Thariq Shihipar (miembro del equipo técnico de Anthropic) sobre cómo trabajar con Claude Fable 5 tratando la distancia entre **el mapa** (tus prompts, skills y contexto) y **el territorio** (el código real y sus restricciones) como el hueco que hay que cerrar. La tesis: a medida que los modelos mejoran, la calidad del trabajo deja de estar limitada por lo bien que planificas y pasa a estar limitada por lo bien que sacas a la luz aquello que no sabías que tenías que decir.

El post ordena lo que aún no has dicho en cuatro tipos —lo conocido conocido, lo conocido desconocido, lo desconocido conocido y lo desconocido desconocido— y luego propone movimientos concretos para cada fase del proyecto: antes de implementar, durante la implementación y después.

## ¿Cuándo es útil?

- Al empezar a trabajar en una parte del código que no conoces bien.
- Al escribir un plan o una especificación y querer detectar los puntos de decisión antes de que Claude empiece a editar.
- Al trabajar en un dominio poco familiar donde todavía no distingues un buen resultado de uno malo.
- Al entregar un cambio terminado a revisores o stakeholders que no siguieron el proceso.
- Cuando quieres verificar que de verdad entiendes un cambio que Claude hizo por ti.

## Puntos clave

- **Cuatro incógnitas.** Lo *conocido conocido* es lo que pones en el prompt. Lo *conocido desconocido* son huecos que sabes nombrar. Lo *desconocido conocido* son detalles obvios para ti que nunca se te ocurre escribir. Lo *desconocido desconocido* son puntos ciegos que ni has considerado.
- **Pasada de puntos ciegos.** Pide a Claude directamente tus puntos ciegos, e indícale tu nivel de experiencia para que calibre.
- **Lluvias de ideas y prototipos.** Explora varios enfoques antes de comprometerte, para que los criterios poco claros aparezcan pronto y barato.
- **Entrevistas.** Pide a Claude que te entreviste con una pregunta a la vez, priorizando aquellas cuya respuesta cambiaría la arquitectura.
- **Referencias.** Señálale código existente que ya implementa el comportamiento que buscas, aunque esté en otro lenguaje de programación.
- **Planes de implementación.** Pide un plan que destaque los probables puntos de decisión antes de empezar.
- **Notas de implementación.** Mantén un `implementation-notes.md` temporal donde Claude registre cada desviación del plan provocada por un caso límite.
- **Pitches y explicativos.** Empaqueta el prototipo, la especificación y las notas en un único documento compartible para conseguir apoyo.
- **Cuestionarios.** Pide un informe con contexto y un cuestionario de autoevaluación para comprobar que realmente entiendes el cambio.
- **Ejemplo real.** El autor editó el vídeo de lanzamiento de Fable con Claude Code, descubriendo incógnitas de forma iterativa en transcripción, etalonaje de color y manipulación de vídeo: dominios que no dominaba al empezar.

## Recursos incluidos

- `skills/finding-your-unknowns/SKILL.md` — el flujo completo como Agent Skill, con plantillas de prompt para cada movimiento.
- `skills/finding-your-unknowns/references/four-unknowns.md` — el modelo de cuatro cuadrantes y cómo atacar cada uno.
- `skills/finding-your-unknowns/templates/` — prompts listos para pegar: puntos ciegos, entrevistas, notas, pitches y cuestionarios.
- `skills/finding-your-unknowns/examples/launching-fable.md` — el caso del vídeo de lanzamiento.
- `guides/knowing-your-unknowns.es.md` — el mismo material como guía narrativa, en cuatro idiomas.

## Fuente

- [A Field Guide to Claude Fable 5: Finding Your Unknowns](https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns) — publicado el 2026-07-06
