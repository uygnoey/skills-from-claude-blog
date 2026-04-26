[English](./transition-roadmap.en.md) · [한국어](./transition-roadmap.ko.md) · **Español** · [日本語](./transition-roadmap.ja.md)

# Hoja de ruta de transición

Una guía breve de transición a nivel organizacional, derivada de [What are the key benefits of transitioning to agentic coding for software development?](https://claude.com/blog/key-benefits-transitioning-agentic-coding) (2025-12-01). Úsala como checklist cuando planifiques la adopción de Claude Code más allá de un solo equipo.

## 1. Encuadra el caso

Elige los dos o tres beneficios que más resuenen con tu audiencia:

- Liderazgo de ingeniería: aceleración de tiempos + escalar sin crecimiento lineal de headcount.
- Engineering managers: compresión del onboarding + acceso democratizado.
- Ingenieros senior: resolución autónoma de problemas + calidad sistemática.
- Seguridad / plataforma: calidad sistemática + modelo de permisos.
- Reclutamiento: acceso democratizado (cambio en hiring: "fundamentos + especialización cubierta por agentes").
- Finanzas: aceleración de tiempos atada a la economía del proyecto.

## 2. Sustenta con evidencia

- Cita el caso enterprise de Augment Code (2 semanas vs. 4–8 meses) y la frase de Guy Gur-Ari: "Tasks that would take weeks for a developer to learn can now be completed in a day or two."
- Cita el asistente de Grafana con PromQL/LogQL en lenguaje natural (acceso democratizado).

## 3. Piloto con un equipo enfocado

- Elige un equipo con un campeón senior dispuesto.
- Instala Claude Code en terminal o IDE; ve a la raíz del proyecto; ejecuta `claude`.
- Corre tareas iniciales: manejo de errores en un endpoint, refactor de un componente complejo, tests para código sin cobertura.
- Durante el piloto, exige aprobación antes de cualquier escritura.

## 4. Define criterios de salida del piloto

Tras dos a cuatro semanas, evalúa contra:

- Tiempo de ciclo en tareas asignadas frente a la línea base previa al piloto.
- Tiempo de onboarding para nuevos integrantes durante el piloto.
- Señal de calidad: incidentes, comentarios por PR, defectos detectados.
- Señal de experiencia: ¿los ingenieros quieren seguir usándolo?

## 5. Expande con criterio

- Agrega archivos CLAUDE.md en la raíz de cada proyecto para que estándares y decisiones persistan entre sesiones y colaboradores.
- Conecta servidores MCP para herramientas fuera del repositorio (gestores de issues, sistemas de diseño, docs internas).
- Posiciona a los agentes como guardianes de calidad y compañeros de pensamiento — no como piloto automático — al definir responsabilidades.

## 6. Mide y comparte resultados

Traduce los beneficios a métricas locales. Las "2 semanas vs. 8 meses" de Augment Code es solo el ejemplo del post; cada equipo debería publicar sus propios equivalentes — tiempo de ciclo, tiempo de onboarding, toil reducido — para que el liderazgo compare decisiones de adopción entre equipos.

## Fuente

[What are the key benefits of transitioning to agentic coding for software development?](https://claude.com/blog/key-benefits-transitioning-agentic-coding) (publicado el 2025-12-01).
