[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un anuncio de que **el panel lateral de Claude in Chrome ahora ejecuta una sesión de Claude Cowork**. Hasta ahora, una conversación en el panel lateral estaba separada de las de las aplicaciones de Claude, así que el contexto no pasaba de una a otra. Ahora las conversaciones se guardan en tu historial, tus skills y conectores funcionan en el navegador, y una tarea que empiezas en una pestaña se puede terminar en las aplicaciones de escritorio, web y móvil — porque las sesiones viven en tu cuenta y no en un único dispositivo. Está disponible hoy en los planes Max y Team, y llegará a los usuarios Pro en las próximas semanas.

El post explica para qué sirve la superficie del navegador: muchas herramientas se conectan directamente a Claude, pero otras no — paneles internos, sistemas heredados, portales de proveedores — y Claude in Chrome puede trabajar en ellas a través del navegador, usando tus sesiones ya iniciadas para hacer clic en enlaces, escribir texto, navegar entre páginas y rellenar formularios. Después aborda el riesgo de frente. Claude in Chrome tiene la misma exposición a la inyección de prompts que cualquier agente de IA que actúa en un navegador: instrucciones ocultas en una página, un correo o un documento — posiblemente invisibles para ti — pueden redirigir a Claude. Desde el piloto se ha añadido una comprobación sobre las propias acciones de Claude: con "automatically approve" activado, Claude avanza sin detenerse en cada paso, pero antes de cualquier acción consecuente (enviar un formulario, mandar un mensaje, descargar un archivo) una comprobación aparte contrasta la acción con lo que pediste originalmente y bloquea lo que no encaje. Claude sigue preguntando antes de ciertas acciones irreversibles o costosas. El post es explícito: estas medidas reducen el riesgo de forma significativa, pero no lo eliminan.

## ¿Cuándo es útil?
- Cuando el trabajo vive en una herramienta sin conector directo a Claude: un panel interno, un sistema heredado, un portal de proveedor.
- Cuando una tarea empieza en el navegador y hay que terminarla donde están los archivos locales, o al revés.
- Cuando decides cuánta autonomía dar a un agente de navegador y quieres el modelo real de salvaguardas, no un eslogan.
- Cuando un administrador activa Claude in Chrome en una organización Enterprise y necesita acotar los dominios aprobados.

## Puntos clave
- **El panel lateral es una sesión de Cowork.** Las conversaciones se guardan en tu historial; las skills y los conectores funcionan en el navegador.
- **Las sesiones siguen a la cuenta, no al dispositivo.** Empieza en una pestaña y continúa en la app de escritorio, web o móvil: el contexto viaja entre superficies.
- **Lo que Claude puede hacer en una página:** ver la página en la que estás, hacer clic en enlaces, escribir texto, navegar entre páginas y rellenar formularios, usando tus sesiones ya iniciadas.
- **Por qué importa el navegador:** llega a paneles internos, sistemas heredados y portales de proveedores que no se conectan directamente a Claude.
- **Ejemplo del post:** pedir a Claude in Chrome que recoja importes y fechas de facturas en varios portales de proveedores y construya una hoja de presupuesto; luego retomar la sesión en la app de escritorio para añadir archivos locales o importar el presupuesto del mes pasado y preguntar qué ha cambiado.
- **La inyección de prompts es el riesgo principal.** Instrucciones maliciosas ocultas en contenido web — una página, un correo, un documento — pueden ser invisibles para ti y redirigir a Claude hacia acciones que nunca pediste.
- **Comprobación de acciones.** Con "automatically approve", una comprobación aparte contrasta cada acción consecuente (enviar un formulario, mandar un mensaje, descargar un archivo) con tu petición original y bloquea lo que no encaje: menos interrupciones, supervisión mantenida.
- **Siguen existiendo paradas.** Claude pregunta antes de ciertas acciones irreversibles o costosas, como hacer una compra o compartir datos personales.
- **Límite declarado.** Estas medidas reducen el riesgo de forma significativa, pero no lo eliminan; la inyección de prompts es un blanco móvil. Empieza en sitios de confianza.
- **Disponibilidad.** Max y Team hoy; Pro en las próximas semanas. En Enterprise, Claude in Chrome está **desactivado por defecto** — los administradores lo activan y pueden limitarlo a dominios aprobados.
- **Lo que no cubre.** Sigues necesitando la app de escritorio para archivos de tu ordenador o para otras aplicaciones; Claude in Chrome todavía no funciona en otros navegadores Chromium ni en móvil.

## Recursos incluidos
- `skills/browser-side-panel-sessions/SKILL.md` — decide cuándo ejecutar una tarea en el navegador, pásala entre superficies y fija el nivel de autonomía adecuado.
- `skills/browser-side-panel-sessions/references/risk-and-guardrails.md` — el riesgo de inyección de prompts y el modelo de salvaguardas, tal como los expone el post.
- `skills/browser-side-panel-sessions/references/surface-capabilities.md` — qué puede y qué no puede hacer cada superficie, y la disponibilidad por plan.
- `skills/browser-side-panel-sessions/templates/browser-task-brief.md` — un briefing rellenable que le facilita el trabajo a la comprobación de acciones.
- `guides/chrome-side-panel-adoption.{en,ko,es,ja}.md` — la guía completa de adopción y administración en cuatro idiomas.

## Fuente
- https://claude.com/blog/cowork-chrome-side-panel
