import matplotlib.pyplot as plt
from shapely.geometry import Point
import geopandas as gpd
import pandas as pd
from geopy.distance import geodesic

# Core climate phase windows database
CORE_PHASES = {
    "Illimani": [
        {"label": "Dry/Dust Spike", "start": -2000, "end": -1000, "color": "red"},
        {"label": "Chiripa/Chavín Expansion", "start": -800, "end": -200, "color": "green"},
        {"label": "Volatile Transition", "start": -200, "end": 500, "color": "orange"},
        {"label": "Moche/Wari Stability", "start": 500, "end": 1000, "color": "green"},
        {"label": "Post-Wari Collapse", "start": 1000, "end": 1400, "color": "red"},
        {"label": "Inka Ascendancy", "start": 1400, "end": 1532, "color": "green"},
        {"label": "Colonial Mining Spike", "start": 1540, "end": 1800, "color": "gray"},
        {"label": "Industrial Era Signal", "start": 1900, "end": 2000, "color": "gray"},
    ]
}

def find_nearest_core(aoi_geojson_path, core_csv_path):
    aoi_gdf = gpd.read_file(aoi_geojson_path)
    aoi_center = aoi_gdf.geometry.unary_union.centroid

    core_df = pd.read_csv(core_csv_path)
    core_df["distance_km"] = core_df.apply(
        lambda row: geodesic((aoi_center.y, aoi_center.x), (row.latitude, row.longitude)).km,
        axis=1
    )
    nearest = core_df.sort_values("distance_km").iloc[0]
    return nearest

def plot_timefoldnet_timeline(core_name, filename=None):
    if core_name not in CORE_PHASES:
        print(f"No predefined climate phases found for core: {core_name}")
        return

    climate_windows = CORE_PHASES[core_name]
    fig, ax = plt.subplots(figsize=(12, 2))

    for phase in climate_windows:
        ax.axvspan(phase["start"], phase["end"], color=phase["color"], alpha=0.4, label=phase["label"])

    ax.set_xlim(-2000, 2025)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.set_xlabel("Year (BCE to CE)")
    ax.set_title(f"🕰️ TimefoldNet Epoch Validation – {core_name} Climate Phases")

    handles, labels = ax.get_legend_handles_labels()
    unique = dict(zip(labels, handles))
    ax.legend(unique.values(), unique.keys(), loc="upper center", bbox_to_anchor=(0.5, 1.4), ncol=4)

    plt.grid(True)
    plt.tight_layout()

    if filename:
        plt.savefig(filename)
        print(f"✅ Timeline saved to {filename}")
    else:
        plt.show()
