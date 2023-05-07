from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from geopy.geocoders import Nominatim
import json
import base64
uri = json.loads(open("adminAuth/adminAuth.json","r").read())["uri"]
cluster=MongoClient(uri, server_api=ServerApi('1'))
db=cluster['locate_db']
collection=db['shop_db']
_geocoder=Nominatim(user_agent="Exera")

def img_base64(url):
    with open(url, "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    return(my_string)

def addShop(name: str, addr: str, imgFile: str, value, cost):
    cords_item = _geocoder.geocode(addr)
    cords = (cords_item.latitude, cords_item.longtitude)
    collection.insert_one({'name':name,
                           'addr': addr,
                           'cords': cords,
                           'img': img_base64('Database_processing/locate_db/'+imgFile),
                           'value': value,
                           'cost': cost})
