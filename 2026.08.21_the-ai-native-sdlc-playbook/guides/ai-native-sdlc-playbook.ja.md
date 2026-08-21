[English](./ai-native-sdlc-playbook.en.md) · [한국어](./ai-native-sdlc-playbook.ko.md) · [Español](./ai-native-sdlc-playbook.es.md) · **日本語**

# AIネイティブSDLCプレイブック

AnthropicのApplied AIチームが社内および顧客との協業で実践してきた方法をもとに、ソフトウェア開発ライフ
サイクル（SDLC）を段階ごとに変革するためのガイド。

## コードはもはやボトルネックではない

各組織は、1年前には考えられなかった速度でAIにコードを書かせ始めた。しかしコードを取り巻くプロセスは同じ
速度では変わっていない。承認ゲート、レビュー、引き継ぎ、ポリシーがそのまま残り、エージェンティックな
コーディングがもたらすはずの生産性向上を止めている。

従来のSDLC（計画 → 設計 → ビルド → テスト → デプロイ → 保守）は、コードを書いて実装することが最も時間と
コストのかかる段階だった時代に、効率を最大化するよう設計された。PRD、見積もりの儀式、プロダクトセキュリティ
レビューは、数週間から数四半期に及ぶ開発期間中に足並みをそろえさせるために存在した。さらに従来のSDLCの統制は、
すべての手順を人間が実行することを前提にしている。

ビルドが数時間に縮むと、次の三つが真になる。

1. **ボトルネックがビルドの左右の手順に移動する。** 計画、レビューとテスト、デプロイは依然として人間の速度で
   動いている。
2. **統制が現実と合わなくなる。** 人が一行ずつ書いていた頃は一行ずつ手でレビューすることに意味があったが、
   エージェントがdiffの大半を書くようになると追いつけない。
3. **ガバナンスのコストが上がる。** 例外処理は依然として週次・月次で開かれる会議や委員会を経由するからだ。

セキュリティが最も分かりやすい例だ。セキュリティチームは人間の産出量に合わせて人員が組まれているため、
エージェントがコードの産出量を何倍にもすると、レビュー待ちが積み上がるか、十分レビューされないコードが出て
いくかのどちらかになる。規制下の組織はどちらも受け入れられないので、セキュリティとポリシーのチェックが
エージェントの速度に追いつく必要がある。

## AIネイティブSDLCとは

AIネイティブSDLCは、従来の統制目的をそのままに、その実施方法を変える。線形の流れの代わりにプロセスはループに
なり、各地点にAIが組み込まれ、段階間の引き継ぎは手作業ではなく自動で行われる。

| 段階 | 従来のSDLC | AIネイティブSDLC |
|---|---|---|
| 計画 | 委員会が要件を集め、ワークショップと承認で絞り込み、手で書き起こす | Claudeが情報源から直接、課題を統合し、人が読めて機械が実行できる`intent.md`として捉える |
| 設計 | アナリストが仕様を書き、デザイナーがそれを読み解く | 要件と設計をエージェントとの1セッションに圧縮。スキルとして符号化された基準が導き、gitでバージョン管理 |
| ビルド | テストとコードは手書きで、ドキュメントは開発が終わってから書く | テストとコードはAIが生成し、組織的知識はバージョン管理された機械可読な`CLAUDE.md`とスキルとして維持 |
| テスト | 段階の境界ごとのQAゲート | 実装に織り込まれた継続的なeval |
| デプロイ | 人がすべての行をレビューし、ガバナンスはレビューサイクルの中で、しばしば一貫性なく行われる | 何層ものエージェンティックレビュー。人のレビューは規制対象・重要コードに集中。ガバナンスはAIが行動する瞬間に実施され、フックが承認ゲートになる |
| 保守 | 人が本番のバグを見張る | エージェントが稼働中のデプロイを監視。管理帯を逸脱すれば診断し、新しい`intent.md`としてループに書き戻す |

ほとんどの組織はこの二列のあいだのどこかにいる。

### コミットされた成果物が糸になる

各段階は成果物をバージョン管理に書き込んで終わり、次の段階はそれを読んで始まる。`intent.md`、`spec.md`、
`plan.md`、diffとそのテスト、レビュー結果を含むPR、そしてインシデント記録である。初期段階でマークダウンが
成果物になるのは、プロダクトオーナーとエージェントの双方が同じファイルを読んで動けるからだ。ビルド以降は、
成果物はコードとその記録になる。

