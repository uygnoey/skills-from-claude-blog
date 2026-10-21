[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un anuncio de que Claude para Google Workspace está en beta pública en todos los planes de pago de
Claude. Abre un panel lateral de Claude junto a un Doc, Sheet o presentación de Slides abiertos, que
puede leer el archivo, ver la selección y editarlo directamente. Los nuevos conectores de Google Docs,
Sheets y Slides (beta) también permiten a Claude crear y editar archivos de Google desde un chat.

## ¿Cuándo es útil?
- Cuando quieres que Claude edite, analice o cree contenido dentro de un archivo de Google ya abierto.
- Cuando quieres empezar en Claude y generar un documento, hoja o presentación nuevos, o trabajar con
  varios archivos.
- Cuando un administrador planifica un despliegue para todo el dominio o por grupos.

## Puntos clave
- Docs: ediciones pequeñas en el sitio; las reescrituras grandes llegan como tarjetas de sugerencia
  que se pueden aplicar o descartar.
- Sheets: fórmulas, tablas dinámicas, gráficos nativos, pestañas nuevas y limpieza o unión de datos
  ejecutando Python sobre un rango y escribiendo los resultados.
- Slides: crea diapositivas con los diseños y temas de la presentación y luego revisa elementos
  superpuestos o fuera de la diapositiva y texto difícil de leer.
- Modos de edición: "Ask before edits" (predeterminado, cada cambio es una tarjeta de aprobación) o
  "Accept all edits".
- El panel usa los mismos modelos, conectores y skills que Claude normal; también aplican los
  controles empresariales (Compliance API, claves de cifrado gestionadas por el cliente, exportación
  de auditoría con OpenTelemetry).
- El acceso a archivos sigue los permisos de uso compartido de Google existentes.
- Configuración: instalar desde Google Workspace Marketplace y luego Extensiones > Claude > Open
  Claude. Los administradores pueden desplegarlo al dominio o a grupos desde la consola de
  administración de Google; en Team y Enterprise, un propietario o propietario principal debe activar
  antes los conectores.

## Recursos incluidos
- Skill: `google-workspace-editing` — elegir entre complemento y conectores, modos de edición y
  patrones por aplicación, con ejemplos en `examples/task-prompts.md`.
- Guía: `google-workspace-rollout` (en/ko/es/ja) — configuración individual y despliegue en la
  organización.

## Fuente
- https://claude.com/resources/articles/claude-now-works-in-google-docs-sheets-and-slides
