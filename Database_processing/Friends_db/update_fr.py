from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
import pickle

from Utils.Sources.getdata_pickle import load_object

uri = json.loads(open("adminAuth/adminAuth.json","r").read())["uri"]
cluster=MongoClient(uri, server_api=ServerApi('1'))
db=cluster['AI_db']

def update_fr_user(username,frlst):
    collection=db['User_db']
    collection.update_one({'username':username},{'$set':{'friend_list':frlst}})
    return True


