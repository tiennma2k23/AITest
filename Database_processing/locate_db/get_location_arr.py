import numpy
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json

uri = json.loads(open("adminAuth/adminAuth.json","r").read())["uri"]
cluster=MongoClient(uri, server_api=ServerApi('1'))
db=cluster['locate_db']
_data=db['data']
def unique(lst):
    # x=numpy.array(lst)
    return set(lst)

def get_arr_province():
    __=_data.find({})
    arr=[]
    for x in __:
        arr.append(x['Province'])
    arr_ans=unique(arr)
    return arr_ans

def get_arr_district(province: str):
    __ = _data.find({'Province': province})
    arr = []
    for x in __:
        arr.append(x['District'])
    arr_ans=unique(arr)
    return arr_ans


def get_arr_commune(province : str, district: str):
    __ = _data.find({'Province': province, 'District': district})
    arr = []
    for x in __:
        arr.append(x['Commune'])
    arr_ans=unique(arr)
    return arr_ans
# print(get_arr_district('Hồ Chí Minh'))