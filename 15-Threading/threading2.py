import logging
import threading

logging.basicConfig(
    level=logging.INFO)

log = logging.getLogger('main')

def thread_target(x, y):
    log = logging.getLogger('thread-%d' % x)
    log.info('Enter')
    for item in range(y):
        log.info('%s', item)
    log.info('Exit')

threads = [ threading.Thread(target=thread_target, args=(x, 4))
            for x in range(4) ]

log.info('Starting threads')
for i, t in enumerate(threads):
    log.info('Starting thread %d', i)
    t.start()
    # Wait for thread to complete
    t.join()
    log.info('Joined thread %d', i)
log.info('All threads started')
