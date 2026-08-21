[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
Anthropic が急成長中の十数社のスタートアップ — Artemis Security、Cainex、Clay、ClickHouse、Cognition、Commure、Crosby、Emergent、Harvey、Heidi、Higgsfield、Omni、Parahelp、Translucent、Zingage — に、Claude Code をどう使ってプロダクトを作り会社をスケールさせているかを聞き、その答えを五つの運用ルールにまとめた記事。全体を貫く問いは、プロダクト開発ライフサイクルをゼロから Claude Code で設計したらどうなるか、である。

五つのルールは、全員が出荷する／退屈な作業を自動化する／信頼せよ、ただし検証せよ／作り直す前提で作る／プロトタイプ・ドッグフーディング・プロダクト化。各章に創業者の言葉と具体的なヒントが入り、最後にそれらを1ページに集約したチェックリストが付く。報告された成果として、出荷機能30%増（ClickHouse）、エンジニアリング生産性2〜3倍（Omni）、バグトリアージ100%自動化（Clay）、週6,000件以上のPR（Artemis Security）が挙げられている。

## どんなときに役立つか
- 機能一覧ではなく、小さなチームがエージェンティックコーディングを軸にどう組織されるべきかの見取り図が欲しいとき。
- プロダクトへの洞察は非エンジニアが持っているのに、アイデアから動くプロトタイプへの道がないとき。
- SDLC のどの部分をエージェントに渡すか、そして信頼する前に何が整っている必要があるかを判断するとき。
- 書き直しが常に優先順位争いで負け、技術的負債の解体が予定に乗らないとき。
- 社内のエージェント実験を顧客向けプロダクトへ昇格させる経路が要るとき。

## 主なポイント
- **0→1 のステップは全員に開かれるが、分業は残る。** マーケターは引き続きマーケティングを、開発者は引き続き開発を行う。ただし最初のバージョンは問題を理解している本人が作る。Heidi はかつてのハンドオフ連鎖を「伝言ゲーム問題」と呼ぶ。
- **貢献に必要なのは激励ではなく仕組み。** MCP か CLI で Claude を実際のツールにつなぎ、プロトタイプがロードマップにつながる場を作り（Clay の四半期レビュー、Omni の Slack チャンネル）、基準をスキルとしてディレクトリやプラグインマーケットプレイスで共有する。
- **エージェントが繰り返し作業を最後まで担う。** ClickHouse の不安定テスト用・カバレッジ用エージェントは同リポジトリの第2位・第3位のコントリビューターであり、Clay は初回仕分けから修正提案までバグトリアージを自動化し、Translucent のレビュアーは変更全体にファンアウトして複数観点の結果を統合する。
- **ルール2と3は対になっている。** Zingage は初期に Claude へ完全な自律性を与え、「一見正しく見えるのに実際には違う」形でアーキテクチャから逸脱したもっともらしいコードを得た。解決策は `CLAUDE.md` に書いた567行の不変条件だった。
- **例ではなく原則を直す。** Cainex は監査担当者の訂正をバージョン管理されたエージェント指示に反映し、ゴールデンセットとランダムサンプルでバックテストする。最初のバージョンが過学習しパッチが積み上がった経験から得た方法だ。
- **恒久的なものはない。** Clay は同じものを四度作り、Harvey はモデル能力の波ごとにアーキテクチャを組み直し、Commure はフィーチャーフラグの解体をスキル呼び出し一つに変えた。作り直しを安くするのが git worktree とプランモードである。
- **フライホイール。** 自らのエージェンティックコーディングの実践を進めることで、フロンティアでハーネス設計がどう進化するかを掴め、それを自社のエージェントとプロダクトに投じられる。社内エージェント → ドッグフーディング → Claude API・SDK・Managed Agents 上の顧客向けプロダクト、という経路だ。

## 同梱リソース
- `skills/agentic-coding-operating-rules/SKILL.md` — 五つのルールを実行可能な運用手順として整理。
- `skills/agentic-coding-operating-rules/references/five-rules.md` — 各ルールの全文、創業者の言葉と境界条件付き。
- `skills/agentic-coding-operating-rules/references/checklist.md` — 記事の技術チェックリスト統合版。
- `skills/agentic-coding-operating-rules/templates/root-context-file.md` — 不変条件を書くルート `CLAUDE.md` の雛形。
- `skills/agentic-coding-operating-rules/examples/self-improvement-loop.md` — Cainex の訂正ループを段階ごとに。
- `skills/agentic-coding-operating-rules/examples/company-patterns.md` — 15社が実際に行ったこと。
- `agents/flaky-test-fixer.md`、`agents/test-coverage-finder.md`、`agents/multi-angle-code-reviewer.md`、`agents/bug-triage.md` — 記事で名指しされた四つのエージェント役割。
- `guides/startup-operating-model.{en,ko,es,ja}.md` — 運用モデルと導入の順序。

## 出典
[The Claude Code guide for startups](https://claude.com/blog/claude-code-guide-for-startups) Michael Segner 著 — 2026-08-20 公開。
