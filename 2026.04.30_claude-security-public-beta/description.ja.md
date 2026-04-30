[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# Claude Security がパブリックベータに

## この記事について

Anthropic が 2026 年 4 月 30 日に公開した発表では、これまで Claude Code Security と呼ばれていた Claude Security が、すべての Claude Enterprise 顧客向けにパブリックベータとして公開されました。本プロダクトは Claude Opus 4.7 を用いてコードベースをスキャンし、ターゲット型のパッチを生成して、発見事項を既存のセキュリティワークフローに流し込みます。Claude Team と Max の顧客向けは "coming soon"。記事では、スキャンの仕組み、研究プレビュー以降の変更点、提携テクノロジー/サービスパートナー、顧客のコメントが説明されています。

## どんなときに役立つか

- Claude Enterprise 顧客として、コードベース全体に Claude Security を展開するかどうか評価しているとき。
- スキャンの頻度、範囲(リポジトリ / ディレクトリ / ブランチ)、そして見つかった事項を Slack・Jira・監査システム・脆弱性管理プログラムへどのように流すかを計画する必要があるとき。
- 導入経路を比較したいとき:`claude.ai/security` で直接利用、パートナープラットフォーム(CrowdStrike、Microsoft Security、Palo Alto Networks、SentinelOne、Trend.ai、Wiz)に組み込み、あるいはサービスパートナー(Accenture、BCG、Deloitte、Infosys、PwC)と一緒に進める。
- エンジニアリングチームに発見事項を共有する前に、dismiss-with-reason と confidence rating のワークフローを理解しておきたいとき。

## 主なポイント

- Claude Security は Claude Enterprise 顧客向けのパブリックベータ。Claude Team と Max 顧客向けは近日提供予定。
- Claude Opus 4.7 ベースで、Claude.ai のサイドバーまたは `claude.ai/security` からアクセス — API 連携やカスタム agent の構築は不要。
- スキャン範囲はリポジトリ、特定のディレクトリ、またはブランチに限定可能。
- Claude はセキュリティリサーチャーのようにコードを推論します:既知シグネチャのパターンマッチではなく、ファイル・モジュール間の相互作用とデータフローを追跡します。
- 各発見事項には confidence rating、深刻度、想定される影響、再現手順、そして Claude Code on the Web で開けるターゲット型パッチが含まれます。
- 限定プレビュー以降の改善:スケジュールスキャン、ディレクトリ単位のターゲットスキャン、理由を明記した dismiss、CSV/Markdown エクスポート、Slack・Jira などへの webhook。
- Opus 4.7 を組み込むテクノロジーパートナー:CrowdStrike、Microsoft Security、Palo Alto Networks、SentinelOne、Trend.ai、Wiz。
- サービスパートナー:Accenture、BCG、Deloitte、Infosys、PwC。
- 記事に登場する顧客コメント:DoorDash のほか、Staff Product Security Engineer、Information Security Officer、Head of Security 二名。
- Claude Opus 4.7 には新しい cyber safeguard があり、正当な業務がそれをトリガーする可能性のある組織は Cyber Verification Program に参加できます。

## 同梱リソース

- Skill: `skills/security-public-beta-rollout-guide/SKILL.md` — Claude Security をいつ使うか、スキャン範囲の指定、発見事項の解釈、そして直接 / パートナープラットフォーム / サービスパートナーのうちどの導入経路が自組織に合うか。
- リファレンス: `skills/security-public-beta-rollout-guide/references/features-and-partners-from-post.md` — 機能、スキャンワークフロー、パートナー、顧客コメントを記事に忠実に整理したもの。
- 例: `skills/security-public-beta-rollout-guide/examples/scan-and-triage-workflows.md` — 記事に基づいたスコーピング・スケジューリング・トリアージのワークフロー例。

## 出典

Claude Security is now in public beta — Anthropic、2026 年 4 月 30 日: <https://claude.com/blog/claude-security-public-beta>
