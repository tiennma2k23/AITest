import pyrebase
import json
import tkinter as tk
from requests.exceptions import HTTPError
from pathlib import Path
from Database_processing.User_db.get import *
from Utils.Sources.savedata_pickle import save_object
CURRENT_WD = Path(__file__).parent.parent.parent
config=json.load(open(CURRENT_WD / 'adminAuth/firebase_config.json', 'r'))
firebase=pyrebase.initialize_app(config)
auth=firebase.auth()

class Auth():
    def __init__(self, *args):
        
        self._username = args[0].get() #Should have getter setter but
        self._password = args[1].get() #I'm too lazy
        # _username=args[0].get()
    def UserAuth(self) -> bool:
        try:
            
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
            
            self.user = auth.create_user_with_email_and_password(self._username, self._password)
            print("User Created!")
            auth.send_email_verification(self.user['idToken'])
            return True
        except HTTPError as e:
            print(json.loads(e.args[1]))
            return False
