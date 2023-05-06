import tkinter as tk
# <<<<<<< Updated upstream
import tkinter.messagebox as MessageBox
# =======
from Database_processing.Friends_db.get_request_fr import get_fr_rq_by_username
from Database_processing.Friends_db.get_friends import get_fr_by_username
from Database_processing.User_db.get_img_profile import get_img_profile
from Database_processing.User_db.get_rank_user import get_rank_user
from Utils.Sources.getdata_pickle import load_object
from Database_processing.Friends_db.ac_friend_rq import accept_fr
from Database_processing.Friends_db.deny_friend_rq import deny_fr
# >>>>>>> Stashed changes
class Friends_frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
# <<<<<<< Updated upstream
#         # self.mainF = tk.Frame(self)
#         self.friendReqs = [
#             {'username': 'friendrq1', 'rank': 125},
#             {'username': 'friendrq2', 'rank': 69}
#         ]
# =======
        self.mainF = tk.Frame(self)
        _db=load_object("Appdata/userData/data.pickle")
        _username="abc"
        _friendReqs=[]
        _friend=[]
        if(_db['status']):
            _username=_db['data']['username']
            __rq=get_fr_rq_by_username(_username)
            __fr=get_fr_by_username(_username)
            for x in __rq:_friendReqs.append({'username':x,'rank':get_rank_user(x),'img_profile':get_img_profile(x)})
            for x in __fr:_friend.append({'username':x,'rank':get_rank_user(x),'img_profile':get_img_profile(x)})
        
        print ("Da chay file Friend.py",_friendReqs)
        self.friendReqs = _friendReqs
# >>>>>>> Stashed changes
        
        self.friends = _friend

        self.listFriendFr = tk.LabelFrame(
            self,
            bg="#fff",
            text='Friends'
        ) #container

        self.listFriendReqFr = tk.LabelFrame(
            self,
            bg="#fff",
            text='Friends Req'
        ) #container

        self.friendFrs = [] #List of friend frames
        self.friendReqFrs = [] #List of friendReq frames
        for friend in self.friends:
            self.addFriendFrame(friend['username'], friend['rank'])
        for friendReq in self.friendReqs:
            self.addFriendReqFrame(friendReq['username'], friendReq['rank'])
        self.listFriendFr.pack()
        self.listFriendReqFr.pack()
        # self.mainF.pack()


    def addFriendFrame(self, usr: str, rank: int):

        
        def onaddfriendBtnClick():
            if (MessageBox.askyesno('Unfr', 'U sure?')):
                print('Addfr succ')
                addFriendBtn.grid_forget()
                unfriendBtn.grid(row=0, column=1, rowspan=2)
            else:
                print('Addfr canceled')

        def onunfriendBtnClick():
            if (MessageBox.askyesno('Unfr', 'U sure?')):
                print('Unfr succ')
                unfriendBtn.grid_forget()
                addFriendBtn.grid(row=0, column=1, rowspan=2)
            else:
                print('Unfr canceled')
        person = tk.Frame(self.listFriendFr,
                          padx=10, pady=10,
                          borderwidth=2,
                          relief='sunken')
        personUsername = tk.Label(person,
                           text='Username: '+usr)
        personUsername.grid(row=0)
        personRank = tk.Label(person,
                              text='Rank: '+str(rank))
        personRank.grid(row=1)

        unfriendBtn = tk.Button(person, text='Unfr',
                                command=lambda: onunfriendBtnClick())
        unfriendBtn.grid(row=0, column=1, rowspan=2)
        addFriendBtn = tk.Button(person, text='Add fr',
                                command=lambda: onaddfriendBtnClick())
        
        person.grid(row=len(self.friendFrs))
        self.friendFrs.append(person)

    def addFriendReqFrame(self, usr: str, rank: int):
        person = tk.Frame(self.listFriendReqFr,
                          padx=10, pady=10,
                          borderwidth=2,
                          relief='sunken')
        
        personUsername = tk.Label(person,
                           text='Username: '+usr)
        personUsername.grid(row=0)
        personRank = tk.Label(person,
                              text='Rank: '+str(rank))
        personRank.grid(row=1)

        acpBtn = tk.Button(person, 
                           text='Accept',
                           command=lambda:accept_fr(usr),
                            # method=self.addFriendFrame(usr,100)
                           )
        denBtn = tk.Button(person, 
                           text='Deny',
                           command=lambda: deny_fr(usr))
        acpBtn.grid(row=0, column=1)
        denBtn.grid(row=1, column=1)
        person.grid(row=len(self.friendReqFrs))
        self.friendReqFrs.append(person)

