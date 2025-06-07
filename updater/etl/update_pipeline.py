import os
from data_pipeline.download_data import fetch_satellite_data
from data_pipeline.process_features import build_ndvi_series, build_chm, build_ade_prob
import psycopg2

def get_db():
    return psycopg2.connect(dbname="engine", user="engine", password="changeme", host="db")

def update_pipeline():
    fetch_satellite_data(start="2025-01-01", end="2025-06-01")
    build_ndvi_series()
    build_chm()
    build_ade_prob()
    conn = get_db(); cur = conn.cursor()
    cur.execute("REFRESH MATERIALIZED VIEW feature_tiles;")
    conn.commit(); conn.close()

if __name__ == "__main__":
    update_pipeline()
