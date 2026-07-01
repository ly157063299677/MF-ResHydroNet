"""Data contracts and demo-data generation for MF-ResHydroNet."""

from __future__ import annotations

import csv
import math
from pathlib import Path

import numpy as np

from .constants import HYDROLOGICAL_CONDITIONS, LOWER_FIDELITY_MESHES


FEATURE_COLUMNS = [
    "x",
    "y",
    "mesh_m",
    "fidelity_code",
    "yangtze_q_m3s",
    "dongting_q_m3s",
    "downstream_level_m",
    "water_level_lf",
    "velocity_magnitude_lf",
    "flow_direction_lf",
    "transverse_velocity_lf",
    "tke_stat_lf",
]

TARGET_COLUMNS = [
    "water_level_hf",
    "velocity_magnitude_hf",
    "flow_direction_hf",
    "transverse_velocity_hf",
    "tke_stat_hf",
]

REQUIRED_PAIR_COLUMNS = [
    "condition_key",
    "sample_id",
    "mesh_m",
    *FEATURE_COLUMNS,
    *TARGET_COLUMNS,
]


def read_csv(path: str | Path) -> list[dict]:
    with Path(path).open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: str | Path, rows: list[dict]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"no rows to write: {path}")
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def validate_pair_rows(rows: list[dict]) -> None:
    if not rows:
        raise ValueError("paired dataset is empty")
    missing = [col for col in REQUIRED_PAIR_COLUMNS if col not in rows[0]]
    if missing:
        raise ValueError(f"paired dataset is missing columns: {missing}")


def rows_to_matrix(rows: list[dict], feature_columns: list[str] | None = None, target_columns: list[str] | None = None):
    validate_pair_rows(rows)
    feature_columns = feature_columns or FEATURE_COLUMNS
    target_columns = target_columns or TARGET_COLUMNS
    x = np.asarray([[float(row[col]) for col in feature_columns] for row in rows], dtype=float)
    y = np.asarray([[float(row[col]) for col in target_columns] for row in rows], dtype=float)
    baseline = np.asarray(
        [
            [
                float(row["water_level_lf"]),
                float(row["velocity_magnitude_lf"]),
                float(row["flow_direction_lf"]),
                float(row["transverse_velocity_lf"]),
                float(row["tke_stat_lf"]),
            ]
            for row in rows
        ],
        dtype=float,
    )
    return x, y, baseline


def deterministic_split(rows: list[dict], seed: int = 42, train_fraction: float = 0.70, validation_fraction: float = 0.15):
    rng = np.random.default_rng(seed)
    indices = np.arange(len(rows))
    rng.shuffle(indices)
    n_train = int(round(len(rows) * train_fraction))
    n_val = int(round(len(rows) * validation_fraction))
    train_idx = indices[:n_train]
    val_idx = indices[n_train : n_train + n_val]
    test_idx = indices[n_train + n_val :]
    return train_idx, val_idx, test_idx


def grouped_condition_location_split(
    rows: list[dict],
    seed: int = 42,
    train_fraction: float = 0.70,
    validation_fraction: float = 0.15,
    group_fields: tuple[str, str] = ("condition_key", "sample_id"),
):
    """Split rows by condition-location groups to avoid target leakage.

    All rows sharing the same hydrological condition and spatial sample are
    assigned to the same subset, including their 30, 40, 50, 100, and 200 m
    lower-fidelity records.
    """

    if not rows:
        raise ValueError("cannot split an empty row list")
    groups: dict[tuple[str, str], list[int]] = {}
    for idx, row in enumerate(rows):
        key = tuple(str(row[field]) for field in group_fields)
        groups.setdefault(key, []).append(idx)

    rng = np.random.default_rng(seed)
    keys = list(groups)
    rng.shuffle(keys)
    n_train = int(round(len(keys) * train_fraction))
    n_val = int(round(len(keys) * validation_fraction))
    train_keys = set(keys[:n_train])
    val_keys = set(keys[n_train : n_train + n_val])
    test_keys = set(keys[n_train + n_val :])

    def collect(selected: set[tuple[str, str]]) -> np.ndarray:
        indices = [idx for key in selected for idx in groups[key]]
        return np.asarray(sorted(indices), dtype=int)

    return collect(train_keys), collect(val_keys), collect(test_keys)


