import cv2
import mediapipe as mp
from threading import Thread
from queue import Queue
from Database_processing.Exercise_db.update import update

# from body_part_angle import BodyPartAngle
from Utils.Calc.types_of_exercise import TypeOfExercise
from Utils.Calc.utils import *
from Utils.Sources.getdata_pickle import load_object

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5,
                        min_tracking_confidence=0.5)

#fr = None
counter = 0
status = False
_endOfQueue = object()
isRunning = True
calcFunc = TypeOfExercise().calculate_exercise

# print(_username)
def capture(exType: str, frame: np.ndarray, _fq: Queue):
    global fr, counter, status, isRunning, calcFunc
    try:
        frame = cv2.resize(frame, (800, 480), interpolation=cv2.INTER_AREA)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    except:
        isRunning = False
        return
    
    results = pose.process(frame) #RGB format required
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) #openCV requires BGR

    #Get landmarks and update
    try:
        if (exType != 'walk'): landmarks = results.pose_landmarks.landmark
        else: landmarks = results.pose_world_landmarks.landmark
        counter, status = calcFunc(
            landmarks, exType, counter, status)
    except:
        pass #In case mediapipe desync

    #Start drawing
    frame.flags.writeable = True #Disable read-only

    #Draw ScoreTable
    frame = score_table(exType, frame, round(counter, 2), status)
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

    #Convert back to RGB for displaying
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # if (_fq.full()):
    #     _fq.get() #Drop last item
    #     print('Frame dropped')
    #Currently unnecessary

    _fq.put(frame)


def __main__(exType: str, webcam: bool, _fq: Queue):
    if not (exType):
        print('Invalid choice')
        return

    global fr, counter, status, isRunning
    isRunning = True
    if (webcam):
        cap = cv2.VideoCapture(0)  # webcam
    else:
        cap = cv2.VideoCapture('_test/videos/'+exType+'.mp4')
    cap.set(3, 800)  # width
    cap.set(4, 480)  # height

    #Get counter from User_db
    counter = 0
    status = False

    # setup mediapipe
    tmp=0
    while (isRunning) & cap.isOpened():
        tmp+=1
        if(tmp==10000):break
        _, frame = cap.read() #np.ndarray format
        renderThread = Thread(daemon=True, target=capture, args=(exType, frame, _fq))
        renderThread.start()
        renderThread.join()

        # cv2.imshow('Video', fr) #Render
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
    # __=load_object("Appdata/userData/data.pickle")
    # user_db=__['data']
    # _username=user_db['username']
    # print(_username,counter,exType)
    # update(_username,counter,exType)
    cap.release()
    _fq.put(_endOfQueue)

#__main__('pull-up')