コミットの連なりは監査証跡でもある。誰が何を求め、エージェントが何を作り、誰が承認したのか。判断を要する
すべての決定について、人が引き続き責任を持つ。変わるのは、人の注意がどの成果物に向くかである。

受理された`intent.md`が要件・設計パスを起動し、承認された`spec.md`がプランモードを起動し、マージされたPRが
パイプラインを起動し、本番で逸脱した管理帯が次の`intent.md`を書く。最初は各手順を手でプロンプトする。到達点は、
受理された成果物が次のゲートを開くループである。

## 段階1 — 計画：意図を捉える

*アイデアが、誰かが書き起こしてくれるのを待たなくなる。*

従来、アイデアはバックログ項目、ユーザーストーリー、ストーリーポイント、リファインメント会議を経てようやく
誰かが動ける状態になる。引き継ぎのたびに所有権が移るため、エンジニアリングに届く頃には発案者の意図から
何段階も離れている。

代わりに、発案者がClaudeとブレインストーミングし、その結果を`intent.md`として書く。自分の言葉によるプロト
スペックで、何を望むのか、なぜか、どんな制約の下でかを含む。形式ばった言い回しは不要だ。Claudeはアナリストが
尋ねるであろう質問をする。範囲、ユーザー、制約、そして成功とは何か。発案者はClaudeが誤解した点を直し、ファイルを
コミットする。

**始め方.** 前提条件なし。エンジニア以外の人向けのClaudeアクセス（claude.aiまたはCowork）、合意された
`intent.md`テンプレート、そしてプロダクトオーナーが見ている共有のバージョン管理された置き場が必要だ。単一
プロダクトなら、プロダクトリポジトリ内の`intent/`フォルダが最も単純で、成果物の連鎖がそこから派生するコードの
隣に置かれる。専用のintentリポジトリは、意図が複数リポジトリにまたがるときにだけオーバーヘッドに見合う。

この整備はプラットフォームチームの一度きりの作業で、誰に書き込み権限を与えるかもここで決める。リポジトリが
できれば、gitの経験がない貢献者はclaude.aiやCoworkからバージョン管理コネクタ経由でコミットできる。

**実際の`intent.md`:**

```markdown
# Intent: claims status self-service
Author: J. Ortiz (claims operations). Status: draft.

## Problem
Customers phone the contact center to ask where their claim is.
Handlers spend roughly a third of call time on status-only queries.

## Proposed outcome
Customers see claim status, next step and expected date in the portal.

## Affected users and systems
Claims handlers, portal team, claims-core API.

## Constraints
No new PII in the portal session. Existing authentication only.

## Open questions
Do third-party loss adjusters need access too?
```

**ガバナンス.** 証拠はコミットされたファイルそのもので、作成者、タイムスタンプ、全改訂履歴がgitに残る。
プロダクトオーナーが承認し、受理・却下の判断はマージまたはレビューのクローズとして記録される。

**測定.** 先行指標：最初の会話からコミットされた`intent.md`までの時間。数週間の要件抽出・洗練サイクルから
数時間へ落ちることが期待値だ。遅行指標：意図が設計段階へ進む生存率、および最初の`spec.md`コミット以降に
`intent.md`へ加えられた変更の数。

## 段階2 — 設計：要件と設計が一つに畳まれる

要件と設計は従来、別々のチームが担う別々のフェーズだ。分離は説明責任のために存在するが、遅く、そして情報を
失う。

いまや両方が一つのプロンプトされたセッションで起こる。Claudeは受理された`intent.md`を受け取り、ブランド、
セキュリティ、コンプライアンス、UXに関する組織のスキルを制約として、懸念箇所にフラグを立てた要件・設計仕様を
作る。プロダクトオーナーは仕様をレビューするが、自分では書かない。

出発点となるプロンプト：

```text
Read the attached intent.md and produce a requirements and design spec for
integrating it into our existing codebase. Apply the skills available to you so
the plan conforms to our brand guidelines, security policies and UX standards.
Document the spec fully as spec.md, ready to hand to the engineering team.
Describe clearly any areas of concern, especially where you cannot satisfy
contradicting policies.
```

最初は手で実行し、次に組織レベルのスラッシュコマンドとして符号化し、その次には意図の受理をトリガーにして、
非対話ジョブが`spec.md`をプルリクエストとしてコミットするようにする。そこから先、プロダクトオーナーの最初の
関与はレビューになる。

