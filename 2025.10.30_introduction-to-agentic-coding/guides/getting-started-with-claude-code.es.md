[English](./getting-started-with-claude-code.en.md) · [한국어](./getting-started-with-claude-code.ko.md) · **Español** · [日本語](./getting-started-with-claude-code.ja.md)

# Primeros pasos con Claude Code

Una guía corta de adopción derivada de [Introduction to agentic coding](https://claude.com/blog/introduction-to-agentic-coding) (2025-10-30). Úsala como checklist del primer día al introducir Claude Code en un proyecto.

## 1. Verifica que el flujo encaja

Antes de instalar, valida que la próxima tarea a delegar es adecuada:

- Atraviesa varios archivos, o
- Requiere ejecutar comandos e interpretar resultados, o
- Es de alto volumen pero bien comprendida (cobertura de tests, documentación, refactor rutinario).

Si la tarea es conceptual o aún estás definiendo el problema, sigue con Claude.ai.

## 2. Instala Claude Code

```
npm install -g @anthropic-ai/claude-code
```

## 3. Lánzalo en tu proyecto

Ubícate en la raíz del proyecto y luego:

```
claude
```

Claude Code lee archivos de configuración, tests e imports para construir un mapa interno antes de hacer cualquier cosa.

## 4. Prueba los tres prompts iniciales

En orden:

```
Explain the structure of this codebase and how the main components interact
```

```
Review the authentication module for potential security issues
```

```
Find all N+1 query problems in our GraphQL resolvers and implement DataLoader batching
```

El primero te da intuición sobre cómo Claude Code lee tu proyecto. El segundo ejercita el análisis. El tercero ejercita una implementación multi-archivo completa.

## 5. Aprueba, revisa o rechaza

Claude Code pide aprobación antes de modificar archivos y muestra el diff propuesto. Aprueba solo lo que entiendes; rechaza o pide cambios cuando algo no encaja.

## 6. Conserva el conocimiento del proyecto en CLAUDE.md

Crea un `CLAUDE.md` en la raíz del proyecto con estándares de código, decisiones arquitectónicas y requisitos específicos. Claude Code lo lee en cada sesión.

## 7. Expándete a los quick wins

Tras la primera sesión, planifica tres usos deliberados en las categorías que destaca el post:

- Automatización de tests para rutas no cubiertas.
- Generación de documentación para sistemas legacy.
- Refactorización rutinaria de deuda técnica.
- Implementación de features bien comprendidas.

Esa experiencia te ayudará a decidir dónde Claude Code se gana la confianza del equipo.

## 8. Opcional: conecta servidores MCP

Si tu workflow depende de herramientas fuera del repositorio (gestores de issues, sistemas de diseño, documentación interna), conecta servidores MCP para que Claude Code incorpore ese contexto a su planificación.

## Fuente

[Introduction to agentic coding](https://claude.com/blog/introduction-to-agentic-coding) (publicado el 2025-10-30).
