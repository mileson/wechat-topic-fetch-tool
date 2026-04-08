#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = SKILL_ROOT / "scripts"
SKILLS_ROOT = SKILL_ROOT.parent
REFERENCES_DIR = SKILL_ROOT / "references"
DATA_DIR = SKILL_ROOT / "data"


def sibling_skill_path(name: str) -> Path:
    return SKILLS_ROOT / name
