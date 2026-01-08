import time
from datetime import datetime
from auto_exit import square_off_all

def auto_exit_loop():
    while True:
        if datetime.now().strftime("%H:%M") >= "15:15":
            square_off_all()
            break
        time.sleep(30)
