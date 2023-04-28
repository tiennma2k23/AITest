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
from UI.UI import UserHandle

"""
uri = json.loads(open("adminAuth/adminAuth.json","r").read())["uri"]
cluster=MongoClient(uri, server_api=ServerApi('1'))

#Check connection
try:
    cluster.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Save and get data
def save_object(obj):
    try:
        with open("Appdata/userData/data.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)
def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)

# Get user_db
user_db=load_object("Appdata/userData/data.pickle")
print(user_db)
"""
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("746x661")
        self.title('Demo')


        self.protocol("WM_DELETE_WINDOW", self.onClose)
        self.Authed = tk.BooleanVar(self, False)
        self.auth = UserHandle(self)
        self.main = Main(self)

        self.auth.pack()

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
    
    """
    #Firebase
    exercise_type=exType
    collection=db[exercise_type]
    
    username=user_db['username']
    if(collection.count_documents({"username":username})==0):
        collection.insert_one({"_id":username,"username":username,"counter":0})
    collection.update_one({"username":username},{"$inc":{"counter":counter}})
    """
    cap.release()
    cv2.destroyAllWindows()
