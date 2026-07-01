"""Write manuscript-reference tables and derived evaluation tables."""

from __future__ import annotations

import csv
from pathlib import Path

from .constants import (
    ABLATION_TABLE,
    COMPLETE_BOUNDARY_CONDITIONS,
    DATASET_RECORDS,
    FEATURE_TARGET_TABLE,
    GENERALIZATION_TABLE,
    HYPERPARAMETER_TABLE,
    HYDROLOGICAL_CONDITIONS,
    MAE_COMPARISON_TABLE,
    MANUSCRIPT_OVERALL_PERFORMANCE,
    MESH_ACCURACY_TABLE,
    MESH_CELLS,
    MESH_RECORDED_TIME,
    MESH_RUNTIME_SECONDS,
    RAW_CORRECTED_RMSE_TABLE,
    SCENARIO_SCREENING_TABLE,
)
from .data import write_csv
from .metrics import error_reduction


def write_rows(path: str | Path, rows: list[dict]) -> None:
    write_csv(path, rows)


def computational_efficiency_rows(inference_time_s: float = 1.8) -> list[dict]:
    hf_time = MESH_RUNTIME_SECONDS[20]
    rows = [
        {
            "prediction_strategy": "Full high-fidelity simulation",
            "numerical_simulation_used": "20 m",
            "simulation_time_s": hf_time,
            "model_inference_time_s": "",
            "total_time_s": hf_time,
            "speed_up_vs_20m": 1.00,
        }
    ]
    for mesh in (50, 100, 200):
        total = MESH_RUNTIME_SECONDS[mesh] + inference_time_s
        rows.append(
            {
                "prediction_strategy": f"{mesh} m simulation + MF-ResHydroNet",
                "numerical_simulation_used": f"{mesh} m",
                "simulation_time_s": MESH_RUNTIME_SECONDS[mesh],
                "model_inference_time_s": inference_time_s,
                "total_time_s": round(total, 1),
                "speed_up_vs_20m": round(hf_time / total, 2),
            }
        )
    return rows


def mesh_statistics_rows() -> list[dict]:
    out = []
    hf_time = MESH_RUNTIME_SECONDS[20]
    for mesh, cells in MESH_CELLS.items():
        runtime = MESH_RUNTIME_SECONDS[mesh]
        out.append(
            {
                "mesh_resolution_m": mesh,
                "mesh_cells": cells,
                "estimated_mesh_nodes": round(cells / 2),
                "samples": 101,
                "recorded_time": MESH_RECORDED_TIME[mesh],
                "runtime_s": runtime,
                "cost_percent_of_20m": round(runtime / hf_time * 100.0, 2),
                "speed_up_vs_20m": round(hf_time / runtime, 2),
                "fidelity_definition": "High fidelity / reference mesh" if mesh == 20 else ("Medium fidelity" if mesh <= 50 else "Low fidelity"),
            }
        )
    return out


def raw_corrected_rows() -> list[dict]:
    rows = []
    for lower_input, variable, raw, corrected in RAW_CORRECTED_RMSE_TABLE:
        rows.append(
            {
                "lower_fidelity_input": lower_input,
                "variable": variable,
                "raw_rmse": raw,
                "mf_reshydronet_rmse": corrected,
                "error_reduction_percent": round(error_reduction(raw, corrected), 1),
            }
        )
    return rows


def hydrological_condition_rows() -> list[dict]:
    return [
        {
            "hydrological_condition": values["label"],
            "yangtze_q_m3s": values["yangtze_q_m3s"],
            "dongting_q_m3s": values["dongting_q_m3s"],
            "downstream_level_m": values["downstream_level_m"],
            "mesh_resolutions_used": "20, 30, 40, 50, 100, and 200 m",
            "fidelity_definition": "High fidelity: 20 m; medium fidelity: 30, 40, and 50 m; low fidelity: 100 and 200 m",
        }
        for values in HYDROLOGICAL_CONDITIONS.values()
    ]


def write_reference_tables(out_dir: str | Path) -> None:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    write_rows(out / "table1_hydrological_conditions.csv", hydrological_condition_rows())
    write_rows(out / "table2_overall_reconstruction_performance.csv", MANUSCRIPT_OVERALL_PERFORMANCE)
    write_rows(out / "table3_mesh_resolution_effect.csv", MESH_ACCURACY_TABLE)
    write_rows(out / "table4_scenario_screening_indicators.csv", SCENARIO_SCREENING_TABLE)
    write_rows(out / "table_s1_complete_boundary_conditions.csv", COMPLETE_BOUNDARY_CONDITIONS)
    write_rows(out / "table_s2_mesh_statistics.csv", mesh_statistics_rows())
    write_rows(out / "table_s3_dataset_records.csv", DATASET_RECORDS)
    write_rows(out / "table_s4_features_targets_residuals.csv", FEATURE_TARGET_TABLE)
    write_rows(out / "table_s5_hyperparameters.csv", HYPERPARAMETER_TABLE)
    write_rows(out / "table_s6_generalization.csv", GENERALIZATION_TABLE)
    write_rows(out / "table_s7_raw_corrected_rmse.csv", raw_corrected_rows())
    write_rows(out / "table_s8_computational_efficiency.csv", computational_efficiency_rows())
    write_rows(out / "table_s9_ablation.csv", ABLATION_TABLE)
    write_rows(out / "table_s10_mae_comparison.csv", MAE_COMPARISON_TABLE)


def read_prediction_csv(path: str | Path) -> list[dict]:
    with Path(path).open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))
