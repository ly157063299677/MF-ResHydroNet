#!/usr/bin/env python
"""Classify scenario-screening priority from reconstructed indicators."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from mf_reshydronet.data import read_csv, write_csv  # noqa: E402
from mf_reshydronet.scenario import screen_scenarios  # noqa: E402


DEMO_ROWS = [
    {
        "case_id": "HC-08",
        "mesh_used": "100 m",
        "yangtze_q_m3s": "12000",
        "dongting_q_m3s": "4000",
        "downstream_level_m": "22.487",
        "max_velocity_mps": "1.34",
        "max_abs_transverse_velocity_mps": "0.14",
    },
    {
        "case_id": "HC-12",
        "mesh_used": "100 m",
        "yangtze_q_m3s": "22000",
        "dongting_q_m3s": "11500",
        "downstream_level_m": "28.631",
        "max_velocity_mps": "1.65",
        "max_abs_transverse_velocity_mps": "0.19",
    },
    {
        "case_id": "HC-14",
        "mesh_used": "200 m",
        "yangtze_q_m3s": "35000",
        "dongting_q_m3s": "6000",
        "downstream_level_m": "30.083",
        "max_velocity_mps": "1.62",
        "max_abs_transverse_velocity_mps": "0.15",
    },
    {
        "case_id": "HC-16",
        "mesh_used": "200 m",
        "yangtze_q_m3s": "35000",
        "dongting_q_m3s": "18000",
        "downstream_level_m": "32.415",
        "max_velocity_mps": "1.83",
        "max_abs_transverse_velocity_mps": "0.20",
    },
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--indicators", type=Path, help="CSV with max_velocity_mps and max_abs_transverse_velocity_mps columns.")
    parser.add_argument("--out", type=Path, default=ROOT / "outputs" / "scenario_screening.csv")
    args = parser.parse_args()

    rows = read_csv(args.indicators) if args.indicators else DEMO_ROWS
    screened = screen_scenarios(rows)
    write_csv(args.out, screened)
    print(f"Wrote scenario-screening table: {args.out}")


if __name__ == "__main__":
    main()

