[English](./ai-native-sdlc-playbook.en.md) · [한국어](./ai-native-sdlc-playbook.ko.md) · **Español** · [日本語](./ai-native-sdlc-playbook.ja.md)

# El manual del SDLC nativo de IA

Una guía para transformar el ciclo de vida del desarrollo de software etapa por etapa, a partir de
las prácticas del equipo de Applied AI de Anthropic dentro de la empresa y con sus clientes.

## El código ya no es el cuello de botella

Las organizaciones han empezado a usar IA para escribir código a una velocidad impensable hace un
año, pero los procesos que rodean al código no han cambiado al mismo ritmo. Siguen las mismas
puertas de aprobación, revisiones, traspasos y políticas, frenando las ganancias de productividad
que la codificación agéntica debía traer.

El SDLC tradicional —planificar, diseñar, construir, probar, desplegar, mantener— se diseñó para
maximizar la eficiencia en una época en la que escribir e implementar código era la etapa más lenta
y cara. Los PRD, los rituales de estimación y las revisiones de seguridad de producto existían para
forzar la alineación durante lo que podían ser semanas o trimestres de desarrollo. Además, sus
controles asumen que cada paso lo ejecuta una persona.

Cuando la construcción se comprime a horas, tres cosas se vuelven ciertas:

1. **El cuello de botella se desplaza a los pasos a izquierda y derecha de la construcción**:
   planificación, revisión y pruebas, y despliegue, que siguen funcionando a velocidad humana.
2. **Los controles dejan de corresponder con la realidad.** Revisar cada línea a mano tenía sentido
   cuando una persona la había escrito; no aguanta el ritmo cuando los agentes escriben la mayor
   parte del diff.
3. **El coste de la gobernanza sube**, porque las excepciones siguen pasando por reuniones y comités
   que se reúnen semanal o mensualmente.

La seguridad es el caso más claro. Los equipos de seguridad están dimensionados para la producción
humana, así que cuando los agentes multiplican la salida de código, o bien crece la cola de revisión
o bien se envía código insuficientemente revisado. Una organización regulada no puede aceptar
ninguna de las dos, de modo que sus controles de seguridad y políticas tienen que seguir el ritmo de
los agentes.

## Qué es un SDLC nativo de IA

El SDLC nativo de IA combina los antiguos objetivos de control con una nueva forma de aplicarlos. En
lugar de un flujo lineal, el proceso se convierte en un bucle con IA integrada en cada punto, y el
traspaso entre etapas se automatiza en vez de hacerse a mano.

| Etapa | SDLC tradicional | SDLC nativo de IA |
|---|---|---|
| Planificar | Requisitos recogidos por comité, destilados en talleres y firmas, redactados a mano | Claude sintetiza los problemas directamente desde las fuentes y los captura en `intent.md`, legible por personas y accionable por máquinas |
| Diseñar | Especificación escrita por analistas y reinterpretada por diseñadores | Requisitos y diseño comprimidos en una sola sesión de trabajo con un agente, guiada por estándares codificados como skills y versionada en git |
| Construir | Pruebas y código escritos a mano; la documentación llega después del desarrollo | Pruebas y código generados por IA; el conocimiento institucional se mantiene como archivos `CLAUDE.md` y skills versionados y legibles por máquina |
| Probar | Puertas de QA en los límites de etapa | Evals continuas entretejidas en la implementación |
| Desplegar | Las personas revisan cada línea y la gobernanza ocurre en ciclos de revisión, a menudo de forma inconsistente | Capas de revisión agéntica, con la revisión humana reservada al código regulado y crítico; la gobernanza se aplica mientras la IA actúa, con hooks como puertas de aprobación |
| Mantener | Las personas vigilan producción en busca de errores | Los agentes monitorizan los despliegues en vivo; cualquier banda de control superada se diagnostica y se devuelve al bucle como un nuevo `intent.md` |

La mayoría de las organizaciones están en algún punto entre ambas columnas.

### El artefacto commiteado es el hilo

Cada etapa termina escribiendo un artefacto en el control de versiones, y la siguiente empieza
leyéndolo: `intent.md`, `spec.md`, `plan.md`, el diff y sus pruebas, la PR con sus hallazgos de
revisión y el registro del incidente. En las primeras etapas el artefacto es markdown porque el
responsable de producto y el agente pueden leer y actuar sobre el mismo archivo. A partir de la
construcción, el artefacto es el código y sus registros.

