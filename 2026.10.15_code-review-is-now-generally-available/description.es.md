[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
El anuncio de que Code Review deja la fase de research preview y pasa a estar disponible de forma
general para las organizaciones de Claude Team y Enterprise, con tres cambios desde la preview:
revisiones más rápidas, hallazgos más precisos y una profundidad de revisión que los administradores
eligen por repositorio.

## ¿Cuándo es útil?
- Cuando una organización con plan Team o Enterprise está decidiendo si activar Code Review y en qué
  repositorios.
- Cuando las revisiones de la preview resultaban demasiado lentas o ruidosas para cambios rutinarios
  y quieres ajustar la profundidad por repositorio en lugar de aceptar un único ajuste para todo.
- Cuando el desarrollo asistido por agentes ha aumentado el volumen de pull requests más rápido que
  la capacidad de revisión humana.

## Puntos clave
- Code Review sale de research preview y está disponible de forma general en los planes Claude Team y
  Enterprise.
- Las organizaciones de Claude Enterprise elegibles pueden reclamar al menos 10.000 USD en créditos
  de Code Review hasta el 15 de enero de 2027; los créditos caducan 30 días después de reclamarse y
  se aplican los términos correspondientes.
- Velocidad: la mayoría de las revisiones termina ahora unas 3 veces más rápido que durante la
  preview: de unos 20 minutos a 6–10 minutos.
- Calidad: encuentra más de los errores que importan y los presenta como hallazgos claros y concisos
  que indican el problema, qué lo desencadena y la solución en unas pocas frases.
- Flexibilidad: los administradores eligen Quick, Standard (el valor por defecto) o Deep para cada
  repositorio, de modo que las bases de código rutinarias reciben una pasada rápida y las más
  críticas una revisión profunda. Todos los niveles entregan revisiones de alta calidad.
- Anthropic ejecuta Code Review en sus propios pull requests, y así ve dónde las revisiones frenan a
  sus propios ingenieros.
- Configuración para administradores: activar Code Review en los ajustes de Claude Code, instalar la
  GitHub App y seleccionar los repositorios a revisar. Los desarrolladores no configuran nada: las
  revisiones se ejecutan automáticamente en los PR nuevos.

## Recursos incluidos
- Skill: `code-review-rollout` — activar Code Review en una organización y asignar una profundidad de
  revisión por repositorio, con una referencia sobre los tres niveles y el programa de créditos.

## Fuente
- https://claude.com/resources/articles/code-review-is-now-generally-available
