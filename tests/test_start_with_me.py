from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "start-with-me"


class StartWithMeSkillTest(unittest.TestCase):
    def read(self, relative_path: str) -> str:
        return (SKILL_ROOT / relative_path).read_text(encoding="utf-8")

    def test_runtime_package_is_minimal(self) -> None:
        expected_files = {
            "SKILL.md",
            "README.md",
            "agents/openai.yaml",
            "references/interaction-modes.md",
            "references/scenario-playbook.md",
        }
        actual_files = {
            str(path.relative_to(SKILL_ROOT))
            for path in SKILL_ROOT.rglob("*")
            if path.is_file()
        }
        self.assertEqual(actual_files, expected_files)

    def test_readme_explains_purpose_and_usage(self) -> None:
        text = self.read("README.md")
        self.assertIn("## 功能", text)
        self.assertIn("## 怎么使用", text)
        self.assertIn("$start-with-me", text)
        self.assertIn("## 能力边界", text)

    def test_skill_contains_starting_contract(self) -> None:
        text = self.read("SKILL.md")
        for marker in (
            "这轮只做：",
            "第一步：",
            "做到这里就算完成：",
            "完成 / 卡住 / 暂停",
            "本轮状态：",
            "下次先做：",
        ):
            self.assertIn(marker, text)
        self.assertIn("no more than two setup questions", text)
        self.assertIn("offer at most three smaller routes", text)

    def test_modes_and_misfire_boundaries_are_defined(self) -> None:
        skill = self.read("SKILL.md")
        modes = self.read("references/interaction-modes.md")
        for mode in ("`start`", "`unstick`", "`resume`", "`reset`"):
            self.assertIn(mode, modes)
        for mode in ("`quiet`", "`gentle`", "`steady`"):
            self.assertIn(mode, modes)
        for rhythm in ("`untimed`", "`countdown`", "`flow`"):
            self.assertIn(rhythm, modes)
        for boundary in (
            "technical troubleshooting",
            "full project planning",
            "long-term task tracking",
            "standalone timer request",
        ):
            self.assertIn(boundary, skill)
        self.assertIn("Do not promise a plan, ongoing tracking, stored state, or future follow-up", skill)

    def test_quick_start_and_start_ritual_are_bounded(self) -> None:
        skill = self.read("SKILL.md")
        modes = self.read("references/interaction-modes.md")
        self.assertIn("use quick start", skill)
        self.assertIn("30-second start ritual", skill)
        self.assertIn("no more than three actions", skill)
        self.assertIn("Do not use quick start when a missing fact could make the action unsafe", modes)

    def test_sidetrack_and_momentum_protocols_are_defined(self) -> None:
        skill = self.read("SKILL.md")
        scenarios = self.read("references/scenario-playbook.md")
        for marker in (
            "先放旁边：",
            "现在回来做：",
            "已经启动：",
            "下一小段：",
            "做到这里可以再停：",
        ):
            self.assertIn(marker, skill)
            self.assertIn(marker, scenarios)

    def test_resume_capsule_is_copyable_and_minimal(self) -> None:
        skill = self.read("SKILL.md")
        for marker in ("本轮状态：", "已经推进：", "停在：", "下次先做：", "需要打开："):
            self.assertIn(marker, skill)
        self.assertIn("do not turn it into a detailed report", skill)

    def test_cross_skill_work_preserves_session_contract(self) -> None:
        skill = self.read("SKILL.md")
        scenarios = self.read("references/scenario-playbook.md")
        self.assertIn("Let `start-with-me` hold the companionship contract", skill)
        self.assertIn("Preserve the current target, enough point, rhythm, and return signal", scenarios)

    def test_countdown_end_is_not_completion(self) -> None:
        skill = self.read("SKILL.md")
        modes = self.read("references/interaction-modes.md")
        self.assertIn("treat time ending as a check-in, never as proof of completion", skill)
        self.assertIn("A `countdown` ending is a check-in event, not a completion transition", modes)

    def test_timer_and_persistence_claims_are_guarded(self) -> None:
        text = self.read("SKILL.md")
        self.assertIn(
            "Never claim that a timer, background wait, notification, or future check-in exists unless a tool actually created it.",
            text,
        )
        self.assertIn(
            "Do not save task details, session history, or user preferences unless the user explicitly asks",
            text,
        )

    def test_ui_metadata_matches_skill(self) -> None:
        text = self.read("agents/openai.yaml")
        self.assertIn('display_name: "Start With Me"', text)
        self.assertIn("$start-with-me", text)
        self.assertNotIn("TODO", text)

    def test_runtime_has_no_placeholders(self) -> None:
        for path in SKILL_ROOT.rglob("*"):
            if path.is_file():
                self.assertNotIn("TODO", path.read_text(encoding="utf-8"), path)


if __name__ == "__main__":
    unittest.main()
