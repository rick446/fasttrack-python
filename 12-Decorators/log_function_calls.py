import logging

logging.basicConfig()

class log_call(object):

    def __init__(self, logger, level=logging.INFO):
        self._logger = logger
        self._level = level

    def __call__(self, function):
        def wrapper(*args, **kwargs):
            self._logger.log(
                self._level, 'Enter %s(*%r, **%r)', function, args, kwargs)
            result = function(*args, **kwargs)
            self._logger.log(
                self._level, 'Exit %s => %r', function, result)
            return result
        return wrapper
            
@log_call(logging.getLogger('mylogger'), logging.ERROR)
def will_log_to_error(a, b):
    return a + b

print will_log_to_error(1, 2)
