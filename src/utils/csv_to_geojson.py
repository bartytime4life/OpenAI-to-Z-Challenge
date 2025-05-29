import csv
import json
import sys

def csv_to_geojson(csv_file, geojson_file, lat_field='latitude', lon_field='longitude'):
    features = []

    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                lat = float(row[lat_field])
                lon = float(row[lon_field])
                props = {k: v for k, v in row.items() if k not in [lat_field, lon_field]}
                features.append({
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [lon, lat]
                    },
                    "properties": props
                })
            except ValueError:
                continue  # skip rows with invalid coordinates

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    with open(geojson_file, 'w', encoding='utf-8') as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)

    print(f"✅ GeoJSON written to {geojson_file} with {len(features)} features.")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python csv_to_geojson.py input.csv output.geojson")
    else:
        csv_to_geojson(sys.argv[1], sys.argv[2])
