"""Reference constants from the IEEE Access submission version.

The values in this module are manuscript-reference summaries. They are not raw
hydrodynamic simulation data.
"""

from __future__ import annotations

MANUSCRIPT_TITLE = (
    "MF-ResHydroNet: Mesh-Resolution-Conditioned Multi-Fidelity Residual "
    "Learning for River Hydrodynamic Reconstruction"
)

HYDROLOGICAL_CONDITIONS = {
    "low_flow": {
        "label": "Low-flow condition",
        "yangtze_q_m3s": 7580.0,
        "dongting_q_m3s": 2000.0,
        "downstream_level_m": 19.316,
    },
    "medium_flow": {
        "label": "Medium-flow condition",
        "yangtze_q_m3s": 18700.0,
        "dongting_q_m3s": 15400.0,
        "downstream_level_m": 28.818,
    },
    "flood_flow": {
        "label": "Flood-flow condition",
        "yangtze_q_m3s": 31100.0,
        "dongting_q_m3s": 24800.0,
        "downstream_level_m": 32.990,
    },
}

COMPLETE_BOUNDARY_CONDITIONS = [
    {"case_id": "HC-01", "case_note": "Navigation-related case recorded on 2018-05-09", "yangtze_q_m3s": 12950, "dongting_q_m3s": 9350, "downstream_level_m": 25.69},
    {"case_id": "HC-02", "case_note": "Navigation-related case recorded on 2018-07-09", "yangtze_q_m3s": 30700, "dongting_q_m3s": 5190, "downstream_level_m": 29.0651},
    {"case_id": "HC-03", "case_note": "Navigation-related case recorded on 2020-08-13", "yangtze_q_m3s": 29000, "dongting_q_m3s": 16600, "downstream_level_m": 30.9112},
    {"case_id": "HC-04", "case_note": "Navigation-related case recorded on 2022-05-14", "yangtze_q_m3s": 18700, "dongting_q_m3s": 15400, "downstream_level_m": 28.8175},
    {"case_id": "HC-05", "case_note": "General simulation boundary condition", "yangtze_q_m3s": 7580, "dongting_q_m3s": 2000, "downstream_level_m": 19.3161},
    {"case_id": "HC-06", "case_note": "General simulation boundary condition", "yangtze_q_m3s": 7580, "dongting_q_m3s": 4500, "downstream_level_m": 20.6206},
    {"case_id": "HC-07", "case_note": "General simulation boundary condition", "yangtze_q_m3s": 7580, "dongting_q_m3s": 12000, "downstream_level_m": 23.9507},
    {"case_id": "HC-08", "case_note": "General simulation boundary condition", "yangtze_q_m3s": 12000, "dongting_q_m3s": 4000, "downstream_level_m": 22.487},
    {"case_id": "HC-09", "case_note": "General simulation boundary condition", "yangtze_q_m3s": 12000, "dongting_q_m3s": 9000, "downstream_level_m": 24.1757},
    {"case_id": "HC-10", "case_note": "General simulation boundary condition", "yangtze_q_m3s": 12000, "dongting_q_m3s": 14000, "downstream_level_m": 26.1959},
    {"case_id": "HC-11", "case_note": "General simulation boundary condition", "yangtze_q_m3s": 22000, "dongting_q_m3s": 4000, "downstream_level_m": 26.1957},
    {"case_id": "HC-12", "case_note": "General simulation boundary condition", "yangtze_q_m3s": 22000, "dongting_q_m3s": 11500, "downstream_level_m": 28.631},
    {"case_id": "HC-13", "case_note": "General simulation boundary condition", "yangtze_q_m3s": 22000, "dongting_q_m3s": 17000, "downstream_level_m": 29.6504},
    {"case_id": "HC-14", "case_note": "General simulation boundary condition", "yangtze_q_m3s": 35000, "dongting_q_m3s": 6000, "downstream_level_m": 30.083},
    {"case_id": "HC-15", "case_note": "General simulation boundary condition", "yangtze_q_m3s": 35000, "dongting_q_m3s": 10700, "downstream_level_m": 31.0335},
    {"case_id": "HC-16", "case_note": "General simulation boundary condition", "yangtze_q_m3s": 35000, "dongting_q_m3s": 18000, "downstream_level_m": 32.4149},
]

