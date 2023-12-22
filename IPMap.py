import geocoder
import folium

g = geocoder.ip("me")

myAddress = g.latlng
# print(myAddress)

app = folium.Map(location =[22.7179, 75.8333],
                     zoom_start =12)

folium.Marker(location=[22.7179, 75.8333],
              tooltip ="This is a tooltip",
              popup= "Current Location").add_to(app)

app.save("my_map.html")