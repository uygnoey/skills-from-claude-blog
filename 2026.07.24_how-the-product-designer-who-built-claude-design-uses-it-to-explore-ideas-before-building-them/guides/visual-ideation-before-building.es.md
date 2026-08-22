[English](./visual-ideation-before-building.en.md) · [한국어](./visual-ideation-before-building.ko.md) · **Español** · [日本語](./visual-ideation-before-building.ja.md)

# Ideación visual antes de construir

Cómo surgió Claude Design, para qué sirve y para qué no, y las diez prácticas que
su creador usa a diario.

## El problema: el diseño se volvió el cuello de botella

En otoño de 2025, Nate Parrott era el único diseñador de producto en Claude Code
para VS Code, trabajando con dos ingenieros para reimaginar todo lo que hace Claude
Code en una interfaz amable fuera del terminal. La beta salió a finales de
septiembre, Opus 4.5 llegó en noviembre y el equipo empezó a lanzar rápido y con
fuerza.

"Los ingenieros lanzaban mucho más que antes, mientras yo seguía entregando al
ritmo de siempre. Necesitaba encontrar la manera de ponerme al día."

## El primer intento fallido

Claude Code corre en el terminal, donde todo es texto, y el primer intento trató el
diseño igual: copiar la salida en Claude, añadir capturas y preguntar "Aquí hay una
función que queremos añadir. ¿Por qué no la diseñas?".

Los resultados no eran buenos. Durante un mes aproximadamente, como proyecto
paralelo, la búsqueda de una forma de mejorar la salida de diseño continuó.

## El avance: el HTML como medio

Al final: Claude se maneja muy bien con HTML. Y el HTML no es solo el formato de
los sitios web — "también es un medio visual rico e interactivo: cualquier cosa que
puedas hacer en una presentación, un archivo de vídeo o un PDF, la puedes hacer en
una página web".

Siguieron dos movimientos:

1. **Una vista dividida.** Pedir HTML, chat a la izquierda, salida en vivo a la
   derecha.
2. **La marca en el prompt.** El diseño de producto consiste en aplicar el
   conocimiento del producto y la marca con los que trabajas, así que la esencia de
   la marca de Anthropic — tipografías, colores, recursos y principios de sus
   productos — se destiló en prompts. A partir de ahí, la salida cumplía la guía de
   marca por defecto.

Los diseñadores adoptaron el prototipo interno de inmediato, en particular para
prototipos interactivos. Hacer un prototipo clic a clic en herramientas de diseño
tradicionales implica maquetar cada estado de cada pantalla y conectarlos a mano.
Aquí le entregas tus recursos a Claude y le dices: haz que funcione. Y cada
artefacto que entrega tiene un enlace que compartes como compartirías un documento.

## De proyecto paralelo a proyecto real

El momento en que quedó claro fue una sesión de presentación de ideas en un offsite
del equipo de Anthropic Labs: "todos los presentes montaron sus diapositivas con
ella, a menudo en mitad de la reunión, justo antes de su turno". Esa sesión
convenció al equipo de Labs para asignarle personas.

El encuadre se amplió. Dejó de ser una herramienta para maquetas de producto y pasó
a ser una herramienta para producir cualquier forma de comunicación visual:
presentaciones, landing pages, one-pagers que imprimes en PDF, correos,
animaciones, visuales para redes sociales. Parrott lo describe como "un clic por
encima del diseño de producto: colaboras con Claude en visuales cuya función
principal es comunicar e idear".

La capacidad sigue a los modelos de visión. Claude Opus 5 lee mejor que los Opus
anteriores gráficos, diagramas y capturas de pantalla, lo que lo hace potente junto
a Claude Design para presentaciones y memorandos de calidad expositiva.

## Lo que no pretende hacer

**Diseño de logotipos.** No hay modelo de imagen ni está construido para generación
de imágenes, así que encaja mal con los logos — "aunque eso no ha impedido que la
gente lo intente". El mejor enfoque es traer el logo y los recursos que ya tienes.
El resto del producto funciona igual: Claude crea opciones y puntos de partida para
que no tengas que mirar un lienzo en blanco, y tú eliges lo que funciona por sí
solo o como combinación de varias versiones.

**Software de producción.** Si vas a lanzar software de producción, quédate con
Claude Code. Claude Code es para programar; Claude Design es para las otras partes
del trabajo de diseño: ideación temprana, colaboración o conseguir aprobación de
una dirección antes de que nadie se comprometa a construirla.

Las dos van y vienen. Sincroniza a Claude Design un prototipo que empezaste en
Claude Code para iterarlo y editarlo en el lienzo, o pasa de Claude Design a Claude
Code un prototipo listo para construirse.

Y por eso importa la frontera: "A medida que los modelos mejoran construyendo
software de producción, el trabajo que más importa se desplaza hacia el principio
del proceso: tener buenas ideas, alinear a todo el mundo y recoger opiniones
mientras la idea aún es temprana."

## Uso diario

