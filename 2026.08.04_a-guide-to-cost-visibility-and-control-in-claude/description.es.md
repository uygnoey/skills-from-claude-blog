[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Guía de visibilidad y control de costes en Claude

## ¿De qué trata este post?

Una guía para administradores de TI y desarrolladores sobre cómo ver y controlar lo que una
organización gasta en Claude. Su tesis central: el **coste por resultado**, y no el consumo de
tokens, es la métrica principal correcta de valor — y la mayoría de los problemas de coste son,
en realidad, problemas de emparejamiento de modelo disfrazados.

La guía cubre cuatro superficies: cómo pensar el coste en primer lugar, los controles de
administración disponibles en Claude Enterprise (control de acceso, controles de modelo, topes
de gasto duros), las herramientas para observar el uso (analítica de uso, la API de analítica y
el chat de analítica) y las palancas disponibles para quien construye sobre la API (caché de
prompts, procesamiento por lotes, el parámetro de esfuerzo y la estrategia del asesor).

## ¿Cuándo es útil?

- Al desplegar Claude Code o Claude Cowork en una organización y decidir quién accede primero.
- Al fijar un presupuesto y necesitar que el gasto se detenga realmente ahí.
- Al conciliar el gasto con las facturas o al alimentar sistemas de BI o finanzas con datos de uso.
- Al decidir en qué modelo debe correr una carga de trabajo, y si un modelo más barato lo es de
  verdad.
- Al reducir el coste de una carga de trabajo en producción sin sacrificar calidad donde importa.

## Puntos clave

- **Mide el coste por resultado, no los tokens.** Dos preguntas para cualquier proyecto: ¿cuánto
  habría costado este trabajo sin IA, contando recursos, tiempo o incluso si se habría intentado
  siquiera?, y ¿el modelo está haciendo trabajo de juicio y razonamiento o procesando volumen
  alto y sencillo?
- **Un modelo mal emparejado cuesta más en ambas direcciones.** Poner un modelo menos capaz en
  razonamiento complejo suele subir el coste final por los reintentos y la corrección humana.
  Poner un modelo de frontera en procesamiento documental básico paga por capacidades que la
  tarea no usa.
- **Cuatro modelos, cuatro tipos de trabajo.** Fable para los problemas más difíciles, Opus para
  trabajo de horizonte largo y programación, Sonnet para el trabajo del día a día y análisis,
  Haiku para tareas rutinarias y de alto volumen.
- **Controles de empresa, en orden:** primero *control de acceso* (qué grupos y roles
  personalizados pueden usar qué productos, para desplegar por departamentos en vez de a toda la
  organización), luego *controles de modelo* (entitlements sobre a qué modelos llega cada equipo,
  y valores por defecto para las conversaciones nuevas), y por último *topes de gasto duros*
  (techos a nivel de organización, usuario o grupo; cada miembro de un grupo recibe el límite
  indicado; los topes surten efecto de inmediato).
- **Herramientas de observación.** La analítica de uso desglosa el gasto por persona, equipo y
  modelo, con exportaciones alineadas con las facturas. La API de analítica lleva los mismos
  datos a los sistemas de BI, finanzas y paneles existentes. El chat de analítica responde
  preguntas de uso en lenguaje natural — "¿Quiénes son nuestros mayores gastadores este mes?",
  "¿Qué equipo creció más rápido este trimestre?" — sin generar un informe completo.
- **Palancas del lado de la API.** La caché de prompts almacena contenido reutilizable entre
  peticiones y puede dejar los aciertos de caché en torno al 10% de la tarifa normal de entrada.
  El procesamiento por lotes ejecuta trabajos no urgentes a mitad de precio y se acumula con la
  caché. El parámetro de esfuerzo ajusta la intensidad de razonamiento por llamada. La estrategia
  del asesor ejecuta la mayor parte del trabajo en un modelo más pequeño y consulta a un modelo
  de frontera solo en los puntos de decisión críticos.
- **Los administradores también pueden** automatizar las solicitudes de aumento de límite,
  identificar a quienes se acercan a su tope y seguir patrones de uso que cambian rápido.

## Recursos incluidos

- `skills/cost-aware-model-selection/SKILL.md` — el procedimiento de decisión como Agent Skill.
- `skills/cost-aware-model-selection/references/model-family.md` — qué modelo encaja con qué trabajo.
- `skills/cost-aware-model-selection/references/enterprise-controls.md` — los tres controles de
  administración y el orden de aplicación.
- `skills/cost-aware-model-selection/references/api-cost-controls.md` — caché, lotes, esfuerzo y
  la estrategia del asesor.
- `skills/cost-aware-model-selection/templates/cost-per-outcome-review.md` — una hoja de trabajo
  para evaluar una carga de trabajo.
- `skills/cost-aware-model-selection/examples/usage-questions.md` — preguntas de analítica y para
  qué sirven.
- `guides/cost-visibility-and-control.es.md` — la guía completa en cuatro idiomas.

## Fuente

- [A Guide to Cost Visibility and Control in Claude](https://claude.com/blog/a-guide-to-cost-visibility-and-control-in-claude) — publicado el 2026-08-04
