import pyrebase
import json
import tkinter as tk
from requests.exceptions import HTTPError
from pathlib import Path
from Database_processing.User_db.get import *
from Utils.Sources.savedata_pickle import save_object
from Database_processing.User_db.insert import insert
CURRENT_WD = Path(__file__).parent.parent.parent
config=json.load(open(CURRENT_WD / 'adminAuth/firebase_config.json', 'r'))
firebase=pyrebase.initialize_app(config)
auth=firebase.auth()

class Auth():
    def __init__(self, *args):
        
        self._username = args[0].get() #Should have getter setter but
        if (len(args)>=2): self._password = args[1].get() #I'm too lazy
        if (len(args)>=3): self._name = args[2].get() #I'm too lazy
        self._args=args
        # _username=args[0].get()
    def UserAuth(self) -> bool:
        try:
            # self._password = self.args[1].get()
            f=find_user(self._username)
            if (f['status']):
                tmp=f['data']
                print(tmp)
                # email="abc@gmail.com"
                _email=tmp["email"]
                self.user = auth.sign_in_with_email_and_password(_email, self._password)
                save_object(tmp)
            print("Access Granted!")
            return True
        except HTTPError as e:
            print(json.loads(e.args[1]))
            return False

    def UserReg(self) -> bool:
        try: #Reg new user
            # self._password = self.args[1].get()
            self.user = auth.create_user_with_email_and_password(self._username, self._password)
            print("User Created!")
            auth.send_email_verification(self.user['idToken'])
            insert(self._name,self._username,self._password)
            return True
        except HTTPError as e:
            print(json.loads(e.args[1]))
            return False
    
    def Resend(self)-> bool:
        try:
            __=find_user(self._username)
            if (__['status']):
                auth.send_password_reset_email(self._username)
                return True
            return False
        except HTTPError as e:
            return False