from pathlib import Path
from tkinter import *

from Database_processing.User_db.get_gendermale import *
from Utils.Sources.getdata_pickle import load_object
from Utils.Sources.savedata_pickle import save_object

OUTPUT_PATH = Path(__file__).parent


ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/homepage")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class guide(Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.geometry("%dx%d+%d+%d" % (800, 480, (1920/2 - 800/2), (1080/2-400/2)))
        self.title = ("Suggested Exercises")
        self.username = ""
        self.gendermale = True
        self.loadData()

        self.pullups = 25 if (self.gendermale) else 5
        self.pushups = 20 if (self.gendermale) else 10
        self.situps = 35 if (self.gendermale) else 30
        self.squat = 35 if (self.gendermale) else 25
        self.walkmin = 90 if (self.gendermale) else 45
        self.walkdis = 5 if (self.gendermale) else 3.5
        self.lunges = 40 if (self.gendermale) else 30
        self.plank = 3 if (self.gendermale) else 1.5

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

        #headline
        self.canvas.create_text(
            243.0,
            25.0,
            anchor="nw",
            text="Suggested Exercises",
            fill="#5F5F5F",
            font=("Lato Regular", 35 * -1, "bold")
        )
        #pullups
        self.canvas.create_text(
            65,
            87,
            anchor="nw",
            text="Pull-ups: " + str(self.pullups) + " pull-ups " + "per day",
            fill="#7C7C7C",
            font=("Lato Regular", 25 * -1, "bold")
        )
        #pushups
        self.canvas.create_text(
            65,
            137,
            anchor="nw",
            text="Push-ups: " + str(self.pushups) + " push-ups " + "per day",
            fill="#7C7C7C",
            font=("Lato Regular", 25 * -1, "bold")
        )
        #situps
        self.canvas.create_text(
            65,
            187,
            anchor="nw",
            text="Sit-ups: " + str(self.situps) + " sit-ups " + "per day",
            fill="#7C7C7C",
            font=("Lato Regular", 25 * -1, "bold")
        )
        #Squat
        self.canvas.create_text(
            65,
            237,
            anchor="nw",
            text="Squat: " + str(self.squat) + " squats " + "per day",
            fill="#7C7C7C",
            font=("Lato Regular", 25 * -1, "bold")
        )
        #Walk
        self.canvas.create_text(
            65,
            287,
            anchor="nw",
            text="Walk: " + str(self.walkmin) + " minutes, " + str(self.walkdis) + " km " + "per day",
            fill="#7C7C7C",
            font=("Lato Regular", 25 * -1, "bold")
        )
        #Lunges
        self.canvas.create_text(
            65,
            337,
            anchor="nw",
            text="Lunges: " + str(self.lunges) + " lunges " + "per day",
            fill="#7C7C7C",
            font=("Lato Regular", 25 * -1, "bold")
        )
        #Plank
        self.canvas.create_text(
            65,
            387,
            anchor="nw",
            text="Plank: " + str(self.plank) + " minutes " + "per day",
            fill="#7C7C7C",
            font=("Lato Regular", 25 * -1, "bold")
        )
        #Plank
        self.canvas.create_text(
            532,
            458,
            anchor="nw",
            text="*Suggested exercises could change per day",
            fill="#5C5C5C",
            font=("Lato Regular", 12 * -1, "italic")
        )





        
    def loadData(self):
        __=load_object("Appdata/userData/data.pickle")
        if (__['status']==True):
            self.username = __['data']['username']
            # update_active(self.username, True)
            self.gendermale = get_gendermale(self.username)
    



        

        


