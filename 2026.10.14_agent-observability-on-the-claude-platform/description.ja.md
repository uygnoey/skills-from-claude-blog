[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
Claude Platform で、Claude Managed Agents、Messages API、Claude SDK から OpenTelemetry（OTel）トレースを
送信できるようになったという発表です。任意の OTel ツールでエージェントの各ステップを追跡できます。

## どんなときに役立つか
- Claude Platform で構築したエージェントをステップ単位で可視化したいとき。
- 遅い・失敗したエージェントのステップを、他のスタックと並べてデバッグするとき。
- 本番トレースを eval に変換したり、チームごとのトークン使用量を追跡したりするとき。

## 主なポイント
- エージェントの各ターン、モデル呼び出し、ツール使用（MCP サーバー呼び出しを含む）が、レイテンシー・
  トークン・ID を含む標準の OTel トレースとして届きます。
- トレースは OpenTelemetry GenAI セマンティック規約に従うため、Claude と他のプロバイダーのデータを同じ
  ツールやダッシュボードで扱えます。Claude Code や Cowork のトレースと同じ場所に集約できます。
- 信頼は証拠とともに育ちます。エージェントのトレースを確認し、信頼性が示されたら権限を広げます。
- 挙げられたツール：Grafana Cloud、Honeycomb、Sentry、Splunk（デバッグ）／Arize AI、Braintrust、Datadog、
  Langfuse、LangSmith、New Relic、PostHog（eval・品質）／Databricks Unity Gateway（組織全体の使用量）。
  OTLP 互換ツールならどれでも利用可能。
- パブリックベータ。Managed Agents と Messages API は Claude Console で送信先を追加する必要があり、
  SDK は自動でエクスポートします。
- Foxglove、Ramp（Reflect により一部のエージェントでトークン使用量を 10–20% 削減、セッションを 30% 高速化）、
  Sterling Labs、会計エージェントチームの顧客コメント。

## 同梱リソース
- Skill：`agent-otel-tracing` — エクスポートの有効化、送信先の選択、段階的な権限拡大、改善ループ
  （`references/observability-tools.md`、`examples/customer-patterns.md`）。

## 出典
- https://claude.com/resources/articles/agent-observability-on-the-claude-platform
