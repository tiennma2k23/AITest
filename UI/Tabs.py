from tkinter import *
# import UI.Login
from UI.Homepage import homepage
from UI.Friends import Friends_frame
from Utils.Sources.authen import Auth
from UI.Login import login_frame

# import Login
# import Register
# import Resend_Password

class Tabs(Frame):
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
        for F in (homepage, Friends_frame):
            frame = F(self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(homepage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()


# if __name__ == "__main__":
#     testObj = root()
#     testObj.mainloop()
