"'""libreria para manejo de mapas"""
import folium #pip install folium

"'""Create a map object"""
#Para buscar las coordenadas: https://www.latlong.net
mapObj = folium.Map(location=[4.649802, -74.055774],zoom_start=20, width=800, height=500)
# save the map as a HTML file
mapObj.save("templates/output.html")