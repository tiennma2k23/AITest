from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
import base64
uri = json.loads(open("adminAuth/adminAuth.json","r").read())["uri"]
cluster=MongoClient(uri, server_api=ServerApi('1'))
db=cluster['locate_db']
collection=db['shop_db']

def get_shop():
    return list(collection.find({}).limit(20))