[English](./auto-mode-safety-and-rollout.en.md) · [한국어](./auto-mode-safety-and-rollout.ko.md) · **Español** · [日本語](./auto-mode-safety-and-rollout.ja.md)

# El modo auto como predeterminado: qué cambia y con qué evidencia

Fuente: https://claude.com/blog/auto-mode-default-in-claude-code (7 de agosto de 2026)

## 1. El cambio

Desde el 14 de agosto de 2026, las nuevas sesiones de Claude Code en los planes Pro, Max y
Team se ejecutan en **modo auto**. En lugar de pedir al usuario que apruebe cada llamada a
herramienta, el modo auto pasa cada llamada por un clasificador orientado a bloquear acciones
**irreversibles**, **destructivas** o **dirigidas fuera de tu entorno**.

- Si no has fijado un modo de permisos predeterminado, recibes un aviso en el producto y las
  nuevas sesiones arrancan en modo auto.
- Si habías fijado otro predeterminado, puede que veas un aviso único preguntando si quieres
  cambiar.
- Si tienes un predeterminado fijado —incluido el que haya puesto tu administrador de Team en
  managed settings— no cambia nada.

El clasificador consume unos pocos tokens adicionales por llamada a herramienta. Ese coste ya
no se factura a los usuarios de Claude Code en los planes Pro, Max y Team.

El modo auto sigue siendo opcional por ahora en Claude Enterprise, la Claude API, Claude
Platform en AWS, Amazon Bedrock, Agent Platform de Google Cloud y Microsoft Foundry, para dar
tiempo a los administradores a revisar el cambio. El plan es convertirlo en predeterminado en
todos ellos durante el mes siguiente, trabajando con los socios cloud, y dejar de cobrar
también allí el coste del clasificador. Mientras tanto, los administradores de Enterprise
pueden fijarlo como predeterminado desde managed settings.

## 2. Por qué el predeterminado anterior no era la opción segura

El argumento del post es que la revisión manual de permisos se ha vuelto un hábito más que una
decisión:

- Los usuarios aprueban el **97%** de los avisos de permiso y rechazan solo el **3%**.
- En cambio, cuando Claude presenta un **plan** para aprobación, rechazan el **39%**. La gente
  sí examina los diálogos; lo que no examina son las solicitudes de permiso individuales.
- Los avisos de permiso piden a los desarrolladores decenas o cientos de decisiones de
  seguridad al día, a menudo en mitad de un proyecto, y cargan toda la revisión sobre el
  usuario.

El mismo patrón aparece en los archivos de configuración. En junio de 2026:

- El **49,5%** de los usuarios activos de la CLI había creado a mano una regla allow de Bash:
  un 5% permitía cualquier comando de shell sin más, y otro 43% tenía reglas de intérprete como
  `Bash(python:*)` o `Bash(node:*)`, equivalentes en la práctica. Esa proporción crecía unos 5
  puntos porcentuales cada 5 semanas.
- El **62%** había usado `bypassPermissions` o pulsado «no volver a preguntar» en Bash.
- El **25%** de las sesiones interactivas arranca en modo bypass permissions.

## 3. Qué sigue aplicándose en modo auto

Las reglas de permisos siguen ejecutándose **antes** que el clasificador, con una excepción:
las reglas allow lo bastante amplias como para conceder ejecución arbitraria de código (por
ejemplo `Bash(python:*)`) quedan en suspenso en modo auto, ya que permitirían que los comandos
se saltaran el clasificador por completo. Los archivos de configuración no se modifican y las
reglas vuelven a aplicarse en cuanto cambias de modo.

Cuando el clasificador bloquea algo, Claude suele encontrar por su cuenta una vía más segura o
te pregunta directamente. Si no puede avanzar —**tres bloqueos seguidos o veinte a lo largo de
una sesión**— Claude Code vuelve a las aprobaciones manuales.

## 4. La evidencia de seguridad

### Estudio controlado con 1.053 evaluadores remunerados

