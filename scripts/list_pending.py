#!/usr/bin/env python3
"""List pending blog URLs, with two-tier priority.

Priority:
  TIER 1 — NEW posts (published after the last batch run): newest → oldest
  TIER 2 — BACKLOG posts (older than the last batch run): oldest → newest
  TIER 3 — Posts only in sitemap.xml (no known date): alphabetical

"Last batch run" is read from state/processed.json -> meta.last_run_at.
If missing, TIER 1 is empty and everything dated goes into TIER 2.

Each output line:
    <url>\t<YYYY-MM-DD or "unknown">\t<tier: NEW|BACKLOG|UNKNOWN>

Usage:
    python scripts/list_pending.py [--limit N] [--urls-only]

Site layout note (2026-10): claude.com moved its blog from /blog/<slug> to
/resources/articles/<slug>. Old /blog/<slug> URLs now answer HTTP 308 to the
new path. Post identity is therefore tracked by slug, so state entries written
under the old URL form still count as processed.
"""
from __future__ import annotations

import argparse
import json
import re
import ssl
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE_FILE = ROOT / "state" / "processed.json"

SITEMAP_URL = "https://claude.com/sitemap.xml"
ARTICLE_URL_TMPL = "https://claude.com/resources/articles/{slug}"

# The /resources/articles index only embeds its most recent cards, so the
# category indexes are scraped too — together they cover the recent stream.
INDEX_URLS = [
    "https://claude.com/resources/articles",
    "https://claude.com/resources/product-announcements",
    "https://claude.com/resources/best-practices",
    "https://claude.com/resources/perspectives",
    "https://claude.com/resources/insights",
]
UA = {"User-Agent": "Mozilla/5.0"}

# English article URLs in the sitemap; locale-prefixed copies (/de/, /ja/, …)
# are skipped.
SITEMAP_ARTICLE_PATTERN = re.compile(
    r"https://claude\.com/resources/articles/([a-z0-9-]+)<"
)

# The index pages are React Server Component payloads: each card arrives as
# escaped JSON with a non-null `slug` (external links carry slug: null) and an
# ISO `date`.
CARD_PATTERN = re.compile(
    r'\\"_type\\":\\"blogPost\\",\\"slug\\":\\"([a-z0-9-]+)\\".{0,400}?'
    r'\\"date\\":\\"(\d{4}-\d{2}-\d{2})\\"'
)


class _AlsoFollow308(urllib.request.HTTPRedirectHandler):
    """Python 3.9's urllib does not follow HTTP 308; claude.com relies on it."""

    def http_error_308(self, req, fp, code, msg, headers):
        return self.http_error_301(req, fp, 301, msg, headers)


_OPENER = urllib.request.build_opener(_AlsoFollow308)


def _fetch(url: str) -> str:
    req = urllib.request.Request(url, headers=UA)
    try:
        with _OPENER.open(req, timeout=30) as resp:
            return resp.read().decode("utf-8", errors="ignore")
    except urllib.error.URLError as e:
        # Some hosts (notably python.org builds on macOS) ship without a system
        # CA bundle, so the default context cannot verify claude.com. Retry once
        # with certifi's bundle before giving up.
        if not isinstance(getattr(e, "reason", None), ssl.SSLCertVerificationError):
            raise
        try:
            import certifi
        except ImportError:
            raise e
        ctx = ssl.create_default_context(cafile=certifi.where())
        opener = urllib.request.build_opener(
            _AlsoFollow308, urllib.request.HTTPSHandler(context=ctx)
        )
        with opener.open(req, timeout=30) as resp:
            return resp.read().decode("utf-8", errors="ignore")


def load_state() -> dict:
    if not STATE_FILE.exists():
        return {"description": "", "meta": {}, "entries": {}}
    return json.loads(STATE_FILE.read_text(encoding="utf-8"))


def url_slug(url: str) -> str:
    return url.rstrip("/").rsplit("/", 1)[-1]


def fetch_sitemap_slugs() -> list[str]:
    body = _fetch(SITEMAP_URL)
    return sorted(set(SITEMAP_ARTICLE_PATTERN.findall(body)))


def fetch_index_slugs() -> list[tuple[str, str]]:
    """Return [(slug, 'YYYY-MM-DD'), ...] from the article/category indexes."""
    dated: dict[str, str] = {}
    errors: list[str] = []
    for url in INDEX_URLS:
        try:
            html = _fetch(url)
        except Exception as e:  # noqa: BLE001
            errors.append(f"{url}: {e}")
            continue
        for slug, date in CARD_PATTERN.findall(html):
            dated.setdefault(slug, date)
    if errors and not dated:
        print(f"# warn: index fetch failed: {'; '.join(errors)}", file=sys.stderr)
    elif errors:
        print(f"# warn: some indexes failed: {'; '.join(errors)}", file=sys.stderr)
    return sorted(dated.items(), key=lambda sd: sd[1], reverse=True)


def build_pending(state: dict) -> list[tuple[str, str, str]]:
    # Identity is the slug: state carries both the legacy /blog/<slug> keys and
    # the current /resources/articles/<slug> ones.
    processed: set[str] = {url_slug(u) for u in state.get("entries", {})}
    last_run = (state.get("meta", {}) or {}).get("last_run_at")  # "YYYY-MM-DD" or None

    index_entries = fetch_index_slugs()

    index_slugs: set[str] = set()
    new_tier: list[tuple[str, str]] = []        # published > last_run
    backlog_dated: list[tuple[str, str]] = []   # published <= last_run (or no last_run)

    for slug, date in index_entries:
        index_slugs.add(slug)
        if slug in processed:
            continue
        if last_run and date > last_run:
            new_tier.append((slug, date))
        else:
            backlog_dated.append((slug, date))

    # TIER 1: new posts — newest first
    new_tier.sort(key=lambda sd: sd[1], reverse=True)
    # TIER 2: backlog — oldest first (user preference)
    backlog_dated.sort(key=lambda sd: sd[1], reverse=False)

    pending: list[tuple[str, str, str]] = []
    for slug, date in new_tier:
        pending.append((ARTICLE_URL_TMPL.format(slug=slug), date, "NEW"))
    for slug, date in backlog_dated:
        pending.append((ARTICLE_URL_TMPL.format(slug=slug), date, "BACKLOG"))

    # TIER 3: sitemap-only leftovers (alphabetical). The indexes embed only
    # their most recent cards, so everything older shows up here without a
    # date; a missing sitemap is not an error.
    try:
        sitemap_slugs = fetch_sitemap_slugs()
    except Exception:  # noqa: BLE001
        sitemap_slugs = []
    for slug in sitemap_slugs:
        if slug in processed or slug in index_slugs:
            continue
        pending.append((ARTICLE_URL_TMPL.format(slug=slug), "unknown", "UNKNOWN"))

    return pending


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument(
        "--urls-only",
        action="store_true",
        help="Print URLs only (no date/tier columns)",
    )
    args = parser.parse_args()

    state = load_state()
    pending = build_pending(state)
    if args.limit:
        pending = pending[: args.limit]

    for url, date, tier in pending:
        if args.urls_only:
            print(url)
        else:
            print(f"{url}\t{date}\t{tier}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
