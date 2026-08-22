[English](./work-around-the-work.en.md) · [한국어](./work-around-the-work.ko.md) · **Español** · [日本語](./work-around-the-work.ja.md)

# El trabajo alrededor del trabajo

Un recorrido por el estudio de Anthropic de mayo de 2026 sobre el uso de Claude
Cowork, y por lo que la forma de esa distribución dice sobre lo que los
trabajadores del conocimiento delegan en realidad.

## Por qué existe el estudio

Cuando Claude Code se lanzó en 2025, a Anthropic le sorprendió cuántos usuarios no
técnicos empezaron a experimentar con él. Personas que nunca habían abierto un
terminal lo usaban para crear agentes que organizaban carpetas, eliminaban archivos
duplicados y escribían fórmulas de hoja de cálculo.

Para otros, el terminal seguía siendo un lugar algo intimidante: literalmente una
"caja negra". Claude Cowork se construyó para llevar las capacidades agénticas de
Claude Code a la misma interfaz de chat que la gente ya usaba para hablar con
Claude.

Desde el lanzamiento en enero, Cowork se ha convertido en una herramienta
especialmente potente para quienes trabajan en la creación e intercambio de
información: el llamado trabajo del conocimiento. El estudio pregunta qué hace esa
población con un agente.

## Lo que muestran los datos

La muestra: 1,2 millones de sesiones anonimizadas y agregadas entre el 11 y el 31
de mayo de 2026, de más de 600.000 organizaciones, clasificadas por un sistema
automático en una taxonomía de 20 categorías de trabajo.

| Categoría | Cuota |
| --- | --- |
| Procesos de negocio y operaciones | 33,4% |
| Creación de contenido y redacción | 16,4% |
| Desarrollo de software | 8,7% |
| DevOps e infraestructura | 7% |
| Investigación e inteligencia | 6,4% |
| Análisis de datos e inteligencia de negocio | 5,8% |
| Procesamiento y extracción de documentos | 4,1% |
| Ventas y operaciones de ingresos | 4% |
| Asistencia personal | 3,8% |
| Educación | 2,4% |
| Inteligencia de reuniones y conversaciones | 1,8% |
| Legal y cumplimiento | 1,3% |
| Atención al cliente | 0,8% |

**Procesos de negocio y operaciones** encabeza con un 33,4%: reunir actualizaciones
dispersas en un único informe, construir listas de verificación de incorporación,
conciliar hojas de cálculo. Tiene sentido, porque las tareas de operaciones
atraviesan muchos puestos distintos: quienes trabajan en finanzas, RR. HH. y
administración recurren todos a ellas.

**Creación de contenido y redacción** sigue con un 16,4%: comunicación de negocio
intensiva en síntesis, como borradores, presentaciones, publicaciones y propuestas.
Enfrentarse a una página en blanco suele ser la primera barrera para empezar, y un
agente resulta útil para hilar ideas e información en un borrador. Estas tareas
también cruzan puestos: marketing, comunicación, desarrollo de negocio y gestión de
proyectos caen aquí.

Todo lo demás queda por debajo del 9%. Entre las categorías por debajo del 4% están
asistencia personal (3,8%), educación (2,4%) e inteligencia de reuniones (1,8%).

## Cómo usan la IA los trabajadores del conocimiento

Es revelador que las dos categorías principales sumen aproximadamente la mitad de
todo el uso. Ambas son abrumadoramente conectivas:

- Las hojas de cálculo reúnen datos dispersos en un contexto donde se pueden leer,
  comparar y seguir.
- Las presentaciones transmiten una idea o decisión a un público amplio con
  distintos niveles de contexto.
- Las listas de incorporación ayudan a una persona recién llegada a acceder al
  conocimiento institucional.

La lectura que ofrece Anthropic: la gente usa Cowork para reunir y estructurar la
información con la que después aplica su experiencia. Tres ejemplos del post:

- Un **abogado** delega el formato y la presentación de documentos, y gana tiempo
  para aplicar su juicio legal a los casos difíciles.
- Un **responsable de contratación** delega la agenda de reuniones y la síntesis de
  comentarios de entrevistas, y gana tiempo para conversar con candidatos y evaluar
  muestras de trabajo.
