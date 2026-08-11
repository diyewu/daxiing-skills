#!/usr/bin/env python3
"""Create a minimal, repository-compliant Codex Skill skeleton."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
RESOURCE_NAMES = {"scripts", "references", "assets"}


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def parse_resources(value: str) -> list[str]:
    if not value:
        return []
    resources = [item.strip() for item in value.split(",") if item.strip()]
    unknown = sorted(set(resources) - RESOURCE_NAMES)
    if unknown:
        raise argparse.ArgumentTypeError(
            "unknown resource directories: " + ", ".join(unknown)
        )
    return list(dict.fromkeys(resources))


def valid_name(value: str) -> str:
    if len(value) >= 64 or not NAME_RE.fullmatch(value):
        raise argparse.ArgumentTypeError(
            "name must be under 64 characters and use lowercase letters, digits, and hyphens"
        )
    return value


def validate_interface(args: argparse.Namespace) -> None:
    length = len(args.short_description)
    if not 25 <= length <= 64:
        raise SystemExit("--short-description must contain 25-64 characters")
    if f"${args.name}" not in args.default_prompt:
        raise SystemExit(f"--default-prompt must explicitly mention ${args.name}")


def skill_markdown(name: str, description: str) -> str:
    return f"""---
name: {yaml_string(name)}
description: {yaml_string(description)}
---

# {name}

## Workflow

1. TODO: Describe the first required action.
2. TODO: Describe the core execution steps and decision points.
3. TODO: Describe validation and the stopping condition.

## Resources

- TODO: Explain when to read or run each bundled resource. Remove this section when no resources are needed.
"""


def readme_markdown(name: str, display_name: str, description: str) -> str:
    return f"""# {display_name}

## 功能

{description}

## 使用

在 Codex 中显式调用 `${name}`，并说明你希望完成的事情和已有材料。

```text
Use ${name} to help me complete this task.
```

使用前请根据实际 Skill 内容补充适用场景、具体示例和能力边界。
"""


def openai_yaml(
    display_name: str, short_description: str, default_prompt: str
) -> str:
    return f"""interface:
  display_name: {yaml_string(display_name)}
  short_description: {yaml_string(short_description)}
  default_prompt: {yaml_string(default_prompt)}
"""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name", type=valid_name)
    parser.add_argument("--path", type=Path, default=Path.cwd())
    parser.add_argument("--description", required=True)
    parser.add_argument("--display-name")
    parser.add_argument("--short-description", required=True)
    parser.add_argument("--default-prompt", required=True)
    parser.add_argument("--resources", type=parse_resources, default=[])
    return parser


def main() -> int:
    args = build_parser().parse_args()
    validate_interface(args)

    target = args.path.expanduser().resolve() / args.name
    if target.exists():
        raise SystemExit(f"target already exists: {target}")

    display_name = args.display_name or args.name.replace("-", " ").title()
    (target / "agents").mkdir(parents=True)
    for resource in args.resources:
        (target / resource).mkdir()

    (target / "SKILL.md").write_text(
        skill_markdown(args.name, args.description), encoding="utf-8"
    )
    (target / "README.md").write_text(
        readme_markdown(args.name, display_name, args.description), encoding="utf-8"
    )
    (target / "agents" / "openai.yaml").write_text(
        openai_yaml(display_name, args.short_description, args.default_prompt),
        encoding="utf-8",
    )

    print(f"Created {target}")
    print("Next: replace every TODO, add only necessary resources, then run make check.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
