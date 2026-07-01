#!/usr/bin/env python
"""Small smoke tests that do not require private data or PyTorch."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from mf_reshydronet.data import generate_demo_pairs, grouped_condition_location_split, rows_to_matrix, write_csv  # noqa: E402
from mf_reshydronet.metrics import mae, r2_score, rmse  # noqa: E402
from mf_reshydronet.ridge import ResidualRidge  # noqa: E402


def assert_close(value: float, expected: float, tol: float = 1e-12) -> None:
    if abs(value - expected) > tol:
        raise AssertionError(f"{value} != {expected}")


def test_metrics() -> None:
    y = [1.0, 2.0, 3.0]
    pred = [1.0, 2.0, 4.0]
    assert_close(mae(y, pred), 1.0 / 3.0)
    assert_close(rmse(y, pred), (1.0 / 3.0) ** 0.5)
    if r2_score(y, pred) <= 0:
        raise AssertionError("R2 should be positive for this toy example")


def test_residual_ridge() -> None:
    rows = generate_demo_pairs(n_points_per_condition=8)
    x, y, baseline = rows_to_matrix(rows)
    model = ResidualRidge(alpha=1e-2).fit(x, y, baseline)
    pred = model.predict(x, baseline)
    if pred.shape != y.shape:
        raise AssertionError("prediction shape mismatch")
    if rmse(y[:, 0], pred[:, 0]) >= rmse(y[:, 0], baseline[:, 0]):
        raise AssertionError("residual model should improve water-level demo RMSE")


def test_grouped_split() -> None:
    rows = generate_demo_pairs(n_points_per_condition=8)
    splits = grouped_condition_location_split(rows)
    assignments = {}
    for split_name, indices in zip(("train", "validation", "test"), splits):
        for idx in indices:
            row = rows[int(idx)]
            key = (row["condition_key"], row["sample_id"])
            if key in assignments and assignments[key] != split_name:
                raise AssertionError("condition-location group leaked across subsets")
            assignments[key] = split_name


def test_scripts() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        pairs = tmp_path / "pairs.csv"
        out_dir = tmp_path / "out"
        write_csv(pairs, generate_demo_pairs(n_points_per_condition=8))
        subprocess.run([sys.executable, str(ROOT / "scripts" / "train_demo.py"), "--pairs", str(pairs), "--out-dir", str(out_dir)], check=True)
        if not (out_dir / "demo_predictions.csv").exists():
            raise AssertionError("demo predictions were not written")
        if not (out_dir / "demo_metrics.csv").exists():
            raise AssertionError("demo metrics were not written")


if __name__ == "__main__":
    test_metrics()
    test_residual_ridge()
    test_grouped_split()
    test_scripts()
    print("Smoke tests passed.")
