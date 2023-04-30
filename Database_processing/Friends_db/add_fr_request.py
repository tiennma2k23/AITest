from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
import pickle

from Utils.Sources.getdata_pickle import load_object

uri = json.loads(open("adminAuth/adminAuth.json","r").read())["uri"]
cluster=MongoClient(uri, server_api=ServerApi('1'))
db=cluster['AI_db']
collection=db['User_db']
def get_fr_request_by_username(username):
    # collection=db['User_db']
    f=collection.find_one({'username':username})
    return f['friend_request']
def get_fr_requested_by_username(username):
    # collection=db['User_db']
    f=collection.find_one({'username':username})
    return f['friend_requested']
def add_fr_requested(username,_name):
    
    f=collection.find_one({'username':username})
    f_list=f['friend_requested']
    f_list.append(_name)
    collection.update_one({"username":username},{"$set":{"friend_requested":f_list}})


def add_fr_request(username_rq,username):
    _f=get_fr_requested_by_username(username)
    if(username_rq not in _f) :
        ff=get_fr_request_by_username(username_rq)
        ff.append(username)
        # _f.append(username_rq)
        add_fr_requested(username,username_rq)
        collection.update_one({"username":username},{"$set":{"friend_request":ff}})

    
