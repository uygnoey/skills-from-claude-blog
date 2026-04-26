[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Introducción al agentic coding

## ¿De qué trata este post?

Un manual introductorio al agentic coding: el paso de herramientas de IA que predicen la siguiente línea a sistemas que toman un objetivo de alto nivel, planifican trabajo en varios pasos, modifican archivos a lo largo del repositorio, ejecutan tests e iteran hasta terminar. El post recorre la evolución desde autocompletado a asistentes de chat y a sistemas agentic, explica cómo Claude Code lee el contexto del proyecto, coordina cambios multi-archivo y respeta un modelo explícito de permisos, y usa la implementación autónoma de Rakuten en vLLM durante siete horas como caso real de cabecera.

## ¿Cuándo es útil?

- Onboardear al equipo en "qué diferencia al agentic coding del autocompletado y los asistentes de chat".
- Decidir qué workflows (automatización de tests, generación de documentación, refactorización rutinaria, features bien definidas) delegar primero a Claude Code.
- Citar las métricas concretas del caso Rakuten (79% más rápido, 99.9% de precisión, capacidad 5x en paralelo).
- Tener a mano el comando de instalación y los tres prompts iniciales que recomienda el post.

## Puntos clave

- Agentic coding = autonomía + alcance. Las herramientas leen el repositorio completo, rastrean dependencias, ejecutan comandos e iteran. El autocompletado tiene una ventana de contexto limitada; el chat es iterativo pero manual; los agentes orquestan por sí solos.
- Dos fases: recolección de contexto y planificación (configs, tests, imports, mapa de dependencias → plan adaptable) y luego implementación y coordinación (ediciones multi-archivo, validación contra tests).
- Instalación de Claude Code: `npm install -g @anthropic-ai/claude-code`; ejecuta `claude` en el directorio del proyecto.
- Modelo de permisos: Claude Code pide aprobación antes de modificar archivos y muestra el diff propuesto. Puedes aprobar, revisar o rechazar.
- Se integra con tus herramientas existentes (npm, Jest, pytest, Git, dev servers) y puede conectar servidores MCP para herramientas adicionales.
- Caso Rakuten: implementación de un método de extracción de vectores de activación en vLLM (12.5M de líneas, Python/C++/CUDA) en siete horas de trabajo autónomo. 99.9% de precisión numérica, entrega de features 79% más rápida (24 días → 5), capacidad 5x en paralelo. Cita de Kenta Naruse: "I didn't write any code during those seven hours, I just provided occasional guidance." Cita de Yusuke Kaji: "You can have five tasks running in parallel by delegating four to Claude Code while focusing on the remaining one."
- Prompts iniciales sugeridos: "Explain the structure of this codebase and how the main components interact"; "Review the authentication module for potential security issues"; "Find all N+1 query problems in our GraphQL resolvers and implement DataLoader batching".
- "Start slow, then expand": comienzos rápidos en automatización de tests, generación de documentación, refactorización rutinaria e implementación de features bien comprendidas.
- Claude Code usa archivos CLAUDE.md para conservar estándares de código, decisiones arquitectónicas y requisitos específicos del proyecto entre sesiones.

## Recursos incluidos

- [skills/agentic-coding-foundations/SKILL.md](./skills/agentic-coding-foundations/SKILL.md): cuándo recurrir a Claude Code, el flujo de dos fases, comandos de instalación/ejecución y prompts de onboarding.
- [references/evolution-of-ai-coding.md](./skills/agentic-coding-foundations/references/evolution-of-ai-coding.md): comparación autocompletado → chat → agentic.
- [examples/first-prompts.md](./skills/agentic-coding-foundations/examples/first-prompts.md): los tres prompts iniciales recomendados y el resumen del caso Rakuten.
- [guides/getting-started-with-claude-code.es.md](./guides/getting-started-with-claude-code.es.md) (+ en/ko/ja): guía paso a paso de adopción.

## Fuente

Basado en [Introduction to agentic coding](https://claude.com/blog/introduction-to-agentic-coding) (publicado el 2025-10-30).
