# Reproducibility Map

This file maps the IEEE Access submission version to the code and public
reference artifacts in this repository.

## Main Manuscript

| Item | Content | Code path | Status |
| --- | --- | --- | --- |
| Table I | Representative hydrological conditions and mesh-fidelity definitions | `scripts/build_reference_tables.py` -> `table1_hydrological_conditions.csv` | Reference values included |
| Table II | Overall reconstruction performance of different models | `scripts/build_reference_tables.py`; recompute from prediction CSV with `scripts/evaluate_predictions.py` | Reference values included; full recomputation requires predictions |
| Table III | Effect of lower-fidelity mesh resolution | `scripts/build_reference_tables.py` | Reference values included |
| Table IV | Scenario-screening indicators | `scripts/scenario_screening.py`; reference table exported by `scripts/build_reference_tables.py` | Demo classifier and reference values included |
| Fig. 1 | Study area and multi-fidelity dataset construction | Not regenerated | External figure asset |
| Fig. 2 | Hydrodynamic model calibration and validation | Requires observation/simulation files | Private data required |
| Fig. 3 | Paired multi-fidelity workflow | Described in `docs/DATA_CONTRACT.md` and README | Method definition |
| Fig. 4 | MF-ResHydroNet architecture | `src/mf_reshydronet/model.py` | Model code included |
| Fig. 5 | Spatial reconstruction of transverse velocity | Requires spatial prediction fields | Private prediction fields required |
| Fig. 6 | Scenario-screening demonstration | `scripts/scenario_screening.py` provides tabular screening output | Figure panels require reconstructed fields |

## Supplementary Material

| Item | Content | Code path | Status |
| --- | --- | --- | --- |
| Table S1 | Complete hydrological boundary conditions | `scripts/build_reference_tables.py` | Reference values included |
| Table S2 | Mesh statistics and computational cost | `scripts/build_reference_tables.py` | Reference values included |
| Table S3 | Multi-resolution records and paired learning samples | `scripts/build_reference_tables.py` | Reference values included |
| Table S4 | Input features, prediction targets, and residual targets | `docs/DATA_CONTRACT.md`; reference CSV exported | Method definition included |
| Table S5 | Hyperparameters and training settings | README, `src/mf_reshydronet/model.py`, and exported reference CSV | Method definition included |
| Table S6 | Generalization performance | `scripts/build_reference_tables.py` | Reference values included |
| Table S7 | Raw and residual-corrected RMSE | `scripts/build_reference_tables.py` | Reference values included |
| Table S8 | Computational efficiency comparison | `scripts/build_reference_tables.py` | Reference values included |
| Table S9 | Ablation study | `scripts/build_reference_tables.py` | Reference values included |
| Table S10 | MAE comparison | `scripts/build_reference_tables.py` | Reference values included |
| Figs. S1-S7 | Hydrological records, mesh sensitivity, diagnostics, spatial reconstruction, and sensitivity plots | Require original simulation/figure data | Private or external data required |

## Reproducible Demo

Run:

```bash
python scripts/make_all.py
```

This executes a synthetic-data residual-learning demo and writes outputs under
`outputs/`. The demo validates the workflow, file contracts, and metrics code.
It does not reproduce the manuscript numerical results.
