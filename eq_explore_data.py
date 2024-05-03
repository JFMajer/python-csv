from pathlib import Path
import plotly.express as px
import json

path = Path('eq-data/eq_data_30_day_m1.geojson')
content = path.read_text()
all_eq_data = json.loads(content)

path = Path('eq-data/readable_eq_data.geojson')
readable_content = json.dumps(all_eq_data, indent=4)
path.write_text(readable_content)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

magnitudes, lons, lats = [], [], []
for eq in all_eq_dicts:
    magnitudes.append(eq["properties"]["mag"])
    lons.append(eq["geometry"]["coordinates"][0])
    lats.append(eq["geometry"]["coordinates"][1])


print(magnitudes[:10])
print(lons[:10])
print(lats[:10])

title = "Global Earthquakes"
fig = px.scatter_geo(lat=lats, lon=lons, size=magnitudes, title=title, 
    color=magnitudes,
    color_continuous_scale='Viridis',
    labels={'color':"Magnitude"},
    projection='natural earth',
    )
fig.show()