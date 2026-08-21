[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
Claude Code チームの Delba de Oliveira が、変更のたびに繰り返している手作業のチェックをスキルに変え、Claude 自身にフィードバックループを閉じさせる方法を解説します。ほとんどのエージェンティックなコーディングセッションは、コンテキスト収集 → 行動 → 結果の検証 → 必要なら戻る、というループをたどります。Claude はすでにコードベースの決定論的シグナル（型チェッカー、リンター、テスト、ランタイムエラー）から一部を自力で検証しています。Claude が推論できない残りが、人が手で踏む手順であり、それこそ書き留める価値のある手順です。

記事は、まず試すべき組み込みループ、検証スキルの最小の `SKILL.md` の形、そしてチェックの配置方法四つ — 単独実行、生成側スキルへの埋め込み、別スキルの後にチェーン、すべての PR で実行 — を、それぞれに合う状況・コスト・卒業の合図とともに扱います。

## どんなときに役立つか
- Claude が機能を実装するたびに、同じ小さな修正を繰り返しているとき。
- プロジェクト固有のルールは確かにあるのに、汎用リンターでは捕まえられないとき。
- 新規プロジェクトを始め、どう振る舞うべきかを書き留める必要があるとき。
- チェックを意図的に呼び出すか、埋め込むか、チェーンするか、チーム全体の PR ゲートにするかを決めるとき。
- 編集できないスキル（組み込みやプラグイン管理のもの）に検証を足したいとき。
- 個人の習慣がチームのインフラになる準備ができたとき。

## 主なポイント
- **検証ループとは、エージェントが自分の作業を確認する繰り返しのサイクル**です。テストやリンター、独自チェックを実行し、失敗を直してから先に進みます。スキルとしてパッケージ化すれば、人が思い出すことに頼らず、すべてのセッションが同じチェックを適用します。
- **まず組み込みを試す**：`/verify`、ツールチェーンのエラーコード（正確なビルド・テストコマンドを `CLAUDE.md` に列挙）、リサーチプレビューの Code Review、GitHub Actions、スペック検証、そして独立した採点エージェントが失敗を手戻りループへ戻す Claude Managed Agents のルーブリック。
- **チェックは平易な言葉で、初日の新しいチームメイトに手渡すつもりで書く。** 言語化しづらければ、まず Claude にベストプラクティスを尋ねて編集を。あなたの版が異なる点こそ書き留めたい内容です。
- **チェックが定性的である必要はない。**「バックフィル手順のないカラム削除マイグレーションは却下する」は決定論的かつプロジェクト固有で、汎用リンターでは捕まえられません。
- **最も単純な検証スキルは、数行の frontmatter と本文だけ**です。何を読み、何を確認し、どう報告して直すか。手書きが面倒なら `skill-creator` がインタビューしてくれます。
- **単独実行**は毎回は当てはまらない横断的チェックに向きます。代償は呼び出しを覚えておくことで、毎回の変更のあとに実行しているなら埋め込みかチェーンへ移る合図です。
- **埋め込み**は生成側スキル本文への 1 行追記ですが、編集できるスキルにしか使えません。組み込みスキルとプラグイン管理スキルは更新時に上書きされます。
- **チェーン**は習慣を契約に変えます。「`/simplify` のあとは必ず `/verify` を回す」が「`/simplify` は終了時に必ず `/verify` を回す」になります。Anthropic の Claude Code チームは `/code-review` → `/simplify` → `/verify` → `/design` をチェーンしています。柔軟性を自動化と引き換えにし、トークン消費が増えうる点に注意。
- **すべての PR で**回した時点で、検証は個人のインフラからチームのインフラになります。ただしチェーンが流動的なうちは見送りを。調整のたびにチーム全体に見えるイベントになります。

## 同梱リソース
- `skills/verification-loop-builder/SKILL.md` — 組み込みループ、チェックの書き方、四つの配置パターン、六段階の作成プロセス。
- `skills/verification-loop-builder/templates/verification-skill.md` — frontmatter + 本文の最小形と各フィールドの書き方。
- `skills/verification-loop-builder/templates/wrapper-chain-skill.md` — 変更できないスキルにチェーンするラッパーパターン。
- `skills/verification-loop-builder/examples/verify-log-hygiene.md` — 記事のログ衛生スキルの完成形。
- `skills/verification-loop-builder/examples/scaffold-component-embedded.md` — コンポーネント生成スキル内の 1 行埋め込み。
- `skills/verification-loop-builder/references/built-in-loops.md` — 六つの組み込み検証手段の詳細。
- `skills/verification-loop-builder/references/deployment-patterns.md` — 単独・埋め込み・チェーン・PR 全体と、それぞれのコストと卒業の合図。
- `guides/verification-loops.{en,ko,es,ja}.md` — 4 言語の完全な解説。

## 出典
[Building verification loops in Claude Code with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills) — Delba de Oliveira、2026年7月22日。
