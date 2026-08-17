# 大星牛来

这是使用 [`make-codex-pet-v2`](../../make-codex-pet-v2/README.md) 从一张用户提供的“牛来”截图生成的 Codex v2 动态宠物样例。

![动作总览](preview/contact-sheet.png)

![角色基准图](preview/canonical-base.png)

生成时采用的角色基准提示词与动作条带策略收录在 [`generation-prompt.md`](generation-prompt.md)。

## 个人化设计

- 保留芥末黄色短绒毛、粉紫色宽口鼻、半眯眼神情，以及钴蓝领巾和橙色四角星组成的“大星AI”识别元素。
- 两支牛角从根部到尖端全部升级为加粗、加高的抛光金角。
- 新增红金牛市战甲、巨大上涨箭头、金元宝腰扣、祖母绿腰带和对称粗金护腕。
- 使用 3D 定格动画玩偶质感；装饰虽然张扬，但都采用大块、固定、易辨认的形状，缩小到 `192×208` 仍能读出主题。

## Codex v2 合同

- 8 列 × 11 行；
- 1536×2288；
- 9 组任务状态；
- 16 个观察方向；
- 透明 WebP；
- `spriteVersionNumber: 2`。

## 安装

把 `pet.json` 和 `spritesheet.webp` 一起复制到：

```text
${CODEX_HOME:-$HOME/.codex}/pets/daxing-niulai/
```

重新加载 Codex 后，在宠物选择器中选择“大星牛来”。

## 验证

`preview/validation.json` 的几何、透明和空单元格检查全部通过；`preview/review.json` 的 11 行切帧检查无错误。`waiting` 行采用经视觉确认的稳定槽位切割，因此保留一条说明性警告。`preview/contact-sheet.png`、`preview/look-directions.png` 和各行 GIF 用于发布前视觉复核。

## 非官方同人声明

这是根据用户提供的网络传播角色截图之视觉意象制作的非官方同人宠物，与相关影视作品的创作者、发行方、权利人或 OpenAI 均无隶属、授权或背书关系。原始参考图不收入本样例目录。角色名称和视觉意象可能受第三方权利保护；商业使用前请自行确认。
