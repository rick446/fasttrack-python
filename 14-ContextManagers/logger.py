import logging

logging.basicConfig()

class log_block(object):

    def __init__(self, logger, level=logging.INFO):
        self._logger = logger
        self._level = level

    def __enter__(self):
        self._logger.log(self._level, 'Enter')

    def __exit__(self, ex_type, ex_value, ex_tb):
        if ex_type is None:
            self._logger.log(self._level, 'Exit (no exception)')
        else:
            self._logger.log(self._level, 'Exit (with exception %s)', ex_type)
            return True

print 'This is before the with statement'

with log_block(logging.getLogger('mylogger'), logging.ERROR):
    print 'Now inside the block'
    print 'still inside block'
    
with log_block(logging.getLogger('mylogger'), logging.ERROR):
    print 'Now inside the 2nd block'
    print 'still inside 2nd block'
    raise ValueError

def log_decorator(logger, level=logging.INFO):
    '''Just for fun'''
    def decorator(function):
        def wrapper(*args, **kwargs):
            with log_block(logger, level):
                return function(*args, **kwargs)
        return wrapper
    return decorator
