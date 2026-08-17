# 大星牛来：基准图提示词

本样例使用 Codex 内置图像生成能力制作。先生成一张稳定的角色基准图，再让后续每个动作条带同时参考这张基准图与对应布局模板；这样比直接要求模型一次生成完整图集更容易保持角色一致。

## 最终采用的基准图提示词

```text
Use case: identity-preserve
Asset type: bold canonical full-body design concept for a tiny animated Codex desktop pet
Primary request: Redesign the supplied “大星牛来” into a much more flamboyant, exaggerated “牛市暴富版”, while preserving the exact character identity and deadpan personality.

Preserve the mustard-yellow fuzzy bull, rounded body proportions, pink-lilac muzzle and hands/feet, sleepy half-lidded expression, ears, tail, cobalt-blue triangular neckerchief, orange four-point star, and stylized 3D stop-motion toy material.

Replace both purple horns completely with oversized solid metallic-gold horns. Every visible part of each horn, from base to tip, must be polished rich gold. Make the horns about 25% larger, thicker, higher, and more dramatically upward-curved.

Add a festive-crimson sleeveless cropped bull-market vest with very wide metallic-gold trim and symmetrical structured shoulders. Keep the blue neckerchief visible on top. Turn the orange star into a dimensional orange-and-gold medallion framed by a thick gold ring. Add one enormous centered metallic-gold upward arrow across the vest, one oversized gold ingot-shaped belt buckle on an emerald belt, and matching chunky gold wrist cuffs.

Place one centered full-body character on a perfectly flat pure cyan #00FFFF background. Preserve the face and body. Keep accessories large, clean, attached, mostly symmetrical, and readable inside a 192×208 cell. No text, currency symbols, logos, tiny patterns, loose chains, floating coins, confetti, cape, crown, sunglasses, scenery, shadows, detached effects, extra limbs, or cropping.
```

## 动作条带策略

每个动作使用独立水平模板，帧数按状态分别为 4、5、6 或 8。由于基准图本身使用青色背景，动作条带改用纯绿色 `#00FF00`，避免色键误伤。11 行依次为：`idle`、`running-right`、`running-left`、`waving`、`jumping`、`failed`、`waiting`、`running`、`review`、`look-000-157-5`、`look-180-337-5`。完整生成、抠图、拼接和验收规则见 [`make-codex-pet-v2`](../../make-codex-pet-v2/SKILL.md)。
