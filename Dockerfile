# Dockerfile for OpenAI-to-Z Challenge

FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gdal-bin libgdal-dev libgeos-dev proj-bin libproj-dev libspatialindex-dev \
    && rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Install Node.js and dependencies for frontend
RUN apt-get update && apt-get install -y curl git \
    && curl -fsSL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/AOI_Explorer
RUN npm install

# Expose ports for Flask and frontend
EXPOSE 5000 3000

# Default command: run flask and frontend (could be improved with scripts)
WORKDIR /app
CMD ["bash", "-c", "cd src && python feedback_app.py & cd ../AOI_Explorer && npm run dev"]