- Un **jefe de equipo** delega la presentación que explica una decisión difícil, y
  queda libre para tomar realmente esas decisiones.

La frontera es coherente en los tres casos: el ensamblaje y la estructura pasan al
agente; la experiencia se queda con la persona.

## El contraste con Claude Code

Este patrón es casi el inverso del uso de Claude Code. Claude Code lo usan sobre
todo desarrolladores de software para las partes centrales de su puesto: construir,
depurar y desplegar código. Así que no sorprende que el desarrollo de software
represente una porción tan pequeña del uso de Cowork: un 8,7%.

Los desarrolladores tienen mucha más probabilidad de usar Claude Code que Cowork
para escribir código. Lo que hacen en Cowork es el trabajo conectivo y comunicativo
que rodea a todos los puestos, incluida la ingeniería de software.

Por tanto, una cuota baja de desarrollo de software en un agente de chat es el
resultado esperado de la especialización de herramientas, no evidencia de escasa
adopción por parte de los desarrolladores.

## El auge de la IA en el trabajo del conocimiento

Programar sigue siendo — comprensiblemente — el uso de IA que más atención recibe.
Pero el uso de IA para el trabajo cotidiano de negocio va en aumento, y las tareas
en las que más ayuda se van perfilando: informes de estado, presentaciones,
seguimientos y el resto de la maquinaria que rastrea y comunica información entre
equipos.

Anthropic lo presenta como una única instantánea de un producto nuevo y de rápida
evolución, pensada como punto de referencia para quienes intentan integrar la IA en
su trabajo diario, con más datos prometidos a medida que el uso cambie.

## Leer las cifras con responsabilidad

Aquí la guía es la propia sección de metodología del post.

**Cómo se midió.** Un sistema automático clasificó sesiones en una taxonomía de 20
categorías, con una herramienta de análisis que preserva la privacidad y mantiene
anónima toda la información de usuario. Ningún analista humano leyó una sesión
individual; solo se usaron estadísticas agregadas por categoría. El muestreo fue
con tope: un máximo fijo de sesiones por hora, no un porcentaje fijo del tráfico.

**Granularidad de la taxonomía.** La taxonomía clasifica por el trabajo realizado,
no por el cargo de quien lo hace. No hay categorías propias para marketing,
finanzas ni RR. HH.; esas funciones quedan mejor representadas por "procesos de
negocio y operaciones", lo que probablemente contribuye a que ocupe un tercio del
uso.

**Cuotas frente a volúmenes.** Como el muestreo tiene tope, los recuentos de
sesiones y organizaciones no reflejan el uso total ni el crecimiento, y las horas
de mayor actividad quedan algo infrarrepresentadas frente a las tranquilas.

**Elección de la ventana.** Se usaron tres semanas completas recientes en lugar de
un periodo más largo porque las cuotas por categoría se movieron alrededor del 11
de mayo de un modo compatible con un cambio en la canalización de etiquetado, no
con un cambio de comportamiento. Las cuotas publicadas se calcularon íntegramente
tras ese cambio y son correctas bajo cualquiera de las dos explicaciones.

**Mezcla de uso laboral y personal.** La muestra cubre el uso en organizaciones
externas, no de individuos, pero incluye algo de uso personal: asistencia personal,
aficiones y conversaciones de compañía suman en conjunto cerca del 5% de las
sesiones.

**Clasificación automática.** Las etiquetas provienen de un sistema automático, no
de un revisor humano, y cualquier clasificador puede errar. Cuando una sesión podía
encajar de forma plausible en varias categorías, el resultado dependió de las
definiciones de la taxonomía.

## Qué llevarse

- Delega primero el ensamblaje y la estructura: ahí ya se concentra la masa
  publicada del uso.
- Conserva el juicio: la decisión legal, la evaluación del candidato, la decisión
  que explica la presentación.
- Espera que un agente de código y uno de chat muestren mezclas de uso opuestas, y
  no lo leas como un problema de adopción.
- Cuando publiques tus propios datos de uso, publica los límites junto a las cuotas.

## Fuente

[How people are using Claude Cowork](https://claude.com/blog/how-people-are-using-claude-cowork) — 7 de julio de 2026
