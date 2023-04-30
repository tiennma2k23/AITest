

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("746x661")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 661,
    width = 746,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    111.81982421875,
    59.925567626953125,
    634.4696044921875,
    601.1089172363281,
    fill="#BAB8B8",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=273.6806640625,
    y=480.0,
    width=198.3193359375,
    height=54.0
)

canvas.create_text(
    223.0,
    148.0,
    anchor="nw",
    text="Username*",
    fill="#FFFFFF",
    font=("Lato Regular", 14 * -1)
)

canvas.create_text(
    223.0,
    372.0,
    anchor="nw",
    text="Repeat Password*",
    fill="#FFFFFF",
    font=("Lato Regular", 14 * -1)
)

canvas.create_text(
    223.0,
    224.0,
    anchor="nw",
    text="E-mail*",
    fill="#FFFFFF",
    font=("Lato Regular", 14 * -1)
)

canvas.create_text(
    223.0,
    298.0,
    anchor="nw",
    text="Password*",
    fill="#FFFFFF",
    font=("Lato Regular", 14 * -1)
)

canvas.create_text(
    314.4547119140625,
    94.52175903320312,
    anchor="nw",
    text="SIGN UP",
    fill="#FFFFFF",
    font=("Lato Regular", 29 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    373.6672668457031,
    196.09378051757812,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=231.26683902740479,
    y=172.0,
    width=284.8008556365967,
    height=46.18756103515625
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    372.8357849121094,
    418.24334716796875,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=230.43535709381104,
    y=394.1495666503906,
    width=284.8008556365967,
    height=46.18756103515625
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    372.8357849121094,
    344.1086120605469,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=230.43535709381104,
    y=320.01483154296875,
    width=284.8008556365967,
    height=46.18756103515625
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    372.8357849121094,
    269.9739227294922,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=230.43535709381104,
    y=245.88014221191406,
    width=284.8008556365967,
    height=46.18756103515625
)
window.resizable(False, False)
window.mainloop()
