from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json

uri = json.loads(open("adminAuth/adminAuth.json","r").read())["uri"]
cluster=MongoClient(uri, server_api=ServerApi('1'))
db=cluster['AI_db']
collection=db['User_db']
def update_login_first(username,status):
    collection=db['User_db']
    collection.update_one({'username':username},{'$set':{'first_login':status}})
    return True
