import time
import logging
import multiprocessing

logging.basicConfig(
    level=logging.INFO,
    format='%(processName)s (%(process)s): %(message)s')

log = logging.getLogger()

def main():
    procs = [ multiprocessing.Process(target=target, args=(x, 4))
                for x in range(4) ]
    log.info('Starting procs')
    for i, p in enumerate(procs):
        log.info('Starting process %d', i)
        p.start()
        p.join()
    log.info('All procs started')

def target(x, y):
    log.info('Enter')
    for item in range(y):
        time.sleep(0.1)
        log.info('(%s,%s)', x, item)
    log.info('Exit')

if __name__ == '__main__':
    main()
