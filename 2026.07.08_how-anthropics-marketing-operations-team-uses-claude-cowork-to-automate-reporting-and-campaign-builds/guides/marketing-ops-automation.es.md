[English](./marketing-ops-automation.en.md) · [한국어](./marketing-ops-automation.ko.md) · **Español** · [日本語](./marketing-ops-automation.ja.md)

# Automatizar marketing operations con Claude Cowork

Cómo dos personas del equipo de marketing operations de Anthropic convirtieron días de
trabajo manual entre plataformas en horas.

## El problema del trabajo de marketing ops

Los equipos de marketing operations dedican una parte considerable de su tiempo a
mantener alineados con el negocio los sistemas que sostienen los programas de
marketing. La automatización está claramente en su ámbito y, sin embargo, buena parte
del trabajo es de todo menos automático: las herramientas de martech no se integran
limpiamente entre sí, los informes se consolidan a mano y las landing pages se crean de
una en una.

Ian Chan dedicaba uno o dos días por semana a montar la revisión semanal de métricas de
marketing. Annabel Custer, centrada en operaciones de campaña, configuraba cada nuevo
evento haciendo clic en secuencia por Salesforce, HubSpot, Swoogo y herramientas de
email. Ambos han comprimido días de trabajo manual en horas montando flujos en Claude
Cowork.

Las horas recuperadas cambiaron la forma de su trabajo. Ahora dedican menos tiempo a
hacer clic por los sistemas y más a enablement, validación y a los datos y procesos de
base de los que depende el equipo de marketing, a medida que más gente en la empresa
saca sus propios números y lleva sus propios programas.

---

## Parte 1 — el informe semanal de métricas

### Por qué llevaba dos días

En un mundo perfecto, cada métrica del informe semanal viviría en un dashboard y el
trabajo sería escribir la narrativa. En la práctica:

- Algunas métricas ya están en el dashboard.
- Otras aún no han llegado allí desde el data warehouse.
- Otras todavía no se han canalizado al warehouse.
- Las nuevas pueden existir solo en un mensaje de Slack o en la transcripción de una
  llamada.

El negocio se mueve más rápido de lo que un pipeline de reporting tradicional puede
seguir. Ian dedicaba entre uno y dos días cada semana a rastrear datos y validarlos.

### La tarea programada del domingo por la noche

Una tarea programada se ejecuta cada domingo por la noche y pide a Claude:

1. Leer la revisión de la semana anterior.
2. Leer la última transcripción de reunión.
3. Mirar en Slack en qué está enfocado el equipo de ventas.
4. Consultar el warehouse.
5. Dejar una carpeta con los números y algunas áreas de foco sugeridas.

El lunes por la mañana Ian abre Claude Cowork y saca el informe inicial, que contiene
las tablas de métricas y los titulares sugeridos.

### La decisión humana, después la expansión

Ian revisa las áreas de foco sugeridas. Una vez que ha confirmado o decidido dónde
centrar la narrativa, le dice a Claude que las expanda con detalles de apoyo y ejemplos.
Algunas semanas el equipo responde a una prioridad de ventas, otras a un lanzamiento de
producto. En el cambio de trimestre le indica encabezar con los planes trimestrales y le
pasa el documento de revisión trimestral.

Claude genera la diapositiva para el liderazgo a partir de los mismos datos y la misma
narrativa: qué cambió, por qué, y qué están haciendo los equipos al respecto. Los
seguimientos se convierten en tareas de Asana.

### Cuando los números no cuadran

Claude señala el desajuste en lugar de adivinar. Tras una reorganización del equipo de
ventas, el reporting de marketing dejó de coincidir con el suyo. Claude sacó la
diferencia a la luz y preguntó a Ian cómo tratarla.

### Sobre qué se apoya

Conectores a las plataformas y herramientas de marketing que usa el equipo, más tres
skills que Ian ha construido y actualiza continuamente:

- **Una skill de preparación** dirige el ensamblado del informe, incluidos el foco, los
  titulares y la expansión con detalle de apoyo.
- **Una skill de corrección** comprueba cada número del borrador contra una fuente
  verificada.
- **Una skill de action items** convierte los seguimientos en tareas de Asana.

### Cerrar el bucle cada semana

Al final de cada sesión semanal, Ian pide a Claude que resuma lo que surgió y debería
volver a las skills: la nueva estructura tras la reorganización de ventas, las
correcciones que hizo, una nueva forma de plantear los titulares.

Todo el proceso, que llegaba a llevar dos días, ahora lleva como mucho dos horas.

### A dónde fue el tiempo recuperado

Una parte importante del tiempo de Ian se ha desplazado a ayudar a los marketers a
formular sus preguntas, afinar sus prompts e interpretar lo que reciben cuando sacan sus
propios números con Claude. También tiene margen para profundizar en la capa de datos,
asegurándose de que Claude interpreta los números, las definiciones y las estructuras
regionales igual que el data warehouse.

La validación humana se ha vuelto parte integral de ambos flujos, un cambio que se
acelera a medida que Claude automatiza las tareas manuales rutinarias que
tradicionalmente ocupaban buena parte del tiempo de los analistas de marketing.

---

## Parte 2 — builds de eventos e importaciones de datos

