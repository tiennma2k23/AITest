import tkinter as tk
from queue import Queue
from threading import Thread
import Utils.camera as camera
from .Friends import Friends_frame
from PIL import ImageTk, Image

ENABLE_WEBCAM = False #True to enable webcam

class chooseEx(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.friends = Friends_frame(self)
        self.eType = ('pull-up', 'push-up', 'sit-up', 'squat', 'walk')
        self.tkStr = tk.StringVar(self)
        self.frameQueue = Queue(30)
        self.mainF = tk.Frame(self)
        self.label = tk.Label(self.mainF,  text='Select:')
        self.label.grid(column=0, row=0)
        # option menu
        self.option_menu = tk.OptionMenu(
            self.mainF,
            self.tkStr,
            '',
            *self.eType)
        self.option_menu.grid(column=1,row=0)
        self.btnCamera = tk.Button(
            self.mainF, 
            text='Show camera',
            command=lambda: self.onShowCameraClicked()
        )
        self.btnCamera.grid(column=2,row=0)
        self.btnFriends = tk.Button(
            self.mainF,
            text='Friends and Reqs',
            command=lambda: self.onShowFriendsClicked()
        )
        self.btnFriends.grid(column=3, row=0)
        self.mainF.pack()

    def onShowFriendsClicked(self):
        self.friends.mainF.pack()
        self.destroy()

    def onShowCameraClicked(self):
        print('show camera clicked')
        
        if not (self.tkStr.get()): 
            print('Invalid')
            return

        def getFrame():
            frameData = self.frameQueue.get(True)
            if (frameData is camera._endOfQueue): 
                self.btn["state"] = 'normal'
                self.cameraCanvas.destroy()
                return

            img = Image.fromarray(frameData)
            imgtk = ImageTk.PhotoImage(image=img)
            self.cameraCanvas.imgtk = imgtk
            self.cameraCanvas['image']=imgtk

            #Call again after 30ms (Simulate ~30FPS)
            self.cameraCanvas.after(30, getFrame)
        
        self.btn["state"] = 'disabled'
        exType = self.tkStr.get()
        #Start rendering in seperated thread
        cameraThread = Thread(target=camera.__main__,
                              args= (exType, ENABLE_WEBCAM, self.frameQueue),
                              daemon=True)
        cameraThread.start()

        self.cameraCanvas = tk.Label(self.mainF)
        self.cameraCanvas.grid(column=0, row=1, columnspan=3)
        getFrame()
