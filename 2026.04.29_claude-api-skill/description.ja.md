[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# claude-api skill が CodeRabbit、JetBrains、Resolve AI、Warp に登場

## この記事について

Anthropic が 2026 年 4 月 29 日に公開した発表によると、CodeRabbit、JetBrains、Resolve AI、Warp が `claude-api` skill をバンドルし、開発者がすでに使っているツールの中で本番運用可能な Claude API コードを得られるようになりました。この skill は 3 月に Claude Code で初めて導入されたもので、今回の発表によって利用範囲が広がります。記事によれば、skill は「どの agent パターンが向くか」「モデル世代ごとに変わるパラメータ」「prompt caching を適用すべきタイミング」など、Claude API コードがうまく動くために必要な詳細を捉えており、Anthropic の SDK が更新されると常に最新の状態に保たれます。

## どんなときに役立つか

- CodeRabbit、JetBrains/Junie、Resolve AI、Warp、Claude Code で Claude API コードを書く際に、パラメータを毎回調べる代わりにバンドルされた skill を活用したいとき。
- 新しい Claude モデルへの移行(記事では Claude Opus 4.7 を例示)を行う際に、モデル名・thinking 設定・パラメータ・beta header の更新をガイドつきで進めたいとき。
- 既存の agent に prompt caching や context compaction を導入したいが、ドキュメントを最初から読み直したくないとき。
- coding agent プロダクトを開発しており、オープンソースの `claude-api` skill をバンドルしてユーザーに同じ専門性を提供したいとき。

## 主なポイント

- `claude-api` skill は 3 月の Claude Code リリースに加え、今後は CodeRabbit、JetBrains、Junie、Resolve AI、Warp にもバンドルされます。
- skill は SDK の変更に追従して Claude を常に最新に保ち、古い API 知識によるレビュー時の事故を減らします。
- 記事が挙げる代表的な 4 つのプロンプト:
  - "Improve my cache hit rate." — 多くの開発者が見落としがちな prompt caching ルールを適用。
  - "Add context compaction to my agent." — compaction のプリミティブと agent パターンを案内。
  - "Upgrade me to the latest Claude model." — ガイド付きのモデル移行。Claude Code では `/claude-api migrate` で実行可能。
  - "Build a deep research agent for my industry." — Claude Managed Agents のガイド付きセットアップ。Claude Code では `/claude-api managed-agents-onboard` で実行可能。
- coding agent ビルダー向け:skill は `anthropics/skills` でオープンソース公開。バンドリングガイドによれば約 20 行の CI で自動更新できます。
- 記事に掲載された顧客コメント:Warp、CodeRabbit、JetBrains、Resolve AI — フローを途切れさせない、レビュー時の事故を減らす、モデル採用を早める、といった点が中心。

## 同梱リソース

- Skill: `skills/bundled-api-skill-usage-patterns/SKILL.md` — 記事が挙げた 4 つのプロンプトと slash command でバンドル skill を使う方法。
- リファレンス: `skills/bundled-api-skill-usage-patterns/references/integrations-and-quotes-from-post.md` — 発表された統合と顧客コメントの整理。
- 例: `skills/bundled-api-skill-usage-patterns/examples/usage-prompts.md` — 記事の 4 つの例示プロンプトを再利用可能な形でまとめたもの。

## 出典

Claude API skill now in CodeRabbit, JetBrains, Resolve AI, and Warp — Anthropic、2026 年 4 月 29 日: <https://claude.com/blog/claude-api-skill>
