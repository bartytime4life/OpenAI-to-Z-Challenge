import pytest
from src.scoring_pipeline import score_aoi

def test_score_aoi_basic():
    dummy_aoi = {
        'elev_mean': 100,
        'slope': 2,
        'pattern_score': 0.8,
        'flora_flag': True,
        'trail_link': 5.0,
    }
    score = score_aoi(dummy_aoi)
    assert isinstance(score, float)
    assert 0.0 <= score <= 1.0
