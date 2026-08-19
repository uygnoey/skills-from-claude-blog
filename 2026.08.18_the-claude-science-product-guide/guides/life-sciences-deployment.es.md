[English](./life-sciences-deployment.en.md) · [한국어](./life-sciences-deployment.ko.md) · **Español** · [日本語](./life-sciences-deployment.ja.md)

# Desplegar un banco de trabajo de investigación con IA en ciencias de la vida

Una guía práctica de despliegue, destilada de la guía de producto de Claude Science.

## El problema que aborda

El Life Sciences Outlook 2026 de Deloitte, una encuesta a 280 líderes de biofarma y medtech, encontró que el 78% espera que la IA tenga un papel central en impulsar cambios importantes este año — y sin embargo solo el 14% declara una implementación completa de herramientas de IA en los flujos de trabajo diarios, con otro 40% todavía avanzando hacia ello. La investigación interna de Anthropic, basada en entrevistas con investigadores de química, física, biología y campos computacionales, encontró que el 91% de los científicos quiere más IA en su investigación, mientras que el 79% señaló la confianza y la fiabilidad como su barrera número uno para adoptarla.

La brecha es estructural. El día de un biólogo abarca literatura, diseño experimental, preparación de datos, análisis, figuras y escritura, pero las herramientas abarcan PubMed, Jupyter, R, una terminal de clúster, visores de datos científicos y hojas de cálculo. Los laboratorios que van por delante no son los que tienen más cómputo o el equipo de bioinformática más grande: son los que han acortado la distancia entre la pregunta de un científico y un resultado defendible.

## Paso 1 — Elegir la superficie antes que el despliegue

Claude Science es la superficie construida para científicos. Las demás cubren el trabajo documental, de software y empresarial que rodea al descubrimiento. La mayoría de las organizaciones despliega más de una, y la línea divisoria fiable es el **resultado**:

| Resultado | Superficie |
|---|---|
| Un análisis, una figura, un resultado | **Claude Science** — app local en macOS/Linux, con despacho a SSH, SLURM o cómputo en la nube |
| Una respuesta rápida o un borrador | **Claude Chat** — navegador, escritorio, móvil |
| Un documento que abarca carpetas y aplicaciones | **Claude Cowork** — app de escritorio sobre archivos locales y sistemas conectados |
| Redacción y revisión en el propio Office | **Claude for Microsoft 365** — complementos más el conector de M365 |
| Software que se entrega a otros equipos | **Claude Code** — terminal e IDE |
| Una integración de sistemas (ELN, LIMS, CTMS, seguridad, RWE) | **Claude Platform** — API, incluida vía Bedrock, Vertex AI y Foundry |
| Un agente alojado y de larga duración | **Claude Managed Agents** — permisos acotados y trazado completo de ejecución |

Ten esta conversación con los responsables funcionales antes de la primera instalación, para que redacción médica, regulatorio y computación científica sepan qué recibirán y cuándo.

## Paso 2 — Entender dónde se ejecuta

Claude Science es una aplicación independiente para macOS y Linux que ejecuta un **daemon local con su interfaz en el navegador**: el mismo modelo que un cuaderno Jupyter, salvo que conduce el agente. Se instala allí donde viven los datos: un portátil, una máquina Linux del laboratorio, un nodo de login HPC o una VM en la nube dentro de tu tenencia. Los datos, los entornos de cómputo y los agentes permanecen en esa máquina; los científicos se conectan desde el navegador de su portátil a través de un túnel SSH cuando el daemon corre en remoto.

Cuando un trabajo necesita hardware mayor, el agente lo despacha desde la misma sesión a la caja GPU del laboratorio, un host SSH, un clúster SLURM (SLURM se detecta automáticamente y las directivas de lote se escriben solas) o una cuenta de GPU serverless que aporte el usuario.

