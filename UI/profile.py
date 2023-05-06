import base64
import os
from tkinter import *
from pathlib import Path
from Database_processing.User_db.get_point_user import get_point_username
from Database_processing.User_db.get_rank_user import get_rank_user
from Database_processing.User_db.update_img_profile_user import update_img_profile_user
import UI.Homepage
import tkinter.messagebox as messagebox
import tkinter.filedialog as dialog
import UI.Friends_list
import UI.Rank
import UI.resendpass
# from PIL import Image
from PIL import Image, ImageTk
import UI.Shop
from Utils.Sources.getdata_pickle import load_object
from img_processing.base64_img import base64_img
from img_processing.img_base64 import img_base64

OUTPUT_PATH = Path(__file__).parent

ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/profile")

class profile(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.userDataFieldID = {
            'username': 0,
            'email': 0,
            'rank': 0,
            'points': 0,
            'streak': 0,
            'pfp': 0
        }
        self.loadData()

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

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
            fill="#5F5F5F",
            font=("Lato Regular", 20 * -1, "underline")
        )
        # hovertxt(profile_txt)
        # self.canvas.tag_bind(profile_txt, '<ButtonPress-1>',
        #                      lambda _: self.onRankClick())

        #Logout text
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
                             lambda _: self.onShopClick())

        #
        ava_txt = self.canvas.create_text(
            65.0,
            316.0,
            anchor="nw",
            text="Change Avatar",
            fill="#7C7C7C",
            font=("Lato Regular", 18 * -1, "underline")
        )
        self.canvas.tag_bind(ava_txt, '<Enter>', lambda _: self.canvas.itemconfig(
                ava_txt, fill="#CCCCCC"))
        self.canvas.tag_bind(ava_txt, '<Leave>', lambda _: self.canvas.itemconfig(
                ava_txt, fill="#7C7C7F"))
        self.canvas.tag_bind(ava_txt, '<ButtonPress-1>',
                             lambda _: onAvaClick())
        #change img func
        def onAvaClick():
            filename = dialog.askopenfilename()
            im = Image.open(filename)
            resized_im = im.resize((161, 161))
            rr_im=resized_im.convert('RGB')
            self.new_im = ImageTk.PhotoImage(resized_im)
            self.canvas.itemconfig(self.userDataFieldID['pfp'], image = self.new_im)
            rr_im.save('Appdata/userData/usr_img.jpg')
            update_img_profile_user(self.username,img_base64('Appdata/userData/usr_img.jpg'))
            # my_string = base64.b64encode(self.new_im)
            # print(my_string)
            


        #profile img
        # base64_img()
        try:
            self.avaimg = ImageTk.PhotoImage(Image.open('./Appdata/userData/usr_img.jpg')) #có thể là file khác nếu db đã có r
        except:
            self.avaimg = ImageTk.PhotoImage(Image.open('./Appdata/userData/default.jpg'))

        self.userDataFieldID['pfp'] = self.canvas.create_image(
                122.0,
                222.0,
                image=self.avaimg
            )
        

        #main info
        self.userDataFieldID['username'] = self.canvas.create_text(
            294.0,
            129.0,
            anchor="nw",
            text="Username: " + self.username,
            fill="#7C7C7C",
            font=("Lato", 20 * -1, "bold")
        )

        self.userDataFieldID['email'] = self.canvas.create_text(
            294.0,
            179.0,
            anchor="nw",
            text="E-mail: " + self.email,
            fill="#7C7C7C",
            font=("Lato", 20 * -1, "bold")
        )
        # rank 
        self.userDataFieldID['rank'] = self.canvas.create_text(
            293.0,
            228.0,
            anchor="nw",
            text="Ranks: " + str(self.rank),
            fill="#7C7C7C",
            font=("Lato ", 20 * -1, "bold")
        )

        self.userDataFieldID['points'] = self.canvas.create_text(
            294.0,
            277.0,
            anchor="nw",
            text="Points: " + str(self.points),
            fill="#7C7C7C",
            font=("Lato", 20 * -1, "bold")
        )

        self.userDataFieldID['streak'] = self.canvas.create_text(
            294.0,
            327.0,
            anchor="nw",
            text="Streak: " + str(self.streak),
            fill="#7C7C7C",
            font=("Lato", 20 * -1, "bold")
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = self.canvas.create_image(
            655,
            87,
            anchor = "nw",
            image = self.button_image_1
        )
        self.canvas.tag_bind(button_1, '<ButtonPress-1>',
                             lambda _: self.onResendClick())
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = self.canvas.create_image(
            487,
            87,
            anchor = "nw",
            image = self.button_image_2
        )
        
    def loadData(self):
        __=load_object("Appdata/userData/data.pickle")
        if (__['status']==True):
            self.username = __['data']['username']
            self.streak = __['data']['login_days']
            self.email = __['data']['email']
            self.rank = get_rank_user(__['data']['username'])
            self.points = get_point_username(__['data']['username'])
        else:
            self.username = "###"
            self.streak = 0
            self.email = "###"
            self.rank = -9999
            self.points = -9999
    #     self.updateData()


    # def updateData(self):
    #     self.canvas.itemconfig(self.userDataFieldID['username'], text='Username: '+self.username)
    #     self.canvas.itemconfig(self.userDataFieldID['email'], text='Email: '+self.email)
    #     self.canvas.itemconfig(self.userDataFieldID['rank'], text='Rank: '+self.rank)
    #     self.canvas.itemconfig(self.userDataFieldID['points'], text='Points: '+self.points)
    #     self.canvas.itemconfig(self.userDataFieldID['streak'], text='Streak: '+self.streak)
    #     self.canvas.itemconfig(self.userDataFieldID['pfp'], image=self.avaimg)
    
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
      
    def onRankClick(self):
        self.parent.show_frame(UI.Rank.rank)

    def onResendClick(self):
        UI.resendpass.resendpass(self).update()

    def onShopClick(self):
        self.parent.show_frame(UI.Shop.shop)
    

    