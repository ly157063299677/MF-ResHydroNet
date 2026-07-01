#!/usr/bin/env python
"""Aggregate prediction CSV files into MAE/RMSE/R2 metrics."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from mf_reshydronet.data import read_csv, write_csv  # noqa: E402
from mf_reshydronet.metrics import grouped_metrics  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--predictions", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--group-fields", default="model,variable,subset")
    args = parser.parse_args()

    rows = read_csv(args.predictions)
    groups = tuple(field.strip() for field in args.group_fields.split(",") if field.strip())
    metrics = grouped_metrics(rows, group_fields=groups)
    write_csv(args.out, metrics)
    print(f"Wrote {len(metrics)} metric rows: {args.out}")


if __name__ == "__main__":
    main()

