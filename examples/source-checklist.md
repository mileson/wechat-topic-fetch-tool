# Source Checklist Example

## Before Research

1. Read `data/memory.md`
2. Read `references/channel-playbook.md`
3. Read `references/source-catalog.md`
4. Read `references/tool-catalog.md`

## Pick Sources

- If target is **official blog / official page**
  - run `official_blog_fetch.py list-targets`
  - then run `official_blog_fetch.py fetch <target_or_url>`
- If target is **Reddit**
  - run `reddit_rss_fetch.py`
  - only try sibling Reddit skills when RSS is insufficient
- If target is **YouTube**
  - run `youtube_source_fetch.py channel`
  - only try transcript when long-form analysis needs it

## After Research

1. Keep only sources that help the current channel goal
2. Note high-signal and low-signal patterns
3. Update `data/memory.md`
