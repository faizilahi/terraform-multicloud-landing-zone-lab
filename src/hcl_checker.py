"""Lightweight HCL structure validator when terraform CLI is missing."""
from __future__ import annotations

import re
import sys
from pathlib import Path


def check_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    if text.count("{") != text.count("}"):
        errors.append(f"{path}: unbalanced braces")
    for i, line in enumerate(text.splitlines(), 1):
        if line.strip().endswith("="):
            errors.append(f"{path}:{i}: dangling '='")
    return errors


def main(root: Path) -> int:
    all_errors: list[str] = []
    for tf in root.rglob("*.tf"):
        all_errors.extend(check_file(tf))
    if all_errors:
        for e in all_errors:
            print("ERROR:", e)
        return 1
    print(f"HCL structure OK ({len(list(root.rglob('*.tf')))} files)")
    return 0


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    sys.exit(main(root))
