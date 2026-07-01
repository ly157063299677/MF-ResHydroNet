"""Small NumPy residual model used for repository smoke tests and demos."""

from __future__ import annotations

import numpy as np


class Standardizer:
    def fit(self, x: np.ndarray):
        self.mean_ = x.mean(axis=0)
        self.scale_ = x.std(axis=0)
        self.scale_[self.scale_ == 0] = 1.0
        return self

    def transform(self, x: np.ndarray) -> np.ndarray:
        return (x - self.mean_) / self.scale_

    def fit_transform(self, x: np.ndarray) -> np.ndarray:
        return self.fit(x).transform(x)


class ResidualRidge:
    """Closed-form ridge regressor for residual correction.

    It predicts ``high_fidelity - low_fidelity`` and adds the predicted residual
    back to the lower-fidelity baseline.
    """

    def __init__(self, alpha: float = 1e-2):
        self.alpha = float(alpha)
        self.scaler = Standardizer()

    def fit(self, x: np.ndarray, y_high: np.ndarray, y_low: np.ndarray):
        residual = y_high - y_low
        x_scaled = self.scaler.fit_transform(x)
        design = np.column_stack([np.ones(x_scaled.shape[0]), x_scaled])
        penalty = np.eye(design.shape[1]) * self.alpha
        penalty[0, 0] = 0.0
        self.coef_ = np.linalg.solve(design.T @ design + penalty, design.T @ residual)
        return self

    def predict_residual(self, x: np.ndarray) -> np.ndarray:
        x_scaled = self.scaler.transform(x)
        design = np.column_stack([np.ones(x_scaled.shape[0]), x_scaled])
        return design @ self.coef_

    def predict(self, x: np.ndarray, y_low: np.ndarray) -> np.ndarray:
        return y_low + self.predict_residual(x)

