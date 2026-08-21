[English](./verification-loops.en.md) · [한국어](./verification-loops.ko.md) · **Español** · [日本語](./verification-loops.ja.md)

# Construir bucles de verificación en Claude Code con skills

## El bucle agéntico

La mayoría de las sesiones de codificación agéntica siguen un bucle: pides un cambio, Claude
**reúne contexto**, **actúa**, **verifica los resultados** y, si hace falta, vuelve a reunir más
contexto.

La verificación es cómo un agente comprueba su propio trabajo antes de responder. Claude ya hace
parte de esto por su cuenta, observando las señales deterministas de tu base de código:
comprobadores de tipos, linters, pruebas, errores en tiempo de ejecución. Todo lo que Claude no
puede inferir se convierte en los pasos que *tú* das para comprobar una funcionalidad a mano.

Esos pasos manuales pueden transformarse en bucles de verificación. En Claude Code, un bucle de
verificación es un proceso iterativo en el que Claude comprueba el trabajo e intenta corregirlo:
un ciclo repetido en el que el agente ejecuta pruebas, linters o comprobaciones personalizadas y
arregla lo que falla antes de seguir. Empaquetados como skills, cada sesión aplica automáticamente
las mismas comprobaciones en lugar de depender de que una persona las recuerde.

## Empieza por los bucles integrados

- **`/verify`** — compila, ejecuta y observa los cambios en tu aplicación.
- **Cadena de herramientas** — Claude intenta detectar los códigos de error y las advertencias de
  cualquier herramienta que le proporciones, como un linter, y actuar en consecuencia. Enumera tus
  comandos exactos de build y test en `CLAUDE.md` para que Claude no tenga que inferirlos.
- **Code Review (vista previa de investigación)** — un servicio multiagente gestionado que ejecuta
  una pasada de revisión automática sobre los PR de los repositorios que habilites. Puedes
  corregir el hallazgo y hacer push, o cerrar el bucle comentando `@claude` sobre el hallazgo
  (requiere tener GitHub Actions ya configurado).
- **GitHub Actions** — define un job que invoque a Claude con una skill de verificación, y las
  mismas comprobaciones que ejecutas en local se dispararán en cada push o PR.
- **Validación de especificaciones** — una skill que verifica cada cambio contra una
  especificación en markdown del repositorio y trata de corregir las violaciones.
- **Rúbricas en Claude Managed Agents (beta)** — verifica los resultados contra una rúbrica usando
  un agente evaluador independiente. Los fallos vuelven automáticamente al bucle para retrabajo.

## Escribir los tuyos

En un proyecto existente, la señal es la repetición: haces las mismas pequeñas correcciones cada
vez que Claude implementa una funcionalidad. Anota todo lo que te encuentras haciendo cada vez.

Si empiezas un proyecto nuevo, escribe la versión de buenas prácticas en lenguaje llano, **como se
la entregarías a alguien que se incorpora al equipo en su primer día**.

Si te cuesta articular la comprobación, pide primero a Claude las buenas prácticas y edita desde
ahí. Tu versión probablemente difiera en unos pocos puntos concretos, y esas diferencias son
justamente lo que quieres capturar.

> **Consejo.** La comprobación no tiene que ser cualitativa para pertenecer aquí. "Rechaza
> cualquier migración que elimine una columna sin un paso de backfill" es una regla determinista
> que ningún linter genérico detectará, pero sí uno específico del proyecto. Cualquier cosa que
> tengas que seguir imponiendo a mano merece capturarse como bucle.

### Conviértelo en una skill

La vía más rápida es instalar el plugin `skill-creator` y dejar que Claude te entreviste:

```
/skill-creator Create a skill for verifying frontend changes end-to-end. Interview me about my workflow.
```

También puedes escribirla a mano dejando un archivo markdown en `.claude/skills/` dentro de tu
proyecto. La skill de verificación más simple posible son unas pocas líneas de frontmatter más un
cuerpo:

```markdown
# .claude/skills/verify-log-hygiene/SKILL.md
---
name: verify-log-hygiene
description: Check that error logs include the request ID and never
  include the request body. Use when the diff touches error handling
  or logging.
allowed-tools: [Read, Edit, Grep]
---
Read the error-handling paths in the current diff.

For each log call on an error path, confirm it includes the request ID
and does not pass the request body, headers, or any user-supplied payload.

Report each violation with file:line, then fix it: add the request ID
where it's missing and strip the payload from the log call.
```

## Ajusta la comprobación a dónde se ejecuta

### Independiente (standalone)

