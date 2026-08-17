---
name: "make-codex-pet-v2"
description: "Create, repair, validate, preview, and package Codex v2 animated pets from a character description or reference image. Use when a user wants a custom Codex desktop pet, an 8×11 v2 spritesheet, 9 task-state animations plus 16 look directions, or a reusable pet package. Do not use for ordinary standalone illustrations, logos, or unrelated sprite formats."
---

# Make Codex Pet V2

Turn one character idea or reference image into a Codex v2 pet package. Let image generation own appearance and poses; let the bundled scripts own geometry, transparency, validation, previews, and packaging.

## Keep The Contract

- Target `spriteVersionNumber: 2` only.
- Produce an `8×11` atlas at exactly `1536×2288` pixels.
- Keep every cell at `192×208` pixels.
- Produce 9 task-state rows and 2 look-direction rows.
- Keep all unused cells fully transparent and normalize their hidden RGB values to zero.
- Treat one consistent character identity as a blocking requirement across all 11 rows.
- Read [codex-pet-contract.md](references/codex-pet-contract.md) before packaging or validating an atlas.
- Read [animation-rows-v2.md](references/animation-rows-v2.md) before generating or repairing rows.
- Read [qa-rubric.md](references/qa-rubric.md) before final acceptance.

Do not use this workflow for a normal illustration, icon, logo, or a spritesheet format that is not intended for Codex.

## Respect Source Rights

- Ask whether the user owns, created, licensed, or is otherwise authorized to use a supplied character when public distribution is requested and the answer is not already clear.
- Keep third-party references out of the public output unless the user confirms redistribution rights.
- Do not claim that an open-source code license grants rights in a character, trademark, reference image, or likeness.
- For fan work, add a concise non-affiliation notice and tell the user that commercial use needs separate review.

Do not block private local prototyping merely because a reference resembles a known character. Keep the rights boundary explicit and avoid making legal conclusions.

## Run The Workflow

### 1. Resolve The Pet Brief

Infer missing fields when safe:

- `pet_name`: short human-facing name;
- `pet_id`: lowercase filesystem-safe slug;
- `description`: one sentence;
- `pet_notes`: stable identity cues that every row must preserve;
- `style_preset`: `auto`, `pixel`, `plush`, `clay`, `sticker`, `flat-vector`, `3d-toy`, `painterly`, or `brand-inspired`;
- `style_notes`: only user-specific visual constraints;
- reference image paths and their roles;
- output run directory.

Ask one focused question only when a missing answer would materially change identity, rights, or output location. Otherwise choose a reversible default and continue.

Keep accessories large, simple, and stable at pet size. Avoid readable text, tiny logos, loose particles, scenery, cast shadows, and asymmetrical details that would break mirrored movement.

### 2. Prepare A Run

Set `SKILL_DIR` to this Skill directory and run:

```bash
python "$SKILL_DIR/scripts/prepare_pet_run.py" \
  --pet-name "<name>" \
  --pet-id "<slug>" \
  --description "<one sentence>" \
  --reference /absolute/path/to/reference.png \
  --pet-notes "<stable identity cues>" \
  --style-preset auto \
  --style-notes "<optional style constraints>" \
  --output-dir /absolute/path/to/run
```

Omit `--reference` for a text-only pet. Use repeated `--reference` flags for multiple authorized inputs. The script selects a chroma key, copies references into the run, creates 11 layout guides, writes row prompts, and creates `imagegen-jobs.json`.

Do not overwrite a non-empty run unless the user wants to resume or rebuild it. Use `--force` only after checking the exact directory.

### 3. Generate The Canonical Base

Read `imagegen-jobs.json`. Generate the `base` job first with the installed `$imagegen` Skill. Attach every listed input image with its role.

Require one centered full-body character on the exact flat chroma-key background. Reject text, checkerboards, scenery, shadows, detached effects, cropped anatomy, or a pose that cannot fit inside `192×208`.

Copy the selected output to `decoded/base.png` and `references/canonical-base.png`, then mark the `base` job complete only after both files exist.

If `$imagegen` is unavailable, stop after preparing the run and tell the user which base and row files are still required. Do not fabricate completion or synthesize replacement art with local drawing code.

### 4. Generate The Identity And Gait Check

Generate `idle` and `running-right` next. For every row job:

- read its prompt and retry prompt;
- attach every `input_images` entry from the manifest;
- use the canonical base as the identity source of truth;
- use the layout guide only for frame count, spacing, centering, and safe padding;
- require one complete pose per invisible slot on the flat chroma background;
- copy the selected strip to `decoded/<state>.png` before marking it complete.

