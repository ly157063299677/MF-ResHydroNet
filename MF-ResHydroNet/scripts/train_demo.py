#!/usr/bin/env python
"""Train a lightweight residual ridge demo model and export predictions."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from mf_reshydronet.data import grouped_condition_location_split, read_csv, rows_to_matrix, subset_rows, write_csv  # noqa: E402
from mf_reshydronet.metrics import grouped_metrics  # noqa: E402
from mf_reshydronet.ridge import ResidualRidge  # noqa: E402


VARIABLE_NAMES = [
    "water_level",
    "velocity_magnitude",
    "flow_direction",
    "transverse_velocity",
    "tke_stat",
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pairs", type=Path, default=ROOT / "data" / "demo" / "demo_pairs.csv")
    parser.add_argument("--out-dir", type=Path, default=ROOT / "outputs" / "demo")
    parser.add_argument("--alpha", type=float, default=1e-2)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    rows = read_csv(args.pairs)
    train_idx, _, test_idx = grouped_condition_location_split(rows, seed=args.seed)
    train_rows = subset_rows(rows, train_idx)
    test_rows = subset_rows(rows, test_idx)
    x_train, y_train, baseline_train = rows_to_matrix(train_rows)
    x_test, y_test, baseline_test = rows_to_matrix(test_rows)

    model = ResidualRidge(alpha=args.alpha).fit(x_train, y_train, baseline_train)
    predicted = model.predict(x_test, baseline_test)
    raw_pred = baseline_test

    prediction_rows = []
    for i, row in enumerate(test_rows):
        for j, variable in enumerate(VARIABLE_NAMES):
            prediction_rows.append(
                {
                    "model": "Lower-fidelity baseline",
                    "variable": variable,
                    "subset": "demo_test",
                    "condition_key": row["condition_key"],
                    "mesh_m": row["mesh_m"],
                    "sample_id": row["sample_id"],
                    "observed": f"{y_test[i, j]:.10g}",
                    "predicted": f"{raw_pred[i, j]:.10g}",
                }
            )
            prediction_rows.append(
                {
                    "model": "Residual ridge demo",
                    "variable": variable,
                    "subset": "demo_test",
                    "condition_key": row["condition_key"],
                    "mesh_m": row["mesh_m"],
                    "sample_id": row["sample_id"],
                    "observed": f"{y_test[i, j]:.10g}",
                    "predicted": f"{predicted[i, j]:.10g}",
                }
            )

    args.out_dir.mkdir(parents=True, exist_ok=True)
    pred_path = args.out_dir / "demo_predictions.csv"
    metrics_path = args.out_dir / "demo_metrics.csv"
    write_csv(pred_path, prediction_rows)
    metrics = grouped_metrics(prediction_rows, group_fields=("model", "variable"))
    write_csv(metrics_path, [{k: (f"{v:.10g}" if isinstance(v, float) and np.isfinite(v) else v) for k, v in row.items()} for row in metrics])
    print(f"Wrote predictions: {pred_path}")
    print(f"Wrote metrics: {metrics_path}")


if __name__ == "__main__":
    main()