Los agentes pueden apuntarse a cualquier carpeta local — archivos FASTQ, objetos AnnData, objetos Seurat — y conectan de forma nativa con S3, GCS, GitHub y el acceso institucional a literatura. Los entornos Conda y pip se gestionan por especialista; sesiones, kernels y artefactos persisten entre reinicios.

## Paso 3 — Saber qué hace defendible el análisis

Cinco decisiones de diseño permiten que el resultado sobreviva a la revisión:

1. **Kernels persistentes.** Un conjunto de datos se carga una vez en un kernel de Python o R y a partir de ahí se explora, no se recarga. Los agentes además ven sus propias gráficas: cada figura vuelve al contexto del agente, así que hace QC sobre su propia salida.
2. **Procedencia en cuatro capas para cada artefacto.** Una descripción legible de lo que se hizo, el código reproducible exacto, la conversación y el razonamiento que llevaron ahí, y una instantánea de cada paquete y versión utilizados.
3. **Un revisor en segundo plano.** Un agente revisor independiente lee la transcripción de cada sesión mientras el agente principal trabaja y marca toda afirmación que no pueda rastrear hasta la evidencia, en línea junto a la frase sospechosa. Se ejecuta en cada sesión por defecto.
4. **Plan antes de la acción, permisos visibles.** Cada tarea se redacta como un plan paso a paso que espera aprobación; el plan permanece visible como una lista editable. Cada nuevo sitio web, carpeta o ejecución de código levanta una tarjeta de aprobación — una vez, para este proyecto o siempre — revisable y revocable desde una sola pantalla. Debajo hay un sandbox a nivel de sistema operativo con egress de red denegado por defecto y un intermediario de aprobación humana que controla trece tipos de acción.
5. **Salvaguardas de bioseguridad integradas.** Las reglas de bioseguridad se incluyen incondicionalmente en el prompt de sistema de todo agente, un clasificador de trayectoria biológica por turno corre dentro del binario y no se puede desactivar, y el producto completó red-teaming externo y la revisión de Anthropic Safeguards antes del lanzamiento público.

## Paso 4 — Sentar las bases

Como el producto se ejecuta localmente, la fase de fundación consiste en ponerlo junto a los datos y el cómputo correctos, no en levantar una tenencia en la nube.

- **Decidir el patrón de host del daemon** y confirmar que los científicos pueden alcanzar ese host desde su navegador.
- **Que TI de investigación revise** el sandbox a nivel de SO, la lista de dominios permitidos con egress denegado por defecto, y el intermediario de aprobación humana que controla ejecución de código, acceso a archivos y cómputo remoto.
- **Configurar cuentas**: el mismo trabajo de SSO y SCIM que en cualquier otra superficie, más un paso extra — un administrador debe habilitar Claude Science antes de que nadie pueda descargarlo o iniciar sesión. En Team, en ajustes de administración → capacidades. En Enterprise, crear un rol que incluya el permiso de Claude Science, asignarlo al grupo piloto y *después* habilitar la capacidad, de modo que el acceso quede acotado desde el primer día.
- **Acotar el gobierno en paralelo.** Para grupos que trabajan con datos controlados del NIH, datos a nivel de paciente o propiedad intelectual del patrocinador que no puede salir de las máquinas del laboratorio, el modelo de daemon local es lo que hace posible el despliegue donde un producto SaaS no lo sería — pero calidad, seguridad de TI y privacidad de datos deben revisar la huella de instalación, la lista de dominios permitidos y los destinos de despacho de cómputo antes de que el primer científico apunte a una carpeta de datos controlados.
- **Elegir equipos piloto** con un responsable motivado que ya esté empujando la IA y cuyo trabajo sea intensivo en análisis y de forma estándar. Los grupos de biología computacional y bioinformática son el punto de partida natural; los científicos de laboratorio húmedo y los PI llegan rápido en cuanto ven a un colega ejecutar un análisis que ellos no habrían podido hacer.

