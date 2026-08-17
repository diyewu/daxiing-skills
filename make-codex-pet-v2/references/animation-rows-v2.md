# Codex Pet v2 Rows

## Contents

- Animation rows
- Look-direction rows
- Direction conventions

## Animation rows

| Row | State | Used columns | Suggested durations |
| ---: | --- | --- | --- |
| 0 | `idle` | 0–5 | 280, 110, 110, 140, 140, 320 ms |
| 1 | `running-right` | 0–7 | 120 ms each, final 220 ms |
| 2 | `running-left` | 0–7 | 120 ms each, final 220 ms |
| 3 | `waving` | 0–3 | 140 ms each, final 280 ms |
| 4 | `jumping` | 0–4 | 140 ms each, final 280 ms |
| 5 | `failed` | 0–7 | 140 ms each, final 240 ms |
| 6 | `waiting` | 0–5 | 150 ms each, final 260 ms |
| 7 | `running` | 0–5 | 120 ms each, final 220 ms |
| 8 | `review` | 0–5 | 150 ms each, final 280 ms |

Keep unused cells after the last used column fully transparent.

## Look-direction rows

The final two rows form one 16-direction set. Treat them as ordered poses, not animation loops.

| Row | Local state id | Columns | Ordered directions |
| ---: | --- | --- | --- |
| 9 | `look-000-157-5` | 0–7 | 0°, 22.5°, 45°, 67.5°, 90°, 112.5°, 135°, 157.5° |
| 10 | `look-180-337-5` | 0–7 | 180°, 202.5°, 225°, 247.5°, 270°, 292.5°, 315°, 337.5° |

Change gaze and head turn first. Rotate the upper body only as much as needed to make the direction readable. Keep scale, baseline, palette, material, markings, and props stable across all 16 frames.

## Direction conventions

- `running-right` must face and travel right.
- `running-left` must face and travel left.
- Mirror `running-right` only when text, markings, light direction, props, and identity remain valid after a horizontal flip.
- Preserve temporal frame order when deriving a mirrored row; do not mirror the whole strip and accidentally reverse the cadence.
- `running` means Codex is actively processing work; it is not foot-running.
