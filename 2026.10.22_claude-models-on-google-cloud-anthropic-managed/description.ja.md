[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
Claude Models on Google Cloud (Anthropic managed) の一般提供開始を伝える発表です（2026年10月22日）。
Google Cloud のお客様は、Google Cloud の IAM・請求・コミットメント消化をそのまま使いながら、Claude
Platform の全機能を利用できます。Google managed の提供形態も引き続き利用できます。

## どんなときに役立つか
- Google Cloud のお客様が Anthropic managed と Google managed のどちらかを選ぶとき。
- Google Cloud を離れずに、Claude の新機能やベータをリリース当日から使いたいとき。
- オンボーディング前に請求・IAM・割引の扱いを計画するとき。

## 主なポイント
- Anthropic managed：Claude API の全機能を提供し、新機能とベータはネイティブの Claude Platform と同日に
  提供されます。サービスの運用とデータ処理者は Anthropic です。
- 既存の Google Cloud IAM 認証情報で動作し、Google Cloud の請求書1通にまとめられ、Google Cloud の
  コミットメントを消化します。現在は US と Global エンドポイントに対応。
- 含まれる機能：Managed Agents（ベータ）、コード実行、コンピュータ使用、エージェントスキル、アドバイザー
  戦略（ベータ）、Files API、引用、ウェブ検索とウェブフェッチ、MCP コネクタ（ベータ）、プロンプト
  キャッシュ、バッチ処理。
- Claude Opus 5.5 の Fast Mode もここで一般提供。出力生成が最大 2.5 倍高速、入力／出力 100 万トークン
  あたり $8 / $40。
- Claude Console でプロンプト作成、エージェントの構成とホスト環境での実行、使用量・コストの監視、
  ワークスペース単位のアクセス管理が可能。モデル：Fable 5.1、Opus 5.5、Sonnet 5.5、Haiku 5.5。
- Google をデータ処理者にする必要がある、厳格な地域データレジデンシーがある、Model Armor や Agent Engine
  などのネイティブ統合が必要、という場合は Google managed が引き続き適しています。
- 既存の割引がある場合は、開始前にアカウントエグゼクティブへ連絡してください。割引は遡って適用されません。

## 同梱リソース
- スキル：`google-cloud-offering-selector`（`references/feature-matrix.md`、
  `templates/offering-decision.md`）。

## 出典
- https://claude.com/resources/articles/claude-models-on-google-cloud-anthropic-managed
