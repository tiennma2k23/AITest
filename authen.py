import pyrebase
import json
import tkinter as tk
from requests.exceptions import HTTPError

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
                print("User Created!")
                auth.send_email_verification(self.user['idToken'])
                self.destroy()
            except HTTPError as e:
                print(json.loads(e.args[1]))
        else:
            try:
                self.user = auth.sign_in_with_email_and_password(self.username.get(), self.password.get())
                print("Access Granted!")
                self.destroy()
            except HTTPError as e:
                print(json.loads(e.args[1]))

main = Auth(None)
main.mainloop()