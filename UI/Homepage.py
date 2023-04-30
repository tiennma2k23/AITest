from tkinter import *
from UI.Friends import Friends_frame
from pathlib import Path
# Explicit imports to satisfy Flake8
# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


class homepage(Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        
        self.mainF = Frame(self)
        self.friends = Friends_frame(self)


        OUTPUT_PATH = Path(__file__).parent


        ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/homepage")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        #create BG
        self.canvas = Canvas(
            self.mainF,
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
                        lambda _: print("profile"))
        
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
                        lambda _: print("ranking"))

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
                        lambda _: print("Shop"))
        
        #create buttons
        #button1
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = self.canvas.create_image(
            65, 
            132,
            image=self.button_image_1,
            anchor = "nw",
        )
        self.canvas.tag_bind(button_1, '<ButtonPress-1>',
                        lambda _: print(1))
        #button2
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = self.canvas.create_image(
            341,
            177,
            image=self.button_image_2,
            anchor="nw",
        )
        self.canvas.tag_bind(button_2, '<ButtonPress-1>',
                        lambda _: print(1))
                    
        #button3
        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = self.canvas.create_image(
            586,
            151,
            image=self.button_image_3,
            anchor="nw",
        )
        self.canvas.tag_bind(button_3, '<ButtonPress-1>',
                        lambda _: print(1))
        #button4
        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = self.canvas.create_image(
            204,
            286,
            image=self.button_image_4,
            anchor="nw",
        )
        self.canvas.tag_bind(button_4, '<ButtonPress-1>',
                        lambda _: print(1))
        #button5
        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = self.canvas.create_image(
            478,
            273,
            image=self.button_image_5,
            anchor="nw",
        )
        self.canvas.tag_bind(button_5, '<ButtonPress-1>',
                        lambda _: print(1))

        self.mainF.pack()

    def onLogoutClicked(self):
        #Do sth with pickle
        self.parent.Authed.set(False)
        self.parent.run()
        self.destroy()

    def onFriendsClicked(self):
        self.friends.mainF.pack()
        self.destroy()









        
        

        




        
        

        
        
        

        


        
        



