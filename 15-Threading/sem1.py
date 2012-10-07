import time
import logging
import threading

# Set logger to just use threadname
logging.basicConfig(
    level=logging.INFO,
    format='%(threadName)s: %(message)s')

log = logging.getLogger()

sem = threading.Semaphore(4)

def thread_target(y):
    with sem:
        log.info('Enter')
        time.sleep(1)
        log.info('Exit')

threads = [ threading.Thread(target=thread_target, args=(4,))
            for x in range(10) ]

for i, t in enumerate(threads):
    t.start()
