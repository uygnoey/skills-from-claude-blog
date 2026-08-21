[English](./agency-rollout.en.md) · [한국어](./agency-rollout.ko.md) · **Español** · [日本語](./agency-rollout.ja.md)

# Desplegar herramientas de codificación agéntica dentro de una agencia pública

Claude Code y Claude Cowork ya están disponibles en beta pública a través de Claude for
Government Desktop, entregados mediante un entorno autorizado FedRAMP High. Esta guía recorre
lo que eso significa en la práctica para quienes deben autorizar, financiar, administrar y
distribuir la herramienta.

## Los dos hechos que reconfiguran el plan

Casi toda la planificación se deriva de dos propiedades de la oferta, y ambas suelen pasarse
por alto en una primera lectura.

**El historial de conversación se almacena localmente en el dispositivo gestionado por la
agencia.** La inferencia corre dentro del entorno autorizado FedRAMP High, pero la
transcripción queda en el portátil. Eso sitúa el endpoint dentro del alcance. En un plan de
seguridad del sistema se trata de datos en poder de la agencia, regidos por su política de
endpoints —cifrado de disco, gestión de copias de seguridad, retención, pérdida del
dispositivo y borrado remoto— y no de una retención por parte del proveedor. Los revisores
que llegan esperando un calendario de retención del proveedor quedan satisfechos antes cuando
ese desplazamiento de alcance se enuncia desde el principio en lugar de descubrirse a mitad
de la evaluación.

**Las exportaciones de uso contienen solo datos de medición.** Eso es lo que permite a una
agencia responder a una pregunta de ATO o a una solicitud del inspector general sobre uso sin
sacar material sensible del perímetro. Conviene sacarlo pronto a la mesa, porque elimina una
objeción antes de que se formule.

## Autorización

La oferta se entrega a través de un entorno autorizado FedRAMP High, y la inferencia se
ejecuta dentro de él. Hay tres documentos que respaldan la revisión, con dos niveles de
disponibilidad: la FedRAMP Secure Configuration Guide y la notificación formal de cambios son
públicas, y el resumen de la prueba de penetración está disponible bajo NDA a través del
centro de confianza de Anthropic.

Construye el mapa de evidencias antes de la reunión de evaluación, no durante. Cada pregunta
del revisor debería tener detrás un artefacto con nombre, y cada pregunta que el anuncio no
responde debería quedar registrada como punto abierto en lugar de rellenarse por suposición.

Algo más pertenece al expediente: la oferta se anuncia como beta pública. Eso es una entrada
en el registro de riesgos, no un detalle que descubrir durante la revisión.

## Administración delegada

La premisa de diseño es que un departamento autoriza una vez y después delega la operación,
en lugar de repetir la contratación y la configuración para cada componente. Los
administradores de nivel departamental asignan asientos a las subagencias, y los límites
viajan con la identidad.

Las asignaciones de grupo por SCIM fijan los límites de tasa, los topes en dólares y los
modelos permitidos de cada grupo. La configuración por capas establece los valores por
defecto de cada subagencia: a qué puede conectarse Claude y qué funciones están disponibles.
Así, tres subagencias con tres posturas de riesgo distintas bajo una sola autorización es un
ejercicio de configuración y no tres acuerdos separados, siempre que la estructura de grupos
sea correcta antes de aprovisionar a nadie.

Resuelve primero esa estructura, asigna un grupo por subagencia y prueba explícitamente el
desaprovisionamiento. Quitar a una persona del grupo tiene que retirarle el acceso, y eso es
algo que se verifica, no que se supone.

## Financiación

El precio por consumo y los fondos presupuestados se reconcilian mediante un solo mecanismo:
el uso se compra en incrementos fijos con un tope duro de no superación. Cuando finanzas
pregunte qué impide una factura abierta, ese tope es la respuesta.

Las organizaciones pueden tomar asientos estándar o un nivel personalizado con límites de
gasto y de modelos. Los administradores siguen el uso por usuario y por modelo en la consola
de administración, y unas alertas automáticas de consumo avisan antes de que el saldo se
agote.

Esas alertas merecen un momento de atención durante la puesta en marcha. Un tope sin alertas
convierte un control presupuestario en una interrupción del servicio: dirige las alertas a
alguien con autoridad para recargar y acuerda la vía de recarga antes de que el primer saldo
se agote, no después.

## Supervisión

Las acciones administrativas quedan registradas en un log de auditoría encadenado por hash
que los administradores de la organización pueden revisar directamente en el producto. Del
lado del proveedor, las operaciones sensibles requieren aprobación de dos personas: esa es la
respuesta al revisor que pregunta qué impide una actuación unilateral de Anthropic.

Asigna revisores con nombre y una cadencia para el log de auditoría durante el despliegue. Un
log que nadie lee es prueba de que el control existe, no de que opera.

## Distribución y cambios

La aplicación de escritorio se despliega mediante plataformas MDM estándar de agencia, así
que la distribución usa maquinaria que las agencias ya tienen. Haz un piloto con un anillo
antes de la difusión amplia, y asegúrate de que la política de endpoints cubra el historial
de conversación almacenado localmente antes de que ese anillo salga.

Las agencias reciben las capacidades en el mismo calendario de publicación que los clientes
comerciales. Ese es el beneficio principal —no esperar trimestres por detrás del producto
comercial— y es también una obligación, porque el cambio llega con la cadencia comercial y la
gestión del cambio de la agencia tiene que absorberlo. La notificación formal de cambios es
el mecanismo para eso; enrútala a quien deba enterarse.

## Contratación

Los clientes nuevos solicitan acceso en claude.com/solutions/government. Anthropic sigue
siendo la parte contratante para la facturación, y no se requiere una relación aparte con un
proveedor de nube.

## Una secuencia practicable

1. Fija el perímetro de autorización y deja por escrito dónde ocurre el procesamiento y dónde
   reposan los datos.
2. Reúne los tres documentos y construye el mapa de evidencias.
3. Diseña la estructura de grupos y después aprovisiona.
4. Elige el modelo de licencia, fija el tope y enruta las alertas.
5. Asigna revisores del log de auditoría y una cadencia.
6. Empaqueta para MDM, confirma la política de endpoints y pilota un anillo.
7. Registra el estado de beta y las preguntas abiertas en el registro de riesgos.

Los pasos 1 y 3 son los caros de rehacer. El resto puede ajustarse una vez que el primer
anillo esté en marcha.

## Fuente

[Bringing Claude Code and Claude Cowork to government](https://claude.com/blog/bringing-claude-code-and-claude-cowork-to-government) — publicado el 2026-07-07.
