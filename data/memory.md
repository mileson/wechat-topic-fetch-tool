# Content Source Governor Memory

> Auto-maintained. Read before each execution, update after completion.

## High-Signal Patterns

- 双事件共振后能够给出更大的范式判断。
- 权威人物 / 机构案例能提炼出反直觉框架。
- Agent-first IDE、工作流平台、编排系统更适合做“开发者角色变化”类题。
- 定价、许可证、基础设施策略变化，往往能转成“生态拐点”判断。

## Low-Signal Patterns

- 只有热闹没有工作流影响的新闻。
- 只有观点没有新增事实的争论。
- 同一事件换包装重复入库。
- 快讯强行写成长文，缺少方法论延展。

## Channel Preferences

- 即刻：优先近 72 小时的新变化、单点突破、强判断。
- 微信公众号：优先权威案例、结构化深挖、方法论和生态变化。

## Validated Sources

- Reddit RSS：可稳定读取。
- YouTube Channel RSS：可稳定读取。
- Anthropic News：可直接抓取页面。
- Anthropic Research：可直接抓取页面。
- Cloudflare Blog：可直接抓取页面。
- Anthropic Glasswing（anthropic.com/glasswing）：可直接抓取，内容丰富。
- Claude Blog（claude.com/blog）：web_fetch 可提取文章列表，但 JS 渲染页面 official_blog_fetch.py 只返回 HTML 片段。
- HN RSS：稳定可用，每日高信号 AI 安全/编程话题。

## Known Limits

- Reddit public JSON：当前云主机侧容易 `403`。
- YouTube transcript：当前云主机侧容易被云 IP 限制。
- OpenAI Blog：当前云主机侧可能触发 Cloudflare challenge。
- X 原站：公开抓取稳定性较差，只适合作为补充层。

## Next Validation Targets

- Cursor Blog：官方脚本返回 HTML 片段，web_fetch 效果待验证
- OpenAI Developers Blog：官方脚本返回 HTML 片段，需进一步探索结构化抓取
- Google AI Blog：同上
- Indie Hackers Stories

## Recent Observations (2026-04-08)

- Anthropic Glasswing 是重大信号事件（12巨头联盟+Mythos模型），适合作为双事件共振选题
- Claude Blog web_fetch 成功获取文章列表，最新4/7 Subagent指南已入库
- Cursor Blog 近期无新文章（最新仍为 warp decode）
- Reddit r/artificial 近期偏向政策/社会议题，AI编程/Agent相关度降低
- Reddit r/MachineLearning 出现 MemPalace 基准争议（虚假基准问题）

## Recent Observations (2026-04-09)

- Claude Blog 4/2新文"Harnessing Claude's Intelligence"是Agent架构设计官方指南，web_fetch可完整提取，高信号
- OpenAI Developers Blog web_fetch成功提取文章列表（Astro站点），最新3/25 Perplexity语音搜索，近两周无新文
- Google AI Blog JS渲染严重，web_fetch只返回极简结构，列为低效源
- Cloudflare Blog web_fetch可完整提取Markdown，4/8符号执行+4/7后量子+4/2 AI缓存重设计，其中AI缓存题有信号
- Reddit r/LocalLLaMA：Gemma 4 GGUF发布、Safetensors迁移PyTorch Foundation（基础设施拐点）、GLM 5.1实测
- Reddit r/singularity：Sam Altman同事评价+AI打破经济论，偏社会议题非AI编程
