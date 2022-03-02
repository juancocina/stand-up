import schedule
import time
import os


def notify():
    os.system("""
        osascript -e 'display notification "{}" with title "{}"'
        osascript -e 'beep 3'
        """.format("Stand Up", "Stretch a little bit, drink water"))

schedule.every().hour.do(notify)

while True:
    schedule.run_pending()
    time.sleep(1)