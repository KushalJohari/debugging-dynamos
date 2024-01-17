import night_camera
import day_detection
from datetime import datetime
current_time=datetime.now()
def ALLcapture():
    if datetime.time(7,0)<=current_time and datetime.time(20,0)>=current_time:
        a = day_detection()

    else:
        b = night_camera()


# ALLcapture()
import alert
a=alert.Alert("kinglucifer514@gmail.com")
a.start()