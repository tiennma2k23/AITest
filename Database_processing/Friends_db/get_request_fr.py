from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
import pickle

from Utils.Sources.getdata_pickle import load_object

uri = json.loads(open("adminAuth/adminAuth.json","r").read())["uri"]
cluster=MongoClient(uri, server_api=ServerApi('1'))
db=cluster['AI_db']

def get_by_username(username):
    collection=db['User_db']
    f=collection.find_one({'username':username})
    return f['friend_request']


