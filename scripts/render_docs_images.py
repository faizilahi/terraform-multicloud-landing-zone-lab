from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

OUT = Path(__file__).resolve().parents[1] / "docs" / "images"
OUT.mkdir(parents=True, exist_ok=True)
fig, ax = plt.subplots(figsize=(8, 3))
ax.axis("off")
boxes = [("AWS VPC + S3", 0.1), ("GCP VPC + GCS", 0.4), ("Azure RG + Storage", 0.7)]
colors = ["#FF9900", "#4285F4", "#0078D4"]
for (label, x), c in zip(boxes, colors):
    rect = mpatches.FancyBboxPatch((x, 0.35), 0.22, 0.3, boxstyle="round", fc=c, alpha=0.3)
    ax.add_patch(rect)
    ax.text(x + 0.11, 0.5, label, ha="center", va="center", fontsize=9)
ax.set_title("Multicloud landing zone teaching skeleton")
fig.savefig(OUT / "multicloud_skeleton.png", dpi=120, bbox_inches="tight")
plt.close(fig)
