# GeoAI Resilience Research Lab

An open, reproducible research toolkit for advanced urban planning, flood intelligence, utility-network risk, urban drainage and Earth-observation change analysis.

> **Status:** research software and decision-support reference implementation. It is not a substitute for calibrated engineering models, authoritative agency data or field verification.

## Why this repository exists

Many GeoAI demonstrations stop at a map and a score. This repository exposes the analytical core: equations, assumptions, data contracts, validation, uncertainty, automation hooks and reproducible tests. Each module can run independently or participate in an agentic workflow with explicit human approval gates.

## Five research programs

| Program | Research question | Implemented core | Production extension |
|---|---|---|---|
| Urban Intelligence | Where should compact, accessible and climate-safe growth occur? | constrained weighted linear combination, sensitivity analysis, Pareto-ready outputs | OSMnx accessibility, raster MCDA, deep-RL scenario generation |
| Flood Intelligence | Which places and routes need action first? | hazard–exposure–vulnerability–access risk, uncertainty band, priority queue | Sentinel-1 flood masks, HAND, gauges, weather forecasts |
| Utility Guardian | Which network assets are most likely to fail and matter most? | transparent failure likelihood × graph consequence | WNTR/EPANET hydraulics, SCADA anomalies, GNN asset models |
| Drainage Lab | Where does runoff exceed system capacity? | Rational Method, capacity gap and surcharge classification | SWMM/PySWMM, GNN surrogate, MPC/RL control |
| Earth Change AI | What changed between observations and how certain is it? | NDVI/NDBI, confidence-filtered change masks and area accounting | STAC, TorchGeo, SAM/GeoAI, temporal transformers |

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[api,test]"
pytest
uvicorn api.main:app --reload
```

Core functions require only NumPy. Install `.[geo]` for GeoPandas, Rasterio, NetworkX, OSMnx and PyProj; install hydraulic and deep-learning tools in dedicated environments because SWMM, TorchGeo and GPU stacks are platform-specific.

## Example

```python
from geoai_resilience.urban import suitability

result = suitability(
    criteria={"access": 0.82, "services": 0.70, "climate": 0.88, "cost": 0.55},
    weights={"access": 0.30, "services": 0.20, "climate": 0.35, "cost": 0.15},
    constraints={"protected_land": False, "floodway": False},
)
print(result)
```

## Repository architecture

```text
authoritative data / STAC / OGC APIs / telemetry
                    ↓
validation · CRS · topology · QA/QC
                    ↓
urban │ flood │ utility │ drainage │ change
                    ↓
uncertainty · explainability · provenance
                    ↓
FastAPI / GIS services / notebooks / agents
                    ↓
human approval → operational action → audit log
```

## GIS and remote-sensing production pathways

- **ArcGIS Pro / ArcPy / ModelBuilder:** enterprise geodatabases, topology, raster functions, network analysis and repeatable geoprocessing.
- **QGIS / Processing:** open desktop review, GDAL algorithms, GeoPackage exchange and publishing.
- **ERDAS IMAGINE:** atmospheric/radiometric preparation, multispectral indices, supervised classification and change workflows.
- **Python:** GeoPandas, Rasterio, Xarray/Rioxarray, PyProj, Shapely, OSMnx, NetworkX and FastAPI.
- **GeoAI:** TorchGeo, PyTorch, Segment Anything/segment-geospatial, foundation-model embeddings and human-in-the-loop QA.
- **Hydraulics:** EPANET/WNTR for water networks; EPA SWMM/PySWMM for drainage systems.

See [TECHNIQUES.md](docs/TECHNIQUES.md) and [ARCGIS_QGIS_ERDAS.md](docs/ARCGIS_QGIS_ERDAS.md).

## Agentic AI contract

The orchestrator never performs an operational action directly. It produces a typed recommendation containing evidence, confidence, missing inputs and an approval requirement. Integrations can then create a draft work order, alert or map package only after authorization.

## Reproducibility and ethics

- Never label simulated results as observed events.
- Record CRS, resolution, acquisition time, sensor and processing lineage.
- Split training/validation data spatially to reduce geographic leakage.
- Report confidence and failure cases, not only headline accuracy.
- Validate demographic and service-equity impacts.
- Respect upstream licenses; this repository implements original reference code and links to inspirations.

## Open-source techniques reviewed

- [opengeos/geoai](https://github.com/opengeos/geoai) — imagery search, dataset preparation, training, inference and visualization.
- [giswqs/segment-geospatial](https://github.com/opengeos/segment-geospatial) — promptable geospatial segmentation.
- [torchgeo/torchgeo](https://github.com/microsoft/torchgeo) — geospatial datasets, samplers, transforms and pretrained models.
- [tsinghua-fib-lab/DRL-urban-planning](https://github.com/tsinghua-fib-lab/DRL-urban-planning) — human–AI spatial planning with deep reinforcement learning.
- [gboeing/osmnx](https://github.com/gboeing/osmnx) — street-network acquisition and analysis.
- [USEPA/WNTR](https://github.com/USEPA/WNTR) and [USEPA/EPANET2.2](https://github.com/USEPA/EPANET2.2) — resilient water-network analysis and hydraulics.
- [pyswmm/pyswmm](https://github.com/pyswmm/pyswmm) and [Zhiyu014/GNN-UDS](https://github.com/Zhiyu014/GNN-UDS) — drainage simulation, hydraulic surrogates and real-time control research.

## Citation

Use the metadata in [CITATION.cff](CITATION.cff). Contributions, regional case studies and benchmark datasets are welcome.

## License

MIT for original code in this repository. Third-party datasets, models and linked projects retain their own licenses.
