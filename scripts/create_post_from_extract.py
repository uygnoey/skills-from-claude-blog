#!/usr/bin/env python3
"""Create a new post folder (blog_slug/) with required artifacts.

This repo intentionally keeps automation minimal. This helper is created by the cron task
when no generator script exists.

Inputs: a JSON file with extracted fields.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def write_text(path: Path, content: str) -> None:
    ensure_dir(path.parent)
    path.write_text(content, encoding="utf-8")


def lang_switcher(current: str) -> str:
    labels = {
        "en": "English",
        "ko": "한국어",
        "es": "Español",
        "ja": "日本語",
    }
    files = {
        "en": "./description.en.md",
        "ko": "./description.ko.md",
        "es": "./description.es.md",
        "ja": "./description.ja.md",
    }
    parts = []
    for code in ["en", "ko", "es", "ja"]:
        if code == current:
            parts.append(f"**{labels[code]}**")
        else:
            parts.append(f"[{labels[code]}]({files[code]})")
    return " · ".join(parts)


def guide_switcher(current: str, stem: str) -> str:
    labels = {
        "en": "English",
        "ko": "한국어",
        "es": "Español",
        "ja": "日本語",
    }
    files = {
        "en": f"./{stem}.en.md",
        "ko": f"./{stem}.ko.md",
        "es": f"./{stem}.es.md",
        "ja": f"./{stem}.ja.md",
    }
    parts = []
    for code in ["en", "ko", "es", "ja"]:
        if code == current:
            parts.append(f"**{labels[code]}**")
        else:
            parts.append(f"[{labels[code]}]({files[code]})")
    return " · ".join(parts)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=str(Path(__file__).resolve().parents[1]))
    ap.add_argument("--json", required=True)
    args = ap.parse_args()

    repo = Path(args.repo)
    data = json.loads(Path(args.json).read_text(encoding="utf-8"))

    blog_slug = data["blog_slug"]
    base = repo / blog_slug

    # source.json
    write_text(
        base / "source.json",
        json.dumps(
            {
                "url": data["url"],
                "title": data["title"],
                "published_date": data["published_date"],
                "blog_slug": blog_slug,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
    )

    # descriptions in 4 languages
    for lang, sections in data["descriptions"].items():
        content = (
            f"{lang_switcher(lang)}\n\n"
            f"# {data['title']}\n\n"
            f"## {sections['what_heading']}\n\n{sections['what']}\n\n"
            f"## {sections['when_heading']}\n\n{sections['when']}\n\n"
            f"## {sections['key_heading']}\n\n{sections['key']}\n\n"
            f"## {sections['bundle_heading']}\n\n{sections['bundle']}\n\n"
            f"## {sections['source_heading']}\n\n- {data['url']}\n"
        )
        write_text(base / f"description.{lang}.md", content)

    # Skill
    skill = data.get("skill")
    if skill:
        skill_dir = base / "skills" / skill["name"]
        skill_md = skill_dir / "SKILL.md"
        write_text(skill_md, skill["skill_md"])
        for rel_path, file_content in skill.get("companion_files", {}).items():
            write_text(skill_dir / rel_path, file_content)

    # Guide
    guide = data.get("guide")
    if guide:
        ensure_dir(base / "guides")
        stem = guide["stem"]
        for lang, md in guide["files"].items():
            write_text(
                base / "guides" / f"{stem}.{lang}.md",
                f"{guide_switcher(lang, stem)}\n\n" + md,
            )

    # Agents
    agents = data.get("agents", [])
    for agent in agents:
        write_text(base / "agents" / f"{agent['name']}.md", agent["md"])
        for rel_path, file_content in agent.get("companion_files", {}).items():
            write_text(base / "agents" / rel_path, file_content)


if __name__ == "__main__":
    main()
