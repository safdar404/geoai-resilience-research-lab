from .common import Decision, classify, unit

def asset_risk(age_ratio: float, break_history: float, condition_deficit: float, service_criticality: float, graph_betweenness: float = 0.0) -> Decision:
    """Transparent asset likelihood × consequence reference model."""
    age, breaks, condition, criticality, centrality = [unit(x,n) for x,n in [(age_ratio,"age_ratio"),(break_history,"break_history"),(condition_deficit,"condition_deficit"),(service_criticality,"service_criticality"),(graph_betweenness,"graph_betweenness")]]
    likelihood = 0.34*age + 0.36*breaks + 0.30*condition
    consequence = 0.72*criticality + 0.28*centrality
    score = (likelihood * consequence) ** .5
    drivers = tuple(k for k,_ in sorted({"age":age,"break history":breaks,"condition":condition,"service criticality":criticality,"network centrality":centrality}.items(), key=lambda kv:kv[1], reverse=True)[:3])
    return Decision(round(score,4), classify(score), .82, drivers, ("coefficients are transparent screening weights","calibrate against local failures before operational use"))