フラグが立った懸念から片づける。アナリストならエスカレーションしていた地点だからだ。それぞれをポリシー
オーナーと解消してからエンジニアリングに仕様を渡す。`spec.md`は`intent.md`の隣にコミットする。この二つ一組が、
何が求められ、何が決まったのかを記録する。

フロントエンドの作業がこの畳み込みを最もよく示す。意図が受理されると、プロダクトオーナーは`intent.md`から
Claude Design（ベータ）でモックを作り、モックを詰めてからClaude Codeへ書き出してビルドさせる。

**ガバナンス.** 生きたポリシーが、数週間後のレビューで発見されるのではなく、仕様が書かれている最中に読まれ、
適用される。仕様、それを生んだプロンプト、適用されたスキルのバージョンがすべてバージョン管理に記録される。

**測定.** 先行指標：同一変更についての`intent.md`コミットと`spec.md`コミットの経過時間（gitのタイムスタンプ
二つ）。遅行指標：ビルド開始後の要件手戻り。同一変更の最初の`plan.md`コミットより後の日付の`spec.md`コミット数で
数える。

## 段階3 — ビルド：承認されたプランなしに実装しない

### 既定の出発点はプランモード

従来、変更をどう作るか——どのファイル、どのテスト——はエンジニアの頭の中か、せいぜいチケットのコメントに留まる。
レビュアーが最初に見るのは出来上がったdiffで、その時点では手戻りが遅い。

代わりに、作業はClaudeがプランモードで作った文書化されたプランから始まる。プランモードでClaudeはコードベースを
読めるが変更はできない。`intent.md`と`spec.md`を渡し、変わるファイル、作業の順序、それを証明するテストを挙げた
実装プランを求める。そして問い詰める。この変更は何を壊しうるか、どの手順が最も危ういか、何をしないと決めたか。
その会話を見ていないエンジニアがプランだけで実装できるまで反復し、`plan.md`としてコミットする。

```markdown
# Plan: claims status self-service (from intent.md 2026-06-02)
## Files that change
portal/src/claims/StatusPanel.tsx (new), claims-api/routes/status.py,
claims-api/tests/test_status.py
## Order of work
1. Add the status endpoint behind existing auth.
2. Panel against the endpoint.
3. Wire into the portal nav.
## Risks
The claims-core API rate-limits at 50 rps; the panel must cache.
## Proof
test_status.py covers the four claim states; screenshot matches the
approved mock.
```

しっかりしたプランがあれば、実装は一度で通ることが多い。実装がプランから外れたら、同じコミットで`plan.md`を
更新する。フックで両者の同期を強制してもよい。

プランモードは設計レビューそのものを強制する。エンジニアがプランを受け入れるまでClaudeはファイルを編集できない
ので、方向転換はまだ文書を直すだけで済む段階にとどまる。

### オートモード

Claude Codeはオートモードでも動く。プランが承認されれば、編集ごとの確認なしに各変更を適用する。後続のプレイの
ガードレールが成熟するにつれ——調整済みの`CLAUDE.md`、ポリシーを符号化したスキル、危険な行動を止めるフック、
Claudeが実行できるテストスイート——自動承認が日常作業の既定になる。引き締まった仕様、小さい影響範囲、すでに
テストが覆っているコードが条件だ。焦点は、エージェントの編集を見守ることから、より長い自律セッションのあとに
成果物をレビューすることへ移る。

### `CLAUDE.md`

`CLAUDE.md`は、新しく入った人が必要とする文脈——規約、コマンド、アーキテクチャ、チームが最もよく見る間違い——を
Claudeに与える。人の頭の中やwikiにあった知識が、毎セッションの冒頭でエージェントが読むファイルになる。

`/init`を実行し、生成されたファイルを新任者が初日に必要とする分まで削り、リポジトリのルートにチェックインして
チーム全体が一つのバージョンを共有し、変更がコードと同じようにレビューされるようにする。実務上のルール：Claudeが
同じ間違いを二度したら、その訂正は`CLAUDE.md`に入れる。1ページ以内に保つこと。Claudeはセッション開始時に全部を
読むので、古い記述は何の利益もなく文脈を占める。

```markdown
# Payments service

## Commands
- Build: make build
- Test: make test (unit), make itest (integration, needs docker)
- Lint: make lint (runs in CI; fix before pushing)

## Conventions
- Java 21, Spring Boot 3. No new Lombok.
- Money is always BigDecimal, never double.
- Every endpoint needs an integration test in src/itest.

## Architecture
- api/ holds REST controllers, core/ holds domain logic,
  adapters/ talks to external systems.
- Kafka events are defined in schemas/; never edit generated classes.

## Things Claude gets wrong
- Do not bump dependency versions; the platform team owns them.
- The legacy v1/ package is frozen; changes go in v2/.
```

