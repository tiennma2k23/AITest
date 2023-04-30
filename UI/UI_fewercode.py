from tkinter import *
# import UI.Login
from UI.Login import login_frame
from UI.Register import sign_up_frame
from UI.Resend_Password import resend
from Utils.Sources.authen import Auth

# import Login
# import Register
# import Resend_Password
import os
import sys

# class root(Tk):
#     def __init__(self, *args, **kwargs):
#         Tk.__init__(self, *args, **kwargs)
#         # Adding a title to the window
#         self.wm_title("Test Application")
#         self.geometry("800x480")
#         self.resizable(False, False)

#         # creating a frame and assigning it to container
#         container = Frame(self)
#         # specifying the region where the frame is packed in root
#         container.pack(side="top", fill="both", expand=True)

#         # configuring the location of the container using grid
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)

#         # We will now create a dictionary of frames
#         self.frames = {}
#         # we'll create the frames themselves later but let's add the components to the dictionary.
#         for F in (Login.login_frame, Register.sign_up_frame, Resend_Password.resend):
#             frame = F(container, self)

#             # the windows class acts as the root window for the frames.
#             self.frames[F] = frame
#             frame.grid(row=0, column=0, sticky="nsew")

#         # Using a method to switch frames
#         self.show_frame(Login.login_frame)

#     def show_frame(self, cont):
#         frame = self.frames[cont]
#         # raises the current frame to the top
#         frame.tkraise()


class UserHandle(Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        # Create a frame and assigning it to container
        # container = Frame(self)
        # Specify the region where the frame is packed in root
        self.pack(side="top", fill="both", expand=True)

        # Configure container's location with grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (login_frame, sign_up_frame, resend):
            frame = F(self, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(login_frame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()


if __name__ == "__main__":
    testObj = root()
    testObj.mainloop()
