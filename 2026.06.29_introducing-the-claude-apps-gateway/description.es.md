[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Este post presenta el Claude apps gateway, un gateway autoalojado que permite a las organizaciones ejecutar Claude Code con Amazon Bedrock y Google Cloud, centralizando autenticación, políticas y controles de coste.

## ¿Cuándo es útil?
Es útil cuando quieres desplegar Claude Code a escala sin aprovisionar credenciales de nube por desarrollador, a la vez que aplicas políticas coherentes (modelos y valores por defecto) y habilitas atribución de costes por usuario y límites de gasto.

## Puntos clave
- El gateway se despliega por tu cuenta como un único contenedor sin estado en Linux, con una base de datos PostgreSQL.
- Conserva la credencial “upstream” del proveedor y autentica a los desarrolladores mediante tu proveedor de identidad (OIDC).
- Las “managed settings” (políticas) se definen una sola vez en el servidor, se aplican al iniciar sesión en el cliente y se hacen cumplir en cada petición.
- El cliente marca métricas de uso por petición; el gateway las reenvía mediante OTLP a un colector que tú configuras.
- Puede enrutar al Claude API, Amazon Bedrock o Google Cloud, con conmutación por error opcional entre proveedores.
- Admite límites de gasto diarios, semanales y mensuales por organización, grupo o usuario.

## Recursos incluidos
- Archivos de configuración de ejemplo mencionados en el post: `gateway.yaml` y `managed-settings.json` (incluye parámetros como `forceLoginMethod` y `forceLoginGatewayUrl`).
- El gateway se distribuye dentro del mismo binario `claude` que los desarrolladores ya instalan.

## Fuente
- https://claude.com/blog/introducing-the-claude-apps-gateway
