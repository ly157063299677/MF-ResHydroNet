# MF-ResHydroNet

Code accompanying the IEEE Access submission:

**MF-ResHydroNet: Mesh-Resolution-Conditioned Multi-Fidelity Residual Learning for River Hydrodynamic Reconstruction**

This repository provides the public code, data contracts, demo workflow, scenario-screening utilities, and manuscript-reference tables for MF-ResHydroNet. The method reconstructs a calibrated 20 m hydrodynamic numerical reference from spatially aligned lower-resolution simulations generated on 30, 40, 50, 100, and 200 m meshes.

## Scope

The repository contains:

- PyTorch model code for MF-ResHydroNet, including spatial-hydrological embedding, lower-fidelity hydrodynamic encoding, mesh-fidelity embedding, fidelity-aware attention/residual fusion, and residual decoding.
- A lightweight NumPy residual-ridge demo that runs without PyTorch.
- CSV data contracts for paired lower-/high-fidelity samples and prediction files.
- Scripts for demo data generation, demo training, metric aggregation, scenario screening, and manuscript-reference table export.
- Reference CSVs corresponding to the IEEE Access main and supplementary tables.

The repository does not contain raw engineering/numerical simulation source files. The manuscript states that derived hydrodynamic datasets and processed reconstruction results are available from the corresponding author upon reasonable request, subject to institutional and project-data restrictions. The included demo data are synthetic and must not be cited as manuscript results.

## Repository Layout

```text
MF-ResHydroNet-IEEEAccess-GitHub/
  README.md
  LICENSE
  CITATION.cff
  pyproject.toml
  requirements.txt
  configs/
    example.json
  data/
    README.md
    demo/
      README.md
      demo_pairs.csv
    manuscript/
      README.md
      reference_tables/
        *.csv
  docs/
    DATA_CONTRACT.md
    REPRODUCIBILITY_MAP.md
  scripts/
    make_demo_data.py
    train_demo.py
    evaluate_predictions.py
    build_reference_tables.py
    scenario_screening.py
    make_all.py
  src/
    mf_reshydronet/
      constants.py
      data.py
      metrics.py
      model.py
      ridge.py
      scenario.py
      tables.py
  tests/
    run_smoke_tests.py
```

## Quick Start

Create a local environment:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Run the lightweight demo pipeline:

```bash
python scripts/make_all.py
```

This creates local generated files under `outputs/`, including demo predictions, metrics, scenario-screening output, and exported reference tables.

Run smoke tests:

```bash
python tests/run_smoke_tests.py
```

## Upload to GitHub

After creating an empty GitHub repository, run:

```bash
git init
git add .
git commit -m "Initial release of MF-ResHydroNet code"
git branch -M main
git remote add origin https://github.com/<your-account>/MF-ResHydroNet.git
git push -u origin main
```

Replace `<your-account>` with the GitHub account or organization name.

## Full Training Dependencies

The demo pipeline requires only NumPy and pandas. Neural-network training and baseline reproduction require optional packages:

```bash
pip install torch scikit-learn xgboost lightgbm matplotlib
```

Full numerical reproduction of the IEEE Access results requires the real paired hydrodynamic dataset and trained prediction outputs. This repository does not fabricate those restricted data.

## Paired-Sample CSV Contract

For full experiments, prepare a paired CSV following `docs/DATA_CONTRACT.md`. At minimum, each row should represent one aligned lower-fidelity/high-fidelity sample and include:

```text
condition_key,sample_id,x,y,mesh_m,fidelity_code,
yangtze_q_m3s,dongting_q_m3s,downstream_level_m,
water_level_lf,velocity_magnitude_lf,flow_direction_lf,transverse_velocity_lf,tke_stat_lf,
water_level_hf,velocity_magnitude_hf,flow_direction_hf,transverse_velocity_hf,tke_stat_hf
```

The grouped evaluation protocol must keep all records sharing the same hydrological condition and spatial location in the same train, validation, or test subset.

## Prediction CSV Contract

Metric aggregation expects:

```text
model,variable,subset,observed,predicted
```

Optional metadata columns such as `condition_key`, `mesh_m`, `sample_id`, `x`, and `y` are allowed.

Example:

```bash
python scripts/evaluate_predictions.py \
  --predictions outputs/demo/demo_predictions.csv \
  --out outputs/demo/metrics_by_subset.csv
```

## Scenario Screening

For scenario screening, supply a CSV with:

```text
case_id,mesh_used,yangtze_q_m3s,dongting_q_m3s,downstream_level_m,max_velocity_mps,max_abs_transverse_velocity_mps
```

Then run:

```bash
python scripts/scenario_screening.py --indicators path/to/scenario_indicators.csv --out outputs/scenario_screening.csv
```

If no input is supplied, the script runs the four-case demonstration corresponding to IEEE Access Table IV.

## Manuscript Reference Tables

The committed reference tables can be regenerated with:

```bash
python scripts/build_reference_tables.py --out-dir data/manuscript/reference_tables
```

These files are transparent manuscript-reference summaries. They are not a substitute for rerunning the full private-data training workflow.

## Citation

If you use this repository, cite the accompanying manuscript once it is published. A provisional `CITATION.cff` is included and should be updated with DOI and publication metadata after acceptance.

## License

Code is released under the MIT License. Data are not included and are governed by the manuscript data-availability statement.
