[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
この記事は、Claude Developer Platform の **structured outputs（構造化出力）** を発表する内容です。API 応答が、指定した JSON スキーマまたは tool 定義に必ず一致することを保証できます。

## どんなときに役立つか
本番アプリやエージェントが、信頼できる構造化データに依存している場合に有用です（例: データ抽出、マルチエージェント間通信、複数の制約フィールドを正確に満たす必要がある検索ツール）。

## 主なポイント
- 構造化出力により、定義済みの構造（スキーマまたは tool 仕様）への準拠が保証され、パースエラーや tool 呼び出し失敗を減らせます。
- モデル性能への影響なしに、本番での信頼性を高める機能として説明されています。
- データ抽出、マルチエージェントアーキテクチャ、複雑な検索ツールなどの用途が挙げられています。

## 同梱リソース
- Skill バンドル: `skills/structured-outputs-reliability-guide/`（信頼性チェックリスト + 参照リンク）

## 出典
- https://claude.com/blog/structured-outputs-on-the-claude-developer-platform
