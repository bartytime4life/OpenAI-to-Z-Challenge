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
maps_exports/       → Final KMZ/PNG/PDF visual overlays
```

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

Final submission due **June 29, 2025**. Let’s uncover the lost civilizations beneath the canopy.
