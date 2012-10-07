import time
import threading

def print_time():
    while True:
        print time.ctime()
        time.sleep(1)


t = threading.Thread(target=print_time)
t.setDaemon(True)
t.start()

time.sleep(10)
