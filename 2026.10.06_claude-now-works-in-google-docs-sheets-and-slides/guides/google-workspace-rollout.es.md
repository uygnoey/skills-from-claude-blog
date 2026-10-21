[English](./google-workspace-rollout.en.md) · [한국어](./google-workspace-rollout.ko.md) · **Español** · [日本語](./google-workspace-rollout.ja.md)

# Implementar Claude para Google Workspace

Hay dos formas de usar Claude con Google Docs, Sheets y Slides. Esta guía explica cómo configurar
cada una para un usuario individual y para una organización.

## Dos superficies

| | Complemento (panel lateral) | Conectores (desde el chat) |
|---|---|---|
| Punto de partida | Un archivo de Google abierto | Una conversación con Claude |
| Ideal para | Editar el archivo que tienes delante, trabajar sobre una selección | Archivos nuevos, trabajo que abarca varios archivos |
| Estado | Beta pública, todos los planes de pago de Claude | Beta |
| Acceso a archivos | Sigue tus permisos de uso compartido de Google | Sigue tus permisos de uso compartido de Google |

El complemento usa los mismos modelos, conectores y skills que Claude normal.

## Configuración individual
1. Instala Claude desde Google Workspace Marketplace.
2. Abre un Doc, Sheet o presentación de Slides y elige Extensiones > Claude > Open Claude.
3. Elige un modo de edición: **Ask before edits** (predeterminado; cada cambio es una tarjeta de
   aprobación) o **Accept all edits** (los cambios se aplican sin detenerse).
4. Para trabajar desde el chat, activa los conectores de Google Docs, Sheets y Slides y pega un
   enlace o pide un archivo nuevo.

## Implementación en la organización
1. **Despliega el complemento** desde la consola de administración de Google a todo el dominio o a
   grupos seleccionados.
2. **Activa los conectores**: en los planes Team y Enterprise, un propietario o propietario principal
   debe activarlos antes de que los usuarios puedan usarlos.
3. **Confirma los controles empresariales**: la Compliance API, las claves de cifrado gestionadas por
   el cliente y la exportación de auditoría con OpenTelemetry también se aplican al complemento.
4. **Define un modo de edición predeterminado** por equipo (p. ej., mantener "Ask before edits" en
   archivos compartidos). Es una práctica sugerida, no un requisito del artículo.
5. **Comparte formatos reutilizables como skills** para obtener resultados coherentes (p. ej., un
   formato de presentación de revisión).

## A tener en cuenta
- Ambas superficies están en beta.
- El artículo no menciona el historial de versiones ni cómo deshacer; consulta la guía de
  configuración del Centro de ayuda.

## Fuente
- https://claude.com/resources/articles/claude-now-works-in-google-docs-sheets-and-slides
