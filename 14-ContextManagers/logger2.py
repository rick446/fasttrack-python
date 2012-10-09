import logging
from contextlib import contextmanager

logging.basicConfig()

@contextmanager
def log_block(logger, level=logging.INFO):
    logger.log(level, 'Enter')
    try:
        yield
    except:
        logger.log(level, 'Exit (with exception)')
    else:
        logger.log(level, 'Exit (no exception)')


print 'This is before the with statement'

with log_block(logging.getLogger('mylogger'), logging.ERROR):
    print 'Now inside the block'
    print 'still inside block'
    
with log_block(logging.getLogger('mylogger'), logging.ERROR):
    print 'Now inside the 2nd block'
    print 'still inside 2nd block'
    raise ValueError