MESH_RESOLUTIONS = [20, 30, 40, 50, 100, 200]
LOWER_FIDELITY_MESHES = [30, 40, 50, 100, 200]

MESH_RUNTIME_SECONDS = {
    20: 72000.0,
    30: 18900.0,
    40: 6300.0,
    50: 3600.0,
    100: 300.0,
    200: 55.0,
}

MESH_RECORDED_TIME = {
    20: "20 h",
    30: "5 h 15 min",
    40: "1 h 45 min",
    50: "1 h",
    100: "5 min",
    200: "55 s",
}

MESH_CELLS = {
    20: 593893,
    30: 264524,
    40: 148461,
    50: 95129,
    100: 23824,
    200: 5963,
}

VARIABLES = [
    "water_level",
    "velocity_magnitude",
    "transverse_velocity",
    "tke_stat",
]

VARIABLE_LABELS = {
    "water_level": "Water level",
    "velocity_magnitude": "Velocity magnitude",
    "transverse_velocity": "Transverse velocity",
    "tke_stat": "TKE-stat",
}

DATASET_RECORDS = [
    {"dataset_subset": "Low-flow", "total_sample_points": 606, "spatial_points": 101, "paired_learning_samples": 505, "training_paired_samples": 355, "validation_paired_samples": 75, "test_paired_samples": 75},
    {"dataset_subset": "Medium-flow", "total_sample_points": 606, "spatial_points": 101, "paired_learning_samples": 505, "training_paired_samples": 355, "validation_paired_samples": 75, "test_paired_samples": 75},
    {"dataset_subset": "Flood-flow", "total_sample_points": 606, "spatial_points": 101, "paired_learning_samples": 505, "training_paired_samples": 355, "validation_paired_samples": 75, "test_paired_samples": 75},
    {"dataset_subset": "All conditions", "total_sample_points": 1818, "spatial_points": 303, "paired_learning_samples": 1515, "training_paired_samples": 1065, "validation_paired_samples": 225, "test_paired_samples": 225},
]

FEATURE_TARGET_TABLE = [
    {"model_component": "Input feature", "feature_or_target_group": "Spatial coordinates", "variables_included": "Projected planar coordinates x and y", "role": "Encodes spatial heterogeneity of the river reach"},
    {"model_component": "Input feature", "feature_or_target_group": "Hydrological boundary condition", "variables_included": "Yangtze discharge, Dongting discharge, downstream water level", "role": "Conditions the network on hydraulic forcing"},
    {"model_component": "Input feature", "feature_or_target_group": "Mesh and fidelity descriptor", "variables_included": "Mesh resolution and fidelity level", "role": "Distinguishes source resolution and correction magnitude"},
    {"model_component": "Input feature", "feature_or_target_group": "Low-fidelity hydrodynamic state", "variables_included": "Water level, velocity magnitude, flow direction", "role": "Provides the baseline hydraulic field"},
    {"model_component": "Input feature", "feature_or_target_group": "Optional derived low-fidelity state", "variables_included": "Transverse velocity and TKE-stat if available", "role": "Extends residual correction to derived indicators"},
    {"model_component": "Prediction target", "feature_or_target_group": "High-fidelity water level", "variables_included": "20 m water level", "role": "Primary supervised output"},
    {"model_component": "Prediction target", "feature_or_target_group": "High-fidelity velocity magnitude", "variables_included": "20 m velocity magnitude", "role": "Primary supervised output"},
    {"model_component": "Prediction target", "feature_or_target_group": "High-fidelity transverse velocity", "variables_included": "20 m transverse velocity", "role": "Navigation-related extended output"},
    {"model_component": "Prediction target", "feature_or_target_group": "High-fidelity turbulence-related statistic", "variables_included": "20 m TKE-stat", "role": "Turbulence-response extended output"},
    {"model_component": "Residual-learning target", "feature_or_target_group": "Multi-fidelity residual", "variables_included": "High-fidelity target minus lower-fidelity baseline", "role": "Enables residual correction rather than direct prediction"},
]