La cadena de commits es también la traza de auditoría: quién pidió qué, qué produjo el agente y
quién lo aprobó. Las personas siguen siendo responsables de toda decisión que requiera juicio; lo
que cambia es sobre qué artefactos recae su atención.

Un `intent.md` aceptado dispara el pase de requisitos y diseño, un `spec.md` aprobado dispara el modo
plan, una PR fusionada dispara el pipeline, y una banda de control superada en producción escribe el
siguiente `intent.md`. Al principio se activa cada paso a mano; el estado final es un bucle en el que
cada artefacto aceptado abre la siguiente puerta.

## Etapa 1 — Planificar: capturar la intención

*Las ideas dejan de esperar a que alguien las redacte.*

Tradicionalmente una idea pasa por entradas de backlog, historias de usuario, story points y
reuniones de refinamiento antes de que nadie pueda actuar sobre ella. La propiedad cambia de manos en
cada traspaso, así que lo que llega a ingeniería está a varios pasos de lo que quería quien la
propuso.

En su lugar, quien la propone hace una lluvia de ideas con Claude y escribe el resultado como
`intent.md`: una proto-especificación en sus propios términos, con qué se quiere, por qué y bajo qué
restricciones. No hace falta lenguaje formal. Claude hace las preguntas que haría un analista:
alcance, usuarios, restricciones y qué significa el éxito. La persona corrige lo que Claude haya
malinterpretado y luego commitea el archivo.

**Para empezar.** Sin prerrequisitos. Hace falta acceso a Claude para quienes no son ingenieros
(claude.ai o Cowork), una plantilla acordada y un hogar compartido y versionado que el responsable de
producto vigile. Para un solo producto, lo más simple es una carpeta `intent/` en el repositorio del
producto, lo que mantiene la cadena de artefactos junto al código que se deriva de ella. Un
repositorio dedicado solo compensa cuando la intención abarca muchos repositorios.

Montarlo es una tarea única del equipo de plataforma, que decide además quién puede escribir en él.
Una vez existe el repositorio, quienes no tienen experiencia con git commitean a través de un conector
al sistema de control de versiones desde claude.ai o Cowork.

**Un `intent.md` real:**

```markdown
# Intent: claims status self-service
Author: J. Ortiz (claims operations). Status: draft.

## Problem
Customers phone the contact center to ask where their claim is.
Handlers spend roughly a third of call time on status-only queries.

## Proposed outcome
Customers see claim status, next step and expected date in the portal.

## Affected users and systems
Claims handlers, portal team, claims-core API.

## Constraints
No new PII in the portal session. Existing authentication only.

## Open questions
Do third-party loss adjusters need access too?
```

**Gobernanza.** La evidencia es el archivo commiteado, con autor, marca de tiempo e historial completo
de revisiones en git. El responsable de producto aprueba, y la decisión de aceptar o rechazar queda
registrada como el merge o el cierre de la revisión.

**Medición.** Indicador adelantado: tiempo desde la primera conversación hasta un `intent.md`
commiteado, que debería caer de un ciclo de elicitación de semanas a horas. Indicador rezagado: la
tasa de supervivencia de las intenciones hacia la etapa de diseño, más los cambios hechos a
`intent.md` después del primer commit de `spec.md`.

## Etapa 2 — Diseñar: requisitos y diseño colapsan

Requisitos y diseño son tradicionalmente fases separadas ejecutadas por equipos distintos. La
separación existe por responsabilidad, pero es lenta y pierde información.

Ahora ambas ocurren en una sola sesión. Claude toma el `intent.md` aceptado y produce una
especificación de requisitos y diseño, restringida por las skills de la organización para marca,
seguridad, cumplimiento y UX, con las áreas de preocupación marcadas. El responsable de producto
revisa la especificación, pero no la escribe.

El prompt de partida:

```text
Read the attached intent.md and produce a requirements and design spec for
integrating it into our existing codebase. Apply the skills available to you so
the plan conforms to our brand guidelines, security policies and UX standards.
Document the spec fully as spec.md, ready to hand to the engineering team.
Describe clearly any areas of concern, especially where you cannot satisfy
contradicting policies.
```

Ejecútalo a mano al principio, después codifícalo como un slash command a nivel de organización, y
después haz que la aceptación de la intención sea el disparador de un trabajo no interactivo que
commitea `spec.md` como pull request. A partir de ahí, la primera intervención del responsable de
producto es la revisión.

