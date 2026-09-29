from pathlib import Path
import json
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"; DATA.mkdir(parents=True, exist_ok=True)
clouds, layers = ["aws", "azure", "gcp"], ["raw", "curated", "analytics"]
buckets = [f"{c}-{l}-dev" for c in clouds for l in layers]
(DATA / "bucket_inventory.json").write_text(json.dumps({"buckets": buckets, "count": len(buckets)}, indent=2), encoding="utf-8")
(DATA / "ALLOW_APPLY").write_text("never\n", encoding="utf-8")
print("buckets", len(buckets))
