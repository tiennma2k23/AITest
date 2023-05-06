import numpy
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json

uri = json.loads(open("adminAuth/adminAuth.json","r").read())["uri"]
cluster=MongoClient(uri, server_api=ServerApi('1'))
db=cluster['locate_db']

def unique(lst):
    x=numpy.array(lst)
    return numpy.unique(x)

def get_arr_province():
    _data=db['data']
    __=_data.find({})
    arr=[]
    for x in __:
        arr.append(x['Province'])
    arr_ans=unique(arr)
    return arr_ans

print(get_arr_province())
        

