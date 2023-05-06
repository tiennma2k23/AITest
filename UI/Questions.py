from tkinter import *
# import UI.Login
from Utils.Sources.authen import Auth
from pathlib import Path
from UI.q1 import q1
from UI.q2 import q2
from UI.q3 import q3
from UI.q4 import q4
from UI.q5 import q5
from UI.q6 import q6


OUTPUT_PATH = Path(__file__).parent

ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/question")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class question(Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        # Create a frame and assigning it to container
        # container = Frame(self)
        # Specify the region where the frame is packed in root
        # self.pack(side="top", fill="both", expand=True)

        # Configure container's location with grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (q1, q2, q3, q4, q5, q6):
            frame = F(self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame

        # Using a method to switch frames
        self.show_frame(q1)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.loadData()
        frame.grid(row=0, column=0, sticky="nsew")
        # raises the current frame to the top
        frame.tkraise()



        





