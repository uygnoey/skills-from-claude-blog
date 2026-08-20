[English](./chrome-side-panel-adoption.en.md) · [한국어](./chrome-side-panel-adoption.ko.md) · **Español** · [日本語](./chrome-side-panel-adoption.ja.md)

# Adoptar el panel lateral de Cowork en Chrome

Una guía para personas y administradores que despliegan el cambio descrito en
[El panel lateral de Claude in Chrome ahora es Claude Cowork](https://claude.com/blog/cowork-chrome-side-panel).
Todo lo que sigue procede de ese anuncio.

## 1. Qué cambió realmente

El panel lateral de Claude in Chrome ahora ejecuta una **sesión de Claude Cowork**.

- Las conversaciones se guardan en tu historial.
- Tus skills y conectores funcionan en el navegador.
- Una tarea iniciada en una pestaña se puede terminar en las aplicaciones de escritorio, web y móvil.
- Las sesiones viven en tu **cuenta**, no en un único dispositivo.

Antes, una sesión del panel lateral estaba separada de las de las aplicaciones de Claude, así
que el contexto y las conversaciones no pasaban de una a otra.

## 2. Por qué el navegador es una superficie

Muchas herramientas se conectan directamente a Claude. Otras no: paneles internos, sistemas
heredados, portales de proveedores. Claude in Chrome es una extensión de navegador que
permite a Claude ver la página en la que estás y actuar en ella: hacer clic en enlaces,
escribir texto, navegar entre páginas y rellenar formularios, usando tus sesiones ya
iniciadas. Así es como Claude alcanza las herramientas que no tienen conector.

## 3. Un ejemplo trabajado

Supón que estás armando una hoja de presupuesto y necesitas facturas de varios portales de
proveedores. Pide a Claude in Chrome que recoja los importes y las fechas: abrirá las
pestañas, leerá cada factura y construirá la hoja. Luego retoma la sesión en la app de
escritorio para añadir archivos de tu ordenador, o importa el presupuesto del mes pasado y
pregunta qué ha cambiado. El contexto se mantiene entre superficies mientras trabajas.

## 4. El riesgo, dicho con claridad

Claude in Chrome tiene los mismos riesgos que cualquier agente de IA que actúa en un
navegador, principalmente la **inyección de prompts**. Actores maliciosos ocultan
instrucciones en contenido web: una página, un correo, un documento. Esas instrucciones
pueden no ser visibles para ti y pueden redirigir a Claude hacia acciones que nunca
pretendiste.

## 5. Las salvaguardas

**La comprobación de acciones.** Desde el piloto existe una comprobación sobre las propias
acciones de Claude. Activa "automatically approve" y Claude avanza sin detenerse a pedir
permiso en cada paso. Pero antes de cualquier acción consecuente — enviar un formulario,
mandar un mensaje, descargar un archivo — una comprobación aparte contrasta la acción con lo
que pediste originalmente y bloquea lo que no encaje. Menos interrupciones, supervisión
mantenida.

**Paradas firmes.** Claude sigue preguntando antes de ciertas acciones irreversibles o
costosas, como hacer una compra o compartir datos personales.

**El límite.** Estas medidas reducen el riesgo de forma significativa, pero no lo eliminan.
La inyección de prompts es un blanco móvil: se siguen buscando nuevos ataques y lo aprendido
se incorpora a cada modelo que se publica. Empieza en sitios de confianza; la guía de
seguridad recoge más buenas prácticas.

**Consecuencia práctica.** La comprobación se contrasta con tu *petición original*. Una
petición vaga le deja poco con qué trabajar. Indica qué sitios entran en el alcance, qué
datos recoger, qué artefacto producir y qué acciones consecuentes se esperan legítimamente.

## 6. Despliegue

**Personas.** Instala Claude in Chrome desde la Chrome Web Store, inicia sesión y abre el
panel lateral. El nuevo panel lateral está hoy en los planes Max y Team, y llega a los
usuarios Pro en las próximas semanas.

**Administradores.** En los planes Enterprise, Claude in Chrome está **desactivado por
defecto**. Los administradores pueden activarlo y limitarlo a dominios aprobados. Consulta la
guía de configuración para administradores. Secuencia práctica:

1. Decide si hace falta la superficie del navegador: se justifica donde el personal trabaja
   en sistemas sin conector.
2. Elabora la lista de dominios aprobados a partir de esos sistemas, en vez de abrir la
   extensión de forma amplia.
3. Actívala y amplía la lista de dominios conforme se establezcan necesidades concretas.

## 7. Lo que esto no cubre

- Sigues necesitando la app de escritorio de Claude para trabajar con archivos de tu
  ordenador o con otras aplicaciones.
- Claude in Chrome no funciona en otros navegadores Chromium.
- Todavía no funciona en móvil.

## 8. Lista de verificación de adopción

- [ ] Confirmado que el plan admite el nuevo panel lateral (Max/Team hoy; Pro en despliegue).
- [ ] En Enterprise: el administrador ha activado Claude in Chrome y fijado los dominios aprobados.
- [ ] Extensión instalada desde la Chrome Web Store y sesión iniciada.
- [ ] Identificados los sistemas concretos sin conector para los que sirve el navegador.
- [ ] El equipo sabe escribir briefings acotados para que la comprobación de acciones tenga con qué contrastar.
- [ ] El equipo conoce la ruta de traspaso: navegador → escritorio para archivos locales y otras aplicaciones.
- [ ] El equipo sabe que el contenido de una página es datos, no instrucciones.

## Fuente

- https://claude.com/blog/cowork-chrome-side-panel
