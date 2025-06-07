import os
import uuid
from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from celery import Celery
import psycopg2
import geojson
from starlette.responses import StreamingResponse

celery = Celery(
    broker=os.getenv("REDIS_URL", "redis://redis:6379/0"),
    backend=os.getenv("REDIS_URL", "redis://redis:6379/0")
)

def get_db():
    return psycopg2.connect(
        dbname="engine", user="engine", password="changeme", host="db"
    )

class PredictRequest(BaseModel):
    polygon_geojson: dict

app = FastAPI(title="ADE API")

@app.post("/predict")
async def submit_prediction(req: PredictRequest):
    job_id = str(uuid.uuid4())
    conn = get_db(); cur = conn.cursor()
    cur.execute("INSERT INTO jobs (id, status) VALUES (%s, %s)", (job_id, 'PENDING'))
    conn.commit(); conn.close()
    celery.send_task("tasks.enqueue_prediction", args=[job_id, req.polygon_geojson])
    return {"job_id": job_id}

@app.get("/status/{job_id}")
async def job_status(job_id: str):
    conn = get_db(); cur = conn.cursor()
    cur.execute("SELECT status FROM jobs WHERE id=%s", (job_id,))
    row = cur.fetchone(); conn.close()
    if not row: raise HTTPException(404, "Job not found")
    return {"job_id": job_id, "status": row[0]}

@app.get("/aoi/{job_id}/result.geojson")
async def get_result_geojson(job_id: str):
    path = f"/data/results/{job_id}.geojson"
    if not os.path.exists(path): raise HTTPException(404, "Result not ready")
    return geojson.load(open(path))

@app.get("/aoi/{job_id}/report.pdf")
async def download_report(job_id: str):
    path = f"/data/reports/{job_id}.pdf"
    if not os.path.exists(path): raise HTTPException(404, "Report not found")
    return StreamingResponse(open(path, "rb"), media_type="application/pdf")
