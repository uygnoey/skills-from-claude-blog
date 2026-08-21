[English](./cost-visibility-and-control.en.md) · [한국어](./cost-visibility-and-control.ko.md) · **Español** · [日本語](./cost-visibility-and-control.ja.md)

# Visibilidad y control de costes en Claude

## Formas útiles de pensar el coste

Mide el **coste por resultado**, no el consumo de tokens. Los tokens son una entrada: te dicen
cuánta maquinaria se puso en marcha, no si produjo algo que valga la pena.

Vale la pena hacerse dos preguntas sobre cualquier proyecto:

1. **¿Cuánto habría costado este trabajo sin IA** — en recursos, en tiempo, o teniendo en cuenta
   si el proyecto se habría intentado siquiera? El tercer caso es el que suele saltarse. Un
   trabajo que nunca se habría iniciado no tiene un predecesor más barato con el que compararse.
2. **¿El modelo está haciendo tareas que requieren juicio y razonamiento, o procesando volumen
   alto y sencillo?** Las respuestas correctas son distintas, y la diferencia no es de volumen.

La segunda pregunta importa porque un modelo mal emparejado cuesta dinero en ambas direcciones.
Asignar modelos menos capaces a razonamiento complejo a menudo *aumenta* el coste final: los
tokens se van en reintentos y después el tiempo humano se va en correcciones. La tarifa por token
baja mientras el coste por resultado sube. En sentido contrario, desplegar modelos de frontera
para procesamiento documental básico paga por capacidades que la tarea no requiere.

## La familia de modelos

Cuatro modelos principales, emparejados con distintos tipos de trabajo:

- **Fable** — los problemas más difíciles
- **Opus** — trabajo de horizonte largo y programación
- **Sonnet** — trabajo cotidiano y análisis
- **Haiku** — tareas rutinarias y de alto volumen

Dos herramientas adicionales hacen que la elección no sea binaria. Los **controles de esfuerzo**
ajustan cuánto "piensa" el modelo al resolver un problema, de modo que un modelo capaz con
esfuerzo bajo es un punto de coste distinto al del mismo modelo con esfuerzo alto. El enfoque de
**asesor** permite que modelos más pequeños consulten a modelos de frontera solo cuando se topan
con un problema difícil: la mayor parte de la carga corre barata y solo los momentos duros
escalan.

## Controles de coste para Claude Enterprise

Los administradores de TI tienen tres controles, y la secuencia recomendada es deliberada: cada
capa reduce lo que la siguiente tiene que gobernar.

**El control de acceso** determina qué grupos y roles personalizados pueden acceder a qué
productos, como Claude Code y Claude Cowork. Hacerlo primero permite un despliegue por fases por
departamento en lugar de un interruptor para toda la organización. El objetivo no es restringir de
forma permanente, sino aprender cómo es el uso real de un departamento antes de que se sume el
siguiente.

**Los controles de modelo** funcionan en dos niveles. Los *entitlements* especifican a qué modelos
puede acceder un equipo. Los *valores por defecto* fijan el modelo con el que arrancan las
conversaciones nuevas. Juntos permiten reservar los modelos más capaces para equipos con trabajo
complejo y dejar a los demás en Sonnet por defecto. Los valores por defecto hacen más trabajo del
que parece: la mayor parte del uso sigue al valor por defecto, así que fijar uno sensato mueve más
gasto que cualquier restricción de entitlements.

**Los topes de gasto duros** colocan techos de uso a nivel de organización, de usuario individual
o de grupo. La semántica de grupo conviene leerla con cuidado: cada miembro recibe el límite
indicado, de modo que un tope de grupo no es un fondo común que agota quien más gasta. Los topes
surten efecto de inmediato, y eso es lo que los distingue de una alerta de presupuesto.

Los administradores también pueden automatizar las solicitudes de aumento de límite, identificar a
quienes se acercan a su tope y seguir patrones de uso que cambian rápido.

## Herramientas para observar el uso

**La analítica de uso** desglosa el gasto por persona, equipo y modelo. Las exportaciones se
alinean con las facturas, lo que la convierte en la herramienta específica para la conciliación
de facturación.

**La API de analítica** entrega los mismos datos a los sistemas de negocio existentes:
herramientas de inteligencia de negocio, sistemas financieros y paneles internos. Todo lo que
acabes exportando de forma periódica pertenece aquí.

**El chat de analítica** responde preguntas de uso en lenguaje natural, sin generar un informe
completo:

> Who are our top spenders this month?

> Which team's usage grew fastest this quarter?

Es la herramienta para las preguntas que surgen en medio de otra cosa. Su valor está en la
ausencia de un ciclo de informes entre la pregunta y la respuesta.

## Controles para construir sobre la API

La Claude Console ofrece cuatro palancas, y varias de ellas se acumulan.

**La caché de prompts** almacena contenido reutilizable entre peticiones, reduciendo el
reprocesamiento a en torno al 10% de la tarifa normal de entrada en los aciertos de caché. Rinde
allí donde un prefijo grande y estable se repite en muchas llamadas: un prompt de sistema, una
taxonomía, un esquema, un documento de referencia.

**El procesamiento por lotes** ejecuta trabajos no urgentes a mitad de precio; la clasificación
nocturna de catálogos es el caso canónico. Los descuentos por lote se acumulan con la caché, y por
eso mover un trabajo masivo recurrente a lotes suele ser el mayor ahorro individual disponible.

**El parámetro de esfuerzo** controla la intensidad de razonamiento por llamada. Los ajustes bajos
sirven para enrutado y extracción; los altos, para la recomendación final. La idea es elegir
*cuándo* pagas procesamiento a tarifa máxima, en lugar de pagarlo de forma uniforme en todo el
pipeline.

**La estrategia del asesor** usa un modelo más pequeño como Sonnet para la mayor parte del trabajo
y consulta a un modelo de frontera solo en los puntos de decisión críticos, pagando tarifas
premium únicamente en los momentos de más juicio.

En un pipeline masivo estas palancas se componen en orden: pásalo a lotes, cachea el prefijo
estable, baja los pasos mecánicos a esfuerzo bajo y escala a un modelo de frontera solo donde
realmente se decide algo. Cada capa actúa sobre una parte distinta de la factura, así que los
ahorros no compiten entre sí.

## Cómo empezar

Los controles de coste están disponibles actualmente en Claude Enterprise. Los planes y precios
están en [claude.com/pricing](https://claude.com/pricing); se puede empezar con Enterprise
directamente en [claude.ai/create/enterprise](https://claude.ai/create/enterprise); y la
documentación de Workspace, caché y lotes está en [docs.claude.com](https://docs.claude.com).

## Fuente

- [A Guide to Cost Visibility and Control in Claude](https://claude.com/blog/a-guide-to-cost-visibility-and-control-in-claude), 2026-08-04
