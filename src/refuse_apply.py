from pathlib import Path

def refuse_apply(repo: Path) -> dict:
    reasons = []
    sentinel = repo / "data" / "ALLOW_APPLY"
    if not sentinel.exists() or sentinel.read_text(encoding="utf-8").strip() != "never":
        reasons.append("ALLOW_APPLY sentinel missing or not 'never'")
    # refuse if env vars look real (simulation checks files only)
    for p in repo.rglob("*.tf"):
        txt = p.read_text(encoding="utf-8")
        if "AKIA" in txt or "BEGIN RSA" in txt:
            reasons.append(f"credential-like material in {p.name}")
    return {"apply_allowed": False, "refuse_reasons": reasons or ["teaching lab: apply disabled by policy"],
            "action": "REFUSE_APPLY"}
