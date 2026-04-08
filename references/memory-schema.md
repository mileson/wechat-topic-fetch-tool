# Memory Schema

## Purpose

`data/memory.md` 用于沉淀可重复复用的选题经验，不存原始抓取结果，只存判断和模式。

## Read Order

1. 先读 `data/memory.md`
2. 再读 `references/channel-playbook.md`
3. 再查 `references/source-catalog.md`
4. 最后按 `references/tool-catalog.md` 和 `scripts/` 执行

## Write Rules

- 每次执行后只追加值得复用的内容
- 不写冗长日志
- 不写敏感凭证
- 同类经验出现 3 次以上，再升级成稳定规则

## Recommended Sections

- `High-Signal Patterns`
- `Low-Signal Patterns`
- `Channel Preferences`
- `Validated Sources`
- `Known Limits`
- `Next Validation Targets`

## Compression Rule

当 `data/memory.md` 超过 200 行时：

1. 合并重复经验
2. 删除已过时限制
3. 把近期偶发问题折叠到 `Known Limits`