La invocas deliberadamente, una vez que el artefacto existe. Una skill independiente se gana su
sitio en comprobaciones transversales que no aplican siempre: un escaneo de seguridad antes del
commit, una auditoría de accesibilidad antes del PR, la verificación de cabeceras de licencia en
todo el repositorio. Cualquier cosa que quieras tener disponible en muchos flujos de trabajo pero
que no quieras que se dispare en cada cambio de código.

El coste es que cada invocación sigue siendo un turno que tienes que acordarte de dar. La señal de
que se te ha quedado pequeña es que la ejecutas después de cada cambio: en ese punto, el
procedimiento se ha ganado un sitio permanente.

### Incrustada (embedded)

Se dispara automáticamente como parte de la skill que produce el artefacto. La comprobación
pertenece a un flujo de trabajo concreto, y ahora ese flujo la ejecuta sin que se lo pidas. La
versión más simple es añadir una línea al cuerpo de la skill productora:

```
After creating the component file, run eslint on it and
address any errors before reporting completion.
```

Verifica que la incrustación funciona invocando la skill en una tarea nueva y confirmando que el
paso añadido se ejecuta como parte de la salida. Si no ocurre, la `description` de la skill o las
instrucciones anteriores no están arrastrando la comprobación añadida.

Lo incrustado solo funciona en skills que puedes editar: las que escribiste tú, o las instaladas a
nivel de proyecto donde el archivo `SKILL.md` está bajo tu control. Las skills integradas y las
gestionadas por plugins (las que se sobrescriben al actualizar) quedan fuera de este patrón:
encadena en su lugar. Evita lo incrustado para comprobaciones que abarcan varios flujos de
trabajo; esas piden ser independientes.

### Encadenada (chained)

Una skill llama a otra al terminar, y varios relevos verificados se ejecutan de extremo a extremo.
Los miembros del equipo de Claude Code de Anthropic usan este patrón a diario: `/code-review` caza
errores, `/simplify` limpia el diff, una skill `/verify` confirma el comportamiento de extremo a
extremo, y una skill `/design` personalizada comprueba las pautas de un archivo `DESIGN.md` si el
cambio tocó la interfaz.

Encadenar es también cómo añades verificación a una skill que no puedes modificar: crea una skill
envoltorio que invoque la original y luego tu skill de verificación.

```markdown
# .claude/skills/safe-refactor/SKILL.md
Run /simplify on the current diff first.
When /simplify finishes, invoke /verify-no-public-api-changes.
```

Lo que empezó como un hábito ("siempre ejecuto `/verify` después de `/simplify`") se convierte en
un contrato ("`/simplify` siempre ejecuta `/verify` al terminar"). La cadena recorre todo el ciclo
de desarrollo por su cuenta; tú solo intervienes cuando algo se escala de vuelta a ti.

Sáltate el encadenamiento cuando los pasos sean lo bastante independientes como para que a veces
quieras ejecutar solo uno: encadenar cambia flexibilidad por automatización. Los bucles encadenados
pueden aumentar el gasto de tokens, así que pruébalos antes de desplegarlos ampliamente.

### En cada PR

Cuando la cadena sea sólida para tus propios cambios, el mismo procedimiento puede ejecutarse en
cada PR. El cambio de un compañero pasa por las mismas puertas que el tuyo, se acordara o no de
invocar la cadena. La infraestructura es lo mismo que la cadena que ya escribiste, un paso más
allá: las mismas skills, las mismas rúbricas, los mismos estándares, aplicados sin depender de la
diligencia del autor.

Aquí es donde la verificación deja de ser infraestructura personal y pasa a ser infraestructura de
equipo. Espera antes de poner puertas para todos los PR mientras la cadena siga cambiando: cada
ajuste se convierte en un evento visible para todo el equipo.

## El proceso

1. Elige el seguimiento manual que más veces hiciste esta semana.
2. Prueba primero la skill integrada `/verify` y comprueba si ayuda a tu proceso.
3. Escribe el procedimiento en lenguaje llano, como se lo entregarías a alguien en su primer día.
4. Pásalo a `skill-creator`, o deja tú mismo el archivo markdown en `.claude/skills/`.
5. Invócalo en una tarea nueva y confirma que la comprobación se ejecuta como parte de la salida;
   itera si hace falta.
6. Experimenta con el encadenamiento de skills para crear un flujo de verificación de extremo a
   extremo.

Cuanto más puedas codificar para que Claude lo siga, más a menudo su respuesta se acercará a lo que
quieres al primer intento. Las correcciones que ya no tienes que ajustar liberan tu atención para
el trabajo que ninguna skill puede escribir por ti.

## Fuente

[Building verification loops in Claude Code with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills)
— Delba de Oliveira, equipo de Claude Code, 22 de julio de 2026.