HYPERPARAMETER_TABLE = [
    {"model": "Linear regression", "main_hyperparameters": "Default least-squares solver; intercept=True", "training_settings": "Standardized continuous inputs"},
    {"model": "Random forest", "main_hyperparameters": "n_estimators=500; max_depth=20; max_features=sqrt; bootstrap=True", "training_settings": "Random seed=42"},
    {"model": "XGBoost", "main_hyperparameters": "n_estimators=600; max_depth=5; learning_rate=0.03; subsample=0.85; colsample_bytree=0.85; reg_lambda=1.0", "training_settings": "Early stopping rounds=50; random seed=42"},
    {"model": "LightGBM", "main_hyperparameters": "n_estimators=800; num_leaves=31; max_depth=8; learning_rate=0.03; lambda_l2=1.0", "training_settings": "Early stopping rounds=50; random seed=42"},
    {"model": "Standard MLP", "main_hyperparameters": "Hidden layers=128-128-64; ReLU; dropout=0.10", "training_settings": "AdamW; lr=1e-3; weight_decay=1e-4; batch_size=64; epochs=500; patience=50"},
    {"model": "Direct multi-fidelity MLP", "main_hyperparameters": "Hidden layers=256-128-64; ReLU; dropout=0.10", "training_settings": "AdamW; lr=1e-3; weight_decay=1e-4; batch_size=64; epochs=500; patience=50"},
    {"model": "MF-ResHydroNet", "main_hyperparameters": "64-d spatial-hydrological, mesh-fidelity, and lower-fidelity embeddings; fidelity-aware AttenRes fusion; residual decoder", "training_settings": "AdamW; lr=1e-3; weight_decay=1e-4; batch_size=64; epochs=500; patience=50"},
]

