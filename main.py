import cv2
import argparse
from utils import *
import mediapipe as mp
from body_part_angle import BodyPartAngle
from types_of_exercise import TypeOfExercise
import time
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x480")
        self.title('Demo')

        self.eType = ('pull-up', 'push-up', 'sit-up', 'squat', 'walk')
        self.tkStr = tk.StringVar(self)

        self.protocol("WM_DELETE_WINDOW", self.onDestroy)
        self.createWidget()

    def onDestroy(self):
        self.tkStr.set('')
        self.destroy()

    def onShowCameraClicked(self):
        if not (self.tkStr.get()): print('Invalid')
        else: self.destroy()

    def createWidget(self):
        self.label = tk.Label(self,  text='Select:')
        self.label.pack()

        # option menu
        self.option_menu = tk.OptionMenu(
            self,
            self.tkStr,
            '',
            *self.eType)
        self.option_menu.pack()

        self.btn = tk.Button(self, text='Show camera',command=self.onShowCameraClicked)
        self.btn.pack()
    
while True:
    app = App()
    app.mainloop()
    if not (app.tkStr.get()): break

    args = [app.tkStr.get(), app.tkStr.get()+".mp4"]
    print(args)

    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    cap = cv2.VideoCapture("Exercise_videos/" + args[1]) #Test videos
    #cap = cv2.VideoCapture(0)  # webcam

    cap.set(3, 800)  # width
    cap.set(4, 480)  # height

    # setup mediapipe
    with mp_pose.Pose(min_detection_confidence=0.5,
                    min_tracking_confidence=0.5) as pose:

        counter = 0  # movement of exercise
        status = True  # state of move
        while cap.isOpened():
            ret, frame = cap.read()
            # result_screen = np.zeros((250, 400, 3), np.uint8)
            try:
                frame = cv2.resize(frame, (800, 480), interpolation=cv2.INTER_AREA)
            except:
                break
            # recolor frame to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame.flags.writeable = False

            # make detection
            start = time.time()
            results = pose.process(frame)
            end = time.time()
            print(results, end-start)
            # recolor back to BGR
            frame.flags.writeable = True
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark
                counter, status = TypeOfExercise(landmarks).calculate_exercise(
                    args[0], counter, status)
            except:
                pass

            frame = score_table(args[0], frame, counter, status)

            # render detections (for landmarks)
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

            cv2.imshow('Video', frame)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
