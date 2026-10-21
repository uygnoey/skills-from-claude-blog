[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Anthropic presenta los mods: pequeñas funciones de TypeScript que cambian cómo funciona y se ve Claude
Code. Un mod puede reescribir un prompt, añadir UI nueva, reemplazar una función integrada o agregar
funcionalidad nueva. Los mods se distribuyen dentro de plugins y funcionan en la CLI de Claude Code y en
la app de escritorio.

## ¿Cuándo es útil?
- Cuando quieres que Claude Code funcione a tu manera sin esperar una nueva función.
- Cuando un hook no basta: necesitas reescribir un evento, dibujar UI o reemplazar una función.
- Cuando un equipo quiere sus propios controles, como estado de CI, salvaguardas de producción o
  registros de auditoría.
- Cuando los administradores deben controlar qué mods pueden instalar los usuarios.

## Puntos clave
- Claude Code emite un evento cada vez que hace algo (llamar a una herramienta, pedir permiso, dibujar
  parte de la pantalla). Un mod se engancha a un evento y se ejecuta antes, después, en lugar de él o
  envolviéndolo.
- Con una sola función se puede reescribir un prompt, bloquear/reescribir/reintentar una llamada a
  herramienta, aprobar o denegar un permiso, o ocultar secretos de la salida de herramientas. También
  se puede editar o reemplazar la UI y añadir botones y campos, en la terminal, la app de escritorio o
  ambas.
- Los mods del mismo evento se ejecutan en orden de carga: el primero en cargarse ve el evento primero
  y el resultado al final, de modo que se pueden apilar mods de distintos autores.
- Las funciones integradas se están pasando a mods: `/diff` ya es un mod que puedes desactivar en
  `/plugin` o reemplazar.
- Los mods no están aislados en un sandbox; instálalos solo de fuentes de confianza. Se aplican los
  controles de plugins existentes y, en Team/Enterprise o en equipos con managed settings, el mod
  integrado `sec-default` se carga primero para impedir acciones riesgosas como anular reglas de
  denegación de permisos.
- Claude Code puede escribir, instalar y recargar en caliente un mod por ti.

## Recursos incluidos
- Skill: `plan-code-mods` — cómo acotar un mod (evento, fase, superficie, orden de carga), elegir entre
  mod y hook, y gobernar mods en equipo, con una hoja de diseño de mods.

## Fuente
- https://claude.com/resources/articles/claude-code-mods
