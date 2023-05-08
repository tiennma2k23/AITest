from geopy.geocoders import Nominatim
from geopy import distance
import geocoder

_geocoder=Nominatim(user_agent="Exera")
# cur_locat=geocoder.ip('me')
# # print(cur_locat.json)
# home_cords=(cur_locat.latlng[0],cur_locat.latlng[1])

# cur_locat=_geocoder.geocode('Lê Lợi, Hồ Chí Minh')
# home_cords=(cur_locat.latitude, cur_locat.longitude)
# print(home_cords)

# def distFromUser(dest: str):
#     cords = _geocoder.geocode(dest)
#     dest_cords=(cords.latitude, cords.longitude)
#     return round(distance.distance(home_cords, dest_cords).kilometers, 2)

# def distFromUser_cords(cords: tuple):
#     return round(distance.distance(home_cords, cords).kilometers, 2)


def get_cords(addr: str) -> tuple:
    cords = _geocoder.geocode(addr, exactly_one=True, language='vi', country_codes='vn')
    # print(cords.raw)
    return (cords.latitude, cords.longitude)

def distBetween(p1: str, p2: str):
    dest_cords1=get_cords(p1)
    dest_cords2=get_cords(p2)
    return round(distance.distance(dest_cords1, dest_cords2).kilometers, 2)


def distBetween_cords(p1: tuple, p2: tuple):
    return round(distance.distance(p1, p2).kilometers, 2)

#print(distFromUser('Bách Khoa, Hai Bà Trưng, Hà Nội'))
