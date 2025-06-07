import os
from celery import Celery
from model_loader import load_models
from data_pipeline.process_features import extract_features
from scripts.utils_map import save_geojson, save_kmz
import psycopg2

celery = Celery(
    'tasks',
    broker=os.getenv("REDIS_URL","redis://redis:6379/0"),
    backend=os.getenv("REDIS_URL","redis://redis:6379/0")
)

def get_db():
    return psycopg2.connect(dbname="engine", user="engine",
                            password="changeme", host="db")

@celery.task(name="tasks.enqueue_prediction")
def enqueue_prediction(job_id, polygon_geojson):
    df = extract_features(polygon_geojson)
    revival, timefold, ensemble = load_models()
    spatial_feats = revival.predict(df['spatial_stack'])
    temp_feats = timefold.predict(df['ndvi_series'])
    fused = spatial_feats  # placeholder
    probs = ensemble.predict_proba(fused)[:,1]
    df['prob'] = probs
    top = df.nlargest(24, 'prob')
    os.makedirs('/data/results', exist_ok=True)
    save_geojson(top, f"/data/results/{job_id}.geojson")
    save_kmz(top, f"/data/results/{job_id}.kmz")
    conn = get_db(); cur = conn.cursor()
    cur.execute("UPDATE jobs SET status=%s WHERE id=%s", ('COMPLETED', job_id))
    conn.commit(); conn.close()
    return {"geojson": f"{job_id}.geojson", "kmz": f"{job_id}.kmz"}