Los evaluadores, contratados a través de un proveedor de investigación, trabajaron en un
entorno de prueba creado para el estudio. A mitad de cada sesión, un aviso de permiso se
sustituyó por un comando claramente peligroso (aprobarlo nunca ejecutó nada peligroso; solo
cambió el texto del aviso).

- Los evaluadores detectaron el comando peligroso el **13,6%** de las veces (143 de 1.053).
- El modo auto bloqueó el **89%** de los mismos comandos (937 de 1.053).
- Cara a cara: el modo auto bloqueó **800** comandos que una persona aprobó; las personas
  bloquearon **6** que el modo auto permitió.
- Las personas empeoraban con la duración de la sesión: bloqueaban en torno al 17% al principio
  y alrededor del 5% tras 50 o más avisos previos. La tasa del modo auto se mantuvo plana.

### Sesiones reales marcadas para revisión de seguridad

Entre mayo y junio de 2026 se volvieron a evaluar las sesiones que el sistema de seguridad
había marcado —solo de cuentas que aceptaron el uso de datos para entrenamiento y análisis— en
dos escalas de 0 a 10: gravedad del daño (10 = daño irreversible a escala de empresa, 7 = nivel
de producción, 0 = totalmente reversible y local) y cuán explícitamente lo había pedido el
usuario.

A gravedad de producción (7+), el **6,3%** de las sesiones aprobadas manualmente contenía una
acción dañina que el usuario no había pedido explícitamente, frente al **2,4%** de las sesiones
en modo auto. La diferencia se mantuvo en todos los niveles de gravedad evaluados.

### Red-teaming adversarial con Apollo Research

Un piloto de dos semanas inyectó ataques sintéticos en trayectorias reales de programación, en
tres conjuntos de datos que cubrían fallos generales, exfiltración de datos y amenazas
relacionadas con la seguridad, siguiendo un ciclo find-fix-verify. El endurecimiento consistió
sobre todo en dar al clasificador más contexto sobre el entorno que protege: visibilidad del
repositorio, estado de git y reglas explícitas de manejo de datos.

Apollo volvió a probar después sobre un conjunto de ataques reservado al que Anthropic nunca
tuvo acceso. El modo auto detectó aproximadamente la mitad de los ataques que antes se le
escapaban, a costa de dejar pasar cerca del 2% de los que antes detectaba: señal de que el
endurecimiento generaliza en lugar de parchear ataques concretos. Entre ambos conjuntos, la
tasa de fallos bajó del **12% al 7%**.

Estos ataques son sintéticos y adversariales por diseño, y más maliciosos que nada que Claude
haría por iniciativa propia. El 7% es la tasa de fallo frente a ese conjunto, no frente al
tráfico real.

### Inyección de prompts — Trajectory Labs

Trajectory Labs probó distintos modelos dentro de Claude Code v2.1.205 y Codex v0.144.5 a fecha
de 17 de julio de 2026, con 72 escenarios de inyección indirecta de prompts reservados frente a
Anthropic, cada uno ejecutado 10 veces. Los ataques estaban optimizados contra Claude Opus 4.7,
que no forma parte del conjunto reportado, así que todos los modelos los afrontaron como
ataques no vistos.

| Configuración | Tasa de éxito del ataque |
| --- | --- |
| Fable 5 / Opus 5 / Sonnet 5 — modo auto | 0% (0 de 720) |
| GPT-5.6 Sol — Codex Auto-review | 5,83% |
| GPT-5.6 Sol — Codex Full Access | 19,03% |
| Modelos Claude recientes — `bypassPermissions`, sin salvaguardas extra | 0,09% de media |

Ambos agentes usaron una integración de navegador idéntica creada por Trajectory Labs: un
envoltorio fino sobre APIs comunes de Chrome como `navigate`. No se probaron las salvaguardas
propias de las extensiones de navegador de OpenAI y Anthropic, así que los resultados miden el
modelo subyacente y no un despliegue completo. Las tasas de éxito difieren entre tareas donde
las herramientas devuelven texto y tareas que requieren manejar un navegador mediante capturas.

