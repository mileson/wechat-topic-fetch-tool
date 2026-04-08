# Discovery Sources

| 发现平台 | 定位 | 适合找什么 | 搜索方式 | 选型标准 | 备注 |
|---|---|---|---|---|---|
| GitHub | 底层实现源 | RSS 聚合器、API wrapper、抓取脚本、MCP、CLI 工具 | 关键词 + repo 搜索 | 真实源码、维护活跃、依赖透明、能独立运行 | 默认优先级最高 |
| ClawHub | Skill 成品层 | 已包装好的 Skill、代理版 Skill、轻运维接入 | `clawhub search` / `clawhub inspect` | 描述清晰、更新近期、Owner 可信、依赖可见 | 适合快速试验 |
| skills.sh | 薄封装 Skill 层 | GitHub repo 的 Skill 封装、轻量工作流 | `npx skills find` / `npx skills add --list` | 安装量、底层 repo 质量、功能单一清晰 | 适合找轻包装 |

## Selection Rules

1. 先看 GitHub 是否有稳定底层实现
2. 再看 skills.sh 是否有薄包装版本
3. 最后看 ClawHub 是否有更适合当前环境的代理版 / 增强版
4. 不要因为安装量高就默认可信，必须确认：
   - 底层抓取方式
   - 是否依赖第三方 API
   - 是否依赖代理 / 登录态
   - 是否适合长期复用

## CLI Bias

优先选择提供明确 CLI 或脚本入口的实现。

原因：

- 更适合 Agent 调用
- 更适合 cron 和自动化
- 更容易在不同 agent 的 `skills/` 目录中迁移
