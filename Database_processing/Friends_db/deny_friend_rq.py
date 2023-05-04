from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# from Database_processing.Friends_db.get_request_fr import get_by_username
# from UI.Friends import Friends_frame
import json
# import pickle

from Utils.Sources.getdata_pickle import load_object

uri = json.loads(open("adminAuth/adminAuth.json","r").read())["uri"]
cluster=MongoClient(uri, server_api=ServerApi('1'))
db=cluster['AI_db']
collection=db['User_db']

def deny_fr(user):
    __=load_object("Appdata/userData/data.pickle")
    _username=__['data']['username']
    _data=collection.find_one({'username':_username})
    _rq=_data['friend_request']
    _rq.remove(user)
    collection.update_one({"username":_username},{"$set":{'friend_request':_rq}})

    __data=collection.find_one({'username':user})
    _rqt=__data['friend_requested']
    _rqt.remove(_username)
    collection.update_one({"username":user},{"$set":{'friend_requested':_rqt}})




    