import logging
import threading

# Set logger to just use threadname
logging.basicConfig(
    level=logging.INFO,
    format='%(threadName)s: %(message)s')

log = logging.getLogger()

lock = threading.Lock()

def thread_target(y):
    lock.acquire()
    log.info('Enter')
    for item in range(y):
        log.info('%s', item)
    log.info('Exit')
    lock.release()

threads = [ threading.Thread(target=thread_target, args=(4,))
            for x in range(4) ]

log.info('Starting threads')
for i, t in enumerate(threads):
    log.info('Starting thread %d', i)
    t.start()
log.info('All threads started')
