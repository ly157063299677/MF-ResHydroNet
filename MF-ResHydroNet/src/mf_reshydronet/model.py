"""PyTorch implementation of MF-ResHydroNet.

The architecture follows the IEEE Access submission description: spatial-hydrological
embedding, lower-fidelity hydrodynamic encoding, mesh-fidelity embedding,
fidelity-aware attention/residual fusion, and residual decoding. The module is
not imported by default so that table-generation scripts can run without
PyTorch.
"""

from __future__ import annotations


def _require_torch():
    try:
        import torch
        import torch.nn as nn
    except ImportError as exc:
        raise ImportError("PyTorch is required for neural-network training. Install the optional training requirements.") from exc
    return torch, nn


def build_mf_reshydronet(
    spatial_dim: int = 2,
    hydrological_dim: int = 3,
    lf_state_dim: int = 5,
    mesh_dim: int = 2,
    target_dim: int = 5,
    latent_dim: int = 64,
    hidden_dim: int = 128,
    dropout: float = 0.10,
):
    """Return an MF-ResHydroNet ``torch.nn.Module``.

    Inputs are supplied as a dictionary with keys ``spatial``, ``hydrological``,
    ``lf_state``, ``mesh`` and ``lf_baseline``. The forward pass returns the
    reconstructed high-fidelity output by adding a learned residual correction
    to ``lf_baseline``.
    """

    torch, nn = _require_torch()

    class MFResHydroNet(nn.Module):
        def __init__(self):
            super().__init__()
            self.spatial_hydro = nn.Sequential(
                nn.Linear(spatial_dim + hydrological_dim, latent_dim),
                nn.GELU(),
                nn.LayerNorm(latent_dim),
                nn.Linear(latent_dim, hidden_dim),
                nn.GELU(),
                nn.Linear(hidden_dim, latent_dim),
                nn.LayerNorm(latent_dim),
            )
            self.lf_encoder = nn.Sequential(
                nn.Linear(lf_state_dim, hidden_dim),
                nn.GELU(),
                nn.LayerNorm(hidden_dim),
                nn.Linear(hidden_dim, hidden_dim),
                nn.GELU(),
                nn.Dropout(dropout),
                nn.Linear(hidden_dim, latent_dim),
                nn.LayerNorm(latent_dim),
            )
            self.mesh_embedding = nn.Sequential(
                nn.Linear(mesh_dim, latent_dim),
                nn.GELU(),
                nn.LayerNorm(latent_dim),
            )
            self.attention = nn.MultiheadAttention(embed_dim=latent_dim, num_heads=4, dropout=dropout, batch_first=True)
            self.gate = nn.Sequential(
                nn.Linear(latent_dim * 2, hidden_dim),
                nn.GELU(),
                nn.Linear(hidden_dim, latent_dim),
                nn.Sigmoid(),
            )
            self.post_fusion = nn.Sequential(
                nn.Linear(latent_dim * 3, hidden_dim),
                nn.GELU(),
                nn.Dropout(dropout),
                nn.Linear(hidden_dim, latent_dim),
                nn.LayerNorm(latent_dim),
            )
            self.decoder = nn.Sequential(
                nn.Linear(latent_dim, hidden_dim),
                nn.GELU(),
                nn.Dropout(dropout),
                nn.Linear(hidden_dim, hidden_dim),
                nn.GELU(),
                nn.Linear(hidden_dim, target_dim),
            )

        def forward(self, inputs):
            spatial_hydro = self.spatial_hydro(torch.cat([inputs["spatial"], inputs["hydrological"]], dim=-1))
            lf_state = self.lf_encoder(inputs["lf_state"])
            mesh = self.mesh_embedding(inputs["mesh"])
            tokens = torch.stack([spatial_hydro, lf_state, mesh], dim=1)
            attn_out, _ = self.attention(tokens, tokens, tokens, need_weights=False)
            pooled = attn_out.mean(dim=1)
            gate = self.gate(torch.cat([pooled, mesh], dim=-1))
            gated_lf = lf_state * gate
            fused = self.post_fusion(torch.cat([pooled, gated_lf, mesh], dim=-1))
            residual = self.decoder(fused)
            return inputs["lf_baseline"] + residual

    return MFResHydroNet()
