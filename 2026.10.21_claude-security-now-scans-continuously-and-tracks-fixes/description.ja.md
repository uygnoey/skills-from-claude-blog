[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
Claude Enterprise 向けにパブリックベータで提供される Claude Security のアップデートです。誰かが
スキャンを開始するのを待つのではなく、コードの変更に合わせてリポジトリを追い続け、どの検出結果が
修正されたかを追跡し、チームから伝えられた環境情報をもとに何が重要かを判断します。

## どんなときに役立つか
- Enterprise のセキュリティチームが、スケジュール不要で常に最新のスキャンを求めるとき。
- 検出結果の優先度付けにチームの文脈(デプロイ方法、ポリシー、リスクポリシー)が必要なとき。
- エンジニアが Claude Code で検出結果をトリアージ・修正したり、既存ツールへ連携したいとき。

## 主なポイント
- 継続的モニタリング:詳細なベースラインスキャンの後、変更をリスクと複雑さに応じて定期的にスキャン。
  Claude GitHub アプリ(GitHub Enterprise Server を含む)または GitLab などの Git プロバイダーの
  アクセストークンで接続。1 つのプロジェクトに複数リポジトリを含め、サービス間の問題も検出。
- 修正の追跡:修正が反映されると(Claude Code でも他の手段でも)自動で修正済みになり、問題が再発
  すると自動で再オープン。
- プロジェクトごとのナレッジベースと、自動生成されチームが編集できる脅威モデル。以降のスキャンは
  これを使って何を報告し何を省くかを判断。
- 各検出結果に、脅威モデルに照らした深刻度と攻撃経路の説明(図を含む場合あり)。
- API(プロジェクト・検出結果の参照、解決/再オープン、リポジトリ管理)、ユーザー権限に限定される
  個人アクセストークン、新規検出の Webhook、Claude.ai と Claude Code の MCP コネクター。
- ロールベースのアクセス制御:プロジェクト閲覧、トリアージ、プロジェクト作成を分離。
- Claude Mythos を含む全モデルファミリーで動作し、Cyber Verification Program へのアクセスは不要。
  2 か月間、毎月 25,000 ドルの無料利用クレジット(2026 年 12 月 31 日までの利用分、詳細は Help Center)。

## 同梱リソース
- Skill: `continuous-security-scanning` — 有効化、ロール、プロジェクト、ナレッジベース、脅威モデル、
  トリアージ、修正追跡、連携(`references/feature-reference.md`、`templates/project-knowledge-base.md`)。

## 出典
- https://claude.com/resources/articles/claude-security-now-scans-continuously-and-tracks-fixes
