from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from Database_processing.User_db.get import *
from Database_processing.Friends_db.add_fr_request import *
from Utils.Sources.getdata_pickle import load_object
import json
username=input("Username: ")
__=load_object("Appdata/userData/data.pickle")
_username=__['data']['username']
_db=get_by_username(username)
if (_db['status']):
    add_fr_request(_username,username)
else :
    print("Fail")
