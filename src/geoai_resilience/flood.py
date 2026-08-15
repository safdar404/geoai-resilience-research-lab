from .common import Decision, classify, unit

def flood_priority(hazard: float, exposure: float, vulnerability: float, access_disruption: float, data_completeness: float = 1.0) -> Decision:
    """Multiplicative risk with an access penalty and uncertainty-aware confidence."""
    h, e, v, a, c = [unit(x, n) for x, n in [(hazard,"hazard"),(exposure,"exposure"),(vulnerability,"vulnerability"),(access_disruption,"access_disruption"),(data_completeness,"data_completeness")]]
    base = (h * e * v) ** (1/3)
    score = min(1.0, base * (0.75 + 0.25 * a))
    contributors = {"hazard": h, "exposure": e, "vulnerability": v, "access disruption": a}
    drivers = tuple(sorted(contributors, key=contributors.get, reverse=True)[:3])
    confidence = c * (0.65 + 0.35 * min(h + e + v + a, 4) / 4)
    return Decision(round(score,4), classify(score), round(confidence,3), drivers, ("screening risk is relative, not a hydraulic forecast","exposure requires current population and road data"))

def uncertainty_band(score: float, input_uncertainty: float) -> tuple[float, float]:
    s, u = unit(score,"score"), unit(input_uncertainty,"input_uncertainty")
    return round(max(0, s-u/2),4), round(min(1, s+u/2),4)
