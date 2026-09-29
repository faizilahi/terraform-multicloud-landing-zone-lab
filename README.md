# Teaching HCL for a Data Landing Zone (No Apply)

[Faiz Elahi](https://www.linkedin.com/in/faizilahi) — [pendataco.com](https://pendataco.com) — [github.com/faizilahi](https://github.com/faizilahi)

Synthetic data only. No vendor-customer employment claim.

Terraform modules sketch a multi-cloud data landing zone. **We refuse to apply**
— this repo is plan/validate teaching only (`terraform plan` simulated).

## The accounts

`modules/accounts` — AWS account `data-dev` / `data-prod`, Azure subscription
placeholder, GCP project placeholder. IDs are synthetic.

## The buckets

`modules/buckets` — `raw`, `curated`, `analytics` prefixes with lifecycle rules
encoded in HCL. Inventory lists **9** bucket definitions.

## What we refuse to apply

`src/refuse_apply.py` blocks `terraform apply` when any of: real credentials
present, non-synthetic account ids, or missing `ALLOW_APPLY=never` sentinel.
Simulated plan: **42** resources to add, **0** changed, apply **refused**.

```powershell
pip install -r requirements.txt
python scripts/generate_synthetic_data.py
python src/run_plan_sim.py
```