MANUSCRIPT_OVERALL_PERFORMANCE = [
    {"model": "Raw lower-fidelity CFD", "water_level_rmse": 0.058, "water_level_r2": 0.967, "velocity_magnitude_rmse": 0.063, "velocity_magnitude_r2": 0.934, "transverse_velocity_rmse": 0.053, "transverse_velocity_r2": 0.912, "tke_stat_rmse": 0.026, "tke_stat_r2": 0.864, "mean_r2": 0.919},
    {"model": "Linear regression", "water_level_rmse": 0.081, "water_level_r2": 0.942, "velocity_magnitude_rmse": 0.092, "velocity_magnitude_r2": 0.903, "transverse_velocity_rmse": 0.074, "transverse_velocity_r2": 0.876, "tke_stat_rmse": 0.036, "tke_stat_r2": 0.842, "mean_r2": 0.891},
    {"model": "SVR", "water_level_rmse": 0.063, "water_level_r2": 0.957, "velocity_magnitude_rmse": 0.071, "velocity_magnitude_r2": 0.918, "transverse_velocity_rmse": 0.059, "transverse_velocity_r2": 0.894, "tke_stat_rmse": 0.029, "tke_stat_r2": 0.851, "mean_r2": 0.905},
    {"model": "GPR / Kriging", "water_level_rmse": 0.059, "water_level_r2": 0.964, "velocity_magnitude_rmse": 0.066, "velocity_magnitude_r2": 0.927, "transverse_velocity_rmse": 0.055, "transverse_velocity_r2": 0.905, "tke_stat_rmse": 0.027, "tke_stat_r2": 0.867, "mean_r2": 0.916},
    {"model": "Random forest", "water_level_rmse": 0.052, "water_level_r2": 0.974, "velocity_magnitude_rmse": 0.061, "velocity_magnitude_r2": 0.942, "transverse_velocity_rmse": 0.051, "transverse_velocity_r2": 0.917, "tke_stat_rmse": 0.024, "tke_stat_r2": 0.889, "mean_r2": 0.931},
    {"model": "XGBoost", "water_level_rmse": 0.044, "water_level_r2": 0.982, "velocity_magnitude_rmse": 0.052, "velocity_magnitude_r2": 0.956, "transverse_velocity_rmse": 0.044, "transverse_velocity_r2": 0.936, "tke_stat_rmse": 0.021, "tke_stat_r2": 0.908, "mean_r2": 0.946},
    {"model": "LightGBM", "water_level_rmse": 0.046, "water_level_r2": 0.981, "velocity_magnitude_rmse": 0.054, "velocity_magnitude_r2": 0.953, "transverse_velocity_rmse": 0.045, "transverse_velocity_r2": 0.932, "tke_stat_rmse": 0.021, "tke_stat_r2": 0.905, "mean_r2": 0.943},
    {"model": "Standard MLP", "water_level_rmse": 0.041, "water_level_r2": 0.985, "velocity_magnitude_rmse": 0.049, "velocity_magnitude_r2": 0.962, "transverse_velocity_rmse": 0.040, "transverse_velocity_r2": 0.947, "tke_stat_rmse": 0.019, "tke_stat_r2": 0.919, "mean_r2": 0.953},
    {"model": "Direct multi-fidelity MLP", "water_level_rmse": 0.036, "water_level_r2": 0.988, "velocity_magnitude_rmse": 0.043, "velocity_magnitude_r2": 0.970, "transverse_velocity_rmse": 0.035, "transverse_velocity_r2": 0.958, "tke_stat_rmse": 0.016, "tke_stat_r2": 0.936, "mean_r2": 0.963},
    {"model": "MF-ResHydroNet", "water_level_rmse": 0.028, "water_level_r2": 0.993, "velocity_magnitude_rmse": 0.034, "velocity_magnitude_r2": 0.981, "transverse_velocity_rmse": 0.027, "transverse_velocity_r2": 0.972, "tke_stat_rmse": 0.012, "tke_stat_r2": 0.956, "mean_r2": 0.976},
]

MAE_COMPARISON_TABLE = [
    {"category": "No-learning baseline", "method": "Raw lower-fidelity CFD", "water_level_mae": 0.041, "velocity_mae": 0.046, "transverse_velocity_mae": 0.039, "tke_stat_mae": 0.018, "mean_mae": 0.036},
    {"category": "Classical regression", "method": "Linear regression", "water_level_mae": 0.056, "velocity_mae": 0.062, "transverse_velocity_mae": 0.051, "tke_stat_mae": 0.024, "mean_mae": 0.048},
    {"category": "Kernel-based surrogate", "method": "SVR (RBF kernel)", "water_level_mae": 0.044, "velocity_mae": 0.049, "transverse_velocity_mae": 0.042, "tke_stat_mae": 0.020, "mean_mae": 0.039},
    {"category": "Probabilistic surrogate", "method": "GPR / Kriging", "water_level_mae": 0.042, "velocity_mae": 0.047, "transverse_velocity_mae": 0.040, "tke_stat_mae": 0.019, "mean_mae": 0.037},
    {"category": "Ensemble learning", "method": "Random forest", "water_level_mae": 0.036, "velocity_mae": 0.041, "transverse_velocity_mae": 0.035, "tke_stat_mae": 0.016, "mean_mae": 0.032},
    {"category": "Ensemble learning", "method": "XGBoost", "water_level_mae": 0.030, "velocity_mae": 0.035, "transverse_velocity_mae": 0.029, "tke_stat_mae": 0.014, "mean_mae": 0.027},
    {"category": "Ensemble learning", "method": "LightGBM", "water_level_mae": 0.031, "velocity_mae": 0.036, "transverse_velocity_mae": 0.030, "tke_stat_mae": 0.014, "mean_mae": 0.028},
    {"category": "Neural network", "method": "Standard MLP", "water_level_mae": 0.028, "velocity_mae": 0.033, "transverse_velocity_mae": 0.027, "tke_stat_mae": 0.013, "mean_mae": 0.025},
    {"category": "Multi-fidelity baseline", "method": "Direct multi-fidelity MLP", "water_level_mae": 0.024, "velocity_mae": 0.029, "transverse_velocity_mae": 0.023, "tke_stat_mae": 0.011, "mean_mae": 0.022},
    {"category": "Proposed method", "method": "MF-ResHydroNet", "water_level_mae": 0.018, "velocity_mae": 0.022, "transverse_velocity_mae": 0.017, "tke_stat_mae": 0.008, "mean_mae": 0.016},
]

