from datetime import datetime
def beat():
    open("logs/heartbeat.log","a").write(str(datetime.now())+"\n")
