import pyrebase
import json
import tkinter as tk
from requests.exceptions import HTTPError
from pathlib import Path

CURRENT_WD = Path(__file__).parent

config=json.load(open(CURRENT_WD / 'firebase_config.json', 'r'))
firebase=pyrebase.initialize_app(config)
auth=firebase.auth()

class Auth():
    def __init__(self, *args):
        self._username = args[0].get() #Should have getter setter but
        self._password = args[1].get() #I'm too lazy

    def UserAuth(self) -> bool:
        try:
            self.user = auth.sign_in_with_email_and_password(self._username, self._password)
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
