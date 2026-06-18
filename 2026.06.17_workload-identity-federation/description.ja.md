[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
この記事は、Claude Platform における Workload Identity Federation（WIF）の一般提供（GA）を発表するものです。

## どんなときに役立つか
CI、クラウドサービス、Kubernetes ジョブなどの「ワークロード」が、長期の静的 API キーを管理せずに Claude API を呼び出したいときに役立ちます。

## 主なポイント
- WIF は静的 API キーを、リクエスト時に発行される短命かつスコープ制限付きの認証情報に置き換えます。
- WIF は OIDC に準拠した任意の ID プロバイダで利用でき、Claude API の全エンドポイント（ファーストパーティ SDK や Claude Code 経由を含む）をカバーします。
- Claude Platform ではサービスアカウントが導入され、ワークロードごとに固有のアイデンティティ、ロール、監査証跡を持てます。
- フェデレーションルールが、外部アイデンティティ（OIDC トークンのクレーム）を Claude のサービスアカウントにバインドします。
- API キーと WIF は併用できるため、ワークロードを段階的に移行できます。

## 同梱リソース
- Agent Skill: WIF のサービスアカウントとフェデレーションルールを構成するための概念チェックリスト。

## 出典
- https://claude.com/blog/workload-identity-federation
