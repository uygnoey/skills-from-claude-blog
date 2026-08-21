[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Una actualización sobre cómo Anthropic está poniendo la capacidad de ciberdefensa de frontera en manos de más defensores. Claude Mythos 5 ya está disponible en Claude Security y llegará pronto a las herramientas de ciberdefensa de los socios; un Defender Advantage Fund de 35 millones de dólares respalda el trabajo de seguridad en código abierto; y el Cyber Verification Program se amplía hacia el acceso de clase Mythos.

La idea que lo organiza todo tiene que ver con la forma de la interacción, no con el tamaño del modelo. El acceso directo al modelo es donde un actor malicioso puede intentar dirigirlo hacia usos dañinos. Si los usuarios solo pueden recibir salidas específicas —un parche para una vulnerabilidad, una alerta de seguridad— ese riesgo es mucho menor. Cada una de las cuatro vías de acceso amplía el acceso de los defensores a los *resultados* defensivos manteniendo las barreras sobre el acceso directo al modelo.

## ¿Cuándo es útil?
- Al decidir qué vía de acceso encaja con tu situación: eres dueño del código, construyes productos de seguridad, apoyas a mantenedores de código abierto, o necesitas salvaguardas reducidas para trabajo defensivo autorizado.
- Cuando un administrador de empresa habilita Claude Security y orienta a un equipo hacia un escaneo de repositorio.
- Al triar hallazgos de escaneo que llegan con categoría CWE, valoraciones de confianza y severidad, y una corrección sugerida.
- Al diseñar un producto o flujo de trabajo sobre capacidad de frontera cuando hay que preservar la forma de "salidas específicas, no acceso al modelo".
- Cuando un proyecto de código abierto necesita recursos para parchear vulnerabilidades o automatizar el escaneo.

## Puntos clave
- **La forma de la interacción es el control.** "Si los usuarios solo pueden recibir salidas específicas, como un parche para una vulnerabilidad o una alerta de seguridad, ese riesgo es mucho menor" que con acceso directo al modelo.
- **Project Glasswing** (abril) puso Mythos Preview y Mythos 5 con un grupo reducido que protege el software más crítico del mundo, dando a los defensores una ventana antes de que una capacidad comparable estuviera ampliamente disponible. **Claude Fable 5** fue el primer paso amplio: disponible para todos, con el trabajo cibernético de doble uso bloqueado.
- **Integraciones de socios:** Mythos 5 se está incorporando a los productos que los defensores ya usan para operaciones de seguridad, respuesta a incidentes, inteligencia de amenazas e ingeniería de detección. El usuario final trabaja mediante una interfaz de propósito específico que ejecuta Mythos en segundo plano para una tarea definida y recibe solo el artefacto previsto —parches sugeridos, por ejemplo, sin forma de pedir un exploit—. Hay medidas de prevención de abuso que verifican que el modelo se mantiene dentro del alcance.
- **Los escaneos de Claude Security ya se ejecutan con Mythos 5.** Beta pública para Claude Enterprise; los administradores lo habilitan en la admin console; desde `claude.ai/security` seleccionas un repositorio; los hallazgos llegan con categoría CWE, valoraciones de confianza y severidad, y una corrección sugerida. Se factura como uso estándar de tokens, sin complemento aparte.
- **El parcheo conserva una puerta humana.** Abre Claude Code en la web para implementar la corrección. El parcheo interactivo usa los modelos que tu organización tiene en Claude Code —el escaneo con Mythos no extiende el acceso a Mythos a otras superficies— y todo parche debe ser revisado y aprobado por una persona.
- **Defender Advantage Fund (0xDAF):** 35 millones en créditos de Claude para organizaciones que ayudan a los mantenedores de código abierto, centrados en parchear vulnerabilidades activas, automatizar el escaneo y el parcheo de forma replicable, y adoptar enfoques resistentes a clases enteras de ataque. Se apoya en 4 millones en donaciones directas y en esfuerzos coordinados como Akrites y Gold Eagle bajo Glasswing. Arranca con un número reducido de subvenciones piloto más grandes.
- **Ampliación del Cyber Verification Program:** los defensores verificados ya obtienen salvaguardas reducidas en Opus y Sonnet. En las próximas semanas, capacidades defensivas como el triaje y la validación de vulnerabilidades se extienden a modelos de clase Mythos, con menos bloqueos en los de clase Opus y Sonnet. El acceso vía Glasswing continúa con socios del Gobierno de EE. UU. para quienes protegen infraestructura crítica y cumplen requisitos estrictos de control de seguridad.

## Recursos incluidos
- `skills/security-scan-triage/SKILL.md` — el flujo habilitar-escanear-triar-parchear, la puerta de aprobación humana y cómo elegir entre las vías de acceso.
- `skills/security-scan-triage/references/access-paths.md` — las cuatro vías en detalle, con el contexto de Glasswing y una tabla de selección.
- `skills/security-scan-triage/templates/finding-triage-report.md` — tabla de triaje por hallazgo y bloque de detalle en torno a CWE, confianza, severidad, verificación, decisión y aprobador.
- `guides/defensive-capability-access.{en,ko,es,ja}.md` — el recorrido completo del anuncio en cuatro idiomas.

## Fuente
[Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenders](https://claude.com/blog/bringing-claude-mythos-5-to-more-defenders) — 21 de agosto de 2026.
