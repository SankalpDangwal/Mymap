import folium
import pandas as pd
 
map = folium.Map(location=[39.33, -98.33], zoom_start=6, titles="Stammen terrain")
data = pd.read_csv(r"C:/Users/sankalp.dangwal/Downloads/original.txt")
def color_procedure(elevation):
    if elevation > 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

fg = folium.FeatureGroup(name="My Map")
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln],radius=6, popup= str(el),fill_color=color_procedure(el), color= 'grey', fill_capacity=0.7))

fg.add_child(folium.GeoJson(data=(open("C:/Users/sankalp.dangwal/Desktop/world.json",'r', encoding='utf-8-sig').read())))

map.add_child(fg)
map.save("try.html")