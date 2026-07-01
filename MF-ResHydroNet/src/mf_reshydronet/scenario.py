"""Scenario-screening helpers for navigation-related hydraulic assessment."""

from __future__ import annotations


def classify_level(value: float, thresholds: tuple[float, float, float]) -> str:
    low, medium, high = thresholds
    if value >= high:
        return "Very High"
    if value >= medium:
        return "High"
    if value >= low:
        return "Medium"
    return "Low"


def combine_priority(high_velocity: str, transverse_flow: str) -> str:
    order = {"Low": 0, "Medium": 1, "High": 2, "Very High": 3}
    score = max(order[high_velocity], order[transverse_flow])
    for label, idx in order.items():
        if idx == score:
            return label
    raise RuntimeError("unreachable")


def screen_scenarios(
    rows: list[dict],
    velocity_thresholds: tuple[float, float, float] = (1.2, 1.5, 1.8),
    transverse_thresholds: tuple[float, float, float] = (0.12, 0.18, 0.24),
) -> list[dict]:
    """Classify scenario priority from reconstructed hydraulic indicators."""

    out = []
    for row in rows:
        max_velocity = float(row["max_velocity_mps"])
        max_abs_transverse = abs(float(row["max_abs_transverse_velocity_mps"]))
        velocity_label = classify_level(max_velocity, velocity_thresholds)
        transverse_label = classify_level(max_abs_transverse, transverse_thresholds)
        out.append(
            {
                **row,
                "high_velocity": velocity_label,
                "transverse_flow": transverse_label,
                "priority": combine_priority(velocity_label, transverse_label),
            }
        )
    return out

