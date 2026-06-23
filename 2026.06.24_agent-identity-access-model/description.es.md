[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Este post explica el modelo de acceso de “identidad de agente” (agent identity) en Claude Tag: cómo las identidades de herramientas aprovisionadas por el administrador del workspace permiten que Claude opere en canales compartidos sin usar las cuentas personales de cada usuario.

## ¿Cuándo es útil?
Es útil cuando habilitas agentes de IA en espacios de equipo (canales compartidos, proyectos, workspaces) y necesitas un modelo de permisos auditable, revocable y acotado para que el acceso del agente no se expanda accidentalmente más allá de lo concedido explícitamente.

## Puntos clave
- Las experiencias multiusuario requieren identidades de herramientas propiedad del workspace, no cuentas personales.
- Los permisos deben estar acotados por canal (o un espacio compartido equivalente) y poder revocarse de forma centralizada.
- Despliega el acceso de manera gradual: empieza con un perfil base en pocos canales, revisa el rastro de auditoría y luego amplía de forma deliberada.
- Mantén límites firmes para que los espacios compartidos no se conviertan en una “puerta lateral” hacia documentos privados; la memoria y el acceso deben respetar esos límites.
- Prefiere un patrón de credenciales donde se almacenan de forma independiente, se asignan a la identidad del canal y se inyectan solo en el momento de la solicitud.
- Bloquea el tráfico saliente hacia hosts no aprobados y audita cada rutina, escritura de memoria y llamada de red.

## Recursos incluidos
- Skill: “Agent identity access model playbook” (guía destilada de este post)

## Fuente
- https://claude.com/blog/agent-identity-access-model
