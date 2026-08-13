#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path


def skill_root() -> Path:
    return Path(__file__).resolve().parent.parent


def load_registry(root: Path | None = None) -> dict:
    root = root or skill_root()
    refs = root / "references"
    index = json.loads((refs / "factor-registry.json").read_text(encoding="utf-8"))
    factors = []
    for rel in index.get("factor_files", []):
        payload = json.loads((refs / rel).read_text(encoding="utf-8"))
        factors.extend(payload.get("factors", []))
    out = dict(index)
    out["factors"] = factors
    return out
