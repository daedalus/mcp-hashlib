#!/usr/bin/env python3
"""Install skill to agent directories."""

from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path

AGENT_DIRECTORIES = {
    "claude": Path.home() / ".claude" / "skills",
    "opencode": Path.home() / ".opencode" / "skills",
}

PROJECT_NAME = "mcp-hashlib"
SOURCE_DIR = Path(__file__).parent.parent / "skills" / PROJECT_NAME


def find_agent_dirs() -> dict[str, Path]:
    """Find available agent skill directories."""
    found = {}
    for agent, base_dir in AGENT_DIRECTORIES.items():
        if base_dir.exists():
            found[agent] = base_dir
    return found


def install_skill(agent: str, target_dir: Path) -> bool:
    """Install the skill to the target directory."""
    target_path = target_dir / PROJECT_NAME

    if target_path.exists():
        if target_path.is_symlink():
            target_path.unlink()
        elif target_path.is_dir():
            shutil.rmtree(target_path)

    try:
        os.symlink(SOURCE_DIR.resolve(), target_path)
        print(f"Installed {PROJECT_NAME} to {agent} at {target_path}")
        return True
    except OSError:
        shutil.copytree(SOURCE_DIR.resolve(), target_path)
        print(f"Copied {PROJECT_NAME} to {agent} at {target_path}")
        return True


def main() -> int:
    if not SOURCE_DIR.exists():
        print(f"Error: Skill source not found at {SOURCE_DIR}", file=sys.stderr)
        return 1

    agents = find_agent_dirs()
    if not agents:
        print("No agent skill directories found", file=sys.stderr)
        return 1

    print(f"Found agents: {', '.join(agents.keys())}")

    for agent, target_dir in agents.items():
        install_skill(agent, target_dir)

    print("\nInstallation complete!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
