#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

from path_helpers import sibling_skill_path

ATOM_NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "yt": "http://www.youtube.com/xml/schemas/2015",
    "media": "http://search.yahoo.com/mrss/",
}
USER_AGENT = "Mozilla/5.0 ContentSourceGovernor/1.0"


def fetch_text(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def channel_feed(channel_id: str, limit: int) -> dict:
    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    xml_text = fetch_text(url)
    root = ET.fromstring(xml_text)
    title = (root.findtext("atom:title", default="", namespaces=ATOM_NS) or "").strip()
    items: list[dict] = []
    for entry in root.findall("atom:entry", ATOM_NS)[:limit]:
        video_id = (entry.findtext("yt:videoId", default="", namespaces=ATOM_NS) or "").strip()
        video_title = (entry.findtext("atom:title", default="", namespaces=ATOM_NS) or "").strip()
        published = (entry.findtext("atom:published", default="", namespaces=ATOM_NS) or "").strip()
        updated = (entry.findtext("atom:updated", default="", namespaces=ATOM_NS) or "").strip()
        description = (entry.findtext("media:group/media:description", default="", namespaces=ATOM_NS) or "").strip()
        items.append(
            {
                "video_id": video_id,
                "title": video_title,
                "published": published,
                "updated": updated,
                "link": f"https://www.youtube.com/watch?v={video_id}" if video_id else "",
                "description": description[:800],
            }
        )
    return {
        "ok": True,
        "source": "youtube_channel_rss",
        "channel_id": channel_id,
        "channel_title": title,
        "count": len(items),
        "items": items,
    }


def oembed(video_url: str) -> dict:
    encoded = urllib.parse.quote(video_url, safe="")
    url = f"https://www.youtube.com/oembed?url={encoded}&format=json"
    payload = json.loads(fetch_text(url))
    return {
        "title": payload.get("title"),
        "author_name": payload.get("author_name"),
        "author_url": payload.get("author_url"),
        "thumbnail_url": payload.get("thumbnail_url"),
        "provider_name": payload.get("provider_name"),
    }


def transcript(video: str) -> dict:
    # First try sibling generic youtube-transcript skill if present
    sibling = sibling_skill_path("youtube-transcript") / "scripts" / "get_transcript.py"
    python_candidates = [
        sibling_skill_path("youtube-transcript").parent.parent / "vendor" / "source-chain" / "venv" / "youtube-transcript" / "bin" / "python",
    ]
    for py in python_candidates:
        if py.exists() and sibling.exists():
            result = subprocess.run([str(py), str(sibling), video, "--timestamps"], text=True, capture_output=True)
            if result.returncode == 0:
                return {
                    "ok": True,
                    "source": "youtube_transcript",
                    "mode": "full_transcript",
                    "video": video,
                    "transcript_preview": result.stdout.splitlines()[:20],
                }
            error_text = (result.stderr or result.stdout).strip()[:3000]
            return {
                "ok": False,
                "source": "youtube_transcript",
                "mode": "oembed_fallback",
                "video": video,
                "error": error_text,
                "fallback": oembed(video),
            }
    return {
        "ok": False,
        "source": "youtube_transcript",
        "mode": "oembed_fallback",
        "video": video,
        "error": "No local transcript runtime found",
        "fallback": oembed(video),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch YouTube source signal.")
    sub = parser.add_subparsers(dest="command", required=True)

    ch = sub.add_parser("channel")
    ch.add_argument("channel_id")
    ch.add_argument("--limit", "-l", type=int, default=5)

    tr = sub.add_parser("transcript")
    tr.add_argument("video")

    args = parser.parse_args()
    if args.command == "channel":
        payload = channel_feed(args.channel_id, args.limit)
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0
    payload = transcript(args.video)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if payload.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
