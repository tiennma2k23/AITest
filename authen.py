import pyrebase
import json
import tkinter as tk
from requests.exceptions import HTTPError
import os 
from subprocess import call
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# import json
import utils


uri = json.loads(open("adminAuth.json","r").read())["uri"]
cluster=MongoClient(uri, server_api=ServerApi('1'))
db=cluster['AI_db']
collection=db['User_db']
 
# Save and get data
import pickle
def save_object(obj):
    try:
        with open("data.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)
def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return {'status':True,'data':pickle.load(f)}
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)
        return {'status':False,'data':'Error during unpickling object (Possibly unsupported):'+ex}
 
# obj = load_object("data.pickle")

config=json.load(open('firebase_config.json', 'r'))
firebase=pyrebase.initialize_app(config)
auth=firebase.auth()

class Auth(tk.Tk):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.geometry('800x480')
        self.username = tk.StringVar(self, '')
        self.password = tk.StringVar(self, '')
        self.newUser = tk.BooleanVar(self, False)

        self.authF = tk.Frame(self)
        self.usrLabel = tk.Label(self.authF, text="Username: ").pack()
        self.pswLabel = tk.Label(self.authF, text="Password: ").pack()
        self.usrEntry = tk.Entry(self.authF, width=20, textvariable=self.username).pack()
        self.pswEntry = tk.Entry(self.authF, width=20, textvariable=self.password).pack()
        self.smbBtn = tk.Button(self.authF, text="Login", command=self.UsrAuth).pack()
        self.reg = tk.Checkbutton(self.authF, text="New account?", command=lambda: self.newUser.set(not self.newUser.get())).pack()
        self.authF.pack()

    def UsrAuth(self):
        print('New User = ', self.newUser.get())
        if (self.newUser.get()):
            try:
                self.user = auth.create_user_with_email_and_password(self.username.get(), self.password.get())
                
                auth.send_email_verification(self.user['idToken'])
                UID=self.user['localId']
                username=input("Username: ")
                fullname=input("Fullname: ")
                user_db={
                    'username':username,
                    'email':self.username.get(),
                    'password':self.password.get(),
                    'fullname':fullname,
                }
                
                collection.insert_one(user_db)
                print("User Created!")
                self.destroy()
            except HTTPError as e:
                print(json.loads(e.args[1]))
        else:
            try:
                _username=self.username.get()
                _password=self.password.get()
                lst1=collection.find_one({'username':_username})
                lst2=collection.find_one({'email':_username})
                # lst1.extend(lst2)
                # print(lst1)
                if ((lst1 is None) and (lst2 is None)):
                    print("Khong ton tai TK! Vui long thu lai hoac nhap email de dang ki")
                else :
                    if (lst1 is not None):
                        user_db=lst1
                    else : user_db=lst2
                    self.user = auth.sign_in_with_email_and_password(user_db['email'],_password)
                    save_object(user_db)
                    print("Access Granted!")
                    # os.system('python main.py')
                    # Popen('python main.py')
                
                    # main.Main()
                    self.destroy()
                    call(["python3","main.py"])
            except HTTPError as e:
                print(json.loads(e.args[1]))

local_db=load_object("data.pickle")
if (local_db['status']==False):
    main = Auth(None)
    main.mainloop()
else:
    call(["python3","main.py"])