Inspect these two strips before paying the cost of the remaining rows. Reject them if the character changes species, face, proportions, palette, material, signature accessory, scale, baseline, or direction.

Generate `running-left` normally unless horizontal mirroring preserves every meaningful detail. If mirroring is safe, derive it frame by frame while preserving temporal order:

```bash
python "$SKILL_DIR/scripts/derive_running_left_from_running_right.py" \
  --run-dir /absolute/path/to/run \
  --confirm-appropriate-mirror \
  --decision-note "<why text, markings, props, light, and identity remain valid>"
```

Never mirror a whole strip in a way that reverses frame cadence.

### 5. Generate The Remaining Rows

Generate each still-pending row through `$imagegen`:

```text
waving
jumping
failed
waiting
running
review
look-000-157-5
look-180-337-5
```

Generate rows sequentially by default. If the user explicitly allows parallel agent work, run at most two independent row jobs at once and keep each worker limited to one row.

For look rows, preserve the same body scale and baseline while progressing through the exact angles in [animation-rows-v2.md](references/animation-rows-v2.md). Treat them as 16 ordered directional poses, not two animation loops.

Repair only the failing row. Do not regenerate a good base or unrelated rows.

### 6. Extract, Inspect, And Compose

Run the deterministic pipeline:

```bash
RUN_DIR=/absolute/path/to/run
mkdir -p "$RUN_DIR/final" "$RUN_DIR/qa"

python "$SKILL_DIR/scripts/extract_strip_frames.py" \
  --decoded-dir "$RUN_DIR/decoded" \
  --output-dir "$RUN_DIR/frames" \
  --states all \
  --method auto

python "$SKILL_DIR/scripts/inspect_frames.py" \
  --frames-root "$RUN_DIR/frames" \
  --json-out "$RUN_DIR/qa/review.json" \
  --require-components

python "$SKILL_DIR/scripts/compose_atlas.py" \
  --frames-root "$RUN_DIR/frames" \
  --output "$RUN_DIR/final/spritesheet.png" \
  --webp-output "$RUN_DIR/final/spritesheet.webp"

python "$SKILL_DIR/scripts/validate_atlas.py" \
  "$RUN_DIR/final/spritesheet.webp" \
  --json-out "$RUN_DIR/final/validation.json"

python "$SKILL_DIR/scripts/make_contact_sheet.py" \
  "$RUN_DIR/final/spritesheet.webp" \
  --output "$RUN_DIR/qa/contact-sheet.png" \
  --look-output "$RUN_DIR/qa/look-directions.png"

python "$SKILL_DIR/scripts/render_animation_previews.py" \
  --frames-root "$RUN_DIR/frames" \
  --output-dir "$RUN_DIR/qa/previews"
```

If component extraction incorrectly changes scale or baseline even though the source strip is stable, rerun extraction with `--method stable-slots`, then rerun inspection with `--allow-stable-slots`. Use this only after visually confirming the source strip is properly separated and unclipped.

### 7. Perform Visual QA

Inspect `qa/contact-sheet.png`, `qa/look-directions.png`, and every file under `qa/previews/`. Use `qa/review.json` and `final/validation.json` as evidence, not substitutes for vision.

Reject the result when any row has:

- identity, style, material, palette, face, proportion, marking, or prop drift;
- missing, repeated, cropped, overlapping, or nearly static frames;
- wrong state semantics or wrong travel direction;
- size popping, baseline jumping, or reversed gait cadence;
- visible guide lines, white rectangles, chroma residue, shadows, glow, dust, detached effects, or scenery;
- look directions that skip, reverse, or duplicate the intended sequence.

Regenerate the smallest failing row, then rerun the full deterministic pipeline.

### 8. Package And Install

Package only after automatic and visual QA pass. Write:

```json
{
  "id": "<pet-id>",
  "displayName": "<display name>",
  "description": "<one sentence>",
  "spriteVersionNumber": 2,
  "spritesheetPath": "spritesheet.webp"
}
```

If local installation is part of the request, copy the manifest and WebP together to:

```text
${CODEX_HOME:-$HOME/.codex}/pets/<pet-id>/
```

If installation was not requested, leave the verified package in the user-approved output directory. Never report the pet as installed until both files exist in the final destination.

## Return The Result

Report:

- pet name and id;
- package path and whether it was installed;
- `spritesheet.webp`, `pet.json`, contact sheet, look-direction preview, validation JSON, and review JSON paths;
- automatic validation result and concise visual QA result;
- any unresolved rights, identity, or app-version caveat;
- the exact identity prompt used for the canonical base.

Do not call an output complete when generation, validation, visual QA, or packaging is still pending.
