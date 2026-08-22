[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un relato en primera persona de Nate Parrott, diseñador de producto en Anthropic, sobre cómo llegó a existir la herramienta que construyó — Claude Design, ahora en beta — y cómo la usa a diario.

El origen es un desajuste de ritmo. En otoño de 2025, Parrott era el único diseñador de producto en Claude Code para VS Code, trabajando con dos ingenieros. La beta salió a finales de septiembre, Opus 4.5 llegó en noviembre y el equipo empezó a lanzar rápido: "Los ingenieros lanzaban mucho más que antes, mientras yo seguía entregando al ritmo de siempre. Necesitaba encontrar la manera de ponerme al día."

Su primer intento trató el diseño como el terminal trata todo: como texto. Copiaba la salida en Claude, añadía capturas y pedía que diseñara una función. Los resultados no eran buenos. El avance llegó al notar que Claude se maneja muy bien con HTML, y que el HTML no es solo un formato de sitios web: "cualquier cosa que puedas hacer en una presentación, un archivo de vídeo o un PDF, la puedes hacer en una página web". Pidió a Claude que produjera HTML, le dio una vista dividida — chat a la izquierda, salida en vivo a la derecha — y después dedicó un tiempo a destilar la esencia de la marca de Anthropic (tipografías, colores, recursos y principios) en forma de prompts, para que la salida cumpliera la guía de marca. Los diseñadores adoptaron el prototipo interno de inmediato para prototipos interactivos: en lugar de maquetar cada estado de cada pantalla y conectarlos a mano, le entregas tus recursos a Claude y le dices: haz que funcione.

Se convirtió en un proyecto real tras una sesión de presentación de ideas en un offsite del equipo de Anthropic Labs, donde "todos los presentes montaron sus diapositivas con ella, a menudo en mitad de la reunión, justo antes de su turno". El encuadre se amplió de las maquetas de producto a cualquier forma de comunicación visual — presentaciones, landing pages, one-pagers que imprimes en PDF, correos, animaciones, visuales para redes —, algo que Parrott describe como "un clic por encima del diseño de producto".

El post también traza límites. No hay modelo de imagen, así que encaja mal con el diseño de logotipos; mejor traer el logo y los recursos que ya tienes. Para lanzar software de producción, Claude Code. Las dos herramientas van y vienen: puedes sincronizar un prototipo de Claude Code a Claude Design para iterarlo en el lienzo, o pasar de Claude Design a Claude Code cuando toca construir. El grueso del texto son diez prácticas de trabajo concretas, y cierra con un alegato — vía la charla de Bret Victor "Stop Drawing Dead Fish" — a favor de hacer diseños que estén vivos.

## ¿Cuándo es útil?
- Cuando el ritmo de ingeniería ha superado al de diseño y el paso de diseño se ha vuelto el cuello de botella.
- Cuando necesitas quince versiones de un flujo para recoger opiniones y el prototipado clic a clic tradicional — maquetar cada estado y conectarlo a mano — es demasiado lento.
- Cuando decides si una pieza de trabajo pertenece a una herramienta de diseño, a Claude Design o a Claude Code.
- Cuando tus visuales generados derivan siempre hacia una estética genérica y necesitas dirigirlos.
- Cuando la misma marca, presentación o conjunto de componentes aparece en todos los artefactos y quieres un punto de partida reutilizable en vez de un lienzo en blanco.
- Cuando necesitas alineación sobre una dirección antes de que alguien se comprometa a construirla.

## Puntos clave
- **El HTML es el medio, no el formato de salida.** Tratar el HTML como un medio visual rico e interactivo — capaz de todo lo que puede una presentación, un vídeo o un PDF — fue lo que hizo buena la salida de diseño, después de que fracasara el enfoque de texto y capturas.
- **La marca va en el prompt.** Destilar tipografías, colores, recursos y principios en prompts es lo que hace que la salida cumpla por defecto, y no por corrección posterior.
- **El valor está antes de construir.** "Claude Code es para programar; Claude Design es para las otras partes del trabajo de diseño: ideación temprana, colaboración o conseguir aprobación de una dirección antes de que nadie se comprometa a construirla." A medida que los modelos mejoran en software de producción, el trabajo que más importa se desplaza hacia el principio: tener buenas ideas, alinear a todos, recoger opiniones mientras la idea aún es temprana.
- **Ida y vuelta, no o lo uno o lo otro.** Los prototipos se sincronizan de Claude Code a Claude Design para iterar en el lienzo, y pasan de Claude Design a Claude Code cuando están listos para construirse.
- **Saber qué no es.** Sin modelo de imagen, el diseño de logotipos encaja mal: trae tu logo y tus recursos. La forma general del producto es que Claude crea opciones y puntos de partida para que no mires un lienzo en blanco, y tú eliges lo que funciona por sí solo o como combinación.
- **Piensa antes de escribir el prompt.** Parrott escribe prompts lejos del ordenador — dictado, la app de Notas, una nota de voz durante un paseo — para que, al sentarse, Claude ejecute una visión ya decidida.
- **Dirige la estética o heredarás una por defecto.** "Sin dirección, Claude elige una de sus estéticas favoritas. Probablemente las reconocerías." Especifica tipografías y colores, aporta un moodboard o pide combinaciones de tipografía y color.
- **Diez opciones y luego remezcla.** La mayoría no servirá; una o dos sí. Entonces: "Me gusta la opción B y un poco de la D. Dame cinco variaciones que mezclen las dos."
- **La última milla, a mano.** Reordenar, borrar, editar texto, redimensionar y recolorear se hacen mejor con las herramientas de edición directa: "Las ediciones directas no consumen tokens, y decisiones pequeñas como el tamaño y la alineación se aprecian mejor a ojo."
- **Dale tu contexto real.** Conecta GitHub para que Claude recupere tus componentes y pantallas existentes como punto de partida; la búsqueda web y las conexiones MCP también funcionan cuando el diseño depende de información externa.
- **Hazlo vivo.** Citando "Stop Drawing Dead Fish" de Bret Victor — "Todo lo que dibujamos debería estar vivo por defecto" —, las creaciones favoritas de Parrott son las que no caben en las cajas existentes: documentos con simulaciones interactivas, presentaciones que te hablan, diagramas que también son vídeos, diseños que son su propio editor.

## Recursos incluidos
- `skills/visual-ideation-workflow/` — las diez prácticas convertidas en procedimiento de trabajo, más una referencia sobre los límites de alcance y la ida y vuelta con Claude Code, plantillas para el brief previo al prompt y para el sistema de diseño reutilizable, y ejemplos trabajados del ciclo de diez opciones y remezcla y de diseños que construyen sus propias herramientas.
- `guides/visual-ideation-before-building.{en,ko,es,ja}.md` — el recorrido completo en cuatro idiomas.

## Fuente
[How the product designer who built Claude Design uses it to explore ideas before building them](https://claude.com/blog/how-the-product-designer-who-built-claude-design-uses-it-to-explore-ideas-before-building-them) — Nate Parrott, 24 de julio de 2026
