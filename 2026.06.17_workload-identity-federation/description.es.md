[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Este post anuncia la disponibilidad general de Workload Identity Federation (WIF) en la plataforma de Claude.

## ¿Cuándo es útil?
Es útil cuando quieres que cargas de trabajo (CI, servicios en la nube, jobs de Kubernetes, etc.) llamen a las APIs de Claude sin gestionar claves de API estáticas y de larga duración.

## Puntos clave
- WIF reemplaza las claves de API estáticas por credenciales de corta duración y con alcance limitado emitidas en el momento de la solicitud.
- WIF funciona con cualquier proveedor de identidad compatible con OIDC y cubre todos los endpoints de la API de Claude (incluyendo SDKs propios y Claude Code).
- La plataforma de Claude introduce cuentas de servicio para que cada carga de trabajo tenga su propia identidad, roles y rastro de auditoría.
- Las reglas de federación vinculan identidades externas (claims del token OIDC) a cuentas de servicio de Claude.
- Las claves de API pueden coexistir con WIF, permitiendo una migración incremental.

## Recursos incluidos
- Agent Skill: Checklist conceptual para configurar cuentas de servicio y reglas de federación con WIF.

## Fuente
- https://claude.com/blog/workload-identity-federation
