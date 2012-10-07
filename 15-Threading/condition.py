import time
import logging
import threading

thread_to_run = None

# Set logger to just use threadname
logging.basicConfig(
    level=logging.INFO,
    format='%(threadName)s: %(message)s')

log = logging.getLogger()

cond = threading.Condition()

def worker(y):
    global thread_to_run
    with cond:
        while thread_to_run != y:
            cond.wait()
        log.info('Running thread %d', y)
        time.sleep(0.5)
        log.info('Now done')
        thread_to_run = None
        cond.notify_all()

def coordinator(num_threads):
    global thread_to_run
    for x in range(num_threads):
        with cond:
            while thread_to_run is not None:
                cond.wait()
            thread_to_run = x
            cond.notify_all()

workers = [ threading.Thread(target=worker, args=(x,))
            for x in range(10) ]
for t in workers: t.start()

coordinator(10)
