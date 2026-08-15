from dataclasses import dataclass, asdict
from typing import Any, Mapping

@dataclass(frozen=True)
class AgentRecommendation:
    workflow: str
    action: str
    confidence: float
    evidence: tuple[str,...]
    missing_inputs: tuple[str,...]
    approval_required: bool = True
    def as_dict(self): return asdict(self)

def recommend(workflow: str, result: Mapping[str,Any], evidence: list[str], required_inputs: list[str]) -> AgentRecommendation:
    """Policy layer that drafts an action but deliberately cannot execute it."""
    missing = tuple(k for k in required_inputs if result.get(k) is None)
    score = float(result.get("score", result.get("utilization", 0)))
    if missing: action = "collect missing authoritative inputs"
    elif score >= .8: action = "prepare high-priority response package"
    elif score >= .55: action = "schedule field verification"
    else: action = "continue monitoring"
    confidence = max(0.0, min(1.0, float(result.get("confidence", .7)) * (1-len(missing)/max(len(required_inputs),1))))
    return AgentRecommendation(workflow, action, round(confidence,3), tuple(evidence), missing)
