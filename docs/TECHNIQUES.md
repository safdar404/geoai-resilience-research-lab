# Advanced techniques and research roadmap

## Urban planning

Baseline: constrained multi-criteria decision analysis with sensitivity and scenario comparison. Advanced track: OSMnx network accessibility, multi-objective Pareto search, spatial cross-validation and deep reinforcement learning for human–AI layout generation. Planning objectives must include accessibility, compactness, service equity, environmental constraints and infrastructure cost.

## Flood monitoring

Use Sentinel-1 SAR for cloud-independent water mapping, terrain correction, speckle-aware processing, pre/post change and connected-component filtering. Fuse rainfall, gauges, HAND/DEM, settlements and roads. Validate flood masks against independent reference samples and report area-adjusted accuracy. Do not confuse a spectral water mask with hydraulic depth.

## Utility networks

Represent assets as a graph; combine physical condition and failure history with hydraulic and topological consequence. Use EPANET/WNTR for pressure, demand, isolation and resilience scenarios. Train ML/GNN models only after preventing temporal and network-neighbour leakage.

## Urban drainage

Use SWMM for calibrated dynamic wave routing. PySWMM supports programmatic experiments and control. GNN surrogates can accelerate scenario screening, but should report uncertainty and remain bounded by the hydraulic training domain. Model predictive control and reinforcement learning require safe constraints and simulation-to-real validation.

## Earth observation

Prepare analysis-ready data with cloud/shadow masks, co-registration and harmonized resolution. Compare classical indices, tree ensembles, U-Net/DeepLab, SAM-assisted delineation and foundation-model embeddings. Use spatial/temporal holdouts and human-in-the-loop review.

## Minimum publication checklist

1. Dataset card and license.
2. Study-area geometry and CRS.
3. Reproducible environment.
4. Spatial train/validation/test split.
5. Baselines and ablations.
6. Accuracy, uncertainty and failure cases.
7. Runtime and hardware.
8. Ethical and operational limitations.
