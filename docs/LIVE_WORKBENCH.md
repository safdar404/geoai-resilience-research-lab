# Live Workbench and Native GIS Integration

## Purpose

The live GeoAI Resilience Intelligence Suite demonstrates how the five research programs present validated spatial inputs, analytical parameters, results and provenance in ArcGIS Pro-style and QGIS-style workspaces.

**Live suite:** https://geoai-resilience-intelligence-suite.neat-grove-8624.chatgpt.site/

## Shared analysis contract

Every program should produce one validated analysis record that drives:

1. map features and symbology;
2. attribute-table rows;
3. summary indicators and confidence;
4. workflow status and provenance;
5. GeoJSON, CSV, report or GIS-package exports.

This avoids contradictory results between the map, lower analytical dashboard and downloaded files.

## Five program contracts

| Program | Primary inputs | Core processing | Required output |
|---|---|---|---|
| Urban Intelligence | parcels, roads, services, DEM, flood/protected constraints | projected-CRS validation, proximity, weighted suitability, exclusion masks | ranked candidate zones with factor audit |
| Flood Intelligence | hazard extent, population/assets, roads, shelters, gauges/forecast | exposure intersection, vulnerability and access scoring, uncertainty | prioritized response zones and affected assets |
| Utility Guardian | assets, topology, failures, condition, critical customers | topology validation, likelihood × consequence, network tracing | ranked assets, service impact and inspection actions |
| Drainage Lab | DEM, catchments, rainfall, pipes/nodes/outfalls | hydrology, runoff, capacity and surcharge assessment | hotspot nodes, capacity deficits and mitigation ranking |
| Earth Change AI | time-stamped imagery, AOI, cloud masks, QA samples | preprocessing, indices/classification, change detection, accuracy assessment | change polygons, transitions, area, confidence and QA pack |

## ArcGIS Pro pathway

Recommended native implementation:

- ArcGIS Pro project templates (`.aprx`) with program-specific maps and layouts.
- File/enterprise geodatabases with domains, subtypes, topology and metadata.
- ArcPy geoprocessing tools or Python toolboxes for deterministic execution.
- ModelBuilder models for auditable desktop automation.
- Spatial Analyst, Image Analyst and Network Analyst where licensed and applicable.
- Portal/ArcGIS Enterprise publishing for controlled services and dashboards.

The browser interface must not claim native execution unless a secured geoprocessing service or desktop bridge returns a signed job result.

## QGIS pathway

Recommended native implementation:

- QGIS project templates (`.qgz`) and GeoPackage/PostGIS workspaces.
- QGIS Processing models using GDAL, GRASS and SAGA where appropriate.
- PyQGIS processing providers for repeatable algorithms.
- QGIS plugins for authenticated job submission, progress and result loading.
- QField or Mergin-compatible field packages where field validation is required.

The browser interface must not claim local QGIS execution unless an installed plugin or configured processing API confirms the completed job.

## Integration API

A production connector should exchange a versioned job object:

```json
{
  "schema_version": "1.0",
  "program": "urban",
  "engine": "arcgis-pro",
  "crs": "EPSG:32643",
  "input_assets": [],
  "parameters": {},
  "requested_outputs": ["geojson", "csv", "report"],
  "approval": {"required": true}
}
```

A completed response should include job ID, engine/version, input checksums, projected CRS, processing log, output URLs, metrics, warnings and provenance.

## Operational readiness checklist

- [ ] Authoritative datasets and data-owner approvals
- [ ] Projected CRS selected for the study area
- [ ] Schema, geometry and topology validation
- [ ] Calibrated parameters and documented assumptions
- [ ] Unit, integration and regression tests
- [ ] Accuracy, uncertainty and failure-case reports
- [ ] ArcGIS/QGIS service endpoints and credentials
- [ ] STAC, PostGIS, telemetry, SCADA, CMMS and weather connectors
- [ ] Human approval and audit logging
- [ ] Honest status labels: demo/local until real services are connected

## Interface QA

The live demonstration supports program-specific ArcGIS Pro and QGIS views, layer visibility, map navigation feedback, tool selection, processing-panel switching, workflow completion, attribute-table visibility and responsive presentation. These interactions demonstrate the operating model; they do not replace native GIS execution.
