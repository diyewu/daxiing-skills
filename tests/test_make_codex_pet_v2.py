from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image, ImageDraw


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "make-codex-pet-v2"
SCRIPTS = SKILL_ROOT / "scripts"

ROW_SPECS = {
    "idle": 6,
    "running-right": 8,
    "running-left": 8,
    "waving": 4,
    "jumping": 5,
    "failed": 8,
    "waiting": 6,
    "running": 6,
    "review": 6,
    "look-000-157-5": 8,
    "look-180-337-5": 8,
}


class MakeCodexPetV2SkillTest(unittest.TestCase):
    def run_script(self, script: str, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPTS / script), *args],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )

    def test_skill_contract_and_user_docs_match_v2(self) -> None:
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        readme = (SKILL_ROOT / "README.md").read_text(encoding="utf-8")
        contract = (SKILL_ROOT / "references/codex-pet-contract.md").read_text(
            encoding="utf-8"
        )
        for text in (skill, readme, contract):
            self.assertIn("1536×2288", text)
            self.assertIn("spriteVersionNumber", text)
        self.assertIn("8×11", skill)
        self.assertIn("16", readme)
        self.assertNotIn("TODO", skill + readme)

    def test_prepare_run_creates_base_plus_eleven_rows(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            run_dir = Path(temp_dir) / "run"
            result = self.run_script(
                "prepare_pet_run.py",
                "--pet-name",
                "Test Otter",
                "--pet-id",
                "test-otter",
                "--pet-notes",
                "a round blue otter with an orange scarf",
                "--output-dir",
                str(run_dir),
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            request = json.loads((run_dir / "pet_request.json").read_text(encoding="utf-8"))
            jobs = json.loads((run_dir / "imagegen-jobs.json").read_text(encoding="utf-8"))
            self.assertEqual(request["atlas"]["rows"], 11)
            self.assertEqual(request["atlas"]["height"], 2288)
            self.assertEqual(request["atlas"]["sprite_version_number"], 2)
            self.assertEqual([row["state"] for row in request["rows"]], list(ROW_SPECS))
            self.assertEqual(len(jobs["jobs"]), 12)
            self.assertEqual(jobs["jobs"][0]["id"], "base")
            for state, frame_count in ROW_SPECS.items():
                guide = run_dir / "references/layout-guides" / f"{state}.png"
                self.assertTrue(guide.is_file())
                with Image.open(guide) as opened:
                    self.assertEqual(opened.size, (frame_count * 192, 208))

    def test_compose_and_validate_complete_v2_atlas(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            frames_root = root / "frames"
            for row_index, (state, frame_count) in enumerate(ROW_SPECS.items()):
                state_dir = frames_root / state
                state_dir.mkdir(parents=True)
                for frame_index in range(frame_count):
                    frame = Image.new("RGBA", (192, 208), (0, 0, 0, 0))
                    draw = ImageDraw.Draw(frame)
                    left = 50 + (frame_index % 3)
                    color = (80 + row_index * 10, 120, 180, 255)
                    draw.rounded_rectangle((left, 35, left + 85, 185), radius=20, fill=color)
                    frame.save(state_dir / f"{frame_index:02d}.png")

            png_path = root / "spritesheet.png"
            webp_path = root / "spritesheet.webp"
            composed = self.run_script(
                "compose_atlas.py",
                "--frames-root",
                str(frames_root),
                "--output",
                str(png_path),
                "--webp-output",
                str(webp_path),
            )
            self.assertEqual(composed.returncode, 0, composed.stdout + composed.stderr)

            validation_path = root / "validation.json"
            validated = self.run_script(
                "validate_atlas.py",
                str(webp_path),
                "--json-out",
                str(validation_path),
            )
            self.assertEqual(validated.returncode, 0, validated.stdout + validated.stderr)
            validation = json.loads(validation_path.read_text(encoding="utf-8"))
            self.assertTrue(validation["ok"])
            self.assertEqual((validation["width"], validation["height"]), (1536, 2288))
            self.assertEqual(validation["rows"], 11)
            self.assertEqual(validation["sprite_version_number"], 2)
            self.assertEqual(validation["transparent_rgb_residue_pixels"], 0)
            self.assertEqual(len(validation["cells"]), 88)

            contact = root / "contact-sheet.png"
            looks = root / "look-directions.png"
            previewed = self.run_script(
                "make_contact_sheet.py",
                str(webp_path),
                "--output",
                str(contact),
                "--look-output",
                str(looks),
            )
            self.assertEqual(previewed.returncode, 0, previewed.stdout + previewed.stderr)
            self.assertTrue(contact.is_file())
            self.assertTrue(looks.is_file())


if __name__ == "__main__":
    unittest.main()
