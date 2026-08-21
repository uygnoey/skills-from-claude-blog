[English](./defensive-capability-access.en.md) · [한국어](./defensive-capability-access.ko.md) · **Español** · [日本語](./defensive-capability-access.ja.md)

# Llevar la capacidad de ciberdefensa de frontera a más defensores

Claude Mythos 5 ya está disponible en Claude Security y llegará pronto a las herramientas de
ciberdefensa de los socios. Junto a ello, un fondo de 35 millones de dólares para la seguridad del
software de código abierto y una ampliación del Cyber Verification Program.

## El problema que resuelve este diseño

En abril, Project Glasswing puso Claude Mythos Preview —y su sucesor, Claude Mythos 5— en manos de
un pequeño grupo de organizaciones que protegen el software más crítico del mundo. La clave era el
tiempo: dar a los defensores una ventana para encontrar y corregir vulnerabilidades antes de que
modelos con capacidades similares estuvieran disponibles de forma general o llegaran a actores
maliciosos.

Ampliar esa ventana a más defensores requiere clasificadores de seguridad y salvaguardas que
permitan que la capacidad de clase Mythos llegue a los defensores sin poner sus capacidades
cibernéticas ofensivas en las manos equivocadas. Claude Fable 5 fue el primer paso: ampliamente
disponible, con el trabajo cibernético de doble uso bloqueado.

El siguiente paso parte de una distinción sobre la forma de la interacción:

> El comportamiento más arriesgado se da cuando una persona tiene acceso directo a un modelo, donde
> un actor malicioso puede intentar dirigirlo hacia usos dañinos. Pero si los usuarios solo pueden
> recibir salidas específicas, como un parche para una vulnerabilidad o una alerta de seguridad, ese
> riesgo es mucho menor.

Todas las vías de acceso que siguen amplían el acceso de los defensores a los *resultados*
defensivos, manteniendo las barreras alrededor del acceso directo al modelo.

## 1. Mythos dentro de las herramientas que los defensores ya usan

Los equipos que defienden hospitales, servicios públicos, sistemas financieros y la cadena de
suministro de software ya dependen de un conjunto de productos y servicios para operaciones de
seguridad, respuesta a incidentes, inteligencia de amenazas e ingeniería de detección. La vía más
rápida para poner capacidad de frontera a su alcance es integrar modelos de clase Mythos en esas
herramientas.

Muchos socios ya han construido productos de ciberseguridad sobre Claude Opus que ayudan a los
equipos a triar alertas, identificar amenazas y remediar vulnerabilidades más rápido. Anthropic
trabaja ahora con estos socios y con más para integrar Claude Mythos 5 en sus productos y
servicios, de modo que puedan ofrecer resultados defensivos de nivel Mythos a sus clientes.

**La forma de la interacción importa.** Quien usa uno de estos productos no interactúa con Mythos
directamente. Trabaja a través de una interfaz de propósito específico que ejecuta Mythos en segundo
plano para una tarea definida, y recibe únicamente el artefacto concreto que el producto está
pensado para entregar. Una herramienta de remediación de vulnerabilidades podría devolver una lista
de parches sugeridos —generados por Mythos, sin que el usuario tenga forma de pedirle al modelo que
desarrolle un exploit—. Anthropic y sus socios mantienen además medidas de prevención de abuso para
verificar que el modelo se mantiene dentro del alcance previsto.

Este trabajo es incipiente y se espera que se amplíe. Quienes construyen productos y servicios de
seguridad pueden registrar su interés.

## 2. Escaneos de Claude Security con Claude Mythos 5

Claude Security escanea bases de código en busca de vulnerabilidades y sugiere parches para
revisión humana. Está en beta pública para clientes de Claude Enterprise, y los escaneos con
Mythos 5 se facturan como uso estándar de tokens dentro de tu plan actual, sin complemento aparte.

El flujo:

1. **Habilitar.** Un administrador de la empresa activa Claude Security en la admin console.
2. **Escanear.** Desde `claude.ai/security`, selecciona un repositorio para escanear con Claude
   Mythos 5.
3. **Leer los hallazgos.** Cada uno llega con una categoría CWE (Common Weakness Enumeration),
   valoraciones de confianza y severidad, y una corrección sugerida.