> **Consejo:** la primera sesión importa. Un científico que abre la herramienta, la apunta a una carpeta de archivos FASTQ, aprueba el plan y obtiene un UMAP agrupado con el código y el entorno capturados debajo, volverá. Un científico que la abre sin datos al alcance la cerrará. Asegúrate de que la instalación aterrice junto a datos reales.

## Paso 5 — Ejecutar el piloto contra criterios definidos

En esta fase los campeones ejecutan análisis reales sobre datos reales del laboratorio, medidos contra criterios definidos de antemano:

- **Tiempo de ciclo** — cuánto tardaba el análisis piloto antes y cuánto tarda ahora, sobre la misma clase de conjunto de datos.
- **Tasa de aceptación** — con qué frecuencia un científico o un PI confía en el resultado sin volver a ejecutarlo a mano.
- **Tasa de reproducción en frío** — entregar el paquete de procedencia de un artefacto de la semana uno a otro científico distinto en la semana cuatro y confirmar que puede reejecutarlo en frío.

**La señal cualitativa más fuerte es que los campeones empiecen a guardar sus propias skills.** Un bioinformático envuelve el pipeline de normalización interno del laboratorio para que toda sesión futura lo herede; un responsable de grupo envuelve la API del LIMS. Esas skills se convierten en el catálogo del laboratorio y pueden compartirse por toda la organización.

Las superficies adyacentes suelen activarse en esta fase: redacción médica y regulatorio piden Cowork y los complementos de Microsoft 365; computación científica pide Claude Code para los pipelines de producción aguas abajo. Ejecútalas como vías paralelas en lugar de condicionarlas al piloto científico.

> **Consejo:** programa revisiones semanales con los equipos piloto. Los casos límite aparecen rápido — un esquema de base de datos que el conector no maneja, una peculiaridad del planificador del clúster, un visor que no cubre un formato de nicho — y el catálogo está diseñado para extenderse en respuesta.

## Paso 6 — Escalar, con el gobierno resuelto primero

Las skills y especialistas que funcionaron durante el piloto se despliegan a más grupos, y TI de investigación pasa de instalaciones por laboratorio a un patrón de despliegue gestionado: un host de daemon estándar por grupo, una lista de dominios verificada, un catálogo de skills curado a partir del piloto y un conjunto definido de destinos de despacho de cómputo.

Las skills se acumulan entre grupos porque gran parte de la biología computacional comparte estructura: una skill de célula única construida en oncología está a medio camino de una construida en inmunología. Los nuevos incorporados empiezan el primer día con los pipelines codificados del laboratorio en lugar de construirlos desde cero.

Decidir antes de escalar, no después:

- quién es el dueño de cada skill del catálogo,
- cómo se hace QC de una skill antes de compartirla más allá del grupo de su autor,
- cómo se retienen los paquetes de procedencia de los análisis que alimentan resultados regulatorios o publicaciones,
- cómo se revisa la lista de dominios permitidos cuando un grupo solicita una nueva base de datos externa.

> **Consejo:** para los análisis que alimentarán una presentación regulatoria o una publicación, trata el paquete de procedencia de cuatro capas como un registro controlado. La descripción, el código, la conversación y la instantánea del entorno juntos son lo que un revisor, un auditor o una revista querrán ver — acordad dónde se almacenan y durante cuánto tiempo.

## Resumen por fases

