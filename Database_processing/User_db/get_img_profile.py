from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json

uri = json.loads(open("adminAuth/adminAuth.json","r").read())["uri"]
cluster=MongoClient(uri, server_api=ServerApi('1'))
db=cluster['AI_db']
_dbex=cluster['excercise_db_test']
def get_img_profile(info):
    User_db=db['User_db']
    xx=User_db.find_one({'username':info})
    return xx['img_profile']

