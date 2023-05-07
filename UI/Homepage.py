from tkinter import *
import UI.Friends
import UI.Friends_list
import UI.chooseEx
import UI.Rank
import UI.profile
import UI.Shop
import tkinter.messagebox as messagebox
from Utils.Sources.getdata_pickle import load_object
from Utils.Sources.savedata_pickle import save_object
from Database_processing.User_db.update_active import *
from Database_processing.User_db.ispremium import *
from pathlib import Path
import os
# Explicit imports to satisfy Flake8
# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent

ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/homepage")
def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

class homepage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.username = ""
        self.ispremium = False
        self.loadData()

        #create BG
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


        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            400.0,
            240.0,
            image=self.image_image_1
        )

        #create rectangle
        self.canvas.create_rectangle(
            0.0,
            0.0,
            800.0,
            78.0,
            fill="#ADAAAA",
            outline="")

        self.logo_img = PhotoImage(file = relative_to_assets("logo.png"))
        self.logo = self.canvas.create_image(
            24,
            23,
            image=self.logo_img,
            anchor="nw",
        )

        #home text
        self.canvas.create_text(
            287.0,
            27.0,
            anchor="nw",
            text="Home",
            fill="#5F5F5F",
            font=("Lato Regular", 20 * -1, "underline")
        )
        #friend text
        friends_txt=self.canvas.create_text(
            370.0,
            27.0,
            anchor="nw",
            text="Friends",
            fill="#FFFFFF",
            font=("Lato Regular", 20 * -1)
        )
        self.canvas.tag_bind(friends_txt, '<Enter>', lambda _: self.canvas.itemconfig(
            friends_txt, fill="#CCCCCC"))
        self.canvas.tag_bind(friends_txt, '<Leave>', lambda _: self.canvas.itemconfig(
            friends_txt, fill="#FFFFFF"))
        self.canvas.tag_bind(friends_txt, '<ButtonPress-1>',
                        lambda _: self.onFriendsClicked())
        
        #profile text
        profile_txt = self.canvas.create_text(
            637.0,
            27.0,
            anchor="nw",
            text="Profile",
            fill="#FFFFFF",
            font=("Lato Regular", 20 * -1)
        )
        self.canvas.tag_bind(profile_txt, '<Enter>', lambda _: self.canvas.itemconfig(
            profile_txt, fill="#CCCCCC"))
        self.canvas.tag_bind(profile_txt, '<Leave>', lambda _: self.canvas.itemconfig(
            profile_txt, fill="#FFFFFF"))
        self.canvas.tag_bind(profile_txt, '<ButtonPress-1>',
                        lambda _: self.onProfileClick())
        
        #Logout text
        logout_txt = self.canvas.create_text(
            723.0,
            27.0,
            anchor="nw",
            text="Log out",
            fill="#FFFFFF",
            font=("Lato Regular", 20 * -1)
        )
        self.canvas.tag_bind(logout_txt, '<Enter>', lambda _: self.canvas.itemconfig(
            logout_txt, fill="#CCCCCC"))
        self.canvas.tag_bind(logout_txt, '<Leave>', lambda _: self.canvas.itemconfig(
            logout_txt, fill="#FFFFFF"))
        self.canvas.tag_bind(logout_txt, '<ButtonPress-1>',
                             lambda _: self.onLogoutClicked())

        #ranking text
        rank_txt = self.canvas.create_text(
            538.0,
            27.0,
            anchor="nw",
            text="Ranking",
            fill="#FFFFFF",
            font=("Lato Regular", 20 * -1)
        )
        self.canvas.tag_bind(rank_txt, '<Enter>', lambda _: self.canvas.itemconfig(
            rank_txt, fill="#CCCCCC"))
        self.canvas.tag_bind(rank_txt, '<Leave>', lambda _: self.canvas.itemconfig(
            rank_txt, fill="#FFFFFF"))
        self.canvas.tag_bind(rank_txt, '<ButtonPress-1>',
                        lambda _: self.onRankClick())

        #shop text
        shop_txt = self.canvas.create_text(
            464.0,
            27.0,
            anchor="nw",
            text="Shop",
            fill="#FFFFFF",
            font=("Lato Regular", 20 * -1)
        )
        self.canvas.tag_bind(shop_txt, '<Enter>', lambda _: self.canvas.itemconfig(
            shop_txt, fill="#CCCCCC"))
        self.canvas.tag_bind(shop_txt, '<Leave>', lambda _: self.canvas.itemconfig(
            shop_txt, fill="#FFFFFF"))
        self.canvas.tag_bind(shop_txt, '<ButtonPress-1>',
                        lambda _: self.onShopClick())
        
        #create buttons
        #button1
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = self.canvas.create_image(
            545, 
            282,
            image=self.button_image_1,
            anchor = "nw",
        )
        self.canvas.tag_bind(self.button_1, '<ButtonPress-1>',
                        lambda _: self.onpullupclick())
        #button2
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = self.canvas.create_image(
            240,
            181,
            image=self.button_image_2,
            anchor="nw",
        )
        self.canvas.tag_bind(button_2, '<ButtonPress-1>',
                        lambda _: UI.chooseEx.chooseEx(self, 'push-up').update())
                    
        #button3
        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = self.canvas.create_image(
            440,
            155,
            image=self.button_image_3,
            anchor="nw",
        )
        self.canvas.tag_bind(button_3, '<ButtonPress-1>',
                        lambda _: UI.chooseEx.chooseEx(self, 'squat').update())
        #button4
        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = self.canvas.create_image(
            42,
            153,
            image=self.button_image_4,
            anchor="nw",
        )
        self.canvas.tag_bind(button_4, '<ButtonPress-1>',
                        lambda _: UI.chooseEx.chooseEx(self, 'sit-up').update())
        #button5
        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = self.canvas.create_image(
            125,
            287,
            image=self.button_image_5,
            anchor="nw",
        )
        self.canvas.tag_bind(button_5, '<ButtonPress-1>',
                        lambda _: UI.chooseEx.chooseEx(self, 'walk').update())

        #plank
        self.img_plank = PhotoImage(
            file=relative_to_assets("plank.png"))
        self.button_plank = self.canvas.create_image(
            648,
            143,
            image=self.img_plank,
            anchor="nw",
        )
        self.canvas.tag_bind(self.button_plank, '<ButtonPress-1>',
                        lambda _: UI.chooseEx.chooseEx(self, 'push-up').update())
        
        #lunges
        self.img_lunges = PhotoImage(
            file=relative_to_assets("lunges.png"))
        self.button_lunges = self.canvas.create_image(
            335,
            296,
            image=self.img_lunges,
            anchor="nw",
        )
        self.canvas.tag_bind(self.button_lunges, '<ButtonPress-1>',
                        lambda _: self.onLungesclick())
        
        self.guide_image = PhotoImage(
            file=relative_to_assets("guide.png"))
        self.guide = self.canvas.create_image(
            578,
            78,
            anchor = "nw",
            image = self.guide_image
        )
        self.canvas.tag_bind(self.guide, '<ButtonPress-1>',
                             lambda _: self.onGuideclick())

        def Lock():
            self.im_guide_lock = PhotoImage(file = relative_to_assets("guide_lock.png"))
            self.im_pullup_lock = PhotoImage(file = relative_to_assets("pullup_lock.png"))
            self.im_lunges_lock = PhotoImage(file = relative_to_assets("lunges_lock.png"))
            self.canvas.itemconfig(self.guide, image = self.im_guide_lock)
            self.canvas.itemconfig(self.button_1, image = self.im_pullup_lock)
            self.canvas.itemconfig(self.button_lunges, image = self.im_lunges_lock)

        if not self.ispremium: Lock()

    def loadData(self):
        __=load_object("Appdata/userData/data.pickle")
        if (__['status']==True):
            self.username = __['data']['username']
            # update_active(self.username, True)
            self.ispremium = ispremium(self.username)
    
    def onLogoutClicked(self):
        #Do sth with pickle
        os.remove("Appdata/userData/data.pickle")
        os.remove("Appdata/userData/usr_img.jpg")
        self.parent.parent.Authed.set(False)
        self.parent.parent.run()
        self.parent.destroy()

    def onFriendsClicked(self):
        print('onFriends cliked')
        # self.friends.pack()
        self.parent.show_frame(UI.Friends_list.Friendslist)
        # self.destroy()

    def onRankClick(self):
        self.parent.show_frame(UI.Rank.rank)

    def onProfileClick(self):
        self.parent.show_frame(UI.profile.profile)
    
    def onShopClick(self):
        self.parent.show_frame(UI.Shop.shop)
    
    def onpullupclick(self):
        if not self.ispremium: 
            messagebox.showerror('Free Account, so poor!', 'Please upgrade to premium account to get access to this feature')
        else:
            UI.chooseEx.chooseEx(self, 'pull-up').update()
    
    def onLungesclick(self):
        if not self.ispremium: 
            messagebox.showerror('Free Account, so poor!', 'Please upgrade to premium account to get access to this feature')
        else:
            UI.chooseEx.chooseEx(self, 'push-up').update()
    def onGuideclick(self):
        if not self.ispremium: 
            messagebox.showerror('Free Account, so poor!', 'Please upgrade to premium account to get access to this feature')


            









        
        

        




        
        

        
        
        

        


        
        



