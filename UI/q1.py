from tkinter import *
from pathlib import Path
from Database_processing.Friends_db.add_fr_request import add_fr_request
from Database_processing.Friends_db.delete_fr import delete_fr
from Database_processing.Friends_db.get_friends import get_fr_by_username
from Database_processing.Friends_db.update_fr import update_fr_user
from Database_processing.User_db.get_img_profile import get_img_profile
from Database_processing.User_db.get_rank_user import get_rank_user
from Utils.Sources.getdata_pickle import load_object
import UI.q2


OUTPUT_PATH = Path(__file__).parent

ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/question")
def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

class q1(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.loadData()
        self.gendermale = True # chắc là up lên db


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
                sometxt, fill="#999999"))
            self.canvas.tag_bind(sometxt, '<Leave>', lambda _: self.canvas.itemconfig(
                sometxt, fill="#646464"))

        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            400.0,
            240.0,
            image=self.image_image_1
        )
        # #logo txt
        # home_txt=self.canvas.create_text(
        #     93,
        #     22,
        #     anchor="nw",
        #     text="EXERA",
        #     fill="#646464",
        #     font=("Lato", int(30))
        # )
        #back button
        button_1 = Button(
            self.canvas,
            text="Back",
            font=('Lato', 14),
            bg="#9E9E9E",
            fg="white",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.onBackClick(),
            relief="flat"
        )
        # button_1.place(
        #     x = 726, 
        #     y = 0,
        #     width = 74,
        #     height = 43,
        # )

        #next button
        button_2 = Button(
            self.canvas,
            text="Next",
            font=('Lato', 14),
            fg="white",
            bg="#636363",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.onNextClick(),
            relief="flat"
        )
        button_2.place(
            x = 726, 
            y = 437,
            width = 74,
            height = 43,
        )

        #question txt
        q_txt=self.canvas.create_text(
            306, 
            128,
            anchor="nw",
            text="Your gender",
            fill="#646464",
            font=("Lato", int(35) * -1, "bold")
        )
        #male txt
        self.male_txt=self.canvas.create_text(
            180,
            234,
            anchor="nw",
            text="Male",
            fill="#646464",
            font=("Lato", int(30) * -1, "underline")
        )
        hovertxt(self.male_txt)
        self.canvas.tag_bind(self.male_txt, '<ButtonPress-1>',
                        lambda _: self.onMaleClick())

        #Female txt
        self.female_txt=self.canvas.create_text(
            526,
            234,
            anchor="nw",
            text="Female",
            fill="#646464",
            font=("Lato", int(30) * -1)
        )
        hovertxt(self.female_txt)
        self.canvas.tag_bind(self.female_txt, '<ButtonPress-1>',
                        lambda _: self.onFemaleClick())
    
    def loadData(self):
        pass
    def onMaleClick(self):
        self.canvas.itemconfig(self.male_txt, fill = "#BBBBBB")
        self.canvas.itemconfig(self.male_txt, font = ("Lato", int(30) * -1, "underline"))
        self.canvas.itemconfig(self.female_txt, fill = "#646464")
        self.canvas.itemconfig(self.female_txt, font=("Lato", int(30) * -1))
        self.gendermale = True
    def onFemaleClick(self):
        self.gendermale = False
        self.canvas.itemconfig(self.female_txt, fill = "#BBBBBB")
        self.canvas.itemconfig(self.female_txt, font = ("Lato", int(30) * -1, "underline"))
        self.canvas.itemconfig(self.male_txt, fill = "#646464")
        self.canvas.itemconfig(self.male_txt, font=("Lato", int(30) * -1))
    
    def onNextClick(self):
        self.parent.show_frame(UI.q2.q2)
    def onBackClick(self):
        pass
    


