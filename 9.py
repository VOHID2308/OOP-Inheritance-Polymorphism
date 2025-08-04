class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        return "Sending email..."

class SMSNotification(Notification):
    def send(self):
        return "Sending SMS..."

notifications = [EmailNotification(), SMSNotification()]
for n in notifications:
    print(n.send())