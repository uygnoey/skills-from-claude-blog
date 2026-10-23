[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
Anthropic のセールス開発リーダー Carl Johnson によるケーススタディ(2026年9月30日)です。Claude Managed
Agents(ベータ)上に構築した購入エージェントが、今ではインバウンド顧客の大半に対応し、「自社に Claude を
導入したい」から購入完了まで導いていること、そしてそれがセールスチームの仕事をどう変えたかを紹介します。

## どんなときに役立つか
- インバウンド需要がフォーム → BDR → AE のプロセスを超え、購入者が簡単な回答を何日も待っているとき。
- 複雑な案件は担当者に引き継ぎつつ、常時利用できるセルフサービスの購入体験を設計するとき。
- 顧客向けセールスエージェントのプロンプトを書き、改善を重ねるとき。

## 主なポイント
- 従来: 月に数万件のインバウンド。担当者はドキュメントに既にある質問への回答に時間を費やしていた。
- エージェントは Contact Sales・Pricing ページ、製品内、メールに配置され、利用は顧客が選ぶオプトイン方式。
- 会話は「購入」「全文脈付きで担当者へ引き継ぎ」「簡単な回答」のいずれかで終わる。
- 構成: プロンプト、少数のツール、Managed Agents 上の Claude(ホスティング・セッション・ツール連携はプラットフォームが担当)。
- Managed Agents を選んだ理由: エンジニア1人が数週間で構築、セールス・コンテンツ担当が Console でステージング
  エージェントを使いプロンプトを直接編集、すべての変更をバージョンとして保存(社内テスト約1週間で v7)。
- 教訓: ルールではなく目標を与える、少ないほど良い、SME を開発ループに入れる、顧客に合ったプランを勧める
  (例: Enterprise ではなく Team)、すべてのエスカレーション理由をフィードバックとして扱う(人の対応が必要な割合は約半分に)。
- 成果: 1日数千件の会話。エスカレーションされたリードの商談化率は従来フォームの2倍以上、成約は約5日短縮。
  ある担当者は1件あたりのメールが約10通から約6通に減り、成約件数が2.5倍に。

## 同梱リソース
- スキル: `inbound-buying-agent-design`(`references/conversation-outcomes.md`、
  `references/lessons-and-results.md`、`templates/goal-first-system-prompt.md`、
  `templates/escalation-feedback-log.md`)。

## 出典
- https://claude.com/resources/articles/how-anthropics-sales-team-rebuilt-inbound-with-claude-managed-agents
