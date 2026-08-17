# 大星牛来：基准图提示词

本样例使用 Codex 内置图像生成能力制作。先生成一张稳定的角色基准图，再让后续每个动作条带同时参考这张基准图与对应布局模板；这样比直接要求模型一次生成完整图集更容易保持角色一致。

## 最终采用的基准图提示词

```text
Create one clean full-body reference sprite for Codex pet 大星牛来.

Pet identity: 一只芥末黄色长毛、略圆润的人形小牛；短而上翘的深紫色牛角，宽大的粉紫色口鼻，半眯眼和淡定荒诞的表情；保留小耳朵、短尾巴；新增对称的钴蓝色三角领巾，领巾中央只有一个无文字的橙色四角星布贴，作为“大星AI”的个人识别元素。

Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `3d-toy`: Stylized 3D toy mascot with smooth rounded forms, simple materials, clear silhouette, and no photoreal complexity. User style notes: 保留参考图的电影定格动画质感，柔软短绒毛、圆钝比例、全身直立；角色自身不带文字或可读 Logo；画面边缘必须清晰，适合缩小成桌面宠物。

Place a single centered pose on a perfectly flat pure cyan #00FFFF chroma-key background. Keep the full pet visible, compact, readable at 192x208, and easy to animate. Preserve approved reference identity cues. No scenery, text, borders, checkerboard transparency, shadows, glows, detached effects, or extra props. Keep #00FFFF and close colors out of the pet, props, highlights, and effects.
```

## 动作条带策略

每一行都使用 8 帧水平模板，要求完整角色留在单元格内，并保持纯青色背景。11 行依次为：`idle`、`waiting`、`running-right`、`running-left`、`waving`、`failed`、`review`、`jumping`、`look-000-157-5`、`look-180-337-5`、`running`。完整生成、抠图、拼接和验收规则见 [`make-codex-pet-v2`](../../make-codex-pet-v2/SKILL.md)。
