[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Anthropic describe el proceso de seis pasos que emplea para ejecutar migraciones de código a gran escala con Claude Code, convirtiendo lo que antes eran proyectos de varios años en trabajo medido en semanas. El principio organizador se enuncia desde el inicio: no arreglas el código, arreglas el proceso (el bucle) que lo produjo.

Los seis pasos son (1) escribir el manual de reglas, el mapa de dependencias y el inventario de brechas, (2) someter las reglas a una mini-migración desechable, (3) traducir todo con agentes en paralelo y después (4) compilar, (5) ejecutar y (6) igualar el comportamiento frente al original. Dos migraciones sostienen la guía: el port de Bun de Zig a Rust por Jarred Sumner —cerca de un millón de líneas en menos de dos semanas, con el 100 % de la suite de pruebas existente en verde antes del merge— y el port de Python a TypeScript de 165.000 líneas que Mike Krieger completó en un fin de semana.

## ¿Cuándo es útil?
- Cuando un port o una reescritura es demasiado grande para revisarse archivo por archivo y el trabajo manual nunca alcanzaría al original.
- Cuando una migración produce código plausible que se aparta en silencio del comportamiento original.
- Cuando hay que decidir cómo repartir la traducción entre agentes paralelos y en qué orden.
- Cuando una reescritura se estanca porque no existe una definición acordada de "hecho" o "correcto".
- Cuando se está estimando lo que una migración de esta forma costaría realmente en tokens y tiempo.

## Puntos clave
- **Construye el árbitro primero.** Clasifica las pruebas existentes en portables y atadas a los internos, reescribe las primeras como aserciones que corran contra ambas bases de código y valida el árbitro en las dos direcciones: debe pasar con el original y fallar con código roto a propósito. Sin suite de pruebas, construye en su lugar un arnés de paridad con escenarios reales de extremo a extremo.
- **El manual de reglas va antes que el inventario de brechas.** El inventario se define por lo que los valores por defecto del manual no cubren, así que no puede escribirse primero. Y la forma del manual depende de una decisión anterior: un port que preserva la estructura da tablas de correspondencia; un rediseño da un documento de diseño.
- **El producto de la prueba de esfuerzo es un manual mejor, no avance.** Ejecuta una mini-migración con un traductor, un revisor y un extractor de reglas, y después descarta los archivos traducidos, para que las decisiones incrustadas en ellos no generen presión por conservarlos.
- **"Hecho" tiene que ser mecánico.** La prueba de finalización de la cola es que el archivo de salida existe en disco. Cualquier criterio que requiera juicio impide reanudar, y toda migración larga se interrumpe.
- **Señala, nunca adivines.** Un implementador inseguro emite `// TODO(port): <motivo>` y sigue, convirtiendo un riesgo de corrección invisible en un ítem visible de la cola. El texto del motivo es lo que permite que una pasada posterior agrupe cincuenta marcas en una sola decisión.
- **Revisión adversarial.** Dos revisores por unidad de trabajo en contextos separados, con el desacuerdo escalando a un tercer agente. Un solo revisor converge hacia el encuadre del implementador y aprueba un error sistémico mil veces seguidas.
- **Cuando un revisor detecta el mismo fallo una y otra vez, añade una frase al manual y regenera la tanda**: un parche archivo por archivo deja el generador produciendo el error.
- **No uses el modelo más grande para todo.** El gasto de tokens se concentra en los bucles: implementadores en modelos más pequeños (doce subagentes Sonnet en paralelo en el port a TypeScript), revisores y delegadores en los más grandes. La migración de Bun consumió 5.900 millones de tokens de entrada y 690 millones de salida, unos 165.000 dólares a precio de API, para un binario un 19 % más pequeño y un rendimiento real entre un 2 % y un 5 % mejor.
- **El éxito incluye regresiones.** Bun se integró limpio y produjo 19 después, todas corregidas. La pregunta es si las regresiones son localizables y baratas, no si están ausentes.

## Recursos incluidos
- `skills/large-scale-code-migration/SKILL.md` — el proceso de seis pasos como procedimiento ejecutable.
- `skills/large-scale-code-migration/references/six-step-process.md` — cada paso en detalle, incluido cuándo el paso 4 se pliega sobre el 3.
- `skills/large-scale-code-migration/references/verification-harness.md` — construir y validar el árbitro, con lista de comprobación.
- `skills/large-scale-code-migration/references/loop-design.md` — diseño de colas, marcas TODO(port), revisión adversarial, elección de modelo, scripts orquestadores.
- `skills/large-scale-code-migration/templates/rulebook.md`, `templates/dependency-map.md`, `templates/gap-inventory.md` — los tres documentos de la fase uno como plantillas rellenables.
- `skills/large-scale-code-migration/examples/case-studies.md` — las cifras de Bun y del port a TypeScript, con qué extraer de cada una.
- `agents/migration-translator.md`, `migration-reviewer.md`, `rule-extractor.md`, `review-tiebreaker.md`, `migration-fixer.md` — los cinco papeles de agente que nombra el post.
- `guides/migration-playbook.{en,ko,es,ja}.md` — el método como manual narrativo.

## Fuente
[How Anthropic Runs Large-Scale Code Migrations with Claude Code](https://claude.com/blog/ai-code-migration) — publicado el 2026-07-16.
