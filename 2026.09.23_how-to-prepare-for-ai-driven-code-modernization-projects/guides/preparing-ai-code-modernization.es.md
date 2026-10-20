[English](./preparing-ai-code-modernization.en.md) · [한국어](./preparing-ai-code-modernization.ko.md) · **Español** · [日本語](./preparing-ai-code-modernization.ja.md)

# Preparar una modernización de código impulsada por IA

Una metodología de los ingenieros de despliegue avanzado (forward deployed engineers) de Anthropic,
de la serie Notes from the Field, para ejecutar grandes modernizaciones de sistemas críticos en
empresas reguladas.

## Por qué la preparación es el trabajo real

Modernizaciones que antes se planificaban como esfuerzos de varios años con toda la plantilla ahora
pueden terminar en meses o semanas. Pero la gestión de cambios, la revisión y la aprobación —los
procesos que hacen fiables los sistemas críticos— asumen que una persona escribe cada cambio y otra
revisa cada diff. Cuando los agentes escriben los cambios, el cuello de botella pasa de producirlos
a movilizar a la organización en torno a ellos.

## Los seis pasos

| # | Paso | Resultado |
|---|---|---|
| 1 | Definir el objetivo | Stack tecnológico y comportamiento que debe tener el código modernizado |
| 2 | Crear el certificado | Condiciones que un cambio debe cumplir para considerarse correcto |
| 3 | Fijar la política de promoción | La vía por la que los cambios certificados llegan a producción al ritmo en que se producen |
| 4 | Preparar los requisitos previos | Entorno, CI/CD, capacidad de revisión, aprobaciones |
| 5 | Construir y refinar el flujo agéntico | Un flujo dinámico de Claude Code con subagentes en paralelo |
| 6 | Ejecutar la modernización | Prueba de extremo a extremo en una partición pequeña y luego escalar |

### 1. Definir el objetivo
Elige **uplift** (subida de versión en el mismo stack), **transform** (reescritura entre stacks con
comportamiento fijo) o **reimagine** (reconstrucción desde cero con comportamiento modificado y una
especificación de comportamiento escrita). Quienes operan producción suelen preferir transform; los
ingenieros veteranos y las áreas de negocio suelen empujar hacia reimagine. Resuélvelo pronto o
volverá como discusiones sobre si cada cambio es "correcto". Mapea el código (los comandos `assess`,
`map` y `extract-rules` del plugin de modernización de código ayudan), complementa con entrevistas y
documentación, y fija la justificación de negocio: normalmente **reducir el riesgo**, no el coste.

### 2. Crear el certificado
Conjunto de condiciones que todo cambio debe superar, cada una verificable sin intervención humana:
tests originales y escritos por Claude, umbrales de cobertura, límites de rendimiento, revisiones
adversariales de Claude en contextos nuevos, comprobaciones de UI con computer use, paridad de
entrada/salida, ida y vuelta de estado y formatos de transmisión, periodo en staging, análisis
estático y escaneos de seguridad, compilaciones limpias. Uplift se apoya en la suite original;
transform en replay de tráfico, pruebas diferenciales y despliegue en paralelo a producción;
reimagine en la especificación. Escríbelo con los revisores; si falta evidencia, que Claude la construya.

### 3. Fijar la política de promoción
Escalona la profundidad de revisión según radio de impacto y confianza del agente; mantén revisión
humana completa en las rutas críticas. Corrige en el origen las alertas recurrentes. Diseña con los
revisores el formato de salida. Dirige el escaso tiempo de los expertos (SME) a los niveles de mayor
riesgo. Decide dónde te sitúas entre velocidad y profundidad, y que la dirección emita la política de
antemano para que la responsabilidad de un fallo en producción sea compartida.

### 4. Requisitos previos
Host remoto y capacidad de pruebas; telemetría, entorno paralelo a producción o datos de replay; un
mapa de dependencias fundamentado; verificaciones de compatibilidad en CI/CD; planes de congelación de
código y de comunicación; tiempo de revisión de los equipos dependientes; una vía de acceso al modelo
aprobada, mínimo privilegio, secretos y datos personales enmascarados, trazabilidad de cada PR a su
transcripción y evidencia, y comprobaciones de licencias y vulnerabilidades. Empieza pronto: los otros
equipos tienen su propio backlog.

### 5. Construir y refinar el flujo
Parte del plugin de modernización de código. Coloca objetivo, certificado, política, código,
documentación y herramientas en el sistema de archivos o vía MCP como base de conocimiento. Pruébalo
en piezas pequeñas con revisión de expertos. Cuando surjan problemas, corrige el flujo, no cada cambio.

### 6. Ejecutar
Lleva una partición pequeña de extremo a extremo a través de la política de promoción, itera mientras
sea barato y luego escala. En un uplift se puede modernizar in situ: particionar desde las hojas hacia
dentro, congelar una partición a la vez y bloquear en CI/CD que nuevos commits deshagan las ya
modernizadas.

## Coste
Factores: volumen de lectura frente a cambio, complejidad del certificado (la verificación suele
dominar en entornos regulados), escritura y reparación de tests y reconciliación con merges
concurrentes. Mide tokens en el piloto y extrapola un coste mínimo; trata como incógnita lo que el
piloto no vio. Pon las comprobaciones caras tras filtros baratos, usa modelos como Sonnet para el
trabajo mecánico, reserva modelos más potentes para transformaciones difíciles y revisión adversarial,
y vigila las tasas de reintento al escalar de modelo.

## Más allá de la modernización
Además del código, obtienes un flujo reutilizable, un certificado escrito, una política de promoción
aceptada y un rastro de evidencias. Codifícalos como playbook para la próxima actualización.

## Fuente
- https://claude.com/resources/articles/how-to-prepare-for-ai-driven-code-modernization-projects
