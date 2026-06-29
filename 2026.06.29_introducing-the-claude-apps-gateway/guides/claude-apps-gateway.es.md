[English](./claude-apps-gateway.en.md) · [한국어](./claude-apps-gateway.ko.md) · **Español** · [日本語](./claude-apps-gateway.ja.md)

# Claude apps gateway: resumen de despliegue y adopción

## ¿De qué trata esta guía?
Esta guía resume el modelo de despliegue y adopción descrito en el post, destacando qué hace el gateway (SSO, políticas, telemetría y enrutamiento) y cómo se configura el cliente para usarlo.

## ¿Cuándo es útil?
Úsala como referencia rápida al planificar un despliegue de Claude Code en toda la organización sobre Amazon Bedrock o Google Cloud, con inicio de sesión centralizado, aplicación de políticas y atribución de uso por usuario.

## Arquitectura (según el post)
- **Gateway**: un único contenedor sin estado en Linux, con una base de datos **PostgreSQL**.
- **Identidad**: el gateway actúa como **relying party OIDC** frente a tu IdP (p. ej., Google Workspace, Microsoft Entra ID, Okta) y emite sesiones de corta duración.
- **Política**: las “managed settings” (políticas) se definen una sola vez en el servidor; el cliente las recibe al iniciar sesión; el gateway las hace cumplir en cada petición.
- **Telemetría**: el cliente marca una métrica de uso por cada petición; el gateway la reenvía mediante **OTLP** a un colector que configuras.
- **Enrutamiento**: el gateway conserva la credencial upstream y enruta la inferencia al **Claude API**, **Amazon Bedrock** o **Google Cloud**, con conmutación por error opcional entre proveedores.

## Pasos de adopción (según el post)
1. **Desplegar el gateway**
   - Descargar el binario del CLI de Claude Code.
   - Configurar `gateway.yaml` con tu emisor OIDC y la credencial upstream.
   - Registrar una aplicación OIDC en tu IdP.
2. **Forzar el inicio de sesión vía gateway en los clientes**
   - Distribuir `managed-settings.json` a las máquinas de los desarrolladores.
   - Establecer `forceLoginMethod` y `forceLoginGatewayUrl` para que el cliente se conecte al gateway en el primer arranque.
3. **Operar y ajustar de forma centralizada**
   - Administrar de forma centralizada los modelos permitidos y los valores por defecto.
   - Usar la telemetría reenviada a tu colector para la atribución por usuario.
   - Aplicar límites de gasto diarios/semanales/mensuales por organización/grupo/usuario.

## Fuente
- https://claude.com/blog/introducing-the-claude-apps-gateway
