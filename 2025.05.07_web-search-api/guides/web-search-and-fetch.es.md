[English](./web-search-and-fetch.en.md) · [한국어](./web-search-and-fetch.ko.md) · **Español** · [日本語](./web-search-and-fetch.ja.md)

## Visión general
Esta guía resume cómo decidir cuándo habilitar web search (y la capacidad relacionada de web fetch mencionada como actualización) al construir con Claude.

## Decisión: search vs fetch
- **web search**: cuando necesitas descubrir fuentes y obtener citas.
- **web fetch**: cuando ya tienes un URL y quieres que Claude lo lea y lo analice.

## Consideraciones operativas
- La latencia puede variar por las solicitudes externas.
- Verifica que las citas respalden las afirmaciones clave.
- Si tu organización usa listas allow/block, prueba el comportamiento en dominios permitidos y bloqueados.

## Fuente
https://claude.com/blog/web-search-api
