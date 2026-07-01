"""Code package for the MF-ResHydroNet manuscript.

The package is intentionally lightweight at import time. PyTorch is required
only when ``mf_reshydronet.model`` is imported for neural-network training.
"""

from .metrics import mae, rmse, r2_score

__all__ = ["mae", "rmse", "r2_score"]

