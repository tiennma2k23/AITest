
from pathlib import Path

from tkinter import *
from PIL import Image, ImageTk


# Explicit imports to satisfy Flake8
# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage



class root(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Test Application")
        self.geometry("800x480")
        self.resizable(False, False)

        # creating a frame and assigning it to container
        container = Frame(self)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (login_frame, sign_up_frame):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(login_frame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()


class login_frame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg="#FFFFFF")
        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=480,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        # create canvas
        canvas.place(x=0, y=0)
        canvas.create_rectangle(
            138.0,
            0.0,
            661.0,
            480.0,
            fill="#A9A9A9",
            outline="")

        # create hyperlink
        def txt_on_click(e):
            txt.configure(fg="#666666")
            controller.show_frame(sign_up_frame)

        txt = Label(self, text="Register here", font=(
            "Lato Regular", 14 * -1), fg="white", bg="#A9A9A9")
        txt.place(x=430, y=393.77)
        txt.bind('<Button-1>', txt_on_click)
        txt.bind('<Enter>', lambda e: txt.configure(fg="#BBBBBB"))
        txt.bind('<Leave>', lambda e: txt.configure(fg="white"))

        # forget pass
        forget_pass = Label(self, text="Forget password?", font=(
            "Lato Regular", 14 * -1), fg="white", bg="#A9A9A9")
        forget_pass.place(x=432, y=288)

        def fgpass_on_click(e):
            forget_pass.configure(fg="#666666")
            # alert/success j do tinh sau

        forget_pass.bind('<Button-1>', fgpass_on_click)
        forget_pass.bind(
            '<Enter>', lambda e: forget_pass.configure(fg="#BBBBBB"))
        forget_pass.bind(
            '<Leave>', lambda e: forget_pass.configure(fg="white"))

        # create other text
        canvas.create_text(
            279.0,
            397.0,
            anchor="nw",
            text="Don’t have an account?",
            fill="#FFFFFF",
            font=("Lato Regular", 14 * -1)
        )

        # create login button
        self.button_image_1 = PhotoImage(file=r'.\assets\frame1\button_1.png')
        self.button_image_2 = PhotoImage(
            file=r'.\assets\frame1\button_1_hover.png')
        self.button_image_3 = PhotoImage(
            file=r'.\assets\frame1\button_1_onclick.png')

        def button_1_onclick():
            button_1.configure(image=self.button_image_3)
            # nhảy sang home page tính sau

        button_1 = canvas.create_image(
            301.0,
            328.0,
            image=self.button_image_1,
            anchor='nw',
        )
        canvas.tag_bind(button_1, '<ButtonPress-1>',
                        lambda _: self.onLoginClick())

        # hover button
        canvas.tag_bind(button_1, '<Enter>', lambda _: canvas.itemconfig(
            button_1, image=self.button_image_2))
        canvas.tag_bind(button_1, '<Leave>', lambda _: canvas.itemconfig(
            button_1, image=self.button_image_1))

        # # place button
        # button_1.place(
        #     x=301.0,
        #     y=328.0,
        #     width=198.3193359375,
        #     height=54.0
        # )

        # create texts above textboxes
        canvas.create_text(
            248.0,
            141.0,
            anchor="nw",
            text="Username/Email*",
            fill="#FFFFFF",
            font=("Lato Regular", 14 * -1)
        )

        canvas.create_text(
            248.0,
            219.0,
            anchor="nw",
            text="Password*",
            fill="#FFFFFF",
            font=("Lato Regular", 14 * -1)
        )

        canvas.create_text(
            355.0,
            57.0,
            anchor="nw",
            text="LOGIN",
            fill="#FFFFFF",
            font=("Lato Regular", 29 * -1)
        )

        # create textboxes
        self.username = StringVar()
        self.password = StringVar()

        self.entry_image_1 = PhotoImage(file=r'.\assets\frame1\entry_1.png')
        entry_bg_1 = canvas.create_image(
            399.667236328125,
            183.09378051757812,
            image=self.entry_image_1
        )
        entry_1 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Lato"),
            textvariable=self.username
        )
        entry_1.place(
            x=257.2668390274048,
            y=159.0,
            width=284.80079460144043,
            height=46.18756103515625
        )

        self.entry_image_2 = PhotoImage(file=r'.\assets\frame1\entry_2.png')
        entry_bg_2 = canvas.create_image(
            399.667236328125,
            261.1086120605469,
            image=self.entry_image_2
        )
        entry_2 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=('Lato'),
            textvariable=self.password,
            show="*"
        )
        entry_2.place(
            x=257.2668390274048,
            y=237.01483154296875,
            width=284.8008556365967,
            height=46.18756103515625
        )

    def onLoginClick(self):
        if (Auth(self.email, self.password).UserAuth()):
            self.parent.parent.Authed.set(True)
            self.parent.parent.geometry('800x480')
            self.parent.parent.main.pack()
            self.parent.destroy()


