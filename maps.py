from geopy.geocoders import Nominatim
from geopy import distance
# import geocoder
import geocoder
# g = geocoder.ip('me')
# print(g.latlng)
_geocoder=Nominatim(user_agent=".")

location1=input("L1: ")
location2=input("L2: ")
cur_locat=geocoder.ip('me')


coordinates1=_geocoder.geocode(location1)
coordinates2=_geocoder.geocode(location2)
# coordinates3=_geocoder.geocode(cur_locat)

lat1,long1=(coordinates1.latitude),(coordinates1.longitude)
lat2,long2=(coordinates2.latitude),(coordinates2.longitude)
# lat3,long3=(coordinates3.latitude),(coordinates3.longitude)


place1=(lat1,long1)
place2=(lat2,long2)
place3=(cur_locat.latlng[0],cur_locat.latlng[1])
print(place1)
print(place3)
print(distance.distance(place1,place2))