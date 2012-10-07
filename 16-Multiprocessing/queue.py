import time
import logging
from multiprocessing import Queue, Process

logging.basicConfig(
    level=logging.INFO,
    format='%(processName)s: %(message)s')

log = logging.getLogger()

q = Queue()

def producer():
    for x in range(10):
        time.sleep(0.5)
        log.info('>>> %s', x)
        q.put(x)

def consumer():
    while True:
        x = q.get()
        log.info('<<< %s', x)

p_producer = Process(target=producer)
p_consumer = Process(target=consumer)

p_producer.start()
time.sleep(2)
p_consumer.start()
p_producer.join()
time.sleep(0)
p_consumer.terminate()