class sign_up_frame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg="#FFFFFF")

        # create canvas
        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=661,
            width=746,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)
        canvas.create_rectangle(
            138.0,
            2.0,
            661.0,
            480.0,
            fill="#A9A9A9",
            outline="")

        # create Back button
        self.back_img = PhotoImage(file=r'./assets/frame0/back.png')
        self.back_img_hover = PhotoImage(
            file=r'./assets/frame0/back_hover.png')

        # back_button = Button(
        #     self,
        #     image=self.back_img,
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=back_button_onclick,
        #     relief="flat"
        # )

        # hover back button
        # back_button.bind('<Enter>', lambda e: back_button.configure(
        #     image=self.back_img_hover))
        # back_button.bind(
        #     '<Leave>', lambda e: back_button.configure(image=self.back_img))
        # # place back button
        # back_button.place(
        #     x=138.0,
        #     y=2.0,
        #     width=74.0,
        #     height=43.0
        # )

        back = canvas.create_image(
            138.0,
            2.0,
            anchor="nw",
            image=self.back_img
        )
        canvas.tag_bind(back, '<Button-1>',lambda _: controller.show_frame(login_frame))
        canvas.tag_bind(back, '<Enter>', lambda _: canvas.itemconfigure(back, image=self.back_img_hover))
        canvas.tag_bind(back, '<Leave>', lambda _: canvas.itemconfigure(back, image=self.back_img))

        # create signup button
        self.button_image_1 = PhotoImage(file=r'.\assets\frame0\button_1.png')
        self.button_image_2 = PhotoImage(
            file=r'.\assets\frame0\button_1_hover.png')
        self.button_image_3 = PhotoImage(
            file=r'.\assets\frame0\button_1_onclick.png')

        button_1 = canvas.create_image(
            301.0,
            398.0,
            image=self.button_image_1,
            anchor='nw',
        )
        canvas.tag_bind(button_1, '<Button-1>', lambda _: self.onRegisterClick())
        # hover button
        canvas.tag_bind(button_1, '<Enter>', lambda _: canvas.itemconfig(button_1, image=self.button_image_2))
        canvas.tag_bind(button_1, '<Leave>', lambda _: canvas.itemconfig(button_1, image=self.button_image_1))

        # create texts above textboxes
        canvas.create_text(
            248.0,
            83.0,
            anchor="nw",
            text="Username*",
            fill="#FFFFFF",
            font=("Lato Regular", 14 * -1)
        )

        canvas.create_text(
            248.0,
            284.0,
            anchor="nw",
            text="Repeat Password*",
            fill="#FFFFFF",
            font=("Lato Regular", 14 * -1)
        )

        canvas.create_text(
            248.0,
            152.0,
            anchor="nw",
            text="E-mail*",
            fill="#FFFFFF",
            font=("Lato Regular", 14 * -1)
        )

        canvas.create_text(
            248.0,
            218.0,
            anchor="nw",
            text="Password*",
            fill="#FFFFFF",
            font=("Lato Regular", 14 * -1)
        )

        canvas.create_text(
            342.0,
            27.0,
            anchor="nw",
            text="SIGN UP",
            fill="#FFFFFF",
            font=("Lato Regular", 29 * -1)
        )

        # create textboxes
        self.username = StringVar()
        self.password = StringVar()
        self.Email = StringVar()
        self.repeated_pass = StringVar()

        self.entry_image_1 = PhotoImage(file=r'.\assets\frame0\entry_1.png')
        entry_bg_1 = canvas.create_image(
            399.6672668457031,
            125.09378051757812,
            image=self.entry_image_1
        )
        entry_1 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Lato"),
            textvariable=self.username
        )
        entry_1.place(
            x=257.2668390274048,
            y=101.0,
            width=284.8008556365967,
            height=46.18756103515625
        )

        self.entry_image_2 = PhotoImage(file=r'.\assets\frame0\entry_2.png')
        entry_bg_2 = canvas.create_image(
            399.6672668457031,
            326.0937805175781,
            image=self.entry_image_2
        )
        entry_2 = Entry(
            self,
            bd=0,
            bg="#FFFDFD",
            fg="#000716",
            highlightthickness=0,
            font=("Lato"),
            textvariable=self.repeated_pass,
            show="*"
        )
        entry_2.place(
            x=257.2668390274048,
            y=302.0,
            width=284.8008556365967,
            height=46.18756103515625
        )

        self.entry_image_3 = PhotoImage(file=r'.\assets\frame0\entry_3.png')
        entry_bg_3 = canvas.create_image(
            399.6672668457031,
            260.0937805175781,
            image=self.entry_image_3
        )
        entry_3 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Lato"),
            textvariable=self.password,
            show="*"
        )
        entry_3.place(
            x=257.2668390274048,
            y=236.0,
            width=284.8008556365967,
            height=46.18756103515625
        )

        self.entry_image_4 = PhotoImage(file=r'.\assets\frame0\entry_4.png')
        entry_bg_4 = canvas.create_image(
            399.6672668457031,
            194.09378051757812,
            image=self.entry_image_4
        )
        entry_4 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Lato"),
            textvariable=self.Email,
        )
        entry_4.place(
            x=257.2668390274048,
            y=170.0,
            width=284.8008556365967,
            height=46.18756103515625
        )

    def onRegisterClick(self):
        if (self.password.get() != self.repeated_pass.get()):
            MessageBox.showerror('Please retry!',
                                 'Repeated password mismatch!')
            return

        if (Auth(self.Email, self.password).UserReg()):
            MessageBox.showinfo('Register Successfully!',
                                'Please check your email for confirmation!')
            self.parent.show_frame(login_frame)


if __name__ == "__main__":
    testObj = root()
    testObj.mainloop()
