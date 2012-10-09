import math
import logging
from multiprocessing import Process, Value, Array

logging.basicConfig(level=logging.INFO)

log = logging.getLogger()

def main():
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    log.info('Before process, num.value = %s', num.value)
    log.info('Before process, arr = %s', list(arr))

    p = Process(target=target, args=(num, arr))
    p.start()
    p.join()

    log.info('After process, num.value = %s', num.value)
    log.info('After process, arr = %s', list(arr))

def target(num, arr):
    log.info('Running target function')
    num.value = math.pi
    for i, aval in enumerate(arr):
        arr[i] = -aval
    
if __name__ == '__main__':
    main()
