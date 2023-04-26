import cv2
#import argparse
from utils import *
import mediapipe as mp
from body_part_angle import BodyPartAngle
from types_of_exercise import TypeOfExercise
#import time
import tkinter as tk
import tkinter.messagebox as messagebox
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json


uri = json.loads(open("adminAuth.json","r").read())["uri"]
cluster=MongoClient(uri, server_api=ServerApi('1'))

#Check connection
try:
    cluster.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db=cluster["excercise_db_test"]
username="demo"

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x480")
        self.title('Demo')


        self.protocol("WM_DELETE_WINDOW", self.onClose)
        self.Authed = tk.BooleanVar(self, False)
        self.auth = Auth(self)
        self.main = Main(self)

        self.auth.pack()

    def onClose(self):
        if (messagebox.askyesno('Quit?', 'U quit?')):
            self.Authed.set(False)
            self.destroy()

class Auth(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.username = tk.StringVar(self, '')
        self.password = tk.StringVar(self, '')

        self.authF = tk.Frame(self)
        self.usrLabel = tk.Label(self.authF, text="Username: ").pack()
        self.pswLabel = tk.Label(self.authF, text="Password: ").pack()
        self.usrEntry = tk.Entry(self.authF, width=20, textvariable=self.username).pack()
        self.pswEntry = tk.Entry(self.authF, width=20, textvariable=self.password).pack()
        self.smbBtn = tk.Button(self.authF, text="Login", command=self.UsrAuth).pack()
        self.authF.pack()

    def UsrAuth(self):
        if (self.username.get()):
            print("Access Granted!")
            self.parent.Authed.set(True)
            self.parent.main.pack()
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
            command=self.onShowCameraClicked).pack()

        self.mainF.pack()

    def onShowCameraClicked(self):
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
    cap = cv2.VideoCapture("Exercise_videos/" + exType + ".mp4") #Test videos
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
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    exercise_type=exType
    collection=db[exercise_type]
    if(collection.count_documents({"username":username})==0):
        collection.insert_one({"_id":username,"username":username,"counter":0})
    collection.update_one({"username":username},{"$inc":{"counter":counter}})
    cap.release()
    cv2.destroyAllWindows()