### 組織的知識としてのスキル

スキルは組織的知識を運用可能にする手段だ。明示的で、バージョン管理され、広く適用され、ポリシーが変われば中央で
更新される。目安は、**一貫して適用されなければならない組織的知識はスキルに書き、`CLAUDE.md`やプロンプトに属する
ものはスキルにしない**こと。

いま一貫して守られていない知識を一つ選び、いつ発火するかをフロントマターに、何をするかを本文に書いた`SKILL.md`を
含むフォルダとして書く。コードと一緒に配布されるよう`.claude/skills/<name>/`に置くか、プラグインとして組織全体に
配布する。実際に発火するかテストする——同じ作業を別の言い方で頼み、毎回ロードされるか確かめる。ポリシーが変われば
スキルを変え、ポリシーオーナーが変更を承認する。エンジニアは次のセッションで自動的に新版を拾う。

```markdown
---
name: secure-api-review
description: Apply the API security standard. Use whenever creating or
  modifying an external-facing endpoint, reviewing API code, or
  generating an OpenAPI spec.
---

# Secure API review

When you create or change an API endpoint:

1. Authentication: every endpoint requires the gateway JWT;
   no anonymous routes outside /health.
2. Input validation: validate request bodies against the OpenAPI
   schema and reject unknown fields.
3. Audit: every state-changing endpoint emits an audit event with
   actor, action, entity and timestamp.
4. Data classification: fields tagged pii in the schema must never
   appear in logs or error messages.

Run the endpoint check script and include its output in your summary.
```

**スキルは統制だが、助言的な統制である。** コードが書かれる最中にClaudeがポリシーを適用する可能性を高めるだけで、
セッションに順守を強制するものはない。常に成り立たねばならないポリシーには、その背後に決定論的な何かが要る。
行動を止めるフックか、PRでポリシーを再確認するレビューパスだ。スキルは違反を稀にし、フックはそれをほぼ不可能に
する。

### ビルド時ガードレールとしてのフック

実装中のClaudeの行動はほとんどがファイル編集とシェルコマンドなので、フックが最も頻繁に発火するのはビルド段階だ。
ビルド段階のフックは、生成クラスや凍結パッケージのような保護パスの編集を止め、ファイル編集後にフォーマッタと
リンタを走らせてドリフトを溜めないようにし、認証情報をdiffから締め出す。

例外なく成り立つ必要のあるポリシーのスキルは、フックで裏打ちする。フックは一致する行動ごとに走るので、ビルド段階の
フックは高速で、変更されたファイルに限定されているべきだ。テストスイート全体のような重いチェックはコミットかPRに
属する。人に承認を求めるフックはデプロイのゲートに属する——ビルド中の承認プロンプトは、並列で走るすべての
セッションのクリティカルパスに人を戻してしまう。

### 並列セッションとサブエージェント

並列セッションとは、自分のgit worktreeで別のタスクをこなす、もう一つの完全なClaude Codeインスタンスだ。互いに
共有しているのは、それらを操るエンジニアだけである。サブエージェントは一つのセッションの中で、自前のコンテキスト
ウィンドウとツール制限を持つ限定的な助手として走り、複数のタスクにまたがって繰り返される仕事に向く。

異なるファイルに触れるタスクへ作業を分ける。どこが独立かはプランを見れば分かる。ファイルを共有するタスクは一つの
セッションで順に走らせる。並列タスクごとに自分のworktreeを与える（あるターミナルで`claude --worktree feature-auth`、
別のターミナルで`claude --worktree fix-rate-limit`）。二つか三つのセッションが妥当な出発点で、実際の上限は一人が
きちんとレビューできるストリーム数だ。

繰り返しの仕事は`.claude/agents/`に定義したサブエージェントにする。メインエージェントが終わったあと不要な複雑さを
削ぎ落とすコードシンプリファイア、アプリを起動して挙動を確かめるベリファイア、コードベースを探索してメインの文脈を
埋めずに報告するリサーチャーなどだ。定義はgitにチェックインする。

```markdown
---
name: verifier
description: Runs the app and checks the change works before the session
  reports done
tools: Bash, Read
---
Start the app with make run. Exercise the changed behavior and the two
nearest neighboring flows. Report what you ran, what you saw, and any
behavior that does not match plan.md. Do not fix anything; report only.
```

