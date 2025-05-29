import os
import nbformat

# Step 1: Folder structure
folders = [
    "data/archaeology",
    "data/culture_history",
    "data/fauna_flora",
    "data/cores",
    "data/links_archive",
    "data/misc",
    "maps_exports",
    "notebooks",
    "src/ingest",
    "src/utils",
    "src/revivalnet",
    "src/timefoldnet",
    "outputs/overlays",
    "outputs/anomaly_registry",
    "outputs/visuals",
    "outputs/kaggle_submission"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Step 2: README
readme = """# 🗺️ OpenAI to Z Challenge – Amazonian Discovery Project

Welcome to the expedition.

This project aims to discover and verify undocumented archaeological sites in the Amazon Basin using AI models, remote sensing data, Indigenous knowledge, and historical overlays.

...

Final submission due **June 29, 2025**. Let’s uncover the lost civilizations beneath the canopy.
"""

with open("README.md", "w") as f:
    f.write(readme)

# Step 3: project_config.yaml
yaml = """aois:
  - name: Kuhikugu
    status: active
    data_sources:
      - lidar: "OpenTopography tile XYZ"
      - oral_history: "Fritz 1707 mission trail"
      - soil: "ADE Schmidt 2020"
    overlays: [ndvi, myth_path, elevation]
    validation_phase: Phase II
    notes: "Promising site; anomaly cluster scored T1 by RevivalNet"

  - name: Llanos de Mojos
    status: active
    data_sources:
      - lidar: "USGS 1m DEM"
      - forest_age: "MapBiomas 2018"
    overlays: [chm, myth_alignment, hydrology]
    validation_phase: Phase I
    notes: "Pending TimefoldNet validation"

  - name: Orinoco (Placeholder)
    status: pending
    data_sources: []
    overlays: []
    validation_phase: Phase 0
"""

with open("project_config.yaml", "w") as f:
    f.write(yaml)

# Step 4: CHANGELOG.md
changelog = """# 📘 Project Changelog – OpenAI to Z Challenge

## ✅ Initial Foundation — Auto-generated

- Folder structure created
- Notebooks added (01–05)
- Scripts and configs established
"""

with open("CHANGELOG.md", "w") as f:
    f.write(changelog)

# Step 5: .gitignore
gitignore = """__pycache__/
*.py[cod]
.venv/
env/
venv/
.ipynb_checkpoints/
outputs/*
!outputs/overlays/
!outputs/anomaly_registry/
!outputs/visuals/
!outputs/kaggle_submission/
.DS_Store
Thumbs.db
"""

with open(".gitignore", "w") as f:
    f.write(gitignore)

# Step 6: Notebooks
notebook_defs = {
    "notebooks/01_data_ingest.ipynb": [
        "# 📥 Data Ingestion & Organization",
        "This notebook helps catalog and inspect raw data.",
        "import os\n\nfor root, dirs, files in os.walk('../data/'):\n    print(root, files)"
    ],
    "notebooks/02_overlay_generation.ipynb": [
        "# 🗺️ Overlay Generation",
        "Create spatial overlays from GeoJSON or SHP data.",
        "import geopandas as gpd\n# gpd.read_file()..."
    ],
    "notebooks/03_timefoldnet_validation.ipynb": [
        "# ⌛ TimefoldNet Epoch Validation",
        "Validate AOIs with paleoclimate time alignment.",
        "# TODO: Load SISAL or Neotoma data"
    ],
    "notebooks/04_site_crossvalidation.ipynb": [
        "# ✅ Anomaly Cross-Validation",
        "Score and validate anomalies from lidar + ADE + NDVI.",
        "# TODO: Spatial overlay scoring logic"
    ],
    "notebooks/05_kaggle_writeup.ipynb": [
        "# 📝 Final Kaggle Submission Writeup",
        "Generate final writeup with citations and visuals.",
        "# Markdown export steps here"
    ]
}

for path, cells in notebook_defs.items():
    nb = nbformat.v4.new_notebook()
    nb.cells = [
        nbformat.v4.new_markdown_cell(cells[0]),
        nbformat.v4.new_markdown_cell(cells[1]),
        nbformat.v4.new_code_cell(cells[2])
    ]
    with open(path, "w") as f:
        nbformat.write(nb, f)

# Step 7: Utility script
with open("src/utils/csv_to_geojson.py", "w") as f:
    f.write("""import csv, json, sys

def csv_to_geojson(csv_file, geojson_file, lat_field='latitude', lon_field='longitude'):
    features = []
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                lat = float(row[lat_field])
                lon = float(row[lon_field])
                props = {k: v for k, v in row.items() if k not in [lat_field, lon_field]}
                features.append({ "type": "Feature", "geometry": {"type": "Point", "coordinates": [lon, lat]}, "properties": props })
            except ValueError:
                continue
    geojson = {"type": "FeatureCollection", "features": features}
    with open(geojson_file, 'w') as f:
        json.dump(geojson, f, indent=2)
    print(f"✅ GeoJSON written to {geojson_file} with {len(features)} features.")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python csv_to_geojson.py input.csv output.geojson")
    else:
        csv_to_geojson(sys.argv[1], sys.argv[2])
""")

print("✅ Full project foundation created. Ready for GitHub commit.")
