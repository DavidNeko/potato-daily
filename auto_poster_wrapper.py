#!/usr/bin/env python3
"""
Smart Potato Blog Auto Poster Wrapper
每天自动思考和发帖
"""
import sys
import os
import subprocess
from pathlib import Path

PROJECT_DIR = Path(__file__).parent
sys.path.insert(0, str(PROJECT_DIR))

def main():
    print(f"[Smart Potato Blog] Starting at: {__import__('datetime').datetime.now()}")

    # 运行 autonomous_poster
    poster_path = PROJECT_DIR / "agents" / "autonomous_poster.py"
    result = subprocess.run(
        [sys.executable, str(poster_path)],
        cwd=str(PROJECT_DIR),
        capture_output=True,
        text=True
    )

    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)

    if result.returncode != 0:
        print(f"[ERROR] Poster failed with code {result.returncode}")
        return 1

    print(f"[Smart Potato Blog] Finished at: {__import__('datetime').datetime.now()}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
