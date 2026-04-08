#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import urllib.request

USER_AGENT = "Mozilla/5.0 ContentSourceGovernor/1.0"


def probe(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            body = resp.read(400).decode("utf-8", errors="ignore")
            return {
                "url": url,
                "ok": True,
                "status": getattr(resp, "status", None),
                "snippet": body[:300].replace("\n", " "),
            }
    except Exception as exc:
        return {"url": url, "ok": False, "error": str(exc)}


def main() -> int:
    parser = argparse.ArgumentParser(description="Probe one or more source URLs.")
    parser.add_argument("urls", nargs="+")
    args = parser.parse_args()
    payload = {"results": [probe(url) for url in args.urls]}
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
