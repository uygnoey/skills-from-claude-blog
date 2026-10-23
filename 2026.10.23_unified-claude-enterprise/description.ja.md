[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
2026年10月23日の発表です。9月にPro・Maxプラン向けに提供されたチャットとCoworkの統合体験が、Claude
Enterpriseでも一般提供（GA）になりました。ユーザーが得られるもの、セキュリティの仕組み、管理者による
コスト管理、始め方を説明しています。

## どんなときに役立つか
- Enterprise管理者として統合体験の有効化を計画するとき。
- 展開前に、セキュリティや財務の担当者がクラウドセッション、データの扱い、支出について確認したいとき。

## 主なポイント
- Web・デスクトップ・モバイルで一つのClaude。会話はチャットから始まり、コードやファイル作業が必要な
  タスクはクラウドで続行され、完成したドキュメント・分析・資料として返ってきます。ノートPCを閉じても
  作業は続きます。チャット、プロジェクト、コネクタ、スキル、プラグインは引き継がれます。
- セキュリティ: SSOとCompliance APIを基盤とし、転送時・保存時に暗号化、デフォルトで学習に使わない、
  クラウドセッションごとに分離されたVM、ネットワークのegressはデフォルトでオフ、コネクタの認証情報は
  サンドボックス外に保管、セキュリティチーム向けの一元的な可視性。
- コスト: 従量課金。Opus 5.5は一般的なワークロードでOpus 5より40%安く、Sonnet 5.5はSonnet 5より最大30%
  安い。管理者の制御: 効率モード、モデル権限、支出上限（組織/グループ/メンバー）、グループ共有予算。
- 展開はOrganization settingsで管理します。Claude Codeのゼロデータ保持、HIPAA対応構成、顧客管理の
  暗号鍵を使う組織は現在の構成のままです。

## 同梱リソース
- スキル: `enterprise-unified-rollout`（`references/security-posture.md`、`references/cost-controls.md`、
  `templates/rollout-checklist.md`）。

## 出典
- https://claude.com/resources/articles/unified-claude-enterprise
