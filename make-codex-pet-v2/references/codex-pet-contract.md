# Codex Pet v2 Contract

## Contents

- Atlas geometry
- Row contract
- Local package
- Validation rules
- Compatibility note

## Atlas geometry

- Format: transparent PNG or lossless WebP.
- Dimensions: `1536×2288`.
- Grid: 8 columns × 11 rows.
- Cell: `192×208` pixels.
- `spriteVersionNumber`: `2`.
- Used cells: non-empty and contained inside their cell.
- Unused cells: fully transparent with RGB normalized to zero.

Do not add labels, gutters, visible grids, borders, floor shadows, scenery, or extra frames to the atlas.

## Row contract

Read [animation-rows-v2.md](animation-rows-v2.md) for row order, used columns, timing, and the 16 look directions.

## Local package

Place the files together under:

```text
${CODEX_HOME:-$HOME/.codex}/pets/<pet-id>/
├── pet.json
└── spritesheet.webp
```

Write this manifest shape:

```json
{
  "id": "pet-id",
  "displayName": "Pet Name",
  "description": "One short sentence.",
  "spriteVersionNumber": 2,
  "spritesheetPath": "spritesheet.webp"
}
```

The directory name is the local pet identifier. Keep it lowercase, filesystem-safe, and stable.

## Validation rules

- Reject any atlas not exactly `1536×2288`.
- Reject PNG/WebP files without usable transparency.
- Reject empty used cells or non-transparent unused cells.
- Reject transparent pixels that retain non-zero RGB residue.
- Reject role drift, wrong action semantics, cropped poses, visible guide marks, shadows, or detached effects during visual QA.
- Treat script validation as necessary but insufficient; inspect the final contact sheet and motion previews.

## Compatibility note

Codex currently distinguishes sprite versions by atlas height: v1 uses 9 rows (`1536×1872`) and v2 uses 11 rows (`1536×2288`). This Skill intentionally targets v2 and always writes `spriteVersionNumber: 2`.
