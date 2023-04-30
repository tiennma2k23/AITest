import tkinter as tk
import tkinter.messagebox as messagebox
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
import pickle

# from body_part_angle import BodyPartAngle
from Utils.Calc.types_of_exercise import TypeOfExercise
from Utils.Calc.utils import *
from UI.UI import UserHandle
from UI.chooseEx import chooseEx
"""
uri = json.loads(open("adminAuth/adminAuth.json","r").read())["uri"]
cluster=MongoClient(uri, server_api=ServerApi('1'))

#Check connection
try:
    cluster.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
"""
# Save and get data
def save_object(obj):
    try:
        with open("Appdata/userData/data.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)
def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)


# Get user_db
user_db=load_object("Appdata/userData/data.pickle")
print(user_db)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("746x661")
        self.title('Demo')


        self.protocol("WM_DELETE_WINDOW", self.onClose)
        self.Authed = tk.BooleanVar(self, False)
        self.auth = UserHandle(self)
        self.main = chooseEx(self)

        self.auth.pack()

    def onClose(self):
        if (messagebox.askyesno('Quit?', 'U quit?')):
            self.Authed.set(False)
            self.destroy()

app = App()
app.mainloop()
"""
exercise_type=exType
collection=db[exercise_type]

username=user_db['username']
if(collection.count_documents({"username":username})==0):
    collection.insert_one({"_id":username,"username":username,"counter":0})
collection.update_one({"username":username},{"$inc":{"counter":counter}})
"""
