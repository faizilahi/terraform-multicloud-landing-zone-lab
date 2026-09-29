import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    tf = shutil.which("terraform")
    env_dir = ROOT / "envs" / "teaching"
    if tf:
        print("Using terraform fmt -check -recursive")
        r = subprocess.run([tf, "fmt", "-check", "-recursive", str(ROOT)], capture_output=True, text=True)
        if r.stdout:
            print(r.stdout)
        if r.returncode != 0:
            print(r.stderr)
            return r.returncode
        print("terraform fmt -check passed")
        return 0
    print("terraform not found — running Python HCL checker")
    sys.path.insert(0, str(ROOT / "src"))
    from hcl_checker import main as hcl_main

    return hcl_main(ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
