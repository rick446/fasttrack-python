import sys
import threading

log_mutex = threading.Lock()

def log(message):
    with log_mutex:
        slow_log(message)

def slow_log(message):
    for ch in message:
        sys.stdout.write(ch)
        sys.stdout.flush()
    sys.stdout.write('\n')
    sys.stdout.flush()

def target(x):
    for y in range(4):
        log('(x,y) is (%d, %d)' % (x,y))

threads = [ threading.Thread(target=target, args=(x,))
            for x in range(4) ]

for t in threads:
    t.start()
