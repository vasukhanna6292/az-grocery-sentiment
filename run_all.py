from pathlib import Path
import subprocess, sys

ROOT = Path(__file__).resolve().parent

print("[1/2] Creating/refreshing dataset...")
subprocess.check_call([sys.executable, str(ROOT / "src" / "data" / "make_dataset.py")])

print("\n[2/2] Training ML baselines...")
subprocess.check_call([sys.executable, str(ROOT / "src" / "models" / "train_ml.py")])

print("\nAll done ✅")