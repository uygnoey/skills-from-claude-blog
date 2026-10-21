[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Un caso de cliente sobre cómo los equipos de seguridad de Comcast y Booz Allen usaron Claude Mythos
Preview, a través de Project Glasswing (el programa de acceso limitado de Anthropic para defensores
de infraestructura crítica), para encontrar, validar y corregir vulnerabilidades que los escáneres
existentes no detectaban, en especial cadenas de explotación, donde pequeñas debilidades se combinan
en una ruta de ataque grave.

## ¿Cuándo es útil?
- Cuando un equipo de seguridad planifica una revisión asistida por modelos sobre un gran portafolio.
- Cuando los hallazgos superan la capacidad del equipo para validarlos y asignarlos.
- Cuando se buscan fallos entre componentes o entre lenguajes que los escáneres de bugs aislados no ven.

## Puntos clave
- Comcast evaluó 258 sistemas críticos para el negocio (~170 millones de líneas de código). El modelo
  encontró una vulnerabilidad crítica de autenticación en una plataforma pública, surgida de varios
  componentes que por separado parecían correctos. Los ingenieros la validaron contra la aplicación
  en ejecución, rastrearon la causa raíz, la corrigieron y verificaron que no había sido explotada.
- Noopur Davis, CISO de Comcast: el cuello de botella ahora es validar el volumen de hallazgos, no
  descubrirlos.
- Booz Allen halló un fallo de firmware en el arranque: una clave de seguridad sin proteger permitía
  sustituirla por la del atacante y suprimir el bloqueo o borrado del dispositivo. El modelo lo
  rastreó a través de dos programas en dos lenguajes y ayudó a redactar correcciones y evidencias
  para los responsables de los sistemas.
- Los equipos siguen validando hallazgos, deduplicando patrones sistémicos y asignándolos a sus
  responsables. Un analista de Booz Allen completó en doce días una revisión que habría llevado meses
  a un equipo mayor.
- Las decisiones las toman personas; Anthropic ampliará el acceso mediante su Cyber Verification
  Program (CVP).

## Recursos incluidos
- Skill: `exploit-chain-validation` — flujo posterior al descubrimiento (validar, causa raíz,
  comprobar explotación, corregir, deduplicar, asignar) con una plantilla de paquete de evidencias.

## Fuente
- https://claude.com/resources/articles/how-comcast-booz-allen-use-claude-mythos-to-secure-their-codebases
