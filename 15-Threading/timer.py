import logging
import threading

# Set logger to just use threadname
logging.basicConfig(
    level=logging.INFO,
    format='%(threadName)s: %(message)s')

log = logging.getLogger()

def hello(x):
    log.info('Hello, %s', x)

t = threading.Timer(5.0, hello, ('World',))
t.start()
log.info('Main program complete')
