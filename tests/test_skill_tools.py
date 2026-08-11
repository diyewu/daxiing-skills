from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
NEW_SKILL = REPO_ROOT / "scripts" / "new_skill.py"
VALIDATE = REPO_ROOT / "scripts" / "validate_skills.py"


class SkillToolsTest(unittest.TestCase):
    def run_command(self, *args: str, cwd: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, *args],
            cwd=cwd,
            check=False,
            capture_output=True,
            text=True,
        )

    def test_create_and_validate_skill(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            created = self.run_command(
                str(NEW_SKILL),
                "sample-skill",
                "--path",
                str(root),
                "--description",
                "Create sample outputs when a user requests the sample workflow.",
                "--short-description",
                "Create dependable sample workflow outputs",
                "--default-prompt",
                "Use $sample-skill to complete the sample workflow.",
                "--resources",
                "scripts,references",
                cwd=root,
            )
            self.assertEqual(created.returncode, 0, created.stderr)
            self.assertTrue((root / "sample-skill" / "SKILL.md").is_file())
            self.assertTrue((root / "sample-skill" / "README.md").is_file())
            self.assertTrue((root / "sample-skill" / "scripts").is_dir())
            self.assertFalse((root / "sample-skill" / "assets").exists())

            validated = self.run_command(str(VALIDATE), str(root), cwd=root)
            self.assertEqual(validated.returncode, 0, validated.stdout + validated.stderr)

    def test_rejects_invalid_name(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            result = self.run_command(
                str(NEW_SKILL),
                "Invalid_Name",
                "--path",
                str(root),
                "--description",
                "Invalid example.",
                "--short-description",
                "Create dependable sample workflow outputs",
                "--default-prompt",
                "Use $Invalid_Name to complete the workflow.",
                cwd=root,
            )
            self.assertNotEqual(result.returncode, 0)

    def test_detects_frontmatter_name_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            skill = root / "sample-skill"
            (skill / "agents").mkdir(parents=True)
            (skill / "SKILL.md").write_text(
                '---\nname: "other-name"\ndescription: "A valid description."\n---\n\n# Body\n',
                encoding="utf-8",
            )
            (skill / "README.md").write_text(
                "# Sample Skill\n\n## 功能\n\nSample.\n\n## 使用\n\nUse `$sample-skill`.\n",
                encoding="utf-8",
            )
            (skill / "agents" / "openai.yaml").write_text(
                'interface:\n'
                '  display_name: "Sample Skill"\n'
                '  short_description: "Create dependable sample workflow outputs"\n'
                '  default_prompt: "Use $sample-skill to complete the workflow."\n',
                encoding="utf-8",
            )

            result = self.run_command(str(VALIDATE), str(root), cwd=root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("must match folder name", result.stdout)

    def test_requires_readme(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            skill = root / "sample-skill"
            (skill / "agents").mkdir(parents=True)
            (skill / "SKILL.md").write_text(
                '---\nname: "sample-skill"\ndescription: "A valid description."\n---\n\n# Body\n',
                encoding="utf-8",
            )
            (skill / "agents" / "openai.yaml").write_text(
                'interface:\n'
                '  display_name: "Sample Skill"\n'
                '  short_description: "Create dependable sample workflow outputs"\n'
                '  default_prompt: "Use $sample-skill to complete the workflow."\n',
                encoding="utf-8",
            )

            result = self.run_command(str(VALIDATE), str(root), cwd=root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("README.md is required", result.stdout)


if __name__ == "__main__":
    unittest.main()
