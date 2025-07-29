import folium
import pandas as pd

df = pd.read_csv("data_with_latitudes_longitudes.csv")

m = folium.Map(location=[df['latitude'].mean() -0.5, df['longitude'].mean() + 1], zoom_start=10)

colors = ['red', 'blue', 'green', 'purple', 'orange']

for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=6,
        color=colors[row['cluster'] % len(colors)],
        fill=True,
        fill_opacity=0.7,
        popup=folium.Popup(f"{row['location1']} - Cluster {row['cluster']}", max_width=200),
        tooltip=row['location1']
    ).add_to(m)

m.save("./static/clusters_map.html")