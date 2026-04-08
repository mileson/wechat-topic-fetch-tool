# Tool Catalog

## Path Convention

优先用相对技能根目录的方式定位工具，不要在 Skill 里写死绝对路径。

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

## Tool Table

| 工具层级 | 工具名 | 类型 | 当前路径 / 来源 | 对应来源 | 使用方法说明 | fallback | 备注 |
|---|---|---|---|---|---|---|---|
| Skill 内置脚本 | `official_blog_fetch.py` | Python CLI 脚本 | `{skill_root}/scripts/official_blog_fetch.py` | 官方博客 / 官方页 | 见 `references/channel-playbook.md` | `source_probe.py` | 支持 `list-targets` / `fetch <target_or_url>` |
| Skill 内置脚本 | `reddit_rss_fetch.py` | Python 脚本 | `{skill_root}/scripts/reddit_rss_fetch.py` | Reddit RSS | 见 `examples/source-checklist.md` | `../reddit-readonly-clawhub` | 当前推荐主实现 |
| Skill 内置脚本 | `youtube_source_fetch.py` | Python 脚本 | `{skill_root}/scripts/youtube_source_fetch.py` | YouTube RSS / transcript fallback | 见 `examples/source-checklist.md` | `../youtube-transcript` / `../youtube-transcript-proxy` | 当前推荐主实现 |
| Skill 内置脚本 | `source_probe.py` | Python 脚本 | `{skill_root}/scripts/source_probe.py` | 所有来源 | 探测可用性 | 无 | 适合新来源预检 |
| Skill 内置脚本 | `source_router.py` | Python 脚本 | `{skill_root}/scripts/source_router.py` | 所有来源 | 统一入口 | 各子脚本 | 标准化路由 |
| 外部服务 | RSSHub | 服务 | `http://127.0.0.1:1200` | 官方站点 / RSS / 部分社交 | 先查对应路由 | 直抓脚本 | 适合统一聚合层 |
| 同级 Skill | `reddit` | Skill | `{skills_root}/reddit` | Reddit public JSON | 仅在确认 JSON 可用时使用 | `reddit_rss_fetch.py` | 当前不建议做主链路 |
| 同级 Skill | `reddit-readonly-clawhub` | Skill | `{skills_root}/reddit-readonly-clawhub` | Reddit 只读 | 可用于补充查询 | `reddit_rss_fetch.py` | 适合补充，不作主链路 |
| 同级 Skill | `youtube-transcript` | Skill | `{skills_root}/youtube-transcript` | YouTube transcript | transcript 需要时调用 | `youtube_source_fetch.py transcript` | 当前云主机易受限 |
| 同级 Skill | `youtube-transcript-proxy` | Skill | `{skills_root}/youtube-transcript-proxy` | YouTube transcript | 优先在代理条件满足时使用 | `youtube_source_fetch.py transcript` | 需要 WireGuard / 代理 |
| 发现层 CLI | `clawhub` | CLI | 系统命令 | Skill 发现 | 查 `discovery-sources.md` | GitHub / skills.sh | 用于搜索和安装候选 Skill |
| 发现层 CLI | `npx skills` | CLI | 系统命令 | Skill 发现 | 查 `discovery-sources.md` | GitHub / ClawHub | 适合薄封装 Skill 检索 |
| 发现层 CLI | Git / GitHub | CLI / 平台 | GitHub 仓库 | 发现底层实现 | 查 `discovery-sources.md` | 无 | 最重要的参考源 |

## Sibling Skill Rule

如果当前 agent 把 `content-source-governor` 放进某个 `skills/` 目录中，默认优先按同级目录查找：

- `{skills_root}/reddit`
- `{skills_root}/reddit-readonly-clawhub`
- `{skills_root}/youtube-transcript`
- `{skills_root}/youtube-transcript-proxy`

只有在同级目录不存在时，才退回到内置脚本或外部服务。
