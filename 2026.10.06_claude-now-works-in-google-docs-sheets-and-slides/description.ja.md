[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
Claude for Google Workspace がすべての有料 Claude プランでパブリックベータになったという発表です。
開いている Google ドキュメント、スプレッドシート、スライドの横に Claude のサイドバーが開き、ファイルを
読み、選択範囲を把握し、直接編集できます。新しい Google Docs・Sheets・Slides コネクタ(ベータ)により、
Claude のチャットから Google ファイルを作成・編集することもできます。

## どんなときに役立つか
- すでに開いている Google ファイルの中で、Claude に編集・分析・作成を任せたいとき。
- Claude から始めて新しいドキュメント・シート・デッキを作る、または複数ファイルにまたがって作業するとき。
- 管理者がドメイン全体やグループ単位の展開を計画するとき。

## 主なポイント
- ドキュメント: 小さな修正はその場で反映し、大きな書き直しは適用・却下できる提案カードとして返します。
- スプレッドシート: 数式、ピボットテーブル、ネイティブグラフ、新しいタブ、範囲に Python を実行して
  データを整形・結合し、結果を書き戻します。
- スライド: デッキのレイアウトとテーマでスライドを作り、重なりやはみ出した要素、読みにくいテキストを
  確認します。
- 編集モード: "Ask before edits"(既定、変更ごとに承認カード)または "Accept all edits"。
- サイドバーも通常の Claude と同じモデル・コネクタ・スキルを使い、エンタープライズ管理(Compliance API、
  顧客管理の暗号鍵、OpenTelemetry 監査エクスポート)も適用されます。
- ファイルへのアクセスは既存の Google 共有権限に従います。
- 設定: Google Workspace Marketplace からインストールし、拡張機能 > Claude > Open Claude。管理者は
  Google 管理コンソールからドメインやグループに配布でき、Team・Enterprise プランではオーナーまたは
  プライマリオーナーが先にコネクタを有効にする必要があります。

## 同梱リソース
- スキル: `google-workspace-editing` — アドオンとコネクタの使い分け、編集モード、アプリ別の作業パターン。
  作業例は `examples/task-prompts.md`。
- ガイド: `google-workspace-rollout`(en/ko/es/ja)— 個人の設定と組織での導入。

## 出典
- https://claude.com/resources/articles/claude-now-works-in-google-docs-sheets-and-slides
