# Channel Playbook

| 渠道 | 主信源层 | 次信源层 | 工具优先级 | 题材侧重点 | 输出目标 |
|---|---|---|---|---|---|
| 即刻 | Reddit RSS、YouTube Channel RSS、官方博客快讯 | Hacker News、单条 X 镜像、科技媒体快讯 | `reddit_rss_fetch.py` → `youtube_source_fetch.py channel` → `official_blog_fetch.py` | 新鲜、单点突破、强判断、AI 编程 / Agent 工作流拐点 | 快速判断、短内容候选 |
| 微信公众号 | 官方博客、Anthropic/Cloudflare/Google 类长文、YouTube Channel RSS、YouTube transcript fallback | Reddit 深帖、工程师调研、Indie Hackers | `official_blog_fetch.py` → `youtube_source_fetch.py transcript` → `youtube_source_fetch.py channel` → `reddit_rss_fetch.py` | 权威案例、结构化深挖、方法论、生态变化、双事件共振 | 长文深挖候选 |

## Working Rules

### 即刻

- 优先近 72 小时新变化
- 优先一句强判断能成立的题
- 不追求信息面面俱到

### 微信公众号

- 必须至少能回答：是什么、为什么、意味着什么、怎么用
- 优先一手官方源 + 至少一条佐证源
- 不把快讯硬写成长文
