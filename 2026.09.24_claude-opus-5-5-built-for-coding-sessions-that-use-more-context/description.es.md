[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un post que explica por qué Claude Opus 5.5 —que según las estimaciones cuesta un 40 % menos que Opus 5
en cargas típicas facturadas por token— ahorra más en sesiones largas de Claude Code con mucho
contexto. Comparte tendencias agregadas de uso de Claude Code entre marzo y septiembre de 2026, desglosa
el ahorro en precios, mejor uso de la caché en el arnés de Claude Code y menos turnos, y termina con
hábitos para proteger las lecturas en caché.

## ¿Cuándo es útil?
- Cuando el gasto en Claude Code facturado por token crece y quieres saber a dónde va.
- Cuando las sesiones son largas o desatendidas y quieres mantener alta la tasa de aciertos de caché.
- Al decidir qué tareas conviene asignar a Opus 5.5.

## Puntos clave
- Tendencias (mar→sep 2026): Claude trabaja 3,3× más por prompt, con más de un 40 % más de llamadas al
  modelo y un 68 % menos de interrupciones; los servidores de herramientas y las skills son el doble de
  comunes; el contexto por solicitud creció 2,6× y la proporción entrada:salida pasó de 189:1 a 324:1.
- Precios: tokens de entrada y salida −20 %, lecturas en caché −60 %. Las lecturas en caché son la mayor
  parte del coste del coding agéntico, así que el recorte pesa más a medida que crece el contexto.
- Arnés de Claude Code: la entrada que no acierta en caché bajó más de un 50 %; es más difícil romper la
  caché (refrescar el login, añadir instrucciones a mitad de conversación, cargar herramientas bajo
  demanda); en Opus 5.5 y Fable 5.1 se puede cambiar el nivel de esfuerzo sin reiniciar la caché; hay
  caché de una hora para usuarios de API y proveedores cloud; los subagentes bifurcados reutilizan la
  caché del padre.
- Menos turnos: Zeta Labs vio menos turnos y llamadas a herramientas con casi la mitad de coste y el
  doble de sus tareas más difíciles completadas. La ganancia es mayor en tareas abiertas; mídelo en tu
  propio código.
- La generación de salida es más de un 30 % más rápida que en Opus 5.
- Hábitos: usa `/usage` para ver tu proporción de lecturas en caché; elige el modelo al inicio de la
  sesión; compacta antes de ausentarte; configura la caché de una hora con clave de API o proveedor cloud.

## Recursos incluidos
- Skill: `protect-cached-reads` — hábitos para mantener eficientes en caché las sesiones largas de
  Claude Code y elegir el trabajo para Opus 5.5, con una referencia de tendencias de uso y precios.

## Fuente
- https://claude.com/resources/articles/claude-opus-5-5-built-for-coding-sessions-that-use-more-context
