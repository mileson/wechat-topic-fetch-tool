# WeChat Topic Fetch Tool

> A content source governor for discovering, fetching, and routing AI/tech news from official blogs, Reddit, YouTube, and more — built for content creators on Jike and WeChat Official Accounts.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-green.svg)]()

[中文文档](README_CN.md)

[Features](#readme-section-1) · [Quick Start](#readme-section-2) · [How It Works](#readme-section-3) · [Tech Stack](#readme-section-4) · [Project Structure](#readme-section-5) · [Contributing](#readme-section-6) · [License](#readme-section-7)

<a id="readme-section-1"></a>

## Features

- **Unified Router** — One CLI entry point dispatches to official blog fetchers, Reddit RSS, YouTube channels, and more
- **Source Memory** — Learns high-signal and low-signal patterns across sessions, persisted in structured memory
- **Channel Strategy** — Tailored source selection and content depth for Jike (quick hits) vs. WeChat (deep long-form)
- **Fallback Chains** — Graceful degradation: `urllib` → `curl` → sibling skill → manual probe
- **Probe Before Commit** — Lightweight URL tester validates new sources before full fetches
- **Zero Dependencies** — Pure Python standard library, no `pip install` needed

<a id="readme-section-2"></a>

## Quick Start

### Prerequisites

- Python 3.10 or later
- `curl` (optional, used as HTTP fallback)

### Installation

```bash
# Clone the repo
git clone https://github.com/Mileson07/wechat-topic-fetch-tool.git
cd wechat-topic-fetch-tool
```

Or install with pipx:

```bash
pipx install git+https://github.com/Mileson07/wechat-topic-fetch-tool.git
```

### Usage

```bash
# Fetch from a named official blog (e.g., OpenAI, Anthropic, Cursor)
python3 scripts/source_router.py official openai_developers_blog

# Fetch from an arbitrary URL
python3 scripts/source_router.py official https://example.com/blog

# Fetch Reddit subreddit RSS
python3 scripts/source_router.py reddit MachineLearning --limit 5

# Fetch YouTube channel videos
python3 scripts/source_router.py youtube-channel <channel_id> --limit 5

# Fetch YouTube video transcript
python3 scripts/source_router.py youtube-transcript <video_url>

# Probe URLs before fetching
python3 scripts/source_router.py probe https://example.com https://another.com
```

<a id="readme-section-3"></a>

## How It Works

1. **Read memory** — Load accumulated source experience from `data/memory.md`
2. **Choose channel** — Jike (fast, punchy) or WeChat (deep, structured)
3. **Select sources** — Consult `references/source-catalog.md` for priority-ranked sources
4. **Route to tool** — Use `references/tool-catalog.md` to pick the right fetcher with fallbacks
5. **Fetch & parse** — Execute via `source_router.py` or individual scripts
6. **Update memory** — Record high/low signal patterns, validated/blocked sources

<a id="readme-section-4"></a>

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.10+ |
| HTTP Client | `urllib.request` (with `curl` fallback) |
| RSS Parsing | `xml.etree.ElementTree` |
| CLI | `argparse` |
| External (optional) | `curl`, sibling skills |

<a id="readme-section-5"></a>

## Project Structure

```
wechat-topic-fetch-tool/
├── scripts/
│   ├── source_router.py         # Unified CLI entry point
│   ├── official_blog_fetch.py   # Official blog/page fetcher
│   ├── reddit_rss_fetch.py      # Reddit RSS Atom feed parser
│   ├── youtube_source_fetch.py  # YouTube channel & transcript fetcher
│   ├── source_probe.py          # Lightweight URL prober
│   └── path_helpers.py          # Portable path constants
├── references/
│   ├── source-catalog.md        # Master source registry with priorities
│   ├── tool-catalog.md          # Tool routing table with fallback chains
│   ├── channel-playbook.md      # Channel-specific content strategy
│   ├── source-targets.json      # Named blog/website target definitions
│   ├── discovery-sources.md     # Guide for finding new source tools
│   └── memory-schema.md         # Rules for source memory management
├── data/
│   └── memory.md                # Accumulated source experience memory
├── examples/
│   └── source-checklist.md      # Source evaluation checklist
├── SKILL.md                     # Skill definition (Claude Code / Agent)
├── pyproject.toml               # Package metadata
├── LICENSE                      # MIT License
└── .gitignore
```

<a id="readme-section-6"></a>

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

<a id="readme-section-7"></a>

## License

This project is licensed under the [MIT License](LICENSE).

<a id="readme-section-8"></a>

## Author

- X: [Mileson07](https://x.com/Mileson07)
- Xiaohongshu: [超级峰](https://xhslink.com/m/4LnJ9aB1f97)
- Douyin: [超级峰](https://v.douyin.com/rH645q7trd8/)
