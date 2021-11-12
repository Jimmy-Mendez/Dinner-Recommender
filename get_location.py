import geocoder
g = geocoder.ip('me')
coordinate1 = str(g.latlng[0])
coordinate2 = str(g.latlng[1])
coordinate = coordinate1 + ", " + coordinate2