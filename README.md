# Daxiing Skills

这是大星统一维护 Codex Skills 的仓库。每个 Skill 位于独立的顶层文件夹，可以单独开发、验证和安装。

## 仓库结构

```text
daxiing-skills/
├── <skill-name>/          # 一个独立 Skill
│   ├── SKILL.md
│   ├── README.md           # 面向使用者的用途与使用说明
│   └── agents/openai.yaml
├── docs/evaluations/      # Skill 评估、重构决策与验收准备
├── docs/forward-tests/    # 隔离前向测试证据
├── scripts/               # 仓库级创建与校验工具
├── tests/                 # 仓库级工具测试
├── AGENTS.md              # Agent 开发约定
└── Makefile
```

每个 Skill 必须包含 `README.md`，说明它有什么用、适合什么场景、如何调用以及能力边界。Skill 可按需增加 `scripts/`、`references/` 和 `assets/`，不要为了占位创建空目录。

## 已收录 Skill

| Skill | 定位 | 状态 |
|---|---|---|
| [`start-with-me`](start-with-me/README.md) | 把难以开始的任务变成一个低压力、可执行的起步动作 | V0.2 已通过 16 个隔离前向测试 |
| [`pick-something-fun`](pick-something-fun/README.md) | 根据当前限制快速选出一个可执行的休闲活动 | V0.1 已通过 12 个隔离前向测试 |

## 评估 Skill

所有 Skill 评估都必须落地到 `docs/evaluations/<skill-name>.md`。同一 Skill 后续调整继续更新同一份文档，记录定位、范围、关键决策、风险、验收场景和实施状态，避免评估结论只存在于对话中。

新评估从 `docs/evaluations/_template.md` 开始。评估文档是仓库开发资料，不属于可安装的 Skill 内容。

完整的评估、独立重建、开发、验证、安装和发布流程见[通用 Skill 二开流程](docs/skill-redevelopment-workflow.md)。

## 创建 Skill

Skill 名只允许小写字母、数字和连字符，长度必须小于 64 个字符。

```bash
python3 scripts/new_skill.py example-skill \
  --description "Describe what the skill does and the requests that should trigger it." \
  --short-description "Create reliable outputs for a focused workflow" \
  --default-prompt 'Use $example-skill to complete this focused workflow.' \
  --resources scripts,references
```

命令会生成 `SKILL.md` 和 `agents/openai.yaml`，并只创建 `--resources` 指定的资源目录。随后删除模板中的 TODO，补齐真实工作流和资源。

## 验证

```bash
make check
```

也可以分别执行：

```bash
python3 scripts/validate_skills.py .
python3 -m unittest discover -s tests -v
```

校验器会检查 Skill 命名、front matter、目录名一致性、必要 UI 元数据、配套 `README.md`，以及 Skill 目录内不应出现的其他旁支文档。

## 安装单个 Skill

开发完成后，把对应 Skill 目录复制或链接到 Codex Skills 目录，并开启新会话让 Codex 重新发现它：

```bash
ln -s "$(pwd)/example-skill" ~/.codex/skills/example-skill
```

## 知识库入口

- [项目状态记录](obsidian://open?vault=Obsidian%20Vault&file=Codex%20Knowledge%2Fprojects%2Fdaxiing-skills.md)
- [知识库项目台](http://192.168.0.30:8089/projects/daxiing-skills)
