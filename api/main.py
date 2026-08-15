from fastapi import FastAPI
from pydantic import BaseModel, Field
from geoai_resilience import suitability, flood_priority, asset_risk, rational_runoff

app=FastAPI(title="GeoAI Resilience Research API",version="0.1.0",description="Transparent reference endpoints; human approval is required for operational action.")

class FloodInput(BaseModel):
    hazard:float=Field(ge=0,le=1);exposure:float=Field(ge=0,le=1);vulnerability:float=Field(ge=0,le=1);access_disruption:float=Field(ge=0,le=1);data_completeness:float=Field(1,ge=0,le=1)
class DrainageInput(BaseModel):
    coefficient:float=Field(ge=0,le=1);intensity_mm_h:float=Field(ge=0);area_km2:float=Field(ge=0);capacity_m3s:float=Field(gt=0)
class UtilityInput(BaseModel):
    age_ratio:float=Field(ge=0,le=1);break_history:float=Field(ge=0,le=1);condition_deficit:float=Field(ge=0,le=1);service_criticality:float=Field(ge=0,le=1);graph_betweenness:float=Field(0,ge=0,le=1)
class UrbanInput(BaseModel):
    criteria:dict[str,float];weights:dict[str,float];constraints:dict[str,bool]={}

@app.get("/health")
def health(): return {"status":"healthy","operational_claim":"research-demonstration"}
@app.post("/v1/flood")
def flood(x:FloodInput): return flood_priority(**x.model_dump()).as_dict()
@app.post("/v1/drainage")
def drainage(x:DrainageInput): return rational_runoff(**x.model_dump()).as_dict()
@app.post("/v1/utility")
def utility(x:UtilityInput): return asset_risk(**x.model_dump()).as_dict()
@app.post("/v1/urban")
def urban(x:UrbanInput): return suitability(**x.model_dump()).as_dict()
