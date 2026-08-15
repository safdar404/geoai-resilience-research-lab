from typing import Mapping
from .common import Decision, normalized_weights, unit

def suitability(criteria: Mapping[str, float], weights: Mapping[str, float], constraints: Mapping[str, bool] | None = None) -> Decision:
    """Constrained weighted linear combination for a candidate planning zone.

    Inputs must already be benefit-oriented and normalized to [0, 1].
    A hard constraint makes the zone ineligible while preserving its diagnostic score.
    """
    values = {k: unit(v, k) for k, v in criteria.items()}
    w = normalized_weights(weights, set(values))
    raw = sum(values[k] * w[k] for k in values)
    blocked = sorted(k for k, present in (constraints or {}).items() if present)
    score = 0.0 if blocked else raw
    drivers = sorted(values, key=lambda k: values[k] * w[k], reverse=True)[:3]
    confidence = min(1.0, 0.55 + 0.09 * len(values))
    label = "ineligible" if blocked else ("recommended" if score >= .75 else "conditional" if score >= .55 else "review")
    assumptions = ("criteria are normalized and directionally consistent", "weights represent an approved planning scenario")
    if blocked:
        assumptions += ("hard constraints override the suitability score: " + ", ".join(blocked),)
    return Decision(round(score, 4), label, round(confidence, 3), tuple(drivers), assumptions)

def sensitivity(criteria: Mapping[str, float], weights: Mapping[str, float], delta: float = .10) -> dict[str, tuple[float, float]]:
    """One-at-a-time weight sensitivity range for transparent scenario testing."""
    result = {}
    for key in weights:
        lo, hi = dict(weights), dict(weights)
        lo[key] = max(0, lo[key] * (1 - delta)); hi[key] = hi[key] * (1 + delta)
        result[key] = (suitability(criteria, lo).score, suitability(criteria, hi).score)
    return result
