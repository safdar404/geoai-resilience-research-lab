# ArcGIS, QGIS and ERDAS implementation guide

## ArcGIS Pro / ModelBuilder / ArcPy

- Enforce project CRS, snap raster, cell size, extent and geodatabase naming.
- Use topology rules for utility connectivity, duplicate geometry and boundary consistency.
- Package ModelBuilder chains for non-developer analysts; export validated logic to Python for testing and scheduling.
- Publish hosted/registered feature and imagery services only after metadata and QA.

## QGIS

- Use Processing models to expose GDAL, GRASS, SAGA and native algorithms.
- Exchange data through GeoPackage/COG/GeoJSON with explicit CRS and field schemas.
- Use QGIS Server or GeoServer for open OGC services where appropriate.

## ERDAS IMAGINE

- Inspect radiometry, sensor metadata, band order and no-data.
- Apply atmospheric/radiometric correction appropriate to the sensor and research question.
- Build spectral indices and classification/change models; export georeferenced raster outputs with lineage.
- Validate in GIS with stratified reference samples.

## Automation pattern

```text
watch data source
 → validate checksum/schema/CRS
 → preprocess imagery or network
 → run model
 → calculate uncertainty
 → create GIS layers and report
 → human QA/approval
 → publish service / draft work order
 → audit result
```
