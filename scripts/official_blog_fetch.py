#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
import urllib.request
from pathlib import Path

USER_AGENT = "Mozilla/5.0 ContentSourceGovernor/1.0"
TARGETS_PATH = Path(__file__).resolve().parents[1] / "references" / "source-targets.json"


def fetch_text(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.read().decode("utf-8", errors="ignore")
    except Exception:
        result = subprocess.run(
            ["curl", "-L", "-A", USER_AGENT, "--max-time", "30", url],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout
        raise


def pick(pattern: str, text: str) -> str:
    match = re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else ""


def load_targets() -> dict:
    return json.loads(TARGETS_PATH.read_text())


def resolve_target(raw: str) -> tuple[str, str]:
    targets = load_targets()
    if raw in targets:
        target = targets[raw]
        return raw, target["url"]
    return "custom", raw


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch official blog / news page summary.")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list-targets", help="List built-in source targets.")
    fetch = sub.add_parser("fetch", help="Fetch a built-in target key or raw URL.")
    fetch.add_argument("target_or_url")
    args = parser.parse_args()

    if args.command == "list-targets":
        print(json.dumps(load_targets(), ensure_ascii=False, indent=2))
        return 0

    target_key, url = resolve_target(args.target_or_url)
    try:
        html = fetch_text(url)
        payload = {
            "ok": True,
            "target": target_key,
            "url": url,
            "title": pick(r"<title>(.*?)</title>", html),
            "meta_description": pick(r'<meta[^>]+name=[\"\\\']description[\"\\\'][^>]+content=[\"\\\'](.*?)[\"\\\']', html),
            "og_title": pick(r'<meta[^>]+property=[\"\\\']og:title[\"\\\'][^>]+content=[\"\\\'](.*?)[\"\\\']', html),
            "og_description": pick(r'<meta[^>]+property=[\"\\\']og:description[\"\\\'][^>]+content=[\"\\\'](.*?)[\"\\\']', html),
            "snippet": re.sub(r"\\s+", " ", html[:1200]).strip(),
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        print(json.dumps({"ok": False, "target": target_key, "url": url, "error": str(exc)}, ensure_ascii=False, indent=2))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
