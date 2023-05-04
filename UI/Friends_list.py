from tkinter import *
from pathlib import Path
from Database_processing.Friends_db.delete_fr import delete_fr
from Database_processing.Friends_db.get_friends import get_fr_by_username
from Database_processing.Friends_db.update_fr import update_fr_user
import UI.Homepage
import tkinter.messagebox as messagebox
import UI.FriendsReq 
import UI.Addfriend
import UI.Rank
import UI.profile
from Utils.Sources.getdata_pickle import load_object


class Friendslist(Frame):
    
    

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        OUTPUT_PATH = Path(__file__).parent


        ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/friendslist")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)
        
        
        _friend=[]
        _db=load_object("Appdata/userData/data.pickle")
        _username="abc"
        if(_db['status']):
            _username=_db['data']['username']
            __fr=get_fr_by_username(_username)
            for x in __fr:_friend.append({'username':x,'rank':100})

        self.friends = _friend
        self.friendsnum = str(self.friends.__len__())


        self.canvas = Canvas(
            self,
            bg="#FFFF0F",
            height=480,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.pack()

        def hovertxt(sometxt):
            self.canvas.tag_bind(sometxt, '<Enter>', lambda _: self.canvas.itemconfig(
                sometxt, fill="#CCCCCC"))
            self.canvas.tag_bind(sometxt, '<Leave>', lambda _: self.canvas.itemconfig(
                sometxt, fill="#FFFFFF"))
            self.canvas.tag_bind(sometxt, '<ButtonPress-1>',
                             lambda _: print("profile"))

        
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            400.0,
            240.0,
            image=self.image_image_1
        )

        # create rectangle
        self.canvas.create_rectangle(
            0.0,
            0.0,
            800.0,
            78.0,
            fill="#ADAAAA",
            outline="")
        # home text
        home_txt=self.canvas.create_text(
            287.0,
            27.0,
            anchor="nw",
            text="Home",
            fill="#FFFFFF",
            font=("Lato Regular", 20 * -1)
        )
        hovertxt(home_txt)
        self.canvas.tag_bind(home_txt, '<ButtonPress-1>',
                             lambda _: self.onHomepageClicked())
        # friend text
        friends_txt = self.canvas.create_text(
            370.0,
            27.0,
            anchor="nw",
            text="Friends",
            fill="#5F5F5F",
            font=("Lato Regular", 20 * -1, "underline")
        )
        # self.canvas.tag_bind(friends_txt, '<Enter>', lambda _: self.canvas.itemconfig(
        #     friends_txt, fill="#CCCCCC"))
        # self.canvas.tag_bind(friends_txt, '<Leave>', lambda _: self.canvas.itemconfig(
        #     friends_txt, fill="#FFFFFF"))
        # self.canvas.tag_bind(friends_txt, '<ButtonPress-1>',
        #                      lambda _: self.onFriendsClicked())

        # profile text
        profile_txt = self.canvas.create_text(
            637.0,
            27.0,
            anchor="nw",
            text="Profile",
            fill="#FFFFFF",
            font=("Lato Regular", 20 * -1)
        )
        hovertxt(profile_txt)
        self.canvas.tag_bind(profile_txt, '<ButtonPress-1>',
                             lambda _: self.onProfileClick())

        # Logout text
        logout_txt = self.canvas.create_text(
            723.0,
            27.0,
            anchor="nw",
            text="Log out",
            fill="#FFFFFF",
            font=("Lato Regular", 20 * -1)
        )
        hovertxt(logout_txt)
        self.canvas.tag_bind(logout_txt, '<ButtonPress-1>',
                             lambda _: self.onLogoutClicked())

        # ranking text
        rank_txt = self.canvas.create_text(
            538.0,
            27.0,
            anchor="nw",
            text="Ranking",
            fill="#FFFFFF",
            font=("Lato Regular", 20 * -1)
        )
        hovertxt(rank_txt)
        self.canvas.tag_bind(rank_txt, '<ButtonPress-1>',
                             lambda _: self.onRankClick())

        # shop text
        shop_txt = self.canvas.create_text(
            464.0,
            27.0,
            anchor="nw",
            text="Shop",
            fill="#FFFFFF",
            font=("Lato Regular", 20 * -1)
        )
        hovertxt(shop_txt)
        self.canvas.tag_bind(shop_txt, '<ButtonPress-1>',
                             lambda _: print("Shop"))
        #number of friends text
        self.canvas.create_text(
            142.0,
            89.0,
            anchor="nw",
            text="All Friends -  " + self.friendsnum,
            fill="#807B7B",
            font=("Lato", 18 * -1, "bold")
        )


        self.canvas.create_rectangle(
            0.0,
            79.0,
            117.0,
            480.0,
            fill="#B5B5B5",
            outline="")
        
        #Friends List Text
        list_txt = self.canvas.create_text(
            13.0,
            189.0,
            anchor="nw",
            text="Friends List",
            fill="#5F5F5F",
            font=("Lato Regular", 18 * -1, "underline")
        )
        #hovertxt(list_txt)
        
        #request_txt
        req_txt = self.canvas.create_text(
            22.0,
            268.0,
            anchor="nw",
            text="Requests",
            fill="#FFFFFF",
            font=("Lato Regular", 18 * -1)
        )
        hovertxt(req_txt)
        self.canvas.tag_bind(req_txt, '<ButtonPress-1>',
                             lambda _: self.onFriendsReqClicked())
        #add addfr txt
        addfr_txt = self.canvas.create_text(
            16.0,
            347.0,
            anchor="nw",
            text="Add Friend",
            fill="#FFFFFF",
            font=("Lato Regular", 18 * -1)
        )
        hovertxt(addfr_txt)
        self.canvas.tag_bind(addfr_txt, '<ButtonPress-1>',
                             lambda _: self.onAddfrClick())


        
        self.friendFrs = []  # List of friend frames
        self.unfr = []  # List of friendReq frames
        for friend in self.friends:
            self.addFriendFrame(friend['username'], friend['rank'])
        
        
    def addFriendFrame(self, usr: str, rank: int):
        posy = int(126 + 68*len(self.friendFrs))
        #create rec
        person = self.canvas.create_rectangle(
            117, 
            posy,
            800,
            posy + 67,
            fill="#ADAAAA",
            outline="white",

        )
        #create username txt
        self.canvas.create_text (
            134,
            posy + 5,
            anchor="nw",
            text='Username: '+ usr,
            fill="#FFFFFF",
            font=("Lato Regular", 18 * -1, "bold")
        )
        #create rank txt
        self.canvas.create_text(
            134,
            posy + 36,
            anchor="nw",
            text='Rank: '+str(rank),
            fill="#FFFFFF",
            font=("Lato Regular", 18 * -1)
        )
        #create button
        unfr = Button(
            self.canvas,
            text="Unfriend",
            font=('Lato', 18 * -1),
            fg = "#7F7F7F",
            bg = "#DEDEDE",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: onunfriendBtnClick(usr),
            relief="flat"
        )
        unfr.place(
            x=662,
            y=posy + 19.0,
            width=122.0,
            height=27.98065185546875
        )
        addButton = Button(
            self.canvas,
            text="Add friend",
            font=('Lato', 18 * -1),
            fg="#E4E4E4",
            bg="#676767",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: onaddfriendBtnClick(),
            relief="flat"
        )

        #unfriend command

        def onaddfriendBtnClick(usr):
            #do sth
            
            print("addfr succ")
            addButton.place_forget()
            self.canvas.create_text(
                658,
                posy + 21,
                anchor="nw",
                text="Request Sent",
                fill="#FFFFFF",
                font=("Lato Regular", 20 * -1, "bold")
            )

        def onunfriendBtnClick(usr):
            if (messagebox.askyesno('Unfriend', 'Are you sure to unfriend with ' + usr + '?')):
                print('Unfr succ')
                delete_fr(usr)
                unfr.place_forget()
                addButton.place(
                    x=662,
                    y=posy + 19.0,
                    width=122.0,
                    height=27.98065185546875
                )
            else:
                print('Unfr canceled')
        
        self.friendFrs.append(person)


    def onLogoutClicked(self):
        # Do sth with pickle
        # os.remove("Appdata/userData/data.pickle")
        self.parent.parent.Authed.set(False)
        self.parent.parent.run()
        self.parent.destroy()

    def onHomepageClicked(self):
        # print('onFriends cliked')
        # self.friends.pack()
        self.parent.show_frame(UI.Homepage.homepage)
        # self.grid_forget()
    
    def onFriendsReqClicked(self):
        # print('onFriends cliked')
        # self.friends.pack()
        self.parent.show_frame(UI.FriendsReq.requests)
        # self.grid_forget()
    
    def onAddfrClick(self):
        UI.Addfriend.Addfriend(self).update()
    
    def onRankClick(self):
        self.parent.show_frame(UI.Rank.rank)

    def onProfileClick(self):
        self.parent.show_frame(UI.profile.profile)


        
