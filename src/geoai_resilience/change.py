import numpy as np

def normalized_difference(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    a, b = np.asarray(a,dtype=float), np.asarray(b,dtype=float)
    return np.divide(a-b, a+b, out=np.zeros_like(a), where=np.abs(a+b)>1e-12)

def spectral_change(red_before, nir_before, red_after, nir_after, threshold: float=.20, valid_mask=None) -> dict:
    """NDVI difference with validity mask, confidence proxy and change accounting."""
    before = normalized_difference(np.asarray(nir_before), np.asarray(red_before))
    after = normalized_difference(np.asarray(nir_after), np.asarray(red_after))
    delta = after-before
    valid = np.ones(delta.shape,dtype=bool) if valid_mask is None else np.asarray(valid_mask,dtype=bool)
    changed = (np.abs(delta) >= threshold) & valid
    confidence = np.clip(np.abs(delta)/max(threshold,1e-6),0,1)
    return {"ndvi_before":before,"ndvi_after":after,"delta":delta,"changed":changed,"confidence":confidence,"changed_pixels":int(changed.sum()),"valid_pixels":int(valid.sum())}
