from pathlib import Path
from tkinter import *

from Database_processing.User_db.get_gendermale import *
from Utils.Sources.getdata_pickle import load_object
from Utils.Sources.savedata_pickle import save_object

OUTPUT_PATH = Path(__file__).parent


ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/premium")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Premium(Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.geometry("%dx%d+%d+%d" % (800, 480, (1920/2 - 800/2), (1080/2-400/2)))
        self.title = ("Suggested Exercises")
        self.loadData()


        #create BG
        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=480,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            400.0,
            240.0,
            image=self.image_image_1
        )
        # headline1
        self.canvas.create_text(
            37,
            100,
            anchor="nw",
            text="Upgrade to Premium",
            fill="#646464",
            font=("Lato", 30 * -1, "bold")
        )
        # headline2
        self.canvas.create_text(
            497,
            100,
            anchor="nw",
            text="Choose your plan",
            fill="#646464",
            font=("Lato", 30 * -1, "bold")
        )
        #intro
        self.canvas.create_text(
            37,
            148,
            anchor="nw",
            text="You can get a lot more out of it.",
            fill="#646464",
            font=("Lato", 17 * -1)
        )
        self.canvas.create_text(
            37,
            170,
            anchor="nw",
            text="Upgrade to premium to get all of these features:",
            fill="#7C7C7C",
            font=("Lato", 17 * -1)
        )
        #features
        self.canvas.create_text(
            104,
            205,
            anchor="nw",
            text="Higher camera quality",
            fill="#7C7C7C",
            font=("Lato", 20 * -1, "bold")
        )
        self.canvas.create_text(
            104,
            341,
            anchor="nw",
            text="Priority tech support",
            fill="#7C7C7C",
            font=("Lato", 20 * -1, "bold")
        )
        self.canvas.create_text(
            104,
            251,
            anchor="nw",
            text="Access to Guides",
            fill="#7C7C7C",
            font=("Lato", 20 * -1, "bold")
        )
        self.canvas.create_text(
            104,
            295,
            anchor="nw",
            text="Additional exercises",
            fill="#7C7C7C",
            font=("Lato", 20 * -1, "bold")
        )
        #duration
        self.canvas.create_text(
            471,
            172,
            anchor="nw",
            text="Weekly:",
            fill="#7C7C7C",
            font=("Lato", 19 * -1, "bold")
        )
        self.canvas.create_text(
            471,
            220,
            anchor="nw",
            text="Monthly",
            fill="#7C7C7C",
            font=("Lato", 19 * -1, "bold")
        )
        self.canvas.create_text(
            471,
            268,
            anchor="nw",
            text="Quaterly:",
            fill="#7C7C7C",
            font=("Lato", 19 * -1, "bold")
        )
        self.canvas.create_text(
            471,
            316,
            anchor="nw",
            text="Annually:",
            fill="#7C7C7C",
            font=("Lato", 19 * -1, "bold")
        )
        #prices
        self.canvas.create_text(
            571,
            172,
            anchor="nw",
            text="$2.99/week",
            fill="#7C7C7C",
            font=("Lato", 19 * -1)
        )
        self.canvas.create_text(
            571,
            220,
            anchor="nw",
            text="$8.99/month",
            fill="#7C7C7C",
            font=("Lato", 19 * -1)
        )
        self.canvas.create_text(
            571,
            268,
            anchor="nw",
            text="$20.7/quarter",
            fill="#7C7C7C",
            font=("Lato", 19 * -1)
        )
        self.canvas.create_text(
            571,
            316,
            anchor="nw",
            text="$52.99/year:",
            fill="#7C7C7C",
            font=("Lato", 19 * -1)
        )
        #images
        self.radio_1_image = PhotoImage(file=relative_to_assets("radio1.png"))
        self.radio_2_image = PhotoImage(file=relative_to_assets("radio2.png"))
        self.radio_3_image = PhotoImage(file=relative_to_assets("radio3.png"))
        self.radio_4_image = PhotoImage(file=relative_to_assets("radio4.png"))
        
        self.radio_1 = self.canvas.create_image(
            72,
            208,
            image=self.radio_1_image,
            anchor = "nw",
        )
        self.radio_2 = self.canvas.create_image(
            72,
            253,
            image=self.radio_2_image,
            anchor = "nw",
        )
        self.radio_3 = self.canvas.create_image(
            72,
            298,
            image=self.radio_3_image,
            anchor = "nw",
        )
        self.radio_4 = self.canvas.create_image(
            72,
            343,
            image=self.radio_4_image,
            anchor = "nw",
        )
        #buttons
        self.submit1 = Button(
                self.canvas,
                text="Select",
                font=('Lato', 18 * -1),
                fg = "#E4E4E4",
                bg = "#676767",
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.func(),
                relief="flat"
            )
        self.submit1.place(
                x=705,
                y=172,
                width=95,
                height=27.98
            )
        self.submit2 = Button(
                self.canvas,
                text="Select",
                font=('Lato', 18 * -1),
                fg = "#E4E4E4",
                bg = "#676767",
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.func(),
                relief="flat"
            )
        self.submit2.place(
                x=705,
                y=216,
                width=95,
                height=27.98
            )
        self.submit3 = Button(
                self.canvas,
                text="Select",
                font=('Lato', 18 * -1),
                fg = "#E4E4E4",
                bg = "#676767",
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.func(),
                relief="flat"
            )
        self.submit3.place(
                x=705,
                y=266,
                width=95,
                height=27.98
            )
        self.submit4 = Button(
                self.canvas,
                text="Select",
                font=('Lato', 18 * -1),
                fg = "#E4E4E4",
                bg = "#676767",
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.func(),
                relief="flat"
            )
        self.submit4.place(
                x=705,
                y=316,
                width=95,
                height=27.98
            )

    def loadData(self):
        pass
    def func(self):
        pass



        

        


