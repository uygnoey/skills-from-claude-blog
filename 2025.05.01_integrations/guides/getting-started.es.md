[English](./getting-started.en.md) · [한국어](./getting-started.ko.md) · **Español** · [日本語](./getting-started.ja.md)

# Primeros pasos con Integrations y Research avanzado

Una guía breve elaborada a partir de [Claude can now connect to your world](https://claude.com/blog/integrations) (2025-05-01, actualizado 2025-06-03). Cubre qué habilitar primero, cómo pensar el catálogo de apps conectadas y cómo enmarcar una solicitud de Research que use tus conexiones.

## 1. Confirmar disponibilidad por plan

Tras la actualización del 2025-06-03, Integrations y Research avanzado están disponibles en Pro, Max, Team y Enterprise. La búsqueda web es global en **todos** los planes de Claude.

En la versión del lanzamiento, Integrations y Research estaban en beta para Max, Team, Enterprise; la búsqueda web era global en planes pagos.

## 2. Elegir la primera app a conectar

Selecciona desde la línea de lanzamiento (Atlassian Jira, Atlassian Confluence, Zapier, Cloudflare, Intercom, Asana, Square, Sentry, PayPal, Linear, Plaid). Si la app no está soportada, revisa si la Integration de Zapier la cubre con un workflow pre-armado. La hoja de ruta del post menciona Stripe, GitLab y Box.

Para cada candidata, anota: qué tareas de Claude necesitan acceso a esos datos, qué acciones debe ejecutar Claude y qué modelo de autenticación permite tu organización.

## 3. Conectar desde la superficie de Integrations

Cada Integration usa un servidor MCP remoto. Una vez conectada, Claude puede leer contexto (historial del proyecto, estado de tareas, conocimiento organizacional) y ejecutar acciones en esa app.

Si construyes tu propia Integration, puedes apoyarte en el hosting de Cloudflare, que provee OAuth, manejo de transporte y despliegue integrados — el post indica que se puede construir una Integration nueva en tan solo 30 minutos.

## 4. Ejecutar una solicitud de Research avanzado

- Activa el botón **Research**.
- Redacta la solicitud como un brief: pregunta, alcance y qué apps conectadas incluir.
- Espera 5 a 15 minutos para la mayoría de reportes; hasta 45 minutos para investigaciones complejas.
- Verifica las citas vinculadas en el reporte antes de actuar sobre los hallazgos.

## 5. Workflows iniciales sugeridos

- Vía Zapier: traer datos de ventas de HubSpot; preparar un brief de reunión desde el calendario.
- Atlassian: resumir un espacio de Confluence; crear masivamente issues de Jira a partir de un documento de kickoff.
- Intercom + Linear: detectar un patrón recurrente en feedback de usuarios y luego crear un bug en Linear desde la misma conversación, con Fin actuando como cliente MCP.

## Fuente

[Claude can now connect to your world](https://claude.com/blog/integrations) (publicado el 2025-05-01, actualizado el 2025-06-03).
