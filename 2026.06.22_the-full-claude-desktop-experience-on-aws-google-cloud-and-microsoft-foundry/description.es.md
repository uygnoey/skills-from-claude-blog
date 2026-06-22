[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Este post anuncia que las organizaciones que usan Claude Desktop a través de AWS, Google Cloud o Microsoft Foundry ahora disponen de la experiencia completa en una sola app: Chat, Claude Cowork y Claude Code.

## ¿Cuándo es útil?
Es útil cuando eres administrador/a o responsable de TI/seguridad y quieres desplegar Claude Desktop a toda la organización manteniendo la inferencia dentro de tu entorno cloud elegido y gestionando el acceso con identidad empresarial y gestión de dispositivos.

## Puntos clave
- Un único despliegue cubre Chat, Claude Cowork y Claude Code, con una clave de política separada por cada superficie para controlar quién accede a qué.
- Los empleados inician sesión con proveedores de identidad empresariales existentes (p. ej., IAM Identity Center, Microsoft Entra ID u otros proveedores OIDC) en lugar de claves compartidas.
- Los administradores pueden exportar plantillas de políticas desde la interfaz de configuración y distribuirlas con herramientas comunes de MDM/gestión de endpoints (p. ej., Intune, GPO, Jamf), incluyendo una opción de instalador sin conexión para entornos aislados (air-gapped).
- La validación previa al despliegue incluye probar conectores, confirmar los modelos de Claude disponibles y verificar la conectividad; se menciona un “model guard” para mantener el enrutamiento en Claude incluso si hay una mala configuración.
- El acceso a Microsoft 365 puede habilitarse mediante un conector usando tu propia app de Entra con allowlisting del tenant; para requisitos estrictos de residencia se describe una opción de conector local.

## Recursos incluidos
- El post hace referencia a plantillas de políticas (exportadas desde la UI de configuración) y a una guía de despliegue para administradores (SSO, plantillas de políticas y validación previa).

## Fuente
- https://claude.com/blog/the-full-claude-desktop-experience-on-aws-google-cloud-and-microsoft-foundry
