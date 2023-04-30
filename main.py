import cv2
#import time
import mediapipe as mp
import tkinter as tk
import tkinter.messagebox as messagebox
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
import pickle

# from body_part_angle import BodyPartAngle
from Utils.Calc.types_of_exercise import TypeOfExercise
from Utils.Calc.utils import *
from UI.UI_fewercode import UserHandle
from Utils.Sources.getdata_pickle import load_object
from Database_processing.Exercise_db.update import update

"""
uri = json.loads(open("adminAuth/adminAuth.json","r").read())["uri"]
cluster=MongoClient(uri, server_api=ServerApi('1'))

#Check connection
try:
    cluster.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
"""

_db=load_object("Appdata/userData/data.pickle")
user_db=_db['data']
# print(user_db)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x480")
        self.resizable(False, False)
        self.title('Demo')


        self.protocol("WM_DELETE_WINDOW", self.onClose)
        
        if(_db['status']==False): 
            self.Authed = tk.BooleanVar(self, False)
            self.auth = UserHandle(self)
            self.main = Main(self)
            self.auth.pack()
        else: 
            self.Authed = tk.BooleanVar(self, True)
            self.main=Main(self)
            self.main.pack()

        

    def onClose(self):
        if (messagebox.askyesno('Quit?', 'U quit?')):
            self.Authed.set(False)
            self.destroy()

class Main(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.eType = ('pull-up', 'push-up', 'sit-up', 'squat', 'walk')
        self.tkStr = tk.StringVar(self)
        
        self.mainF = tk.Frame(self)

        self.label = tk.Label(self.mainF,  text='Select:').pack()
        # option menu
        self.option_menu = tk.OptionMenu(
            self.mainF,
            self.tkStr,
            '',
            *self.eType).pack()
        self.btn = tk.Button(
            self.mainF, 
            text='Show camera',
            command=lambda: self.onShowCameraClicked()).pack()

        self.mainF.pack()

    def onShowCameraClicked(self):
        print('show camera clicked')
        if not (self.tkStr.get()): print('Invalid')
        else: self.quit()

app = App()
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5,
                        min_tracking_confidence=0.5)


while True:
    app.mainloop()
    if not (app.Authed.get()): break

    exType = app.main.tkStr.get()
    cap = cv2.VideoCapture("_test/videos/" + exType + ".mp4") #Test videos
    #cap = cv2.VideoCapture(0)  # webcam
    cap.set(3, 800)  # width
    cap.set(4, 480)  # height

    # setup mediapipe
    counter = 0  # movement of exercise
    status = False  # state of move
    while cap.isOpened():
        frame = cap.read()[1] #np.ndarray format
        try:
            frame = cv2.resize(frame, (800, 480), interpolation=cv2.INTER_AREA)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        except:
            break

        #start = time.time()
        results = pose.process(frame) #RGB format required
        #end = time.time()
        #print(results, end-start)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) #openCV requires BGR

        #Get landmarks and update
        try:
            landmarks = results.pose_landmarks.landmark
            counter, status = TypeOfExercise(landmarks).calculate_exercise(
                exType, counter, status)
        except:
            pass

        #Start drawing
        frame.flags.writeable = True #Disable read-only

        #Draw ScoreTable
        frame = score_table(exType, frame, counter, status)
        #Draw landmarks and connections
        mp_drawing.draw_landmarks(
            frame,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(255, 255, 255),
                                thickness=2,
                                circle_radius=2),
            mp_drawing.DrawingSpec(color=(174, 139, 45),
                                thickness=2,
                                circle_radius=2),
        )

        cv2.imshow('Video', frame) #Render
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    _db=load_object("Appdata/userData/data.pickle")
    user_db=_db['data']
    username=user_db['username']
    update(username,counter,exType)
    """
    
    """
    cap.release()
    cv2.destroyAllWindows()