Trabaja primero las preocupaciones marcadas: son los puntos que un analista habría escalado. Resuelve
cada una con su responsable de política antes de que ingeniería vea la especificación. Commitea
`spec.md` junto a `intent.md`; el par registra qué se pidió y qué se decidió.

El trabajo de front-end es el ejemplo más claro del colapso: el responsable de producto maqueta el
diseño en Claude Design (beta) a partir del `intent.md`, itera sobre la maqueta y la exporta a Claude
Code para construirla.

**Gobernanza.** La política viva se lee y se aplica mientras se escribe la especificación, en lugar de
descubrirse en una revisión semanas después. La especificación, el prompt que la produjo y las
versiones de skills vigentes quedan registradas en el control de versiones.

**Medición.** Adelantado: tiempo transcurrido entre el commit de `intent.md` y el de `spec.md` para el
mismo cambio (dos marcas de tiempo de git). Rezagado: retrabajo de requisitos tras iniciar la
construcción, contando los commits de `spec.md` posteriores al primer commit de `plan.md` del mismo
cambio.

## Etapa 3 — Construir: nada se implementa sin un plan aceptado

### El modo plan como punto de partida por defecto

Tradicionalmente, cómo se hará el cambio —qué archivos, qué pruebas— se queda en la cabeza del
ingeniero o, como mucho, en un comentario del ticket. Lo primero que ve un revisor es el diff
terminado, y para entonces el retrabajo es lento.

En su lugar, el trabajo empieza con un plan escrito que Claude produce en modo plan, donde puede leer
el código sin modificar nada. Dale a Claude `intent.md` y `spec.md` y pide un plan que nombre los
archivos que cambian, el orden del trabajo y las pruebas que lo demuestran. Interrógalo: ¿qué podría
romper esto?, ¿qué paso es el más arriesgado?, ¿qué opciones descartaste? Itera hasta que un ingeniero
que nunca vio la conversación pueda implementar el cambio solo con el plan, y commitéalo como
`plan.md`.

```markdown
# Plan: claims status self-service (from intent.md 2026-06-02)
## Files that change
portal/src/claims/StatusPanel.tsx (new), claims-api/routes/status.py,
claims-api/tests/test_status.py
## Order of work
1. Add the status endpoint behind existing auth.
2. Panel against the endpoint.
3. Wire into the portal nav.
## Risks
The claims-core API rate-limits at 50 rps; the panel must cache.
## Proof
test_status.py covers the four claim states; screenshot matches the
approved mock.
```

Con un plan sólido, la implementación suele ser de una sola pasada. Cuando se aparta del plan,
actualiza `plan.md` en el mismo commit; un hook puede forzar esa sincronización.

El modo plan impone por sí mismo la revisión de diseño: Claude no puede editar archivos hasta que el
ingeniero acepta el plan, así que cambiar de rumbo sigue siendo cuestión de editar un documento.

### Modo automático

Claude Code también puede funcionar en modo automático, aplicando cada cambio sin pedir confirmación
por edición una vez aprobado el plan. A medida que maduran las barreras —un `CLAUDE.md` afinado, skills
que codifican políticas, hooks que bloquean acciones inseguras y una suite de pruebas que Claude puede
ejecutar—, la auto-aceptación se convierte en el valor por defecto para el trabajo rutinario: una
especificación ajustada, un radio de impacto pequeño y código que las pruebas ya cubren. El foco se
desplaza de mirar al agente editar a revisar artefactos tras sesiones autónomas más largas.

### `CLAUDE.md`

`CLAUDE.md` le da a Claude el contexto que necesitaría alguien que acaba de incorporarse: convenciones,
comandos, arquitectura y los errores que el equipo ve más a menudo. El conocimiento que vivía en las
cabezas de la gente y en wikis se convierte en un archivo que el agente lee al inicio de cada sesión.

Ejecuta `/init`, recorta el archivo generado a lo que alguien nuevo necesitaría el primer día y
regístralo en la raíz del repositorio para que todo el equipo comparta una versión y los cambios se
revisen como código. Una regla práctica: cuando Claude comete el mismo error dos veces, la corrección
va a `CLAUDE.md`. Mantenlo por debajo de una página: Claude lo lee entero al inicio de la sesión, así
que lo obsoleto ocupa contexto sin aportar nada.

