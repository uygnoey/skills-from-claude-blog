[English](./claude-platform-on-aws-vs-bedrock.en.md) · [한국어](./claude-platform-on-aws-vs-bedrock.ko.md) · **Español** · [日本語](./claude-platform-on-aws-vs-bedrock.ja.md)

# Claude Platform on AWS vs Claude on Amazon Bedrock

## Qué cubre esta guía

Una guía breve para decidir entre:

- **Claude Platform on AWS** (plataforma operada por Anthropic a la que se accede mediante puntos de entrada de AWS)
- **Claude on Amazon Bedrock** (servicio gestionado por AWS dentro del perímetro de AWS)

## Lista de decisión

### Elegir Claude Platform on AWS cuando

- Quieres la experiencia nativa de Claude Platform a través de IAM, facturación y CloudTrail de AWS.
- Tus requisitos permiten que los datos del cliente sean procesados por Anthropic fuera del perímetro de AWS.

### Elegir Claude on Amazon Bedrock cuando

- Necesitas que los datos permanezcan dentro de la infraestructura de AWS.
- Prefieres funciones gestionadas por AWS y una selección más amplia de modelos dentro de un único servicio.

## Fuente

- https://claude.com/blog/claude-platform-on-aws
