[English](./securing-ai-agents-like-insiders.en.md) · [한국어](./securing-ai-agents-like-insiders.ko.md) · **Español** · [日本語](./securing-ai-agents-like-insiders.ja.md)

# Proteger a los agentes de IA como a personal interno

Lecciones de Philip Martin, CISO de Uber, sobre la arquitectura de seguridad y las prioridades al
desplegar modelos de frontera dentro de una empresa.

## 1. Por qué un programa de amenazas internas para la IA
- Las empresas ya tienen programas de amenazas internas para sus empleados y aceptan una retención de
  datos y una monitorización a veces onerosas, porque las personas actúan a veces fuera de los límites
  de su función.
- Los modelos de frontera también pueden recibir instrucciones para actuar fuera de las restricciones
  esperadas. El riesgo crece a medida que son más capaces y autónomos.
- Adoptar la IA es un imperativo de negocio; el programa es lo que permite desplegarla de forma segura.
- Martin presta mucha atención al mal uso accidental, no solo al abuso deliberado.

## 2. Arquitectura
| Capa | Función |
|---|---|
| Gateway de LLM | Perímetro que controla cómo se usa la IA en la empresa |
| AI Detection and Response (ADR, código abierto) | Telemetría y acción en tiempo real en los arneses de agentes desplegados |
| Enterprise Frontier Safeguards | Señales del clasificador del proveedor; la empresa controla sus datos y la respuesta |
| Entorno de detección | Correlaciona ambas fuentes, como un entorno de ciberseguridad tradicional |

El objetivo es reunir contexto y decidir lo más rápido y con la mayor certeza posible.

## 3. Dónde centrarse a continuación
1. **Detección e intervención en tiempo real** — avisar a la persona en el arnés antes de un prompt
   arriesgado o antes de que el modelo llame a una herramienta o se conecte a un destino indebido.
2. **Patrones emergentes** — analizar tendencias de comportamiento (a menudo con ayuda de LLM),
   encontrar comportamientos nuevos, incorporar salvaguardas a la plataforma en tiempo real y repetir.
   Las restricciones generan comportamientos nuevos.

## 4. Los modelos como compañeros de seguridad
- Dar al modelo el código, los documentos de diseño, las incidencias de Jira y el historial del servicio
  para revisiones y modelos de amenazas.
- Dirección futura: un agente por servicio que lo conozca bien e intercambie modelos de amenazas con los
  agentes de otros servicios.

## Fuente
- https://claude.com/resources/articles/uber-s-ciso-on-building-an-insider-threat-program-for-ai