def subset_rows(rows: list[dict], indices: np.ndarray) -> list[dict]:
    return [rows[int(i)] for i in indices]


def generate_demo_pairs(n_points_per_condition: int = 24, seed: int = 42) -> list[dict]:
    """Generate a deterministic synthetic paired dataset.

    The demo data are not the manuscript data. They only exercise the same
    column contract and residual-learning workflow.
    """

    rng = np.random.default_rng(seed)
    rows: list[dict] = []
    for condition_key, condition in HYDROLOGICAL_CONDITIONS.items():
        qy = condition["yangtze_q_m3s"]
        qd = condition["dongting_q_m3s"]
        z = condition["downstream_level_m"]
        flow_scale = (qy + 0.6 * qd) / 50000.0
        for sample_id in range(1, n_points_per_condition + 1):
            phase = sample_id / n_points_per_condition * 2.0 * math.pi
            x = sample_id / n_points_per_condition
            y = math.sin(phase) * 0.2 + 0.5
            hf_water = z + 0.08 * math.sin(phase) + 0.02 * flow_scale
            hf_velocity = 0.35 + 1.4 * flow_scale + 0.08 * math.cos(phase)
            hf_direction = 18.0 * math.sin(phase / 2.0) + 4.0 * flow_scale
            hf_transverse = 0.12 * math.sin(phase) + 0.04 * flow_scale
            hf_tke = 0.015 + 0.020 * flow_scale + 0.004 * math.cos(phase)
            for mesh in LOWER_FIDELITY_MESHES:
                mesh_factor = mesh / 20.0 - 1.0
                fidelity_code = 1.0 if mesh <= 50 else 0.0
                smooth = 1.0 / (1.0 + 0.18 * mesh_factor)
                noise = rng.normal(0.0, 0.002, 5)
                lf_water = hf_water - 0.012 * mesh_factor + noise[0]
                lf_velocity = hf_velocity * smooth - 0.015 * mesh_factor + noise[1]
                lf_direction = hf_direction * smooth - 0.9 * mesh_factor + noise[2]
                lf_transverse = hf_transverse * smooth - 0.008 * mesh_factor + noise[3]
                lf_tke = max(0.0, hf_tke * smooth - 0.002 * mesh_factor + noise[4])
                rows.append(
                    {
                        "condition_key": condition_key,
                        "sample_id": sample_id,
                        "x": f"{x:.8f}",
                        "y": f"{y:.8f}",
                        "mesh_m": mesh,
                        "fidelity_code": f"{fidelity_code:.1f}",
                        "yangtze_q_m3s": f"{qy:.6g}",
                        "dongting_q_m3s": f"{qd:.6g}",
                        "downstream_level_m": f"{z:.6g}",
                        "water_level_lf": f"{lf_water:.8f}",
                        "velocity_magnitude_lf": f"{lf_velocity:.8f}",
                        "flow_direction_lf": f"{lf_direction:.8f}",
                        "transverse_velocity_lf": f"{lf_transverse:.8f}",
                        "tke_stat_lf": f"{lf_tke:.8f}",
                        "water_level_hf": f"{hf_water:.8f}",
                        "velocity_magnitude_hf": f"{hf_velocity:.8f}",
                        "flow_direction_hf": f"{hf_direction:.8f}",
                        "transverse_velocity_hf": f"{hf_transverse:.8f}",
                        "tke_stat_hf": f"{hf_tke:.8f}",
                    }
                )
    return rows