### レガシーシステムと信頼できる唯一の情報源

既存プロセスもすでにこれらの成果物を追跡している。ただしマークダウンではないだけだ。作業項目はJira、要件は規制
トレーサビリティを備えたツール、デザインはFigma、変更承認は変更審議会にあるかもしれない。監査人がすでに受け入れて
いるため、これらのシステムは押しのけにくい。

プロセスが生むすべての成果物について、**一つ**のシステムを信頼できる情報源に指名し、他はコピーかリンクだけを持つ
ようにする。三つの構成が機能する。リポジトリを情報源とし、レガシー側がコミット内のファイルを参照する構成。レガシー
システムを情報源とし、Claudeがセッション開始時に記録を読み、同じセッションでMCPコネクタ経由で結果を書き戻す構成。
最低線として連結だけを保ち、成果物にはレコードIDを、レコードにはマークダウンファイルのコミットSHAを記す構成。情報源が
二つあることを受け入れるなら、連結は移行の出発点として良い。

## 段階4 — テスト：検証がセッションの内側へ入る

### Claudeにフィードバックループを与える

コードが動くという信号は、従来は遅れて届く。CIは数分後、テスターは数日後、本番は数週間後だ。エージェントがコードを
作る状況で信号が遅いということは、人がその出力すべてを確認しなければならず、その人がボトルネックになるということだ。

Claudeには常に自分の仕事を検証する手段を与える。テスト、ビルド、あるいはスクリーンショットの差分だ。

1. いま作業の確認に一連のコマンドと環境知識が要るなら、失敗時に非ゼロで終了する単一のターゲットに包む。
2. `CLAUDE.md`のCommandsセクションに、各コマンドを健全な出力例つきで挙げる。
3. Claudeが尋ねずに自分で確認できるよう、定量化した目標を示す。「test_status.pyの全テストが通る」「スクリーン
   ショットが添付のモックと一致する」「エンドポイントが新しいフィールドとともに200を返す」といった具合だ。
4. バグ修正では、失敗するテストを先に書く。Claudeにバグをテストとして再現させ、実行させ、期待どおりの理由で失敗する
   ことを確かめる。そのテストをコミットする。そのうえで初めて、テストを編集せずに通すよう依頼する。修正の前から存在し、
   エージェントが書き換えられなかったテストこそ、バグが消えた証拠になる。
5. UI作業では視覚的な確認でループを閉じる。ブラウザかスクリーンショットのツールとモックを渡し、実装→撮影→比較→調整を
   反復させる。二、三巡が普通だ。
6. 検証を「完了」の一部にする。指示は`CLAUDE.md`に置く。

```markdown
## Verifying your work
- Build: make build (must finish with "Build succeeded")
- Test: make test (all green; never skip or delete a failing test)
- Lint: make lint (zero warnings)

Run all three before reporting any task complete, and paste the output.
If a test fails, fix the code, not the test.
```

ループ自体も守る必要がある。コードを直すエージェントが、そのコードに対する検査を弱められてはならない。修正タスク中に
テストファイルの編集を止めるフックがこれを果たす。代替はレビューでdiffを確認し、テストに触れた変更を却下することだ。

フィードバックループとベリファイアのサブエージェントを混同しないこと。ループはタスクの全体を通じて必要なだけ回る。
ベリファイアは、セッションが作業を終えたと判断したあと、新しいコンテキストウィンドウで一度だけ走る最終確認を担い、
その判定はコードを生んだ前提に染まらない。

### CIでの継続的eval

evalは段階ゲート型QAのAIネイティブ版だ。エージェントの構成が変わるたびに走るスイートである。新しいモデルに差し替えたり
プロンプトを書き直したりしたとき、エージェントが同じ水準で仕事をこなせているかをスイートが答える。生きたスイートとして
扱うこと。モデルが良くなるにつれ、かつて弁別力のあったケースがそうでなくなるので、継続的な監視から生まれた新しいケースを
足し続ける必要がある。

最近の作業から実際のタスクを20〜50件、その期待される・受け入れられた結果とともに集め、それぞれをプロンプトと受容基準
（テスト通過、リントがきれい、挙動が不変、ポリシー順守）として書く。スイートはCIで非対話に、スケジュールに従って、
そして`CLAUDE.md`・スキル・フックへのあらゆる変更時に走る。その構成がエージェントを操るのだから、コードが受けるのと同じ
回帰テストを受けるに値する。構成変更は結果でゲートする。通過率を下げるスキル変更は、マージ前にレビューされる。本番
インシデントはそれぞれevalになり、インシデントを所有したチームが書き、回帰テストとしてスイートに残る。

