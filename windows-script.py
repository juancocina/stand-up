import time
import schedule
from win10toast import ToastNotifier

def notify():
    toaster = ToastNotifier()
    toaster.show_toast("Stand up",
                       "Remember to stretch and drink water",
                       icon_path=None,
                       duration=10)

schedule.every().hour.at(":45").do(notify)

while True:
    schedule.run_pending()
    time.sleep(1)






