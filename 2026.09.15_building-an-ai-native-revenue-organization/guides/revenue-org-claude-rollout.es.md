[English](./revenue-org-claude-rollout.en.md) · [한국어](./revenue-org-claude-rollout.ko.md) · **Español** · [日本語](./revenue-org-claude-rollout.ja.md)

# Desplegar Claude en toda una organización de ingresos

Resumen de la guía de Anthropic para líderes de ingresos. Para la referencia detallada y una
plantilla de plan, consulta el skill `revenue-org-ai-rollout` de esta carpeta.

## 1. Por qué importa todo el equipo
Un vendedor ahorra tiempo en la preparación de llamadas, pero los beneficios se multiplican cuando
lo adopta todo el equipo. El camino va de las ganancias individuales, pasando por flujos de equipo y
de departamento, hasta resultados en KPI u OKR. El retorno crece con el acceso y la confianza que se
le da a Claude.

## 2. Decisiones antes del piloto
- **Responsable:** RevOps, porque gestiona el CRM y los informes de pipeline y previsión.
- **Sistemas:** conecta el CRM, la grabación de llamadas, el correo y Slack para que nadie mueva
  archivos a mano.
- **TI:** nombra un responsable de TI para el aprovisionamiento, el SSO y los consentimientos de
  administrador; fija fechas primero.
- **Seguridad:** empieza pronto — límites de datos, modelo de permisos de conectores, auditabilidad,
  exportación de telemetría.
- **Métricas:** una de actividad y una de ingresos, con línea base y fechas de revisión.
- **Gasto:** límites por organización, grupo y usuario; funciones más costosas restringidas por rol;
  más margen para los champions.
- **Cohorte:** dos o tres equipos con líderes motivados.

## 3. Configuración del equipo
El plugin de Ventas ofrece `/call-summary`, `/forecast`, `/pipeline-review` y skills de investigación
de cuentas, preparación de llamadas, informe diario, borradores de prospección, inteligencia
competitiva y creación de materiales. Precarga su archivo de configuración. Los conectores respetan
los permisos de cada vendedor. Las rutinas de los mejores se convierten en skills compartidos; editar
el archivo los actualiza para todos.

## 4. Tres fases
1. **Preparación** — TI y RevOps en paralelo; champions: 2-3 por departamento o 1 por cada 25-50 usuarios.
2. **Piloto** — 2-3 casos de uso por equipo; los champions hacen demos, horas de consulta y los
   primeros skills.
3. **Escala** — paquete de skills compartido; oleadas como 25 → 150 → todos; resultados de Claude en
   las reuniones habituales.

## 5. Medir el ROI
Compara equipos piloto y no piloto en el mismo trimestre (pipeline por vendedor, duración del ciclo,
tasa de cierre). Agrupa los retornos en eficiencia, expansión y nuevas capacidades. En las
conversaciones de presupuesto, empieza por expansión y nuevas capacidades, no por horas ahorradas.
Lee el gasto junto al resultado; capacita antes de recortar límites.

## 6. Errores comunes
- Piloto sin fecha de fin → agenda la fecha de decisión y a quien decide en el calendario del patrocinador.
- Más licencias sin más champions → mantén 1 champion por cada 25-50 usuarios en cada oleada.
- Ignorar el gasto hasta la factura → fija límites pronto y revisa el uso cada semana.

Fuente: https://claude.com/resources/articles/building-an-ai-native-revenue-organization
