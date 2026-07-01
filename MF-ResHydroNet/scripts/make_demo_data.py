#!/usr/bin/env python
"""Generate a deterministic demo paired dataset.

The generated file follows the repository data contract but is not the
manuscript dataset.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from mf_reshydronet.data import generate_demo_pairs, write_csv  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=ROOT / "data" / "demo" / "demo_pairs.csv")
    parser.add_argument("--points-per-condition", type=int, default=24)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    rows = generate_demo_pairs(n_points_per_condition=args.points_per_condition, seed=args.seed)
    write_csv(args.out, rows)
    print(f"Wrote {len(rows)} rows to {args.out}")


if __name__ == "__main__":
    main()

