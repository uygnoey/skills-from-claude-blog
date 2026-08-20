[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
**Compliance API が Claude Cowork と Claude Code もカバーするようになった**という発表です。ベータ版で、対象は Claude Enterprise のお客様です。Cowork はデスクトップ・ウェブ・モバイルで、Claude Code は CLI とデスクトップアプリでカバーされます。両製品とも同じ Compliance API インターフェースから読み出せるため、コンプライアンス／セキュリティチームはセッションのコンテンツとメタデータを 2 か所ではなく 1 か所から取得できます。

記事はセッションレコードに含まれる内容を列挙しています。プロンプトと応答、ツール呼び出しのコンテンツ（ウェブおよび Model Context Protocol）、そしてトランスクリプトのテキストとして取り込まれるスキルとアーティファクトです。付随するメタデータは、検証済みのユーザー ID とメールアドレス、組織 ID、セッション ID とメッセージごとの ID、タイムスタンプです。また、今回のベータが**対象外**とする範囲を明示し、新たなインフラが不要であることも確認しています。カバレッジは Compliance API に含まれ、既存の Compliance Access Key をそのまま使います。すでに OpenTelemetry データをエクスポートしている組織は、両方のシステムを並行して運用し続けられます。

## どんなときに役立つか
- コンプライアンス／セキュリティチームが、すでに Compliance API で使っている監査フィードに Cowork と Claude Code のセッションもまとめたいとき。
- 保持（リテンション）、eDiscovery、調査プログラムの範囲を決めるにあたり、現時点でどのサーフェスが対象になるかを正確に把握したいとき。
- セッション単位・メッセージ単位でどのフィールドが取得されるかを監査人やレビュアーに説明する必要があるとき。
- Compliance API と並行して OpenTelemetry のエクスポートを維持するかどうかを判断するとき。

## 主なポイント
- **ベータ、Claude Enterprise 限定。** カバレッジは本日から利用可能で、Compliance API に含まれます。別途の権利は不要で、既存の Compliance Access Key を使います。
- **統一インターフェース。** Cowork と Claude Code のセッションコンテンツとメタデータを、同じ Compliance API インターフェースから取得します。
- **対象サーフェス。** Cowork はデスクトップ・ウェブ・モバイル、Claude Code は CLI とデスクトップアプリ。
- **取得されるセッションコンテンツ。** プロンプトと応答、ツール呼び出しのコンテンツ（ウェブおよび Model Context Protocol）、トランスクリプトのテキストとして取り込まれるスキルとアーティファクト。
- **取得されるセッションメタデータ。** 検証済みユーザー ID とメールアドレス、組織 ID、セッション ID とメッセージごとの ID、タイムスタンプ。
- **ベータの対象外。** ウェブ版の Claude Code、Claude Platform 経由の Claude Code、そして Amazon Bedrock・Google Cloud Vertex AI・Microsoft Foundry 上のセッション。
- **OpenTelemetry と共存。** すでに OTel データをエクスポートしている組織は、追加のインフラ要件なしに両システムを同時に運用し続けられます。

## 同梱リソース
- `skills/compliance-session-coverage/SKILL.md` — Cowork と Claude Code をまたぐ Compliance API 取得の範囲を定め、依拠する前にカバレッジを確認します。
- `skills/compliance-session-coverage/references/coverage-matrix.md` — 対象サーフェス、対象外サーフェス、記事に明記された取得フィールドの一覧。
- `skills/compliance-session-coverage/templates/coverage-verification-checklist.md` — 監査や調査の前に範囲を確定するための記入式チェックリスト。

## 出典
- https://claude.com/blog/compliance-api-cowork-and-claude-code