```yaml
name: Agent evals
on:
  pull_request:
    paths: ['CLAUDE.md', '.claude/**']
  schedule:
    - cron: '0 2 * * *'
jobs:
  evals:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm install -g @anthropic-ai/claude-code
      - name: Run eval suite
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          for eval in evals/*.json; do
            claude -p "$(jq -r '.prompt' $eval)" \
              --allowedTools "Read,Edit,Bash(make test)" \
              --output-format json > result.json
            ./evals/check.sh "$eval" result.json
          done
```

## 段階5 — デプロイ：レビューは双方向に、リリースはゲートで

### PRレビューループの中のAI

レビュー能力は人間の産出量を前提に計画されていた。PRはレビュアーが全部を読むまで待ち、品質はレビュアーの負荷で揺れ、
著者が催促するあいだにバックログが積み上がる。

Claudeはレビューをし、レビューを受けもする。すべてのPRが同一のレビューパス群を通り、指摘は深刻度で並ぶ。人の注意は
一段上へ移る——この変更はプランが意図したことをしているか、そしてそのリスクは受け入れられるか。

最短の出発点はマネージドなCode Reviewサービス（リサーチプレビュー）だ。管理者が有効化し、リポジトリを選ぶ。パイプラインを
自分で制御したい場合や、API呼び出しを自社のクラウド契約（Bedrock、Vertex、Foundry）経由にしたい場合は、
`claude-code-action`で自前のCIでレビューを走らせる。

テックリードはレビューポリシーをリポジトリルートの`REVIEW.md`として書く。

```markdown
# Review instructions

## Passes
Run three passes and tag each finding with its pass:
- Bugs: logic errors, broken edge cases, subtle regressions
- Security: injection risks, authentication gaps, PII in logs
- Compliance: the change matches spec.md, plan.md and our design principles

## What Important means here
Reserve Important for findings that would break behavior, leak data
or breach a policy. Style and naming are nits.

## Cap the nits
Report at most five nits per review; summarize the rest as a count.

## Do not report
Generated files under src/gen/ and anything CI already enforces.
```

指摘それ自体がPRを承認したり止めたりはしない。ブランチ保護は依然としてコードオーナーの承認を要求する。指摘でマージを
ゲートしたいプラットフォームエンジニアは、チェックランが機械可読な集計として公開する深刻度カウントを読めばよい。

レビュアーか著者がレビューコメントで`@claude`をタグ付けすると、Claudeがそのコメントに対応して修正をプッシュし、スレッドに
依頼と変更の両方が記録される。Claudeが開いたPRについては、未解決コメントと失敗チェックを掃き出して対応し、PRがグリーンに
なりコードオーナーの承認だけを待つ状態になるまで回すループを、独自コマンドで包むチームもある。

レビューの指摘は`CLAUDE.md`へ還る。同じ間違いが二度目に指摘されたとき、その訂正はそのレビューの一部としてファイルに入り、
レビューは`CLAUDE.md`を読むので、次のPRからその間違いは捕まる。月に一度、テックリードは指摘を評価し、nitの量に上限を設けて
設定を調整する。

**職務分離は保たれる。** コードを書いたエージェントには、それを承認する手段がない。

### 承認ゲートとしてのフック

フックは**尋ねる**こともできる。特定の人が承認するまで行動を止めるのだ。リリースのゲートに必要なのはこれである。
エンジニアリングのリーダーシップが、変更管理・コンプライアンスとともに、残さねばならない人間の承認ゲートを列挙する。
変更管理の承認、リリース許可、保護パスの編集などだ。プラットフォームエンジニアがそれぞれを、許可・質問・拒否のできる
フックとして表現する。

チームのフックはgitの`.claude/settings.json`に、譲れないフックはプラットフォームやIT管理者が所有するmanaged settingsに置く。
後者は個々のエンジニアが無効化できない。拒否は自らを説明すべきだ。フックが行動を止めたとき、その理由と承認への経路が
Claudeの出力に現れる。

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/production-gate.sh"
          }
        ]
      }
    ]
  }
}
```

```bash
#!/bin/bash
# Production deploys require a named release authorization
cmd=$(jq -r '.tool_input.command' < /dev/stdin)
if [[ "$cmd" == *"deploy"* && "$cmd" == *"production"* ]]; then
  if [ -z "$RELEASE_APPROVAL" ]; then
    echo "Production deploys need a release authorization." >&2
    exit 2   # exit 2 blocks the action; the message goes to Claude
  fi
