---
name: wechat-topic-fetch-tool
description: |
  Govern content research sources, tool routing, and source-memory for topic discovery. Use this skill when Claude needs to choose or standardize which official blogs, Reddit sources, YouTube sources, sibling skills, CLI tools, or local scripts should be used for topic research, trend monitoring, first-hand source discovery, or channel-specific sourcing, especially for 即刻 and 微信公众号. It should also be used when Claude needs to evaluate new source tools from GitHub, ClawHub, or skills.sh, or when it needs to read/write source experience memory before and after research.
---

# Content Source Governor

## Overview

Use this skill to decide **which source to use, which tool to call, and how to fallback** before doing content research.

This skill is a governor, not a generic crawler. It standardizes:

- source selection
- tool routing
- channel strategy
- learned source memory

## Persistent Memory

Before each execution, read:

- `data/memory.md`
- `references/channel-playbook.md`

After each meaningful execution:

1. update `data/memory.md` with new high-signal / low-signal patterns
2. record newly validated or newly blocked sources
3. merge repeated lessons instead of appending noisy logs

For memory rules, see [references/memory-schema.md](references/memory-schema.md).

## Path Rules

Always derive paths relative to this skill, never hardcode machine-specific paths in the workflow itself.

### Shell

```bash
SKILL_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"
SCRIPTS_DIR="$SKILL_ROOT/scripts"
SKILLS_ROOT="$(cd "$SKILL_ROOT/.." && pwd)"
```

### Python

```python
from pathlib import Path
SKILL_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = SKILL_ROOT / "scripts"
SKILLS_ROOT = SKILL_ROOT.parent
```

This allows the skill to move together with sibling skills and remain portable.

## Workflow

### 1. Read memory first

Always start by reading:

- `data/memory.md`
- `references/channel-playbook.md`

If the task is source discovery rather than immediate research, also read:

- `references/discovery-sources.md`

### 2. Decide the channel

Choose one of:

- `即刻`
- `微信公众号`
- `通用监控`

Then use [references/channel-playbook.md](references/channel-playbook.md) to determine:

- main source layers
- secondary source layers
- output goal

### 3. Choose the source

Use [references/source-catalog.md](references/source-catalog.md) as the source entry table.

Do not decide from memory alone.

### 4. Choose the tool

Use [references/tool-catalog.md](references/tool-catalog.md) as the routing table.

Tool priority rules:

- official blogs / official pages
  - use `scripts/official_blog_fetch.py`
- Reddit
  - use `scripts/reddit_rss_fetch.py` first
  - only try sibling Reddit skills if RSS is insufficient
- YouTube
  - use `scripts/youtube_source_fetch.py channel` first
  - only request transcript when long-form analysis actually needs it
- source debugging / unknown source
  - use `scripts/source_probe.py`

### 5. If you need a new tool

Search in this order:

1. GitHub
2. skills.sh
3. ClawHub

Use [references/discovery-sources.md](references/discovery-sources.md) for the selection criteria.

### 6. Use the unified router when helpful

For repeatable execution, prefer:

```bash
python3 scripts/source_router.py official <url>
python3 scripts/source_router.py reddit <subreddit> --limit 5
python3 scripts/source_router.py youtube-channel <channel_id> --limit 5
python3 scripts/source_router.py youtube-transcript <video_url>
python3 scripts/source_router.py probe <url1> <url2>
```

### 7. Update memory after execution

Update `data/memory.md` when you discover:

- a high-signal pattern
- a low-signal pattern
- a source that is newly validated
- a source that is newly blocked
- a duplicate-topic pattern worth avoiding

## References

- Source entry table: [references/source-catalog.md](references/source-catalog.md)
- Tool routing table: [references/tool-catalog.md](references/tool-catalog.md)
- Discovery platforms: [references/discovery-sources.md](references/discovery-sources.md)
- Channel strategy: [references/channel-playbook.md](references/channel-playbook.md)
- Memory rules: [references/memory-schema.md](references/memory-schema.md)
- Example checklist: [examples/source-checklist.md](examples/source-checklist.md)

## Output Rules

When using this skill in a real task, always make the result explicit:

- chosen channel
- chosen sources
- chosen tools
- fallback used or not
- why these sources are relevant

If a source is blocked, say it plainly and route to the fallback instead of pretending it worked.