| Fase | Acciones | Qué verás |
|---|---|---|
| **Fundación** | Revisión de TI y gobierno de datos sobre instalación local, sandbox y lista de dominios. Decidir el patrón de host del daemon. Identificar 2–3 grupos campeones en biología computacional o bioinformática. Confirmar SSO/SCIM y el plan. | Campeones reportando casos de uso. Los primeros momentos de "esto me habría llevado tres semanas". |
| **Piloto** | Los campeones ejecutan análisis reales con datos reales. Revisiones semanales. Medir tiempo de ciclo, tasa de aceptación y reproducción en frío. Levantar Cowork y M365 en paralelo para las funciones documentales adyacentes. | Ahorros de tiempo medibles. Campeones guardando skills y especialistas propios. Científicos de laboratorio húmedo y PI sumándose detrás de los líderes computacionales. |
| **Escala** | Patrón gestionado de host del daemon. Catálogo de skills organizativo curado. Lista de dominios verificada y destinos de despacho definidos. Política acordada de retención de procedencia para análisis regulados y destinados a publicación. Incorporar la siguiente oleada de grupos. | Skills compartidas entre áreas terapéuticas. Nuevos incorporados arrancando sobre pipelines codificados. Menos solicitudes de "¿alguien me ayuda a ejecutar esto?" al núcleo de bioinformática. |

## Cómo se ve en el terreno

- **Novo Nordisk** construyó NovoScribe, una plataforma de IA generativa impulsada por Claude que automatiza la creación de informes de estudios clínicos, protocolos de verificación de dispositivos y materiales para pacientes. Documentación clínica que antes llevaba más de diez semanas alcanza ahora un primer borrador revisable en unos diez minutos. "Claude nos ha ayudado a recortar los tiempos de escritura de los CSR en un 90% para poder poner la documentación directamente en manos humanas para su revisión y aprobación." — Waheed Jowiya, Digitalization Strategy Director, Novo Nordisk
- **El Garvan Institute of Medical Research** ha adoptado Claude en investigación, operaciones y administración, con más de veinte ingenieros de software y científicos de datos usando herramientas de desarrollo agénticas para investigación en descubrimiento de fármacos, diagnóstico de enfermedades raras mediante sistemas multiagente que interpretan variantes genéticas, y análisis de datos en proyectos de genómica. "Claude Code ha transformado por completo mi forma de trabajar como científico y como líder." — Daniel MacArthur, Professor, Garvan Institute
- **Sanofi** ha desplegado Claude en toda la empresa dentro de su aplicación interna Concierge, hoy usada a diario por la mayoría de sus empleados a lo largo de la cadena de valor.

## Límites conocidos, a declarar desde el principio

La guía es explícita sobre las fronteras, y declararlas pronto es lo que evita que un piloto se atasque en una pregunta de cumplimiento sin respuesta:

- Solo uso en investigación; **no está diseñado para decisiones clínicas o diagnósticas**.
- **No es un sistema validado** para GxP. Despliégalo en roles de investigación, análisis y apoyo a borradores, con un revisor cualificado aprobando cada salida antes de que entre en un registro validado, una presentación o una publicación.
- **No está listo para HIPAA en el lanzamiento**; esa preparación está en la hoja de ruta posterior.
- Los conjuntos de datos de acceso controlado del NIH suelen exigir que el propio entorno de análisis cumpla los controles NIST SP 800-171; el producto aún no ha sido evaluado frente a ese estándar.
- **Windows no está soportado**; la instalación en el endpoint es un daemon firmado en espacio de usuario más una interfaz de navegador, sin componentes de kernel.
- **No está disponible a través de Amazon Bedrock, Google Vertex AI ni Microsoft Foundry.**
- **Zero Data Retention no aplica** — el producto tiene estado, ya que sesiones, artefactos y paquetes de procedencia requieren almacenamiento para funcionar. ZDR está disponible en Claude Platform y Claude Code para clientes aprobados.
- El uso es **intensivo en tokens**; los usuarios individuales intensivos pueden necesitar límites de nivel Max. No hay licencia aparte ni capa gratuita: consume del plan existente del usuario.
- Las bases de datos públicas y los recursos de terceros tienen sus propias licencias; verificar la idoneidad para uso comercial es responsabilidad de la organización.
- Los elementos de la hoja de ruta pueden cambiar y no representan un compromiso.

## Fuente

- https://claude.com/blog/the-claude-science-product-guide