fi
exit 0
```

フックはデプロイ専用ではない。Claudeが行動するところならどこでも走る。ビルド段階で変更チケットなしのマイグレーションや
インフラ編集を止めることもできるし、修正タスク中にエージェントがテストファイルを編集するのを止めることもできる。

### 規制産業向けのmanaged settings

プラットフォームチームがMDMや管理コンソールで配布し、エンジニアは編集できない。denyルールは秘密情報をエージェントの文脈の
外に置き、ツール経由のネットワーク送出を止める。allowリストは安全な内側のループを事前承認し、denyリストがプロンプト疲れに
ならないようにする。`disableBypassPermissionsMode`と`allowManagedPermissionRulesOnly`は、どのエンジニアも、プロジェクト
ファイルも、コマンドラインフラグもルールを広げられないようにする。サンドボックスは権限では埋まらない隙間を塞ぐ。ツール
レベルのdenyはシェルコマンドがネットワークに届くのを止めないが、OSレベルのドメイン許可リストは送出そのものを遮断し、
`failIfUnavailable`はサンドボックスを好みではなくゲートにする。credentialsブロックは、サンドボックス内のシェルが`~/.ssh`や
クラウド認証情報を読むことを拒み、指定した秘密をすべてのサンドボックスコマンドの環境から取り除く。`allowManagedHooksOnly`、
`disableSideloadFlags`、`strictKnownMarketplaces`、`allowManagedMcpServersOnly`は、エンジニアのマシン上のあらゆるスキル、
エージェント、フック、MCPサーバーが承認済みマーケットプレイス経由で来たことを保証し、`requiredMinimumVersion`は組織が
評価していないビルドでの起動を拒む。

こうした構成は、そのまま写す推奨ではなく、調整して使う出発点として扱うこと。あらゆるdenyは能力とのトレードオフであり、
適切な均衡はリポジトリのデータ分類次第だ。

### CI/CD統合とデプロイ

パイプラインは従来、決定論的なスクリプトを走らせ、判断を要するものは人を待つ。代わりに、判断を要する手順について、
スコープを絞った認証情報を持つサンドボックスの中でClaudeを非対話にパイプライン内で走らせる。

読み取り専用の判断手順から始める。失敗したビルドのトリアージ、フレーキーテストの要約、チェンジログの下書きなどだ。

```yaml
- name: Triage failed build
  if: failure()
  run: >
    claude -p "Read the build log at out/build.log. Identify the most
    likely cause, say whether the failure looks flaky or real, and write a
    three-line summary for the PR thread." >> triage.md
