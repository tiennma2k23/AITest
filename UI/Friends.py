import tkinter as tk

class Friends_frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.mainF = tk.Frame()
        
        self.friendReqs = [
            {'username': 'friendrq1', 'rank': 125},
            {'username': 'friendrq2', 'rank': 69}
        ]

        self.friends = [
            {'username': 'friend1', 'rank': 123},
            {'username': 'friend2', 'rank': 15},
            {'username': 'friend3', 'rank': 727}
        ] #{ {'username': <rank>} }

        self.listFriendFr = tk.LabelFrame(
            self.mainF,
            bg="#fff",
            text='Friends'
        ) #container

        self.listFriendReqFr = tk.LabelFrame(
            self.mainF,
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


    def addFriendFrame(self, usr: str, rank: int):
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
                           command=lambda: print('Acp clicked'))
        denBtn = tk.Button(person, 
                           text='Deny',
                           command=lambda: print('Den clicked'))
        acpBtn.grid(row=0, column=1)
        denBtn.grid(row=1, column=1)
        person.grid(row=len(self.friendReqFrs))
        self.friendReqFrs.append(person)

