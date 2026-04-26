[English](./skills-deployment-paths.en.md) · [한국어](./skills-deployment-paths.ko.md) · [Español](./skills-deployment-paths.es.md) · **日本語**

## このガイドについて
このガイドは、元記事で説明されている Claude スキルの主要な導入／管理経路（Claude Apps、Claude Code、API）と、任意の組織単位プロビジョニングを要約します。

## 展開経路
- **Claude Apps**: スキルディレクトリを参照し、Settings > Capabilities > Skills から有効化します。
- **Claude Code**: プラグインディレクトリからスキルをインストールするか、スキルフォルダをリポジトリにチェックインします。
- **API**: `/v1/skills` エンドポイントでスキルを利用します（プラットフォーム文書参照）。

## 組織単位の管理
- 管理者（Team/Enterprise）は管理設定からスキルを中央プロビジョニングできます。
- 一部のスキルでは Code Execution と File Creation の有効化が必要な場合があります。

## 出典
- https://claude.com/blog/organization-skills-and-directory
