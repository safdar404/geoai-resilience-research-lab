"""QGIS Processing reference script; run from the QGIS Python console."""
def build_change_polygons(before, after, threshold, output):
    from qgis import processing
    delta=processing.run("gdal:rastercalculator",{"INPUT_A":before,"BAND_A":1,"INPUT_B":after,"BAND_B":1,"FORMULA":"abs(B-A)","OUTPUT":"TEMPORARY_OUTPUT"})["OUTPUT"]
    mask=processing.run("gdal:rastercalculator",{"INPUT_A":delta,"BAND_A":1,"FORMULA":f"A>{threshold}","OUTPUT":"TEMPORARY_OUTPUT"})["OUTPUT"]
    return processing.run("gdal:polygonize",{"INPUT":mask,"BAND":1,"FIELD":"change","EIGHT_CONNECTEDNESS":True,"OUTPUT":output})["OUTPUT"]
