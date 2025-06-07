import folium
from src.map_interface import create_map

def test_create_map_runs():
    m = create_map(data_path='data/Archaeology_master.csv')
    assert hasattr(m, 'save')
