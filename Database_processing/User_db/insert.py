from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
import pickle

# from body_part_angle import BodyPartAngle
from Utils.Calc.types_of_exercise import TypeOfExercise
from Utils.Calc.utils import *
# from UI.UI import UserHandle
from Utils.Sources.getdata_pickle import load_object
from img_processing.img_base64 import img_base64

uri = json.loads(open("adminAuth/adminAuth.json","r").read())["uri"]
cluster=MongoClient(uri, server_api=ServerApi('1'))
db=cluster['AI_db']
collection=db['User_db']
def insert(username,email,password):
    
    if(collection.count_documents({"username":username})==0):
        collection.insert_one({'username':username,'email':email,'password':password,'friend_list':[],'friend_request':[],'friend_requested':[],'login_time':'','login_days':0,'img_profile':img_base64("UI/assets/profile/image_3.png"),
                               'gendermale':True,'first_login':False,'activate':False,'locate':''})
        # True la Nam False la Nu 
        return {'status':"OK"}
    else:
        return {'status':"Username already exist"}