import time
import logging
import multiprocessing

# Set logger to just use threadname
logging.basicConfig(
    level=logging.INFO,
    format='%(processName)s: %(message)s')

log = logging.getLogger()

lock = multiprocessing.Lock()

def target(y):
    with lock:
        log.info('Enter')
        for item in range(y):
            time.sleep(0.1)
            log.info('%s', item)
        log.info('Exit')

procs = [ multiprocessing.Process(target=target, args=(4,))
            for x in range(4) ]

log.info('Starting procs')
for i, t in enumerate(procs):
    log.info('Starting proc %d', i)
    t.start()
log.info('All procs started')