### Por qué era manual

Montar la infraestructura detrás de las campañas de marketing ha sido tradicionalmente
uno de los procesos más manuales del área. Cada evento, webinar o campaña integrada
debe configurarse en el CRM, en la plataforma de automatización de marketing que ejecuta
las secuencias de email y la automatización asociada, y en la plataforma de gestión de
eventos que aloja la página de registro y la landing page del evento. Cada una suele ser
de un proveedor distinto, y las integraciones entre ellas rara vez están completas.

Antes de Claude Cowork, Annabel recogía cada solicitud de un canal de Slack dedicado y
recorría la secuencia a mano.

### Entrada y despacho

Su configuración empieza con un formulario de entrada donde quien solicita especifica el
tipo de ayuda que necesita: build de evento, importación de datos, apply-to-attend o
soporte de aprobaciones.

Una vez por hora, una skill dispatcher lee el canal, escoge la solicitud más urgente,
marca el ticket para que el trabajo no se duplique y lo entrega a una de las cinco skills
especialistas. Ella misma no configura ningún evento; su función es decidir qué se
ejecuta a continuación, y mantenerla separada permite a Annabel refinar cada especialista
por su cuenta sin tocar el enrutado.

### El build del evento

Para un build de evento —el tipo de solicitud más complejo— una skill de event build se
encarga de la secuencia completa de extremo a extremo: creación de la campaña en el CRM,
campaña en la plataforma de automatización con sus workflows y listas, configuración de
la plataforma de eventos, redacción de emails, generación de la landing page y todas las
integraciones entre ellas.

La skill deja escritas dos actualizaciones en Slack: cuando Claude toma la solicitud y
cuando la landing page está lista para la revisión de quien la pidió y la auditoría toma
el relevo.

### La auditoría

Cuando el build termina, se entrega a un nuevo agente para auditoría. El agente de
auditoría empieza sin contexto previo, envía un registro de prueba en la landing page en
vivo, abre el email de confirmación en Gmail y marca la tarea de Asana como completa si
todo se ve bien. Annabel revisa cada resultado antes de que salga.

### Las skills que lo sostienen

Conectores a las plataformas y herramientas de marketing con las que trabaja, más las
skills que ha construido y actualiza a medida que encuentra nuevos casos límite:

- **Una skill dispatcher** lee el canal de entrada y enruta cada solicitud a la skill
  especialista adecuada.
- **Una skill de event build** dirige la configuración de extremo a extremo entre
  plataformas.
- **Una skill de creación de landing pages de webinar** genera páginas para webinars.
- **Una skill de auditoría**, ejecutada por una instancia de Claude nueva y separada,
  verifica la salida de la skill de event build antes de dar la tarea por completa.
- **Una skill de apply-to-attend** gestiona cambios sobre la marcha en el flujo de
  registro.
- **Una skill de soporte de aprobaciones** gestiona las aprobaciones de eventos y envía
  los emails correspondientes con una cadencia programada.
- **Una skill de importación de datos** depura listas y procesa datos de asistentes.

También mantiene abierto un agente "manager" aparte. Cuando una ejecución falla, lo abre
y le pide que mire qué pasó y proponga qué ajustar. Lo que merece la pena conservar vuelve
a la skill correspondiente.

### La motivación fue la calidad, no la velocidad

Aunque estos flujos supondrán un ahorro de tiempo importante, la motivación principal de
Annabel para construirlos fue la calidad del trabajo. A medida que el equipo de marketing
crece, los marketers que clonan páginas de evento desde cualquier plantilla cercana pueden
producir bugs: emails de confirmación con el nombre de ciudad equivocado, landing pages
rotas. Con Claude Cowork consigue consistencia entre builds, a escala.

A medida que Claude asume las partes repetitivas de las operaciones de campaña, Annabel
puede centrarse en proyectos más estratégicos, como el enablement, y en automatizar u
optimizar procesos y arquitectura de campañas para obtener mejores insights.

---

## Consejos para equipos de marketing ops que empiezan

- **Convierte las correcciones repetidas en skills.** Cuando te descubras corrigiendo a
  Claude sobre lo mismo más de una vez, ese feedback pertenece a una skill. Tampoco hace
  falta que las construyas tú: Claude puede hacerlo por ti.
- **Construye primero una skill de corrección.** Comprueba que cada número que Claude pone
  en un informe se remonta a una fuente verificada.
- **Pide a Claude que reflexione.** Claude lee las instrucciones de forma distinta a como
  las escribe una persona, así que tras las primeras ejecuciones de un flujo nuevo,
  pregúntale qué resultó difícil de las instrucciones. Lo que salga vuelve a la skill, como
  parte de una práctica más amplia de actualizarlas constantemente.
- **Apóyate en las tareas programadas.** El trabajo que se ejecuta solo cada domingo por la
  noche o cada hora es trabajo que nadie tiene que recordar.

## Fuente

[How Anthropic's marketing operations team uses Claude Cowork to automate reporting and campaign builds](https://claude.com/blog/how-anthropics-marketing-operations-team-uses-claude-cowork-to-automate-reporting-and-campaign-builds) — Ian Chan y Annabel Custer, 8 de julio de 2026
