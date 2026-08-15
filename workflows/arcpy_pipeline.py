"""ArcGIS Pro reference automation. Execute inside an ArcGIS Pro Python environment."""
def run(study_area, criteria_rasters, output_gdb):
    try:
        import arcpy
        from arcpy.sa import Raster, WeightedSum, SetNull
    except ImportError as exc:
        raise RuntimeError("ArcPy is available only in a licensed ArcGIS Pro environment") from exc
    arcpy.env.overwriteOutput=True
    arcpy.env.workspace=output_gdb
    arcpy.env.extent=study_area
    arcpy.env.snapRaster=criteria_rasters[0][0]
    arcpy.CheckOutExtension("Spatial")
    weighted=WeightedSum([[Raster(path),weight] for path,weight in criteria_rasters])
    result=SetNull(weighted<0,weighted)
    out=f"{output_gdb}/urban_suitability"
    result.save(out)
    arcpy.management.CalculateStatistics(out)
    return out
