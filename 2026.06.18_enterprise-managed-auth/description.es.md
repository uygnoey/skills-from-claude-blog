[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Este post anuncia la autorización gestionada por la empresa para conectores MCP en Claude, empezando con el aprovisionamiento mediante Okta.

## ¿Cuándo es útil?
Es útil cuando necesitas que TI gestione de forma centralizada el acceso a conectores en un entorno corporativo, con acceso automático para el usuario en su primer inicio de sesión y revocación gobernada por el IdP.

## Puntos clave
- Los administradores autorizan un conector una sola vez; los usuarios heredan el acceso mediante grupos y roles del IdP.
- Configuración “sin intervención” para el usuario final (sin paso de autorización OAuth por usuario).
- Acceso coherente en Claude chat, Claude Code y Cowork.
- Se basa en una extensión abierta de autorización empresarial del Model Context Protocol, por lo que los conectores personalizados pueden soportarla.
- La gestión centralizada permite acortar la vida de los tokens y acelerar la desactivación al retirar permisos.

## Recursos incluidos
- Skill: enterprise-managed-connector-auth (lista de verificación + pasos de despliegue)
- Guide: enterprise-managed-connector-auth-rollout (guía práctica de adopción)

## Fuente
- https://claude.com/blog/enterprise-managed-auth
