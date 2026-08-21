[English](./startup-operating-model.en.md) · [한국어](./startup-operating-model.ko.md) · **Español** · [日本語](./startup-operating-model.ja.md)

# Operar una startup sobre codificación agéntica

Un panorama de cómo más de una docena de startups de rápido crecimiento organizan
su ciclo de vida de desarrollo de producto en torno a Claude Code, y qué conviene
copiar primero.

La pregunta de fondo que plantea la guía: ¿cómo se vería una organización que
construyera su ciclo de vida de desarrollo de producto con Claude Code desde
cero?

## Resultados reportados

| Empresa | Reportado |
| --- | --- |
| ClickHouse | 30% más funcionalidades entregadas |
| Omni | 2–3x de productividad en ingeniería |
| Clay | 100% del triaje de bugs automatizado |
| Artemis Security | Más de 6.000 PR por semana |

## El modelo operativo en cinco reglas

1. **Todo el mundo entrega.** La barrera para producir una primera versión
   funcional baja lo suficiente como para que la construya quien entiende el
   problema.
2. **Automatiza lo tedioso.** Los agentes se hacen cargo del 80% mecánico del
   ciclo de vida.
3. **Confía, pero verifica.** No se puede automatizar lo que no se puede
   comprobar.
4. **Construye para reconstruir.** La capacidad de los modelos cambia bajo tus
   pies; trata el andamiaje como desechable.
5. **Prototipa, usa internamente, productiza.** Construir con IA es como se
   aprende a construir productos con IA.

Las reglas 2 y 3 forman un par. Adoptar la 2 sin la 3 es como los equipos acaban
con código plausible que se desvía de su arquitectura de formas que parecen
correctas pero no lo son.

## Qué cambia a nivel organizativo

**La cadena de traspasos se colapsa.** Heidi llama al camino antiguo el problema
del teléfono descompuesto: idea → PM → diseñador → ingeniero, con la esencia
perdida por el camino y semanas transcurridas. Ahora quien entiende el problema
entrega el PR y suma a diseñadores e ingenieros en las partes donde su
experiencia importa.

**La división del trabajo sobrevive.** Marketing sigue haciendo marketing y
desarrollo sigue desarrollando. Lo que se abre a todos es el paso 0→1.

**Las contribuciones necesitan un camino.** Sin un foro, la contribución de
perfiles no técnicos queda librada a la ambición individual. Clay realiza
revisiones trimestrales donde los prototipos entran en la hoja de ruta formal.
Omni mantiene un canal de Slack para prototipos generados con Claude y acompaña
"todo el mundo entrega" con "todo el mundo habla con clientes", poniendo
deliberadamente a los ingenieros frente al cliente para acortar el ciclo de
retroalimentación.

**Los estándares se mudan a archivos compartidos.** Las skills —archivos de
instrucciones reutilizables que codifican los estándares y el contexto del
equipo— hacen que un proceso democratizado siga produciendo un producto
coherente. Compártelas mediante un directorio o un marketplace de plugins
interno. La postura de Emergent vale la pena adoptarla: un archivo de contexto
algo desactualizado está bien mientras el agente pueda verificarlo y corregir el
rumbo rápidamente.

## Qué cambia a nivel técnico

**Conecta Claude a la fuente de verdad.** No puede entender lo que no puede ver.
Usa MCP allí donde tu equipo esté copiando y pegando entre una herramienta y
Claude; usa la CLI cuando ya exista una herramienta de línea de comandos madura
(`gh`, `kubectl`, `bq`, `psql`) y quieras que el agente trabaje contra la misma
fuente de verdad que tus ingenieros: suele ser más eficiente en tokens.

**Estratifica el contexto.** `CLAUDE.md` en la raíz para lo que no puede cambiar.
`CLAUDE.md` por subdirectorio para las convenciones que aplican siempre en esa
parte del repositorio. Skills para flujos procedimentales bajo demanda.

**Pon agentes en el trabajo recurrente.** Los agentes de tests inestables y de
cobertura faltante de ClickHouse son el segundo y tercer contribuyente de su
repositorio. Clay automatizó el triaje de bugs desde el primer pase hasta la
corrección sugerida. El revisor de Translucent se despliega en abanico sobre un
cambio y sintetiza hallazgos desde múltiples ángulos.

**Automatiza también fuera del SDLC.** El proceso no técnico más comúnmente
automatizado fue la analítica de datos de autoservicio: agentes internos de
analítica, categorización de feedback junto a datos de uso, resumen de miles de
documentos legales con subagentes, barridos de datos de reclamaciones en busca de
anomalías, y minería continua de datos financieros hospitalarios.

**Pon compuertas en las partes deterministas.** Los hooks se disparan en puntos
fijos del ciclo de vida y se ejecutan sin importar lo que decida el modelo:
bloquear una escritura que no pasa el linter, exigir que los tests pasen antes de
un commit, eliminar secretos antes de que algo salga del entorno aislado. Los
flujos de trabajo dinámicos aportan secuenciación determinista con ventanas de
contexto separadas y objetivos acotados; `/goal` ayuda cuando una tarea larga
corre el riesgo de darse por terminada antes de tiempo o de desviarse.

**Haz que reconstruir salga barato.** Los worktrees de git ejecutan la v2 junto a
la v1 en un checkout aislado con su propia rama, compartiendo un único almacén de
objetos: corre las evaluaciones contra ambas y fusiona solo cuando gane la nueva.
El modo plan antes de una reescritura no trivial detecta la desviación antes de
escribir código.

## La verificación es la inversión que habilita todo

Artemis Security atribuye su velocidad de despliegue a la infraestructura de
pruebas, la organización del código y los sistemas de conocimiento, no a los
agentes en sí: estructura eso correctamente y cada contribución se acumula.

Las prácticas concretas:

- **Invariantes por escrito.** Las 567 líneas de Zingage sobre cómo piensa el
  equipo, escritas después de que la autonomía total produjera desviación
  arquitectónica.
- **Bucles con condición de parada autocontenida.** Un agente de tests inestables
  verifica su propia corrección volviendo a ejecutar el test.
- **Revisión experta que mejora el principio.** Cainex canaliza las correcciones
  de los auditores hacia instrucciones de agente versionadas y hace back-testing
  contra un conjunto dorado más muestras aleatorias. "Corrige el principio, no el
  ejemplo." Su primera versión sobreajustaba y acumulaba parches, así que pusieron
  un tope a cuántos casos específicos pueden entrar en un cambio.
- **Múltiples conjuntos de evaluación, mantenidos.** El punto de quiebre para los
  equipos que operan por intuición llega cuando los usuarios reportan que el
  agente empeoró y no hay forma de verificarlo salvo probar y adivinar.

## Secuencia de adopción

1. Escribe los invariantes del `CLAUDE.md` raíz y conecta Claude a tus
   herramientas reales. Sin esto, todo lo demás se desvía.
2. Monta un conjunto dorado y una suite de evaluación para tu caso de uso de
   mayor riesgo.
3. Pon un agente en una tarea recurrente y autoverificable: los tests inestables
   son la primera elección estándar.
4. Abre el camino 0→1 a perfiles no técnicos y crea el foro donde los prototipos
   obtienen prioridad.
5. Añade hooks donde un paso deba ejecutarse idéntico cada vez.
6. Usa worktrees y modo plan para la primera reconstrucción, y termínala: la
   reconstrucción está hecha cuando el camino viejo ha desaparecido.

## Fuente

[The Claude Code guide for startups](https://claude.com/blog/claude-code-guide-for-startups)
por Michael Segner (publicado el 2026-08-20).
