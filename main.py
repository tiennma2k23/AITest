import tkinter as tk
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
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
from UI.Questions import question
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
        self.geometry("%dx%d+%d+%d" % (800, 480, (self.winfo_screenwidth()/2 - 800/2), (self.winfo_screenheight()/2-480/2)))
        self.iconphoto(True, ImageTk.PhotoImage(Image.open('logo.png')))
        # self.resizable(False, False)
        self.title('EXERA')
        self.protocol("WM_DELETE_WINDOW", self.onClose)
        self.Authed = tk.BooleanVar(self, True)
        self.run()

    def run(self):
        self.auth = UserHandle(self)
        self.main = Tabs(self)
        self.questions = question(self)
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
