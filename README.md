<a id="微信选题素材采集工具"></a>

<div align="center">

# 微信选题素材 · 多源采集与内容源治理

**从官方博客、社区和视频来源组织内容调研材料。**

来源发现 · 可达性探测 · 内容抓取 · 素材路由

[![中文说明](https://img.shields.io/badge/%E8%AF%B4%E6%98%8E-%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-059669)](#readme-detail-12)
[![项目类型](https://img.shields.io/badge/%E9%A1%B9%E7%9B%AE-Skill-6366f1)](#readme-detail-12)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![零依赖](https://img.shields.io/badge/依赖-零-green.svg)]()

[✨ 核心特性](#readme-detail-12) · [✅ 适用场景](#readme-detail-audience) · [🚀 快速开始](#readme-detail-14) · [🧩 模块速查](#readme-detail-22) · [🔄 工作流程](#readme-detail-16) · [🏗️ 技术栈](#readme-detail-18)

</div>

---

<a id="wechat-topic-fetch-tool"></a>


> 内容源治理工具 —— 从官方博客、Reddit、YouTube 等多源发现、抓取和路由 AI/科技资讯，专为即刻和微信公众号内容创作者打造。

<a id="readme-section-1"></a>

<a id="功能特性"></a>

<a id="readme-detail-12"></a>

## ✨ 核心特性

- **统一路由** — 一个 CLI 入口分发到官方博客、Reddit RSS、YouTube 频道等多个抓取器
- **源记忆** — 跨会话学习高信号/低信号模式，持久化到结构化记忆文件
- **频道策略** — 为即刻（快节奏短内容）和微信公众号（深度长文）定制不同的源选择和内容深度
- **降级链** — 优雅降级：`urllib` → `curl` → 兄弟 Skill → 手动探针
- **先探后抓** — 轻量 URL 探测器，在正式抓取前验证新源可用性
- **零依赖** — 纯 Python 标准库，无需 `pip install`

<a id="readme-detail-audience"></a>

## ✅ 适用场景

适合为即刻与公众号准备 AI 科技素材的创作者。

<a id="readme-section-2"></a>

<a id="快速开始"></a>

<a id="readme-detail-14"></a>

## 🚀 快速开始

从下面的现有入口开始，按顺序准备环境、配置并完成首次运行。

### 前置条件

- Python 3.10 或更高版本
- `curl`（可选，作为 HTTP 降级方案）

### 安装

```bash
# 克隆仓库
git clone https://github.com/Mileson07/wechat-topic-fetch-tool.git
cd wechat-topic-fetch-tool
```

或使用 pipx 安装：

```bash
pipx install git+https://github.com/Mileson07/wechat-topic-fetch-tool.git
```

### 使用方法

```bash
# 抓取指定官方博客（如 OpenAI、Anthropic、Cursor）
python3 scripts/source_router.py official openai_developers_blog

# 抓取任意 URL
python3 scripts/source_router.py official https://example.com/blog

# 抓取 Reddit 子版块 RSS
python3 scripts/source_router.py reddit MachineLearning --limit 5

# 抓取 YouTube 频道视频
python3 scripts/source_router.py youtube-channel <channel_id> --limit 5

# 抓取 YouTube 视频字幕
python3 scripts/source_router.py youtube-transcript <video_url>

# 在抓取前探测 URL 可达性
python3 scripts/source_router.py probe https://example.com https://another.com
```

<a id="readme-section-3"></a>

<a id="工作流程"></a>

<a id="readme-detail-16"></a>

## 🔄 工作流程

1. **读取记忆** — 从 `data/memory.md` 加载积累的源经验
2. **选择频道** — 即刻（快速、有力）或微信公众号（深度、结构化）
3. **选择源** — 查阅 `references/source-catalog.md` 获取优先级排序的源列表
4. **路由到工具** — 使用 `references/tool-catalog.md` 选择正确的抓取器及降级方案
5. **抓取与解析** — 通过 `source_router.py` 或独立脚本执行
6. **更新记忆** — 记录高/低信号模式、已验证/已屏蔽的源

<a id="readme-section-4"></a>

<a id="技术栈"></a>

<a id="readme-detail-18"></a>

## 🏗️ 技术栈

微信选题素材 的实现按下列技术与模块组织，接入和维护时可据此定位。

| 层级 | 技术 |
|------|------|
| 语言 | Python 3.10+ |
| HTTP 客户端 | `urllib.request`（`curl` 降级） |
| RSS 解析 | `xml.etree.ElementTree` |
| 命令行 | `argparse` |
| 外部依赖（可选） | `curl`、兄弟 Skill |

<a id="readme-section-5"></a>

<a id="项目结构"></a>

<a id="readme-detail-20"></a>

## 📁 项目结构

下面按实现职责列出目录位置，便于把修改放回对应模块。

<details>
<summary>展开目录与模块位置</summary>

```
wechat-topic-fetch-tool/
├── scripts/
│   ├── source_router.py         # 统一 CLI 入口
│   ├── official_blog_fetch.py   # 官方博客/页面抓取器
│   ├── reddit_rss_fetch.py      # Reddit RSS Atom 解析器
│   ├── youtube_source_fetch.py  # YouTube 频道和字幕抓取器
│   ├── source_probe.py          # 轻量 URL 探测器
│   └── path_helpers.py          # 便携路径常量
├── references/
│   ├── source-catalog.md        # 主源注册表（含优先级）
│   ├── tool-catalog.md          # 工具路由表（含降级链）
│   ├── channel-playbook.md      # 频道专属内容策略
│   ├── source-targets.json      # 命名博客/网站目标定义
│   ├── discovery-sources.md     # 新源工具发现指南
│   └── memory-schema.md         # 源记忆管理规则
├── data/
│   └── memory.md                # 积累的源经验记忆
├── examples/
│   └── source-checklist.md      # 源评估检查清单
├── SKILL.md                     # Skill 定义（Claude Code / Agent）
├── pyproject.toml               # 包元信息
├── LICENSE                      # MIT 许可证
└── .gitignore
```

</details>

<a id="readme-section-6"></a>

<a id="仓库导航"></a>

<a id="readme-detail-22"></a>

## 🧩 模块速查

按要处理的工作选择入口，先看模块职责，再进入对应文件或目录。

| 模块入口 | 负责什么 | 什么时候看 |
| --- | --- | --- |
| [`SKILL.md`](SKILL.md) | Agent 使用规则与执行入口 | 让 Agent 读取任务规则、所需材料与交付要求 |
| [`examples/`](examples/) | 可参考的输入与调用示例 | 用现有样例核对输入格式和调用方式 |
| [`pyproject.toml`](pyproject.toml) | Python 包与工具配置 | 核对依赖、工程目标与现有命令 |
| [`references/`](references/) | 技能规则与输入输出合同 | 核对输入约定、操作细节与适用边界 |
| [`scripts/`](scripts/) | 开发与维护脚本 | 查找构建、验证或维护的现有命令 |

<a id="readme-section-7"></a>

<a id="贡献"></a>

<a id="readme-detail-24"></a>

## 🤝 贡献

欢迎贡献！随时可以提 Issue 或提交 Pull Request。

<a id="readme-section-8"></a>

<a id="许可证"></a>

<a id="readme-detail-26"></a>

## 📄 许可证

本项目基于 [MIT 许可证](LICENSE) 开源。

<a id="readme-section-9"></a>

<a id="作者"></a>

<a id="readme-detail-28"></a>

## 👤 作者

- X: [Mileson07](https://x.com/Mileson07)
- 小红书: [超级峰](https://xhslink.com/m/4LnJ9aB1f97)
- 抖音: [超级峰](https://v.douyin.com/rH645q7trd8/)
