

import Login
from tkinter import *
# Explicit imports to satisfy Flake8
# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


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
        self.back_img_hover = PhotoImage(file=r'./assets/frame0/back_hover.png')

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
            image = self.back_img
        )
        canvas.tag_bind(back, '<Button-1>', lambda _: controller.show_frame(Login.login_frame))
        canvas.tag_bind(back, '<Enter>', lambda _: canvas.itemconfigure(back, image = self.back_img_hover))
        canvas.tag_bind(back, '<Leave>', lambda _: canvas.itemconfigure(back, image = self.back_img))

        # create signup button
        self.button_image_1 = PhotoImage(file=r'.\assets\frame0\button_1.png')
        self.button_image_2 = PhotoImage(file=r'.\assets\frame0\button_1_hover.png')
        self.button_image_3 = PhotoImage(file=r'.\assets\frame0\button_1_onclick.png')

        button_1 = canvas.create_image(
            301.0,
            398.0,
            image=self.button_image_1,
            anchor='nw',
        )
        canvas.tag_bind(button_1, '<Button-1>',lambda _: self.onRegisterClick())
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
            self.parent.show_frame(Login.login_frame)
