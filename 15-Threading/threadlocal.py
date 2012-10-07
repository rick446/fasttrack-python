import logging
import threading

logging.basicConfig(
    level=logging.INFO,
    format='%(threadName)s: %(message)s')

thread_local = threading.local()
thread_local.name = 'Set in main thread'

log = logging.getLogger()

def target():
    thread_local.name = 'Set in target thread'
    log.info('thread_local.name = %s', thread_local.name)

log.info('thread_local.name = %s', thread_local.name)
t = threading.Thread(target=target)
t.start()
t.join()
log.info('thread_local.name = %s', thread_local.name)
