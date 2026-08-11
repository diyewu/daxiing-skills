#!/usr/bin/env python3
"""Validate every top-level Codex Skill in this repository."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FORBIDDEN_DOCS = {
    "INSTALLATION_GUIDE.md",
    "QUICK_REFERENCE.md",
    "CHANGELOG.md",
}


def scalar(value: str) -> str:
    value = value.strip()
    if value.startswith(('"', "'")):
        try:
            return json.loads(value) if value.startswith('"') else value[1:-1]
        except (json.JSONDecodeError, IndexError):
            return ""
    return value


def parse_skill_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        return {}, ["SKILL.md must start with YAML front matter"]

    try:
        closing = lines.index("---", 1)
    except ValueError:
        return {}, ["SKILL.md front matter is not closed"]

    fields: dict[str, str] = {}
    for line in lines[1:closing]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")) or ":" not in line:
            errors.append(f"unsupported front matter line: {line!r}")
            continue
        key, value = line.split(":", 1)
        if key in fields:
            errors.append(f"duplicate front matter field: {key}")
        fields[key] = scalar(value)

    if not any(line.strip() for line in lines[closing + 1 :]):
        errors.append("SKILL.md body must not be empty")
    return fields, errors


def yaml_interface_value(text: str, key: str) -> str | None:
    match = re.search(rf"^\s{{2}}{re.escape(key)}:\s*(.+?)\s*$", text, re.MULTILINE)
    return scalar(match.group(1)) if match else None


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    name = skill_dir.name
    if len(name) >= 64 or not NAME_RE.fullmatch(name):
        errors.append("folder name must be under 64 characters and use lowercase letters, digits, and hyphens")

    fields, frontmatter_errors = parse_skill_frontmatter(skill_dir / "SKILL.md")
    errors.extend(frontmatter_errors)
    if set(fields) != {"name", "description"}:
        errors.append("SKILL.md front matter must contain exactly name and description")
    if fields.get("name") != name:
        errors.append(f"front matter name must match folder name {name!r}")
    if not fields.get("description", "").strip():
        errors.append("description must not be empty")

    readme_path = skill_dir / "README.md"
    if not readme_path.is_file():
        errors.append("README.md is required for every Skill")
    else:
        readme = readme_path.read_text(encoding="utf-8")
        if "## 功能" not in readme:
            errors.append("README.md must contain a 功能 section")
        if not re.search(r"^## (?:怎么)?使用\s*$", readme, re.MULTILINE):
            errors.append("README.md must contain a 使用 section")
        if f"${name}" not in readme:
            errors.append(f"README.md must show how to invoke ${name}")

    for filename in sorted(FORBIDDEN_DOCS):
        if (skill_dir / filename).exists():
            errors.append(f"remove auxiliary document {filename} from the Skill directory")

    interface_path = skill_dir / "agents" / "openai.yaml"
    if not interface_path.is_file():
        errors.append("agents/openai.yaml is required by this repository")
        return errors

    text = interface_path.read_text(encoding="utf-8")
    if not re.search(r"^interface:\s*$", text, re.MULTILINE):
        errors.append("agents/openai.yaml must contain an interface mapping")
    for key in ("display_name", "short_description", "default_prompt"):
        value = yaml_interface_value(text, key)
        if not value:
            errors.append(f"agents/openai.yaml is missing interface.{key}")

    short_description = yaml_interface_value(text, "short_description") or ""
    if short_description and not 25 <= len(short_description) <= 64:
        errors.append("interface.short_description must contain 25-64 characters")
    default_prompt = yaml_interface_value(text, "default_prompt") or ""
    if default_prompt and f"${name}" not in default_prompt:
        errors.append(f"interface.default_prompt must explicitly mention ${name}")
    return errors


def discover(path: Path) -> list[Path]:
    path = path.expanduser().resolve()
    if (path / "SKILL.md").is_file():
        return [path]
    return sorted(
        child for child in path.iterdir() if child.is_dir() and (child / "SKILL.md").is_file()
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=Path.cwd())
    args = parser.parse_args()

    skills = discover(args.path)
    if not skills:
        print("No Skill directories found; repository foundation is valid.")
        return 0

    failures = 0
    for skill in skills:
        errors = validate_skill(skill)
        if errors:
            failures += 1
            print(f"FAIL {skill}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK   {skill}")

    if failures:
        print(f"Validation failed for {failures} Skill(s).")
        return 1
    print(f"Validated {len(skills)} Skill(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
