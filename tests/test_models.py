import numpy as np
import pytest
from geoai_resilience import suitability,flood_priority,asset_risk,rational_runoff,spectral_change

def test_urban_constraints_override_score():
    r=suitability({"access":.9,"climate":.8},{"access":1,"climate":1},{"floodway":True})
    assert r.score==0 and r.classification=="ineligible"
def test_flood_priority_increases_with_hazard():
    low=flood_priority(.2,.8,.7,.6).score; high=flood_priority(.9,.8,.7,.6).score
    assert high>low
def test_utility_risk_is_bounded():
    r=asset_risk(.9,.8,.7,.9,.6)
    assert 0<=r.score<=1 and r.requires_human_approval
def test_rational_method_units():
    r=rational_runoff(.7,90,2,20)
    assert r.peak_runoff_m3s==35 and r.status=="surcharge"
def test_change_mask_and_invalid_pixels():
    red0=np.array([[.2,.2]]);nir0=np.array([[.6,.6]])
    red1=np.array([[.4,.2]]);nir1=np.array([[.4,.6]])
    r=spectral_change(red0,nir0,red1,nir1,.2,[[True,False]])
    assert r["changed_pixels"]==1 and r["valid_pixels"]==1
def test_invalid_unit_input():
    with pytest.raises(ValueError): flood_priority(1.2,.2,.2,.2)
