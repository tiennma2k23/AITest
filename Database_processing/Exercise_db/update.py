from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
import pickle

# from body_part_angle import BodyPartAngle
from Utils.Calc.types_of_exercise import TypeOfExercise
from Utils.Calc.utils import *
from UI.UI import UserHandle
from Utils.Sources.getdata_pickle import load_object

uri = json.loads(open("adminAuth/adminAuth.json","r").read())["uri"]
cluster=MongoClient(uri, server_api=ServerApi('1'))
db=cluster['excercise_db_test']

def update(username,counter,exType):
    exercise_type=exType
    collection=db[exercise_type]
    if(collection.count_documents({"username":username})==0):
        collection.insert_one({"_id":username,"username":username,"counter":0})
    collection.update_one({"username":username},{"$inc":{"counter":counter}})
