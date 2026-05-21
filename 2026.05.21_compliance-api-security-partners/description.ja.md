[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# Claude がより多くのセキュリティ・コンプライアンスツールと連携

## この記事について

2026 年 5 月 21 日に Anthropic が公開した、**Claude Compliance API** をベースとした **28 件の新しいセキュリティ/コンプライアンスインテグレーション**の発表記事です。IT・セキュリティチームが自社スタックの他アプリと同じやり方で Claude Enterprise と Claude Platform 全体を統制できるようになります。本文は API が何を公開するか、カテゴリ別の通用範囲、28 のローンチパートナー、そして顧客とパートナーそれぞれの次のステップを整理します。

## どんなときに役立つか

- IT/セキュリティチームが、既存の DLP・SASE・SIEM・アイデンティティ・eDiscovery・AI-SPM・AI オブザーバビリティスタックに Claude をどう接続するか検討するとき。
- 独自インテグレーションを作るのではなく、現行のセキュリティ/コンプライアンスベンダー側で Claude カバレッジを拡張するか判断するとき。
- セキュリティ/コンプライアンスプラットフォームベンダーが、インテグレーションネットワークへの参加を判断するとき。
- Claude Enterprise/Platform のロールアウトに対する CISO/CRO のサインオフ用ガバナンスストーリーをまとめるとき。

## 主なポイント

- 28 のインテグレーションすべての基盤が Claude Compliance API。
- API がエンタープライズチームに対してプログラマブルに公開する **2 種類のデータ**:
  - **Claude Enterprise の会話コンテンツ** — チャット、アップロードファイル、プロジェクト。他のワークプレイスアプリと同じセキュリティ・モニタリング・DLP ポリシーを Claude にも適用可能。
  - **Claude Enterprise と Claude Platform 横断のアクティビティイベント** — ユーザーログイン、管理者アクション、構成変更。利用状況を統合ビューで把握。
- 28 件のローンチインテグレーションの **カバレッジカテゴリ**: DLP、SASE、データセキュリティ、SIEM/セキュリティオペレーション、アイデンティティ、eDiscovery、AI セキュリティポスチャマネジメント、AI オブザーバビリティ/テレメトリ。
- **28 のローンチパートナー**: Cloudflare、Cribl、CrowdStrike、Cyera、Datadog、Forcepoint、Fortinet、Geordie AI、IBM Guardium、Microsoft Purview、Mimecast、Netskope、Okta、Palo Alto Networks、Proofpoint、Relativity、ReliaQuest、Rubrik、SailPoint、Smarsh、Snyk、Sumo Logic、Tenable、Theta Lake、Trellix、Varonis、Wiz(現 Google Cloud 傘下)、Zscaler。
- **顧客のオンボーディング** — Claude インスタンスをパートナープラットフォームへ connect/configure すると、既存のダッシュボードとアラートワークフローへデータが流れる。
- **パートナーのオンボーディング** — Compliance API インテグレーションを構築済みのセキュリティ/コンプライアンス/IT プラットフォームはネットワーク参加申請が可能。

## 同梱リソース

- `skills/governance-via-compliance-api/SKILL.md` — 既存スタックに合う Compliance API インテグレーションを選び、Claude のガバナンスを設計するためのプレイブック。
- `skills/governance-via-compliance-api/references/launch-partners-by-category.md` — 本文カテゴリ別に整理したパートナーカタログ。
- `skills/governance-via-compliance-api/examples/dlp-and-siem-wiring.md` — Claude Enterprise/Platform 横断で DLP/SIEM カバレッジを Compliance API 経由で繋いだワーキング例。

## 出典

- [Claude now works with more security and compliance tools](https://claude.com/blog/compliance-api-security-partners) (Anthropic ブログ、2026 年 5 月 21 日)
