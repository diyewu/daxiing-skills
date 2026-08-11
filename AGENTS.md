# Daxiing Skills 开发约定

## 仓库定位

本仓库集中维护多个相互独立的 Codex Skill。每个 Skill 必须使用独立的顶层目录，目录名与 Skill 名一致。

## Skill 结构

```text
<skill-name>/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── scripts/       # 仅在需要确定性执行时创建
├── references/    # 仅在需要按需加载资料时创建
└── assets/        # 仅在输出需要复用素材时创建
```

- 新建或修改 Skill 时使用 `$skill-creator`。
- Skill 名只使用小写字母、数字和连字符，长度小于 64 个字符。
- `SKILL.md` front matter 只包含 `name` 和 `description`。
- `description` 同时写清能力和触发场景；正文使用祈使句。
- 保持 `SKILL.md` 精简，详细资料移入 `references/`，不要重复维护同一内容。
- 每个 Skill 必须包含 `README.md`，面向使用者说明用途、适用场景、调用方式、示例和能力边界。
- `README.md` 是用户文档，`SKILL.md` 是 Agent 运行指令；两者服务对象不同，但不得互相矛盾。
- 不在 Skill 目录内创建 `CHANGELOG.md`、安装指南或快速参考等其他旁支文档。
- `agents/openai.yaml` 的 `default_prompt` 必须显式包含 `$<skill-name>`。
- 只创建实际需要的 `scripts/`、`references/`、`assets/`。

## 开发流程

1. 收到 Skill 评估需求时，必须把结论落到 `docs/evaluations/<skill-name>.md`，不能只保留在对话中。
2. 评估文档使用 `docs/evaluations/_template.md`，至少记录定位、触发场景、边界、保留/重建/删除决策、风险、版本范围、验收场景和下一步。
3. 对同一个 Skill 继续评估时更新原文档，并维护“更新记录”；不要为每轮讨论创建相互割裂的文档。
4. 评估结论发生变化时，先更新评估文档，再进入实现；实现完成后补记实际落地情况和验证结果。
5. 用具体用户请求明确触发条件、边界和验收方式。
6. 运行 `scripts/new_skill.py` 创建骨架。
7. 先实现可复用资源，再完善 `SKILL.md`。
8. 完成面向使用者的 `README.md`。
9. 实际运行新增脚本，并为重要逻辑补测试。
10. 运行 `make check`。
11. 用真实请求前向测试复杂 Skill，再根据结果迭代。

评估文档属于仓库级开发资料，不放进 Skill 运行目录，也不随 Skill 安装。

## 验证

```bash
make check
```

提交前保持改动只覆盖当前 Skill 或明确的仓库级工具，不要顺手改动无关 Skill。
