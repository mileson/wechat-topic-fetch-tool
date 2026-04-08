# Source Catalog

| 来源层级 | 来源名 | URL / 标识 | 信源类型 | 抓取入口 | 主要特征 | 优先级 | 备注 |
|---|---|---|---|---|---|---|---|
| 特定目标源 | Cursor Blog | `https://cursor.com/cn/blog` | 官方博客 | `official_blog_fetch.py` | AI 编程工具版本更新、产品策略变化 | P0 | 适合跟踪 Cursor、IDE、工作流变化 |
| 特定目标源 | Claude Blog | `https://claude.com/blog` | 官方博客 | `official_blog_fetch.py` | Claude / Agent / 产品发布与案例 | P0 | 适合产品、案例、方法论 |
| 特定目标源 | OpenAI Developers Blog | `https://developers.openai.com/blog` | 官方博客 | `official_blog_fetch.py` | API、开发者工作流、产品能力变化 | P0 | 高价值，但远端直抓可能遇到 challenge |
| 特定目标源 | Google AI Blog | `https://blog.google/innovation-and-ai/technology/ai/` | 官方博客 | `official_blog_fetch.py` | 模型、产品、生态变化 | P0 | 适合“范式变化”类选题 |
| 特定目标源 | Indie Hackers Stories | `https://www.indiehackers.com/stories` | 创业案例站点 | `official_blog_fetch.py` | 独立开发者案例、增长、产品故事 | P1 | 更适合深挖案例 |
| 官方一手源 | Anthropic News | `https://www.anthropic.com/news` | 官方新闻页 | `official_blog_fetch.py` | 官方长文、研究和产品发布 | P0 | 当前已知可直抓 |
| 官方一手源 | Anthropic Research | `https://www.anthropic.com/research` | 官方研究页 | `official_blog_fetch.py` | 研究报告、方法论、案例长文 | P0 | 当前已知可直抓，适合公众号深挖 |
| 官方一手源 | Cloudflare Blog | `https://blog.cloudflare.com/` | 官方博客 | `official_blog_fetch.py` | 基础设施、AI 流量、工程实践 | P0 | 当前已知可直抓 |
| 官方一手源 | GitHub Blog | `https://github.blog/` | 官方博客 | `official_blog_fetch.py` | Copilot、开发者工具、工作流升级 | P1 | 适合开发者生态类选题 |
| 官方一手源 | Vercel Blog | `https://vercel.com/blog` | 官方博客 | `official_blog_fetch.py` | AI 应用工程化与 Agent 工作流 | P1 | 适合公众号深挖 |
| 社区一手源 | Reddit RSS | `https://www.reddit.com/r/<subreddit>/.rss` | 社区 RSS | `reddit_rss_fetch.py` | 热帖、评论势能、案例信号 | P0 | 当前最稳的社区源 |
| 社区一手源 | Hacker News RSS | `https://news.ycombinator.com/rss` | 社区 RSS | `official_blog_fetch.py` 或 `source_probe.py` | 开发者热点、Show HN、工具讨论 | P1 | 适合作为社区势能补充 |
| 视频一手源 | YouTube Channel RSS | `https://www.youtube.com/feeds/videos.xml?channel_id=<id>` | 视频 RSS | `youtube_source_fetch.py channel` | 频道更新、标题、描述、发布时间 | P0 | 当前最稳的视频主源 |
| 视频一手源 | YouTube Transcript | YouTube 视频 URL | 视频正文 | `youtube_source_fetch.py transcript` | transcript、字幕、长视频摘要 | P1 | 当前云主机侧需 fallback |
| 舆情补充源 | FxTwitter | `https://fxtwitter.com/<user>/status/<id>` | 单条帖子镜像 | `official_blog_fetch.py` 或外部工具 | 单条 X 帖子内容镜像 | P2 | 只适合作为补充，不作底座 |
