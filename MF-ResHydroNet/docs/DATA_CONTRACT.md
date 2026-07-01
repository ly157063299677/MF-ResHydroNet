# Data Contract

## Paired Lower-/High-Fidelity Dataset

Each row represents one aligned lower-fidelity input and its corresponding
20 m high-fidelity reference at the same hydrological condition and spatial
sample point.

Required columns:

| Column | Meaning |
| --- | --- |
| `condition_key` | Hydrological condition identifier, e.g. `low_flow`, `medium_flow`, `flood_flow` |
| `sample_id` | Spatial sample identifier |
| `x`, `y` | Projected or normalized spatial coordinates |
| `mesh_m` | Lower-fidelity mesh resolution in metres |
| `fidelity_code` | Numeric descriptor of fidelity level; example: 1 for medium fidelity, 0 for low fidelity |
| `yangtze_q_m3s` | Yangtze River inlet discharge |
| `dongting_q_m3s` | Dongting Lake inlet discharge |
| `downstream_level_m` | Downstream water level |
| `water_level_lf` | Lower-fidelity water level |
| `velocity_magnitude_lf` | Lower-fidelity velocity magnitude |
| `flow_direction_lf` | Lower-fidelity flow direction |
| `transverse_velocity_lf` | Lower-fidelity transverse velocity if available |
| `tke_stat_lf` | Lower-fidelity turbulent kinetic energy-related statistic if available |
| `water_level_hf` | 20 m reference water level |
| `velocity_magnitude_hf` | 20 m reference velocity magnitude |
| `flow_direction_hf` | 20 m reference flow direction |
| `transverse_velocity_hf` | 20 m reference transverse velocity |
| `tke_stat_hf` | 20 m reference TKE-related statistic |

If transverse velocity or TKE-related quantities are unavailable for a specific
experiment, either omit those targets and adapt `TARGET_COLUMNS`, or provide a
separate prediction file for the available variables only.

## Prediction File

Required columns:

```text
model,variable,subset,observed,predicted
```

Optional columns:

```text
condition_key,mesh_m,sample_id,x,y,inference_time_s
```

The script `scripts/evaluate_predictions.py` aggregates this file into MAE,
RMSE, and R2.

## Scenario-Screening Indicator File

Required columns:

```text
case_id,mesh_used,yangtze_q_m3s,dongting_q_m3s,downstream_level_m,max_velocity_mps,max_abs_transverse_velocity_mps
```

The script `scripts/scenario_screening.py` converts these indicators into
high-velocity, transverse-flow, and overall priority classes.

