from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "pick-something-fun"


class PickSomethingFunSkillTest(unittest.TestCase):
    def read(self, relative_path: str) -> str:
        return (SKILL_ROOT / relative_path).read_text(encoding="utf-8")

    def test_runtime_package_is_minimal(self) -> None:
        expected_files = {
            "SKILL.md",
            "README.md",
            "agents/openai.yaml",
            "references/decision-framework.md",
            "references/live-facts-and-actions.md",
        }
        actual_files = {
            str(path.relative_to(SKILL_ROOT))
            for path in SKILL_ROOT.rglob("*")
            if path.is_file()
        }
        self.assertEqual(actual_files, expected_files)

    def test_readme_explains_purpose_usage_and_boundaries(self) -> None:
        text = self.read("README.md")
        self.assertIn("## 功能", text)
        self.assertIn("## 怎么使用", text)
        self.assertIn("$pick-something-fun", text)
        self.assertIn("## 能力边界", text)
        self.assertIn("默认不会保存", text)

    def test_routing_boundaries_are_explicit(self) -> None:
        text = self.read("SKILL.md")
        for boundary in (
            "multi-day trip",
            "factual lookup",
            "large party",
            "calendar, reminder, invitation, purchase, booking, or message action",
            "starting a known work, study, or household task",
        ):
            self.assertIn(boundary, text)

    def test_decision_modes_and_question_limit_are_defined(self) -> None:
        skill = self.read("SKILL.md")
        reference = self.read("references/decision-framework.md")
        for mode in ("`quick-pick`", "`compare`", "`shape-it`"):
            self.assertIn(mode, skill)
        self.assertIn("Ask at most one material question per response", skill)
        self.assertIn("no more than three options", reference)
        self.assertIn("Never use a survey", skill)

    def test_hard_constraints_precede_novelty(self) -> None:
        skill = self.read("SKILL.md")
        reference = self.read("references/decision-framework.md")
        self.assertIn("Reject any option that violates a hard constraint", skill)
        self.assertIn("Novelty never overrides safety", skill)
        self.assertIn("Never let novelty or a “surprise” mode override a hard constraint", reference)

    def test_live_facts_must_be_verified_or_labeled(self) -> None:
        skill = self.read("SKILL.md")
        live = self.read("references/live-facts-and-actions.md")
        for item in ("opening hours", "showtime", "ticket availability", "current price"):
            self.assertIn(item, skill)
        self.assertIn("Never invent a venue, event, price, rating, opening hour, showtime, ticket, route, link, or streaming availability", skill)
        self.assertIn("Only `verified-current` facts may be stated as current without qualification", live)

    def test_direct_sources_are_preferred(self) -> None:
        skill = self.read("SKILL.md")
        live = self.read("references/live-facts-and-actions.md")
        self.assertIn("Prefer direct sources", skill)
        self.assertIn("organizer, venue, cinema, museum, park", live)
        self.assertIn("Do not use a search result snippet as the sole proof", live)

    def test_decision_card_is_actionable_and_not_padded(self) -> None:
        skill = self.read("SKILL.md")
        for marker in ("今天就选：", "为什么合适：", "怎么开始：", "时间与预算：", "出发前确认："):
            self.assertIn(marker, skill)
        self.assertIn("Do not include a rating, review count, price, or travel time merely to make the card look complete", skill)

    def test_external_actions_require_confirmation_and_tool_success(self) -> None:
        skill = self.read("SKILL.md")
        live = self.read("references/live-facts-and-actions.md")
        self.assertIn("confirm the exact plan and target", skill)
        self.assertIn("report success only from the tool result", skill)
        self.assertIn("An accepted idea does not authorize an external write", live)
        self.assertIn("Without a messaging tool, draft a copyable message and say it was not sent", live)

    def test_persistence_is_opt_in(self) -> None:
        skill = self.read("SKILL.md")
        live = self.read("references/live-facts-and-actions.md")
        self.assertIn("Do not collect or save preferences, contacts, history, or location by default", skill)
        self.assertIn("Do not persist this decision", skill)
        self.assertIn("Save only after explicit authorization and a real write", live)

    def test_safety_filters_cover_material_constraints(self) -> None:
        skill = self.read("SKILL.md")
        live = self.read("references/live-facts-and-actions.md")
        for marker in ("accessibility", "dietary", "age", "transport", "weather"):
            self.assertIn(marker, skill.lower())
        self.assertIn("Do not suggest driving after alcohol use", live)
        self.assertIn("Do not guarantee allergen safety", live)

    def test_long_references_have_contents(self) -> None:
        for relative_path in (
            "references/decision-framework.md",
            "references/live-facts-and-actions.md",
        ):
            text = self.read(relative_path)
            self.assertIn("## Contents", text)
            self.assertGreater(len(text.splitlines()), 100)

    def test_ui_metadata_matches_skill(self) -> None:
        text = self.read("agents/openai.yaml")
        self.assertIn('display_name: "Pick Something Fun"', text)
        self.assertIn("$pick-something-fun", text)
        self.assertNotIn("TODO", text)

    def test_runtime_has_no_placeholders(self) -> None:
        for path in SKILL_ROOT.rglob("*"):
            if path.is_file():
                self.assertNotIn("TODO", path.read_text(encoding="utf-8"), path)


if __name__ == "__main__":
    unittest.main()
