[English](./integration-planning-workflow.en.md) · [한국어](./integration-planning-workflow.ko.md) · **Español** · [日本語](./integration-planning-workflow.ja.md)

# Flujo de planificación de integraciones

Flujo paso a paso elaborado a partir de [How to integrate APIs seamlessly](https://claude.com/blog/integrate-apis-seamlessly) (2025-10-27). Úsalo para estandarizar cómo tu equipo planifica, implementa, valida y publica integraciones de APIs de terceros con Claude.ai y Claude Code.

## 1. Triaje de la API en Claude.ai

- Abre Claude.ai. Pega la URL de la documentación, la especificación OpenAPI o los extractos relevantes.
- Pide: "Integration risks ranked by likelihood". Exige solo elementos específicos del proveedor — umbrales de rate limit, método de conteo (por usuario / IP / clave), headers requeridos, claves de idempotencia, garantías de entrega de webhooks, nullability de campos.
- Haz preguntas de seguimiento sobre cualquier modo de fallo poco claro (p. ej. "Why might OAuth tokens expire during multi-step checkout flows?", "Here's a Stripe webhook signature error. What validation steps am I missing?").
- Resultado: una lista concreta de modos de fallo y una decisión de estrategia de autenticación (dónde viven las credenciales, cadencia de refresco, plan de rotación).

## 2. Decidir webhook vs polling

- Compara opciones para el caso de uso concreto (p. ej. "webhook vs polling for real-time inventory updates").
- Elige según latencia, volumen y restricciones de infraestructura. Una estrategia híbrida (webhook para tiempo real, polling para reconciliación) es aceptable.
- Registra la decisión y las restricciones que la motivaron.

## 3. Implementar con Claude Code

- Instala: `npm install -g @anthropic-ai/claude-code`. Lanza desde la raíz del proyecto: `claude`.
- Pide a Claude Code generar un cliente tipado que coincida con las convenciones del proyecto.
- Implementa el flujo de autenticación elegido:
  - "Build OAuth2 flow for Google Calendar with automatic token refresh"
  - "Create rotating API key system for Twilio with monitoring"
  - "Implement JWT validation for microservices"
- Agrega manejo de rate limit: backoff exponencial con jitter para 429, encolado de peticiones cuando aplique, circuit breaker para llamadas con riesgo de cascada.
- Conecta validación de esquema en la frontera de respuesta; agrega una capa adaptadora para clientes versionados.

## 4. Validar

Pide a Claude Code generar y ejecutar tests:

- "Create tests that reproduce this rate limit scenario"
- "Generate contract tests for schema validation"
- "Run tests for authentication refresh during long operations"

Itera hasta que los tests confirmen que la integración maneja los modos de fallo capturados en el paso 1.

## 5. Publicar

Ejecuta dentro de Claude Code:

```
> Commit these API changes and open a PR
```

Claude Code genera un mensaje de commit descriptivo y una descripción de PR que vincula la implementación con la cobertura de tests.

## Fuente

[How to integrate APIs seamlessly](https://claude.com/blog/integrate-apis-seamlessly) (publicado el 2025-10-27).