```

次に、既存のゲートの背後に書き込み手順を足す。リントの修正、生成ドキュメントの更新、`@claude`メンション経由のレビュー
コメント対応などだ。エージェントが書くものはすべてブランチ保護を通じてPRとして届き、エージェントにmainへ直接プッシュする
経路はない。エージェントのジョブはネットワークポリシー下のコンテナで短命のスコープ付きトークンとともに走り、既定では本番の
認証情報を持たない。

デプロイはMCPで公開し、deploy・status・rollbackを環境ごとにスコープされたツールにする。認証情報を抱えたシェルスクリプトでは
なく、許可リストになるということだ。自律性は環境ごとに段階をつける。開発ではエージェントが自由にデプロイし、本番では
エージェントがリリースを準備してリリースマネージャーが許可し、フックがゲートを実施する。ロールバックはパイプラインで最も
リハーサルされた経路であるべきだ。ステージングで定期的に走らせておく。保守のループがこれを呼ぶからである。

**支配的な原則：エージェントは本番ゲートまで行動でき、その先へは行けない。**

## 段階6 — 保守：ループを閉じる

保守は従来、受動的だ。午前3時にアラートが鳴っても見逃されうるし、チケットは誰かが拾うまでバックログに座り、別の火事が
起きればポストモーテムのアクションがコードベースに届かないこともある。

代わりに、トリガー——管理帯の逸脱、チケット、チャンネルのメッセージ、スケジュール——が人を介さずにClaudeを呼ぶ。Claudeは
診断し、ゲートされた経路でのみ行動し、見つけたことを`intent.md`として書き、それが上記の段階を通っていく。この段階は
ヘッドレスで走り、段階間の独立した信頼度ゲート——決定論的なチェック、あるいは敵対的にレビューするエージェント——が、前段階の
出力を先へ進めるか人へエスカレーションするかを決める。

**ループを閉じる手順：**

1. 安定したローリングベースラインを持つ指標を一つ選ぶ。CIのテスト失敗率、デプロイ後の5xx率、PRサイクルタイムなど。
2. 検知スクリプトを書く。通常はローリングウィンドウの平均と標準偏差に、Western Electricなどのルールを重ね、スパイクだけでなく
   緩やかなドリフトも捉えるようにする。バージョン管理し、ユニットテストを付ける。**検知は完全に決定論的で、モデルは関与しない。**
3. 対応の段階をバージョン管理された設定に定義する。1σではスクリプトはログを残すだけ、2σではClaudeを読み取り専用で呼んで
   診断させ、3σではClaudeが行動できる——ただしレビューゲートへ入るPRを開くか、事前承認済みのランブックを起動する方法だけで。
4. トリガーはGitHubやGitLabのスケジュールワークフロー、既存監視スタックからのWebhook、あるいはネットワーク内のcronジョブで
   よい。Claudeはステートレスに走る。CIランナー上の非対話ステップか、サンドボックス化されたコンテナ内のAgent SDKサービスだ。
   ステートレスかつ非対話だからこそ、誰も始めなくてもループが始まり、終わる。
5. エージェントは診断を段階1の形式の`intent.md`として書く。異常とその証拠、提案する結果、影響するシステム、未解決の質問を含める。
6. サービスオーナーかオンコールのエンジニアがキューをトリアージする。いま直すか、予定に入れるか、却下するか。却下は帯の調整に
   使われ、ノイズを減らす。
7. 修正が出たら、そのインシデントのevalを追加し、同種の問題が今後守られるようにする。

```yaml
metric: ci_test_failure_rate
baseline: rolling_30d
rules: western_electric
tiers:
  1sigma: { action: log }
  2sigma: { action: diagnose, tools: "Read,Grep,Bash(gh run view *)" }
  3sigma: { action: propose, routes: [pull_request, runbook:rollback-deploy] }
```

実際にどう働くか。CIのテスト失敗率が3σを超えると、エージェントはフレーキーテストを隔離するかリバートPRを開き、レビューゲートが
判断する。デプロイ後の5xx率が、その窓の中のデプロイとともに3σを超えると、エージェントは既存のロールバックパイプラインを起動する。
PRサイクルタイムがドリフトのルールに触れると、エージェントはエンジニアリングのリーダーシップ向けのレポートを書く。このハーネスが
本番指標だけでなくプロセス指標にも効くことを示す例だ。

### Claude TagでオンコールにつくClaude

インシデントは職場のコミュニケーションアプリからも届く。インシデントチャンネルの夜10時のSlackメッセージも、いまや即座に対応
できる。Claude Tag（パブリックベータ、現在はSlack）はClaudeを自らのアイデンティティでそれらのチャンネルの一員にする。だから
新しいインシデントごとに一次対応者がつき、その対応自体がループの一部となり、次のインシデントのための記憶になる。

会話と組織的知識はチャンネルに残る。チャンネルにいる誰もが対応を導き、仮説を試し、リアルタイムに調査でき、チャンネルの履歴が
監査可能性を高める。MCPアクセスを通じてClaudeは指標がベースラインに戻ったことを確認してスレッドで報告し、ポストモーテムを、
将来の調査が読めるバージョン管理されたlessonsファイルに書く。

Claude Tagが拾うのはインシデントだけではない。MCP経由でチケットにタグ付けされたり、チャンネルで尋ねられたりすると、Claudeは同じ
ようにトリアージする。小さく境界の明確な修正はレビューゲートを通ってPRとして届き、それより大きいものは段階1のための`intent.md`
として書き起こされる。この時点で、ループは自らを養い始める。

## むすび

モデルとハーネスは、組織がコードの作り方だけでなくソフトウェア開発ライフサイクル全体を変革できるところまで進んだ。人の判断を
中心に置いたまま、大企業のガバナンスと規制の要件に応えながら、である。

ループは回り続ける。人の判断はその上に留まる。

## 出典

[The AI-Native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook) — 著者 Louis Claxton、
寄稿 Jim Blackhurst、Will Steuk、Jamal Arif。2026-08-21 公開。
