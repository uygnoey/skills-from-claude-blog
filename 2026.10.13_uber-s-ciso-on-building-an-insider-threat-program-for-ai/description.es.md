[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Una entrevista con Philip Martin, CISO de Uber, sobre por qué los agentes de IA necesitan el mismo tipo
de programa de amenazas internas (insider threat) que las empresas ya aplican a sus empleados, cómo los
modelos de frontera cambian el trabajo de seguridad y cómo la herramienta de código abierto de Uber, AI
Detection and Response (ADR), funciona junto con Enterprise Frontier Safeguards de Anthropic.

## ¿Cuándo es útil?
- Al diseñar monitorización, detección y respuesta para agentes de IA dentro de una empresa.
- Al combinar la telemetría propia de los agentes con las señales de salvaguarda del proveedor del modelo.
- Al decidir dónde deben centrarse los defensores para proteger sistemas de IA.
- Al justificar ante la dirección la monitorización de despliegues de modelos de frontera.

## Puntos clave
- Los modelos de frontera pueden incorporar mucho más contexto en horizontes largos (código, documentos de
  diseño, incidencias de Jira, historial del servicio) y generar modelos de amenazas y revisiones de
  seguridad muy específicos. Martin prevé agentes por servicio que intercambien modelos de amenazas entre sí.
- Enterprise Frontier Safeguards: Uber conserva el control de sus datos (Anthropic no puede acceder sin
  permiso) y de las acciones que se toman cuando salta una salvaguarda.
- Arquitectura de seguridad de IA de Uber: un gateway de LLM como perímetro, ADR de código abierto para
  telemetría y acción en tiempo real en los arneses de agentes, y la salida del clasificador del proveedor
  integrada en el entorno de detección.
- Prioridad 1: detección e intervención en tiempo real, lo más cerca posible del momento en que una persona
  escribe un prompt o el modelo llama a una herramienta.
- Prioridad 2: entender los patrones emergentes — descubrir nuevos comportamientos, crear salvaguardas y
  repetir (las restricciones generan comportamientos nuevos).
- Toda empresa tiene un programa de amenazas internas para las personas; los modelos introducen el mismo
  riesgo y necesitan el equivalente.

## Recursos incluidos
- Skill: `ai-insider-threat-program` — arquitectura por capas, intervención en tiempo real, ciclo de
  descubrimiento de comportamientos (`references/ai-security-architecture.md`).
- Guía: "Proteger a los agentes de IA como a personal interno" (4 idiomas).

## Fuente
- https://claude.com/resources/articles/uber-s-ciso-on-building-an-insider-threat-program-for-ai