```markdown
# Payments service

## Commands
- Build: make build
- Test: make test (unit), make itest (integration, needs docker)
- Lint: make lint (runs in CI; fix before pushing)

## Conventions
- Java 21, Spring Boot 3. No new Lombok.
- Money is always BigDecimal, never double.
- Every endpoint needs an integration test in src/itest.

## Architecture
- api/ holds REST controllers, core/ holds domain logic,
  adapters/ talks to external systems.
- Kafka events are defined in schemas/; never edit generated classes.

## Things Claude gets wrong
- Do not bump dependency versions; the platform team owns them.
- The legacy v1/ package is frozen; changes go in v2/.
```

### Las skills como conocimiento institucional

Las skills hacen operativo el conocimiento institucional: explícito, versionado, aplicado de forma
amplia y actualizado centralmente cuando cambia la política. La regla general: escribe una skill para
el conocimiento institucional que deba aplicarse de forma consistente; no escribas una para lo que
pertenece a `CLAUDE.md` o a un prompt.

Elige una pieza de conocimiento que hoy se aplique de forma inconsistente, escríbela como una carpeta
con un `SKILL.md` cuyo frontmatter diga cuándo se activa y cuyo cuerpo diga qué hacer, y colócala en
`.claude/skills/<name>/` para que viaje con el código, o distribúyela en toda la organización mediante
un plugin. Comprueba que realmente se activa pidiéndole a Claude la tarea de varias formas. Cuando
cambie la política, cambia la skill y que el responsable de la política firme el cambio; los ingenieros
recogen la nueva versión en su siguiente sesión.

```markdown
---
name: secure-api-review
description: Apply the API security standard. Use whenever creating or
  modifying an external-facing endpoint, reviewing API code, or
  generating an OpenAPI spec.
---

# Secure API review

When you create or change an API endpoint:

1. Authentication: every endpoint requires the gateway JWT;
   no anonymous routes outside /health.
2. Input validation: validate request bodies against the OpenAPI
   schema and reject unknown fields.
3. Audit: every state-changing endpoint emits an audit event with
   actor, action, entity and timestamp.
4. Data classification: fields tagged pii in the schema must never
   appear in logs or error messages.

Run the endpoint check script and include its output in your summary.
```

**Una skill es un control, pero consultivo.** Hace probable que Claude aplique la política mientras se
escribe el código, y nada obliga a una sesión a cumplirla. Una política que siempre debe cumplirse
necesita algo determinista detrás: un hook que bloquee la acción, o un pase de revisión que la vuelva a
comprobar en la PR. La skill hace raras las infracciones; el hook las hace casi imposibles.

### Los hooks como barreras en tiempo de construcción

La mayoría de las acciones de Claude durante la implementación son ediciones de archivos y comandos de
shell, así que la construcción es donde más se disparan los hooks. Los hooks de esta fase bloquean
ediciones en rutas protegidas como clases generadas o un paquete congelado, ejecutan el formateador y
el linter tras las ediciones para que no se acumule deriva, y mantienen las credenciales fuera del diff.

Respalda con un hook cualquier skill cuya política deba cumplirse sin excepción. Un hook se ejecuta en
cada acción que coincide, así que los de construcción deben ser rápidos y acotados al archivo que
cambió; las comprobaciones pesadas, como la suite completa, corresponden al commit o a la PR. Un hook
que pide aprobación humana pertenece a las puertas de despliegue: un aviso de aprobación durante la
construcción vuelve a poner a una persona en el camino crítico de todas las sesiones en paralelo.

### Sesiones paralelas y subagentes

Una sesión paralela es otra instancia completa de Claude Code trabajando una tarea distinta en su
propio worktree de git; lo único que comparten es el ingeniero que las dirige. Un subagente corre
dentro de una sola sesión como ayudante acotado, con su propia ventana de contexto y límites de
herramientas, y encaja con trabajos que se repiten entre tareas.

Divide el trabajo en tareas que toquen archivos distintos, usando el plan para ver dónde es
independiente; las tareas que comparten archivos van en una sola sesión, una tras otra. Da a cada tarea
paralela su propio worktree (`claude --worktree feature-auth` en una terminal y
`claude --worktree fix-rate-limit` en otra). Dos o tres sesiones es un buen punto de partida; el techo
práctico es cuántos flujos puede revisar bien una persona.

Convierte los trabajos repetidos en subagentes definidos en `.claude/agents/`: un simplificador de
código que quita complejidad innecesaria cuando el agente principal termina, un verificador que ejecuta
la app y comprueba el comportamiento, un investigador que explora el código y reporta sin inundar el
contexto principal. Registra las definiciones en git.

