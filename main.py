import tkinter as tk
import tkinter.messagebox as messagebox
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
# import json
# import pickle
from Utils.Sources.getdata_pickle import load_object
from Database_processing.Exercise_db.update import update

# from UI.chooseEx import chooseEx
# from UI.Homepage import homepage
from UI.UI_fewercode import UserHandle
from UI.Tabs import Tabs
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

# user_db=_db['data']
# print(user_db)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x480")
        # self.resizable(False, False)
        self.title('Demo')
        self.protocol("WM_DELETE_WINDOW", self.onClose)
        self.Authed = tk.BooleanVar(self, True)
        self.run()

    def run(self):
        self.auth = UserHandle(self)
        self.main = Tabs(self)
        _db=load_object("Appdata/userData/data.pickle")
        if(_db['status']==False): #Not pre-login
            self.Authed.set(False)
            self.auth.pack()
        else: 
            self.Authed.set(True)
            self.auth.destroy()
            self.main.pack()

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
