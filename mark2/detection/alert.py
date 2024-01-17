import smtplib
from email.message import EmailMessage

class Alert:
    def __init__(self,to) -> None:
        self.subject = "An alert message related to your station."
        self.body = '''An unusual activity is detected in your station so you would check it as fast as possible.
        THANK YOU
        DEBUGGING DYNAMOS'''
        self.to = to
    
    def start(self):
        msg = EmailMessage()
        msg.set_content(self.body)
        msg["subject"] = self.subject
        msg["to"] = self.to

        user = "debuggingdynamos@gmail.com"
        msg["from"] = user
        password = "mgwupqvkaoakfmjc"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, password)
        server.send_message(msg)
        server.quit()

if __name__=="__main__":
    A = Alert("kushaljohari28@gmail.com")
    A.start()