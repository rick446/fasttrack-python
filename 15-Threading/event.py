import logging
import threading

# Set logger to just use threadname
logging.basicConfig(
    level=logging.INFO,
    format='%(threadName)s: %(message)s')

log = logging.getLogger()

ev = threading.Event()

def timer():
    log.info('Timer running')
    ev.set()

def target():
    log.info('Target waiting')
    ev.wait()
    log.info('Target running')
    ev.clear()

t1 = threading.Thread(target=target)
t1.start()

t2 = threading.Timer(3, timer)
t2.start()
