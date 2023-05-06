from tkinter import *
from pathlib import Path
from Database_processing.User_db.get_point_data import get_point_data
import tkinter.messagebox as messagebox
from Database_processing.User_db.get_point_user import get_point_username
import UI.Homepage
import tkinter.messagebox as messagebox
import UI.Friends_list
import UI.profile
import UI.Rank
import os
from PIL import Image, ImageTk

from Utils.Sources.getdata_pickle import load_object

OUTPUT_PATH = Path(__file__).parent

ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/shop")

class shop(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.loadData()
        self.img_shop=[]
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        
        __=load_object('Appdata/userData/data.pickle')
        __username=""
        if (__['status']) :__username=__['data']['username']
        self.points = get_point_username(__username)
        self.shops = [
            {'image': 'cali.png', 'name': 'California Fitness', 'district': 'Ha Dong', 'city': 'Ha Noi', 'distance': '300 m', 'value': 15, 'points': 10},
            {'image': 'citygym.jpeg', 'name': 'CITYGYM', 'district': 'Le Loi', 'city': 'Ho Chi Minh', 'distance': '1700 km', 'value': 40, 'points': 20}
        ]


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
            fill="#FFFFFF",
            font=("Lato Regular", 20 * -1,)
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
            fill="#5F5F5F",
            font=("Lato Regular", 20 * -1, "underline")
        )
        # hovertxt(shop_txt)
        # self.canvas.tag_bind(shop_txt, '<ButtonPress-1>',
        #                      lambda _: print("Shop"))

        #create line
        self.canvas.create_line(
            0,
            127,
            800,
            127,
            width=2,
            fill = "#595959",
        )
        #Name txt
        self.canvas.create_text(
            64,
            94,
            anchor="nw",
            text="Name",
            fill="#7C7C7C",
            font=("Lato", 16 * -1, "bold")
        )
        #Address txt
        self.canvas.create_text(
            208,
            94,
            anchor="nw",
            text="Address",
            fill="#7C7C7C",
            font=("Lato", 16 * -1, "bold")
        )
        #Value txt
        self.canvas.create_text(
            490,
            94,
            anchor="nw",
            text="Value",
            fill="#7C7C7C",
            font=("Lato", 16 * -1, "bold")
        )
        #Points txt
        self.canvas.create_text(
            627,
            94,
            anchor="nw",
            text="Points",
            fill="#7C7C7C",
            font=("Lato", 16 * -1, "bold")
        )
        #Current point txt
        self.curpoint = self.canvas.create_text(
            627.0,
            448.0,
            anchor="nw",
            text="Current Point - " + str(self.points),
            fill="#7C7C7C",
            font=("Lato", 18 * -1,"bold")
        )       

        self.curshops = []  # List of friend frames
        for x in range (len(self.shops)):
            users=self.shops[x]
            self.addShop(users['name'], users['district'], users['city'], users['distance'], users['value'], users['points'],users['image'],x)

    def loadData(self):
        pass
    
    def addShop(self, name: str, distr: str, cit: str, dist: str, val: int, pts: int,img_url:str,index:int):
        posy = int(127 + 49*len(self.curshops))
        #name
        cur = self.canvas.create_text(
            64,
            posy + 16,
            anchor="nw",
            text= name,
            fill="#7C7C7C",
            font=("Lato", 16 * -1)
        )
        self.canvas.tag_bind(cur, '<Enter>', lambda _: self.canvas.itemconfig(
                cur, fill="#BBBBBB"))
        self.canvas.tag_bind(cur, '<Leave>', lambda _: self.canvas.itemconfig(
                cur, fill="#7C7C7C"))
        # self.canvas.tag_bind(cur, '<ButtonPress-1>', lambda _: self.canvas.itemconfig(
        #         cur, fill="#7C7C7C"))
        
        #address
        self.canvas.create_text(
            208,
            posy + 3,
            anchor="nw",
            text=distr + ', ' + cit,
            fill="#7C7C7C",
            font=("Lato", 16 * -1)
        )
        #distance
        self.canvas.create_text(
            208,
            posy + 26,
            anchor="nw",
            text='Distance: ' + str(dist),
            fill="#7C7C7C",
            font=("Lato", 12 * -1, "italic")
        )
        #value
        self.canvas.create_text(
            490,
            posy + 16,
            anchor="nw",
            text=str(val) + '%',
            fill="#7C7C7C",
            font=("Lato", 16 * -1)
        )
        #points
        self.canvas.create_text(
            627,
            posy + 16,
            anchor="nw",
            text=str(pts),
            fill="#7C7C7C",
            font=("Lato", 16 * -1)
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
        strr='UI/assets/shop/'+img_url
        im = Image.open(strr)
        resized_im = im.resize((40, 40))
        self.img_shop.append(ImageTk.PhotoImage(resized_im))
        self.canvas.create_image (
            
            10,
            posy + 4,
            anchor = "nw",
            image = self.img_shop[index]
        )
        #button
        exch = Button(
            self.canvas,
            text="Exchange",
            font=('Lato', 18 * -1),
            fg="#E4E4E4",
            bg="#676767",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: onexchBtnClick(),
            relief="flat"
        )
        exch.place(
            x=705,
            y=posy + 12,
            width=95,
            height=27.98
        )
        exch.bind(
            '<Enter>', lambda e: exch.configure(bg="#B5B5B5"))
        exch.bind(
            '<Leave>', lambda e: exch.configure(bg="#676767"))

        def onexchBtnClick():
            if self.points < pts: messagebox.showerror('So poor', "You do not have enough points")
            else:
                if (messagebox.askyesno('Purchase offer', 'Are you sure to purchase this offer?')):
                    self.points -= pts
                    self.canvas.itemconfig(self.curpoint, text="Current Point - " + str(self.points))
                    exch.place_forget()
                    self.canvas.create_text( #purchased text
                        705,
                        posy + 16,
                        anchor="nw",
                        text="Purchased",
                        fill="#7C7C7C",
                        font=("Lato", 18 * -1, "bold")
                    )                    

                

        self.curshops.append(cur)

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

    def onRankClick(self):
        self.parent.show_frame(UI.Rank.rank)

    