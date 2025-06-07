FROM python:3.11-slim
WORKDIR /updater
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY etl/update_pipeline.py etl/update_pipeline.py
CMD ["python", "etl/update_pipeline.py"]
