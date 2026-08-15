from dataclasses import dataclass, asdict

@dataclass(frozen=True)
class DrainageResult:
    peak_runoff_m3s: float
    capacity_gap_m3s: float
    utilization: float
    status: str
    equation: str = "Q = C × i × A / 3.6"
    def as_dict(self): return asdict(self)

def rational_runoff(coefficient: float, intensity_mm_h: float, area_km2: float, capacity_m3s: float) -> DrainageResult:
    """Rational Method screening. Use SWMM for time-varying hydraulic design."""
    if not 0 <= coefficient <= 1: raise ValueError("coefficient must be in [0,1]")
    if min(intensity_mm_h, area_km2, capacity_m3s) < 0: raise ValueError("physical inputs cannot be negative")
    q = coefficient * intensity_mm_h * area_km2 / 3.6
    gap = q - capacity_m3s
    utilization = q / capacity_m3s if capacity_m3s else float("inf")
    status = "surcharge" if gap > 0 else "available"
    return DrainageResult(round(q,4), round(gap,4), round(utilization,4), status)
