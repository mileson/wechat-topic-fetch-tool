#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import urllib.request
import xml.etree.ElementTree as ET

ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}
USER_AGENT = "Mozilla/5.0 ContentSourceGovernor/1.0"


def fetch_text(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def parse_feed(xml_text: str, limit: int) -> list[dict]:
    root = ET.fromstring(xml_text)
    items: list[dict] = []
    for entry in root.findall("atom:entry", ATOM_NS)[:limit]:
        title = (entry.findtext("atom:title", default="", namespaces=ATOM_NS) or "").strip()
        link_node = entry.find("atom:link", ATOM_NS)
        link = link_node.attrib.get("href", "").strip() if link_node is not None else ""
        published = (entry.findtext("atom:published", default="", namespaces=ATOM_NS) or "").strip()
        updated = (entry.findtext("atom:updated", default="", namespaces=ATOM_NS) or "").strip()
        author = (entry.findtext("atom:author/atom:name", default="", namespaces=ATOM_NS) or "").strip()
        content = (entry.findtext("atom:content", default="", namespaces=ATOM_NS) or "").strip()
        items.append(
            {
                "title": title,
                "link": link,
                "published": published,
                "updated": updated,
                "author": author,
                "summary_snippet": content[:500],
            }
        )
    return items


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch Reddit subreddit feed via RSS.")
    parser.add_argument("subreddit", help="Subreddit name without r/")
    parser.add_argument("--limit", "-l", type=int, default=5)
    args = parser.parse_args()

    url = f"https://www.reddit.com/r/{args.subreddit}/.rss"
    try:
        xml_text = fetch_text(url)
        items = parse_feed(xml_text, args.limit)
        payload = {
            "ok": True,
            "source": "reddit_rss",
            "subreddit": args.subreddit,
            "url": url,
            "count": len(items),
            "items": items,
        }
    except Exception as exc:
        payload = {"ok": False, "source": "reddit_rss", "url": url, "error": str(exc)}
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 1

    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
