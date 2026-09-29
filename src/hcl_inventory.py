import re
from pathlib import Path

def list_tf_files(root: Path) -> list:
    return [p.as_posix() for p in root.rglob("*.tf")]

def count_resources_simulated(tf_text: str) -> int:
    # teaching sim: count locals/output blocks roughly
    return len(re.findall(r"\b(locals|output|variable)\b", tf_text))
