# 🗺️ OpenAI to Z Challenge – Amazonian Discovery Project

Welcome to the expedition.

This project aims to discover and verify undocumented archaeological sites in the Amazon Basin using AI models, remote sensing data, Indigenous knowledge, and historical overlays.

---

## 🔍 Project Objective

- Detect previously unknown sites linked to ancient Amazonian civilizations
- Use open-source lidar, NDVI, ADE, myth-path, and paleoclimate datasets
- Validate sites through two independent modalities
- Generate high-quality, reproducible outputs for Kaggle’s OpenAI to Z submission

---

## 📁 Folder Structure

```
data/               → Archived sources (archaeology, oral history, soil, flora/fauna)
notebooks/          → Jupyter workflows for processing and analysis
src/                → Python modules (RevivalNet, TimefoldNet, ingest scripts)
outputs/            → Anomaly maps, GeoJSONs, and final writeup
maps_exports/       → Final KMZ/PNG/PDF visual ---

## 🗺️ Maps Exports Documentation

### Purpose
The `maps_exports/` folder contains maps generated from GPS coordinates overlaid on Google Maps. These maps are designed for visualization and analysis purposes.

### File Formats
- **PNG/JPEG**: For static image maps.
- **GeoJSON**: For interactive map data.
- **PDF**: For high-quality print-ready maps.

### File Naming Conventions
Files are named using the following format:
- `map_<timestamp>.png`
- `map_<location>.geojson`

### Usage
1. **Generate Maps**:
   - Use the provided scripts to process GPS coordinates and overlay them on Google Maps.
   - Export maps in desired formats (e.g., PNG, GeoJSON, PDF).

2. **Examples**:
   - `map_20230530.png`: Static map image generated on May 30, 2023.
   - `map_amazon_rainforest.geojson`: Interactive map of the Amazon Rainforest.

### Notes
- Ensure all generated files are validated for accuracy and compatibility before upload.
- Use consistent naming conventions for better organization.

---

## 🧠 Models in Use

- **RevivalNet**: weighted prediction grid (NDVI, fire, fauna, trails, CHM, myth)
- **TimefoldNet**: memory-decay + epoch validation model (anchored to paleodata)

---

## ✅ Submission Criteria

To comply with Kaggle rules:
- Use at least 2 open data sources per site
- Cite lidar tile IDs, DOI, or dataset links
- Ensure reproducibility of each prediction pipeline

---

## 🛠️ AOI Status Tracker

See `project_config.yaml` for active region tracking, validation phases, and overlay status.

---

## 📜 Automation Script Setup

### Purpose
Scripts for automating map generation and exporting are available in the repository. These scripts use Python libraries and APIs to process GPS data.

### Workflow
1. **Input**: Read GPS coordinates from a file or database.
2. **Processing**: Use Python libraries like `folium`, `matplotlib`, or `geopy` to visualize data.
3. **Overlay**: Integrate Google Maps API for map overlays.
4. **Export**: Save maps in PNG, GeoJSON, or PDF formats.

### Example Libraries
- **folium**: For creating interactive maps.
- **matplotlib**: For visualizing map data.
- **geopy**: For handling GPS data.
- **Google Maps API**: For advanced overlays.

---

Final submission due **June 29, 2025**. Let’s uncover the lost civilizations beneath the canopy.

---

