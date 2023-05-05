from tkinter import *
from pathlib import Path
from Database_processing.Friends_db.ac_friend_rq import accept_fr
from Database_processing.Friends_db.deny_friend_rq import deny_fr
from Database_processing.Friends_db.get_request_fr import get_fr_rq_by_username
import UI.Homepage
import tkinter.messagebox as messagebox
import UI.Friends_list
import UI.Addfriend 
import UI.Rank
from Utils.Sources.getdata_pickle import load_object
from PIL import Image, ImageTk
import os



class requests(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        OUTPUT_PATH = Path(__file__).parent

        ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/friendslist")
        

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)
        _db=load_object("Appdata/userData/data.pickle")
        _username="abc"
        _friendReqs=[]
        if(_db['status']):
            _username=_db['data']['username']
            __rq=get_fr_rq_by_username(_username)
            for x in __rq:_friendReqs.append({'username':x,'rank':100})

        im = Image.open(relative_to_assets("image_3.png"))
        resized_im = im.resize((60, 60))
        self.profile_im = ImageTk.PhotoImage(resized_im)


        self.friendReqs = _friendReqs
        self.reqsnum = str(self.friendReqs.__len__())

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
        home_txt = self.canvas.create_text(
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
        # number of friends text
        self.canvas.create_text(
            142.0,
            89.0,
            anchor="nw",
            text="Requests -  " + self.reqsnum,
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

        # Friends List Text
        list_txt = self.canvas.create_text(
            13.0,
            189.0,
            anchor="nw",
            text="Friends List",
            fill="#FFFFFF",
            font=("Lato Regular", 18 * -1,)
        )
        hovertxt(list_txt)
        self.canvas.tag_bind(list_txt, '<ButtonPress-1>',
                             lambda _: self.onFriendslistClicked())

        # request_txt
        req_txt = self.canvas.create_text(
            22.0,
            268.0,
            anchor="nw",
            text="Requests",
            fill="#5F5F5F",
            font=("Lato Regular", 18 * -1, "underline")
        )
        # hovertxt(req_txt)
        # self.canvas.tag_bind(req_txt, '<ButtonPress-1>',
        #                      lambda _: print("req"))
        # add addfr txt
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

        self.Reqs = []  # List of friend frames
        for friend in self.friendReqs:
            self.addFriendFrame(friend['username'], friend['rank'], self.profile_im)

    def addFriendFrame(self, usr: str, rank: int, im):
        posy = int(126 + 68*len(self.Reqs))
        # create rec
        person = self.canvas.create_rectangle(
            214,
            posy,
            800,
            posy + 67,
            fill="#ADAAAA",
            outline="white",

        )
        # create username txt
        self.canvas.create_text(
            214,
            posy + 5,
            anchor="nw",
            text='Username: ' + usr,
            fill="#FFFFFF",
            font=("Lato Regular", 18 * -1, "bold")
        )
        self.canvas.create_image(
            126,
            posy + 4.5,
            anchor = "nw",
            image = self.profile_im
        )


        # create rank txt
        self.canvas.create_text(
            134,
            posy + 36,
            anchor="nw",
            text='Rank: '+str(rank),
            fill="#FFFFFF",
            font=("Lato Regular", 18 * -1)
        )
        # create button
        deny = Button(
            self.canvas,
            text="Deny",
            font=('Lato', 18 * -1),
            fg="#7F7F7F",
            bg="#DEDEDE",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: onDenyBtnClick(usr),
            relief="flat"
        )
        deny.place(
            x=662,
            y=posy + 19.0,
            width=122.0,
            height=27.98065185546875
        )
        accept = Button(
            self.canvas,
            text="Accept",
            font=('Lato', 18 * -1),
            fg="#E4E4E4",
            bg="#676767",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: onAcceptBtnClick(usr),
            relief="flat"
        )
        accept.place(
            x=504,
            y=posy + 19.0,
            width=122.0,
            height=27.98065185546875
        )

        # unfriend command

        def onAcceptBtnClick(usr):
            # do sth
            accept_fr(usr)
            print("Accept")
            accept.place_forget()
            deny.place_forget()
            self.canvas.create_text(
                584,
                posy + 21,
                anchor="nw",
                text="Request Accepted!",
                fill="#FFFFFF",
                font=("Lato Regular", 20 * -1, "bold")
            )

        def onDenyBtnClick(usr):
            # do sth
            deny_fr(usr)
            print("Deny")
            accept.place_forget()
            deny.place_forget()
            self.canvas.create_text(
                584,
                posy + 21,
                anchor="nw",
                text="Request Denied!",
                fill="#FFFFFF",
                font=("Lato Regular", 20 * -1, "bold")
            )



        self.Reqs.append(person)

    def onLogoutClicked(self):
        # Do sth with pickle
        os.remove("Appdata/userData/data.pickle")
        self.parent.parent.Authed.set(False)
        self.parent.parent.run()
        self.parent.destroy()

    def onHomepageClicked(self):
        # print('onFriends cliked')
        # self.friends.pack()
        self.parent.show_frame(UI.Homepage.homepage)
        # self.grid_forget()

    def onFriendslistClicked(self):
        print('onFriends cliked')
        # self.friends.pack()
        self.parent.show_frame(UI.Friends_list.Friendslist)
        # self.destroy()
    
    def onAddfrClick(self):
        UI.Addfriend.Addfriend(self).update()

    def onRankClick(self):
        self.parent.show_frame(UI.Rank.rank)

    def onProfileClick(self):
        self.parent.show_frame(UI.profile.profile)

