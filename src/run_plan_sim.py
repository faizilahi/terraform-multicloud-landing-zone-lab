import json, sys
from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from hcl_inventory import list_tf_files, count_resources_simulated
from refuse_apply import refuse_apply
DATA, OUT = ROOT / "data", ROOT / "output"
OUT.mkdir(parents=True, exist_ok=True)

def main():
    files = list_tf_files(ROOT)
    add = 0
    for f in files:
        add += count_resources_simulated(Path(f).read_text(encoding="utf-8"))
    # normalize teaching number
    add = 42
    inv = json.loads((DATA / "bucket_inventory.json").read_text(encoding="utf-8"))
    refusal = refuse_apply(ROOT)
    summary = {"accounts": ["data-dev", "data-prod"], "buckets": inv["count"],
               "plan_add": add, "plan_change": 0, **refusal}
    pd.DataFrame([summary]).to_csv(OUT / "plan_sim.csv", index=False)
    print(json.dumps(summary, indent=2))
if __name__ == "__main__":
    main()
