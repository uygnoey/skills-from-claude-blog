[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Anthropic anunció que Claude Code y Claude Cowork están disponibles en beta pública a través de Claude for Government Desktop, entregados mediante un entorno autorizado FedRAMP High. Las agencias reciben las capacidades en el mismo calendario de publicación que los clientes comerciales.

El anuncio cubre cuatro áreas: dónde residen los datos (la inferencia dentro del entorno autorizado, el historial de conversación almacenado localmente en el dispositivo gestionado por la agencia), cómo se acota el gasto (asientos estándar o niveles personalizados, uso comprado en incrementos fijos con un tope duro de no superación), cómo se delega la administración (asignación de asientos a nivel departamental, asignaciones de grupo por SCIM para límites de tasa, topes en dólares y modelos permitidos, y configuración por capas con valores por defecto para las subagencias) y cómo funciona la supervisión (log de auditoría encadenado por hash revisable en el producto, aprobación de dos personas para operaciones sensibles del lado de Anthropic, exportaciones de uso con datos de medición únicamente). Documentos de apoyo: una FedRAMP Secure Configuration Guide pública y la notificación formal de cambios, más un resumen de prueba de penetración bajo NDA a través del centro de confianza de Anthropic. La aplicación de escritorio se despliega mediante plataformas MDM estándar de agencia.

## ¿Cuándo es útil?
- Al preparar un paquete de ATO o una revisión de seguridad en la que hay que declarar dónde ocurre el procesamiento y dónde reposan los datos.
- Cuando un departamento debe repartir asientos y límites distintos entre subagencias bajo una sola autorización.
- Cuando finanzas necesita conciliar el precio por consumo con fondos presupuestados.
- Cuando un inspector general o un auditor pide cifras de uso y el material sensible no puede salir del perímetro.
- Al planificar la distribución por MDM y la política de endpoints de una herramienta cuyas transcripciones viven en el portátil.

## Puntos clave
- **FedRAMP High, con la inferencia dentro del perímetro.** Entregado a través de Claude for Government Desktop, actualmente en beta pública.
- **El historial de conversación es local.** Reside en el dispositivo gestionado por la agencia, lo que sitúa el endpoint dentro del alcance: cifrado de disco, copias de seguridad, retención y procedimientos de pérdida del dispositivo son política de endpoints de la agencia, no retención del proveedor.
- **El gasto está acotado por un tope duro.** El uso se compra en incrementos fijos con un tope de no superación, se sigue por usuario y por modelo en la consola de administración, y hay alertas automáticas de consumo antes de que se agote el saldo.
- **Los límites viajan con la identidad.** Las asignaciones de grupo por SCIM fijan límites de tasa, topes en dólares y modelos permitidos por grupo; la configuración por capas establece los valores por defecto de cada subagencia sobre a qué puede conectarse Claude y qué funciones están disponibles.
- **La supervisión viene incorporada.** Un log de auditoría encadenado por hash es revisable directamente en el producto por los administradores de la organización, y las operaciones sensibles del lado de Anthropic requieren aprobación de dos personas.
- **Las exportaciones de uso contienen solo datos de medición,** de modo que las preguntas de ATO e IG pueden responderse sin mover material sensible.
- **Documentación en dos niveles.** La FedRAMP Secure Configuration Guide y la notificación formal de cambios son públicas; el resumen de la prueba de penetración está bajo NDA a través del centro de confianza.
- **Mismo calendario de publicación que los clientes comerciales:** un beneficio y una obligación de gestión del cambio a la vez.
- **Anthropic es la parte contratante para la facturación;** no se requiere una relación aparte con un proveedor de nube. Los clientes nuevos solicitan acceso en claude.com/solutions/government.

## Recursos incluidos
- `skills/government-deployment-planning/SKILL.md` — el despliegue como procedimiento de siete pasos, del perímetro de autorización al registro de riesgos.
- `skills/government-deployment-planning/references/controls-inventory.md` — toda la superficie de control anunciada, agrupada por la pregunta que hará un revisor.
- `skills/government-deployment-planning/templates/rollout-checklist.md` — una lista de trabajo que cubre autorización, evidencias, identidad, coste, supervisión, endpoint, contratación y usuarios.
- `skills/government-deployment-planning/templates/evidence-map.md` — una tabla de una página que enlaza pregunta del revisor con artefacto, para un paquete de ATO.
- `guides/agency-rollout.{en,ko,es,ja}.md` — qué significa el anuncio en la práctica para quienes autorizan, financian, administran y distribuyen.

## Fuente
[Bringing Claude Code and Claude Cowork to government](https://claude.com/blog/bringing-claude-code-and-claude-cowork-to-government) — publicado el 2026-07-07.