```markdown
---
name: verifier
description: Runs the app and checks the change works before the session
  reports done
tools: Bash, Read
---
Start the app with make run. Exercise the changed behavior and the two
nearest neighboring flows. Report what you ran, what you saw, and any
behavior that does not match plan.md. Do not fix anything; report only.
```

### Sistemas heredados y la fuente de verdad

Los procesos existentes ya registran estos artefactos, solo que no en markdown. Los elementos de
trabajo pueden estar en Jira, los requisitos en una herramienta con trazabilidad regulatoria, los
diseños en Figma y las aprobaciones de cambio en un comité. Esos sistemas son difíciles de desplazar
porque los auditores ya los aceptan.

Para cada artefacto que produce el proceso, nombra **un** sistema como fuente de verdad y deja que todo
lo demás guarde una copia o un enlace. Funcionan tres configuraciones: el repositorio como fuente de
verdad, con el sistema heredado referenciando archivos dentro de commits; el sistema heredado como
fuente de verdad, con Claude leyendo el registro al inicio de la sesión y escribiendo el resultado de
vuelta mediante un conector MCP; o el enlace como mínimo exigible, donde los artefactos anotan el ID del
registro y los registros contienen el SHA del commit. El enlace es un buen punto de partida, aceptando
que hay dos fuentes de verdad.

## Etapa 4 — Probar: la verificación entra en la sesión

### Dale a Claude un bucle de retroalimentación

La señal de que el código funciona llega tradicionalmente tarde: CI minutos después, un tester días
después, producción semanas después. Con un agente produciendo el código, una señal tardía significa
que una persona tiene que comprobar toda su salida, y esa persona se convierte en el cuello de botella.

Dale siempre a Claude una forma de verificar su propio trabajo: pruebas, una compilación o una
comparación de capturas.

1. Si comprobar el trabajo hoy requiere una secuencia de comandos y conocimiento del entorno, envuélvelo
   en un único objetivo que salga con código distinto de cero si falla.
2. Lista cada comando en la sección Commands de `CLAUDE.md` con un ejemplo de salida sana.
3. Fija un objetivo cuantificable para que Claude pueda comprobarse solo: «todas las pruebas de
   test_status.py pasan», «la captura coincide con la maqueta adjunta», «el endpoint devuelve 200 con el
   nuevo campo».
4. Para corregir errores, escribe primero la prueba que falla. Pide a Claude que reproduzca el error como
   prueba, la ejecute y confirme que falla por el motivo esperado. Commitea esa prueba. Solo entonces pide
   el arreglo, sin editar la prueba. Una prueba que existía antes del arreglo, y que el agente no pudo
   reescribir, es la demostración de que el error desapareció.
5. Para trabajo de UI, cierra el bucle con una comprobación visual: dale a Claude un navegador o una
   herramienta de capturas y la maqueta, y deja que implemente, capture, compare y ajuste. Dos o tres
   rondas es lo normal.
6. Haz que la verificación forme parte de «hecho», con la instrucción en `CLAUDE.md`.

```markdown
## Verifying your work
- Build: make build (must finish with "Build succeeded")
- Test: make test (all green; never skip or delete a failing test)
- Lint: make lint (zero warnings)

Run all three before reporting any task complete, and paste the output.
If a test fails, fix the code, not the test.
```

El propio bucle necesita protección: un agente que arregla código no debe poder debilitar la
comprobación sobre ese código. Un hook que bloquea ediciones a archivos de prueba durante una tarea de
corrección hace justo eso; la alternativa es revisar el diff y rechazar cualquier cambio que toque una
prueba.

No confundas el bucle de retroalimentación con un subagente verificador. El bucle corre a lo largo de
toda la tarea; el verificador empaqueta la comprobación final en una ventana de contexto nueva una vez
que la sesión cree haber terminado, de modo que el veredicto no queda teñido por las suposiciones que
produjeron el código.

### Evals continuas en CI

Las evals son el equivalente nativo de IA a las puertas de QA por etapas: una suite que se ejecuta cada
vez que cambia la configuración del agente. Cuando se cambia el modelo o se reescribe un prompt, la
suite dice si el agente sigue haciendo el trabajo con el mismo nivel. Trátala como una suite viva: a
medida que los modelos mejoran, los casos que antes discriminaban dejan de hacerlo y hay que añadir
otros nuevos surgidos de la monitorización.

