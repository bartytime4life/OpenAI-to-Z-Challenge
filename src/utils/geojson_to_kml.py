import geopandas as gpd
import simplekml
import sys

def geojson_to_kml(geojson_path, kml_path):
    gdf = gpd.read_file(geojson_path)
    kml = simplekml.Kml()

    for _, row in gdf.iterrows():
        geom = row.geometry
        props = row.drop(labels='geometry').to_dict()

        if geom.geom_type == 'Point':
            p = kml.newpoint(name=props.get('site_name', 'Site'), coords=[(geom.x, geom.y)])
        elif geom.geom_type == 'Polygon':
            p = kml.newpolygon(name=props.get('source', 'Overlay'))
            p.outerboundaryis = [(x, y) for x, y in geom.exterior.coords]
        else:
            continue

        # Style
        p.style.iconstyle.color = simplekml.Color.red  # default red
        p.style.iconstyle.scale = 1.1
        p.style.linestyle.width = 2
        p.style.linestyle.color = simplekml.Color.black

    kml.save(kml_path)
    print(f"✅ KML saved to {kml_path}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python geojson_to_kml.py input.geojson output.kml")
    else:
        geojson_to_kml(sys.argv[1], sys.argv[2])
