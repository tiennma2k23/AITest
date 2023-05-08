import tkinter as tk
from queue import Queue
from threading import Thread
import Utils.camera as camera
from .Friends import Friends_frame
from PIL import ImageTk, Image

ENABLE_WEBCAM = False #True to enable webcam

class chooseEx(tk.Toplevel):
    def __init__(self, parent, exType: str):
        super().__init__()
        self.parent = parent
        self.geometry("%dx%d+%d+%d" % (800, 480, (1920/2 - 800/2), (1080/2-400/2)))
        self.title('EXERA Camera')
        self.eType = ('pull-up', 'push-up', 'sit-up', 'squat', 'walk')
        self.tkStr = tk.StringVar(self)
        self.tkStr.set(exType)
        self.frameQueue = Queue(30)
        self.protocol("WM_DELETE_WINDOW", self.onClose)
        self.onShowCameraClicked()

    def onShowCameraClicked(self):
        print('show camera clicked')
        isRunning = False
        
        if not (self.tkStr.get()): 
            print('Invalid')
            return

        def getFrame():
            frameData = self.frameQueue.get(True)
            #True = Wait until got a frame
            if (frameData is camera._endOfQueue): 
                self.cameraCanvas.destroy()
                return

            img = Image.fromarray(frameData)
            imgtk = ImageTk.PhotoImage(image=img)
            self.cameraCanvas.imgtk = imgtk
            self.cameraCanvas['image']=imgtk

            #Call again after 30ms (Simulate ~30FPS)
            self.cameraCanvas.after(30, getFrame)


        exType = self.tkStr.get()
        #Start rendering in seperated thread
        self.cameraThread = Thread(target=camera.__main__,
                              args= (exType, ENABLE_WEBCAM, self.frameQueue),
                              daemon=True)
        self.cameraThread.start()

        self.cameraCanvas = tk.Label(self)
        self.cameraCanvas.grid(column=0, row=1)
        getFrame()

    def onClose(self):
        camera.isRunning = False
        self.cameraThread.join()
        self.withdraw()
