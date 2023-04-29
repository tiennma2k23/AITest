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
    if (f is not None): 
        return {'status':True,'data':f}
    return {'status':False,'data':''}

def get_by_email(email):
    collection=db['User_db']
    f=collection.find_one({'email':email})
    if (f is not None): 
        return {'status':True,'data':f}
    return {'status':False,'data':''}

def find_user(info):
    l1=get_by_username(info)
    if (l1['status']): return {'status':True,'data':l1['data']}
    l2=get_by_email(info)
    if (l2['status']): return {'status':True,'data':l2['data']}
    return {'status':True,'data':''}

