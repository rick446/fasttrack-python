import logging
import threading

# Set logger to just use threadname
logging.basicConfig(
    level=logging.INFO,
    format='%(threadName)s: %(message)s')

log = logging.getLogger()

def thread_target(x, y):
    log.info('Enter')
    for item in range(y):
        log.info('%s', item)
    log.info('Exit')

threads = [ threading.Thread(target=thread_target, args=(x,4))
            for x in range(4) ]

log.info('Daemonizing threads')
for i, t in enumerate(threads):
    t.setDaemon(True)

log.info('Starting threads')
for i, t in enumerate(threads):
    log.info('Starting thread %d', i)
    t.start()
log.info('All threads started')
