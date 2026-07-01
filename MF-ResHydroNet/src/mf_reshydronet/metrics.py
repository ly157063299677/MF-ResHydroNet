"""Evaluation metrics for hydrodynamic reconstruction."""

from __future__ import annotations

from collections import defaultdict
from typing import Iterable

import numpy as np


def _as_array(values: Iterable[float]) -> np.ndarray:
    arr = np.asarray(list(values), dtype=float)
    if arr.ndim != 1:
        arr = arr.reshape(-1)
    if arr.size == 0:
        raise ValueError("metric input is empty")
    return arr


def mae(y_true: Iterable[float], y_pred: Iterable[float]) -> float:
    true = _as_array(y_true)
    pred = _as_array(y_pred)
    return float(np.mean(np.abs(pred - true)))


def rmse(y_true: Iterable[float], y_pred: Iterable[float]) -> float:
    true = _as_array(y_true)
    pred = _as_array(y_pred)
    return float(np.sqrt(np.mean((pred - true) ** 2)))


def r2_score(y_true: Iterable[float], y_pred: Iterable[float]) -> float:
    true = _as_array(y_true)
    pred = _as_array(y_pred)
    ss_res = float(np.sum((true - pred) ** 2))
    ss_tot = float(np.sum((true - np.mean(true)) ** 2))
    if ss_tot == 0:
        return float("nan")
    return 1.0 - ss_res / ss_tot


def error_reduction(raw_rmse: float, corrected_rmse: float) -> float:
    if raw_rmse == 0:
        return float("nan")
    return (raw_rmse - corrected_rmse) / raw_rmse * 100.0


def grouped_metrics(rows: list[dict], group_fields: tuple[str, ...] = ("model", "variable")) -> list[dict]:
    """Aggregate prediction rows into MAE, RMSE, and R2 by group.

    Expected row fields are ``observed`` and ``predicted`` plus any group fields.
    """

    groups: dict[tuple[str, ...], list[dict]] = defaultdict(list)
    for row in rows:
        key = tuple(str(row[field]) for field in group_fields)
        groups[key].append(row)

    out = []
    for key, group in sorted(groups.items()):
        observed = [float(row["observed"]) for row in group]
        predicted = [float(row["predicted"]) for row in group]
        record = {field: value for field, value in zip(group_fields, key)}
        record.update(
            {
                "n": len(group),
                "mae": mae(observed, predicted),
                "rmse": rmse(observed, predicted),
                "r2": r2_score(observed, predicted),
            }
        )
        out.append(record)
    return out

