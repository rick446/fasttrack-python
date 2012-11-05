import time
import Queue
import logging
import threading

logging.basicConfig(
    level=logging.INFO,
    format='%(threadName)s: %(message)s')

log = logging.getLogger()

q = Queue.Queue()

def producer():
    for x in range(10):
        time.sleep(0.5)
        log.info('>>> %s', x)
        q.put(x)

def consumer():
    while True:
        x = q.get()
        log.info('<<< %s', x)

t_producer = threading.Thread(target=producer)
t_consumer = threading.Thread(target=consumer)
t_consumer.setDaemon(True)

t_producer.start()
time.sleep(2)
t_consumer.start()
