[English](./session-cost-optimization.en.md) · [한국어](./session-cost-optimization.ko.md) · **Español** · [日本語](./session-cost-optimization.ja.md)

# Sacar más partido a cada sesión de Claude Code

Las herramientas de codificación agéntica facturan por token, no por puesto, así que la
misma tarea puede costar cantidades muy distintas según cómo se haya llevado la sesión.
Una sesión lee el archivo de tests y la implementación y arregla el fallo. Otra hace
primero un grep del repositorio, abre una docena de archivos y luego los arrastra todos
—junto con lo que leyó esa mañana— a cada turno restante.

Vale la pena quedarse con el encuadre de su autora, Lydia Hallie: ser eficiente con los
tokens no significa usar menos en total, sino asegurarse de que los que usas van a lo que
realmente pediste.

Dos variables fijan la factura: cuánto cuesta un token y cuántos tokens envía la sesión.

## Parte 1 — Cuánto cuesta un token

### Modelo

Los modelos grandes hacen más trabajo tanto en tokens de entrada como de salida, y su
precio lo refleja. Ajusta el modelo al problema: uno grande para trabajo genuinamente
difícil o ambiguo, uno pequeño para cambios rutinarios.

### Entrada frente a salida

Cada turno tiene dos fases. En el **prellenado**, el modelo lee lo que se le ha dado: el
prompt de sistema, las definiciones de herramientas, `CLAUDE.md`, la conversación hasta
ahora y tu nuevo mensaje. Son tokens de entrada. En la **decodificación**, escribe su
respuesta token a token: tokens de salida, con un precio de aproximadamente 5× el de
entrada.

Los tokens de razonamiento son tokens de salida, así que el nivel de esfuerzo es un dial
directo sobre la mitad cara. Conviene ejecutar `/model` y `/effort` en una sesión nueva y
confirmar ambos: persisten de la sesión anterior, de modo que lo que está en vigor puede
no ser lo que pretendías. Si quieres una sesión sin razonamiento,
`MAX_THINKING_TOKENS=0` baja un escalón por debajo de `/effort low` (no aplica a Fable 5).

### Caché de prompts

La caché es lo que hace asequibles las conversaciones largas. Una lectura de caché cuesta
unas 0,1× el precio de entrada; una escritura hasta 2×, pagada una sola vez por token. Se
escribe una vez y se lee barato en cada turno posterior.

Por eso invalidar la caché es el evento caro:

| Disparador | Efecto |
|---|---|
| `/model` | Otro modelo, otra caché — prellenado completo |
| `/effort` | Forma parte de la clave de caché — prellenado completo |
| Modo rápido | También forma parte de la clave |
| `/compact` | Sustituye la conversación; el prompt de sistema sobrevive |
| Tiempo | Expira tras 1 hora con suscripción, 5 minutos con clave de API (`ENABLE_PROMPT_CACHING_1H=1` la amplía) |
| Reanudar sesión | Suele estar expirada; el prompt de sistema se reconstruye al arrancar |

La excepción que conviene conocer: `/rewind` no cuesta nada. Recorta turnos del final y
deja cacheado todo lo anterior. `/compact`, en cambio, reescribe la conversación y siempre
cuesta algo — por eso el consejo es compactar *antes* de una pausa, mientras todo sigue
caliente, y no después de que la caché haya expirado.

## Parte 2 — Cuántos tokens envía la sesión

Nada se envía una sola vez. Cada archivo leído y cada salida de comando se reenvían en
cada turno durante el resto de la sesión. Cacheados, así que baratos, pero presentes y
ocupando contexto.

### Lo que ya está cargado antes de escribir

Ejecuta `/context` en una sesión nueva y verás la carga permanente: definiciones de
herramientas de cada servidor MCP conectado, el prompt de sistema, `CLAUDE.md`, elementos
de arranque. Todo ello se paga en cada turno.

Dos formas de reducirla. Mantén `CLAUDE.md` específico y traslada las instrucciones de
flujo de trabajo a skills, que se cargan solo cuando se usan. Y desactiva con `/mcp` los
servidores MCP que no estés usando.

### Lo que se añade mientras trabajas

**Archivos.** Cómo preguntas determina cuánto entra. "Los tests fallan" produce un grep y
una ristra de lecturas. Nombrar el archivo da una sola lectura. Mencionarlo con `@` no da
ninguna: Claude Code adjunta el archivo antes de enviar el mensaje. El archivo ocupa el
mismo espacio en ambos casos; lo que ahorras es el viaje de ida y vuelta. Menciónalo una
vez por conversación, ya que volver a mencionarlo adjunta otra copia.

**Salida de comandos.** Se añade igual que un archivo, y se queda. Un ejecutor de tests
verboso puede depositar cientos de líneas que luego se reenvían todo el día. La salida por
encima de unos 30.000 caracteres se escribe a un archivo con una vista previa en línea
(`BASH_MAX_OUTPUT_LENGTH` fija el umbral), lo que cubre el caso extremo pero no la
acumulación constante.

La solución es poner los dos o tres comandos que usas todo el día en `CLAUDE.md`, con sus
flags silenciosos, escritos tal como los teclearías — por ejemplo, ejecutar un único
archivo de tests con `--reporter=dot`. Ahorras el turno dedicado a deducir la invocación y
la salida que si no se quedaría en contexto el resto de la sesión.

### Cuánto tiempo permanece

El turno 40 reenvía los treinta y nueve anteriores. Por eso una sesión larga cuesta más
que el mismo trabajo repartido en varias cortas.

- `/clear` al empezar una tarea nueva. `/rename` antes si podrías querer recuperarla.
- `/compact` cuando una parte del trabajo termina pero necesitas lo que estableció. Di qué
  conservar; si la respuesta es siempre la misma, ponla como sección de instrucciones de
  compactado en `CLAUDE.md`.
- En un modelo de 1M de contexto, `/autocompact 200k` restaura la red de seguridad de
  compactado automático (Claude Code v2.1.221+).

Una trampa: `/loop` se dispara como un turno completo dentro de la sesión que lo inició,
arrastrando toda la conversación cada vez — y si pasa más de una hora entre disparos, cada
uno falla además la caché. Arranca los bucles en una sesión nueva, en otra terminal.

### Subagentes

Un subagente tiene su propio contexto — prompt de sistema, herramientas, `CLAUDE.md` —
pero no tu conversación. Consume sus propios turnos y solo vuelve su respuesta. Todo lo
demás se descarta.

El intercambio es real en ambos sentidos: puede releer material que tu sesión principal ya
tiene, y paga sus propios turnos. Compensa cuando un trabajo genera mucha salida que no
necesitas conservar, siendo el análisis de logs el caso más claro: recibes el informe, no
el log. Para un trabajo ruidoso que delegas a menudo, define el subagente con un modelo más
pequeño fijado en su configuración; si no, se ejecuta con el modelo de la sesión principal.

## Por dónde empezar

Aproximadamente por impacto:

1. **Duración de la sesión** — cuánta conversación se reenvía en cada turno.
2. **Tamaño de la salida de comandos** — cuánto ruido se acumula en ella.
3. **Archivos leídos** — con qué precisión señalas lo que necesitas.
4. **Modelo y esfuerzo** — fijados a propósito al principio y no cambiados a mitad.

Los dos primeros suelen importar más que el último.

## Artefactos incluidos

- La skill `token-efficient-sessions` de esta carpeta — el mismo material como skill
  accionable, con referencias de precios y de ciclo de vida del contexto, fragmentos de
  `CLAUDE.md` y patrones de sesión de antes y después.

## Fuente

- https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions (14 de agosto de 2026)
