[English](./enterprise-managed-connector-auth-rollout.en.md) · [한국어](./enterprise-managed-connector-auth-rollout.ko.md) · **Español** · [日本語](./enterprise-managed-connector-auth-rollout.ja.md)

# Guía de despliegue de autorización empresarial de conectores (Okta)

## Objetivo
Implantar una autorización gestionada centralmente para conectores MCP, de modo que los usuarios hereden el acceso mediante grupos y roles del IdP y puedan usarlos desde el primer inicio de sesión.

## Fases recomendadas
1. Definir alcance: conectores, grupo piloto y criterios de éxito.
2. Aprovisionar de forma centralizada: el admin autoriza una vez y delimita por grupo/rol del IdP.
3. Validación en piloto: comprobar acceso “sin intervención” y comportamiento de revocación.
4. Despliegue a producción: ampliar asignaciones; documentar procedimientos de soporte.

## Consideraciones operativas
- Gestiona el acceso a conectores como el resto de tu control de accesos: aprovisiona, audita y revoca desde el IdP.
- Considera acortar la vida de los tokens para reducir accesos persistentes tras la desactivación.
- Si es necesario, exige conexiones solo vía IdP para evitar mezclar cuentas personales y corporativas.

## Fuente
- https://claude.com/blog/enterprise-managed-auth
