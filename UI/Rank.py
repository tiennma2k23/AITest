from tkinter import *
from pathlib import Path
from Database_processing.User_db.get_img_profile import get_img_profile
from Database_processing.User_db.get_point_data import get_point_data
import UI.Homepage
import tkinter.messagebox as messagebox
import UI.Friends_list
import UI.profile
import os
import UI.Shop
from PIL import Image, ImageTk

from img_processing.base64_img import base64_img_with_base64url

OUTPUT_PATH = Path(__file__).parent

ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/friendslist")

class rank(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.loadData()

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        # im = Image.open(relative_to_assets("image_3.png"))
        # resized_im = im.resize((40, 40))
        # self.profile_im = ImageTk.PhotoImage(resized_im)

        self.users = get_point_data()

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
            fill="#FFFFFF",
            font=("Lato Regular", 20 * -1)
        )
        hovertxt(friends_txt)
        self.canvas.tag_bind(friends_txt, '<ButtonPress-1>',
                             lambda _: self.onFriendsClicked())

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
            fill="#5F5F5F",
            font=("Lato Regular", 20 * -1,"underline")
        )
        # hovertxt(rank_txt)
        # self.canvas.tag_bind(rank_txt, '<ButtonPress-1>',
        #                      lambda _: print("ranking"))

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
                             lambda _: self.onShopClick())

        # rank text
        self.canvas.create_text(
            30,
            91,
            anchor="nw",
            text="#",
            fill="#7C7C7C",
            font=("Lato", 18 * -1, "bold")
        )
        #Usrname txt
        self.canvas.create_text(
            88,
            91,
            anchor="nw",
            text="Username",
            fill="#7C7C7C",
            font=("Lato", 18 * -1, "bold")
        )
        #Points txt
        self.canvas.create_text(
            679,
            91,
            anchor="nw",
            text="Points",
            fill="#7C7C7C",
            font=("Lato", 18 * -1, "bold")
        )

        #create line
        self.canvas.create_line(
            0,
            127,
            800,
            127,
            width=2,
            fill = "#595959",
        )
        
        self.usr = []  # List of friend frames
        for x in range (len(self.users)):
            users=self.users[x]
            self.addUser(users['username'], users['rank'], users['point'],x)

    def loadData(self):
        pass
    
    def addUser(self, usr: str, ranks: int, pts: int,index:int):
        img_url=get_img_profile(usr)
        # print(usr)
        # __url=str(index)
        base64_img_with_base64url(img_url,'fr_img'+str(index)+'.jpg')
        im = Image.open('./Appdata/userData/fr_img'+str(index)+'.jpg')
        
        resized_im = im.resize((40, 40))
        self.profile_im = ImageTk.PhotoImage(resized_im)
        posy = int(127 + 49*len(self.usr))

        #rank
        person = self.canvas.create_text(
            31,
            posy + 16,
            anchor="nw",
            text=str(len(self.usr) + 1),
            fill="#7C7C7C",
            font=("Lato", 18 * -1)
        )
        #name
        self.canvas.create_text(
            140,
            posy + 16,
            anchor="nw",
            text=usr,
            fill="#7C7C7C",
            font=("Lato", 18 * -1)
        )
        #points
        self.canvas.create_text(
            679,
            posy + 16,
            anchor="nw",
            text=str(pts),
            fill="#7C7C7C",
            font=("Lato", 18 * -1)
        )
        # create line
        self.canvas.create_line(
            0,
            posy + 49,
            800,
            posy + 49,
            width=0.5,
            fill="#B5B5B5",
        )
        # create img
        self.canvas.create_image(
            88,
            posy + 4,
            anchor = "nw",
            image = self.profile_im
        )
        # os.remove('Appdata/userData/fr_img.jpg')
        self.usr.append(person)

    def onLogoutClicked(self):
        # Do sth with pickle
        os.remove("Appdata/userData/data.pickle")
        os.remove("Appdata/userData/usr_img.jpg")
        self.parent.parent.Authed.set(False)
        self.parent.parent.run()
        self.parent.destroy()

    def onHomepageClicked(self):
        # print('onFriends cliked')
        # self.friends.pack()
        self.parent.show_frame(UI.Homepage.homepage)
        # self.grid_forget()

    def onFriendsClicked(self):
        print('onFriends cliked')
        # self.friends.pack()
        self.parent.show_frame(UI.Friends_list.Friendslist)
        # self.destroy()
    
    def onProfileClick(self):
        self.parent.show_frame(UI.profile.profile)
    
    def onShopClick(self):
        self.parent.show_frame(UI.Shop.shop)

