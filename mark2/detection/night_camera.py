import cv2
import pyttsx3
import datetime
import time as t
import numpy as np
import alert

class Person_recording:
    def sound(self) -> None:
        voice = pyttsx3.init()
        voice.say("Detection is on")
        voice.runAndWait()
    
    def __init__(self) -> None:
        print('day vision camera is start')
        
        video = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")
  
        length = int(video.get(3)), int(video.get(4))        #getting weight and height
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        # recording = cv2.VideoWriter("video90.mp4", fourcc, 20, length)
        detection = False
        detection_stop = None
        timer_started = False
        SECONDS_TO_RECORD_AFTER_DETECTION = 5
        a=0



        while True:
            ret, frame = video.read()

            grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            face = face_cascade.detectMultiScale(grey, 1.3, 3)
            body = body_cascade.detectMultiScale(grey, 1.3, 3)
            
            time = str(datetime.datetime.now())
            font = cv2.FONT_HERSHEY_SIMPLEX
            put_lint = cv2.putText(frame, time, (3,20), font, 0.60, (0,0,0), 2, cv2.LINE_AA )

            
            for a,b,c,d in face:
                cv2.rectangle(frame, (a,b), (a+c,b+d), (255,0,0),7)
            for a,b,c,d in body:
                cv2.rectangle(frame, (a,b),(a+c, b+d), (0,0,0),7)
            # recording.write(frame)  
            if len(face) + len(body) > 0:
                if detection:
                    timer_started = False
                else:
                    detection = True
                    a=2
                    current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                    out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 20, length)
                    print("start recording")

            elif detection:
                if timer_started:
                    if t.time()-detection_stop >= SECONDS_TO_RECORD_AFTER_DETECTION:
                        detection = False
                        timer_started = False
                        out.release()
                        print("stop recording")
                
                else:
                    timer_started = True
                    detection_stop = t.time()
            # out.write()
            if detection:
                out.write(frame)

   

            cv2.imshow('frame', frame)

            if cv2.waitKey(1)==ord('q'):
                break
        
        # recording.release()
        if a == 2:
            a=alert.Alert("kinglucifer514@gmail.com")
            a.start()

        video.release()
        cv2.destroyAllWindows()
    
    def soundOff(self) -> None:
        voice = pyttsx3.init()
        voice.say("stoping the detection.")
        voice.runAndWait()


if __name__=="__main__":
    a = Person_recording()


