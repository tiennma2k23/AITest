from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json

from Database_processing.User_db.get_point_user import get_point_username

uri = json.loads(open("adminAuth/adminAuth.json","r").read())["uri"]
cluster=MongoClient(uri, server_api=ServerApi('1'))
db=cluster['AI_db']
_dbex=cluster['excercise_db_test']
def get_point_data():
    arr=[]
    User_db=db['User_db']
    _userdb=User_db.find({})
    for x in _userdb:
        arr.append({'username':x['username'],'point':get_point_username(x['username']),'img_url':x['img_profile']})
    arr.sort(key=lambda x: x['point'], reverse=True)
    for i in range(len(arr)):
        arr[i]['rank']=i+1
    return arr

# print(get_point_data())
    

