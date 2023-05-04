import string
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
import pickle
from Database_processing.Friends_db.get_friends import get_fr_by_username

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


def add_fr_request(username,_fr_rq):
    if (username==_fr_rq): return "Fail..."
    _f=get_fr_requested_by_username(username)
    if(_fr_rq not in _f) :
        _fr=get_fr_by_username(username)
        if (_fr_rq in _fr): 
            print(1)
            return (_fr_rq+" was friend")
        else :
            print (0)
            ff=get_fr_request_by_username(_fr_rq)
            ff.append(username)
            collection.update_one({"username":_fr_rq},{"$set":{"friend_request":ff}})
            # _f.append(username)
            add_fr_requested(username,_fr_rq)
            return ("Request Sent! "+_fr_rq)
        

    