Reúne de 20 a 50 tareas reales de trabajo reciente con su resultado esperado o aceptado, y escribe cada
una como un prompt más las comprobaciones que definen lo aceptable (pruebas en verde, lint limpio,
comportamiento sin cambios, política cumplida). La suite se ejecuta de forma no interactiva en CI según
un calendario y ante cualquier cambio en `CLAUDE.md`, skills o hooks, ya que esa configuración dirige al
agente y merece las pruebas de regresión que recibe el código. Condiciona los cambios de configuración a
los resultados: un cambio de skill que baja la tasa de aprobación se revisa antes de fusionarse. Cada
incidente de producción genera una eval, escrita por el equipo que fue dueño del incidente, y se queda
en la suite como prueba de regresión.

```yaml
name: Agent evals
on:
  pull_request:
    paths: ['CLAUDE.md', '.claude/**']
  schedule:
    - cron: '0 2 * * *'
jobs:
  evals:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm install -g @anthropic-ai/claude-code
      - name: Run eval suite
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          for eval in evals/*.json; do
            claude -p "$(jq -r '.prompt' $eval)" \
              --allowedTools "Read,Edit,Bash(make test)" \
              --output-format json > result.json
            ./evals/check.sh "$eval" result.json
          done
```

## Etapa 5 — Desplegar: revisión en ambos sentidos, release con puerta

### IA en el bucle de revisión de PR

La capacidad de revisión se planificó en torno a la producción humana: una PR espera a que un revisor la
lea entera, la calidad varía con su carga y el autor persigue mientras crece el backlog.

Claude tanto revisa como recibe revisiones. Todas las PR reciben el mismo conjunto de pases, con los
hallazgos ordenados por gravedad, así que la atención humana sube un nivel: si el cambio hace lo que el
plan pretendía y si el riesgo es aceptable.

El servicio gestionado de Code Review (research preview) es el arranque más rápido: un administrador lo
habilita y selecciona repositorios. Ejecuta la revisión en tu propio CI con `claude-code-action` cuando
necesites controlar el pipeline o enrutar las llamadas por tu propio acuerdo de nube —Bedrock, Vertex o
Foundry.

El tech lead escribe la política de revisión como `REVIEW.md` en la raíz del repositorio:

```markdown
# Review instructions

## Passes
Run three passes and tag each finding with its pass:
- Bugs: logic errors, broken edge cases, subtle regressions
- Security: injection risks, authentication gaps, PII in logs
- Compliance: the change matches spec.md, plan.md and our design principles

## What Important means here
Reserve Important for findings that would break behavior, leak data
or breach a policy. Style and naming are nits.

## Cap the nits
Report at most five nits per review; summarize the rest as a count.

## Do not report
Generated files under src/gen/ and anything CI already enforces.
```

Los hallazgos no aprueban ni bloquean una PR por sí solos; la protección de rama sigue exigiendo la
aprobación de un code owner. Quien quiera condicionar los merges a los hallazgos puede leer el recuento
de gravedades que el check run publica como tabla legible por máquina.

Cuando un revisor o el autor etiqueta `@claude` en un comentario, Claude lo atiende y sube el arreglo,
y el hilo registra tanto la petición como el cambio. Para las PR que abrió Claude, algunos equipos
envuelven el bucle en un comando propio que barre comentarios sin resolver y checks fallidos hasta que
la PR está en verde y solo espera la aprobación del code owner.

Los hallazgos realimentan `CLAUDE.md`: cuando una revisión marca el mismo error por segunda vez, la
corrección entra en el archivo como parte de esa revisión y, como la revisión lee `CLAUDE.md`, el error
se detecta desde la PR siguiente. Una vez al mes el tech lead afina el sistema puntuando hallazgos y
limitando el volumen de nits.

**La separación de funciones se preserva**: el agente que escribió el código no tiene forma de aprobarlo.

### Los hooks como puertas de aprobación

Un hook también puede **preguntar**, pausando la acción hasta que una persona concreta apruebe, que es
lo que necesita la puerta de release. La dirección de ingeniería, junto con gestión del cambio y
cumplimiento, enumera las puertas de aprobación humana que deben sobrevivir: firma de gestión del
cambio, autorización de release, ediciones en rutas protegidas. El ingeniero de plataforma expresa cada
una como un hook que puede permitir, preguntar o bloquear.