4. **Parchear.** Abre Claude Code en la web para implementar la corrección. El parcheo interactivo
   usa los modelos a los que tu organización tiene acceso en Claude Code: el escaneo con Mythos no
   extiende el acceso a Mythos a otras superficies.
5. **Aprobar.** Todo parche debe ser revisado y aprobado por una persona antes de implementarse.

Claude Security usa Mythos 5 para escanear código de tu propiedad y devuelve hallazgos detallados en
lugar de salidas en bruto, sin exponer el modelo. Los defensores acceden a las capacidades de Claude
Mythos 5 sin que el modelo quede accesible para quienes podrían usarlo indebidamente.

## 3. El Defender Advantage Fund (0xDAF)

Algunos de los programas más usados del mundo funcionan sobre software de código abierto. Sin
embargo, esos proyectos suelen estar mantenidos por voluntarios o fundaciones sin ánimo de lucro,
que pueden carecer de los recursos o el personal para defenderlos de forma integral.

A través de Project Glasswing, Anthropic donó 4 millones de dólares directamente a organizaciones de
seguridad de código abierto, aportó créditos a las fundaciones de seguridad de código abierto del
programa, ayudó a escanear y parchear proyectos muy usados y apoyó esfuerzos coordinados de
corrección de vulnerabilidades como Akrites y Gold Eagle.

El Defender Advantage Fund se apoya en ese trabajo con **35 millones de dólares en créditos de
Claude** para organizaciones que ayudan a los mantenedores de código abierto a asegurar su software.
Las subvenciones se centran en tres áreas:

- parchear vulnerabilidades activas en proyectos muy utilizados;
- automatizar el escaneo y el parcheo de formas que otros proyectos puedan replicar;
- ayudar a los proyectos a adoptar enfoques de seguridad más ambiciosos que los hagan resistentes a
  clases enteras de ataque.

El fondo arranca con un número reducido de subvenciones piloto más grandes, para aprender qué
funciona y qué escala mejor. Los primeros receptores se anunciarán más adelante.

## 4. Ampliación del Cyber Verification Program

El Cyber Verification Program da a las organizaciones acceso a capacidades de doble uso en los
modelos Claude Opus y Sonnet. Los equipos aceptados experimentan salvaguardas reducidas, lo que
minimiza las interrupciones en trabajo legítimo de ciberseguridad sobre sistemas que están
autorizados a proteger.

En las próximas semanas el programa evolucionará para ampliar el acceso con salvaguardas a Claude
Mythos: el acceso a capacidades defensivas como el triaje y la validación de vulnerabilidades se
extenderá a modelos de clase Mythos, y los defensores verán menos bloqueos en modelos de clase Opus
y Sonnet.

En paralelo, el acceso a Claude Mythos sigue ampliándose mediante Project Glasswing en colaboración
con socios del Gobierno de EE. UU., centrado en quienes protegen infraestructura crítica y cumplen
requisitos estrictos de control de seguridad.

Se anima a los equipos de seguridad que realizan trabajo legítimo a solicitar ya el programa para
obtener salvaguardas reducidas en Opus y Sonnet. Los equipos ya inscritos y aceptados no necesitan
hacer nada.

## Qué vía te corresponde

| Situación | Vía |
|---|---|
| Eres dueño de la base de código y estás en Claude Enterprise | Escaneo de Claude Security |
| Construyes productos o servicios de seguridad para otros defensores | Integración de socios — registrar interés |
| Ayudas a mantenedores de código abierto y necesitas recursos | Defender Advantage Fund |
| Necesitas salvaguardas reducidas sobre el uso directo del modelo para trabajo defensivo autorizado | Cyber Verification Program |

## Qué viene después

Estas iniciativas continúan el esfuerzo por poner las capacidades defensivas de los modelos de
frontera al alcance de más personas y organizaciones, y por apoyar a la comunidad de código abierto
en el endurecimiento de sus proyectos. La dirección declarada es seguir trabajando con socios
gubernamentales, organizaciones, mantenedores de código abierto y la industria en general para
construir la infraestructura cibernética resiliente que exigen los modelos de IA altamente capaces
de hoy.

## Fuente

[Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenders](https://claude.com/blog/bringing-claude-mythos-5-to-more-defenders)
— 21 de agosto de 2026.
