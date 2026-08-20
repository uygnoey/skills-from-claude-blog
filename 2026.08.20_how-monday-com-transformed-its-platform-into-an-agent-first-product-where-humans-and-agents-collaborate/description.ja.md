[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
25万社以上が利用する業務管理プラットフォーム monday.com が、人が更新しなければならないツールから、人とエージェントが同じアイテムの上で一緒に働く agent-first（エージェント優先）の製品へと自らを作り直した顧客事例。作り直された体験は 2026年5月にローンチし、2か月でエージェントとのやり取り 500万件に達した。

記事はまず、うまくいかなかったほうから始まる。2025年5月の「AI month」で monday は既存のワークフローに AI 機能を埋め込んだ。テキストの要約、情報の分類といったものだ。導入自体は確かに進んだが、使われ方として定着はしなかった。プロダクト担当 VP の Orly Stern Izhaki はこの時期を「AI dust」を作っていた時期 — それ以外は変わっていないワークフローの上に自動化を振りかけていた時期 — と呼び、そこから引き出された結論は、AI 機能を導入することと AI 企業になることは同じではない、というものだった。最高プロダクト・技術責任者の Daniel Lereya は、agent-first 製品への転換を同社で最も重要な決断の一つだったと述べている。

そのあとに起きたのは追加ではなく再構築だった。Claude をプラットフォームに取り込む4つの方法、IT・人事・マーケティング・経営オフィスにまたがる、役割の定まった名前付きエージェント群、そして別立てのチャット画面ではなくボード内のトリガーとメンションで仕事を割り当てられる「チームメイトとしてのエージェント」である。

## どんなときに役立つか
- AI 機能はすでに出していて、初月の数字は悪くなかったのに、利用が時折の要約程度で頭打ちになっているとき。
- エージェントを既存のワークフローに埋め込むのか、ワークフロー自体をエージェント中心に作り直すのかを決めるとき。
- エージェントが実際の仕事のある場所と平行したチャット画面で動いていて、文脈を人が手で貼り付けている状態のとき。
- ガバナンス・権限・信頼性を最初から設計していないために、エージェントの試験導入が本番の手前で止まり続けるとき。
- 汎用アシスタントを1つ配るのではなく、職能ごとに具体的なエージェントの仕事を定義する必要があるとき。

## 主なポイント
- **「AI dust」が失敗の形。** 既存ワークフローの上に自動化を振りかけると、要約や分類のように役には立つ機能はできるが、働き方は変わらず、利用も積み上がらない。
- **4つの導入経路。** Claude をモデルとしてプロンプトで作る monday Agents、Claude Managed Agents をプラットフォームに参加させる bring-your-own-agent、法務・財務プラグインを含む monday Agents Store の既製の専門エージェント、そしてダッシュボードで Claude をつなぎ、タスクを割り当て、顧客環境で実行するコーディング統合。
- **エージェントには汎用の権限ではなく名前の付いた仕事を与える。** IT は Intake & Triage Agent、Knowledge Agent、Incident Agent を運用し、人事は履歴書スクリーニング・面接調整・採用コーディネーション・フィードバック管理を、マーケティングは競合インテリジェンスとバトルカードを、経営オフィスは Operator Agent、Org Health Agent、Strategy Consultant Agent を持つ。
- **チームメイトとしての設計。** 各エージェントには名前とアバターがあり、ワークフロー内に居場所がある。仕事は別のチャット画面ではなく、従業員がすでにいる場所でトリガーとメンションによって割り当てられる。
- **生産ラインが1つのアイテムの上で回る。** キャンペーンの例では、ブリーフをマーケターとコンテンツリードが形にし、Strategist Agent が目的・メッセージの柱・チャネル・指標へ構造化し、Claude Managed Agent がランディングページの複数案を生成し、Brand Reviewer がブランドガイドラインと突き合わせて問題を指摘し、人が承認してから公開される。
- **顧客の顧客、Cooke Seafood。** 世界最大の家族経営水産企業で、進行中・提案中あわせて約200プロジェクトのデリバリーとリソース管理、130件の契約管理、そしてリスクを RAID ログへ上げる自動レポーティングを運用している。戦略担当ディレクターの Patti Stevens は、この変化を「更新しなければならなかったプラットフォーム」から「そこから運営するプラットフォーム」への移行として語る。
- **5つの教訓。** 技術よりメンタルモデルを動かすほうが難しかった。方向性・UX・技術・価格・信頼モデル・品質の定義が同時に動く中では、所有者が明確で意思決定の速い小さなチームのほうが階層構造よりも足並みを保てた。導入の可否はガバナンス・権限・透明性・信頼性という信頼インフラで決まった。エージェントの能力はバックエンド投資に依存し、エンタープライズ規模で生きたプロジェクトデータに接地させるため monday DB に投資した。そしてこの変革は、既存のアイデンティティを置き換えるのではなく拡張するものだった。

## 同梱リソース
- `skills/agent-first-product-transformation/SKILL.md` — AI 機能の段階から agent-first 製品へ移行する。
- `skills/agent-first-product-transformation/references/deployment-models.md` — エージェントをプラットフォームに取り込む4つの方法と、それぞれが適する場面。
- `skills/agent-first-product-transformation/references/agent-job-map.md` — 職能別の名前付きエージェントの仕事。
- `skills/agent-first-product-transformation/references/transformation-lessons.md` — 5つの教訓と、それぞれが計画に対して意味すること。
- `skills/agent-first-product-transformation/examples/campaign-production-line.md` — マーケティングの一気通貫の例と Cooke での導入。
- `agents/*.md` — 記事に名前が出た役割から抽出したサブエージェント5つ。
- `guides/agent-first-platform-rollout.{en,ko,es,ja}.md` — AI 機能から agent-first への展開順序。

## 出典
[How monday.com transformed its platform into an agent-first product where humans and agents collaborate](https://claude.com/blog/how-monday-com-transformed-its-platform-into-an-agent-first-product-where-humans-and-agents-collaborate) — 2026-08-20 公開。