Los hooks de equipo van en `.claude/settings.json` en git; los innegociables van en managed settings
propiedad de plataforma o IT, donde los ingenieros no pueden desactivarlos. Un bloqueo debe explicarse:
cuando un hook detiene una acción, el motivo y la vía de aprobación aparecen en la salida de Claude.

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/production-gate.sh"
          }
        ]
      }
    ]
  }
}
```

```bash
#!/bin/bash
# Production deploys require a named release authorization
cmd=$(jq -r '.tool_input.command' < /dev/stdin)
if [[ "$cmd" == *"deploy"* && "$cmd" == *"production"* ]]; then
  if [ -z "$RELEASE_APPROVAL" ]; then
    echo "Production deploys need a release authorization." >&2
    exit 2   # exit 2 blocks the action; the message goes to Claude
  fi
fi
exit 0
```

Los hooks no son exclusivos del despliegue: corren allí donde Claude actúa. Pueden bloquear ediciones a
migraciones e infraestructura sin ticket de cambio durante la construcción, y evitar que el agente edite
archivos de prueba durante una corrección.

### Managed settings para una empresa regulada

Los despliega el equipo de plataforma vía MDM o la consola de administración, y los ingenieros no pueden
editarlos. Las reglas de denegación mantienen los secretos fuera del contexto del agente y bloquean la
salida de red a través de herramientas, mientras que una lista de permitidos preaprueba el bucle interno
seguro para que la lista de denegación no derive en fatiga de avisos. `disableBypassPermissionsMode` y
`allowManagedPermissionRulesOnly` impiden que ningún ingeniero, archivo de proyecto o flag amplíe las
reglas. El sandbox cierra el hueco que los permisos no cubren: una denegación a nivel de herramienta no
impide que un comando de shell alcance la red, pero una lista de dominios permitidos a nivel de sistema
operativo bloquea la salida por completo, y `failIfUnavailable` convierte el sandbox en una puerta y no
en una preferencia. Un bloque de credenciales deniega que un shell dentro del sandbox lea `~/.ssh` o las
credenciales de nube y elimina los secretos nombrados del entorno de todos los comandos. `allowManagedHooksOnly`,
`disableSideloadFlags`, `strictKnownMarketplaces` y `allowManagedMcpServersOnly` garantizan que toda
skill, agente, hook y servidor MCP llegó por el marketplace aprobado, y `requiredMinimumVersion` impide
arrancar con una versión que la organización no ha evaluado.

Trata cualquier configuración así como un punto de partida a medida, no como una recomendación para
copiar. Cada denegación se cambia por capacidad, y el equilibrio adecuado depende de la clasificación de
datos del repositorio.

### Integración CI/CD y despliegue

Los pipelines ejecutan tradicionalmente scripts deterministas, y todo lo que requiere juicio espera a una
persona. En su lugar, ejecuta Claude de forma no interactiva dentro del pipeline para los pasos de juicio,
en un sandbox con credenciales acotadas.

Empieza por pasos de juicio de solo lectura: triaje de una compilación fallida, resumen de una prueba
inestable, borrador del changelog.

```yaml
- name: Triage failed build
  if: failure()
  run: >
    claude -p "Read the build log at out/build.log. Identify the most
    likely cause, say whether the failure looks flaky or real, and write a
    three-line summary for the PR thread." >> triage.md
