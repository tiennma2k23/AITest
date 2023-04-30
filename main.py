import tkinter as tk
import tkinter.messagebox as messagebox

from UI.UI import UserHandle
from UI.chooseEx import chooseEx

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("746x661")
        self.title('Demo')


        self.protocol("WM_DELETE_WINDOW", self.onClose)
        self.Authed = tk.BooleanVar(self, False)
        self.auth = UserHandle(self)
        self.main = chooseEx(self)

        self.auth.pack()

    def onClose(self):
        if (messagebox.askyesno('Quit?', 'U quit?')):
            self.Authed.set(False)
            self.destroy()

app = App()
app.mainloop()
