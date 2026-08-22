[English](./admin-analytics-and-cost-controls.en.md) · [한국어](./admin-analytics-and-cost-controls.ko.md) · **Español** · [日本語](./admin-analytics-and-cost-controls.ja.md)

# Analítica de administración y controles de coste para Claude Enterprise

Anthropic introdujo una analítica de administración más rica, entitlements a nivel de modelo y
alertas de gasto para Claude Enterprise. El razonamiento se expone con claridad: **a medida que
Claude asume trabajo agéntico cada vez más difícil y complejo en toda la organización, los patrones
de uso y coste dejan de parecerse a los de una herramienta de chat estándar.** Estos controles dan a
los administradores la visibilidad para entender cómo se usa Claude y las herramientas para
gestionar los costes.

Estas incorporaciones se apoyan en controles que Anthropic ya ofrecía: topes de gasto en todos los
niveles, control de acceso y enrutamiento de modelos, un panel de analítica de uso con exportaciones
y una Analytics API, y controles de esfuerzo (effort). La analítica más rica y los controles de
coste más granulares son las adiciones más recientes a una superficie de control construida durante
meses.

## Seguir la adopción y el coste

### El panel de analítica

El panel de analítica para administradores ahora muestra **uso y coste por grupo y por usuario**,
con el resultado producido —artefactos creados, archivos editados, skills y conectores usados—
mostrado directamente junto a su coste. Los administradores pueden filtrar por los **grupos SCIM que
su equipo de IT ya gestiona**, de modo que el desglose sigue el organigrama existente.

### Insights de Claude Code

Claude Code gana insights más ricos mediante dos nuevas pestañas en la consola de administración,
centradas en valor y uso.

**Uso** muestra desarrolladores activos, número de sesiones y los comandos más usados en toda la
organización, y se actualiza a diario.

**Valor** resume los datos de uso y coste para ayudar a los administradores a entender de un vistazo
el valor de Claude Code, estimando el aumento de productividad, el coste por commit y el valor
anual. Todas las fórmulas son visibles en la pestaña y sus entradas son ajustables.

### Chat de analítica

El chat de analítica ahora puede responder un conjunto de preguntas mucho más amplio y producir
artefactos más ricos para profundizar. Los administradores preguntan en lenguaje natural —"¿Qué
equipos duplicaron su uso de Claude este mes?" o "¿Dónde estamos obteniendo más valor por
licencia?"— y Claude devuelve gráficos que pueden exportarse y compartirse con las partes
interesadas.

### La Analytics API

Los datos de uso y coste están disponibles de forma programática a través de la Analytics API, para
que finanzas e IT puedan llevarlos a las herramientas que ya utilizan —como **Datadog Cloud Cost
Management** y **CloudZero**— y verlos junto al resto de su gasto en nube e IA. Los resultados
pueden filtrarse por **rango de fechas, equipo, producto o modelo**. **Las skills reportan su propio
uso y coste**, y nuevos endpoints rastrean la **adopción de plugins** y la **creación de
artefactos**.

### Visibilidad a nivel de usuario

Los administradores pueden extender la visibilidad de uso a usuarios individuales —coste, desglose
por producto y modelo, y progreso frente a los límites de gasto— para que nadie se encuentre con un
corte inesperado. Los usuarios también pueden ver sus propias tendencias de uso a lo largo del
tiempo, incluidos qué productos, modelos y skills usan más, y cómo esa actividad se acumula en
gasto.

## Controles para gestionar el gasto

**Los valores por defecto y los entitlements de modelo** permiten a los administradores fijar con qué
modelo de Claude arrancan las conversaciones nuevas en chat, Cowork y Claude Code, para que el
trabajo rutinario no vaya necesariamente por defecto a la opción más cara. Los administradores
controlan qué modelos están disponibles para roles concretos o para toda la organización.

**Las alertas de umbral de gasto** notifican a los administradores al **75%** y al **90%** de un
límite de gasto a nivel de organización, dándoles tiempo para subir el tope antes de que alguien
quede bloqueado a mitad de una tarea. Los usuarios reciben notificaciones in-app al **75%** y al
**95%**, y pueden solicitar un aumento de límite directamente a su administrador sin salir de
Claude.

**La Admin API** traslada los flujos de control de coste a scripts para organizaciones que gestionan
límites en muchos grupos, de modo que los controles escalen con la organización. Permite automatizar
la revisión de solicitudes de aumento, identificar a los miembros próximos a su límite de gasto y
señalar cambios rápidos de uso, todo a escala.

## Lo que dicen quienes lo usan

> "La visibilidad de costes no es un ejercicio de una vez al mes. Los datos de gasto granulares y las
> alertas dan a los equipos avisos periódicos para reevaluar cómo están usando Claude, en lugar de
> una sorpresa al final del ciclo de facturación."
>
> — Kyra Abbu, Product Manager

> "No voy a frenar a la gente que está impulsando nuestro mejor trimestre. Él pide ROI. Hemos
> vinculado Claude, conectado a nuestros servidores MCP empresariales, a un aumento de ingresos del
> 4%."
>
> — Carter Busse, CIO

> "El uso de tokens por sí solo no dice gran cosa. Lo que de verdad quiero ver es qué skills se
> ejecutan una y otra vez en toda la organización: esa es la señal real de valor."
>
> — Ciro Yamada, Product Director

## Cómo empezar

Para administradores que gestionan Claude en su organización: explorar los desgloses de uso y coste
en la consola de administración, fijar valores por defecto de modelo y límites de gasto por grupo, y
configurar alertas de umbral de gasto para anticiparse a los sobrecostes. Los datos de uso están
disponibles en el panel de administración, y la Analytics API permite a finanzas e IT llevar esas
mismas métricas a los sistemas de reporting existentes.

## Fuente

["Giving admins more visibility and control over Claude spend"](https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend)
— Anthropic, 2 de julio de 2026.
