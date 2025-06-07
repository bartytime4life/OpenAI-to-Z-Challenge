import geojson, simplekml

def save_geojson(df, path):
    features = []
    for _, r in df.iterrows():
        features.append(geojson.Feature(
            geometry=geojson.Point((r.lon, -r.lat)),
            properties={"ID": r.ID, "prob": float(r.prob)}
        ))
    fc = geojson.FeatureCollection(features)
    with open(path, "w") as f:
        geojson.dump(fc, f)

def save_kmz(df, path):
    kml = simplekml.Kml()
    for _, r in df.iterrows():
        p = kml.newpoint(name=r.ID, coords=[(r.lon, -r.lat)])
        p.description = f"Score: {r.prob:.2f}"
    kml.savekmz(path)