Trabajo de diseño de todos los días: wireframear ideas tempranas o generar 15
versiones de un flujo para recoger opiniones de colegas. Ejemplos recientes:

- **La animación de introducción.** La animación que se reproduce al registrarte se
  hizo en la propia herramienta, pero no directamente: "No soy animador, así que
  primero hice que Claude Design me construyera un editor de vídeo a medida, y
  luego usé ese editor para hacer la animación."
- **Una app de horarios de metro** con controles de animación ajustables, para
  afinar la física del movimiento.
- **Controles de color estilo Instagram** — ajustar la paleta de una app con
  deslizadores y presets en vez de describir colores con palabras.
- **Un rediseño de Claude Design.** Con dos compañeros, Helen y Andrew, exploran un
  nuevo diseño del editor dentro de la propia herramienta. No lo lanzarán tal cual;
  es su forma de explorar en qué podría convertirse el producto.

## Las diez prácticas

1. **Piensa antes de escribir el prompt.** Dile a Claude lo que necesitas por
   adelantado. Parrott dedica mucho tiempo a escribir prompts antes de diseñar: los
   dicta con el botón de voz, los teclea en la app de Notas desde el sofá o graba
   una nota de voz durante un paseo y pega la transcripción después. Decide lo que
   quieres lejos del ordenador, para que Claude ejecute exactamente esa visión
   cuando te sientes.
2. **Dile a Claude cómo debe verse.** "Sin dirección, Claude elige una de sus
   estéticas favoritas. Probablemente las reconocerías." Anticípate especificando
   tipografías y colores, aportando un moodboard, o pidiendo combinaciones de
   tipografía y color hasta dar con una que encaje.
3. **Convierte el trabajo recurrente en un sistema de diseño.** Sube tus archivos y
   recursos de marca — logos, presentaciones, capturas, especificaciones
   tipográficas y todo lo que reutilices — y Claude los analizará y generará un
   sistema de diseño. Así cada artefacto parte de tus decisiones y no de cero.
4. **Pide diez opciones y luego remezcla.** La mayoría no servirá, y está bien; una
   o dos sí. Entonces: "Me gusta la opción B y un poco de la D. Dame cinco
   variaciones que mezclen las dos."
5. **Dibuja lo que no puedes describir.** Si tienes un layout en la cabeza y no
   encuentras las palabras, dibújalo en papel y sube una foto.
6. **Señala y habla.** En vez de escribir un párrafo identificando el elemento,
   haz clic en él y habla. Activa el dictado en tu dispositivo, selecciona
   "comment" y entra en el cuadro de comentario; tus palabras aparecen como si las
   escribieras.
7. **Wireframe primero cuando la fidelidad no importa.** Es mucho más rápido y
   mantiene a Claude centrado en la estructura de alto nivel en lugar de en lo
   visual: una gran manera de probar muchas ideas deprisa.
8. **La última milla, a mano.** Usa las herramientas de edición directa —
   reordenar, borrar, editar texto, redimensionar, cambiar colores — para los
   retoques finales en vez de pedirlos. "Las ediciones directas no consumen tokens,
   y decisiones pequeñas como el tamaño y la alineación se aprecian mejor a ojo."
9. **Dale a Claude tu contexto real.** Si diseñas una función para una app o web
   existente, conecta GitHub: Claude recuperará tus componentes y pantallas y los
   usará como punto de partida, y con unos intentos puede recrear tus diseños
   existentes con bastante fidelidad. La búsqueda web y las conexiones MCP también
   funcionan cuando el diseño depende de información externa.
10. **Sigue trabajando junto a Claude.** No tienes que esperar a un resultado
    terminado para pedir nuevos cambios o tareas. Puedes encolar varios mensajes a
    la vez o seguir hablando mientras Claude trabaja en el turno anterior.

## Hazlo vivo

Hay una charla de Bret Victor que todo diseñador debería ver en algún momento:
"Stop Drawing Dead Fish". De su resumen: "Todo lo que dibujamos debería estar vivo
por defecto."

Parrott anima a los diseñadores, en esta herramienta o en cualquier otra, a pensar
en cómo hacer que sus creaciones estén vivas. Sus creaciones favoritas son las que
no caben en las cajas existentes: documentos con simulaciones interactivas,
presentaciones que te hablan, diagramas que también son vídeos, diseños que son su
propio editor. El código, en concreto el HTML, es un medio increíble para la
creatividad, y por fin resulta bastante fácil de usar para los diseñadores.

Claude Design adoptó su forma actual porque en Anthropic la gente no dejaba de
encontrarle usos que él no había previsto. Ahora está en beta en los planes Claude
Pro, Max, Team y Enterprise, con una invitación: "llévala a algún sitio en el que
no hayamos pensado todavía".

## Fuente

[How the product designer who built Claude Design uses it to explore ideas before building them](https://claude.com/blog/how-the-product-designer-who-built-claude-design-uses-it-to-explore-ideas-before-building-them) — Nate Parrott, 24 de julio de 2026. El artículo expresa sus opiniones, patrones de uso y consejos.
