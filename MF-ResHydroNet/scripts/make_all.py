#!/usr/bin/env python
"""Run the lightweight reproducibility demo pipeline."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable


def run(args: list[str]) -> None:
    print("+", " ".join(args))
    subprocess.run(args, check=True, cwd=ROOT)


def main() -> None:
    run([PYTHON, "scripts/make_demo_data.py"])
    run([PYTHON, "scripts/train_demo.py"])
    run([PYTHON, "scripts/build_reference_tables.py"])
    run([PYTHON, "scripts/scenario_screening.py"])


if __name__ == "__main__":
    main()