```

Después añade pasos de escritura detrás de las puertas existentes: arreglar lint, actualizar documentación
generada, atender comentarios de revisión vía `@claude`. Todo lo que el agente escribe llega como PR a
través de la protección de rama, y el agente no tiene ruta para empujar a main. Los trabajos del agente
corren en contenedores bajo una política de red con tokens acotados de corta vida y sin credenciales de
producción por defecto.

Expón el despliegue mediante MCP para que deploy, status y rollback sean herramientas acotadas por
entorno: una lista de permitidos en lugar de un script de shell con credenciales. Escalona la autonomía
por entorno: en desarrollo el agente despliega libremente; en producción prepara la release y el release
manager autoriza, con un hook aplicando la puerta. El rollback debería ser la ruta más ensayada del
pipeline, ejercitada con regularidad en staging, porque el bucle de mantenimiento la invoca.

**El principio rector: el agente puede actuar hasta la puerta de producción y no puede pasarla.**

## Etapa 6 — Mantener: cerrar el bucle

El mantenimiento es tradicionalmente reactivo. Una alerta suena a las 3 de la mañana y puede pasarse por
alto, un ticket se queda en el backlog hasta que alguien lo coge, y las acciones del post-mortem pueden no
llegar nunca al código si empieza otro incendio.

En su lugar, un disparador —una banda de control superada, un ticket, un mensaje de canal, un calendario—
invoca a Claude sin una persona en el camino. Claude diagnostica, actúa solo por rutas con puerta y escribe
lo que encuentra como `intent.md`, que recorre las etapas anteriores. La etapa corre headless, con una
puerta de confianza independiente entre etapas —una comprobación determinista o un agente revisor
adversarial— que decide si la salida de la etapa previa continúa o se escala a una persona.

**Cerrar el bucle, paso a paso:**

1. Elige una métrica con una línea base móvil estable: tasa de fallo de pruebas en CI, tasa de 5xx tras el
   despliegue o tiempo de ciclo de PR.
2. Escribe el script de detección: normalmente media y desviación estándar sobre una ventana móvil con
   reglas de Western Electric o similares, para que las bandas capturen tanto derivas lentas como picos.
   Versiónalo y cúbrelo con pruebas unitarias. **La detección es enteramente determinista, sin modelo
   implicado.**
3. Define los niveles de respuesta en configuración versionada. A 1σ el script solo registra; a 2σ invoca a
   Claude en solo lectura para diagnosticar; a 3σ Claude puede actuar, pero únicamente abriendo una PR
   hacia la puerta de revisión o disparando un runbook preaprobado.
4. El disparador puede ser un workflow programado, un webhook del stack de monitorización existente o un
   cron dentro de la red. Claude corre sin estado —un paso no interactivo en un runner de CI, o un servicio
   con el Agent SDK en un contenedor aislado—, así que un bucle puede empezar y terminar sin que nadie lo
   inicie.
5. El agente escribe su diagnóstico como `intent.md` en el formato de la Etapa 1: la anomalía y su
   evidencia, un resultado propuesto, los sistemas afectados y las preguntas abiertas.
6. El responsable del servicio o el ingeniero de guardia hace triaje: arreglar ahora, planificar o
   descartar. Los descartes afinan las bandas y reducen el ruido.
7. Cuando el arreglo se envía, añade una eval para el incidente para proteger esa clase de problema en
   adelante.

```yaml
metric: ci_test_failure_rate
baseline: rolling_30d
rules: western_electric
tiers:
  1sigma: { action: log }
  2sigma: { action: diagnose, tools: "Read,Grep,Bash(gh run view *)" }
  3sigma: { action: propose, routes: [pull_request, runbook:rollback-deploy] }
```

Qué significa en la práctica: cuando la tasa de fallo de pruebas en CI supera 3σ, el agente pone en
cuarentena la prueba inestable o abre una PR de revert, y la puerta de revisión decide. Cuando la tasa de
5xx tras el despliegue supera 3σ con un despliegue en la ventana, el agente dispara el pipeline de rollback
existente. Cuando el tiempo de ciclo de PR activa una regla de deriva, el agente escribe un informe para la
dirección de ingeniería, lo que muestra que el arnés funciona también con métricas de proceso.

### Claude de guardia con Claude Tag

Los incidentes también llegan por las apps de comunicación del trabajo. Un mensaje de Slack a las 22:00 en
un canal de incidentes puede atenderse de inmediato: Claude Tag (beta pública, hoy en Slack) hace de Claude
un miembro de esos canales bajo su propia identidad, así que cada incidente nuevo tiene un primer
respondedor y la respuesta pasa a formar parte del bucle y de la memoria para incidentes futuros.

La conversación y el conocimiento institucional se quedan en el canal. Cualquiera puede guiar la respuesta,
poner a prueba hipótesis e investigar en tiempo real, y el histórico del canal suma auditabilidad. Con
acceso por MCP, Claude verifica que la métrica ha vuelto a su línea base, lo confirma en el hilo y escribe
el post-mortem en un archivo de lecciones versionado que futuras investigaciones podrán leer.

Los incidentes no son lo único que recoge Claude Tag. Etiquetado en un ticket por MCP o consultado en el
canal, Claude hace el mismo triaje: un arreglo pequeño y bien acotado llega como PR por la puerta de
revisión, y cualquier cosa mayor se redacta como `intent.md` para la Etapa 1, momento en el que el bucle
empieza a alimentarse solo.

## Reflexiones finales

Los modelos y los arneses han avanzado lo suficiente para que las organizaciones transformen no solo cómo
producen código, sino todo el ciclo de vida del desarrollo de software, manteniendo el juicio humano en el
centro y atendiendo los requisitos de gobernanza y regulación de las grandes empresas.

El bucle sigue girando. El juicio humano permanece por encima de él.

## Fuente

[The AI-Native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook), de Louis Claxton, con
contribuciones de Jim Blackhurst, Will Steuk y Jamal Arif — publicado el 2026-08-21.
