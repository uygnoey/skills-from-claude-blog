[English](./building-long-running-agents.en.md) · [한국어](./building-long-running-agents.ko.md) · **Español** · [日本語](./building-long-running-agents.ja.md)

# Construir agentes de larga duración

Cómo Outtake construyó el Recon Agent —un investigador cibernético autónomo— y qué resistió cuando las sesiones empezaron a durar horas.

## 1. El problema

Outtake fue fundada en 2023 por Alex Dhillon, antes en el equipo de proyectos moonshot de Palantir. La empresa unifica toda la cadena de ataque a la confianza digital en una única defensa, y escaneó más de 20 millones de posibles ciberataques en 2025.

Dhillon plantea la situación desde el lado del atacante:

> "Si te pones el sombrero del actor malicioso, en realidad es un gran momento para lanzar ataques. El ataque medio no solo se ejecuta más rápido gracias a la IA, sino que además consigue un acceso más profundo gracias a la IA."

Los ataques transcurren en tres etapas: recolectar datos públicos, construir suplantaciones como señuelo y explotar sistemas internos. Las herramientas tradicionales abordan cada etapa por separado, y ahí está la brecha: las tres etapas pertenecen a una única red adversaria.

## 2. Qué hace el Recon Agent

A partir de una **única página de acceso clonada**, reúne y clasifica evidencia, sigue las pistas hasta infraestructura conectada —por ejemplo una cuenta falsa de Telegram que se presenta como "Atención al cliente"—, cartografía la red adversaria en un grafo y produce un informe de investigación con perfiles de actores y una cronología del ataque.

Lee, escribe y ejecuta código, e interactúa directamente con páginas de acceso maliciosas para rastrear adónde van las credenciales robadas.

| Medida | Valor |
| --- | --- |
| Mediana de duración de sesión | 16 minutos |
| Habitual | hasta una hora y más |
| Más larga observada | 2 horas |

## 3. Cuatro etapas de desarrollo

### Etapa 1 — Conviértete primero en experto

El equipo realizó investigaciones cibernéticas reales por su cuenta y extrajo experiencia de dominio de clientes y socios de diseño, para definir qué significa "bueno".

> "Lo más importante al construir agentes de larga duración es que realmente tienes que entender *¿cómo es lo bueno? ¿Qué se supone que debe hacer el agente?*" — Jack Hayford, responsable de ingeniería

### Etapa 2 — Prototipa en Claude Code

Los marcos de agentes tradicionales no bastaban:

> "Cada investigación es distinta y profundamente técnica. El agente necesitaba músculo y capacidad de programación, y Claude Code fue un arnés inicial sólido."

El principio de diseño que se fijó aquí: **restringe la orquestación con rigor** —realiza siempre X, Y, Z— **pero permite la improvisación en los escenarios que exigen criterio.**

### Etapa 3 — Gradúate a un arnés de nivel de producción

> "Nos gustaban mucho los patrones que había introducido Claude Code, pero necesitábamos acceso adicional a las primitivas de más bajo nivel."

El equipo migró al **Claude Agent SDK** para producción, ganando un control más estrecho sobre la memoria, el contexto y el sistema de archivos sin reconstruir el bucle del agente.

### Etapa 4 — Construye bucles de iteración estrechos guiados por evaluaciones

Las suites de evaluación automatizadas permitieron al equipo hacer cambios de gran alcance con seguridad. Un agente de programación aparte lee las sugerencias de la investigación, escribe nuevas herramientas y construye escenarios de prueba; las personas solo evalúan los resultados finales.

> "Cuando construyes estos agentes largos y complejos, es muy importante que el bucle de retroalimentación esté automatizado."

## 4. Cuatro aprendizajes sobre agentes de larga duración

### Herramientas: un sistema de archivos y bash son suficientes

Un sistema de archivos da una memoria que sobrevive a la compactación del contexto. El sistema de archivos más bash permite al agente responder de forma creativa ante los obstáculos.

> "Entregar a un agente esas herramientas y capacidades tan potentes y abiertas es un cambio de escalón enorme. Hemos visto muchos casos en los que una herramienta fallaba por un problema de red o lo que fuera, y el agente simplemente encontraba el rodeo adecuado y continuaba."

### Los prompts son sugerencias

Los prompts de sistema dan flexibilidad, pero carecen de permanencia en agentes de larga duración.

> "Cuando construyes estos agentes de larga duración que se complican con el tiempo, los prompts son sugerencias. Probablemente cada palabra de ese prompt acabará siendo ignorada."

La respuesta es arquitectónica: sacar los requisitos de comportamiento del prompt y llevarlos a **barreras codificadas en la capa de orquestación**, lo que además preserva espacio de contexto para las tareas de alto criterio.

### Las evaluaciones son para la velocidad, no solo para la fiabilidad

Revisar a mano transcripciones de 30 minutos no escala. Las evaluaciones automatizan la reflexión en comprobaciones estructuradas y puntuadas, y aceleran enormemente los ciclos de desarrollo.

> "Construir alguna versión de evaluaciones desde el principio hará que construyas ese agente más rápido, por poco oficiales o 'perfectas' que sean."

### Proteger a tus agentes

La inyección de prompts es una amenaza real. Outtake eligió Claude en parte por su solidez frente a ataques de inyección de prompts, pero la defensa es arquitectónica.

> "La seguridad es un punto importante para nosotros al construir el Recon Agent. Le dimos un sistema de archivos y bash y lo estamos enviando a entornos adversarios."

La estrategia: suponer que el agente podría ser secuestrado y diseñar el sistema circundante para contener el daño. Outtake puntúa la confianza justo en el punto en que el agente sale a internet, implementando un control que evalúa aquello que el agente está a punto de tocar: "¿Es esta página una suplantación? ¿Es malware? ¿Está intentando inyectarle un prompt al agente ahora mismo?"

## 5. Resumen de buenas prácticas

**¿Sabes cómo es lo "bueno"?**
Haz la tarea tú primero. Extrae experiencia de dominio de clientes y socios de diseño. Establece un estándar fijo para cada iteración.

**¿Está justificada cada pieza de complejidad?**
Encuentra la versión más simple que funcione. Automatiza de forma incremental. Añade complejidad solo cuando los resultados lo justifiquen.

**¿Está tu arnés a la altura de la carga de trabajo?**
Valida las hipótesis en Claude Code. Gradúate al Agent SDK cuando necesites control de más bajo nivel. No reconstruyas tú mismo el bucle del agente.

**¿Dónde hay que restringir al agente?**
Codifica las barreras en la capa de orquestación. Evita restricciones en las decisiones de criterio de bajo nivel. El espacio de improvisación produce los mejores resultados.

## Fuente

[How Outtake built a cyber investigator on Claude](https://claude.com/blog/how-outtake-built-a-cyber-investigator-on-claude) — Michael Segner, 22 de julio de 2026
