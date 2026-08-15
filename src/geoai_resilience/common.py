from dataclasses import dataclass, asdict
from math import isfinite
from typing import Mapping

@dataclass(frozen=True)
class Decision:
    score: float
    classification: str
    confidence: float
    drivers: tuple[str, ...]
    assumptions: tuple[str, ...]
    requires_human_approval: bool = True

    def as_dict(self) -> dict:
        return asdict(self)

def unit(value: float, name: str) -> float:
    value = float(value)
    if not isfinite(value) or not 0 <= value <= 1:
        raise ValueError(f"{name} must be finite and between 0 and 1")
    return value

def normalized_weights(weights: Mapping[str, float], keys: set[str]) -> dict[str, float]:
    if set(weights) != keys:
        raise ValueError("weight keys must exactly match criterion keys")
    if any(float(v) < 0 for v in weights.values()):
        raise ValueError("weights cannot be negative")
    total = sum(float(v) for v in weights.values())
    if total <= 0:
        raise ValueError("at least one weight must be positive")
    return {k: float(v) / total for k, v in weights.items()}

def classify(score: float, breaks=(0.35, 0.60, 0.80), labels=("low", "moderate", "high", "critical")) -> str:
    for threshold, label in zip(breaks, labels):
        if score < threshold:
            return label
    return labels[-1]
