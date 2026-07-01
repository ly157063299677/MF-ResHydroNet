#!/usr/bin/env python
"""Export IEEE Access manuscript-reference summary tables as CSV."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from mf_reshydronet.tables import write_reference_tables  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", type=Path, default=ROOT / "outputs" / "reference_tables")
    args = parser.parse_args()
    write_reference_tables(args.out_dir)
    print(f"Wrote manuscript-reference tables under {args.out_dir}")


if __name__ == "__main__":
    main()