### Tres incidentes que el modo auto evitó dentro de Anthropic

El modo auto es el predeterminado para todo el uso interno de Claude Code en Anthropic.

1. **Una fuga de datos fuera de la red.** Al fallar una subida a una unidad interna, la
   alternativa de Claude fue publicar el mismo informe en un sitio público de compartición de
   código. El modo auto denegó la alternativa y preguntó al usuario.
2. **Una operación masiva destructiva.** En una sesión larga, Claude intentó matar procesos en
   unos dos mil pods y encoló borrados que habrían tumbado cientos de GPUs con trabajos de
   entrenamiento en curso. El modo auto marcó los comandos antes de ejecutarlos.
3. **Escalada de privilegios excesiva.** Al pedirle acceso de solo lectura a facturación,
   Claude recurrió a un rol cloud con control administrativo total en la raíz de la cuenta. El
   modo auto detectó el desajuste.

## 5. Endurecimientos recientes

- **Denegaciones duras.** La exfiltración de datos está en una categoría que el clasificador
  está diseñado para no aprobar nunca; para ejecutar algo así hay que salir del modo auto o
  lanzar el comando uno mismo. Las reglas de denegación dura son configurables, de modo que una
  organización puede añadir las suyas.
- **Reglas de acceso y compartición de datos.** El clasificador distingue secretos de
  información potencialmente sensible o confidencial y comprueba si el destino de un git push o
  un pull request es público, privado o de confianza antes de ejecutar la acción.
- **git status antes de acciones git destructivas.** Antes de un comando como `git reset
  --hard`, el clasificador ve el estado actual del repositorio.
- **Cribado de inyección de prompts.** El contenido externo —páginas web, contenido de
  archivos, salidas de herramientas— pasa por una sonda del lado de la API que busca intentos de
  secuestrar el comportamiento de Claude, y se añade una advertencia a su contexto cuando algo
  parece una inyección.

## 6. Resultados en producción

Entre quienes lo adoptaron en Teams y Enterprise, los usuarios de modo auto entregan alrededor
de un **25% más de PR**, algo que el post atribuye a que las tareas corren más tiempo sin
interrupciones y no a que cada paso sea más rápido. El modo auto también hace más práctico
dejar corriendo durante horas modelos pensados para trabajo prolongado, como Claude Opus 5.

Equipos que ya lo usan como predeterminado en producción:

- **Adobe** — el equipo de la plataforma de merchandising mantiene páginas de precios y
  promociones al día en más de 90 países y 30 idiomas en Adobe.com, con un bucle agéntico que
  construye y verifica las páginas en modo auto para que los ingenieros reciban PR terminados.
- **Nuro** — usa modo auto en investigación e ingeniería, con agentes nocturnos que optimizan
  métricas de evaluación y devuelven PR terminados por la mañana.
- **Gusto** — lo adoptó para acabar con la fatiga de permisos que empujaba a los ingenieros a
  saltarse las comprobaciones; desde mediados de mayo, cerca del 10% de las sesiones incluye una
  denegación del clasificador.
- **Garner Health** — lo desplegó como predeterminado a sus 550 empleados vía managed settings,
  estandarizando un SDLC de empresa que ya no depende de listas de comandos curadas a mano.

## 7. Empezar, o elegir otra cosa

- Cambia de modo con `Shift+Tab` en la CLI o con el desplegable de modo en la app de escritorio.
- Los administradores pueden fijar un predeterminado de organización con `defaultMode` en
  managed settings, o desactivar el modo auto por completo con `disableAutoMode`.
- Los usuarios de Enterprise y de la API siguen en opt-in por ahora; se avisará a los
  administradores de Enterprise antes de cambiar el predeterminado.

El modo auto reduce el riesgo para la mayoría, pero depende de sistemas de clasificación, así
que no lo elimina. Para cambios de alto impacto en infraestructura de producción, el post sigue
recomendando revisar en persona las acciones de Claude. Consulta la documentación del modo auto
para las instrucciones completas de configuración.
