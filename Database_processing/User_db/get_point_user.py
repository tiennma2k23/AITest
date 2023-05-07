from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json

uri = json.loads(open("adminAuth/adminAuth.json","r").read())["uri"]
cluster=MongoClient(uri, server_api=ServerApi('1'))
db=cluster['AI_db']
_dbex=cluster['excercise_db_test']
exType=['squat','pull-up','sit-up','push-up','walk']
def get_point_username(info):
    User_db=db['User_db']
    xx=User_db.find_one({'username':info})
    if (xx is None): return 0
    point=0
    for x in exType:
        __=_dbex[x]
        _dt=__.find_one({"username":info})
        if (_dt is not None):
            if (exType=='walk'):
                point+=0.01*_dt['counter']
            else : point+=_dt['counter']
    point*=(xx['login_days']*0.01+1)
    return round(point,2)

