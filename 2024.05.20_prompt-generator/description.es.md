[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Generar mejores prompts en la Console para desarrolladores

## ¿De qué trata este post?

El anuncio de Anthropic del 20 de mayo de 2024 presenta un prompt generator dentro de la Anthropic Console que convierte una descripción corta de una tarea en una plantilla de prompt lista para producción. El generador incorpora técnicas de prompt engineering — definición clara del rol, scratchpads de chain-of-thought, etiquetas XML alrededor de variables ambiguas y variables simples en línea — para que las personas desarrolladoras no tengan que aplicar manualmente estos patrones cada vez que inician un proyecto.

## ¿Cuándo es útil?

- Estás empezando una nueva funcionalidad basada en Claude y necesitas un primer borrador sólido del prompt.
- Quieres un estilo de plantilla consistente entre equipos que ya codifique las mejores prácticas de prompt engineering de Anthropic.
- Estás migrando un prompt existente a la Console y quieres una línea base con la que comparar.
- Estás construyendo un conjunto de evaluación y necesitas separar limpiamente las instrucciones fijas de las variables por ejemplo.

## Puntos clave

- Los prompts generados incluyen una definición de rol explícita (por ejemplo, "You will be acting as a content moderator").
- Las tareas complejas se andamian con un bloque `<scratchpad>` de chain-of-thought donde se le pide a Claude que piense antes de responder.
- Las variables ambiguas o grandes se envuelven en etiquetas XML como `<code>{{CODE}}</code>` para hacer los límites inequívocos.
- Las variables cortas y simples pueden referenciarse en línea, por ejemplo `{{LANGUAGE}}`.
- Las variables usan notación handlebars, así la misma plantilla se conecta tanto con el workbench de la Console como con herramientas posteriores.
- Por detrás, el generador ejecuta un meta-prompt largo que primero planifica la estructura y usa etiquetas XML como "espina dorsal" del resultado.
- ZoomInfo aparece como caso de cliente; Spencer Fox, Principal Data Scientist en ZoomInfo, dice que el equipo llegó a MVP en solo unos días, reduciendo en un 80% el tiempo de refinamiento de prompts.

## Recursos incluidos

- Skill: `skills/prompt-template-bootstrap/SKILL.md` — cuándo usar el generador, qué técnicas trae ya incorporadas y cómo editar y evaluar el resultado.
- Referencia: `skills/prompt-template-bootstrap/references/best-practices-from-post.md` — las técnicas de prompt engineering que el post afirma estar integradas en el generador.
- Ejemplos: `skills/prompt-template-bootstrap/examples/template-fragments.md` — fragmentos de plantilla citados textualmente en el post (rol de moderador de contenido, recomendación del scratchpad, XML para traducción de código, testimonio de ZoomInfo).

## Fuente

Generate better prompts in the developer Console — Anthropic, 20 de mayo de 2024: <https://claude.com/blog/prompt-generator>