MESH_ACCURACY_TABLE = [
    {"lower_fidelity_input": "30 m -> 20 m", "wl_rmse": 0.018, "velocity_rmse": 0.025, "transverse_velocity_rmse": 0.021, "tke_stat_rmse": 0.010, "mean_r2": 0.982},
    {"lower_fidelity_input": "40 m -> 20 m", "wl_rmse": 0.022, "velocity_rmse": 0.028, "transverse_velocity_rmse": 0.023, "tke_stat_rmse": 0.011, "mean_r2": 0.977},
    {"lower_fidelity_input": "50 m -> 20 m", "wl_rmse": 0.025, "velocity_rmse": 0.031, "transverse_velocity_rmse": 0.026, "tke_stat_rmse": 0.012, "mean_r2": 0.971},
    {"lower_fidelity_input": "100 m -> 20 m", "wl_rmse": 0.035, "velocity_rmse": 0.041, "transverse_velocity_rmse": 0.032, "tke_stat_rmse": 0.015, "mean_r2": 0.955},
    {"lower_fidelity_input": "200 m -> 20 m", "wl_rmse": 0.052, "velocity_rmse": 0.057, "transverse_velocity_rmse": 0.043, "tke_stat_rmse": 0.021, "mean_r2": 0.925},
    {"lower_fidelity_input": "Pooled lower-fidelity inputs", "wl_rmse": 0.028, "velocity_rmse": 0.034, "transverse_velocity_rmse": 0.027, "tke_stat_rmse": 0.012, "mean_r2": 0.976},
]

SCENARIO_SCREENING_TABLE = [
    {"case_id": "HC-08", "mesh_used": "100 m", "yangtze_q_m3s": 12000, "dongting_q_m3s": 4000, "downstream_level_m": 22.487, "high_velocity": "Medium", "transverse_flow": "Medium", "priority": "Medium"},
    {"case_id": "HC-12", "mesh_used": "100 m", "yangtze_q_m3s": 22000, "dongting_q_m3s": 11500, "downstream_level_m": 28.631, "high_velocity": "High", "transverse_flow": "High", "priority": "High"},
    {"case_id": "HC-14", "mesh_used": "200 m", "yangtze_q_m3s": 35000, "dongting_q_m3s": 6000, "downstream_level_m": 30.083, "high_velocity": "High", "transverse_flow": "Medium", "priority": "High"},
    {"case_id": "HC-16", "mesh_used": "200 m", "yangtze_q_m3s": 35000, "dongting_q_m3s": 18000, "downstream_level_m": 32.415, "high_velocity": "Very High", "transverse_flow": "High", "priority": "Very High"},
]

GENERALIZATION_TABLE = [
    {"testing_scenario": "Random split", "wl_rmse": 0.028, "velocity_rmse": 0.034, "transverse_velocity_rmse": 0.027, "tke_stat_rmse": 0.012, "mean_r2": 0.976},
    {"testing_scenario": "Leave-low-flow-out", "wl_rmse": 0.043, "velocity_rmse": 0.053, "transverse_velocity_rmse": 0.041, "tke_stat_rmse": 0.018, "mean_r2": 0.940},
    {"testing_scenario": "Leave-medium-flow-out", "wl_rmse": 0.039, "velocity_rmse": 0.048, "transverse_velocity_rmse": 0.037, "tke_stat_rmse": 0.016, "mean_r2": 0.950},
    {"testing_scenario": "Leave-flood-flow-out", "wl_rmse": 0.057, "velocity_rmse": 0.066, "transverse_velocity_rmse": 0.052, "tke_stat_rmse": 0.024, "mean_r2": 0.911},
    {"testing_scenario": "Spatial extrapolation", "wl_rmse": 0.049, "velocity_rmse": 0.060, "transverse_velocity_rmse": 0.047, "tke_stat_rmse": 0.021, "mean_r2": 0.925},
]

