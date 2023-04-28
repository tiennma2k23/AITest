import Login
from tkinter import *
# Explicit imports to satisfy Flake8
# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


class resend(Frame):
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
        canvas.place(x=0, y=0)
        canvas.create_rectangle(
            138.0,
            2.0,
            661.0,
            480.0,
            fill="#BAB8B8",
            outline="")

        self.back_img = PhotoImage(file=r'./assets/resendpass/button_1.png')
        self.back_img_hover = PhotoImage(file=r'./assets/resendpass/back_hover.png')

        back = canvas.create_image(
            138.0,
            2.0,
            anchor="nw",
            image=self.back_img
        )
        canvas.tag_bind(back, '<Button-1>',lambda _: controller.show_frame(Login.login_frame))
        canvas.tag_bind(back, '<Enter>', lambda _: canvas.itemconfigure(back, image=self.back_img_hover))
        canvas.tag_bind(back, '<Leave>', lambda _: canvas.itemconfigure(back, image=self.back_img))


        self.button_image_2 = PhotoImage(file=r'./assets/resendpass/button_2.png')
        button_2 = canvas.create_image(
            309,
            241,
            image=self.button_image_2,
            anchor="nw"
        )
        canvas.tag_bind(button_2, '<ButtonPress-1>', lambda _: print("Button_2 clicked"))


        canvas.create_text(
            248.0,
            146.0,
            anchor="nw",
            text="Send E-mail for resetting password",
            fill="#FFFFFF",
            font=("Lato Regular", 14 * -1)
        )

        self.resend_email = StringVar()
        self.entry_image_1 = PhotoImage(file=r'./assets/resendpass/entry_1.png')
        entry_bg_1 = canvas.create_image(
            399.667236328125,
            194.09378051757812,
            image=self.entry_image_1
        )
        entry_1 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=('Lato'),
            textvariable=self.resend_email
        )
        entry_1.place(
            x=257.2668390274048,
            y=170.0,
            width=284.80079460144043,
            height=46.18756103515625
        )
        