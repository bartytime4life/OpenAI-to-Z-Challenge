

## Field Feedback Loop

A simple Flask app is provided for field teams to submit **AOI field notes**:

- Run the server:
```bash
cd src
python feedback_app.py
```

- **POST** feedback in JSON to `http://localhost:5000/feedback` with:
  ```json
  {
    "AOI_ID": "X11",
    "notes": "Visited site; walls eroded but mounds visible."
  }
  ```

- **GET** all feedback:
  ```
  curl http://localhost:5000/feedback
  ```

The `data/feedback.json` file will store all submissions and can be ingested back into the scoring pipeline (`scoring_pipeline.py`) using the `--feedback data/feedback.json` flag to adjust AOI scores.

## Installation Requirements

### Python Backend
Install Python dependencies:
```bash
pip install -r requirements.txt
```

### Frontend Explorer
Navigate to the `AOI_Explorer/` directory and install Node modules:
```bash
cd AOI_Explorer
npm install
```

Ensure you have Node.js (v14+) and npm installed.

### Running the Services
1. **Start the Flask feedback server**:
   ```bash
   cd src
   python feedback_app.py
   ```
2. **Run the scoring pipeline**:
   ```bash
   python scoring_pipeline.py --input ../data/Archaeology_master.csv --feedback ../data/feedback.json --output ../results/AOI_index.csv
   ```
3. **Run the frontend locally**:
   ```bash
   cd ../AOI_Explorer
   npm run dev
   ```

## Prerequisites

Before installation, ensure the following OS-level dependencies are installed:

### Ubuntu / Debian
```bash
sudo apt update
sudo apt install -y gdal-bin libgdal-dev libgeos-dev proj-bin libproj-dev libspatialindex-dev
```

### macOS (Homebrew)
```bash
brew install gdal geos proj spatialindex
```

### Environment Variables
Create a `.env` file in the project root with:
```bash
EARTHDATA_USER=<your_earthdata_username>
EARTHDATA_PASS=<your_earthdata_password>
OPENAI_API_KEY=<your_openai_api_key>
```


### System Dependencies

On **Ubuntu**:
```bash
sudo apt update
sudo apt install -y gdal-bin libgdal-dev libgeos-dev proj-bin libproj-dev libspatialindex-dev
```

On **macOS** (Homebrew):
```bash
brew install gdal geos proj spatialindex
```

### Environment Variables

Copy `.env.sample` to `.env` and fill in credentials:
```bash
cp .env.sample .env
```

### Data Download

Use the stub script to fetch datasets:
```bash
python3 src/download_data.py --gedi --anadem --jers --lidar --output data/raw
```

### Docker Setup (Optional)

Build and run all services via Docker Compose:
```bash
docker-compose up --build
```


## Environment Configuration

Copy the `.env.example` to `.env` and fill in your credentials:
```bash
cp .env.example .env
```

## Data Download

Use the `download_data.py` script to fetch large datasets:
```bash
python src/download_data.py
```

## Docker Deployment

Build and run all services via Docker Compose:
```bash
docker-compose up --build
```
- **backend** runs the Flask feedback server on port 5000  
- **pipeline** executes the scoring pipeline  
- **frontend** serves the React app on port 3000  
