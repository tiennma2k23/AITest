from pathlib import Path
from tkinter import *

from Database_processing.Friends_db.add_fr_request import add_fr_request, add_fr_requested
from Database_processing.User_db.get import get_by_username
from Utils.Sources.getdata_pickle import load_object

class resendpass(Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.geometry("400x240")
        self.title = ("Add Friend")

        OUTPUT_PATH = Path(__file__).parent


        ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/addfriend")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)



        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=240,
            width=400,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)


        self.canvas.create_rectangle(
            0.0,
            0.0,
            400.0,
            400.0,
            fill="#BAB8B8",
            outline=""
        )

        self.button_image = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_image_hover = PhotoImage(file=relative_to_assets("button_2.png"))
        self.button_1 = self.canvas.create_image(
            317,
            98,
            image=self.button_image,
            anchor = "nw",
        )
        #press button
        self.canvas.tag_bind(self.button_1, '<ButtonPress-1>',
                        lambda _: self.onButtonClicked())
        #hover button
        self.canvas.tag_bind(self.button_1, '<Enter>', lambda _: self.canvas.itemconfigure(
            self.button_1, image=self.button_image_hover))
        self.canvas.tag_bind(self.button_1, '<Leave>', lambda _: self.canvas.itemconfigure(
            self.button_1, image=self.button_image))

        self.canvas.create_text(
            31.0,
            75.0,
            anchor="nw",
            text="Enter Password",
            fill="#FFFFFF",
            font=("Lato Regular", 14 * -1)
        )


        self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        self.username = StringVar()
        entry_bg_1 = self.canvas.create_image(
            168.5,
            120.0,
            image=self.entry_image_1
        )
        entry_1 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=('Lato', 14 * -1),
            textvariable = self.username
        )
        entry_1.place(
            x=40.266839027404785,
            y=96.0,
            width=256.46632194519043,
            height=46.0
        )
# <<<<<<< Updated upstream
        self.addFrtxt = self.canvas.create_text(
            31.0,
            150,
            anchor="nw",
            text="",
            fill="#FFFFFF",
            font=("Lato Regular", 14 * -1, "bold")
        )
# =======
        self.password = ""
    def onButtonClicked(self):
        # nếu sai pass thì alert
        # if (__['status']==False):
            
            self.canvas.itemconfig(
                self.addFrtxt,
                text="Wrong Password",
            )
        # nếu đúng pass
        
        # else :
            # _method=add_fr_request(_username,self.username.get())
            
            # self.canvas.itemconfig(
                # self.addFrtxt,
                # text=add_fr_request(_username,self.username.get()),
            # )
# >>>>>>> Stashed changesif (__['status']==False):
            
            self.canvas.itemconfig(
                self.addFrtxt,
                text="Wrong Password",
            )
    
    # def onButtonClicked(self):
    #     # nếu sai tên thì cút, y hệt dưới nhưng text = "Username does not exist!""
    #     # nếu đúng tên
    #     self.canvas.itemconfig(self.addFrtxt, text=self.username.get()+'req sent!')
    



        

        


