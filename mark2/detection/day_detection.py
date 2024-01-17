import cv2
import cvzone
from ultralytics import YOLO
import alert
import math

cap = cv2.VideoCapture(0)
cap.set(3, 200)
cap.set(4, 200)
model = YOLO("camdect.pt")

while True:
    _, frame = cap.read()
    result = model(frame, stream=True)
    for i in result:
        boxes = i.boxes
        for j in boxes:
            x1, y1, x2, y2 = j.xyxy[0]
            x1, y1, x2, y2= int(x1), int(y1), int(x2), int(y2)
            # ==== bounding box
            # x1, y1, w, h = j.xywh[0]
            # bbox = int(x1), int(y1), int(w), int(h)
            w, h = x2-x1, y2-y1
            # print(x1, y1, w, h)
            # cv2.rectangle(frame, (x1, y1), (x2,y2),(255,0,0), 3)
            cvzone.cornerRect(frame, (x1, y1, w, h))
# ==================================================================================
            conf =math.ceil((j.conf[0]*100))/100
            # cvzone.putTextRect(frame, f"{conf}", (max(0, x1), max(35, y1)), scale=1 , thickness=1)
            # cls = int(j.cls[0])
    if conf>=0.70:
        print("Yes")
        a=alert.Alert("kushaljohari28@gmail.com")
        a.start()
        break

           
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1)==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()