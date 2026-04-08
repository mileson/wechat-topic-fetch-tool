#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys

from path_helpers import SCRIPTS_DIR


def run(cmd: list[str]) -> int:
    result = subprocess.run(cmd, text=True, capture_output=True)
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr:
        print(result.stderr.strip(), file=sys.stderr)
    return result.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description="Unified source routing entrypoint.")
    sub = parser.add_subparsers(dest="command", required=True)

    blog = sub.add_parser("official")
    blog.add_argument("target_or_url")

    sub.add_parser("official-list")

    reddit = sub.add_parser("reddit")
    reddit.add_argument("subreddit")
    reddit.add_argument("--limit", "-l", default="5")

    yt_channel = sub.add_parser("youtube-channel")
    yt_channel.add_argument("channel_id")
    yt_channel.add_argument("--limit", "-l", default="5")

    yt_transcript = sub.add_parser("youtube-transcript")
    yt_transcript.add_argument("video")

    probe = sub.add_parser("probe")
    probe.add_argument("urls", nargs="+")

    args = parser.parse_args()

    if args.command == "official":
        return run([sys.executable, str(SCRIPTS_DIR / "official_blog_fetch.py"), "fetch", args.target_or_url])
    if args.command == "official-list":
        return run([sys.executable, str(SCRIPTS_DIR / "official_blog_fetch.py"), "list-targets"])
    if args.command == "reddit":
        return run([sys.executable, str(SCRIPTS_DIR / "reddit_rss_fetch.py"), args.subreddit, "--limit", args.limit])
    if args.command == "youtube-channel":
        return run([sys.executable, str(SCRIPTS_DIR / "youtube_source_fetch.py"), "channel", args.channel_id, "--limit", args.limit])
    if args.command == "youtube-transcript":
        return run([sys.executable, str(SCRIPTS_DIR / "youtube_source_fetch.py"), "transcript", args.video])
    return run([sys.executable, str(SCRIPTS_DIR / "source_probe.py"), *args.urls])


if __name__ == "__main__":
    raise SystemExit(main())