RAW_CORRECTED_RMSE_TABLE = [
    ("30 m -> 20 m", "Water level", 0.032, 0.018),
    ("30 m -> 20 m", "Velocity magnitude", 0.041, 0.025),
    ("30 m -> 20 m", "Transverse velocity", 0.034, 0.021),
    ("30 m -> 20 m", "TKE-stat", 0.017, 0.010),
    ("40 m -> 20 m", "Water level", 0.037, 0.022),
    ("40 m -> 20 m", "Velocity magnitude", 0.046, 0.028),
    ("40 m -> 20 m", "Transverse velocity", 0.039, 0.023),
    ("40 m -> 20 m", "TKE-stat", 0.018, 0.011),
    ("50 m -> 20 m", "Water level", 0.044, 0.025),
    ("50 m -> 20 m", "Velocity magnitude", 0.051, 0.031),
    ("50 m -> 20 m", "Transverse velocity", 0.043, 0.026),
    ("50 m -> 20 m", "TKE-stat", 0.020, 0.012),
    ("100 m -> 20 m", "Water level", 0.061, 0.035),
    ("100 m -> 20 m", "Velocity magnitude", 0.067, 0.041),
    ("100 m -> 20 m", "Transverse velocity", 0.052, 0.032),
    ("100 m -> 20 m", "TKE-stat", 0.021, 0.015),
    ("200 m -> 20 m", "Water level", 0.079, 0.052),
    ("200 m -> 20 m", "Velocity magnitude", 0.086, 0.057),
    ("200 m -> 20 m", "Transverse velocity", 0.066, 0.043),
    ("200 m -> 20 m", "TKE-stat", 0.027, 0.021),
]

ABLATION_TABLE = [
    {"model_variant": "Full MF-ResHydroNet", "wl_rmse": 0.028, "velocity_rmse": 0.034, "transverse_velocity_rmse": 0.027, "tke_stat_rmse": 0.012, "mean_r2": 0.976, "avg_rmse_increase": "0.0%"},
    {"model_variant": "w/o spatial-hydrological embedding", "wl_rmse": 0.041, "velocity_rmse": 0.047, "transverse_velocity_rmse": 0.039, "tke_stat_rmse": 0.017, "mean_r2": 0.958, "avg_rmse_increase": "+42.6%"},
    {"model_variant": "w/o mesh-fidelity embedding", "wl_rmse": 0.035, "velocity_rmse": 0.042, "transverse_velocity_rmse": 0.033, "tke_stat_rmse": 0.015, "mean_r2": 0.968, "avg_rmse_increase": "+23.8%"},
    {"model_variant": "w/o fidelity-aware AttenRes fusion", "wl_rmse": 0.033, "velocity_rmse": 0.039, "transverse_velocity_rmse": 0.031, "tke_stat_rmse": 0.014, "mean_r2": 0.972, "avg_rmse_increase": "+15.8%"},
    {"model_variant": "w/o residual-correction branch", "wl_rmse": 0.037, "velocity_rmse": 0.045, "transverse_velocity_rmse": 0.036, "tke_stat_rmse": 0.016, "mean_r2": 0.965, "avg_rmse_increase": "+32.7%"},
    {"model_variant": "w/o lower-fidelity hydrodynamic input", "wl_rmse": 0.062, "velocity_rmse": 0.073, "transverse_velocity_rmse": 0.058, "tke_stat_rmse": 0.028, "mean_r2": 0.902, "avg_rmse_increase": "+118.8%"},
]
