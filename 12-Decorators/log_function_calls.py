import logging

logging.basicConfig()

class log_call(object):

    def __init__(self, logger, level=logging.INFO):
        self._logger = logger
        self._level = level

    def __call__(self, function):
        def wrapper(*args, **kwargs):
            self._logger.log(
                self._level, 'Enter %s(*%r, **%r)',
                function, args, kwargs)
            result = function(*args, **kwargs)
            self._logger.log(
                self._level, 'Exit %s => %r', function, result)
            return result
        return wrapper

def log_call_alt(logger, level=logging.INFO):
    def decorator(function):
        def wrapper(*args, **kwargs):
            logger.log(
                level, 'Enter %s(*%r, **%r)',
                function, args, kwargs)
            result = function(*args, **kwargs)
            logger.log(
                level, 'Exit %s => %r', function, result)
            return result
        return wrapper
    return decorator
            
@log_call(logging.getLogger('mylogger'), logging.ERROR)
def will_log_to_error(a, b):
    return a + b

@log_call_alt(logging.getLogger('mylogger'), logging.ERROR)
def will_log_to_error_2(a, b):
    return a + b

print will_log_to_error(1, 2)
print will_log_to_error_2(3, 4)
