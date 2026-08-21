[English](./agent-capability-selection.en.md) · [한국어](./agent-capability-selection.ko.md) · **Español** · [日本語](./agent-capability-selection.ja.md)

# Elegir capacidades para un agente en producción

El uso de computadora (computer use), la Skills API y la Files API están
disponibles de forma general en la Claude Platform desde el 2026-08-20, y el uso
de computadora incorpora una nueva herramienta de uso de navegador. Esta guía
trata de cómo elegir entre ellas.

## Las tres preguntas que responde este lanzamiento

Un agente que hace trabajo real suele necesitar tres cosas además del modelo:

1. **Una forma de actuar sobre software que no expone una API.** → uso de
   computadora, o la herramienta de uso de navegador en la web.
2. **Una forma de llevar la experiencia de tu equipo a la ejecución.** → la
   Skills API.
3. **Una forma de conservar documentos entre turnos y devolver artefactos
   terminados.** → la Files API.

La ejecución de código y la búsqueda web, ya disponibles de forma general,
encajan en el mismo bucle.

## Actuar sobre software

El **uso de computadora** construye agentes que operan el software que pueden
ver. Dada una captura de pantalla, el agente hace clic, escribe y desplaza igual
que alguien frente al teclado, que es precisamente lo que le permite funcionar en
aplicaciones que nunca se diseñaron para ser automatizadas.

La **herramienta de uso de navegador**, nueva en este lanzamiento, lo extiende a
la web. Junto a la captura, el agente lee la estructura de la página y actúa
sobre un campo o botón concreto en lugar de sobre una posición en pantalla.

El orden de decisión:

| Situación | Elección |
| --- | --- |
| Existe una API real | Usa la API: más barata, más rápida, determinista |
| Aplicación web sin API | Herramienta de uso de navegador |
| Escritorio u otra superficie sin navegador y sin API | Uso de computadora |

Ambas herramientas ejecutan ahora **varias acciones por turno** en vez de una por
llamada al modelo, así que las tareas terminan en menos llamadas y menos tiempo.

**Por qué la estructura gana a los píxeles.** Apuntar a un elemento con nombre
sobrevive a cambios de maquetación, diferencias de resolución y re-renderizados
que mueven un control unos píxeles. En la web, la ruta estructural es la mejora
de fiabilidad, y no te cuesta los turnos multi-acción.

## Llevar la experiencia

Una **skill** es una carpeta de instrucciones, scripts y plantillas que Claude
carga solo cuando la tarea lo requiere. La Skills API te deja subir y versionar
tus propias skills y adjuntarlas a cualquier petición; se ejecutan en el entorno
aislado de ejecución de código de Claude, así que no hay nada que alojar.

De esa forma se derivan tres cosas:

- **Carga bajo demanda.** La experiencia codificada no tiene que competir por
  espacio en el prompt de cada petición.
- **Versionado.** Un procedimiento obtiene su propio historial de cambios,
  separado del código de aplicación que lo invoca. Es la diferencia entre una
  cadena de prompt que alguien editó el trimestre pasado y un artefacto con
  versión.
- **La skill es la superficie de personalización.** El caso de Box es la
  ilustración más clara: un único Box Agent con una skill por firma que captura su
  metodología crediticia y su formato de memo aprobado, en vez de un agente hecho
  a medida desde cero por cada flujo.

## Conservar documentos

La **Files API** es almacenamiento para los documentos que un agente lee y
escribe: sube un PDF o una hoja de cálculo una vez, refiérela por ID en peticiones
posteriores en lugar de reenviarla, y descarga los archivos que el agente crea. La
disponibilidad general añade expiración automática de archivos, límites de tasa 5
veces mayores y 1 TB de almacenamiento por organización.

La referencia por ID es lo que cambia el diseño. Un flujo multi-turno deja de
retransmitir el mismo documento fuente en cada petición, y el entregable pasa a
ser un artefacto que recuperas en vez de texto que extraes de una respuesta.

## El bucle compuesto

El ejemplo trabajado del anuncio, un agente de reclamaciones:

1. Lee el documento de ingreso desde la Files API.
2. Sigue una skill que codifica el procedimiento de presentación del equipo.
3. Completa el envío en el portal web de una aseguradora con la herramienta de
   uso de navegador.
4. Guarda la confirmación de vuelta como archivo.

Delimita tu propio agente recorriendo las mismas cuatro preguntas en orden: qué
lee, el procedimiento de quién sigue, qué software debe operar y qué entrega.

## Resultados reportados

- **Sistemas de salud y seguros sin API.** Con la nueva herramienta de uso de
  computadora, el flujo de reclamaciones más largo de un equipo pasó de 32
  minutos a 13, el coste por tarea cayó cerca de un 30% en todos los flujos
  probados y la finalización llegó al 100%, sin cambios en sus prompts.
- **Box.** Una skill captura la metodología crediticia de un banco y su formato de
  memo aprobado; Box Agent la aplica a los estados financieros y documentos de
  operación que ya están en Box y produce un memo de crédito con fundamento en las
  fuentes para revisión del analista.

Fíjate en el límite del segundo caso: la salida es *para revisión del analista*.
En dominios donde un error es un evento de cumplimiento, el trabajo del agente
termina en un artefacto revisable.

## Disponibilidad

| Superficie | Estado |
| --- | --- |
| Claude Platform | Uso de computadora, uso de navegador, Skills API, Files API |
| Microsoft Foundry | Skills API y Files API |
| Google Cloud Vertex AI | Uso de computadora actualizado y uso de navegador próximamente |

El uso de computadora ahora es apto para cargas de trabajo reguladas por HIPAA
bajo el BAA de Anthropic. Las integraciones beta existentes siguen funcionando
mientras migras. Consulta la documentación de la plataforma sobre uso de
computadora, la herramienta de uso de navegador, la Skills API y la Files API para
empezar.

## Fuente

[Build production agents with computer use, the Skills API, and the Files API](https://claude.com/blog/computer-use-skills-api-files-api) (publicado el 2026-08-20).
